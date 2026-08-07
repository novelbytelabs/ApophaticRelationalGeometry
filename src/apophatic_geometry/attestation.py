"""Fail-closed source, runtime, and execution attestation utilities.

No caller-supplied environment variable is accepted as provenance. Scientific
artifacts derive identity from a clean Git checkout, tracked source bytes, the
frozen protocol lock, declared implementation files, and installed runtime
files.
"""

from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import importlib
import importlib.metadata
import io
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
from typing import Any, Iterable, Mapping

import numpy as np

from .protocol import canonical_json_sha256, file_sha256, load_json

_COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


class AttestationError(RuntimeError):
    """Raised when execution provenance cannot be established fail closed."""


def _run_git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def _require_repo_root(repo_root: str | Path) -> Path:
    root = Path(repo_root).resolve(strict=True)
    result = _run_git(root, "rev-parse", "--show-toplevel")
    if result.returncode != 0:
        raise AttestationError("attestation requires a Git checkout")
    top = Path(result.stdout.strip()).resolve(strict=True)
    if top != root:
        raise AttestationError("repo_root must be the Git checkout root")
    return root


def require_clean_tracked_tree(repo_root: str | Path) -> tuple[Path, str]:
    """Return ``(root, commit)`` for a clean tracked checkout.

    Modified, deleted, staged, conflicted, or untracked files fail. This closes
    import-shadowing paths in which an untracked module could affect execution
    without entering the tracked-tree digest.
    """

    root = _require_repo_root(repo_root)
    status = _run_git(root, "status", "--porcelain", "--untracked-files=all")
    if status.returncode != 0 or status.stdout.strip():
        raise AttestationError("attested execution requires a completely clean tree, including no untracked files")
    head = _run_git(root, "rev-parse", "HEAD")
    commit = head.stdout.strip()
    if head.returncode != 0 or _COMMIT_RE.fullmatch(commit) is None:
        raise AttestationError("unable to derive a canonical 40-character source commit")
    return root, commit


def _root_confined_file(root: Path, relative: str) -> Path:
    source_path = root / relative
    if source_path.is_symlink():
        raise AttestationError(f"tracked source must not be a symlink: {relative}")
    candidate = source_path.resolve(strict=True)
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise AttestationError(f"tracked path escapes repository root: {relative}") from exc
    if not candidate.is_file():
        raise AttestationError(f"tracked source must be a regular file: {relative}")
    return candidate


def tracked_source_sha256(repo_root: str | Path) -> str:
    """Hash every tracked regular file with path and length framing."""

    root = _require_repo_root(repo_root)
    listed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=False,
        capture_output=True,
    )
    if listed.returncode != 0:
        raise AttestationError("unable to enumerate tracked source files")
    relative_paths = [
        item.decode("utf-8", errors="strict")
        for item in listed.stdout.split(b"\0")
        if item
    ]
    if not relative_paths:
        raise AttestationError("tracked source set is empty")

    digest = hashlib.sha256()
    for relative in sorted(relative_paths):
        path = _root_confined_file(root, relative)
        path_bytes = relative.encode("utf-8")
        content = path.read_bytes()
        digest.update(len(path_bytes).to_bytes(8, "big"))
        digest.update(path_bytes)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest()


def distribution_tree_sha256(name: str) -> str:
    """Hash installed files declared by one Python distribution."""

    try:
        distribution = importlib.metadata.distribution(name)
    except importlib.metadata.PackageNotFoundError as exc:
        raise AttestationError(f"required distribution is unavailable: {name}") from exc
    files = distribution.files
    if not files:
        raise AttestationError(
            f"distribution does not expose an installed-file manifest: {name}"
        )

    digest = hashlib.sha256()
    file_count = 0
    for entry in sorted(files, key=lambda value: str(value)):
        path = Path(distribution.locate_file(entry))
        if not path.is_file():
            continue
        relative = str(entry).replace("\\", "/")
        path_bytes = relative.encode("utf-8")
        content = path.read_bytes()
        digest.update(len(path_bytes).to_bytes(8, "big"))
        digest.update(path_bytes)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
        file_count += 1
    if file_count == 0:
        raise AttestationError(f"distribution has no hashable installed files: {name}")
    return digest.hexdigest()


def runtime_environment() -> dict[str, Any]:
    """Return versions and installed-byte fingerprints for runtime dependencies."""

    stream = io.StringIO()
    with redirect_stdout(stream):
        np.show_config()
    module_names = {
        "apophatic-relational-geometry": "apophatic_geometry",
        "numpy": "numpy",
        "scipy": "scipy",
    }
    distributions: dict[str, dict[str, str]] = {}
    for name, module_name in module_names.items():
        distribution = importlib.metadata.distribution(name)
        module = importlib.import_module(module_name)
        raw_module_file = getattr(module, "__file__", None)
        if not raw_module_file:
            raise AttestationError(f"imported module has no file identity: {module_name}")
        module_file = Path(raw_module_file).resolve(strict=True)
        distribution_root = Path(distribution.locate_file("")).resolve(strict=True)
        distributions[name] = {
            "version": importlib.metadata.version(name),
            "installed_tree_sha256": distribution_tree_sha256(name),
            "module_name": module_name,
            "module_file": str(module_file),
            "distribution_root": str(distribution_root),
        }
    numpy_configuration = stream.getvalue()
    if not numpy_configuration.strip():
        raise AttestationError("NumPy configuration identity is empty")
    return {
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "python_build": list(platform.python_build()),
        "python_executable_sha256": file_sha256(
            Path(sys.executable).resolve(strict=True)
        ),
        "operating_system": platform.system(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "numpy_configuration": numpy_configuration,
        "numpy_configuration_sha256": hashlib.sha256(
            numpy_configuration.encode("utf-8")
        ).hexdigest(),
        "distributions": distributions,
    }


def protocol_lock_attestation(repo_root: str | Path) -> dict[str, str]:
    root = _require_repo_root(repo_root)
    path = root / "protocol" / "phase5_v1" / "LOCK.json"
    manifest = load_json(path)
    if not isinstance(manifest, Mapping):
        raise AttestationError("protocol lock is not a JSON object")
    return {
        "path": str(path.relative_to(root)),
        "file_sha256": file_sha256(path),
        "canonical_sha256": canonical_json_sha256(manifest),
        "lock_id": str(manifest.get("lock_id", "")),
    }


def implementation_hashes(
    repo_root: str | Path,
    relative_paths: Iterable[str],
) -> dict[str, str]:
    root = _require_repo_root(repo_root)
    hashes: dict[str, str] = {}
    for relative in sorted(set(relative_paths)):
        path = _root_confined_file(root, relative)
        hashes[relative] = file_sha256(path)
    if not hashes:
        raise AttestationError("implementation hash set is empty")
    return hashes


def build_attestation(
    repo_root: str | Path,
    *,
    integrator: str,
    implementation_paths: Iterable[str],
) -> dict[str, Any]:
    """Construct a complete attestation derived from the execution substrate."""

    if not integrator:
        raise ValueError("integrator identifier is required")
    root, source_commit = require_clean_tracked_tree(repo_root)
    environment = runtime_environment()
    attestation = {
        "attestation_version": "ARG-ATTEST-v1",
        "artifact_kind": "clean_git_checkout",
        "source_commit": source_commit,
        "source_tree_sha256": tracked_source_sha256(root),
        "protocol_lock": protocol_lock_attestation(root),
        "integrator": integrator,
        "implementation_files": implementation_hashes(root, implementation_paths),
        "runtime_environment": environment,
        "runtime_environment_sha256": canonical_json_sha256(environment),
    }
    attestation["attestation_sha256"] = canonical_json_sha256(attestation)
    return attestation


def write_canonical_json_bytes(value: Any) -> bytes:
    """Serialize strict canonical JSON with one terminating newline."""

    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")

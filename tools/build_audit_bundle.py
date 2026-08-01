#!/usr/bin/env python3
"""Build a self-validating ARG audit bundle without trajectory data.

The builder uses committed Git content only. It runs the advertised tests and
data-free validation in a fresh clone reconstructed from the included Git
bundle, creates the manifest only after those checks pass, packages the result,
then extracts and verifies the final archive before atomically publishing it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
from typing import Any, Iterable, Mapping

AUDIT_FORMAT = "ARG-AUDIT-BUNDLE-v2"
FORBIDDEN_TRACKED_PATHS = {
    "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json",
}
FORBIDDEN_TRACKED_SUFFIXES = ("run.csv",)


class AuditBundleError(RuntimeError):
    """Raised when an audit bundle cannot attest its own construction."""


def _run(
    args: list[str],
    *,
    cwd: Path,
    env: Mapping[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        args,
        cwd=cwd,
        env=None if env is None else dict(env),
        text=True,
        capture_output=True,
        check=False,
    )
    return result


def _require_success(result: subprocess.CompletedProcess[str], label: str) -> str:
    if result.returncode != 0:
        raise AuditBundleError(
            f"{label} failed with exit {result.returncode}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result.stdout


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _canonical_json_bytes(value: Any) -> bytes:
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


def _write_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())


def _git_root(repo_root: Path) -> tuple[Path, str]:
    root = repo_root.resolve(strict=True)
    top = _run(["git", "rev-parse", "--show-toplevel"], cwd=root)
    _require_success(top, "Git root resolution")
    actual = Path(top.stdout.strip()).resolve(strict=True)
    if actual != root:
        raise AuditBundleError("--repo-root must be the Git checkout root")
    dirty = _run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=root,
    )
    _require_success(dirty, "Git status")
    if dirty.stdout.strip():
        raise AuditBundleError("audit bundle requires a clean tracked tree")
    head = _run(["git", "rev-parse", "HEAD"], cwd=root)
    commit = _require_success(head, "Git HEAD resolution").strip()
    if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit):
        raise AuditBundleError("source commit is not canonical lowercase SHA-1 text")
    return root, commit


def _tracked_paths(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise AuditBundleError("unable to enumerate tracked files")
    paths = [
        item.decode("utf-8", errors="strict")
        for item in result.stdout.split(b"\0")
        if item
    ]
    if not paths:
        raise AuditBundleError("tracked source set is empty")
    return sorted(paths)


def _reject_forbidden_content(root: Path, tracked: Iterable[str]) -> None:
    tracked_set = set(tracked)
    forbidden = sorted(FORBIDDEN_TRACKED_PATHS.intersection(tracked_set))
    if forbidden:
        raise AuditBundleError(
            "execution authorization is forbidden in an audit-only bundle: "
            + ", ".join(forbidden)
        )
    stale = sorted(
        path
        for path in tracked_set
        if any(path.endswith(suffix) for suffix in FORBIDDEN_TRACKED_SUFFIXES)
    )
    if stale:
        raise AuditBundleError(
            "legacy or unclassified generated output is forbidden: "
            + ", ".join(stale)
        )
    if (root / "artifacts" / "phase6_pilot").exists():
        raise AuditBundleError("pilot artifact directory is forbidden")


def _safe_extract_tar(archive: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    resolved_destination = destination.resolve(strict=True)
    with tarfile.open(archive, "r:*") as handle:
        members = handle.getmembers()
        for member in members:
            target = (resolved_destination / member.name).resolve()
            try:
                target.relative_to(resolved_destination)
            except ValueError as exc:
                raise AuditBundleError(
                    f"archive member escapes destination: {member.name}"
                ) from exc
            if member.issym() or member.islnk():
                raise AuditBundleError(
                    f"archive symlink/hardlink is not permitted: {member.name}"
                )
        handle.extractall(resolved_destination)


def _snapshot_source(root: Path, destination: Path) -> None:
    tar_path = destination.parent / "source.tar"
    result = _run(
        ["git", "archive", "--format=tar", "-o", str(tar_path), "HEAD"],
        cwd=root,
    )
    _require_success(result, "Git source archive")
    _safe_extract_tar(tar_path, destination)
    tar_path.unlink()


def _create_git_bundle(root: Path, destination: Path) -> None:
    result = _run(
        ["git", "bundle", "create", str(destination), "HEAD"],
        cwd=root,
    )
    _require_success(result, "Git history bundle")
    verify = _run(["git", "bundle", "verify", str(destination)], cwd=root)
    _require_success(verify, "Git history bundle verification")


def _clone_bundle(bundle: Path, destination: Path, commit: str) -> None:
    result = _run(
        ["git", "clone", "--no-checkout", str(bundle), str(destination)],
        cwd=bundle.parent,
    )
    _require_success(result, "Audit clone")
    checkout = _run(["git", "checkout", "--detach", commit], cwd=destination)
    _require_success(checkout, "Audit checkout")
    resolved = _run(["git", "rev-parse", "HEAD"], cwd=destination)
    if _require_success(resolved, "Audit clone HEAD").strip() != commit:
        raise AuditBundleError("audit clone resolved the wrong source commit")


def _test_environment(clone: Path) -> dict[str, str]:
    environment = dict(os.environ)
    environment.pop("ARG_SOURCE_COMMIT", None)
    environment["PYTHONPATH"] = str(clone / "src")
    return environment


def _run_self_tests(clone: Path) -> dict[str, Any]:
    environment = _test_environment(clone)
    commands = {
        "pytest": [sys.executable, "-m", "pytest"],
        "pilot_validate": [
            sys.executable,
            "-m",
            "apophatic_geometry.pilot_cli",
            "validate",
            "--repo-root",
            str(clone),
        ],
        "pilot_plan": [
            sys.executable,
            "-m",
            "apophatic_geometry.pilot_cli",
            "plan",
            "--repo-root",
            str(clone),
        ],
    }
    records: dict[str, Any] = {}
    for name, command in commands.items():
        result = _run(command, cwd=clone, env=environment)
        _require_success(result, name)
        records[name] = {
            "command": command,
            "returncode": result.returncode,
            "stdout_sha256": _sha256_bytes(result.stdout.encode("utf-8")),
            "stderr_sha256": _sha256_bytes(result.stderr.encode("utf-8")),
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    plan = json.loads(records["pilot_plan"]["stdout"])
    if plan.get("configuration_count") != 50:
        raise AuditBundleError("pilot plan does not contain exactly 50 configurations")
    if plan.get("confirmatory_execution") != "BLOCKED":
        raise AuditBundleError("pilot plan does not block confirmatory execution")
    return records


def _build_wheel(clone: Path, destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)
    result = _run(
        [
            sys.executable,
            "-m",
            "pip",
            "wheel",
            "--no-deps",
            "--no-build-isolation",
            "--wheel-dir",
            str(destination),
            ".",
        ],
        cwd=clone,
    )
    _require_success(result, "Wheel build")
    wheels = sorted(destination.glob("*.whl"))
    if len(wheels) != 1:
        raise AuditBundleError(f"expected one wheel, found {len(wheels)}")
    return wheels[0]


def _file_manifest(root: Path, *, exclude: set[str] | None = None) -> dict[str, str]:
    excluded = exclude or set()
    manifest: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = str(path.relative_to(root)).replace("\\", "/")
        if relative in excluded:
            continue
        manifest[relative] = _sha256_file(path)
    return manifest


def _verify_file_manifest(root: Path, manifest: Mapping[str, str]) -> None:
    actual = _file_manifest(root, exclude={"AUDIT_MANIFEST.json"})
    if actual != dict(manifest):
        missing = sorted(set(manifest).difference(actual))
        unexpected = sorted(set(actual).difference(manifest))
        changed = sorted(
            path
            for path in set(actual).intersection(manifest)
            if actual[path] != manifest[path]
        )
        raise AuditBundleError(
            "audit file manifest mismatch; "
            f"missing={missing}, unexpected={unexpected}, changed={changed}"
        )


def _package_directory(source: Path, archive: Path) -> None:
    with tarfile.open(archive, "w:gz", format=tarfile.PAX_FORMAT) as handle:
        for path in sorted(source.rglob("*")):
            arcname = Path("arg-audit-bundle") / path.relative_to(source)
            handle.add(path, arcname=str(arcname), recursive=False)


def _verify_final_archive(archive: Path, expected_commit: str) -> None:
    with tempfile.TemporaryDirectory(prefix="arg-audit-final-") as raw:
        root = Path(raw)
        _safe_extract_tar(archive, root)
        package = root / "arg-audit-bundle"
        manifest_path = package / "AUDIT_MANIFEST.json"
        if not manifest_path.is_file():
            raise AuditBundleError("final archive lacks AUDIT_MANIFEST.json")
        manifest = json.loads(
            manifest_path.read_text(encoding="utf-8"),
            parse_constant=lambda token: (_ for _ in ()).throw(
                ValueError(f"non-standard JSON constant: {token}")
            ),
        )
        if manifest.get("source_commit") != expected_commit:
            raise AuditBundleError("final archive source commit mismatch")
        _verify_file_manifest(package, manifest["files"])
        clone = root / "final-clone"
        _clone_bundle(package / "repository.bundle", clone, expected_commit)
        _run_self_tests(clone)


def build_bundle(repo_root: Path, output: Path) -> Path:
    root, commit = _git_root(repo_root)
    tracked = _tracked_paths(root)
    _reject_forbidden_content(root, tracked)
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"output already exists: {output}")
    if root == output or root in output.parents:
        raise AuditBundleError("audit output must be outside the repository")
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(
        prefix="arg-audit-build-", dir=output.parent
    ) as raw:
        work = Path(raw)
        package = work / "package"
        source = package / "source"
        wheels = package / "wheel"
        package.mkdir()
        _snapshot_source(root, source)
        bundle_path = package / "repository.bundle"
        _create_git_bundle(root, bundle_path)

        verification_clone = work / "verification-clone"
        _clone_bundle(bundle_path, verification_clone, commit)
        records = _run_self_tests(verification_clone)
        wheel = _build_wheel(verification_clone, wheels)

        file_manifest = _file_manifest(package)
        manifest = {
            "audit_format": AUDIT_FORMAT,
            "status": "SELF_TESTED_NO_TRAJECTORY_DATA",
            "source_commit": commit,
            "source_snapshot_file_count": len(
                [path for path in source.rglob("*") if path.is_file()]
            ),
            "repository_bundle_sha256": _sha256_file(bundle_path),
            "wheel": {
                "name": wheel.name,
                "sha256": _sha256_file(wheel),
            },
            "advertised_test": {
                "command": records["pytest"]["command"],
                "returncode": 0,
                "stdout_sha256": records["pytest"]["stdout_sha256"],
                "stderr_sha256": records["pytest"]["stderr_sha256"],
            },
            "data_free_validation": {
                "pilot_validate_stdout_sha256": records["pilot_validate"][
                    "stdout_sha256"
                ],
                "pilot_plan_stdout_sha256": records["pilot_plan"][
                    "stdout_sha256"
                ],
                "pilot_configuration_count": 50,
                "confirmatory_execution": "BLOCKED",
            },
            "forbidden_content": {
                "execution_authorization": False,
                "pilot_trajectory": False,
                "confirmatory_trajectory": False,
                "legacy_run_csv": False,
            },
            "files": file_manifest,
        }
        _write_bytes(
            package / "AUDIT_MANIFEST.json",
            _canonical_json_bytes(manifest),
        )

        temporary_archive = work / "bundle.tar.gz"
        _package_directory(package, temporary_archive)
        _verify_final_archive(temporary_archive, commit)
        os.replace(temporary_archive, output)
        directory_descriptor = os.open(output.parent, os.O_RDONLY)
        try:
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build_bundle(args.repo_root, args.output)
    print(result)


if __name__ == "__main__":
    main()

"""Write-once archive and confirmatory-contamination checks for Phase 6."""

from __future__ import annotations

import json
from pathlib import Path
import stat
from typing import Any, Iterable, Mapping

import numpy as np

from .models import CONTRACT_VERSION
from .pilot_types import (
    PILOT_SPLIT,
    SMOKE_SPLIT,
    RUNNER_ID,
    RUNNER_VERSION,
    ArchiveWriteResult,
    ConfirmatoryAccessError,
    PilotConfiguration,
    Trajectory,
)
from .protocol import PROTOCOL_ID, PROTOCOL_VERSION, file_sha256, load_json


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


def _write_new_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(content)


def _write_new_json(path: Path, value: Any) -> None:
    _write_new_bytes(path, _canonical_json_bytes(value))


def _write_new_npy(path: Path, value: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        np.save(handle, np.asarray(value, dtype=np.float64), allow_pickle=False)


class PilotArchiveWriter:
    """Write-once archive builder with deterministic files and final checksums."""

    def __init__(self, root: str | Path, run_manifest: Mapping[str, Any]) -> None:
        if run_manifest.get("runner_id") != RUNNER_ID:
            raise ValueError("run manifest has wrong runner_id")
        if run_manifest.get("split") != PILOT_SPLIT:
            raise ConfirmatoryAccessError("run manifest must be pilot-only")
        if run_manifest.get("confirmatory_execution") != "BLOCKED":
            raise ConfirmatoryAccessError("run manifest must block confirmatory execution")
        self.root = Path(root).resolve()
        if self.root.exists() and any(self.root.iterdir()):
            raise FileExistsError("pilot archive directory must not already contain files")
        self.root.mkdir(parents=True, exist_ok=True)
        for name in ("environment", "configs", "raw", "summaries"):
            (self.root / name).mkdir(exist_ok=False)
        _write_new_json(self.root / "RUN_MANIFEST.json", run_manifest)
        _write_new_bytes(self.root / "failures.jsonl", b"")
        self._finalized = False

    def write_environment(self, environment: Mapping[str, Any]) -> str:
        path = self.root / "environment" / "runtime.json"
        _write_new_json(path, environment)
        return file_sha256(path)

    def write_configuration(self, configuration: PilotConfiguration) -> str:
        if configuration.split != PILOT_SPLIT:
            raise ConfirmatoryAccessError("only pilot configurations may enter the archive")
        path = self.root / "configs" / f"{configuration.config_id}.json"
        payload = configuration.canonical_payload() | {
            "configuration_hash": configuration.configuration_hash
        }
        _write_new_json(path, payload)
        return file_sha256(path)

    def write_trajectory(self, trajectory: Trajectory) -> ArchiveWriteResult:
        if trajectory.split != PILOT_SPLIT:
            raise ConfirmatoryAccessError("only pilot trajectories may enter the archive")
        relative = Path(
            "raw",
            trajectory.config_id,
            trajectory.model_id,
            trajectory.profile,
            trajectory.control_id,
        )
        directory = self.root / relative
        if directory.exists():
            raise FileExistsError(f"trajectory output already exists: {relative}")
        directory.mkdir(parents=True)
        metadata = {
            "runner_id": RUNNER_ID,
            "runner_version": RUNNER_VERSION,
            "source_commit": trajectory.source_commit,
            "protocol_id": PROTOCOL_ID,
            "protocol_version": PROTOCOL_VERSION,
            "contract_version": CONTRACT_VERSION,
            "config_id": trajectory.config_id,
            "inferential_unit": trajectory.direction_id,
            "split": trajectory.split,
            "model_id": trajectory.model_id,
            "integrator": trajectory.integrator,
            "dt_or_tolerance_profile": trajectory.profile,
            "control_id": trajectory.control_id,
        }
        _write_new_json(directory / "metadata.json", metadata)
        _write_new_npy(
            directory / "observation_steps.npy",
            np.arange(trajectory.times.size, dtype=np.float64),
        )
        _write_new_npy(
            directory / "step_indices.npy",
            np.arange(1, trajectory.step_times.size + 1, dtype=np.float64),
        )
        for name, array in trajectory.raw_arrays().items():
            _write_new_npy(directory / f"{name}.npy", array)
        hashes = {
            str(path.relative_to(self.root)): file_sha256(path)
            for path in sorted(directory.iterdir())
            if path.is_file()
        }
        return ArchiveWriteResult(
            relative_directory=str(relative),
            files=hashes,
        )

    def write_summary(
        self,
        name: str,
        summary: Mapping[str, Any],
        raw_input_hashes: Mapping[str, str],
    ) -> str:
        if not name or "/" in name or "\\" in name:
            raise ValueError("summary name must be one path-safe component")
        if not raw_input_hashes:
            raise ValueError("summary must name all raw input hashes")
        payload = dict(summary)
        payload["raw_input_hashes"] = dict(sorted(raw_input_hashes.items()))
        path = self.root / "summaries" / f"{name}.json"
        _write_new_json(path, payload)
        return file_sha256(path)

    def append_failure(self, record: Mapping[str, Any]) -> None:
        if self._finalized:
            raise RuntimeError("archive has been finalized")
        if record.get("split") not in {PILOT_SPLIT, SMOKE_SPLIT}:
            raise ConfirmatoryAccessError("confirmatory failure records are forbidden")
        path = self.root / "failures.jsonl"
        with path.open("ab") as handle:
            handle.write(_canonical_json_bytes(record))

    def finalize(self) -> Mapping[str, str]:
        if self._finalized:
            raise RuntimeError("archive already finalized")
        checksum_path = self.root / "checksums.sha256"
        entries: dict[str, str] = {}
        for path in sorted(self.root.rglob("*")):
            if path.is_file() and path != checksum_path:
                relative = str(path.relative_to(self.root))
                entries[relative] = file_sha256(path)
        lines = "".join(f"{digest}  {relative}\n" for relative, digest in entries.items())
        _write_new_bytes(checksum_path, lines.encode("utf-8"))
        entries[str(checksum_path.relative_to(self.root))] = file_sha256(checksum_path)

        for path in sorted(self.root.rglob("*"), reverse=True):
            if path.is_file():
                path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
            elif path.is_dir():
                path.chmod(
                    stat.S_IRUSR
                    | stat.S_IXUSR
                    | stat.S_IRGRP
                    | stat.S_IXGRP
                    | stat.S_IROTH
                    | stat.S_IXOTH
                )
        self.root.chmod(
            stat.S_IRUSR
            | stat.S_IXUSR
            | stat.S_IRGRP
            | stat.S_IXGRP
            | stat.S_IROTH
            | stat.S_IXOTH
        )
        self._finalized = True
        return entries


def _contains_forbidden_identifier(value: Any, forbidden: set[str]) -> bool:
    if isinstance(value, Mapping):
        return any(
            _contains_forbidden_identifier(key, forbidden)
            or _contains_forbidden_identifier(item, forbidden)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_forbidden_identifier(item, forbidden) for item in value)
    if isinstance(value, str):
        return value in forbidden or any(
            value.startswith(f"p5-{item}-c") for item in forbidden
        )
    return False


def _path_contains_forbidden(parts: Iterable[str], forbidden: set[str]) -> bool:
    return any(
        component in forbidden
        or any(component.startswith(f"p5-{item}-c") for item in forbidden)
        for component in parts
    )


def archive_has_confirmatory_identifiers(
    archive_root: str | Path,
    confirmatory_direction_ids: Iterable[str],
) -> bool:
    """Inspect path components and structured fields, never raw hash substrings."""

    root = Path(archive_root)
    forbidden = {str(value) for value in confirmatory_direction_ids}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if _path_contains_forbidden(relative.parts, forbidden):
            return True
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix == ".json":
            if _contains_forbidden_identifier(load_json(path), forbidden):
                return True
        elif suffix == ".jsonl":
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip() and _contains_forbidden_identifier(
                    json.loads(line), forbidden
                ):
                    return True
        elif suffix == ".sha256":
            for line in path.read_text(encoding="utf-8").splitlines():
                if "  " not in line:
                    continue
                _, relative_name = line.split("  ", 1)
                if _path_contains_forbidden(Path(relative_name).parts, forbidden):
                    return True
    return False

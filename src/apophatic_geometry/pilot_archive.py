"""Write-once, attested archive and confirmatory-contamination checks."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import stat
from typing import Any, Iterable, Mapping

import numpy as np

from .models import CONTRACT_VERSION, ModelId
from .pilot_types import (
    PILOT_SPLIT,
    SMOKE_SPLIT,
    EXPECTED_PILOT_CONFIGURATIONS,
    RUNNER_ID,
    RUNNER_VERSION,
    ArchiveWriteResult,
    ConfirmatoryAccessError,
    FrozenProtocolBundle,
    PilotConfiguration,
    Trajectory,
)
from .protocol import PROTOCOL_ID, PROTOCOL_VERSION, file_sha256, load_json

_HEX_64 = re.compile(r"^[0-9a-f]{64}$")
_SAFE_COMPONENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")



def _safe_archive_path(root: Path, *components: str) -> Path:
    for component in components:
        if not isinstance(component, str) or _SAFE_COMPONENT.fullmatch(component) is None:
            raise ValueError(f"unsafe archive path component: {component!r}")
    candidate = root.joinpath(*components).resolve(strict=False)
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError("archive path escapes the archive root") from exc
    return candidate


def expected_trajectory_schema(
    bundle: FrozenProtocolBundle,
) -> tuple[tuple[str, str, str, str], ...]:
    """Return the exact 29 allowed trajectory labels per pilot configuration."""

    dts = [float(value) for value in bundle.protocol["time_and_sampling"]["refinement_dts"]]
    if dts != [0.001, 0.0005, 0.00025]:
        raise ValueError("frozen RK4 schedule differs from the runner contract")
    records: list[tuple[str, str, str, str]] = []
    for model in ModelId:
        for dt in dts:
            records.append((model.value, "RK4", f"rk4-dt-{dt:.8g}", "canonical"))
    for model in ModelId:
        records.append(
            (
                model.value,
                "DOP853",
                "dop853-rtol-1.0e-10-atol-1.0e-12-max-1.0e-03",
                "canonical",
            )
        )
    records.append(
        (ModelId.MF.value, "RK4", f"rk4-dt-{dts[2]:.8g}", "exogenous_replay")
    )
    for ablation in ("freeze_s", "freeze_q", "freeze_sq"):
        for model in ModelId:
            records.append((model.value, "RK4", f"rk4-dt-{dts[0]:.8g}", ablation))
    if len(records) != 29 or len(set(records)) != 29:
        raise RuntimeError("frozen trajectory schema is not exactly 29 unique records")
    return tuple(records)

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
        handle.flush()
        os.fsync(handle.fileno())


def _write_new_json(path: Path, value: Any) -> None:
    _write_new_bytes(path, _canonical_json_bytes(value))


def _write_new_npy(path: Path, value: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    array = np.asarray(value)
    if array.dtype.kind not in {"f", "i", "u"}:
        raise ValueError(f"unsupported numeric archive dtype: {array.dtype}")
    if array.dtype.kind == "f" and not np.all(np.isfinite(array)):
        raise ValueError(f"archive array contains non-finite values: {path.name}")
    with path.open("xb") as handle:
        np.save(handle, array, allow_pickle=False)
        handle.flush()
        os.fsync(handle.fileno())


def _require_digest(value: Any, name: str) -> str:
    if not isinstance(value, str) or _HEX_64.fullmatch(value) is None:
        raise ValueError(f"run manifest lacks valid {name}")
    return value


class PilotArchiveWriter:
    """Write-once archive builder with deterministic files and final checksums."""

    def __init__(
        self,
        root: str | Path,
        run_manifest: Mapping[str, Any],
        *,
        bundle: FrozenProtocolBundle | None = None,
    ) -> None:
        if run_manifest.get("runner_id") != RUNNER_ID:
            raise ValueError("run manifest has wrong runner_id")
        if run_manifest.get("runner_version") != RUNNER_VERSION:
            raise ValueError("run manifest has wrong runner_version")
        if run_manifest.get("protocol_id") != PROTOCOL_ID:
            raise ValueError("run manifest has wrong protocol_id")
        if run_manifest.get("protocol_version") != PROTOCOL_VERSION:
            raise ValueError("run manifest has wrong protocol_version")
        if run_manifest.get("split") != PILOT_SPLIT:
            raise ConfirmatoryAccessError("run manifest must be pilot-only")
        if run_manifest.get("confirmatory_execution") != "BLOCKED":
            raise ConfirmatoryAccessError(
                "run manifest must block confirmatory execution"
            )
        self.run_identity_sha256 = _require_digest(
            run_manifest.get("run_identity_sha256"), "run_identity_sha256"
        )
        self.attestation_sha256 = _require_digest(
            run_manifest.get("attestation_sha256"), "attestation_sha256"
        )
        self.source_tree_sha256 = _require_digest(
            run_manifest.get("source_tree_sha256"), "source_tree_sha256"
        )
        self.runtime_environment_sha256 = _require_digest(
            run_manifest.get("runtime_environment_sha256"),
            "runtime_environment_sha256",
        )
        self.run_manifest = dict(run_manifest)
        self.bundle = bundle
        source_commit = run_manifest.get("source_commit")
        self.source_commit = (
            source_commit
            if isinstance(source_commit, str) and _SAFE_COMPONENT.fullmatch(source_commit)
            else ""
        )
        execution_scope = run_manifest.get("execution_scope")
        self.execution_scope = (
            dict(execution_scope) if isinstance(execution_scope, Mapping) else {}
        )
        raw_schema = run_manifest.get("trajectory_schema")
        self.declared_trajectory_schema: set[tuple[str, str, str, str]] = set()
        self.declared_trajectory_schema_count = 0
        if isinstance(raw_schema, list):
            for entry in raw_schema:
                if isinstance(entry, Mapping):
                    values = tuple(
                        str(entry.get(name, ""))
                        for name in ("model_id", "integrator", "profile", "control_id")
                    )
                    if all(_SAFE_COMPONENT.fullmatch(value) for value in values):
                        self.declared_trajectory_schema.add(values)
                        self.declared_trajectory_schema_count += 1
        protocol_lock = run_manifest.get("protocol_lock")
        implementation_files = run_manifest.get("implementation_files")
        if not isinstance(protocol_lock, Mapping):
            raise ValueError("run manifest lacks protocol-lock attestation")
        _require_digest(protocol_lock.get("file_sha256"), "protocol lock hash")
        if not isinstance(implementation_files, Mapping) or not implementation_files:
            raise ValueError("run manifest lacks implementation-file hashes")
        for name, digest in implementation_files.items():
            if not isinstance(name, str):
                raise ValueError("implementation-file path must be text")
            _require_digest(digest, f"implementation hash for {name}")

        configuration_hashes = run_manifest.get("configuration_hashes")
        if not isinstance(configuration_hashes, Mapping) or not configuration_hashes:
            raise ValueError("run manifest lacks exact configuration membership")
        expected_hashes: dict[str, str] = {}
        for config_id, digest in configuration_hashes.items():
            if not isinstance(config_id, str) or not config_id:
                raise ValueError("configuration identifier must be non-empty text")
            expected_hashes[config_id] = _require_digest(
                digest, f"configuration hash for {config_id}"
            )
        expected_configuration_count = run_manifest.get("configuration_count")
        expected_trajectory_records = run_manifest.get("expected_trajectory_records")
        expected_summary_records = run_manifest.get("expected_summary_records")
        for name, value in (
            ("configuration_count", expected_configuration_count),
            ("expected_trajectory_records", expected_trajectory_records),
            ("expected_summary_records", expected_summary_records),
        ):
            if not isinstance(value, int) or value <= 0:
                raise ValueError(f"run manifest lacks positive {name}")
        if expected_configuration_count != len(expected_hashes):
            raise ValueError("configuration_count differs from exact membership")
        if expected_summary_records != expected_configuration_count:
            raise ValueError("one summary is required for every configuration")

        self.expected_configuration_hashes = expected_hashes
        self.expected_configuration_count = expected_configuration_count
        self.expected_trajectory_records = expected_trajectory_records
        self.expected_summary_records = expected_summary_records
        self._environment_written = False
        self._written_configurations: set[str] = set()
        self._trajectory_records: set[tuple[str, str, str, str, str]] = set()
        self._summaries: set[str] = set()
        self._summary_raw_hashes: dict[str, dict[str, str]] = {}
        self._trajectory_hashes_by_config: dict[str, dict[str, str]] = {}
        self._trajectory_source_commits: set[str] = set()
        self._failure_records = 0

        self.root = Path(root).resolve()
        if self.root.exists() and any(self.root.iterdir()):
            raise FileExistsError(
                "pilot archive directory must not already contain files"
            )
        self.root.mkdir(parents=True, exist_ok=True)
        for name in ("environment", "configs", "raw", "summaries"):
            (self.root / name).mkdir(exist_ok=False)
        _write_new_json(self.root / "RUN_MANIFEST.json", run_manifest)
        _write_new_json(
            self.root / "ARCHIVE_STATUS.json",
            {
                "completion_status": "IN_PROGRESS",
                "run_identity_sha256": self.run_identity_sha256,
                "confirmatory_execution": "BLOCKED",
            },
        )
        _write_new_bytes(self.root / "failures.jsonl", b"")
        self._finalized = False

    def write_environment(self, environment: Mapping[str, Any]) -> str:
        path = self.root / "environment" / "runtime.json"
        payload = dict(environment) | {
            "run_identity_sha256": self.run_identity_sha256,
            "attestation_sha256": self.attestation_sha256,
        }
        _write_new_json(path, payload)
        self._environment_written = True
        return file_sha256(path)

    def write_configuration(self, configuration: PilotConfiguration) -> str:
        if configuration.split != PILOT_SPLIT:
            raise ConfirmatoryAccessError(
                "only pilot configurations may enter the archive"
            )
        expected = self.expected_configuration_hashes.get(configuration.config_id)
        if expected is None:
            raise ConfirmatoryAccessError(
                "configuration is not a member of the frozen pilot set"
            )
        if configuration.configuration_hash != expected:
            raise ConfirmatoryAccessError(
                "configuration hash differs from frozen pilot membership"
            )
        path = _safe_archive_path(
            self.root, "configs", f"{configuration.config_id}.json"
        )
        payload = configuration.canonical_payload() | {
            "configuration_hash": configuration.configuration_hash,
            "run_identity_sha256": self.run_identity_sha256,
        }
        _write_new_json(path, payload)
        self._written_configurations.add(configuration.config_id)
        return file_sha256(path)

    def write_trajectory(self, trajectory: Trajectory) -> ArchiveWriteResult:
        if trajectory.split != PILOT_SPLIT:
            raise ConfirmatoryAccessError(
                "only pilot trajectories may enter the archive"
            )
        expected_hash = self.expected_configuration_hashes.get(trajectory.config_id)
        if expected_hash is None or trajectory.config_id not in self._written_configurations:
            raise ConfirmatoryAccessError(
                "trajectory configuration is not an archived frozen pilot member"
            )
        config_path = self.root / "configs" / f"{trajectory.config_id}.json"
        config = load_json(config_path)
        if not isinstance(config, Mapping):
            raise ValueError("archived configuration is invalid")
        if config.get("configuration_hash") != expected_hash:
            raise ConfirmatoryAccessError("archived configuration membership changed")
        if trajectory.direction_id != config.get("direction_id"):
            raise ConfirmatoryAccessError("trajectory direction was relabeled")
        initial = config.get("initial_state")
        if not isinstance(initial, Mapping):
            raise ValueError("archived configuration lacks initial state")
        expected_state = np.concatenate(
            [
                np.asarray(initial[name], dtype=np.float64)
                for name in ("x", "s", "q")
            ]
        )
        if not np.array_equal(trajectory.states[0], expected_state):
            raise ConfirmatoryAccessError(
                "trajectory initial state differs from frozen pilot configuration"
            )
        record_key = (
            trajectory.config_id,
            trajectory.model_id,
            trajectory.integrator,
            trajectory.profile,
            trajectory.control_id,
        )
        if record_key in self._trajectory_records:
            raise FileExistsError(f"duplicate trajectory record: {record_key}")
        directory = _safe_archive_path(
            self.root,
            "raw",
            trajectory.config_id,
            trajectory.model_id,
            trajectory.profile,
            trajectory.control_id,
        )
        relative = directory.relative_to(self.root)
        if directory.exists():
            raise FileExistsError(f"trajectory output already exists: {relative}")
        directory.mkdir(parents=True)
        metadata = {
            "runner_id": RUNNER_ID,
            "runner_version": RUNNER_VERSION,
            "source_commit": trajectory.source_commit,
            "source_tree_sha256": self.source_tree_sha256,
            "attestation_sha256": self.attestation_sha256,
            "runtime_environment_sha256": self.runtime_environment_sha256,
            "run_identity_sha256": self.run_identity_sha256,
            "protocol_id": PROTOCOL_ID,
            "protocol_version": PROTOCOL_VERSION,
            "contract_version": CONTRACT_VERSION,
            "config_id": trajectory.config_id,
            "configuration_hash": expected_hash,
            "inferential_unit": trajectory.direction_id,
            "split": trajectory.split,
            "model_id": trajectory.model_id,
            "integrator": trajectory.integrator,
            "dt_or_tolerance_profile": trajectory.profile,
            "control_id": trajectory.control_id,
            "observation_count": int(trajectory.times.size),
            "integration_step_count": int(trajectory.step_times.size),
            "start_time": float(trajectory.times[0]),
            "end_time": float(trajectory.times[-1]),
        }
        _write_new_json(directory / "metadata.json", metadata)
        _write_new_npy(
            directory / "observation_indices.npy",
            np.arange(trajectory.times.size, dtype=np.int64),
        )
        _write_new_npy(
            directory / "step_indices.npy",
            np.arange(1, trajectory.step_times.size + 1, dtype=np.int64),
        )
        for name, array in trajectory.raw_arrays().items():
            _write_new_npy(directory / f"{name}.npy", array)
        hashes = {
            str(path.relative_to(self.root)): file_sha256(path)
            for path in sorted(directory.iterdir())
            if path.is_file()
        }
        self._trajectory_records.add(record_key)
        self._trajectory_source_commits.add(trajectory.source_commit)
        self._trajectory_hashes_by_config.setdefault(trajectory.config_id, {}).update(hashes)
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
        payload["run_identity_sha256"] = self.run_identity_sha256
        payload["raw_input_hashes"] = dict(sorted(raw_input_hashes.items()))
        if name not in self.expected_configuration_hashes:
            raise ConfirmatoryAccessError(
                "summary is not associated with a frozen pilot configuration"
            )
        path = _safe_archive_path(self.root, "summaries", f"{name}.json")
        _write_new_json(path, payload)
        self._summaries.add(name)
        self._summary_raw_hashes[name] = dict(sorted(raw_input_hashes.items()))
        return file_sha256(path)

    def append_failure(self, record: Mapping[str, Any]) -> None:
        if self._finalized:
            raise RuntimeError("archive has been finalized")
        if record.get("split") not in {PILOT_SPLIT, SMOKE_SPLIT}:
            raise ConfirmatoryAccessError(
                "confirmatory failure records are forbidden"
            )
        payload = dict(record)
        payload["run_identity_sha256"] = self.run_identity_sha256
        path = self.root / "failures.jsonl"
        with path.open("ab") as handle:
            handle.write(_canonical_json_bytes(payload))
            handle.flush()
            os.fsync(handle.fileno())
        self._failure_records += 1

    def _validate_semantic_completion(self) -> None:
        if self.bundle is None:
            raise RuntimeError(
                "archive semantic completion requires the frozen protocol bundle"
            )
        from .pilot_manifest import build_pilot_configurations

        frozen = build_pilot_configurations(self.bundle)
        expected_hashes = {item.config_id: item.configuration_hash for item in frozen}
        expected_schema = set(expected_trajectory_schema(self.bundle))
        if self.expected_configuration_hashes != expected_hashes:
            raise RuntimeError("archive manifest does not name the exact frozen 50 configurations")
        if self.expected_configuration_count != EXPECTED_PILOT_CONFIGURATIONS:
            raise RuntimeError("archive manifest configuration count is not the frozen 50")
        if self.expected_trajectory_records != EXPECTED_PILOT_CONFIGURATIONS * 29:
            raise RuntimeError("archive manifest trajectory count is not the frozen 50 x 29")
        if self.expected_summary_records != EXPECTED_PILOT_CONFIGURATIONS:
            raise RuntimeError("archive manifest summary count is not the frozen 50")
        if (
            self.declared_trajectory_schema_count != 29
            or self.declared_trajectory_schema != expected_schema
        ):
            raise RuntimeError("archive manifest trajectory schema differs from the frozen 29")
        if self.execution_scope.get("configuration_count") != EXPECTED_PILOT_CONFIGURATIONS:
            raise RuntimeError("execution scope configuration count is inconsistent")
        if self.execution_scope.get("expected_trajectory_records") != EXPECTED_PILOT_CONFIGURATIONS * 29:
            raise RuntimeError("execution scope trajectory count is inconsistent")
        if self.execution_scope.get("expected_summary_records") != EXPECTED_PILOT_CONFIGURATIONS:
            raise RuntimeError("execution scope summary count is inconsistent")
        expected_records = {
            (config_id, model, integrator, profile, control)
            for config_id in expected_hashes
            for model, integrator, profile, control in expected_schema
        }
        if self._trajectory_records != expected_records:
            raise RuntimeError("archive trajectory membership differs from the frozen 50 x 29 set")
        if re.fullmatch(r"[0-9a-f]{40}", self.source_commit) is None:
            raise RuntimeError("run manifest source commit is not a full Git commit")
        if self._trajectory_source_commits != {self.source_commit}:
            raise RuntimeError("trajectory source commits do not match the run manifest")
        for config_id in expected_hashes:
            if self._summary_raw_hashes.get(config_id) != self._trajectory_hashes_by_config.get(config_id):
                raise RuntimeError(
                    f"summary raw-input hashes do not match archived trajectories: {config_id}"
                )

    def finalize(self) -> Mapping[str, str]:
        if self._finalized:
            raise RuntimeError("archive already finalized")
        if not self._environment_written:
            raise RuntimeError("archive cannot complete without runtime environment")
        expected_ids = set(self.expected_configuration_hashes)
        if self._written_configurations != expected_ids:
            missing = sorted(expected_ids - self._written_configurations)
            raise RuntimeError(
                f"archive configuration coverage is incomplete: {missing}"
            )
        if len(self._trajectory_records) != self.expected_trajectory_records:
            raise RuntimeError(
                "archive trajectory coverage mismatch: "
                f"{len(self._trajectory_records)} != {self.expected_trajectory_records}"
            )
        if self._summaries != expected_ids or len(self._summaries) != self.expected_summary_records:
            missing = sorted(expected_ids - self._summaries)
            raise RuntimeError(f"archive summary coverage is incomplete: {missing}")
        if self._failure_records:
            raise RuntimeError(
                "archive with failure records cannot be marked COMPLETE"
            )
        self._validate_semantic_completion()
        checksum_path = self.root / "checksums.sha256"
        _write_new_json(
            self.root / "ARCHIVE_COMPLETE.json",
            {
                "completion_status": "COMPLETE",
                "run_identity_sha256": self.run_identity_sha256,
                "attestation_sha256": self.attestation_sha256,
                "configuration_records": len(self._written_configurations),
                "trajectory_records": len(self._trajectory_records),
                "summary_records": len(self._summaries),
                "failure_records": self._failure_records,
                "confirmatory_execution": "BLOCKED",
            },
        )
        entries: dict[str, str] = {}
        for path in sorted(self.root.rglob("*")):
            if path.is_file() and path != checksum_path:
                relative = str(path.relative_to(self.root))
                entries[relative] = file_sha256(path)
        lines = "".join(
            f"{digest}  {relative}\n" for relative, digest in entries.items()
        )
        _write_new_bytes(checksum_path, lines.encode("utf-8"))
        entries[str(checksum_path.relative_to(self.root))] = file_sha256(
            checksum_path
        )

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
        return any(
            _contains_forbidden_identifier(item, forbidden) for item in value
        )
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
    """Inspect path components and strict structured fields, never raw hashes."""

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
                    json.loads(
                        line,
                        parse_constant=lambda token: (_ for _ in ()).throw(
                            ValueError(
                                f"non-standard JSON constant: {token}"
                            )
                        ),
                    ),
                    forbidden,
                ):
                    return True
        elif suffix == ".sha256":
            for line in path.read_text(encoding="utf-8").splitlines():
                if "  " not in line:
                    continue
                _, relative_name = line.split("  ", 1)
                if _path_contains_forbidden(
                    Path(relative_name).parts, forbidden
                ):
                    return True
    return False

"""Read-only independent verification of a completed Phase 6 pilot archive."""

from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Any, Mapping

import numpy as np

from .pilot_archive import expected_trajectory_schema
from .pilot_manifest import build_pilot_configurations
from .pilot_types import (
    EXPECTED_PILOT_CONFIGURATIONS,
    PILOT_SPLIT,
    FrozenProtocolBundle,
    ProtocolIntegrityError,
)
from .protocol import file_sha256, load_json

_HEX_40 = re.compile(r"^[0-9a-f]{40}$")
_HEX_64 = re.compile(r"^[0-9a-f]{64}$")


def _object(path: Path) -> Mapping[str, Any]:
    value = load_json(path)
    if not isinstance(value, Mapping):
        raise ProtocolIntegrityError(f"expected JSON object: {path}")
    return value


def _load_numeric(path: Path) -> np.ndarray:
    try:
        value = np.load(path, allow_pickle=False)
    except Exception as exc:  # pragma: no cover - NumPy supplies details
        raise ProtocolIntegrityError(f"unable to load numeric archive member: {path}") from exc
    if value.dtype.kind not in {"f", "i", "u"}:
        raise ProtocolIntegrityError(f"unsupported archive dtype: {path}")
    if value.dtype.kind == "f" and not np.all(np.isfinite(value)):
        raise ProtocolIntegrityError(f"non-finite archive array: {path}")
    return value


def _verify_checksums(root: Path) -> dict[str, str]:
    checksum_path = root / "checksums.sha256"
    if not checksum_path.is_file():
        raise ProtocolIntegrityError("completed archive lacks checksums.sha256")
    declared: dict[str, str] = {}
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        if "  " not in line:
            raise ProtocolIntegrityError("malformed checksum record")
        digest, relative = line.split("  ", 1)
        if _HEX_64.fullmatch(digest) is None or not relative:
            raise ProtocolIntegrityError("invalid checksum record")
        if relative in declared:
            raise ProtocolIntegrityError("duplicate checksum record")
        declared[relative] = digest
    actual_members = {
        str(path.relative_to(root))
        for path in root.rglob("*")
        if path.is_file() and path != checksum_path
    }
    if set(declared) != actual_members:
        raise ProtocolIntegrityError("archive checksum membership is incomplete or excessive")
    for relative, digest in declared.items():
        path = (root / relative).resolve(strict=True)
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise ProtocolIntegrityError("archive checksum path escapes root") from exc
        if file_sha256(path) != digest:
            raise ProtocolIntegrityError(f"archive checksum mismatch: {relative}")
    return declared


def verify_pilot_archive(
    archive_root: str | Path,
    bundle: FrozenProtocolBundle,
) -> dict[str, Any]:
    """Verify exact frozen membership, labels, hashes, grids, and provenance."""

    root = Path(archive_root).resolve(strict=True)
    if not root.is_dir():
        raise ProtocolIntegrityError("pilot archive root is not a directory")
    checksums = _verify_checksums(root)
    manifest = _object(root / "RUN_MANIFEST.json")
    complete = _object(root / "ARCHIVE_COMPLETE.json")
    if complete.get("completion_status") != "COMPLETE":
        raise ProtocolIntegrityError("archive is not marked COMPLETE")
    if manifest.get("split") != PILOT_SPLIT or manifest.get("confirmatory_execution") != "BLOCKED":
        raise ProtocolIntegrityError("archive is not pilot-only")
    source_commit = manifest.get("source_commit")
    if not isinstance(source_commit, str) or _HEX_40.fullmatch(source_commit) is None:
        raise ProtocolIntegrityError("archive source commit is invalid")

    frozen = build_pilot_configurations(bundle)
    expected_hashes = {item.config_id: item.configuration_hash for item in frozen}
    expected_states = {item.config_id: item.initial_state.pack() for item in frozen}
    if len(expected_hashes) != EXPECTED_PILOT_CONFIGURATIONS:
        raise ProtocolIntegrityError("frozen pilot reconstruction is incomplete")
    if manifest.get("configuration_hashes") != expected_hashes:
        raise ProtocolIntegrityError("archive configuration membership differs from frozen pilot")
    if manifest.get("configuration_count") != EXPECTED_PILOT_CONFIGURATIONS:
        raise ProtocolIntegrityError("archive configuration count differs from frozen pilot")
    if manifest.get("expected_trajectory_records") != EXPECTED_PILOT_CONFIGURATIONS * 29:
        raise ProtocolIntegrityError("archive trajectory count differs from frozen pilot")
    if manifest.get("expected_summary_records") != EXPECTED_PILOT_CONFIGURATIONS:
        raise ProtocolIntegrityError("archive summary count differs from frozen pilot")

    schema = set(expected_trajectory_schema(bundle))
    declared_schema = manifest.get("trajectory_schema")
    if not isinstance(declared_schema, list):
        raise ProtocolIntegrityError("archive trajectory schema is missing")
    parsed_schema = {
        (
            str(item.get("model_id", "")),
            str(item.get("integrator", "")),
            str(item.get("profile", "")),
            str(item.get("control_id", "")),
        )
        for item in declared_schema
        if isinstance(item, Mapping)
    }
    if parsed_schema != schema:
        raise ProtocolIntegrityError("archive trajectory schema differs from frozen 29")

    time_policy = bundle.protocol["time_and_sampling"]
    horizon = float(time_policy["horizon"])
    observation_interval = float(time_policy["observation_interval"])
    expected_times = np.linspace(
        0.0,
        horizon,
        int(round(horizon / observation_interval)) + 1,
        dtype=np.float64,
    )

    raw_hashes_by_config: dict[str, dict[str, str]] = {
        config_id: {} for config_id in expected_hashes
    }
    record_count = 0
    required_arrays = {
        "times", "states", "geometry", "local_proposal", "feedback",
        "combined_proposal", "projection_correction", "constraint_residual",
        "tangency_residual", "denominator", "step_times",
        "raw_constraint_residual", "post_constraint_residual",
        "retraction_magnitude", "observation_indices", "step_indices",
    }
    for config_id, model_id, integrator, profile, control_id in (
        (config_id, *labels)
        for config_id in expected_hashes
        for labels in schema
    ):
        directory = root / "raw" / config_id / model_id / profile / control_id
        resolved = directory.resolve(strict=True)
        try:
            resolved.relative_to(root)
        except ValueError as exc:
            raise ProtocolIntegrityError("trajectory directory escapes archive root") from exc
        metadata = _object(resolved / "metadata.json")
        expected_labels = {
            "config_id": config_id,
            "configuration_hash": expected_hashes[config_id],
            "split": PILOT_SPLIT,
            "model_id": model_id,
            "integrator": integrator,
            "dt_or_tolerance_profile": profile,
            "control_id": control_id,
            "source_commit": source_commit,
            "run_identity_sha256": manifest.get("run_identity_sha256"),
        }
        for key, expected in expected_labels.items():
            if metadata.get(key) != expected:
                raise ProtocolIntegrityError(f"trajectory metadata mismatch: {config_id}:{key}")
        files = {path.stem for path in resolved.glob("*.npy")}
        if files != required_arrays:
            raise ProtocolIntegrityError(f"trajectory array membership mismatch: {config_id}:{profile}:{control_id}")
        times = _load_numeric(resolved / "times.npy")
        states = _load_numeric(resolved / "states.npy")
        geometry = _load_numeric(resolved / "geometry.npy")
        if not np.array_equal(times, expected_times):
            raise ProtocolIntegrityError("trajectory observation grid differs from frozen policy")
        if states.shape != (expected_times.size, 9) or geometry.shape != (expected_times.size, 3):
            raise ProtocolIntegrityError("trajectory state/geometry shape is invalid")
        if not np.array_equal(states[0], expected_states[config_id]):
            raise ProtocolIntegrityError("trajectory initial state differs from frozen configuration")
        observation_indices = _load_numeric(resolved / "observation_indices.npy")
        if not np.array_equal(observation_indices, np.arange(expected_times.size, dtype=np.int64)):
            raise ProtocolIntegrityError("trajectory observation indices are invalid")
        step_times = _load_numeric(resolved / "step_times.npy")
        step_indices = _load_numeric(resolved / "step_indices.npy")
        if step_times.ndim != 1 or not np.all(np.diff(step_times) > 0.0):
            raise ProtocolIntegrityError("trajectory step grid is invalid")
        if not np.array_equal(step_indices, np.arange(1, step_times.size + 1, dtype=np.int64)):
            raise ProtocolIntegrityError("trajectory step indices are invalid")
        for path in resolved.iterdir():
            if path.is_file():
                relative = str(path.relative_to(root))
                raw_hashes_by_config[config_id][relative] = checksums[relative]
        record_count += 1

    if record_count != EXPECTED_PILOT_CONFIGURATIONS * 29:
        raise ProtocolIntegrityError("archive does not contain exactly 50 x 29 trajectories")

    for config in frozen:
        config_payload = _object(root / "configs" / f"{config.config_id}.json")
        if config_payload.get("configuration_hash") != config.configuration_hash:
            raise ProtocolIntegrityError("archived configuration hash differs")
        summary = _object(root / "summaries" / f"{config.config_id}.json")
        if summary.get("status") != "ACCEPTED":
            raise ProtocolIntegrityError("completed archive contains a non-accepted summary")
        if summary.get("config_id") != config.config_id:
            raise ProtocolIntegrityError("summary configuration identity differs")
        if summary.get("raw_input_hashes") != dict(sorted(raw_hashes_by_config[config.config_id].items())):
            raise ProtocolIntegrityError("summary raw-input hashes do not resolve to raw trajectories")

    if complete.get("configuration_records") != EXPECTED_PILOT_CONFIGURATIONS:
        raise ProtocolIntegrityError("completion configuration count is false")
    if complete.get("trajectory_records") != EXPECTED_PILOT_CONFIGURATIONS * 29:
        raise ProtocolIntegrityError("completion trajectory count is false")
    if complete.get("summary_records") != EXPECTED_PILOT_CONFIGURATIONS:
        raise ProtocolIntegrityError("completion summary count is false")
    if complete.get("failure_records") != 0:
        raise ProtocolIntegrityError("completed archive contains failures")

    return {
        "status": "VERIFIED_COMPLETE",
        "configuration_records": EXPECTED_PILOT_CONFIGURATIONS,
        "trajectory_records": EXPECTED_PILOT_CONFIGURATIONS * 29,
        "summary_records": EXPECTED_PILOT_CONFIGURATIONS,
        "source_commit": source_commit,
        "checksummed_files": len(checksums),
    }

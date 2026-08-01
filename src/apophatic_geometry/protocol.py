"""Executable definitions for the frozen ARG Phase 5 comparison protocol.

This module contains metrics, manifest validation, deterministic uncertainty
summaries, strict JSON loading, root-confined lock verification, and fail-closed
decision logic. It does not execute trajectories.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]

PROTOCOL_ID = "ARG-P5-COMP-v1"
PROTOCOL_VERSION = "1.0.0"
PRIMARY_DETECT_THRESHOLD = 0.02
PRIMARY_EQUIVALENCE_MARGIN = 0.002
PRIMARY_NUMERICAL_RATIO = 10.0
PRIMARY_REQUIRED_FRACTION = 0.80
PRIMARY_BOOTSTRAP_SEED = 20260801
PRIMARY_BOOTSTRAP_RESAMPLES = 50_000


class PrimaryOutcome(str, Enum):
    """Fail-closed outcomes for the frozen primary decision rule."""

    DETECTED = "DETECTED"
    EQUIVALENT_WITHIN_PROTOCOL_MARGIN = "EQUIVALENT_WITHIN_PROTOCOL_MARGIN"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True)
class BootstrapInterval:
    """Percentile interval for a direction-level statistic."""

    estimate: float
    lower: float
    upper: float
    confidence_level: float
    resamples: int
    seed: int


@dataclass(frozen=True)
class PrimaryDecision:
    """Complete output from the preregistered primary rule."""

    outcome: PrimaryOutcome
    interval: BootstrapInterval
    detected_fraction: float
    direction_count: int
    effects: tuple[float, ...]
    numerical_floors: tuple[float, ...]


def _as_trajectory(value: Sequence[Sequence[float]] | FloatArray) -> FloatArray:
    array = np.asarray(value, dtype=np.float64)
    if array.ndim == 1:
        array = array[:, None]
    if array.ndim != 2:
        raise ValueError(
            f"trajectory must be one- or two-dimensional, received {array.ndim}"
        )
    if array.shape[0] < 1:
        raise ValueError("trajectory must contain at least one observation")
    if not np.all(np.isfinite(array)):
        raise ValueError("trajectory contains non-finite values")
    return array


def symmetric_normalized_rms(
    left: Sequence[Sequence[float]] | FloatArray,
    right: Sequence[Sequence[float]] | FloatArray,
    *,
    epsilon: float = 1.0e-30,
) -> float:
    """Return the frozen dimensionless symmetric trajectory distance."""

    a = _as_trajectory(left)
    b = _as_trajectory(right)
    if a.shape != b.shape:
        raise ValueError(f"trajectory shapes differ: {a.shape} != {b.shape}")
    if not np.isfinite(epsilon) or epsilon <= 0.0:
        raise ValueError("epsilon must be finite and positive")
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            difference_energy = float(np.sum((a - b) ** 2, dtype=np.float64))
            state_energy = float(
                np.sum(a**2, dtype=np.float64) + np.sum(b**2, dtype=np.float64)
            )
            value = float(
                np.sqrt(2.0 * difference_energy / (state_energy + epsilon))
            )
    except FloatingPointError as exc:
        raise FloatingPointError("trajectory distance left the finite FP64 domain") from exc
    if not np.isfinite(value):
        raise FloatingPointError("non-finite trajectory distance")
    return value


def max_abs_discrepancy(
    left: Sequence[Sequence[float]] | FloatArray,
    right: Sequence[Sequence[float]] | FloatArray,
) -> float:
    """Return the maximum absolute elementwise trajectory discrepancy."""

    a = _as_trajectory(left)
    b = _as_trajectory(right)
    if a.shape != b.shape:
        raise ValueError(f"trajectory shapes differ: {a.shape} != {b.shape}")
    value = float(np.max(np.abs(a - b)))
    if not np.isfinite(value):
        raise FloatingPointError("non-finite maximum discrepancy")
    return value


def root_energy_ratio(
    numerator: Sequence[Sequence[float]] | FloatArray,
    denominator: Sequence[Sequence[float]] | FloatArray,
    *,
    epsilon: float = 1.0e-30,
) -> float:
    """Return ``sqrt(sum ||N||^2) / (sqrt(sum ||D||^2) + epsilon)``."""

    n = _as_trajectory(numerator)
    d = _as_trajectory(denominator)
    if n.shape[0] != d.shape[0]:
        raise ValueError("numerator and denominator must share observation count")
    if not np.isfinite(epsilon) or epsilon <= 0.0:
        raise ValueError("epsilon must be finite and positive")
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            numerator_energy = float(np.sqrt(np.sum(n**2, dtype=np.float64)))
            denominator_energy = float(np.sqrt(np.sum(d**2, dtype=np.float64)))
            ratio = numerator_energy / (denominator_energy + epsilon)
    except FloatingPointError as exc:
        raise FloatingPointError("energy ratio left the finite FP64 domain") from exc
    if not np.isfinite(ratio):
        raise FloatingPointError("non-finite energy ratio")
    return float(ratio)


def percentile_bootstrap_median(
    values: Sequence[float] | FloatArray,
    *,
    confidence_level: float = 0.95,
    resamples: int = PRIMARY_BOOTSTRAP_RESAMPLES,
    seed: int = PRIMARY_BOOTSTRAP_SEED,
) -> BootstrapInterval:
    """Return the frozen percentile-bootstrap interval for the median."""

    array = np.asarray(values, dtype=np.float64)
    if array.ndim != 1 or array.size < 2:
        raise ValueError(
            "bootstrap input must be a one-dimensional array of length >= 2"
        )
    if not np.all(np.isfinite(array)):
        raise ValueError("bootstrap input contains non-finite values")
    if not 0.0 < confidence_level < 1.0:
        raise ValueError("confidence_level must lie strictly between zero and one")
    if resamples < 100:
        raise ValueError("resamples must be at least 100")
    if not isinstance(seed, (int, np.integer)):
        raise TypeError("seed must be an integer")

    generator = np.random.Generator(np.random.PCG64(int(seed)))
    indices = generator.integers(0, array.size, size=(int(resamples), array.size))
    medians = np.median(array[indices], axis=1)
    alpha = 1.0 - confidence_level
    lower, upper = np.quantile(medians, [alpha / 2.0, 1.0 - alpha / 2.0])
    return BootstrapInterval(
        estimate=float(np.median(array)),
        lower=float(lower),
        upper=float(upper),
        confidence_level=float(confidence_level),
        resamples=int(resamples),
        seed=int(seed),
    )


def evaluate_primary(
    direction_effects: Sequence[float] | FloatArray,
    direction_numerical_floors: Sequence[float] | FloatArray,
    *,
    detect_threshold: float = PRIMARY_DETECT_THRESHOLD,
    equivalence_margin: float = PRIMARY_EQUIVALENCE_MARGIN,
    numerical_ratio: float = PRIMARY_NUMERICAL_RATIO,
    required_fraction: float = PRIMARY_REQUIRED_FRACTION,
    confidence_level: float = 0.95,
    resamples: int = PRIMARY_BOOTSTRAP_RESAMPLES,
    seed: int = PRIMARY_BOOTSTRAP_SEED,
) -> PrimaryDecision:
    """Apply the frozen H1 decision rule without discretionary branches."""

    effects = np.asarray(direction_effects, dtype=np.float64)
    floors = np.asarray(direction_numerical_floors, dtype=np.float64)
    if effects.ndim != 1 or floors.ndim != 1 or effects.shape != floors.shape:
        raise ValueError("effects and numerical floors must be matching 1D arrays")
    if effects.size < 2:
        raise ValueError("at least two direction units are required")
    if not np.all(np.isfinite(effects)) or not np.all(np.isfinite(floors)):
        raise ValueError("effects and numerical floors must be finite")
    if np.any(effects < 0.0) or np.any(floors < 0.0):
        raise ValueError("effects and numerical floors must be nonnegative")
    if not 0.0 < equivalence_margin < detect_threshold:
        raise ValueError("require 0 < equivalence_margin < detect_threshold")
    if not np.isfinite(numerical_ratio) or numerical_ratio <= 1.0:
        raise ValueError("numerical_ratio must be finite and exceed one")
    if not 0.0 < required_fraction <= 1.0:
        raise ValueError("required_fraction must lie in (0, 1]")

    interval = percentile_bootstrap_median(
        effects,
        confidence_level=confidence_level,
        resamples=resamples,
        seed=seed,
    )
    ratio_pass = effects >= numerical_ratio * np.maximum(floors, 1.0e-30)
    effect_pass = effects > detect_threshold
    detected_fraction = float(np.mean(effect_pass & ratio_pass))

    if interval.lower > detect_threshold and detected_fraction >= required_fraction:
        outcome = PrimaryOutcome.DETECTED
    elif (
        interval.upper < equivalence_margin
        and bool(np.all(effects < equivalence_margin))
        and bool(np.all(floors < equivalence_margin / 3.0))
    ):
        outcome = PrimaryOutcome.EQUIVALENT_WITHIN_PROTOCOL_MARGIN
    else:
        outcome = PrimaryOutcome.INCONCLUSIVE

    return PrimaryDecision(
        outcome=outcome,
        interval=interval,
        detected_fraction=detected_fraction,
        direction_count=int(effects.size),
        effects=tuple(float(value) for value in effects),
        numerical_floors=tuple(float(value) for value in floors),
    )


def canonical_json_sha256(value: Any) -> str:
    """Hash a JSON-compatible value using sorted compact UTF-8 JSON."""

    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def file_sha256(path: str | Path) -> str:
    """Return the SHA-256 of an existing regular file."""

    file_path = Path(path)
    if not file_path.is_file():
        raise ValueError(f"not a regular file: {file_path}")
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _reject_json_constant(token: str) -> None:
    raise ValueError(f"non-standard JSON constant: {token}")


def load_json(path: str | Path) -> Any:
    """Load RFC-compliant UTF-8 JSON and reject NaN/Infinity constants."""

    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle, parse_constant=_reject_json_constant)


def validate_protocol_manifest(manifest: Mapping[str, Any]) -> None:
    """Fail closed if the frozen protocol manifest is incomplete or altered."""

    if manifest.get("protocol_id") != PROTOCOL_ID:
        raise ValueError("unexpected protocol_id")
    if manifest.get("protocol_version") != PROTOCOL_VERSION:
        raise ValueError("unexpected protocol_version")
    if manifest.get("status") != "FROZEN_NO_DATA":
        raise ValueError("protocol must remain FROZEN_NO_DATA at Phase 5")
    if manifest.get("model_ids") != ["m0", "mf", "mp", "mfp"]:
        raise ValueError("model order differs from the frozen protocol")

    primary = manifest.get("primary_hypothesis")
    if not isinstance(primary, Mapping):
        raise ValueError("primary_hypothesis is missing")
    if primary.get("comparison") != ["mf", "mp"]:
        raise ValueError("primary comparison differs from the frozen protocol")
    if primary.get("observation_map") != "full":
        raise ValueError("primary observation map differs from the frozen protocol")
    if float(primary.get("detect_threshold")) != PRIMARY_DETECT_THRESHOLD:
        raise ValueError("primary detect threshold differs from the frozen protocol")
    if float(primary.get("equivalence_margin")) != PRIMARY_EQUIVALENCE_MARGIN:
        raise ValueError("primary equivalence margin differs from the frozen protocol")

    time_policy = manifest.get("time_and_sampling")
    if not isinstance(time_policy, Mapping):
        raise ValueError("time_and_sampling is missing")
    if time_policy.get("refinement_dts") != [0.001, 0.0005, 0.00025]:
        raise ValueError("refinement schedule differs from the frozen protocol")
    if int(time_policy.get("observation_count")) != 1001:
        raise ValueError("observation count differs from the frozen protocol")

    authorization = manifest.get("authorization")
    if not isinstance(authorization, Mapping):
        raise ValueError("authorization is missing")
    if authorization.get("confirmatory_execution") != "BLOCKED":
        raise ValueError("confirmatory execution must remain blocked")


def validate_initial_condition_manifest(manifest: Mapping[str, Any]) -> None:
    """Validate counts, geometry, split integrity, and configuration generator."""

    if manifest.get("protocol_id") != PROTOCOL_ID:
        raise ValueError("initial-condition manifest has wrong protocol_id")
    if manifest.get("status") != "FROZEN_NO_TRAJECTORIES":
        raise ValueError("initial-condition status must remain frozen and unexecuted")

    directions = manifest.get("directions")
    if not isinstance(directions, list) or len(directions) != 24:
        raise ValueError("unexpected direction count")

    generation = manifest.get("generation")
    rule = manifest.get("configuration_rule")
    counts = manifest.get("counts")
    if not isinstance(generation, Mapping) or not isinstance(rule, Mapping):
        raise ValueError("generation and configuration_rule are required")
    if not isinstance(counts, Mapping):
        raise ValueError("counts are required")
    if generation.get("c0_levels") != [0.05, 0.1, 0.25, 0.5, 1.0]:
        raise ValueError("unexpected c0 levels")
    if rule.get("enumeration") != (
        "Cartesian product of each frozen direction with each c0 level."
    ):
        raise ValueError("configuration enumeration differs from the frozen rule")

    direction_ids: set[str] = set()
    split_hashes: dict[str, str] = {}
    split_by_direction: dict[str, str] = {}
    for entry in directions:
        direction_id = str(entry["direction_id"])
        if direction_id in direction_ids:
            raise ValueError(f"duplicate direction_id: {direction_id}")
        direction_ids.add(direction_id)
        vector = np.asarray(entry["unit_vector"], dtype=np.float64)
        if vector.shape != (3,) or not np.all(np.isfinite(vector)):
            raise ValueError(f"invalid unit vector for {direction_id}")
        if not np.isclose(np.linalg.norm(vector), 1.0, rtol=0.0, atol=1.0e-14):
            raise ValueError(f"direction {direction_id} is not normalized")
        if vector[2] <= 0.0:
            raise ValueError(
                f"direction {direction_id} is not on the declared hemisphere"
            )
        expected_hash = hashlib.sha256(
            f"{direction_id}|{PROTOCOL_ID}".encode("utf-8")
        ).hexdigest()
        if entry["split_hash"] != expected_hash:
            raise ValueError(f"split hash mismatch for {direction_id}")
        split_hashes[direction_id] = expected_hash
        split_by_direction[direction_id] = str(entry["split"])

    expected_pilot = {
        direction_id
        for direction_id, _ in sorted(split_hashes.items(), key=lambda item: item[1])[:10]
    }
    actual_pilot = {
        direction_id
        for direction_id, split in split_by_direction.items()
        if split == "pilot"
    }
    if actual_pilot != expected_pilot:
        raise ValueError("pilot/confirmatory split does not match the frozen hash rule")
    if set(split_by_direction.values()) != {"pilot", "confirmatory"}:
        raise ValueError("unexpected split label")

    if int(counts.get("pilot_directions")) != 10:
        raise ValueError("pilot direction count mismatch")
    if int(counts.get("confirmatory_directions")) != 14:
        raise ValueError("confirmatory direction count mismatch")
    if int(counts.get("configurations_total")) != 120:
        raise ValueError("configuration count mismatch")
    if int(counts.get("pilot_configurations")) != 50:
        raise ValueError("pilot configuration count mismatch")
    if int(counts.get("confirmatory_configurations")) != 70:
        raise ValueError("confirmatory configuration count mismatch")


def _locked_path(root: Path, relative_path: str) -> Path:
    """Resolve one lock target and require containment within ``root``."""

    if not relative_path or Path(relative_path).is_absolute():
        raise ValueError(f"lock path must be non-empty and relative: {relative_path!r}")
    resolved_root = root.resolve(strict=True)
    candidate = (resolved_root / relative_path).resolve(strict=True)
    try:
        candidate.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(
            f"lock path escapes repository root: {relative_path}"
        ) from exc
    if not candidate.is_file():
        raise ValueError(f"lock target is not a regular file: {relative_path}")
    return candidate


def verify_lock(repo_root: str | Path, lock_manifest: Mapping[str, Any]) -> None:
    """Verify every root-confined critical file named by the lock manifest."""

    if lock_manifest.get("protocol_id") != PROTOCOL_ID:
        raise ValueError("lock manifest has wrong protocol_id")
    files = lock_manifest.get("files")
    if not isinstance(files, Mapping) or not files:
        raise ValueError("lock manifest has no files")

    root = Path(repo_root)
    for raw_relative_path, expected_digest in files.items():
        relative_path = str(raw_relative_path)
        if not isinstance(expected_digest, str) or len(expected_digest) != 64:
            raise ValueError(f"invalid SHA-256 for lock target: {relative_path}")
        path = _locked_path(root, relative_path)
        if path.suffix.lower() == ".json":
            actual = canonical_json_sha256(load_json(path))
        else:
            actual = file_sha256(path)
        if actual != expected_digest:
            raise ValueError(f"lock mismatch for {relative_path}")

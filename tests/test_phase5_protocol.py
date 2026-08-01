from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from apophatic_geometry.protocol import (
    PRIMARY_BOOTSTRAP_SEED,
    PrimaryOutcome,
    canonical_json_sha256,
    evaluate_primary,
    max_abs_discrepancy,
    percentile_bootstrap_median,
    root_energy_ratio,
    symmetric_normalized_rms,
    validate_initial_condition_manifest,
    validate_protocol_manifest,
    verify_lock,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_ROOT = REPO_ROOT / "protocol" / "phase5_v1"


def _load(name: str) -> dict:
    with (PROTOCOL_ROOT / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def test_symmetric_normalized_rms_known_cases() -> None:
    zero = np.zeros((3, 2), dtype=np.float64)
    ones = np.ones((3, 2), dtype=np.float64)

    assert symmetric_normalized_rms(ones, ones) == 0.0
    assert np.isclose(
        symmetric_normalized_rms(ones, zero),
        np.sqrt(2.0),
        rtol=0.0,
        atol=1.0e-15,
    )
    assert np.isclose(
        symmetric_normalized_rms(ones, -ones),
        2.0,
        rtol=0.0,
        atol=1.0e-15,
    )


def test_trajectory_metrics_fail_closed() -> None:
    with pytest.raises(ValueError, match="shapes differ"):
        symmetric_normalized_rms(np.zeros((2, 2)), np.zeros((3, 2)))
    with pytest.raises(ValueError, match="non-finite"):
        symmetric_normalized_rms(np.array([[np.nan]]), np.array([[0.0]]))
    with pytest.raises(ValueError, match="shapes differ"):
        max_abs_discrepancy(np.zeros((2, 1)), np.zeros((2, 2)))


def test_root_energy_ratio_known_case() -> None:
    numerator = np.array([[3.0, 4.0]], dtype=np.float64)
    denominator = np.array([[0.0, 5.0]], dtype=np.float64)
    assert np.isclose(root_energy_ratio(numerator, denominator), 1.0)


def test_percentile_bootstrap_is_deterministic() -> None:
    values = np.array([0.01, 0.02, 0.03, 0.04, 0.05], dtype=np.float64)
    first = percentile_bootstrap_median(
        values,
        resamples=2_000,
        seed=PRIMARY_BOOTSTRAP_SEED,
    )
    second = percentile_bootstrap_median(
        values,
        resamples=2_000,
        seed=PRIMARY_BOOTSTRAP_SEED,
    )
    assert first == second
    assert first.lower <= first.estimate <= first.upper


def test_primary_rule_detected() -> None:
    effects = np.full(14, 0.05, dtype=np.float64)
    floors = np.full(14, 1.0e-5, dtype=np.float64)
    decision = evaluate_primary(effects, floors, resamples=1_000)
    assert decision.outcome is PrimaryOutcome.DETECTED
    assert decision.detected_fraction == 1.0


def test_primary_rule_equivalent_within_margin() -> None:
    effects = np.full(14, 5.0e-4, dtype=np.float64)
    floors = np.full(14, 1.0e-5, dtype=np.float64)
    decision = evaluate_primary(effects, floors, resamples=1_000)
    assert decision.outcome is PrimaryOutcome.EQUIVALENT_WITHIN_PROTOCOL_MARGIN


def test_primary_rule_inconclusive_gap() -> None:
    effects = np.full(14, 0.01, dtype=np.float64)
    floors = np.full(14, 1.0e-5, dtype=np.float64)
    decision = evaluate_primary(effects, floors, resamples=1_000)
    assert decision.outcome is PrimaryOutcome.INCONCLUSIVE


def test_primary_rule_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        evaluate_primary([0.1], [0.001], resamples=100)
    with pytest.raises(ValueError):
        evaluate_primary([0.1, 0.2], [0.001], resamples=100)
    with pytest.raises(ValueError):
        evaluate_primary([0.1, -0.2], [0.001, 0.001], resamples=100)


def test_protocol_manifest_is_frozen_and_valid() -> None:
    manifest = _load("protocol.json")
    validate_protocol_manifest(manifest)
    assert manifest["authorization"]["confirmatory_execution"] == "BLOCKED"
    assert manifest["status"] == "FROZEN_NO_DATA"


def test_initial_condition_manifest_split_and_geometry() -> None:
    manifest = _load("initial_conditions.json")
    validate_initial_condition_manifest(manifest)

    pilot_directions = {
        entry["direction_id"]
        for entry in manifest["directions"]
        if entry["split"] == "pilot"
    }
    confirmatory_directions = {
        entry["direction_id"]
        for entry in manifest["directions"]
        if entry["split"] == "confirmatory"
    }
    assert len(pilot_directions) == 10
    assert len(confirmatory_directions) == 14
    assert pilot_directions.isdisjoint(confirmatory_directions)

    assert manifest["counts"]["pilot_configurations"] == 50
    assert manifest["counts"]["confirmatory_configurations"] == 70
    assert manifest["counts"]["configurations_total"] == 120


def test_parameter_manifest_has_no_tuning() -> None:
    manifest = _load("parameters.json")
    assert manifest["status"] == "FROZEN_NO_FITTING"
    assert manifest["policy"]["fitting"] == "none"
    assert manifest["policy"]["tuning"] == "none"


def test_intervention_manifest_excludes_contract_changes() -> None:
    manifest = _load("interventions.json")
    assert manifest["status"] == "FROZEN_NO_EXECUTION"
    assert (
        manifest["graph_structure_manifest"]["status"]
        == "EXCLUDED_BY_CONTRACT_V1"
    )
    assert manifest["soft_penalty_control"]["status"] == "EXCLUDED_BY_CONTRACT_V1"
    assert len(manifest["relabeling_tripwire"]["permutations"]) == 6


def test_canonical_json_hash_is_order_invariant() -> None:
    left = {"b": 2, "a": [1, 3]}
    right = {"a": [1, 3], "b": 2}
    assert canonical_json_sha256(left) == canonical_json_sha256(right)


def test_phase5_lock_matches_critical_files() -> None:
    lock = _load("LOCK.json")
    verify_lock(REPO_ROOT, lock)

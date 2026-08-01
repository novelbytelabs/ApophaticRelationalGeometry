from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path
import subprocess

import pytest

import apophatic_geometry.pilot as pilot_module
import apophatic_geometry.pilot_manifest as manifest_module
from apophatic_geometry.models import ModelId
from apophatic_geometry.pilot import (
    CONFIRMATORY_SPLIT, EXPECTED_PILOT_CONFIGURATIONS, EXPECTED_PILOT_DIRECTIONS,
    ConfirmatoryAccessError, PilotConfiguration, ProtocolIntegrityError,
    authorize_pilot_batch, build_pilot_configurations, execute_pilot,
    frozen_parameters, integrate_dop853, integrate_rk4, load_frozen_bundle,
    pilot_plan, require_complete_pilot_batch, validate_execution_authorization,
    verify_model_baseline,
)
from reference_pilot import independent_configuration_hashes, independent_pilot_ids

REPO_ROOT = Path(__file__).resolve().parents[1]

@pytest.fixture(scope="module")
def bundle():
    return load_frozen_bundle(REPO_ROOT)

@pytest.fixture(scope="module")
def params(bundle):
    return frozen_parameters(bundle)

def test_phase6_bundle_and_plan_are_pilot_only(bundle) -> None:
    plan = pilot_plan(bundle)
    assert plan["configuration_count"] == EXPECTED_PILOT_CONFIGURATIONS
    assert plan["direction_count"] == EXPECTED_PILOT_DIRECTIONS
    assert plan["split"] == "pilot"
    assert plan["pilot_executed"] is False
    assert plan["confirmatory_execution"] == "BLOCKED"
    assert len(plan["configuration_ids"]) == len(set(plan["configuration_ids"]))

    confirmatory = {
        entry["direction_id"]
        for entry in bundle.initial_conditions["directions"]
        if entry["split"] == CONFIRMATORY_SPLIT
    }
    assert not any(
        any(config_id.startswith(f"p5-{direction_id}-") for direction_id in confirmatory)
        for config_id in plan["configuration_ids"]
    )


def test_independent_pilot_reconstruction_matches_production(bundle) -> None:
    production = build_pilot_configurations(bundle)
    assert tuple(item.config_id for item in production) == independent_pilot_ids(
        bundle.initial_conditions
    )
    independent_hashes = independent_configuration_hashes(bundle.initial_conditions)
    assert {item.config_id: item.configuration_hash for item in production} == independent_hashes


def test_complete_batch_gate_requires_all_fifty(bundle) -> None:
    configurations = build_pilot_configurations(bundle)
    assert len(require_complete_pilot_batch(configurations)) == 50
    with pytest.raises(ConfirmatoryAccessError, match="exactly 50"):
        require_complete_pilot_batch(configurations[:-1])


def test_confirmatory_and_mixed_batches_fail_before_integration(bundle, monkeypatch) -> None:
    pilot = build_pilot_configurations(bundle)[0]
    confirmatory = PilotConfiguration(
        config_id="p5-d01-c005",
        direction_id="d01",
        split="confirmatory",
        c0=pilot.c0,
        initial_state=pilot.initial_state,
        configuration_hash="0" * 64,
    )
    with pytest.raises(ConfirmatoryAccessError):
        authorize_pilot_batch([confirmatory])
    with pytest.raises(ConfirmatoryAccessError):
        authorize_pilot_batch([pilot, confirmatory])

    called = False

    def forbidden(*args, **kwargs):
        nonlocal called
        called = True
        raise AssertionError("integration must not be reached")

    monkeypatch.setattr(pilot_module, "integrate_rk4", forbidden)
    with pytest.raises(ConfirmatoryAccessError):
        authorize_pilot_batch([pilot, confirmatory])
    assert called is False


def test_direct_confirmatory_integration_is_rejected(bundle, params) -> None:
    pilot = build_pilot_configurations(bundle)[0]
    confirmatory = replace(
        pilot,
        config_id="p5-d01-c005",
        direction_id="d01",
        split="confirmatory",
        configuration_hash="1" * 64,
    )
    with pytest.raises(ConfirmatoryAccessError):
        integrate_rk4(
            confirmatory,
            params,
            ModelId.MF,
            dt=0.001,
            horizon=0.01,
            observation_interval=0.01,
            source_commit="test",
        )
    with pytest.raises(ConfirmatoryAccessError):
        integrate_dop853(
            confirmatory,
            params,
            ModelId.MP,
            horizon=0.001,
            observation_interval=0.001,
            source_commit="test",
        )


def test_model_baseline_is_available_and_unchanged(bundle) -> None:
    source_commit = verify_model_baseline(REPO_ROOT, bundle.protocol)
    assert len(source_commit) == 40


def test_model_baseline_mutation_fails_closed(bundle, monkeypatch) -> None:
    original = manifest_module._run_git

    def mutated(root: Path, *args: str):
        if args and args[0] == "diff":
            return subprocess.CompletedProcess(args, 1, "", "changed")
        return original(root, *args)

    monkeypatch.setattr(manifest_module, "_run_git", mutated)
    with pytest.raises(ProtocolIntegrityError, match="model equations differ"):
        verify_model_baseline(REPO_ROOT, bundle.protocol)


def test_execution_authorization_names_prior_runner_commit(tmp_path, monkeypatch) -> None:
    auth_path = tmp_path / "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json"
    auth_path.parent.mkdir(parents=True)
    runner_commit = "1" * 40
    execution_commit = "2" * 40
    auth_path.write_text(
        json.dumps(
            {
                "authorization_id": "ARG-P6-PILOT-EXEC-v1",
                "status": "AUTHORIZED",
                "protocol_id": "ARG-P5-COMP-v1",
                "protocol_version": "1.0.0",
                "runner_id": "ARG-P6-PILOT-RUNNER-v1",
                "runner_version": "1.0.0",
                "split": "pilot",
                "runner_source_commit": runner_commit,
                "execution_id": "test",
                "execution_utc": "2026-08-01T00:00:00Z",
                "confirmatory_execution": "BLOCKED",
            }
        ),
        encoding="utf-8",
    )

    def git_ok(root: Path, *args: str):
        return subprocess.CompletedProcess(args, 0, "", "")

    monkeypatch.setattr(manifest_module, "_run_git", git_ok)
    authorization = validate_execution_authorization(tmp_path, execution_commit)
    assert authorization["runner_source_commit"] == runner_commit


def test_execute_is_blocked_without_separate_authorization(tmp_path) -> None:
    archive = tmp_path / "pilot-archive"
    with pytest.raises(ProtocolIntegrityError, match="execution record is absent"):
        execute_pilot(REPO_ROOT, archive)
    assert not archive.exists()


def test_no_execution_authorization_or_pilot_archive_is_committed() -> None:
    assert not (REPO_ROOT / "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json").exists()
    assert not (REPO_ROOT / "artifacts/phase6_pilot").exists()

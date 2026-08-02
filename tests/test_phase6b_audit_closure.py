from __future__ import annotations

from dataclasses import replace
import hashlib
import json
from pathlib import Path

import numpy as np
import pytest

from apophatic_geometry.model import State
from apophatic_geometry.models import ModelId
from apophatic_geometry.pilot import (
    ConfirmatoryAccessError,
    PilotArchiveWriter,
    PilotConfiguration,
    build_pilot_configurations,
    configuration_payload,
    frozen_parameters,
    integrate_rk4,
    load_frozen_bundle,
    validate_execution_environment_policy,
)
from apophatic_geometry.pilot_types import Trajectory
from apophatic_geometry.protocol import canonical_json_sha256

REPO_ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUTS = REPO_ROOT / "audits/external/arg_phase6a2_reaudit_inputs.json"


def _bogus_manifest(config: PilotConfiguration) -> dict[str, object]:
    return {
        "runner_id": "ARG-P6-PILOT-RUNNER-v1",
        "runner_version": "1.1.0",
        "protocol_id": "ARG-P5-COMP-v1",
        "protocol_version": "1.0.0",
        "source_commit": "not-a-commit",
        "split": "pilot",
        "configuration_count": 1,
        "configuration_hashes": {config.config_id: config.configuration_hash},
        "expected_trajectory_records": 1,
        "expected_summary_records": 1,
        "confirmatory_execution": "BLOCKED",
        "run_identity_sha256": "1" * 64,
        "attestation_sha256": "2" * 64,
        "source_tree_sha256": "3" * 64,
        "runtime_environment_sha256": "4" * 64,
        "protocol_lock": {"file_sha256": "5" * 64},
        "implementation_files": {"anything.py": "6" * 64},
        "execution_scope": {
            "configuration_count": 50,
            "expected_trajectory_records": 1450,
            "expected_summary_records": 50,
        },
        "trajectory_schema": [],
    }


def _fake_trajectory(config: PilotConfiguration) -> Trajectory:
    n = 2
    states = np.repeat(config.initial_state.pack()[None, :], n, axis=0)
    zero9 = np.zeros((n, 9))
    return Trajectory(
        config_id=config.config_id,
        direction_id=config.direction_id,
        split="pilot",
        model_id="bogus",
        integrator="BOGUS",
        profile="bogus-profile",
        control_id="bogus-control",
        source_commit="not-a-commit",
        times=np.array([0.0, 1.0]),
        states=states,
        geometry=np.zeros((n, 3)),
        local_proposal=zero9,
        feedback=zero9,
        combined_proposal=zero9,
        projection_correction=zero9,
        constraint_residual=np.zeros(n),
        tangency_residual=np.zeros(n),
        denominator=np.ones(n),
        step_times=np.array([1.0]),
        raw_constraint_residual=np.zeros(1),
        post_constraint_residual=np.zeros(1),
        retraction_magnitude=np.zeros(1),
    )


def test_auditor_report_and_tripwire_are_hash_bound_exactly() -> None:
    inputs = json.loads(AUDIT_INPUTS.read_text(encoding="utf-8"))
    assert inputs["report"]["sha256"] == "985e0534fd52dcf1f2832e17d3796ad6627d728dedd5711c4e6bdc546ddfe749"
    assert inputs["report"]["verdict"] == "CONDITIONAL_PASS"
    assert inputs["tripwire"]["sha256"] == "8979a1aa6a481b3376f7f86be26f511acf6b2b1fe4f1add5fa7e9861430049b3"
    assert inputs["tripwire"]["observed_after_remediation"] == "19_PASS_0_FAIL_0_INCONCLUSIVE"


def test_confirmatory_state_relabel_is_rejected_at_public_integrator() -> None:
    bundle = load_frozen_bundle(REPO_ROOT)
    params = frozen_parameters(bundle)
    entry = next(
        item
        for item in bundle.initial_conditions["directions"]
        if item["split"] == "confirmatory"
    )
    c0 = float(bundle.initial_conditions["generation"]["c0_levels"][0])
    state = State(
        x=np.sqrt(3.0 * c0) * np.asarray(entry["unit_vector"], dtype=np.float64),
        s=np.asarray(bundle.initial_conditions["generation"]["shared_s0"], dtype=np.float64),
        q=np.asarray(bundle.initial_conditions["generation"]["shared_q0"], dtype=np.float64),
    )
    payload = configuration_payload("p5-fake-c005", "fake", "pilot", c0, state)
    relabelled = PilotConfiguration(
        config_id="p5-fake-c005",
        direction_id="fake",
        split="pilot",
        c0=c0,
        initial_state=state,
        configuration_hash=canonical_json_sha256(payload),
    )
    with pytest.raises(ConfirmatoryAccessError):
        integrate_rk4(
            relabelled,
            params,
            ModelId.MF,
            dt=0.001,
            horizon=0.001,
            observation_interval=0.001,
            source_commit="tripwire",
        )
    with pytest.raises(ConfirmatoryAccessError):
        integrate_rk4(
            relabelled,
            params,
            ModelId.MF,
            bundle=bundle,
            dt=0.001,
            horizon=0.001,
            observation_interval=0.001,
            source_commit="tripwire",
        )


def test_platform_policy_rejects_declared_windows_arm_runtime() -> None:
    runtime = {
        "python_implementation": "CPython",
        "python_version": "3.12.13",
        "operating_system": "Windows",
        "platform": "Windows-11-arm64",
        "machine": "arm64",
        "numpy_configuration": "fake",
        "numpy_configuration_sha256": hashlib.sha256(b"fake").hexdigest(),
        "distributions": {},
    }
    with pytest.raises(Exception):
        validate_execution_environment_policy(
            REPO_ROOT, runtime, require_execution_clearance=False
        )


def test_semantically_bogus_archive_cannot_be_complete(tmp_path: Path) -> None:
    bundle = load_frozen_bundle(REPO_ROOT)
    config = build_pilot_configurations(bundle)[0]
    trajectory = _fake_trajectory(config)
    writer = PilotArchiveWriter(
        tmp_path / "bogus", _bogus_manifest(config), bundle=bundle
    )
    writer.write_environment({"fake": True})
    writer.write_configuration(config)
    written = writer.write_trajectory(trajectory)
    writer.write_summary(
        config.config_id,
        {"status": "ACCEPTED", "effects": {"primary": 12345}},
        {"made-up": "7" * 64},
    )
    assert written.files
    with pytest.raises(RuntimeError):
        writer.finalize()
    assert not (writer.root / "ARCHIVE_COMPLETE.json").exists()


def test_archive_path_components_are_root_confined(tmp_path: Path) -> None:
    bundle = load_frozen_bundle(REPO_ROOT)
    config = build_pilot_configurations(bundle)[0]
    writer = PilotArchiveWriter(tmp_path / "archive", _bogus_manifest(config), bundle=bundle)
    writer.write_environment({"fake": True})
    writer.write_configuration(config)
    escaped = replace(_fake_trajectory(config), model_id="../../../../escaped")
    with pytest.raises(ValueError, match="unsafe archive path component"):
        writer.write_trajectory(escaped)
    assert not (tmp_path / "escaped").exists()


def test_full_horizon_workflow_checks_triggering_sha() -> None:
    workflow = (
        REPO_ROOT / ".github/workflows/phase6a2-full-horizon.yml"
    ).read_text(encoding="utf-8")
    assert "ref: ${{ github.sha }}" in workflow
    assert "ref: phase6a2-defensive-hardening" not in workflow
    assert "git rev-parse HEAD^{tree}" in workflow


def test_authorization_validator_has_complete_tree_binding() -> None:
    source = (
        REPO_ROOT / "src/apophatic_geometry/pilot_manifest.py"
    ).read_text(encoding="utf-8")
    tail = source[source.index("def validate_execution_authorization"):]
    assert "src/apophatic_geometry/__init__.py" in tail
    assert "runner_git_tree" in tail
    assert "runner_source_tree_sha256" in tail
    assert "post-audit execution commit must change only" in tail

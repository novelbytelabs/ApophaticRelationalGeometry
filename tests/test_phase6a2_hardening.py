from __future__ import annotations

from dataclasses import replace
import json
import os
from pathlib import Path
import subprocess

import numpy as np
import pytest

from apophatic_geometry.attestation import AttestationError, require_clean_tracked_tree
from apophatic_geometry.models import (
    PROJECTOR_TOLERANCE,
    ModelId,
    ProjectionTarget,
    project_node_derivative,
)
from apophatic_geometry.pilot import (
    PilotArchiveWriter,
    ProtocolIntegrityError,
    assess_numerics,
    frozen_parameters,
    integrate_dop853,
    integrate_rk4,
    load_frozen_bundle,
    smoke_configuration,
    validate_execution_authorization,
)
from apophatic_geometry.pilot_types import ControlSpec
from apophatic_geometry.protocol import canonical_json_sha256

REPO_ROOT = Path(__file__).resolve().parents[1]


def _manifest(config_id: str, configuration_hash: str, *, trajectories: int = 1) -> dict[str, object]:
    return {
        "runner_id": "ARG-P6-PILOT-RUNNER-v1",
        "runner_version": "1.0.0",
        "protocol_id": "ARG-P5-COMP-v1",
        "protocol_version": "1.0.0",
        "split": "pilot",
        "configuration_count": 1,
        "configuration_hashes": {config_id: configuration_hash},
        "expected_trajectory_records": trajectories,
        "expected_summary_records": 1,
        "confirmatory_execution": "BLOCKED",
        "run_identity_sha256": "1" * 64,
        "attestation_sha256": "2" * 64,
        "source_tree_sha256": "3" * 64,
        "runtime_environment_sha256": "4" * 64,
        "protocol_lock": {"file_sha256": "5" * 64},
        "implementation_files": {"test.py": "6" * 64},
    }


def test_control_arrays_are_owned_and_read_only() -> None:
    times = np.array([0.0, 1.0])
    values = np.array([1.0, 2.0])
    control = ControlSpec(exogenous_times=times, exogenous_c=values)
    times[0] = 99.0
    values[0] = 99.0
    assert control.exogenous_times is not None
    assert control.exogenous_c is not None
    assert control.exogenous_times.tolist() == [0.0, 1.0]
    assert control.exogenous_c.tolist() == [1.0, 2.0]
    assert not control.exogenous_times.flags.writeable
    assert not control.exogenous_c.flags.writeable


def test_trajectory_arrays_are_owned_and_read_only() -> None:
    bundle = load_frozen_bundle(REPO_ROOT)
    params = frozen_parameters(bundle)
    config = smoke_configuration(bundle)
    trajectory = integrate_rk4(
        config,
        params,
        ModelId.MF,
        dt=0.001,
        horizon=0.002,
        observation_interval=0.001,
        source_commit="test",
    )
    for array in trajectory.raw_arrays().values():
        assert not array.flags.writeable
        with pytest.raises(ValueError):
            array.flat[0] = array.flat[0]


def test_empty_archive_cannot_be_marked_complete(tmp_path: Path) -> None:
    writer = PilotArchiveWriter(tmp_path / "archive", _manifest("p", "1" * 64))
    with pytest.raises(RuntimeError, match="runtime environment"):
        writer.finalize()


def test_archive_rejects_relabelled_initial_state(tmp_path: Path) -> None:
    bundle = load_frozen_bundle(REPO_ROOT)
    params = frozen_parameters(bundle)
    pilot = next(iter(__import__("apophatic_geometry.pilot", fromlist=["build_pilot_configurations"]).build_pilot_configurations(bundle)))
    writer = PilotArchiveWriter(
        tmp_path / "archive",
        _manifest(pilot.config_id, pilot.configuration_hash),
    )
    writer.write_environment({"test": True})
    writer.write_configuration(pilot)

    smoke = smoke_configuration(bundle)
    relabelled = integrate_rk4(
        smoke,
        params,
        ModelId.MF,
        dt=0.001,
        horizon=0.001,
        observation_interval=0.001,
        source_commit="test",
    )
    relabelled = replace(
        relabelled,
        config_id=pilot.config_id,
        direction_id=pilot.direction_id,
        split="pilot",
    )
    with pytest.raises(Exception, match="initial state differs"):
        writer.write_trajectory(relabelled)


def test_untracked_python_shadow_file_blocks_attestation() -> None:
    shadow = REPO_ROOT / "numpy.py"
    assert not shadow.exists()
    shadow.write_text("raise RuntimeError('shadowed')\n", encoding="utf-8")
    try:
        with pytest.raises(AttestationError, match="untracked"):
            require_clean_tracked_tree(REPO_ROOT)
    finally:
        shadow.unlink(missing_ok=True)


def test_authorization_scope_mismatch_fails_closed(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    from apophatic_geometry import pilot_manifest as manifest_module

    path = tmp_path / "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json"
    path.parent.mkdir(parents=True)
    expected_scope = {"scope_version": "ARG-P6-EXEC-SCOPE-v2", "value": 1}
    wrong_scope = {"scope_version": "ARG-P6-EXEC-SCOPE-v2", "value": 2}
    path.write_text(
        json.dumps(
            {
                "authorization_id": "ARG-P6-PILOT-EXEC-v1",
                "status": "AUTHORIZED",
                "protocol_id": "ARG-P5-COMP-v1",
                "protocol_version": "1.0.0",
                "runner_id": "ARG-P6-PILOT-RUNNER-v1",
                "runner_version": "1.0.0",
                "split": "pilot",
                "runner_source_commit": "1" * 40,
                "execution_id": "test",
                "execution_utc": "2026-08-01T00:00:00Z",
                "scope": wrong_scope,
                "scope_sha256": canonical_json_sha256(wrong_scope),
                "external_audit": {
                    "clearance": "CLEARED_FOR_PILOT",
                    "bundle_sha256": "2" * 64,
                    "report_sha256": "3" * 64,
                    "tripwire_sha256": "4" * 64,
                },
                "confirmatory_execution": "BLOCKED",
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        manifest_module,
        "_run_git",
        lambda root, *args: subprocess.CompletedProcess(args, 0, "", ""),
    )
    with pytest.raises(ProtocolIntegrityError, match="scope differs"):
        validate_execution_authorization(
            tmp_path,
            "5" * 40,
            expected_scope=expected_scope,
        )


def test_near_radial_projection_roundoff_cleanup_meets_frozen_tolerance() -> None:
    x = np.array(
        [-0.7103751263703857, -0.6378792663177448, 0.8209154395162704],
        dtype=np.float64,
    )
    proposal = np.array(
        [-1.365806732675058, -1.2264221769407428, 1.5783377204086004],
        dtype=np.float64,
    )
    denominator = float(np.dot(x, x))
    legacy = proposal - x * (float(np.dot(x, proposal)) / denominator)
    legacy_tangency = abs(float(np.dot(x, legacy))) / (
        float(np.linalg.norm(x)) * float(np.linalg.norm(legacy)) + 1.0e-30
    )
    assert legacy_tangency > PROJECTOR_TOLERANCE

    target = ProjectionTarget(c0=denominator / 3.0)
    projected, correction, tangency, actual_denominator = project_node_derivative(
        x, proposal, target
    )
    assert actual_denominator == denominator
    assert tangency <= PROJECTOR_TOLERANCE
    np.testing.assert_allclose(
        proposal + correction,
        projected,
        rtol=0.0,
        atol=5.0e-16,
    )


def test_integrity_baseline_records_roundoff_only_projector_remediation() -> None:
    baseline = json.loads(
        (REPO_ROOT / "protocol/phase6_runner_v1/INTEGRITY_BASELINE.json").read_text(
            encoding="utf-8"
        )
    )
    assert baseline["baseline_id"] == "ARG-P6-INTEGRITY-BASELINE-v3"
    assert baseline["scientific_equations_changed"] is False
    remediation = baseline["numerical_remediation"]
    assert remediation["scientific_equation_changed"] is False
    assert remediation["protocol_threshold_changed"] is False
    assert remediation["pilot_data_generated"] is False
    assert PROJECTOR_TOLERANCE == 1.0e-12


@pytest.mark.slow
@pytest.mark.skipif(
    os.environ.get("ARG_RUN_FULL_HORIZON") != "1",
    reason="full-horizon smoke gate runs only in the dedicated numerical job",
)
def test_full_horizon_smoke_primary_models_pass_numerical_gates() -> None:
    """Full protocol horizon on smoke-only data; this is not pilot evidence."""

    bundle = load_frozen_bundle(REPO_ROOT)
    params = frozen_parameters(bundle)
    config = smoke_configuration(bundle)
    policy = bundle.protocol["time_and_sampling"]
    horizon = float(policy["horizon"])
    observation_interval = float(policy["observation_interval"])
    dts = [float(value) for value in policy["refinement_dts"]]
    for model in (ModelId.MF, ModelId.MP):
        runs = [
            integrate_rk4(
                config,
                params,
                model,
                dt=dt,
                horizon=horizon,
                observation_interval=observation_interval,
                source_commit="smoke-full-horizon",
            )
            for dt in dts
        ]
        alternate = integrate_dop853(
            config,
            params,
            model,
            horizon=horizon,
            observation_interval=observation_interval,
            source_commit="smoke-full-horizon",
        )
        assessment = assess_numerics(*runs, alternate, "full")
        assert assessment.passed

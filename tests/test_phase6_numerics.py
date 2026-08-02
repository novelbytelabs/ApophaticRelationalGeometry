from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path
import stat

import numpy as np
import pytest

from apophatic_geometry.models import ModelId
from apophatic_geometry.pilot import (
    ArchiveWriteResult,
    ConfirmatoryAccessError,
    ControlSpec,
    PilotArchiveWriter,
    PilotConfiguration,
    Trajectory,
    archive_has_confirmatory_identifiers,
    assess_numerics,
    exogenous_replay_control,
    frozen_parameters,
    integrate_dop853,
    integrate_rk4,
    load_frozen_bundle,
    require_constraint_gate,
    require_same_state_identity_gate,
    run_permutation_tripwires,
    smoke_configuration,
    summarize_configuration,
)
from apophatic_geometry.protocol import canonical_json_sha256
from reference_pilot import independent_file_hashes, independent_reference_trajectory

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def bundle():
    return load_frozen_bundle(REPO_ROOT)


@pytest.fixture(scope="module")
def params(bundle):
    return frozen_parameters(bundle)


@pytest.mark.parametrize("model", list(ModelId))
def test_smoke_rk4_matches_independent_reference(
    bundle, params, model: ModelId
) -> None:
    config = smoke_configuration(bundle)
    production = integrate_rk4(
        config,
        params,
        model,
        dt=0.001,
        horizon=0.02,
        observation_interval=0.01,
        source_commit="smoke",
    )
    reference = independent_reference_trajectory(
        config.initial_state,
        params,
        model.value,
        c0=config.c0,
        dt=0.001,
        horizon=0.02,
        observation_interval=0.01,
    )
    np.testing.assert_allclose(
        production.states, reference, rtol=0.0, atol=2.0e-14
    )
    assert production.split == "smoke"
    assert production.states.shape == (3, 9)
    assert production.geometry.shape == (3, 3)


@pytest.mark.parametrize("model", [ModelId.MP, ModelId.MFP])
def test_smoke_projected_validity_gates(
    bundle, params, model: ModelId
) -> None:
    config = smoke_configuration(bundle)
    trajectory = integrate_rk4(
        config,
        params,
        model,
        dt=0.001,
        horizon=0.02,
        observation_interval=0.01,
        source_commit="smoke",
    )
    require_constraint_gate(trajectory, config.c0)
    require_same_state_identity_gate(trajectory, params, config.c0)
    assert np.max(np.abs(trajectory.post_constraint_residual)) <= 1.0e-12
    assert np.max(trajectory.tangency_residual) <= 1.0e-12


@pytest.mark.parametrize("model", list(ModelId))
def test_smoke_dop853_policy_is_finite(
    bundle, params, model: ModelId
) -> None:
    config = smoke_configuration(bundle)
    trajectory = integrate_dop853(
        config,
        params,
        model,
        horizon=0.002,
        observation_interval=0.001,
        source_commit="smoke",
    )
    assert trajectory.states.shape == (3, 9)
    assert np.all(np.isfinite(trajectory.states))
    if model in {ModelId.MP, ModelId.MFP}:
        require_constraint_gate(trajectory, config.c0)
        require_same_state_identity_gate(trajectory, params, config.c0)


def test_exogenous_replay_uses_frozen_observation_signal(bundle, params) -> None:
    config = smoke_configuration(bundle)
    reference = integrate_rk4(
        config,
        params,
        ModelId.MF,
        dt=0.001,
        horizon=0.02,
        observation_interval=0.01,
        source_commit="smoke",
    )
    control = exogenous_replay_control(reference)
    replay = integrate_rk4(
        config,
        params,
        ModelId.MF,
        dt=0.001,
        horizon=0.02,
        observation_interval=0.01,
        source_commit="smoke",
        control=control,
    )
    assert replay.control_id == "exogenous_replay"
    expected_c = np.mean(reference.states[:, 0:3] ** 2, axis=1)
    np.testing.assert_allclose(
        replay.feedback[:, 3],
        params.eta_2 * expected_c / params.tau_s,
        rtol=0.0,
        atol=1.0e-15,
    )


@pytest.mark.parametrize(
    ("ablation", "s_frozen", "q_frozen"),
    [
        ("freeze_s", True, False),
        ("freeze_q", False, True),
        ("freeze_sq", True, True),
    ],
)
def test_adaptive_substrate_ablations_hold_declared_state(
    bundle, params, ablation: str, s_frozen: bool, q_frozen: bool
) -> None:
    config = smoke_configuration(bundle)
    trajectory = integrate_rk4(
        config,
        params,
        ModelId.MFP,
        dt=0.001,
        horizon=0.01,
        observation_interval=0.01,
        source_commit="smoke",
        control=ControlSpec(ablation=ablation),
    )
    if s_frozen:
        np.testing.assert_array_equal(
            trajectory.states[:, 3:6],
            np.repeat(
                config.initial_state.s[None, :],
                trajectory.times.size,
                axis=0,
            ),
        )
    if q_frozen:
        np.testing.assert_array_equal(
            trajectory.states[:, 6:9],
            np.repeat(
                config.initial_state.q[None, :],
                trajectory.times.size,
                axis=0,
            ),
        )


@pytest.mark.parametrize("model", list(ModelId))
def test_all_six_permutation_tripwires_pass_on_smoke(
    bundle, params, model: ModelId
) -> None:
    config = smoke_configuration(bundle)
    results = run_permutation_tripwires(
        config,
        params,
        model,
        dt=0.001,
        horizon=0.01,
        observation_interval=0.01,
        source_commit="smoke",
        tolerance=1.0e-11,
    )
    assert set(results) == {"012", "021", "102", "120", "201", "210"}
    assert max(results.values()) <= 1.0e-11


def test_configuration_summary_contains_frozen_primary_floor(
    bundle, params
) -> None:
    config = smoke_configuration(bundle)
    dts = [0.004, 0.002, 0.001]
    trajectories: dict[tuple[str, str], Trajectory] = {}
    for model in ModelId:
        for dt in dts:
            trajectory = integrate_rk4(
                config,
                params,
                model,
                dt=dt,
                horizon=0.004,
                observation_interval=0.004,
                source_commit="smoke",
            )
            trajectories[(model.value, trajectory.profile)] = trajectory
    alternates = {
        model.value: integrate_dop853(
            config,
            params,
            model,
            horizon=0.004,
            observation_interval=0.004,
            source_commit="smoke",
            max_step=0.001,
        )
        for model in ModelId
    }
    summary = summarize_configuration(trajectories, alternates, dts)
    primary = summary["primary"]
    assert primary["comparison"] == ["mf", "mp"]
    assert primary["configuration_numerical_floor"] == max(
        primary["model_numerical_floors"].values()
    )
    assert primary["effect"] >= 0.0
    assert set(summary["mechanism_ratios"]) == {
        "mf_feedback",
        "mp_projection",
        "mfp_feedback",
        "mfp_projection",
    }


def test_numerical_assessment_known_pass(bundle, params) -> None:
    config = smoke_configuration(bundle)
    base = integrate_rk4(
        config,
        params,
        ModelId.MF,
        dt=0.001,
        horizon=0.01,
        observation_interval=0.01,
        source_commit="smoke",
    )
    coarse = replace(base, states=base.states + 1.0e-4)
    medium = replace(base, states=base.states + 1.0e-7)
    fine = base
    alternate = replace(
        base,
        integrator="DOP853",
        profile="test-alt",
        states=base.states + 1.0e-8,
    )
    assessment = assess_numerics(coarse, medium, fine, alternate, "full")
    assert assessment.refinement_pass
    assert assessment.endpoint_pass
    assert assessment.alternate_pass
    assert assessment.passed


def _test_pilot_config(smoke: PilotConfiguration) -> PilotConfiguration:
    state = smoke.initial_state
    payload = {
        "protocol_id": "ARG-P5-COMP-v1",
        "protocol_version": "1.0.0",
        "contract_version": "1.0",
        "config_id": "test-pilot",
        "direction_id": "test-pilot",
        "split": "pilot",
        "c0": smoke.c0,
        "initial_state": {
            "x": state.x.tolist(),
            "s": state.s.tolist(),
            "q": state.q.tolist(),
        },
    }
    return PilotConfiguration(
        config_id="test-pilot",
        direction_id="test-pilot",
        split="pilot",
        c0=smoke.c0,
        initial_state=state,
        configuration_hash=canonical_json_sha256(payload),
    )


def _make_test_pilot_trajectory(
    bundle, params
) -> tuple[PilotConfiguration, Trajectory]:
    smoke = smoke_configuration(bundle)
    config = _test_pilot_config(smoke)
    trajectory = integrate_rk4(
        config,
        params,
        ModelId.MF,
        dt=0.001,
        horizon=0.01,
        observation_interval=0.01,
        source_commit="0" * 40,
    )
    return config, trajectory


def _archive_manifest(configuration_hash: str = "1" * 64) -> dict[str, object]:
    return {
        "runner_id": "ARG-P6-PILOT-RUNNER-v1",
        "runner_version": "1.0.0",
        "protocol_id": "ARG-P5-COMP-v1",
        "protocol_version": "1.0.0",
        "execution_id": "test-execution",
        "execution_utc": "2026-08-01T00:00:00Z",
        "split": "pilot",
        "configuration_count": 1,
        "configuration_hashes": {"test-pilot": configuration_hash},
        "expected_trajectory_records": 1,
        "expected_summary_records": 1,
        "confirmatory_execution": "BLOCKED",
        "run_identity_sha256": "1" * 64,
        "attestation_sha256": "2" * 64,
        "source_tree_sha256": "3" * 64,
        "runtime_environment_sha256": "4" * 64,
        "protocol_lock": {"file_sha256": "5" * 64},
        "implementation_files": {"test.py": "6" * 64},
    }


def _restore_write_permissions(root: Path) -> None:
    if not root.exists():
        return
    for path in root.rglob("*"):
        if path.is_dir():
            path.chmod(stat.S_IRWXU)
        else:
            path.chmod(stat.S_IRUSR | stat.S_IWUSR)
    root.chmod(stat.S_IRWXU)


def test_archive_is_deterministic_and_independently_hashed(
    tmp_path, bundle, params
) -> None:
    config, trajectory = _make_test_pilot_trajectory(bundle, params)
    manifest = _archive_manifest(config.configuration_hash)
    checksum_bytes = []
    try:
        for name in ("archive-a", "archive-b"):
            root = tmp_path / name
            writer = PilotArchiveWriter(root, manifest)
            writer.write_environment({"python": "test", "packages": {}})
            writer.write_configuration(config)
            written = writer.write_trajectory(trajectory)
            assert isinstance(written, ArchiveWriteResult)
            writer.write_summary(
                "test-pilot",
                {"status": "ACCEPTED"},
                written.files,
            )
            checksums = writer.finalize()
            assert checksums
            assert (root / "ARCHIVE_COMPLETE.json").is_file()
            checksum_bytes.append((root / "checksums.sha256").read_bytes())
            independently_hashed = independent_file_hashes(root)
            for relative, digest in independently_hashed.items():
                if relative != "checksums.sha256":
                    assert digest in checksum_bytes[-1].decode("utf-8")
        assert checksum_bytes[0] == checksum_bytes[1]
    finally:
        _restore_write_permissions(tmp_path / "archive-a")
        _restore_write_permissions(tmp_path / "archive-b")


def test_archive_rejects_incomplete_attestation(tmp_path) -> None:
    manifest = _archive_manifest()
    manifest.pop("run_identity_sha256")
    with pytest.raises(ValueError, match="run_identity_sha256"):
        PilotArchiveWriter(tmp_path / "archive", manifest)


def test_archive_rejects_confirmatory_trajectory(
    tmp_path, bundle, params
) -> None:
    _, trajectory = _make_test_pilot_trajectory(bundle, params)
    confirmatory = replace(
        trajectory,
        config_id="p5-d01-c005",
        direction_id="d01",
        split="confirmatory",
    )
    writer = PilotArchiveWriter(tmp_path / "archive", _archive_manifest())
    with pytest.raises(ConfirmatoryAccessError):
        writer.write_trajectory(confirmatory)


def test_confirmatory_identifier_scanner_uses_structured_values(
    tmp_path,
) -> None:
    root = tmp_path / "archive"
    root.mkdir()
    (root / "manifest.json").write_text(
        json.dumps({"digest": "000d01000", "direction_id": "test-pilot"}),
        encoding="utf-8",
    )
    assert not archive_has_confirmatory_identifiers(root, {"d01"})
    (root / "forbidden.json").write_text(
        json.dumps({"direction_id": "d01"}),
        encoding="utf-8",
    )
    assert archive_has_confirmatory_identifiers(root, {"d01"})


def test_trajectory_rejects_nonfinite_mutation(bundle, params) -> None:
    _, trajectory = _make_test_pilot_trajectory(bundle, params)
    bad = trajectory.states.copy()
    bad[0, 0] = np.nan
    with pytest.raises(ValueError, match="non-finite"):
        replace(trajectory, states=bad)

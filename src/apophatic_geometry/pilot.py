"""Phase 6 pilot-only runner facade and gated execution orchestrator.

Importing or validating this module never executes a frozen pilot configuration.
The complete 50-configuration development pilot requires a separately committed
execution-authorization record at the fixed protocol path.
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

from .models import CONTRACT_VERSION, ModelId
from .pilot_archive import PilotArchiveWriter, archive_has_confirmatory_identifiers
from .pilot_integrate import (
    all_permutations,
    assess_numerics,
    exogenous_replay_control,
    integrate_dop853,
    integrate_rk4,
    inverse_permute_state,
    inverse_permute_state_trajectory,
    permute_state,
    require_constraint_gate,
    require_same_state_identity_gate,
    run_permutation_tripwires,
    same_state_identity_error,
)
from .pilot_manifest import (
    authorize_pilot_batch,
    build_pilot_configurations,
    configuration_payload,
    frozen_parameters,
    load_frozen_bundle,
    require_complete_pilot_batch,
    runtime_environment,
    smoke_configuration,
    validate_execution_authorization,
    verify_model_baseline,
)
from .pilot_types import (
    CONFIRMATORY_SPLIT,
    EXPECTED_PILOT_CONFIGURATIONS,
    EXPECTED_PILOT_DIRECTIONS,
    PILOT_SPLIT,
    RUNNER_ID,
    RUNNER_VERSION,
    ArchiveWriteResult,
    ConfirmatoryAccessError,
    ControlSpec,
    FrozenProtocolBundle,
    NumericalAssessment,
    NumericalGateError,
    PilotConfiguration,
    PilotRunnerError,
    ProtocolIntegrityError,
    Trajectory,
)
from .protocol import (
    PROTOCOL_ID,
    PROTOCOL_VERSION,
    max_abs_discrepancy,
    root_energy_ratio,
    symmetric_normalized_rms,
)


def pilot_plan(bundle: FrozenProtocolBundle) -> dict[str, Any]:
    """Return the exact pilot plan without integrating any trajectory."""

    configurations = build_pilot_configurations(bundle)
    return {
        "runner_id": RUNNER_ID,
        "runner_version": RUNNER_VERSION,
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "split": PILOT_SPLIT,
        "configuration_count": len(configurations),
        "direction_count": len({item.direction_id for item in configurations}),
        "configuration_ids": [item.config_id for item in configurations],
        "configuration_hashes": {
            item.config_id: item.configuration_hash for item in configurations
        },
        "canonical_models": [item.value for item in ModelId],
        "rk4_dts": bundle.protocol["time_and_sampling"]["refinement_dts"],
        "alternate_integrator_models": [item.value for item in ModelId],
        "controls": ["exogenous_replay", "freeze_s", "freeze_q", "freeze_sq"],
        "permutations": [list(value) for value in all_permutations()],
        "pilot_executed": False,
        "confirmatory_execution": "BLOCKED",
    }


def summarize_configuration(
    trajectories: dict[tuple[str, str], Trajectory],
    alternates: dict[str, Trajectory],
    dts: list[float],
) -> dict[str, Any]:
    """Compute frozen configuration-level effects and numerical floors."""

    fine_profile = f"rk4-dt-{dts[2]:.8g}"
    medium_profile = f"rk4-dt-{dts[1]:.8g}"
    required = {
        (model.value, fine_profile) for model in ModelId
    } | {
        (ModelId.MF.value, medium_profile),
        (ModelId.MP.value, medium_profile),
    }
    missing = required.difference(trajectories)
    if missing:
        raise ProtocolIntegrityError(f"configuration summary lacks trajectories: {sorted(missing)}")
    expected_alternates = {model.value for model in ModelId}
    if set(alternates) != expected_alternates:
        raise ProtocolIntegrityError("configuration summary lacks canonical alternate runs")

    m0 = trajectories[(ModelId.M0.value, fine_profile)]
    mf = trajectories[(ModelId.MF.value, fine_profile)]
    mp = trajectories[(ModelId.MP.value, fine_profile)]
    mfp = trajectories[(ModelId.MFP.value, fine_profile)]
    mf_medium = trajectories[(ModelId.MF.value, medium_profile)]
    mp_medium = trajectories[(ModelId.MP.value, medium_profile)]

    mf_num = max(
        symmetric_normalized_rms(mf_medium.states, mf.states),
        symmetric_normalized_rms(mf.states, alternates[ModelId.MF.value].states),
    )
    mp_num = max(
        symmetric_normalized_rms(mp_medium.states, mp.states),
        symmetric_normalized_rms(mp.states, alternates[ModelId.MP.value].states),
    )
    primary_floor = max(mf_num, mp_num)

    return {
        "primary": {
            "comparison": ["mf", "mp"],
            "observation_map": "full",
            "effect": symmetric_normalized_rms(mf.states, mp.states),
            "max_abs": max_abs_discrepancy(mf.states, mp.states),
            "configuration_numerical_floor": primary_floor,
            "model_numerical_floors": {"mf": mf_num, "mp": mp_num},
        },
        "secondary": {
            "h2_mp_mfp_x": symmetric_normalized_rms(
                mp.observation("x"), mfp.observation("x")
            ),
            "h3_m0_mf_full": symmetric_normalized_rms(m0.states, mf.states),
            "h4_m0_mp_full": symmetric_normalized_rms(m0.states, mp.states),
            "mf_mp_geometry": symmetric_normalized_rms(mf.geometry, mp.geometry),
            "mp_mfp_geometry": symmetric_normalized_rms(mp.geometry, mfp.geometry),
        },
        "mechanism_ratios": {
            "mf_feedback": root_energy_ratio(mf.feedback, mf.local_proposal),
            "mp_projection": root_energy_ratio(
                mp.projection_correction, mp.combined_proposal
            ),
            "mfp_feedback": root_energy_ratio(
                mfp.feedback, mfp.local_proposal
            ),
            "mfp_projection": root_energy_ratio(
                mfp.projection_correction, mfp.combined_proposal
            ),
        },
        "validity": {
            "mp_max_constraint_residual": float(
                max(abs(mp.constraint_residual).max(), abs(mp.post_constraint_residual).max())
            ),
            "mfp_max_constraint_residual": float(
                max(abs(mfp.constraint_residual).max(), abs(mfp.post_constraint_residual).max())
            ),
        },
    }


def execute_pilot(repo_root: str | Path, archive_root: str | Path) -> None:
    """Execute the frozen pilot only after the separate authorization gate.

    Phase 6 runner verification intentionally ships without the authorization
    record. Calling this function therefore fails before archive creation or
    integration until a later, explicit execution slice adds that record.
    """

    bundle = load_frozen_bundle(repo_root)
    source_commit = verify_model_baseline(bundle.repo_root, bundle.protocol)
    authorization = validate_execution_authorization(bundle.repo_root, source_commit)
    configurations = require_complete_pilot_batch(build_pilot_configurations(bundle))
    params = frozen_parameters(bundle)

    time_policy = bundle.protocol["time_and_sampling"]
    horizon = float(time_policy["horizon"])
    observation_interval = float(time_policy["observation_interval"])
    dts = [float(value) for value in time_policy["refinement_dts"]]
    if dts != [0.001, 0.0005, 0.00025]:
        raise ProtocolIntegrityError("RK4 schedule changed after protocol freeze")

    run_manifest = {
        "runner_id": RUNNER_ID,
        "runner_version": RUNNER_VERSION,
        "source_commit": source_commit,
        "model_implementation_commit": bundle.protocol["model_implementation_commit"],
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "contract_version": CONTRACT_VERSION,
        "execution_id": authorization["execution_id"],
        "execution_utc": authorization["execution_utc"],
        "split": PILOT_SPLIT,
        "configuration_count": len(configurations),
        "confirmatory_execution": "BLOCKED",
    }
    archive = PilotArchiveWriter(archive_root, run_manifest)
    archive.write_environment(runtime_environment())
    for configuration in configurations:
        archive.write_configuration(configuration)

    failures = 0
    for configuration in configurations:
        raw_hashes: dict[str, str] = {}
        trajectories: dict[tuple[str, str], Trajectory] = {}
        try:
            for model in ModelId:
                for dt in dts:
                    trajectory = integrate_rk4(
                        configuration,
                        params,
                        model,
                        dt=dt,
                        horizon=horizon,
                        observation_interval=observation_interval,
                        source_commit=source_commit,
                    )
                    require_constraint_gate(trajectory, configuration.c0)
                    require_same_state_identity_gate(
                        trajectory, params, configuration.c0
                    )
                    write = archive.write_trajectory(trajectory)
                    raw_hashes.update(write.files)
                    trajectories[(model.value, trajectory.profile)] = trajectory

            alternates: dict[str, Trajectory] = {}
            for model in ModelId:
                trajectory = integrate_dop853(
                    configuration,
                    params,
                    model,
                    horizon=horizon,
                    observation_interval=observation_interval,
                    source_commit=source_commit,
                )
                require_constraint_gate(trajectory, configuration.c0)
                require_same_state_identity_gate(
                    trajectory, params, configuration.c0
                )
                write = archive.write_trajectory(trajectory)
                raw_hashes.update(write.files)
                alternates[model.value] = trajectory

            assessments: dict[str, Any] = {}
            decision_maps = {
                ModelId.M0: ("full",),
                ModelId.MF: ("full",),
                ModelId.MP: ("full", "x"),
                ModelId.MFP: ("x",),
            }
            for model, maps in decision_maps.items():
                coarse = trajectories[(model.value, f"rk4-dt-{dts[0]:.8g}")]
                medium = trajectories[(model.value, f"rk4-dt-{dts[1]:.8g}")]
                fine = trajectories[(model.value, f"rk4-dt-{dts[2]:.8g}")]
                for map_id in maps:
                    assessment = assess_numerics(
                        coarse,
                        medium,
                        fine,
                        alternates[model.value],
                        map_id,
                    )
                    assessments[f"{model.value}:{map_id}"] = asdict(assessment) | {
                        "passed": assessment.passed
                    }
                    if not assessment.passed:
                        raise NumericalGateError(
                            f"numerical acceptance failed for {model.value}:{map_id}"
                        )

            mf_fine = trajectories[(ModelId.MF.value, f"rk4-dt-{dts[2]:.8g}")]
            replay = integrate_rk4(
                configuration,
                params,
                ModelId.MF,
                dt=dts[2],
                horizon=horizon,
                observation_interval=observation_interval,
                source_commit=source_commit,
                control=exogenous_replay_control(mf_fine),
            )
            raw_hashes.update(archive.write_trajectory(replay).files)

            for ablation in ("freeze_s", "freeze_q", "freeze_sq"):
                for model in ModelId:
                    controlled = integrate_rk4(
                        configuration,
                        params,
                        model,
                        dt=dts[0],
                        horizon=horizon,
                        observation_interval=observation_interval,
                        source_commit=source_commit,
                        control=ControlSpec(ablation=ablation),
                    )
                    require_constraint_gate(controlled, configuration.c0)
                    require_same_state_identity_gate(
                        controlled, params, configuration.c0
                    )
                    raw_hashes.update(archive.write_trajectory(controlled).files)

            permutation_results: dict[str, Any] = {}
            for model in ModelId:
                permutation_results[model.value] = run_permutation_tripwires(
                    configuration,
                    params,
                    model,
                    dt=dts[0],
                    horizon=horizon,
                    observation_interval=observation_interval,
                    source_commit=source_commit,
                    tolerance=1.0e-6,
                )

            effects = summarize_configuration(trajectories, alternates, dts)
            archive.write_summary(
                configuration.config_id,
                {
                    "config_id": configuration.config_id,
                    "direction_id": configuration.direction_id,
                    "split": configuration.split,
                    "configuration_hash": configuration.configuration_hash,
                    "effects": effects,
                    "numerical_assessments": assessments,
                    "permutation_tripwires": permutation_results,
                    "status": "ACCEPTED",
                },
                raw_hashes,
            )
        except Exception as exc:
            failures += 1
            archive.append_failure(
                {
                    "config_id": configuration.config_id,
                    "direction_id": configuration.direction_id,
                    "split": configuration.split,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
            if isinstance(exc, (ProtocolIntegrityError, ConfirmatoryAccessError)):
                raise
            if failures / len(configurations) > 0.10:
                raise NumericalGateError(
                    "pilot paused: more than 10% of configurations failed"
                ) from exc

    confirmatory_ids = {
        str(entry["direction_id"])
        for entry in bundle.initial_conditions["directions"]
        if entry["split"] == CONFIRMATORY_SPLIT
    }
    if archive_has_confirmatory_identifiers(archive.root, confirmatory_ids):
        raise ConfirmatoryAccessError("confirmatory identifier contamination detected")
    archive.finalize()


__all__ = [
    "ArchiveWriteResult",
    "CONFIRMATORY_SPLIT",
    "EXPECTED_PILOT_CONFIGURATIONS",
    "EXPECTED_PILOT_DIRECTIONS",
    "ConfirmatoryAccessError",
    "ControlSpec",
    "FrozenProtocolBundle",
    "NumericalAssessment",
    "NumericalGateError",
    "PILOT_SPLIT",
    "PilotArchiveWriter",
    "PilotConfiguration",
    "PilotRunnerError",
    "ProtocolIntegrityError",
    "RUNNER_ID",
    "RUNNER_VERSION",
    "Trajectory",
    "all_permutations",
    "archive_has_confirmatory_identifiers",
    "assess_numerics",
    "authorize_pilot_batch",
    "build_pilot_configurations",
    "configuration_payload",
    "execute_pilot",
    "exogenous_replay_control",
    "frozen_parameters",
    "integrate_dop853",
    "integrate_rk4",
    "inverse_permute_state",
    "inverse_permute_state_trajectory",
    "load_frozen_bundle",
    "permute_state",
    "pilot_plan",
    "require_complete_pilot_batch",
    "require_constraint_gate",
    "require_same_state_identity_gate",
    "run_permutation_tripwires",
    "same_state_identity_error",
    "smoke_configuration",
    "summarize_configuration",
    "validate_execution_authorization",
    "verify_model_baseline",
]

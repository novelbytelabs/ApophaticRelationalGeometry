"""Phase 6 pilot-only runner facade and gated execution orchestrator.

Importing or validating this module never executes a frozen pilot configuration.
Execution requires a separate committed authorization, a cleared external-audit
environment policy, a clean source tree, and a full execution attestation.
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

from .attestation import build_attestation
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
    smoke_configuration,
    validate_execution_authorization,
    validate_execution_environment_policy,
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
    canonical_json_sha256,
    load_json,
    max_abs_discrepancy,
    root_energy_ratio,
    symmetric_normalized_rms,
)

PILOT_IMPLEMENTATION_PATHS = (
    "src/apophatic_geometry/model.py",
    "src/apophatic_geometry/models.py",
    "src/apophatic_geometry/protocol.py",
    "src/apophatic_geometry/attestation.py",
    "src/apophatic_geometry/pilot_types.py",
    "src/apophatic_geometry/pilot_manifest.py",
    "src/apophatic_geometry/pilot_mechanisms.py",
    "src/apophatic_geometry/pilot_integrators.py",
    "src/apophatic_geometry/pilot_gates.py",
    "src/apophatic_geometry/pilot_integrate.py",
    "src/apophatic_geometry/pilot_archive.py",
    "src/apophatic_geometry/pilot.py",
    "src/apophatic_geometry/pilot_cli.py",
    "protocol/phase5_v1/LOCK.json",
    "protocol/phase6_runner_v1/INTEGRITY_BASELINE.json",
    "protocol/phase6_runner_v1/EXECUTION_ENVIRONMENT.json",
)
PILOT_INTEGRATOR_SUITE = "rk4-refinement-plus-segmented-dop853-v1"
EXPECTED_TRAJECTORIES_PER_CONFIGURATION = 29


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
    required = {(model.value, fine_profile) for model in ModelId} | {
        (ModelId.MF.value, medium_profile),
        (ModelId.MP.value, medium_profile),
    }
    missing = required.difference(trajectories)
    if missing:
        raise ProtocolIntegrityError(
            f"configuration summary lacks trajectories: {sorted(missing)}"
        )
    expected_alternates = {model.value for model in ModelId}
    if set(alternates) != expected_alternates:
        raise ProtocolIntegrityError(
            "configuration summary lacks canonical alternate runs"
        )

    m0 = trajectories[(ModelId.M0.value, fine_profile)]
    mf = trajectories[(ModelId.MF.value, fine_profile)]
    mp = trajectories[(ModelId.MP.value, fine_profile)]
    mfp = trajectories[(ModelId.MFP.value, fine_profile)]
    mf_medium = trajectories[(ModelId.MF.value, medium_profile)]
    mp_medium = trajectories[(ModelId.MP.value, medium_profile)]

    mf_num = max(
        symmetric_normalized_rms(mf_medium.states, mf.states),
        symmetric_normalized_rms(
            mf.states, alternates[ModelId.MF.value].states
        ),
    )
    mp_num = max(
        symmetric_normalized_rms(mp_medium.states, mp.states),
        symmetric_normalized_rms(
            mp.states, alternates[ModelId.MP.value].states
        ),
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
            "mf_mp_geometry": symmetric_normalized_rms(
                mf.geometry, mp.geometry
            ),
            "mp_mfp_geometry": symmetric_normalized_rms(
                mp.geometry, mfp.geometry
            ),
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
                max(
                    abs(mp.constraint_residual).max(),
                    abs(mp.post_constraint_residual).max(),
                )
            ),
            "mfp_max_constraint_residual": float(
                max(
                    abs(mfp.constraint_residual).max(),
                    abs(mfp.post_constraint_residual).max(),
                )
            ),
        },
    }


def execute_pilot(repo_root: str | Path, archive_root: str | Path) -> None:
    """Execute the frozen pilot only after every independent gate passes."""

    bundle = load_frozen_bundle(repo_root)
    source_commit = verify_model_baseline(bundle.repo_root, bundle.protocol)
    configurations = require_complete_pilot_batch(
        build_pilot_configurations(bundle)
    )
    configuration_hashes = {
        item.config_id: item.configuration_hash for item in configurations
    }
    expected_trajectory_records = (
        len(configurations) * EXPECTED_TRAJECTORIES_PER_CONFIGURATION
    )
    expected_scope = {
        "scope_version": "ARG-P6-EXEC-SCOPE-v2",
        "protocol_lock_sha256": canonical_json_sha256(
            load_json(bundle.repo_root / "protocol/phase5_v1/LOCK.json")
        ),
        "integrity_baseline_sha256": canonical_json_sha256(
            load_json(
                bundle.repo_root
                / "protocol/phase6_runner_v1/INTEGRITY_BASELINE.json"
            )
        ),
        "execution_environment_sha256": canonical_json_sha256(
            load_json(
                bundle.repo_root
                / "protocol/phase6_runner_v1/EXECUTION_ENVIRONMENT.json"
            )
        ),
        "pilot_membership_sha256": canonical_json_sha256(
            configuration_hashes
        ),
        "integrator_suite": PILOT_INTEGRATOR_SUITE,
        "archive_schema_version": "ARG-P6-ARCHIVE-v2",
        "configuration_count": len(configurations),
        "expected_trajectory_records": expected_trajectory_records,
        "expected_summary_records": len(configurations),
        "confirmatory_execution": "BLOCKED",
    }
    authorization = validate_execution_authorization(
        bundle.repo_root,
        source_commit,
        expected_scope=expected_scope,
    )
    params = frozen_parameters(bundle)

    attestation = build_attestation(
        bundle.repo_root,
        integrator=PILOT_INTEGRATOR_SUITE,
        implementation_paths=PILOT_IMPLEMENTATION_PATHS,
    )
    if attestation.get("source_commit") != source_commit:
        raise ProtocolIntegrityError(
            "source commit differs between runner and attestation gates"
        )
    environment = attestation.get("runtime_environment")
    if not isinstance(environment, dict):
        raise ProtocolIntegrityError("runtime environment attestation is missing")
    environment_policy = validate_execution_environment_policy(
        bundle.repo_root,
        environment,
        require_execution_clearance=True,
    )

    time_policy = bundle.protocol["time_and_sampling"]
    horizon = float(time_policy["horizon"])
    observation_interval = float(time_policy["observation_interval"])
    dts = [float(value) for value in time_policy["refinement_dts"]]
    if dts != [0.001, 0.0005, 0.00025]:
        raise ProtocolIntegrityError("RK4 schedule changed after protocol freeze")

    run_identity_payload = {
        "authorization": dict(authorization),
        "attestation_sha256": attestation["attestation_sha256"],
        "environment_policy_id": environment_policy["environment_id"],
        "configuration_hashes": {
            item.config_id: item.configuration_hash for item in configurations
        },
        "integrator_suite": PILOT_INTEGRATOR_SUITE,
    }
    run_identity_sha256 = canonical_json_sha256(run_identity_payload)
    run_manifest = {
        "runner_id": RUNNER_ID,
        "runner_version": RUNNER_VERSION,
        "source_commit": source_commit,
        "source_tree_sha256": attestation["source_tree_sha256"],
        "attestation_sha256": attestation["attestation_sha256"],
        "protocol_lock": attestation["protocol_lock"],
        "implementation_files": attestation["implementation_files"],
        "runtime_environment_sha256": attestation[
            "runtime_environment_sha256"
        ],
        "environment_policy_id": environment_policy["environment_id"],
        "integrator_suite": PILOT_INTEGRATOR_SUITE,
        "run_identity_sha256": run_identity_sha256,
        "model_implementation_commit": bundle.protocol[
            "model_implementation_commit"
        ],
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "contract_version": CONTRACT_VERSION,
        "execution_id": authorization["execution_id"],
        "execution_utc": authorization["execution_utc"],
        "split": PILOT_SPLIT,
        "configuration_count": len(configurations),
        "configuration_hashes": configuration_hashes,
        "execution_scope": expected_scope,
        "execution_scope_sha256": canonical_json_sha256(expected_scope),
        "expected_trajectory_records": expected_trajectory_records,
        "expected_summary_records": len(configurations),
        "confirmatory_execution": "BLOCKED",
    }
    archive = PilotArchiveWriter(archive_root, run_manifest)
    archive.write_environment(
        {
            "policy": dict(environment_policy),
            "attested_runtime": environment,
            "runtime_environment_sha256": attestation[
                "runtime_environment_sha256"
            ],
        }
    )
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
                coarse = trajectories[
                    (model.value, f"rk4-dt-{dts[0]:.8g}")
                ]
                medium = trajectories[
                    (model.value, f"rk4-dt-{dts[1]:.8g}")
                ]
                fine = trajectories[
                    (model.value, f"rk4-dt-{dts[2]:.8g}")
                ]
                for map_id in maps:
                    assessment = assess_numerics(
                        coarse,
                        medium,
                        fine,
                        alternates[model.value],
                        map_id,
                    )
                    assessments[f"{model.value}:{map_id}"] = asdict(
                        assessment
                    ) | {"passed": assessment.passed}
                    if not assessment.passed:
                        raise NumericalGateError(
                            "numerical acceptance failed for "
                            f"{model.value}:{map_id}"
                        )

            mf_fine = trajectories[
                (ModelId.MF.value, f"rk4-dt-{dts[2]:.8g}")
            ]
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
                    raw_hashes.update(
                        archive.write_trajectory(controlled).files
                    )

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
                    "run_identity_sha256": run_identity_sha256,
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
                    "run_identity_sha256": run_identity_sha256,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
            if isinstance(
                exc, (ProtocolIntegrityError, ConfirmatoryAccessError)
            ):
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
        raise ConfirmatoryAccessError(
            "confirmatory identifier contamination detected"
        )
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
    "validate_execution_environment_policy",
    "verify_model_baseline",
]

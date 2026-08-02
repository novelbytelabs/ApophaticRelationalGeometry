"""Numerical, invariant, and relabeling gates for the Phase 6 runner."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

import numpy as np
from numpy.typing import NDArray

from .model import EDGES, Parameters, State
from .models import ModelId, ProjectionTarget, combined_projected_derivative, projected_derivative
from .pilot_integrators import _integrate_rk4_unchecked
from .pilot_manifest import configuration_payload, require_frozen_configuration
from .pilot_mechanisms import all_permutations
from .pilot_types import FrozenProtocolBundle, NumericalAssessment, NumericalGateError, PilotConfiguration, Trajectory
from .protocol import canonical_json_sha256, max_abs_discrepancy, symmetric_normalized_rms

FloatArray = NDArray[np.float64]
H6_POLICY_ID = "ARG-H6-CONDITION-AWARE-v2"
_EDGE_TO_INDEX = {edge: index for index, edge in enumerate(EDGES)}
_H6_RELATIVE_TOLERANCE = 1.0e-12
_H6_BACKWARD_TOLERANCE = 128.0 * np.finfo(np.float64).eps
_H6_CONDITIONING_THRESHOLD = (
    _H6_BACKWARD_TOLERANCE / _H6_RELATIVE_TOLERANCE
)


@dataclass(frozen=True)
class SameStateIdentityAssessment:
    """Condition-aware diagnostics for the exact same-state node identity."""

    regime: str
    absolute_error: float
    forward_relative_error: float
    backward_error: float
    radiality_error: float
    conditioning_ratio: float
    signal_scale: float
    input_scale: float
    identity_pass: bool
    radiality_pass: bool

    @property
    def passed(self) -> bool:
        return self.identity_pass and self.radiality_pass


def assess_numerics(
    coarse: Trajectory,
    medium: Trajectory,
    fine: Trajectory,
    alternate: Trajectory,
    map_id: str,
) -> NumericalAssessment:
    """Apply frozen refinement, endpoint, and alternate-integrator gates."""

    labels = {
        (item.config_id, item.model_id, item.control_id)
        for item in (coarse, medium, fine, alternate)
    }
    if len(labels) != 1:
        raise ValueError("numerical assessment trajectories are not matched")
    for candidate in (medium, fine, alternate):
        if not np.array_equal(candidate.times, coarse.times):
            raise ValueError("numerical assessment observation grids differ")
    coarse_medium = symmetric_normalized_rms(
        coarse.observation(map_id), medium.observation(map_id)
    )
    medium_fine = symmetric_normalized_rms(
        medium.observation(map_id), fine.observation(map_id)
    )
    fine_alternate = symmetric_normalized_rms(
        fine.observation(map_id), alternate.observation(map_id)
    )
    endpoint_error = max_abs_discrepancy(
        medium.observation(map_id)[-1],
        fine.observation(map_id)[-1],
    )
    endpoint_limit = 1.0e-6 + 1.0e-5 * float(
        np.max(np.abs(fine.observation(map_id)[-1]))
    )
    alternate_limit = max(1.0e-5, 10.0 * medium_fine)
    return NumericalAssessment(
        map_id=map_id,
        coarse_medium=coarse_medium,
        medium_fine=medium_fine,
        fine_alternate=fine_alternate,
        endpoint_error=endpoint_error,
        endpoint_limit=endpoint_limit,
        refinement_pass=medium_fine < coarse_medium,
        endpoint_pass=endpoint_error <= endpoint_limit,
        alternate_pass=fine_alternate <= alternate_limit,
    )


def require_constraint_gate(trajectory: Trajectory, c0: float) -> None:
    if trajectory.model_id not in {ModelId.MP.value, ModelId.MFP.value}:
        return
    tolerance = 1.0e-12 * max(1.0, float(c0))
    if trajectory.post_constraint_residual.size:
        if float(np.max(np.abs(trajectory.post_constraint_residual))) > tolerance:
            raise NumericalGateError("H5 post-retraction constraint gate failed")
    if float(np.max(np.abs(trajectory.constraint_residual))) > tolerance:
        raise NumericalGateError("H5 sampled-state constraint gate failed")


def _dot3(left: FloatArray, right: FloatArray) -> float:
    return float(
        math.fsum(float(left[index]) * float(right[index]) for index in range(3))
    )


def same_state_identity_assessment(
    state: State,
    params: Parameters,
    c0: float,
) -> SameStateIdentityAssessment:
    """Assess H6 without dividing machine residuals by a vanishing signal.

    The exact identity is structural: MFP adds a radial node-feedback vector,
    which the tangent projector annihilates. A forward-relative comparison is
    meaningful only while the projected derivative is not cancellation
    dominated. Near a projected equilibrium, the gate switches to a
    dimensionless backward-error bound derived from binary64 precision.
    """

    target = ProjectionTarget(c0)
    mp_diagnostics = projected_derivative(state, params, target)
    mfp_diagnostics = combined_projected_derivative(state, params, target)
    mp = mp_diagnostics.projected.x
    mfp = mfp_diagnostics.projected.x

    absolute_error = float(np.linalg.norm(mp - mfp))
    signal_scale = float(np.linalg.norm(mp) + np.linalg.norm(mfp))
    input_scale = max(
        float(np.linalg.norm(mfp_diagnostics.local_proposal.x)),
        float(np.linalg.norm(mfp_diagnostics.proposal.x)),
        float(np.linalg.norm(mfp_diagnostics.feedback.x)),
        np.finfo(np.float64).tiny,
    )
    forward_relative_error = absolute_error / max(
        signal_scale, np.finfo(np.float64).tiny
    )
    backward_error = absolute_error / input_scale
    conditioning_ratio = signal_scale / input_scale

    feedback = mfp_diagnostics.feedback.x
    feedback_norm = float(np.linalg.norm(feedback))
    denominator = _dot3(state.x, state.x)
    radial_coefficient = _dot3(state.x, feedback) / denominator
    radial_residual = float(
        np.linalg.norm(feedback - radial_coefficient * state.x)
    )
    if feedback_norm == 0.0:
        radiality_error = 0.0 if radial_residual == 0.0 else math.inf
    else:
        radiality_error = radial_residual / feedback_norm

    well_conditioned = conditioning_ratio >= _H6_CONDITIONING_THRESHOLD
    regime = "well_conditioned" if well_conditioned else "cancellation_dominated"
    identity_pass = (
        forward_relative_error <= _H6_RELATIVE_TOLERANCE
        if well_conditioned
        else backward_error <= _H6_BACKWARD_TOLERANCE
    )
    radiality_pass = radiality_error <= _H6_BACKWARD_TOLERANCE

    return SameStateIdentityAssessment(
        regime=regime,
        absolute_error=absolute_error,
        forward_relative_error=forward_relative_error,
        backward_error=backward_error,
        radiality_error=radiality_error,
        conditioning_ratio=conditioning_ratio,
        signal_scale=signal_scale,
        input_scale=input_scale,
        identity_pass=identity_pass,
        radiality_pass=radiality_pass,
    )


def same_state_identity_error(state: State, params: Parameters, c0: float) -> float:
    """Return the legacy forward-relative H6 diagnostic.

    This value remains available for reporting, but the gate no longer treats
    it as well-conditioned when both projected derivatives approach zero.
    """

    return same_state_identity_assessment(
        state, params, c0
    ).forward_relative_error


def _h6_failure_ratio(assessment: SameStateIdentityAssessment) -> float:
    identity_ratio = (
        assessment.forward_relative_error / _H6_RELATIVE_TOLERANCE
        if assessment.regime == "well_conditioned"
        else assessment.backward_error / _H6_BACKWARD_TOLERANCE
    )
    radial_ratio = assessment.radiality_error / _H6_BACKWARD_TOLERANCE
    return max(identity_ratio, radial_ratio)


def require_same_state_identity_gate(
    trajectory: Trajectory,
    params: Parameters,
    c0: float,
) -> SameStateIdentityAssessment | None:
    if trajectory.model_id not in {ModelId.MP.value, ModelId.MFP.value}:
        return None
    assessments = [
        same_state_identity_assessment(State.unpack(vector), params, c0)
        for vector in trajectory.states
    ]
    worst = max(assessments, key=_h6_failure_ratio)
    if not worst.passed:
        raise NumericalGateError(
            "H6 same-state node identity gate failed: "
            f"regime={worst.regime}, "
            f"absolute_error={worst.absolute_error}, "
            f"forward_relative_error={worst.forward_relative_error}, "
            f"backward_error={worst.backward_error}, "
            f"radiality_error={worst.radiality_error}, "
            f"conditioning_ratio={worst.conditioning_ratio}"
        )
    return worst


def _validate_permutation(permutation: Sequence[int]) -> tuple[int, int, int]:
    value = tuple(int(index) for index in permutation)
    if len(value) != 3 or set(value) != {0, 1, 2}:
        raise ValueError("node permutation must contain 0,1,2 exactly once")
    return value


def permute_state(state: State, permutation: Sequence[int]) -> State:
    """Relabel nodes; new node i carries old node permutation[i]."""

    p = _validate_permutation(permutation)
    x = state.x[list(p)]
    s = np.empty(3, dtype=np.float64)
    q = np.empty(3, dtype=np.float64)
    for new_edge_index, (i, j) in enumerate(EDGES):
        old_edge_index = _EDGE_TO_INDEX[tuple(sorted((p[i], p[j])))]
        s[new_edge_index] = state.s[old_edge_index]
        q[new_edge_index] = state.q[old_edge_index]
    return State(x=x, s=s, q=q)


def inverse_permute_state(state: State, permutation: Sequence[int]) -> State:
    p = _validate_permutation(permutation)
    inverse = [0, 0, 0]
    for new_index, old_index in enumerate(p):
        inverse[old_index] = new_index
    return permute_state(state, inverse)


def inverse_permute_state_trajectory(
    states: FloatArray,
    permutation: Sequence[int],
) -> FloatArray:
    array = np.asarray(states, dtype=np.float64)
    if array.ndim != 2 or array.shape[1] != 9:
        raise ValueError("state trajectory must have shape (n,9)")
    if not np.all(np.isfinite(array)):
        raise ValueError("state trajectory contains non-finite values")
    result = np.empty_like(array)
    for index, vector in enumerate(array):
        result[index] = inverse_permute_state(
            State.unpack(vector), permutation
        ).pack()
    return result


def run_permutation_tripwires(
    configuration: PilotConfiguration,
    params: Parameters,
    model: ModelId | str,
    *,
    bundle: FrozenProtocolBundle | None = None,
    dt: float,
    horizon: float,
    observation_interval: float,
    source_commit: str,
    tolerance: float,
) -> dict[str, float]:
    """Execute all six relabelings and compare after inverse permutation."""

    if tolerance <= 0.0 or not np.isfinite(tolerance):
        raise ValueError("permutation tolerance must be finite and positive")
    if configuration.split == "pilot":
        if bundle is None:
            raise ValueError("pilot permutation checks require frozen membership")
        require_frozen_configuration(bundle, configuration)
    elif bundle is not None:
        require_frozen_configuration(bundle, configuration)
    base = _integrate_rk4_unchecked(
        configuration,
        params,
        model,
        dt=dt,
        horizon=horizon,
        observation_interval=observation_interval,
        source_commit=source_commit,
    )
    results: dict[str, float] = {}
    for permutation in all_permutations():
        permuted_state = permute_state(configuration.initial_state, permutation)
        payload = configuration_payload(
            configuration.config_id,
            configuration.direction_id,
            configuration.split,
            configuration.c0,
            permuted_state,
        )
        permuted_config = PilotConfiguration(
            config_id=configuration.config_id,
            direction_id=configuration.direction_id,
            split=configuration.split,
            c0=configuration.c0,
            initial_state=permuted_state,
            configuration_hash=canonical_json_sha256(payload),
        )
        candidate = _integrate_rk4_unchecked(
            permuted_config,
            params,
            model,
            dt=dt,
            horizon=horizon,
            observation_interval=observation_interval,
            source_commit=source_commit,
        )
        restored = inverse_permute_state_trajectory(candidate.states, permutation)
        error = max_abs_discrepancy(base.states, restored)
        key = "".join(str(index) for index in permutation)
        results[key] = error
        if error > tolerance:
            raise NumericalGateError(
                f"permutation tripwire {key} failed with discrepancy {error}"
            )
    return results

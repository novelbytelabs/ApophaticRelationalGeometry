"""Numerical, invariant, and relabeling gates for the Phase 6 runner."""

from __future__ import annotations

from typing import Sequence
import numpy as np
from numpy.typing import NDArray

from .model import EDGES, Parameters, State
from .models import ModelId, ProjectionTarget, combined_projected_derivative, projected_derivative
from .pilot_integrators import integrate_rk4
from .pilot_manifest import configuration_payload
from .pilot_mechanisms import all_permutations
from .pilot_types import NumericalAssessment, NumericalGateError, PilotConfiguration, Trajectory
from .protocol import canonical_json_sha256, max_abs_discrepancy, symmetric_normalized_rms

FloatArray = NDArray[np.float64]
_EDGE_TO_INDEX = {edge: index for index, edge in enumerate(EDGES)}


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


def same_state_identity_error(state: State, params: Parameters, c0: float) -> float:
    target = ProjectionTarget(c0)
    mp = projected_derivative(state, params, target).projected.x
    mfp = combined_projected_derivative(state, params, target).projected.x
    return float(
        np.linalg.norm(mp - mfp)
        / (np.linalg.norm(mp) + np.linalg.norm(mfp) + 1.0e-30)
    )


def require_same_state_identity_gate(
    trajectory: Trajectory,
    params: Parameters,
    c0: float,
) -> None:
    if trajectory.model_id not in {ModelId.MP.value, ModelId.MFP.value}:
        return
    maximum = max(
        same_state_identity_error(State.unpack(vector), params, c0)
        for vector in trajectory.states
    )
    if maximum > 1.0e-12:
        raise NumericalGateError(f"H6 same-state node identity gate failed: {maximum}")


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
    dt: float,
    horizon: float,
    observation_interval: float,
    source_commit: str,
    tolerance: float,
) -> dict[str, float]:
    """Execute all six relabelings and compare after inverse permutation."""

    if tolerance <= 0.0 or not np.isfinite(tolerance):
        raise ValueError("permutation tolerance must be finite and positive")
    base = integrate_rk4(
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
        candidate = integrate_rk4(
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

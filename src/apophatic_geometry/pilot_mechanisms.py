"""Mechanism decomposition and low-level stepping for the Phase 6 runner."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from .model import Parameters, State, intrinsic_distance_matrix
from .models import (
    ModelId, ProjectionTarget, combined_projected_rk4_step, constraint_residual,
    feedback_vector, local_adaptive_derivatives, project_node_derivative,
    projected_rk4_step, retract_to_constraint, rk4_step,
)
from .pilot_types import ALLOWED_ABLATIONS, ControlSpec, NumericalGateError, PilotConfiguration, Trajectory

FloatArray = NDArray[np.float64]

def all_permutations() -> tuple[tuple[int, int, int], ...]:
    return (
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    )


def _feedback_from_c(state: State, params: Parameters, c_value: float) -> State:
    c = float(c_value)
    if not np.isfinite(c) or c < 0.0:
        raise FloatingPointError("invalid exogenous collective statistic")
    return State(
        x=-params.chi * c * state.x,
        s=np.full(3, params.eta_2 * c / params.tau_s, dtype=np.float64),
        q=np.full(3, -params.rho * c / params.tau_q, dtype=np.float64),
    )


def _apply_ablation(derivative: State, ablation: str | None) -> State:
    if ablation not in ALLOWED_ABLATIONS:
        raise ValueError(f"unsupported ablation: {ablation}")
    ds = derivative.s.copy()
    dq = derivative.q.copy()
    if ablation in {"freeze_s", "freeze_sq"}:
        ds.fill(0.0)
    if ablation in {"freeze_q", "freeze_sq"}:
        dq.fill(0.0)
    return State(x=derivative.x.copy(), s=ds, q=dq)


def _c_override(control: ControlSpec, time: float) -> float | None:
    if control.exogenous_times is None or control.exogenous_c is None:
        return None
    if time < control.exogenous_times[0] - 1.0e-15:
        raise NumericalGateError("exogenous replay requested before signal domain")
    if time > control.exogenous_times[-1] + 1.0e-15:
        raise NumericalGateError("exogenous replay requested after signal domain")
    return float(np.interp(time, control.exogenous_times, control.exogenous_c))


def _mechanism_components(
    state: State,
    params: Parameters,
    model: ModelId,
    target: ProjectionTarget | None,
    control: ControlSpec,
    time: float,
) -> tuple[State, State, State, State, State, float, float, float]:
    local = _apply_ablation(local_adaptive_derivatives(state, params), control.ablation)
    feedback = State(
        x=np.zeros(3, dtype=np.float64),
        s=np.zeros(3, dtype=np.float64),
        q=np.zeros(3, dtype=np.float64),
    )
    if model in {ModelId.MF, ModelId.MFP}:
        override = _c_override(control, time)
        raw_feedback = (
            feedback_vector(state, params)
            if override is None
            else _feedback_from_c(state, params, override)
        )
        feedback = _apply_ablation(raw_feedback, control.ablation)
    elif control.exogenous_times is not None:
        raise ValueError("exogenous replay is defined only for feedback-bearing models")

    proposal = State(
        x=local.x + feedback.x,
        s=local.s + feedback.s,
        q=local.q + feedback.q,
    )
    correction = State(
        x=np.zeros(3, dtype=np.float64),
        s=np.zeros(3, dtype=np.float64),
        q=np.zeros(3, dtype=np.float64),
    )
    projected = proposal
    residual = 0.0
    tangency = 0.0
    denominator = 0.0
    if model in {ModelId.MP, ModelId.MFP}:
        if target is None:
            raise ValueError("projected mechanism snapshot requires a target")
        projected_x, correction_x, tangency, denominator = project_node_derivative(
            state.x,
            proposal.x,
            target,
        )
        correction = State(
            x=correction_x,
            s=np.zeros(3, dtype=np.float64),
            q=np.zeros(3, dtype=np.float64),
        )
        projected = State(x=projected_x, s=proposal.s.copy(), q=proposal.q.copy())
        residual = constraint_residual(state, target)
    return local, feedback, proposal, correction, projected, residual, tangency, denominator


def _controlled_derivative(
    time: float,
    state: State,
    params: Parameters,
    model: ModelId,
    target: ProjectionTarget | None,
    control: ControlSpec,
) -> State:
    return _mechanism_components(state, params, model, target, control, time)[4]


def _controlled_rk4_step(
    time: float,
    state: State,
    params: Parameters,
    dt: float,
    model: ModelId,
    target: ProjectionTarget | None,
    control: ControlSpec,
) -> tuple[State, float, float, float]:
    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")
    if model in {ModelId.MP, ModelId.MFP}:
        if target is None:
            raise ValueError("projected controlled step requires a target")
        tolerance = 1.0e-12 * max(1.0, target.c0)
        if abs(constraint_residual(state, target)) > tolerance:
            raise NumericalGateError("controlled projected step started off manifold")

    y0 = state.pack()

    def rhs(stage_time: float, vector: FloatArray) -> FloatArray:
        return _controlled_derivative(
            stage_time,
            State.unpack(vector),
            params,
            model,
            target,
            control,
        ).pack()

    k1 = rhs(time, y0)
    k2 = rhs(time + 0.5 * dt, y0 + 0.5 * dt * k1)
    k3 = rhs(time + 0.5 * dt, y0 + 0.5 * dt * k2)
    k4 = rhs(time + dt, y0 + dt * k3)
    raw = State.unpack(y0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4))
    if model in {ModelId.MP, ModelId.MFP}:
        assert target is not None
        retraction = retract_to_constraint(raw, target)
        return (
            retraction.state,
            retraction.raw_constraint_residual,
            retraction.post_constraint_residual,
            retraction.magnitude,
        )
    return raw, 0.0, 0.0, 0.0


def _canonical_step(
    state: State,
    params: Parameters,
    dt: float,
    model: ModelId,
    target: ProjectionTarget | None,
) -> tuple[State, float, float, float]:
    if model is ModelId.MP:
        if target is None:
            raise ValueError("MP requires target")
        result = projected_rk4_step(state, params, dt, target)
        return (
            result.state,
            result.raw_constraint_residual,
            result.post_constraint_residual,
            result.retraction_magnitude,
        )
    if model is ModelId.MFP:
        if target is None:
            raise ValueError("MFP requires target")
        result = combined_projected_rk4_step(state, params, dt, target)
        return (
            result.state,
            result.raw_constraint_residual,
            result.post_constraint_residual,
            result.retraction_magnitude,
        )
    return rk4_step(state, params, dt, model=model), 0.0, 0.0, 0.0


def _validate_time_grid(
    horizon: float,
    observation_interval: float,
    dt: float,
) -> tuple[int, int, int]:
    for name, value in (
        ("horizon", horizon),
        ("observation_interval", observation_interval),
        ("dt", dt),
    ):
        if not np.isfinite(value) or value <= 0.0:
            raise ValueError(f"{name} must be finite and positive")
    steps = int(round(horizon / dt))
    stride = int(round(observation_interval / dt))
    observations = int(round(horizon / observation_interval)) + 1
    if not np.isclose(steps * dt, horizon, rtol=0.0, atol=1.0e-12):
        raise ValueError("horizon must be an integer multiple of dt")
    if stride <= 0 or not np.isclose(
        stride * dt, observation_interval, rtol=0.0, atol=1.0e-12
    ):
        raise ValueError("observation interval must be an integer multiple of dt")
    if steps // stride + 1 != observations:
        raise ValueError("inconsistent observation grid")
    return steps, stride, observations


def _record_observation(
    index: int,
    time: float,
    state: State,
    params: Parameters,
    model: ModelId,
    target: ProjectionTarget | None,
    control: ControlSpec,
    arrays: dict[str, FloatArray],
) -> None:
    components = _mechanism_components(state, params, model, target, control, time)
    arrays["states"][index] = state.pack()
    distances = intrinsic_distance_matrix(state, params)
    arrays["geometry"][index] = np.array(
        [distances[0, 1], distances[0, 2], distances[1, 2]],
        dtype=np.float64,
    )
    arrays["local"][index] = components[0].pack()
    arrays["feedback"][index] = components[1].pack()
    arrays["proposal"][index] = components[2].pack()
    arrays["correction"][index] = components[3].pack()
    arrays["residual"][index] = components[5]
    arrays["tangency"][index] = components[6]
    arrays["denominator"][index] = components[7]


def _observation_arrays(nobs: int) -> dict[str, FloatArray]:
    return {
        "states": np.empty((nobs, 9), dtype=np.float64),
        "geometry": np.empty((nobs, 3), dtype=np.float64),
        "local": np.empty((nobs, 9), dtype=np.float64),
        "feedback": np.empty((nobs, 9), dtype=np.float64),
        "proposal": np.empty((nobs, 9), dtype=np.float64),
        "correction": np.empty((nobs, 9), dtype=np.float64),
        "residual": np.empty(nobs, dtype=np.float64),
        "tangency": np.empty(nobs, dtype=np.float64),
        "denominator": np.empty(nobs, dtype=np.float64),
    }


def _trajectory(
    configuration: PilotConfiguration,
    model: ModelId,
    source_commit: str,
    times: FloatArray,
    arrays: dict[str, FloatArray],
    step_times: FloatArray,
    raw: FloatArray,
    post: FloatArray,
    retraction: FloatArray,
    *,
    integrator: str,
    profile: str,
    control_id: str,
) -> Trajectory:
    return Trajectory(
        config_id=configuration.config_id,
        direction_id=configuration.direction_id,
        split=configuration.split,
        model_id=model.value,
        integrator=integrator,
        profile=profile,
        control_id=control_id,
        source_commit=source_commit,
        times=times,
        states=arrays["states"],
        geometry=arrays["geometry"],
        local_proposal=arrays["local"],
        feedback=arrays["feedback"],
        combined_proposal=arrays["proposal"],
        projection_correction=arrays["correction"],
        constraint_residual=arrays["residual"],
        tangency_residual=arrays["tangency"],
        denominator=arrays["denominator"],
        step_times=step_times,
        raw_constraint_residual=raw,
        post_constraint_residual=post,
        retraction_magnitude=retraction,
    )

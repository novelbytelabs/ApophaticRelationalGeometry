"""RK4 and DOP853 trajectory integration for pilot and smoke configurations."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from scipy.integrate import solve_ivp

from .model import Parameters, State
from .models import ModelId, ProjectionTarget, derivatives_for_model, parse_model_id, retract_to_constraint
from .pilot_mechanisms import (
    _canonical_step, _controlled_rk4_step, _observation_arrays, _record_observation,
    _trajectory, _validate_time_grid,
)
from .pilot_types import (
    CONFIRMATORY_SPLIT, PILOT_SPLIT, SMOKE_SPLIT, ConfirmatoryAccessError,
    ControlSpec, NumericalGateError, PilotConfiguration, Trajectory,
)

FloatArray = NDArray[np.float64]


def integrate_rk4(
    configuration: PilotConfiguration,
    params: Parameters,
    model: ModelId | str,
    *,
    dt: float,
    horizon: float,
    observation_interval: float,
    source_commit: str,
    control: ControlSpec | None = None,
) -> Trajectory:
    """Integrate one pilot or smoke configuration with fixed-step RK4."""

    model_id = parse_model_id(model)
    control = control or ControlSpec()
    if configuration.split == CONFIRMATORY_SPLIT:
        raise ConfirmatoryAccessError("confirmatory trajectory generation is forbidden")
    if configuration.split not in {PILOT_SPLIT, SMOKE_SPLIT}:
        raise ConfirmatoryAccessError("unsupported execution split")
    steps, stride, nobs = _validate_time_grid(horizon, observation_interval, dt)
    state = configuration.initial_state
    target = (
        ProjectionTarget(configuration.c0)
        if model_id in {ModelId.MP, ModelId.MFP}
        else None
    )
    times = np.linspace(0.0, horizon, nobs, dtype=np.float64)
    arrays = _observation_arrays(nobs)
    step_times = np.arange(1, steps + 1, dtype=np.float64) * dt
    raw = np.zeros(steps, dtype=np.float64)
    post = np.zeros(steps, dtype=np.float64)
    retraction = np.zeros(steps, dtype=np.float64)
    _record_observation(0, 0.0, state, params, model_id, target, control, arrays)

    obs_index = 1
    canonical = control.id == "canonical"
    for step_index in range(steps):
        time = step_index * dt
        if canonical:
            state, raw_value, post_value, magnitude = _canonical_step(
                state, params, dt, model_id, target
            )
        else:
            state, raw_value, post_value, magnitude = _controlled_rk4_step(
                time, state, params, dt, model_id, target, control
            )
        raw[step_index] = raw_value
        post[step_index] = post_value
        retraction[step_index] = magnitude
        if (step_index + 1) % stride == 0:
            _record_observation(
                obs_index,
                (step_index + 1) * dt,
                state,
                params,
                model_id,
                target,
                control,
                arrays,
            )
            obs_index += 1
    if obs_index != nobs:
        raise RuntimeError("RK4 observation schedule was not completed")
    return _trajectory(
        configuration,
        model_id,
        source_commit,
        times,
        arrays,
        step_times,
        raw,
        post,
        retraction,
        integrator="RK4",
        profile=f"rk4-dt-{dt:.8g}",
        control_id=control.id,
    )


def integrate_dop853(
    configuration: PilotConfiguration,
    params: Parameters,
    model: ModelId | str,
    *,
    horizon: float,
    observation_interval: float,
    source_commit: str,
    rtol: float = 1.0e-10,
    atol: float = 1.0e-12,
    max_step: float = 1.0e-3,
) -> Trajectory:
    """Integrate one canonical run with the frozen DOP853 policy."""

    model_id = parse_model_id(model)
    if configuration.split == CONFIRMATORY_SPLIT:
        raise ConfirmatoryAccessError("confirmatory trajectory generation is forbidden")
    if configuration.split not in {PILOT_SPLIT, SMOKE_SPLIT}:
        raise ConfirmatoryAccessError("unsupported execution split")
    settings = (horizon, observation_interval, rtol, atol, max_step)
    if not all(np.isfinite(value) and value > 0.0 for value in settings):
        raise ValueError("DOP853 numerical settings must be finite and positive")
    n_segments = int(round(horizon / max_step))
    stride = int(round(observation_interval / max_step))
    nobs = int(round(horizon / observation_interval)) + 1
    if not np.isclose(n_segments * max_step, horizon, rtol=0.0, atol=1.0e-12):
        raise ValueError("horizon must be an integer multiple of DOP853 max_step")
    if stride <= 0 or not np.isclose(
        stride * max_step, observation_interval, rtol=0.0, atol=1.0e-12
    ):
        raise ValueError("observation interval must be an integer multiple of max_step")

    state = configuration.initial_state
    target = (
        ProjectionTarget(configuration.c0)
        if model_id in {ModelId.MP, ModelId.MFP}
        else None
    )
    control = ControlSpec()
    times = np.linspace(0.0, horizon, nobs, dtype=np.float64)
    arrays = _observation_arrays(nobs)
    step_times = np.arange(1, n_segments + 1, dtype=np.float64) * max_step
    raw = np.zeros(n_segments, dtype=np.float64)
    post = np.zeros(n_segments, dtype=np.float64)
    retraction = np.zeros(n_segments, dtype=np.float64)
    _record_observation(0, 0.0, state, params, model_id, target, control, arrays)

    def rhs(time: float, vector: FloatArray) -> FloatArray:
        return derivatives_for_model(
            State.unpack(vector), params, model_id, target=target
        ).pack()

    obs_index = 1
    if target is None:
        result = solve_ivp(
            rhs,
            (0.0, horizon),
            state.pack(),
            method="DOP853",
            t_eval=times,
            rtol=rtol,
            atol=atol,
            max_step=max_step,
        )
        if not result.success or result.y.shape != (9, nobs):
            raise NumericalGateError(f"DOP853 failed: {result.message}")
        if not np.all(np.isfinite(result.y)):
            raise NumericalGateError("DOP853 returned non-finite states")
        for obs_index in range(1, nobs):
            state = State.unpack(result.y[:, obs_index])
            _record_observation(
                obs_index,
                float(times[obs_index]),
                state,
                params,
                model_id,
                target,
                control,
                arrays,
            )
        obs_index = nobs
    else:
        for segment in range(n_segments):
            start = segment * max_step
            end = (segment + 1) * max_step
            result = solve_ivp(
                rhs,
                (start, end),
                state.pack(),
                method="DOP853",
                t_eval=np.array([end], dtype=np.float64),
                rtol=rtol,
                atol=atol,
                max_step=max_step,
            )
            if not result.success or result.y.shape != (9, 1):
                raise NumericalGateError(
                    f"DOP853 failed at segment {segment}: {result.message}"
                )
            if not np.all(np.isfinite(result.y)):
                raise NumericalGateError("DOP853 returned non-finite projected state")
            retracted = retract_to_constraint(State.unpack(result.y[:, -1]), target)
            state = retracted.state
            raw[segment] = retracted.raw_constraint_residual
            post[segment] = retracted.post_constraint_residual
            retraction[segment] = retracted.magnitude
            if (segment + 1) % stride == 0:
                _record_observation(
                    obs_index,
                    end,
                    state,
                    params,
                    model_id,
                    target,
                    control,
                    arrays,
                )
                obs_index += 1
    if obs_index != nobs:
        raise RuntimeError("DOP853 observation schedule was not completed")
    return _trajectory(
        configuration,
        model_id,
        source_commit,
        times,
        arrays,
        step_times,
        raw,
        post,
        retraction,
        integrator="DOP853",
        profile=(
            f"dop853-rtol-{rtol:.1e}-atol-{atol:.1e}-max-{max_step:.1e}"
        ),
        control_id="canonical",
    )


def exogenous_replay_control(reference_mf_fine: Trajectory) -> ControlSpec:
    """Build the piecewise-linear c_ref(t) control from MF observations."""

    if reference_mf_fine.model_id != ModelId.MF.value:
        raise ValueError("exogenous replay source must be MF")
    if reference_mf_fine.control_id != "canonical":
        raise ValueError("exogenous replay source must be canonical")
    x = reference_mf_fine.states[:, 0:3]
    return ControlSpec(
        exogenous_times=reference_mf_fine.times.copy(),
        exogenous_c=np.mean(x * x, axis=1),
    )

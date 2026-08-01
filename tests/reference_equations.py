"""Independent contract-v1.0 equations used only by tests.

This module may share immutable data containers with production code, but it
must not call production derivative, feedback, conductance, projector,
retraction, or integrator helpers.
"""

from __future__ import annotations

import numpy as np

from apophatic_geometry.model import EDGES, Parameters, State


_MINIMUM_C0 = 1.0e-6
_PROJECTOR_TOLERANCE = 1.0e-12


def _sigmoid_scalar(value: float) -> float:
    if value >= 0.0:
        return 1.0 / (1.0 + np.exp(-value))
    exp_value = np.exp(value)
    return exp_value / (1.0 + exp_value)


def _validate_c0(c0: float | None) -> float:
    if c0 is None:
        raise ValueError("reference MP requires c0")
    value = float(c0)
    if not np.isfinite(value) or value < _MINIMUM_C0:
        raise ValueError("invalid reference c0")
    return value


def _minimum_norm(c0: float) -> float:
    radius = float(np.sqrt(3.0 * c0))
    return max(1.0e-12, 1.0e-8 * radius)


def _project_reference_node_derivative(
    x: np.ndarray,
    proposal: np.ndarray,
    c0: float,
) -> np.ndarray:
    norm = float(np.linalg.norm(x))
    if norm <= _minimum_norm(c0):
        raise FloatingPointError("reference projection rank loss")
    denominator = float(np.dot(x, x))
    projected = proposal - x * (float(np.dot(x, proposal)) / denominator)
    tangency = abs(float(np.dot(x, projected))) / (
        norm * float(np.linalg.norm(projected)) + 1.0e-30
    )
    if tangency > _PROJECTOR_TOLERANCE:
        raise FloatingPointError("reference tangency failure")
    return projected


def reference_derivative(
    state: State,
    params: Parameters,
    model: str,
    c0: float | None = None,
) -> State:
    params.validate()
    if model not in {"m0", "mf", "mp"}:
        raise ValueError(f"unsupported reference model: {model}")

    x = state.x.copy()
    dx = params.alpha * x - params.beta * x**3
    ds = np.empty(3, dtype=np.float64)
    dq = np.empty(3, dtype=np.float64)

    for edge_index, (i, j) in enumerate(EDGES):
        activation = _sigmoid_scalar(float(state.s[edge_index]))
        weight = activation * np.exp(-state.q[edge_index])
        difference = x[i] - x[j]
        coupling = weight * difference
        dx[i] -= coupling
        dx[j] += coupling

        ds[edge_index] = (
            params.eta_0
            - params.eta_1 * difference**2
            - state.s[edge_index]
        ) / params.tau_s
        dq[edge_index] = (
            -params.gamma * state.q[edge_index]
            + params.kappa * difference**2
        ) / params.tau_q

    if model == "mf":
        c = float(np.dot(x, x) / 3.0)
        dx += -params.chi * c * x
        ds += params.eta_2 * c / params.tau_s
        dq += -params.rho * c / params.tau_q
    elif model == "mp":
        target = _validate_c0(c0)
        dx = _project_reference_node_derivative(x, dx, target)

    return State(x=dx, s=ds, q=dq)


def reference_mp_step_with_diagnostics(
    state: State,
    params: Parameters,
    dt: float,
    c0: float,
) -> tuple[State, float, float, float]:
    """Independent projected RK4 plus radial retraction."""

    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")
    target = _validate_c0(c0)
    initial_residual = float(np.dot(state.x, state.x) / 3.0 - target)
    if abs(initial_residual) > _PROJECTOR_TOLERANCE * max(1.0, target):
        raise ValueError("reference initial state is off manifold")

    y0 = state.pack()

    def rhs(vector: np.ndarray) -> np.ndarray:
        candidate = State(
            x=np.asarray(vector[0:3], dtype=np.float64),
            s=np.asarray(vector[3:6], dtype=np.float64),
            q=np.asarray(vector[6:9], dtype=np.float64),
        )
        return reference_derivative(candidate, params, "mp", c0=target).pack()

    k1 = rhs(y0)
    k2 = rhs(y0 + 0.5 * dt * k1)
    k3 = rhs(y0 + 0.5 * dt * k2)
    k4 = rhs(y0 + dt * k3)
    raw = State.unpack(y0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4))

    raw_norm = float(np.linalg.norm(raw.x))
    if raw_norm <= _minimum_norm(target):
        raise FloatingPointError("reference retraction rank loss")
    radius = float(np.sqrt(3.0 * target))
    retracted_x = radius * raw.x / raw_norm
    retracted = State(x=retracted_x, s=raw.s.copy(), q=raw.q.copy())

    raw_residual = float(np.dot(raw.x, raw.x) / 3.0 - target)
    post_residual = float(np.dot(retracted.x, retracted.x) / 3.0 - target)
    magnitude = float(np.linalg.norm(retracted.x - raw.x))
    if abs(post_residual) > _PROJECTOR_TOLERANCE * max(1.0, target):
        raise FloatingPointError("reference post-retraction residual failure")
    return retracted, raw_residual, post_residual, magnitude


def reference_rk4_step(
    state: State,
    params: Parameters,
    dt: float,
    model: str,
    c0: float | None = None,
) -> State:
    if model == "mp":
        return reference_mp_step_with_diagnostics(
            state,
            params,
            dt,
            _validate_c0(c0),
        )[0]

    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")

    y0 = state.pack()

    def rhs(vector: np.ndarray) -> np.ndarray:
        candidate = State(
            x=np.asarray(vector[0:3], dtype=np.float64),
            s=np.asarray(vector[3:6], dtype=np.float64),
            q=np.asarray(vector[6:9], dtype=np.float64),
        )
        return reference_derivative(candidate, params, model).pack()

    k1 = rhs(y0)
    k2 = rhs(y0 + 0.5 * dt * k1)
    k3 = rhs(y0 + 0.5 * dt * k2)
    k4 = rhs(y0 + dt * k3)
    return State.unpack(y0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4))

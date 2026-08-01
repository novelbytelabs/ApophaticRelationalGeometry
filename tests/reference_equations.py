"""Independent contract-v1.0 equations used only by tests.

This module may share immutable data containers with production code, but it
must not call production derivative, feedback, conductance, or integrator
helpers.
"""

from __future__ import annotations

import numpy as np

from apophatic_geometry.model import EDGES, Parameters, State


def _sigmoid_scalar(value: float) -> float:
    if value >= 0.0:
        return 1.0 / (1.0 + np.exp(-value))
    exp_value = np.exp(value)
    return exp_value / (1.0 + exp_value)


def reference_derivative(state: State, params: Parameters, model: str) -> State:
    params.validate()
    if model not in {"m0", "mf"}:
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

    return State(x=dx, s=ds, q=dq)


def reference_rk4_step(
    state: State,
    params: Parameters,
    dt: float,
    model: str,
) -> State:
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

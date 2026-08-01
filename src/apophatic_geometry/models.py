"""Contract-v1.0 dispatch for the implemented ARG model family.

Phase 2 adds the no-feedback local/adaptive baseline M0 while preserving the
existing MF implementation in :mod:`apophatic_geometry.model`. Projected
models remain fail-closed until later roadmap gates.
"""

from __future__ import annotations

from enum import Enum
from typing import Final

import numpy as np
from numpy.typing import NDArray

from .model import (
    EDGES,
    Parameters,
    State,
    collective_mode,
    conductances,
    derivatives as mf_derivatives,
)

FloatArray = NDArray[np.float64]
CONTRACT_VERSION: Final[str] = "1.0"


class ModelId(str, Enum):
    """Canonical identifiers from the frozen four-model contract."""

    M0 = "m0"
    MF = "mf"
    MP = "mp"
    MFP = "mfp"


def parse_model_id(model: ModelId | str) -> ModelId:
    """Normalize a model identifier and reject unknown values."""

    if isinstance(model, ModelId):
        return model
    try:
        return ModelId(str(model).lower())
    except ValueError as exc:
        allowed = ", ".join(member.value for member in ModelId)
        raise ValueError(f"unknown model {model!r}; expected one of: {allowed}") from exc


def _validate_finite_parameters(params: Parameters) -> None:
    values = vars(params)
    nonfinite = [name for name, value in values.items() if not np.isfinite(value)]
    if nonfinite:
        raise ValueError(f"Parameters must be finite: {', '.join(nonfinite)}")


def local_adaptive_derivatives(state: State, params: Parameters) -> State:
    """Evaluate M0 without computing or consuming ``c(x)``.

    The transition equations contain local nonlinear dynamics, neighbor
    coupling, adaptive edge activation, and metric deformation. No collective
    statistic enters the transition graph.
    """

    _validate_finite_parameters(params)
    params.validate()
    x, s, q = state.x, state.s, state.q
    weights = conductances(state)

    dx = params.alpha * x - params.beta * x**3
    ds = np.empty(3, dtype=np.float64)
    dq = np.empty(3, dtype=np.float64)

    for edge_index, (i, j) in enumerate(EDGES):
        difference = x[i] - x[j]
        coupling = weights[edge_index] * difference
        dx[i] -= coupling
        dx[j] += coupling

        ds[edge_index] = (
            params.eta_0
            - params.eta_1 * difference**2
            - s[edge_index]
        ) / params.tau_s

        dq[edge_index] = (
            -params.gamma * q[edge_index]
            + params.kappa * difference**2
        ) / params.tau_q

    derivative = State(x=dx, s=ds, q=dq)
    if not np.all(np.isfinite(derivative.pack())):
        raise FloatingPointError("non-finite M0 derivative encountered")
    return derivative


def feedback_vector(state: State, params: Parameters) -> State:
    """Return the explicit MF feedback contribution ``F_F``."""

    _validate_finite_parameters(params)
    params.validate()
    c = collective_mode(state.x)
    return State(
        x=-params.chi * c * state.x,
        s=np.full(3, params.eta_2 * c / params.tau_s, dtype=np.float64),
        q=np.full(3, -params.rho * c / params.tau_q, dtype=np.float64),
    )


def derivatives_for_model(
    state: State,
    params: Parameters,
    model: ModelId | str,
) -> State:
    """Dispatch implemented models and fail closed for MP and MFP."""

    model_id = parse_model_id(model)
    if model_id is ModelId.M0:
        return local_adaptive_derivatives(state, params)
    if model_id is ModelId.MF:
        return mf_derivatives(state, params)
    raise NotImplementedError(
        f"{model_id.value} is defined by contract v{CONTRACT_VERSION} "
        "but is not implemented at the current roadmap gate"
    )


def _validate_dt(dt: float) -> None:
    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")


def rk4_step(
    state: State,
    params: Parameters,
    dt: float,
    model: ModelId | str = ModelId.MF,
) -> State:
    """Advance one classical fixed-step fourth-order Runge--Kutta step."""

    _validate_dt(dt)
    model_id = parse_model_id(model)
    y0 = state.pack()

    def rhs(vector: FloatArray) -> FloatArray:
        return derivatives_for_model(State.unpack(vector), params, model_id).pack()

    k1 = rhs(y0)
    k2 = rhs(y0 + 0.5 * dt * k1)
    k3 = rhs(y0 + 0.5 * dt * k2)
    k4 = rhs(y0 + dt * k3)
    result = y0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    if not np.all(np.isfinite(result)):
        raise FloatingPointError("non-finite RK4 state encountered")
    return State.unpack(result)

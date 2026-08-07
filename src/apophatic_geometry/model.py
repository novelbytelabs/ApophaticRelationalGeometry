"""Minimal nonlinear dynamic relational geometry.

The implementation uses a complete undirected graph on three nodes. The
collective mode is derived from the node states and feeds back into local,
edge, and metric dynamics. No claim is made that these equations are physical
law; they are the first executable model of the proposed architecture.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]

# Fixed edge order for the three-node complete graph.
EDGES: Final[tuple[tuple[int, int], ...]] = ((0, 1), (0, 2), (1, 2))


@dataclass(frozen=True)
class Parameters:
    """Model parameters with conservative defaults."""

    alpha: float = 1.0
    beta: float = 1.0
    chi: float = 0.35
    tau_s: float = 1.0
    eta_0: float = 0.25
    eta_1: float = 1.0
    eta_2: float = 0.2
    tau_q: float = 1.0
    gamma: float = 0.8
    kappa: float = 0.4
    rho: float = 0.15
    epsilon: float = 1.0e-6

    def validate(self) -> None:
        values = vars(self)
        nonfinite = [name for name, value in values.items() if not np.isfinite(value)]
        if nonfinite:
            raise ValueError(f"Parameters must be finite: {', '.join(nonfinite)}")

        positive = {
            "beta": self.beta,
            "tau_s": self.tau_s,
            "eta_1": self.eta_1,
            "tau_q": self.tau_q,
            "gamma": self.gamma,
            "epsilon": self.epsilon,
        }
        invalid = [name for name, value in positive.items() if value <= 0.0]
        if invalid:
            raise ValueError(f"Parameters must be positive: {', '.join(invalid)}")


@dataclass(frozen=True)
class State:
    """Immutable three-node state, edge logits, and metric variables.

    Arrays are copied on construction and marked read-only. This prevents
    caller aliasing or direct array mutation from changing a validated state.
    """

    x: FloatArray
    s: FloatArray
    q: FloatArray

    def __post_init__(self) -> None:
        for name, value in (("x", self.x), ("s", self.s), ("q", self.q)):
            array = np.array(value, dtype=np.float64, copy=True)
            if array.shape != (3,):
                raise ValueError(f"{name} must have shape (3,), received {array.shape}")
            if not np.all(np.isfinite(array)):
                raise ValueError(f"{name} contains non-finite values")
            array.setflags(write=False)
            object.__setattr__(self, name, array)

    def pack(self) -> FloatArray:
        """Return a fresh writable packed copy of the state."""

        return np.concatenate((self.x, self.s, self.q))

    @classmethod
    def unpack(cls, vector: FloatArray) -> "State":
        vector = np.asarray(vector, dtype=np.float64)
        if vector.shape != (9,):
            raise ValueError(f"state vector must have shape (9,), received {vector.shape}")
        if not np.all(np.isfinite(vector)):
            raise ValueError("state vector contains non-finite values")
        return cls(x=vector[0:3], s=vector[3:6], q=vector[6:9])


def _strict_exp(value: FloatArray | float, context: str) -> FloatArray:
    """Evaluate an exponential only when the FP64 result is finite and positive.

    Underflow is rejected rather than silently converted to zero because zero
    conductance or zero intrinsic length violates the declared model domain.
    """

    array = np.asarray(value, dtype=np.float64)
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{context} exponent contains non-finite values")
    try:
        with np.errstate(over="raise", under="raise", invalid="raise"):
            result = np.exp(array)
    except FloatingPointError as exc:
        raise FloatingPointError(
            f"{context} exponential lies outside the finite FP64 domain"
        ) from exc
    if not np.all(np.isfinite(result)) or np.any(result <= 0.0):
        raise FloatingPointError(f"{context} exponential must remain finite and positive")
    return np.asarray(result, dtype=np.float64)


def sigmoid(value: FloatArray) -> FloatArray:
    """Numerically stable logistic activation with fail-closed saturation.

    The mathematical logistic lies strictly in ``(0, 1)``. Inputs whose FP64
    evaluation would round to exactly zero or one are outside the executable
    numeric domain and are rejected.
    """

    value = np.asarray(value, dtype=np.float64)
    if not np.all(np.isfinite(value)):
        raise ValueError("sigmoid input contains non-finite values")
    out = np.empty_like(value)
    nonnegative = value >= 0.0
    if np.any(nonnegative):
        exp_value = _strict_exp(-value[nonnegative], "sigmoid")
        out[nonnegative] = 1.0 / (1.0 + exp_value)
    if np.any(~nonnegative):
        exp_value = _strict_exp(value[~nonnegative], "sigmoid")
        out[~nonnegative] = exp_value / (1.0 + exp_value)
    if (
        not np.all(np.isfinite(out))
        or np.any(out <= 0.0)
        or np.any(out >= 1.0)
    ):
        raise FloatingPointError("sigmoid activation must remain strictly between zero and one")
    return out


def collective_mode(x: FloatArray) -> float:
    """Endogenous whole-state observable generated by local states."""

    x = np.asarray(x, dtype=np.float64)
    if x.shape != (3,) or not np.all(np.isfinite(x)):
        raise ValueError("x must be a finite vector of shape (3,)")
    try:
        with np.errstate(over="raise", invalid="raise"):
            value = float(np.mean(x * x))
    except FloatingPointError as exc:
        raise FloatingPointError("collective mode overflow") from exc
    if not np.isfinite(value):
        raise FloatingPointError("collective mode is non-finite")
    return value


def conductances(state: State) -> FloatArray:
    """Return finite, strictly positive edge conductances in fixed edge order."""

    activation = sigmoid(state.s)
    scale = _strict_exp(-state.q, "conductance")
    try:
        with np.errstate(over="raise", under="raise", invalid="raise"):
            result = activation * scale
    except FloatingPointError as exc:
        raise FloatingPointError("conductance arithmetic left the finite FP64 domain") from exc
    if not np.all(np.isfinite(result)) or np.any(result <= 0.0):
        raise FloatingPointError("conductances must remain finite and strictly positive")
    return np.asarray(result, dtype=np.float64)


def intrinsic_edge_lengths(state: State, params: Parameters) -> FloatArray:
    """Return finite, strictly positive state-dependent intrinsic edge lengths."""

    params.validate()
    activation = sigmoid(state.s)
    scale = _strict_exp(state.q, "intrinsic length")
    lengths = np.empty(3, dtype=np.float64)
    try:
        with np.errstate(over="raise", under="raise", divide="raise", invalid="raise"):
            for edge_index, (i, j) in enumerate(EDGES):
                mismatch = state.x[i] - state.x[j]
                local_scale = np.sqrt(params.epsilon**2 + mismatch**2)
                lengths[edge_index] = (
                    scale[edge_index] * local_scale / activation[edge_index]
                )
    except FloatingPointError as exc:
        raise FloatingPointError("intrinsic length arithmetic left the finite FP64 domain") from exc
    if not np.all(np.isfinite(lengths)) or np.any(lengths <= 0.0):
        raise FloatingPointError("intrinsic edge lengths must remain finite and strictly positive")
    return lengths


def intrinsic_distance_matrix(state: State, params: Parameters) -> FloatArray:
    """Compute finite all-pairs shortest-path distances for the graph."""

    lengths = intrinsic_edge_lengths(state, params)
    distance = np.full((3, 3), np.inf, dtype=np.float64)
    np.fill_diagonal(distance, 0.0)
    for edge_index, (i, j) in enumerate(EDGES):
        distance[i, j] = lengths[edge_index]
        distance[j, i] = lengths[edge_index]

    try:
        with np.errstate(over="raise", invalid="raise"):
            for k in range(3):
                for i in range(3):
                    for j in range(3):
                        candidate = distance[i, k] + distance[k, j]
                        if candidate < distance[i, j]:
                            distance[i, j] = candidate
    except FloatingPointError as exc:
        raise FloatingPointError("intrinsic distance arithmetic overflow") from exc

    off_diagonal = distance[~np.eye(3, dtype=bool)]
    if (
        not np.all(np.isfinite(distance))
        or np.any(off_diagonal <= 0.0)
        or not np.array_equal(distance, distance.T)
    ):
        raise FloatingPointError("intrinsic distance matrix violated metric-domain invariants")
    return distance


def derivatives(state: State, params: Parameters) -> State:
    """Evaluate the coupled nonlinear right-hand side."""

    params.validate()
    x, s, q = state.x, state.s, state.q
    c = collective_mode(x)
    weights = conductances(state)

    try:
        with np.errstate(over="raise", under="raise", divide="raise", invalid="raise"):
            dx = params.alpha * x - params.beta * x**3 - params.chi * c * x
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
                    + params.eta_2 * c
                    - s[edge_index]
                ) / params.tau_s

                dq[edge_index] = (
                    -params.gamma * q[edge_index]
                    + params.kappa * difference**2
                    - params.rho * c
                ) / params.tau_q
    except FloatingPointError as exc:
        raise FloatingPointError("derivative arithmetic left the finite FP64 domain") from exc

    derivative = State(x=dx, s=ds, q=dq)
    if not np.all(np.isfinite(derivative.pack())):
        raise FloatingPointError("non-finite derivative encountered")
    return derivative


def euler_step(state: State, params: Parameters, dt: float) -> State:
    """Advance one explicit Euler step for transparent reference testing."""

    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")
    rhs = derivatives(state, params)
    try:
        with np.errstate(over="raise", under="raise", invalid="raise"):
            packed = state.pack() + dt * rhs.pack()
    except FloatingPointError as exc:
        raise FloatingPointError("Euler update left the finite FP64 domain") from exc
    return State.unpack(packed)

from __future__ import annotations

import itertools

import numpy as np

from apophatic_geometry.model import (
    EDGES,
    Parameters,
    State,
    collective_mode,
    derivatives,
    intrinsic_distance_matrix,
    intrinsic_edge_lengths,
)


def sample_state() -> State:
    return State(
        x=np.array([0.8, -0.25, 0.45]),
        s=np.array([0.2, -0.1, 0.1]),
        q=np.array([0.0, 0.05, -0.05]),
    )


def test_edge_lengths_are_positive_and_finite() -> None:
    lengths = intrinsic_edge_lengths(sample_state(), Parameters())
    assert np.all(np.isfinite(lengths))
    assert np.all(lengths > 0.0)


def test_shortest_path_distance_is_a_metric() -> None:
    distance = intrinsic_distance_matrix(sample_state(), Parameters())
    assert np.allclose(distance, distance.T)
    assert np.allclose(np.diag(distance), 0.0)
    assert np.all(distance[np.triu_indices(3, k=1)] > 0.0)

    for i, j, k in itertools.product(range(3), repeat=3):
        assert distance[i, j] <= distance[i, k] + distance[k, j] + 1.0e-12


def test_collective_mode_is_nonnegative_and_permutation_invariant() -> None:
    state = sample_state()
    expected = collective_mode(state.x)
    assert expected >= 0.0
    for permutation in itertools.permutations(range(3)):
        assert np.isclose(collective_mode(state.x[list(permutation)]), expected)


def permute_state(state: State, permutation: tuple[int, int, int]) -> State:
    inverse_edge_lookup = {tuple(sorted(edge)): index for index, edge in enumerate(EDGES)}
    new_s = np.empty(3)
    new_q = np.empty(3)
    for new_index, (i, j) in enumerate(EDGES):
        old_edge = tuple(sorted((permutation[i], permutation[j])))
        old_index = inverse_edge_lookup[old_edge]
        new_s[new_index] = state.s[old_index]
        new_q[new_index] = state.q[old_index]
    return State(x=state.x[list(permutation)], s=new_s, q=new_q)


def test_derivatives_are_permutation_equivariant() -> None:
    state = sample_state()
    params = Parameters()
    base = derivatives(state, params)
    permutation = (2, 0, 1)
    permuted_state = permute_state(state, permutation)
    permuted_rhs = derivatives(permuted_state, params)
    expected_rhs = permute_state(base, permutation)
    assert np.allclose(permuted_rhs.pack(), expected_rhs.pack())


def test_derivatives_are_finite() -> None:
    rhs = derivatives(sample_state(), Parameters())
    assert np.all(np.isfinite(rhs.pack()))

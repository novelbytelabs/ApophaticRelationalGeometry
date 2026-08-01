from __future__ import annotations

import csv

import numpy as np
import pytest

from apophatic_geometry.model import Parameters, State, collective_mode
from apophatic_geometry.models import (
    MINIMUM_C0,
    PROJECTOR_TOLERANCE,
    ModelId,
    ProjectionTarget,
    constraint_residual,
    derivatives_for_model,
    project_node_derivative,
    projected_derivative,
    projected_rk4_step,
    retract_to_constraint,
    rk4_step,
    tangent_projector,
)
from apophatic_geometry.simulate import run
from tests.reference_equations import (
    reference_derivative,
    reference_mp_step_with_diagnostics,
    reference_rk4_step,
)
from tests.test_model import permute_state, sample_state


def test_projection_target_is_derived_and_validated() -> None:
    state = sample_state()
    target = ProjectionTarget.from_state(state)
    assert target.c0 == collective_mode(state.x)
    assert target.radius == np.sqrt(3.0 * target.c0)
    assert target.minimum_norm == max(1.0e-12, 1.0e-8 * target.radius)

    with pytest.raises(ValueError):
        ProjectionTarget(c0=MINIMUM_C0 / 2.0)
    with pytest.raises(ValueError):
        ProjectionTarget(c0=np.nan)


def test_tangent_projector_identities() -> None:
    x = np.array([0.8, -0.25, 0.45], dtype=np.float64)
    target = ProjectionTarget(c0=float(np.dot(x, x) / 3.0))
    projector = tangent_projector(x, target)

    assert np.allclose(projector.T, projector, rtol=0.0, atol=1.0e-12)
    assert np.allclose(projector @ projector, projector, rtol=0.0, atol=1.0e-12)
    assert np.allclose(projector @ x, np.zeros(3), rtol=0.0, atol=1.0e-12)


def test_hand_computed_projection_case() -> None:
    x = np.array([1.0, 0.0, 0.0], dtype=np.float64)
    proposal = np.array([2.0, 3.0, 4.0], dtype=np.float64)
    target = ProjectionTarget(c0=1.0 / 3.0)

    projected, correction, tangency, denominator = project_node_derivative(
        x,
        proposal,
        target,
    )

    assert np.array_equal(projected, np.array([0.0, 3.0, 4.0]))
    assert np.array_equal(correction, np.array([-2.0, 0.0, 0.0]))
    assert tangency == 0.0
    assert denominator == 1.0


def test_projected_derivative_is_tangent_and_preserves_sq_proposal() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    diagnostics = projected_derivative(state, params, target)

    assert abs(float(np.dot(state.x, diagnostics.projected.x))) <= 1.0e-14
    assert diagnostics.normalized_tangency_residual <= PROJECTOR_TOLERANCE
    assert np.array_equal(diagnostics.projected.s, diagnostics.proposal.s)
    assert np.array_equal(diagnostics.projected.q, diagnostics.proposal.q)
    assert np.array_equal(diagnostics.correction.s, np.zeros(3))
    assert np.array_equal(diagnostics.correction.q, np.zeros(3))
    assert np.allclose(
        diagnostics.projected.pack(),
        diagnostics.proposal.pack() + diagnostics.correction.pack(),
        rtol=0.0,
        atol=1.0e-14,
    )


def test_mp_dispatch_matches_explicit_projected_derivative() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    dispatched = derivatives_for_model(state, params, ModelId.MP, target=target)
    explicit = projected_derivative(state, params, target).projected
    assert np.array_equal(dispatched.pack(), explicit.pack())


def test_retraction_restores_constraint_and_preserves_sq() -> None:
    state = sample_state()
    target = ProjectionTarget.from_state(state)
    raw = State(x=1.01 * state.x, s=state.s.copy(), q=state.q.copy())
    result = retract_to_constraint(raw, target)

    tolerance = PROJECTOR_TOLERANCE * max(1.0, target.c0)
    assert abs(result.post_constraint_residual) <= tolerance
    assert abs(constraint_residual(result.state, target)) <= tolerance
    assert result.magnitude > 0.0
    assert np.array_equal(result.state.s, state.s)
    assert np.array_equal(result.state.q, state.q)


def test_retraction_is_no_change_within_roundoff_on_admissible_state() -> None:
    state = sample_state()
    target = ProjectionTarget.from_state(state)
    result = retract_to_constraint(state, target)
    assert result.magnitude <= 1.0e-15
    assert np.allclose(result.state.pack(), state.pack(), rtol=0.0, atol=1.0e-15)


def test_projection_fails_closed_at_rank_loss() -> None:
    target = ProjectionTarget(c0=1.0 / 3.0)
    with pytest.raises(FloatingPointError, match="fail-closed threshold"):
        tangent_projector(np.zeros(3), target)

    near_zero = np.array([0.5 * target.minimum_norm, 0.0, 0.0])
    with pytest.raises(FloatingPointError, match="fail-closed threshold"):
        tangent_projector(near_zero, target)


def test_projected_step_rejects_wrong_target() -> None:
    state = sample_state()
    wrong_target = ProjectionTarget(c0=1.0)
    with pytest.raises(ValueError, match="does not lie"):
        projected_rk4_step(state, Parameters(), 0.005, wrong_target)


def test_mp_is_permutation_equivariant() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    permutation = (2, 0, 1)

    base = projected_derivative(state, params, target)
    permuted_state = permute_state(state, permutation)
    actual = projected_derivative(permuted_state, params, target)

    expected_projected = permute_state(base.projected, permutation)
    expected_correction = permute_state(base.correction, permutation)
    assert np.allclose(
        actual.projected.pack(), expected_projected.pack(), rtol=0.0, atol=1.0e-14
    )
    assert np.allclose(
        actual.correction.pack(), expected_correction.pack(), rtol=0.0, atol=1.0e-14
    )


def test_mp_derivative_matches_independent_reference() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    actual = derivatives_for_model(state, params, ModelId.MP, target=target)
    expected = reference_derivative(state, params, "mp", c0=target.c0)
    assert np.allclose(actual.pack(), expected.pack(), rtol=0.0, atol=1.0e-14)


def test_mp_rk4_and_retraction_match_independent_reference() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    dt = 0.005

    actual = projected_rk4_step(state, params, dt, target)
    expected_state, expected_raw, expected_post, expected_magnitude = (
        reference_mp_step_with_diagnostics(state, params, dt, target.c0)
    )

    assert np.allclose(actual.state.pack(), expected_state.pack(), rtol=0.0, atol=1.0e-14)
    assert np.isclose(actual.raw_constraint_residual, expected_raw, rtol=0.0, atol=1.0e-15)
    assert np.isclose(actual.post_constraint_residual, expected_post, rtol=0.0, atol=1.0e-15)
    assert np.isclose(actual.retraction_magnitude, expected_magnitude, rtol=0.0, atol=1.0e-15)
    assert len(actual.stage_diagnostics) == 4
    assert all(
        stage.normalized_tangency_residual <= PROJECTOR_TOLERANCE
        for stage in actual.stage_diagnostics
    )


def test_generic_rk4_mp_matches_independent_reference() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    dt = 0.005
    actual = rk4_step(state, params, dt, ModelId.MP, target=target)
    expected = reference_rk4_step(state, params, dt, "mp", c0=target.c0)
    assert np.allclose(actual.pack(), expected.pack(), rtol=0.0, atol=1.0e-14)


def test_raw_constraint_drift_and_retraction_shrink_under_step_refinement() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    results = [
        projected_rk4_step(state, params, dt, target)
        for dt in (0.01, 0.005, 0.0025)
    ]
    raw = [abs(result.raw_constraint_residual) for result in results]
    retraction = [result.retraction_magnitude for result in results]

    assert raw[2] < raw[1] < raw[0]
    assert retraction[2] < retraction[1] < retraction[0]
    assert all(
        abs(result.post_constraint_residual)
        <= PROJECTOR_TOLERANCE * max(1.0, target.c0)
        for result in results
    )


def test_mp_simulation_records_projection_diagnostics(tmp_path) -> None:
    output = tmp_path / "mp.csv"
    run(steps=2, dt=0.005, output=output, model=ModelId.MP)

    with output.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 3
    assert {row["model_id"] for row in rows} == {ModelId.MP.value}
    assert len({row["configuration_hash"] for row in rows}) == 1
    for row in rows:
        assert row["constraint_residual"] != ""
        assert row["normalized_tangency_residual"] != ""
        assert row["projection_correction_norm"] != ""
        assert row["projection_denominator"] != ""
        assert row["pre_retraction_constraint_residual"] != ""
        assert row["post_retraction_constraint_residual"] != ""
        assert row["retraction_magnitude"] != ""
        assert abs(float(row["post_retraction_constraint_residual"])) <= 1.0e-12

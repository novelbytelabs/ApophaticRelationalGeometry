from __future__ import annotations

import csv

import numpy as np
import pytest

from apophatic_geometry.model import Parameters, derivatives
from apophatic_geometry.models import (
    PROJECTOR_TOLERANCE,
    ModelId,
    ProjectionTarget,
    combined_feedback_proposal,
    combined_projected_derivative,
    combined_projected_rk4_step,
    derivatives_for_model,
    local_adaptive_derivatives,
    project_node_derivative,
    projected_derivative,
    rk4_step,
)
from apophatic_geometry.simulate import run
from tests.reference_equations import (
    reference_derivative,
    reference_mfp_step_with_diagnostics,
    reference_rk4_step,
)
from tests.test_model import permute_state, sample_state


def test_combined_feedback_proposal_reconstructs_mf() -> None:
    state = sample_state()
    params = Parameters()
    local, feedback, proposal = combined_feedback_proposal(state, params)

    assert np.array_equal(proposal.x, local.x + feedback.x)
    assert np.array_equal(proposal.s, local.s + feedback.s)
    assert np.array_equal(proposal.q, local.q + feedback.q)
    assert np.allclose(
        proposal.pack(), derivatives(state, params).pack(), rtol=0.0, atol=1.0e-14
    )


def test_combined_feedback_proposal_reduces_exactly_to_m0() -> None:
    state = sample_state()
    params = Parameters(chi=0.0, eta_2=0.0, rho=0.0)
    local, feedback, proposal = combined_feedback_proposal(state, params)

    assert np.array_equal(local.pack(), local_adaptive_derivatives(state, params).pack())
    assert np.array_equal(feedback.pack(), np.zeros(9))
    assert np.array_equal(proposal.pack(), local.pack())


def test_radial_node_feedback_is_annihilated_by_projection() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    _, feedback, _ = combined_feedback_proposal(state, params)

    projected, correction, tangency, _ = project_node_derivative(
        state.x, feedback.x, target
    )
    assert np.allclose(projected, np.zeros(3), rtol=0.0, atol=1.0e-14)
    assert np.allclose(correction, -feedback.x, rtol=0.0, atol=1.0e-14)
    assert tangency <= PROJECTOR_TOLERANCE


def test_mfp_node_identity_and_retained_substrate_feedback() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    mp = projected_derivative(state, params, target)
    mfp = combined_projected_derivative(state, params, target)

    assert np.allclose(mfp.projected.x, mp.projected.x, rtol=0.0, atol=1.0e-14)
    assert np.allclose(
        mfp.correction.x,
        mp.correction.x - mfp.feedback.x,
        rtol=0.0,
        atol=1.0e-14,
    )
    assert np.array_equal(mfp.projected.s, mp.projected.s + mfp.feedback.s)
    assert np.array_equal(mfp.projected.q, mp.projected.q + mfp.feedback.q)
    assert not np.array_equal(mfp.projected.s, mp.projected.s)
    assert not np.array_equal(mfp.projected.q, mp.projected.q)


def test_mfp_diagnostics_keep_mechanisms_separate() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    diagnostics = combined_projected_derivative(state, params, target)

    assert diagnostics.feedback_norm > 0.0
    assert diagnostics.node_feedback_norm > 0.0
    assert diagnostics.correction_norm > 0.0
    assert np.allclose(
        diagnostics.proposal.pack(),
        diagnostics.local_proposal.pack() + diagnostics.feedback.pack(),
        rtol=0.0,
        atol=1.0e-14,
    )
    assert np.allclose(
        diagnostics.projected.pack(),
        diagnostics.proposal.pack() + diagnostics.correction.pack(),
        rtol=0.0,
        atol=1.0e-14,
    )
    assert np.array_equal(diagnostics.correction.s, np.zeros(3))
    assert np.array_equal(diagnostics.correction.q, np.zeros(3))
    assert diagnostics.normalized_tangency_residual <= PROJECTOR_TOLERANCE


def test_mfp_dispatch_matches_explicit_derivative() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    actual = derivatives_for_model(state, params, ModelId.MFP, target=target)
    expected = combined_projected_derivative(state, params, target).projected
    assert np.array_equal(actual.pack(), expected.pack())


def test_mfp_requires_explicit_target() -> None:
    with pytest.raises(ValueError, match="ProjectionTarget"):
        derivatives_for_model(sample_state(), Parameters(), ModelId.MFP)
    with pytest.raises(ValueError, match="ProjectionTarget"):
        rk4_step(sample_state(), Parameters(), 0.005, ModelId.MFP)


def test_zero_feedback_mfp_reduces_exactly_to_mp() -> None:
    state = sample_state()
    params = Parameters(chi=0.0, eta_2=0.0, rho=0.0)
    target = ProjectionTarget.from_state(state)
    mp = projected_derivative(state, params, target)
    mfp = combined_projected_derivative(state, params, target)

    assert np.array_equal(mfp.feedback.pack(), np.zeros(9))
    assert np.array_equal(mfp.proposal.pack(), mp.proposal.pack())
    assert np.array_equal(mfp.correction.pack(), mp.correction.pack())
    assert np.array_equal(mfp.projected.pack(), mp.projected.pack())


def test_mfp_is_permutation_equivariant() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    permutation = (2, 0, 1)

    base = combined_projected_derivative(state, params, target)
    permuted_state = permute_state(state, permutation)
    actual = combined_projected_derivative(permuted_state, params, target)

    assert np.allclose(
        actual.local_proposal.pack(),
        permute_state(base.local_proposal, permutation).pack(),
        rtol=0.0,
        atol=1.0e-14,
    )
    assert np.allclose(
        actual.feedback.pack(),
        permute_state(base.feedback, permutation).pack(),
        rtol=0.0,
        atol=1.0e-14,
    )
    assert np.allclose(
        actual.projected.pack(),
        permute_state(base.projected, permutation).pack(),
        rtol=0.0,
        atol=1.0e-14,
    )


def test_mfp_derivative_matches_independent_reference() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    actual = derivatives_for_model(state, params, ModelId.MFP, target=target)
    expected = reference_derivative(state, params, "mfp", c0=target.c0)
    assert np.allclose(actual.pack(), expected.pack(), rtol=0.0, atol=1.0e-14)


def test_mfp_rk4_and_retraction_match_independent_reference() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    dt = 0.005

    actual = combined_projected_rk4_step(state, params, dt, target)
    expected_state, expected_raw, expected_post, expected_magnitude = (
        reference_mfp_step_with_diagnostics(state, params, dt, target.c0)
    )

    assert np.allclose(actual.state.pack(), expected_state.pack(), rtol=0.0, atol=1.0e-14)
    assert np.isclose(actual.raw_constraint_residual, expected_raw, rtol=0.0, atol=1.0e-15)
    assert np.isclose(actual.post_constraint_residual, expected_post, rtol=0.0, atol=1.0e-15)
    assert np.isclose(actual.retraction_magnitude, expected_magnitude, rtol=0.0, atol=1.0e-15)
    assert len(actual.stage_diagnostics) == 4
    assert all(stage.feedback_norm > 0.0 for stage in actual.stage_diagnostics)
    assert all(
        stage.normalized_tangency_residual <= PROJECTOR_TOLERANCE
        for stage in actual.stage_diagnostics
    )


def test_generic_rk4_mfp_matches_independent_reference() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    dt = 0.005
    actual = rk4_step(state, params, dt, ModelId.MFP, target=target)
    expected = reference_rk4_step(state, params, dt, "mfp", c0=target.c0)
    assert np.allclose(actual.pack(), expected.pack(), rtol=0.0, atol=1.0e-14)


def test_mfp_step_preserves_constraint_and_changes_substrate_from_mp() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    dt = 0.005
    mfp = combined_projected_rk4_step(state, params, dt, target)
    mp = rk4_step(state, params, dt, ModelId.MP, target=target)

    assert abs(mfp.post_constraint_residual) <= PROJECTOR_TOLERANCE * max(
        1.0, target.c0
    )
    assert not np.allclose(mfp.state.s, mp.s, rtol=0.0, atol=1.0e-15)
    assert not np.allclose(mfp.state.q, mp.q, rtol=0.0, atol=1.0e-15)


def test_mfp_rejects_wrong_target() -> None:
    state = sample_state()
    wrong_target = ProjectionTarget(c0=1.0)
    with pytest.raises(ValueError, match="does not lie"):
        combined_projected_rk4_step(state, Parameters(), 0.005, wrong_target)


def test_mfp_raw_drift_and_retraction_shrink_under_step_refinement() -> None:
    state = sample_state()
    params = Parameters()
    target = ProjectionTarget.from_state(state)
    results = [
        combined_projected_rk4_step(state, params, dt, target)
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


def test_mfp_simulation_records_separate_mechanism_diagnostics(tmp_path) -> None:
    output = tmp_path / "mfp.csv"
    run(steps=2, dt=0.005, output=output, model=ModelId.MFP)

    with output.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 3
    assert {row["model_id"] for row in rows} == {ModelId.MFP.value}
    assert len({row["configuration_hash"] for row in rows}) == 1
    for row in rows:
        assert row["constraint_residual"] != ""
        assert row["normalized_tangency_residual"] != ""
        assert row["projection_correction_norm"] != ""
        assert row["projection_denominator"] != ""
        assert row["feedback_norm"] != ""
        assert row["node_feedback_norm"] != ""
        assert row["local_proposal_norm"] != ""
        assert row["combined_proposal_norm"] != ""
        assert row["pre_retraction_constraint_residual"] != ""
        assert row["post_retraction_constraint_residual"] != ""
        assert row["retraction_magnitude"] != ""
        assert float(row["feedback_norm"]) > 0.0
        assert abs(float(row["post_retraction_constraint_residual"])) <= 1.0e-12

# Apophatic Relational Geometry

> **Status: Candidate synthesis — not a claim of a new fundamental geometry.**
>
> ARG investigates whether nonlinear dynamics, adaptive networks, state-dependent geometry, collective feedback, local-to-global compatibility, and constrained dynamics can be combined into a coherent and useful framework. Mathematical novelty, explanatory value, and physical relevance remain open research questions.

## Implemented model family

### $M_0$ — local/adaptive baseline

Local nonlinear dynamics, neighbor coupling, adaptive edge activation, and metric deformation, with no collective statistic in any transition equation.

### $M_F$ — collective feedback

$$
c(x)=\frac13\sum_{i=1}^{3}x_i^2,
$$

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

Licensed description:

> **implemented prototype-level downward feedback/constraint with adaptive relational geometry**

This does not establish macro-level causal autonomy.

### $M_P$ — projected admissibility

Contract v1.0 implements the constant-amplitude sandbox

$$
\Gamma(Z)=c(x)-c_0
=\frac13x^Tx-c_0=0,
\qquad
c_0=c(x(0))\ge10^{-6},
$$

with node projection

$$
\boxed{
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The implementation includes projection at every RK4 stage, mandatory radial retraction, fail-closed singular handling, mechanism diagnostics, and an independently written reference path.

This is a **software-verified constant-amplitude projection prototype**, not ARG's completed relational-admissibility geometry and not a validated physical model.

### $M_{FP}$ — next implementation gate

Feedback followed by projection remains unimplemented and unverified.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP}\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

ARG does not assume

$$
M_F\equiv M_P.
$$

## Phase 3 software verification

The merged $M_P$ slice verifies:

- projector symmetry, idempotence, and $P_Tx=0$;
- continuous-time tangency $x^Tf_P=0$;
- projected RK4 stages;
- mandatory retraction to $c(x)=c_0$;
- zero-norm and near-singular fail-closed behavior;
- permutation equivariance;
- production/reference derivative and projected-step parity;
- decreasing one-step raw drift and retraction magnitude under refinement;
- retention of all prior $M_0/M_F$ regressions.

Verification record:

- PR `#5`;
- squash merge `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`;
- GitHub Actions run `30717582276`;
- **35 tests passed** on Python 3.10;
- **35 tests passed** on Python 3.12.

These are software tests, not scientific observations.

## What this project is—and is not

This project is:

- a candidate synthesis of established mathematical ideas;
- an executable family separating local dynamics, collective feedback, and explicit projection;
- a phase-gated program for fair mechanism comparison;
- a source of explicit proof obligations, baselines, diagnostics, and falsification tests.

This project is not presently:

- evidence that feedback and projection are equivalent;
- an implementation of $M_{FP}$;
- validation that projection improves prediction;
- validation of macro-level causal autonomy or strong emergence;
- a claim of a new fundamental geometry;
- a completed physical theory;
- evidence that reality literally is a graph, manifold, constraint surface, or computational structure.

## Repository map

### Foundations

- `docs/00_scope_and_status.md` — exact scope and claim discipline.
- `docs/01_apophatic_meta_axiom.md` — interpretive non-reification schema.
- `docs/02_design_requirements.md` — target requirements.
- `docs/03_formalism.md` — model family and mechanism definitions.
- `docs/04_minimal_model.md` — original $M_F$ prototype.
- `docs/05_proof_obligations.md` — model-specific obligations.
- `docs/06_experimental_plan.md` — four-model comparison plan.

### Research grounding and execution

- `docs/07_research_grounding_plan.md`
- `docs/08_claim_ledger.md`
- `docs/09_novelty_matrix.md`
- `docs/10_literature_landscape.md`
- `docs/11_benchmark_specification.md`
- `docs/12_falsification_criteria.md`
- `docs/13_alignment_and_claim_ceiling.md`
- `docs/14_roadmap.md`
- `docs/15_four_model_design_contract.md`
- `docs/16_phase3_mp_verification.md`

### Implementation and tests

- `src/apophatic_geometry/model.py` — legacy $M_F$ equation path retained for regression stability.
- `src/apophatic_geometry/models.py` — canonical $M_0/M_F/M_P$ dispatch, projection, diagnostics, and RK4.
- `tests/reference_equations.py` — independently written reference equations and integrators.
- `tests/` — software verification and tripwires.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
python -m apophatic_geometry.simulate --model m0 --steps 2000 --dt 0.005 --output m0.csv
python -m apophatic_geometry.simulate --model mf --steps 2000 --dt 0.005 --output mf.csv
python -m apophatic_geometry.simulate --model mp --steps 2000 --dt 0.005 --output mp.csv
```

## Roadmap position

**Phases 0–3 are complete. Phase 4 is in progress.**

The next gate implements

$$
M_{FP}:\qquad F_{\mathrm{proposal}}=F_0+F_F
$$

followed by projection. Contract v1.0 predicts

$$
\boxed{f_{FP}=f_P}
$$

for node derivatives because the radial node-feedback term is annihilated, while feedback remains in the $s$ and $q$ equations.

## Research maxim

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

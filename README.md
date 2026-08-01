# Apophatic Relational Geometry

> **Status: Candidate synthesis — not a claim of a new fundamental geometry.**
>
> ARG investigates whether nonlinear dynamics, adaptive networks, state-dependent geometry, collective feedback, local-to-global compatibility, and constrained dynamics can be combined into a coherent and useful framework. Mathematical novelty, explanatory value, and physical relevance remain open research questions.

## Current executable status

The repository now implements two matched three-node prototypes.

### $M_0$ — local/adaptive baseline

$$
\dot x_i
=
\alpha x_i-\beta x_i^3
+
\sum_{j\ne i}w_{ij}(x_j-x_i),
$$

with adaptive $s_{ij}$ and $q_{ij}$ dynamics but no collective statistic in any transition equation.

### $M_F$ — collective feedback

$$
c(x)=\frac13\sum_{i=1}^{3}x_i^2,
$$

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

This supports the narrow description:

> **implemented prototype-level downward feedback/constraint with adaptive relational geometry**

Neither executable currently implements $\Gamma/H$ admissibility projection.

The binding claim ceiling is

$$
\boxed{
M_0,M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Target model family

### $M_0$ — implemented

Local/adaptive dynamics without collective feedback or projection.

### $M_F$ — implemented

The $M_0$ substrate plus endogenous collective feedback.

### $M_P$ — Phase 3 target

Version 1.0 freezes a minimal constant-amplitude projection sandbox:

$$
\Gamma(Z)=c(x)-c_0=0,
\qquad
c_0=c(x(0))>0.
$$

Implementation, preservation, and code-equation parity remain unverified.

### $M_{FP}$ — later target

Feedback plus projection with separate mechanism diagnostics. It remains unimplemented and unverified.

ARG does not assume

$$
M_F\equiv M_P.
$$

## Phase 2 software verification

The merged $M_0$ slice includes:

- canonical four-model identifiers with fail-closed projected-model dispatch;
- exact $M_0$ equations;
- unchanged legacy $M_F$ right-hand side;
- shared fixed-step RK4;
- model ID and contract-version output labels;
- independent derivative and RK4 reference paths;
- exact zero-feedback reduction tests;
- permutation, dependency, regression, and invalid-input tripwires.

A clean local reconstruction passed **20 software tests**. No hosted check run was attached at merge time. This is not a scientific experiment.

## What this project is—and is not

This project is:

- a candidate synthesis of established mathematical ideas;
- an executable matched pair of local/adaptive and collective-feedback prototypes;
- a phase-gated program for defining and testing projection separately from feedback;
- a source of explicit proof obligations, baselines, ablations, and falsification tests.

This project is not presently:

- an implementation of global-admissibility projection;
- evidence that feedback and projection are equivalent;
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

### Implementation and tests

- `src/apophatic_geometry/model.py` — legacy $M_F$ implementation retained for regression stability.
- `src/apophatic_geometry/models.py` — canonical dispatch, $M_0$, feedback diagnostics, and shared RK4.
- `tests/reference_equations.py` — independently written derivative and integrator reference path.
- `tests/` — software verification and tripwires.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
python -m apophatic_geometry.simulate --model m0 --steps 2000 --dt 0.005 --output m0.csv
python -m apophatic_geometry.simulate --model mf --steps 2000 --dt 0.005 --output mf.csv
```

## Roadmap position

**Phases 0–2 are complete. Phase 3 is in progress.**

The next gate is implementation and independent verification of $M_P$:

- tangent projection;
- projected RK4 stages;
- mandatory radial retraction;
- preservation and tangency diagnostics;
- singular fail-closed behavior;
- independent parity and step-refinement tests.

## Research maxim

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

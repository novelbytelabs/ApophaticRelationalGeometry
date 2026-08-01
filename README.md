# Apophatic Relational Geometry

> **Status: Candidate synthesis — not a claim of a new fundamental geometry.**
>
> ARG investigates whether established ideas from nonlinear dynamics, adaptive networks, state-dependent geometry, collective feedback, local-to-global compatibility, and constrained dynamics can be combined into a coherent and useful framework. Mathematical novelty, explanatory value, and physical relevance remain open research questions.

## Current executable status

The repository currently implements the three-node **collective-feedback prototype** $M_F$:

$$
c(x)=\frac13\sum_{i=1}^{3}x_i^2,
$$

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

This supports the narrow description:

> **implemented prototype-level downward feedback/constraint with adaptive relational geometry**

The executable does **not** currently define $\Gamma$, $H$, an admissible tangent space, or a projection operator.

The binding claim ceiling is

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Target model family

### $M_0$ — local/adaptive baseline

No collective feedback and no admissibility projection. This is the next implementation gate.

### $M_F$ — collective feedback

A substrate-computed statistic enters constituent transition equations. This is the current executable.

### $M_P$ — projected admissibility

Version 1.0 freezes a minimal constant-amplitude projection sandbox:

$$
\Gamma(Z)=c(x)-c_0=0,
\qquad
c_0=c(x(0))>0.
$$

This remains unimplemented and unverified.

### $M_{FP}$ — feedback plus projection

Both mechanisms are present and separately measurable. This remains unimplemented and unverified.

ARG does not assume

$$
M_F\equiv M_P.
$$

## What this project is—and is not

This project is:

- a candidate synthesis of established mathematical ideas;
- an executable prototype of endogenous collective feedback and adaptive relational geometry;
- a phase-gated program to define, prove, implement, and compare feedback and projection mechanisms;
- a source of explicit proof obligations, baselines, ablations, and falsification tests;
- an investigation into whether the combined framework yields a new theorem, invariant, dynamical regime, or predictive advantage.

This project is not presently:

- an implementation of global-admissibility projection;
- evidence that feedback and projection are equivalent;
- validation of macro-level causal autonomy or strong emergence;
- a claim of a new fundamental geometry;
- a completed physical theory;
- evidence that reality literally is a graph, manifold, constraint surface, or computational structure;
- a claim that combining known mechanisms is itself a scientific breakthrough.

## Core commitments

- Mechanisms are named and tested separately.
- Local states, relations, metric variables, and collective modes may coevolve.
- Node labels and coordinate choices carry no physical privilege.
- Projection claims remain fail-closed until explicit constraints, implementation, preservation tests, code-equation parity, and substrate-path identification pass.
- Software tests validate implementation contracts, not scientific hypotheses.
- Stronger claims require mathematical proof, primary-source comparison, matched alternatives, and falsifiable experiments.
- The formalism is not identified with absolute reality.

## Repository map

### Foundations

- `docs/00_scope_and_status.md` — exact current scope and claim ceiling.
- `docs/01_apophatic_meta_axiom.md` — the interpretive non-reification schema.
- `docs/02_design_requirements.md` — requirements the target geometry must satisfy.
- `docs/03_formalism.md` — target family and mechanism definitions.
- `docs/04_minimal_model.md` — current executable $M_F$ prototype.
- `docs/05_proof_obligations.md` — model-specific theorem and verification obligations.
- `docs/06_experimental_plan.md` — four-model comparison plan.

### Research grounding and execution

- `docs/07_research_grounding_plan.md` — path from prototype to evidence.
- `docs/08_claim_ledger.md` — status and evidence requirements for every major claim.
- `docs/09_novelty_matrix.md` — comparison framework for neighboring work.
- `docs/10_literature_landscape.md` — primary-source research tracks.
- `docs/11_benchmark_specification.md` — frozen comparison and fairness rules.
- `docs/12_falsification_criteria.md` — conditions that narrow or reject claims.
- `docs/13_alignment_and_claim_ceiling.md` — canonical feedback/projection split.
- `docs/14_roadmap.md` — phase-gated execution roadmap.
- `docs/15_four_model_design_contract.md` — frozen version 1.0 model contract.

### Decisions, implementation, and tests

- `docs/adr/0001-separate-math-from-ontology.md` — architectural decision record.
- `docs/history/negation_operator_path.md` — archived path that motivated the meta-axiom.
- `src/apophatic_geometry/` — executable reference implementation of current $M_F$.
- `tests/` — software invariance, metric, and numerical sanity tests.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
python -m apophatic_geometry.simulate --steps 2000 --dt 0.005 --output run.csv
```

## Roadmap position

**Phase 0 and Phase 1 are complete. Phase 2 is in progress.**

The four-model contract is frozen as version 1.0 with:

- exact $M_0,M_F,M_P,M_{FP}$ definitions;
- shared fixed-step RK4 integration;
- mandatory retraction for projected models;
- fail-closed singular handling;
- fixed observation maps and independent-reference requirements;
- the exact version 1.0 prediction $f_{FP}=f_P$ for node derivatives.

The active task is implementation and verification of the true $M_0$ baseline while preserving current $M_F$ behavior.

Immediate sequence:

1. implement and independently verify $M_0$;
2. update the claim ledger only after its gate passes;
3. implement and verify $M_P$;
4. implement and verify $M_{FP}$;
5. freeze the comparative experiment protocol;
6. run a development pilot;
7. authorize a confirmatory run only after all tripwires pass.

## Research maxim

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

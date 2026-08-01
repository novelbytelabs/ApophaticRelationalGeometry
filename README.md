# Apophatic Relational Geometry

> **Status: Candidate synthesis — not a claim of a new fundamental geometry.**
>
> This repository investigates whether established ideas from constrained dynamics, adaptive networks, state-dependent geometry, local-to-global compatibility, and relational modeling can be combined into a coherent and useful framework. The project does **not** currently claim that this synthesis is mathematically novel, that it is a fundamental theory of physics, or that it identifies the structure or substance of reality. Novelty, explanatory value, and physical relevance must be established through primary-source comparison, mathematical proof, and falsifiable experiments.

A research program for a candidate nonlinear, dynamic relational constraint formalism in which local states and local rules generate proposed motion, while global coherence removes inadmissible motion.

The project separates two layers:

1. **Mathematical layer:** a concrete, testable candidate synthesis of dynamic relational and constrained-dynamical mechanisms.
2. **Interpretive layer:** an apophatic non-reification schema that forbids identifying any internal mathematical object with absolute reality.

The central dynamical form is

$$
\dot Z
=
F_{\mathrm{local}}(Z)
-
\Pi_{N_Z\mathcal M}F_{\mathrm{local}}(Z),
$$

where local dynamics propose change and the global admissible geometry removes the component incompatible with coherence.

## What this project is—and is not

This project is:

- a candidate synthesis of existing mathematical ideas;
- a framework to be compared directly with neighboring established theories;
- a source of explicit proof obligations, baselines, ablations, and falsification tests;
- an investigation into whether the combined framework yields any genuinely new theorem, invariant, dynamical regime, or predictive advantage.

This project is not presently:

- a claim of a new fundamental geometry;
- a completed physical theory;
- evidence that reality literally is a graph, manifold, constraint surface, or computational structure;
- a claim that combining known mechanisms is itself a scientific breakthrough.

## Core commitments

- No fixed background geometry is assumed within the candidate model.
- Local states, relations, metric variables, and collective modes may coevolve.
- Local neighborhoods provide direct causal influence.
- Global constraints delimit admissible collective motion.
- The whole is not a separate controller; it is represented by the jointly compatible configuration.
- Node labels and coordinate choices carry no physical privilege.
- The formalism is a hypothesis and modeling framework, not an identification with reality itself.
- Stronger claims require demonstrated novelty, mathematical consistency, and empirical discrimination from existing models.

## Repository map

### Foundations

- `docs/00_scope_and_status.md` — what the project claims and does not claim.
- `docs/01_apophatic_meta_axiom.md` — the interpretive non-reification schema.
- `docs/02_design_requirements.md` — requirements the geometry must satisfy.
- `docs/03_formalism.md` — mathematical definitions.
- `docs/04_minimal_model.md` — the first explicit three-node system.
- `docs/05_proof_obligations.md` — theorems and checks required before strong claims.
- `docs/06_experimental_plan.md` — falsification-oriented experiments and ablations.

### Research grounding

- `docs/07_research_grounding_plan.md` — staged path from proposal to evidence.
- `docs/08_claim_ledger.md` — status and evidence requirements for every major claim.
- `docs/09_novelty_matrix.md` — comparison framework for established neighboring work.
- `docs/10_literature_landscape.md` — primary-source research tracks and intake protocol.
- `docs/11_benchmark_specification.md` — fixed baselines, measurements, and fairness rules.
- `docs/12_falsification_criteria.md` — conditions that weaken, narrow, or reject the hypotheses.

### Decisions, implementation, and tests

- `docs/adr/0001-separate-math-from-ontology.md` — architectural decision record.
- `docs/history/negation_operator_path.md` — archived path that motivated the meta-axiom.
- `src/apophatic_geometry/` — executable reference implementation.
- `tests/` — invariance, metric, and numerical sanity tests.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
python -m apophatic_geometry.simulate --steps 2000 --dt 0.005 --output run.csv
```

## Current status

The repository begins with a specified minimal model and executable tests. It does **not** yet establish mathematical novelty, a new fundamental geometry, or a description of physical reality. Its current status is **candidate synthesis under investigation**.

The immediate goals are to:

- determine how much of the framework is already contained in established research;
- prove or disprove its mathematical consistency claims;
- compare it fairly with simpler and neighboring models;
- identify whether the synthesis produces any distinct, reproducible result;
- narrow or reject the hypothesis when the evidence requires it.

## Research maxim

> Construct freely. Test rigorously. Reify nothing.

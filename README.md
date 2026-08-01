# Apophatic Relational Geometry

A research program for a nonlinear, dynamic geometry in which local states and local rules generate proposed motion, while global coherence removes inadmissible motion.

The project separates two layers:

1. **Mathematical layer:** a concrete, testable dynamic relational constraint geometry.
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

## Core commitments

- No fixed background geometry is assumed.
- Local states, relations, metric variables, and collective modes may coevolve.
- Local neighborhoods provide direct causal influence.
- Global constraints delimit admissible collective motion.
- The whole is not a separate controller; it is realized by the jointly compatible configuration.
- Node labels and coordinate choices carry no physical privilege.
- The formalism is a hypothesis and modeling framework, not an identification with reality itself.

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

The repository begins with a fully specified minimal model and executable tests. It does **not** yet establish that the geometry describes physical reality. The immediate goals are mathematical consistency, numerical stability, identifiable mechanisms, falsifiable predictions, and a primary-source novelty audit.

## Research maxim

> Construct freely. Test rigorously. Reify nothing.

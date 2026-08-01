# Apophatic Relational Geometry

> **Status: candidate synthesis — not a claim of a new fundamental geometry.**

ARG investigates whether nonlinear local dynamics, adaptive relations, state-dependent geometry, endogenous collective feedback, and explicit admissibility projection can form a coherent and scientifically useful framework. Mathematical novelty, physical relevance, and explanatory value remain open.

## Implemented four-model family

### $M_0$ — local/adaptive baseline

Local nonlinear dynamics, neighbor coupling, adaptive edge activation, and metric deformation, with no collective statistic entering a transition equation.

### $M_F$ — collective feedback

$$
c(x)=\frac13\sum_{i=1}^{3}x_i^2,
\qquad
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

Licensed description:

> **implemented prototype-level downward feedback/constraint with adaptive relational geometry**

This does not establish macro-level causal autonomy.

### $M_P$ — projected admissibility

Contract v1.0 implements

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
$$

$$
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

The implementation projects every RK4 stage, applies mandatory radial retraction, fails closed near rank loss, exposes mechanism diagnostics, and agrees with an independently written software reference at tested cases.

### $M_{FP}$ — feedback followed by projection

$$
F_{\mathrm{proposal}}=F_0+F_F
$$

is followed by the same node projection and retraction policy as $M_P$.

At the same regular full state,

$$
\boxed{f_{FP}=f_P}
$$

because the node-feedback term is radial and $P_Tx=0$. This is not trajectory equivalence: $M_{FP}$ retains feedback in $s$ and $q$, which can change later conductances and node proposals.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

No implemented result establishes scientific superiority, physical adequacy, strong emergence, macro-level causal autonomy, mathematical novelty, or a fundamental geometry.

## Frozen Phase 5 protocol

Protocol `ARG-P5-COMP-v1` is frozen before trajectory generation. Its primary question is whether $M_F$ and $M_P$ are dynamically distinguishable under the full-state map.

It freezes:

- a symmetric normalized RMS trajectory metric;
- detection threshold `0.02` and scoped-equivalence margin `0.002`;
- direction-level inferential units;
- 24 deterministic directions and five amplitude conditions;
- 10 pilot directions and 14 held-out confirmatory directions;
- fixed parameters with no tuning;
- RK4 refinement and segmented DOP853 replication;
- numerical floors, missing-run rules, stop rules, and provenance;
- executable bootstrap and fail-closed decision logic;
- a SHA-256 lock over critical protocol and analysis files.

Hosted verification reported **65 passing tests** on Python 3.10 and **65 passing tests** on Python 3.12. No trajectory or scientific result was produced.

Current authorization:

$$
\boxed{
\text{development pilot authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

Authorization is not execution. The development pilot has not run.

## What this project is—and is not

ARG is:

- a candidate synthesis of established mathematical ingredients;
- an executable family separating local dynamics, feedback, projection, and their combination;
- a phase-gated research program with explicit proof obligations and falsification criteria;
- a preregistered mechanism-comparison framework.

ARG is not presently:

- evidence that feedback and projection are equivalent;
- validation that any mechanism improves prediction;
- evidence of macro-level causal autonomy or strong emergence;
- a completed physical theory;
- proof that reality literally is a graph, manifold, constraint surface, or computational structure.

## Repository map

### Foundations

- `docs/00_scope_and_status.md`
- `docs/01_apophatic_meta_axiom.md`
- `docs/02_design_requirements.md`
- `docs/03_formalism.md`
- `docs/04_minimal_model.md`
- `docs/05_proof_obligations.md`
- `docs/06_experimental_plan.md`

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
- `docs/17_phase4_mfp_verification.md`
- `docs/18_phase5_comparative_protocol.md`
- `protocol/phase5_v1/` — frozen machine-readable protocol bundle and lock.

### Implementation and tests

- `src/apophatic_geometry/model.py` — legacy $M_F$ equation path retained for regression stability.
- `src/apophatic_geometry/models.py` — canonical four-model equations, projection, diagnostics, and RK4.
- `src/apophatic_geometry/protocol.py` — frozen Phase 5 metrics, bootstrap, validation, hashing, and decision rules.
- `tests/reference_equations.py` — independently written reference equations and integrators.
- `tests/` — software, mathematical-contract, and protocol tripwires.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
python -m apophatic_geometry.simulate --model m0 --steps 2000 --dt 0.005 --output m0.csv
python -m apophatic_geometry.simulate --model mf --steps 2000 --dt 0.005 --output mf.csv
python -m apophatic_geometry.simulate --model mp --steps 2000 --dt 0.005 --output mp.csv
python -m apophatic_geometry.simulate --model mfp --steps 2000 --dt 0.005 --output mfp.csv
```

## Roadmap position

**Phases 0–5 are complete. Phase 6 is the active implementation gate.**

Phase 6 must implement and independently verify a pilot-only runner, immutable archive, numerical replication, and confirmatory-access tripwires. No pilot has yet been executed.

## Research maxim

> Separate the mechanisms. Freeze the contracts. Test the alternatives. Reify nothing.

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

Contract v1.0 implements

$$
\Gamma(Z)=c(x)-c_0
=\frac13x^Tx-c_0=0,
$$

with node projection

$$
\boxed{
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The implementation includes projection at every RK4 stage, mandatory radial retraction, fail-closed singular handling, separate diagnostics, and an independently written reference path.

### $M_{FP}$ — feedback followed by projection

The combined proposal is

$$
F_{\mathrm{proposal}}=F_0+F_F,
$$

followed by the same node-state projection and retraction policy as $M_P$.

At the same regular full state,

$$
\boxed{f_{FP}=f_P}
$$

because the node-feedback term is radial and $P_Tx=0$.

This same-state identity is not trajectory equivalence. $M_{FP}$ retains collective feedback in $s$ and $q$, which can alter later conductances and node proposals.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

The four-model implementation does not establish scientific superiority, physical adequacy, macro-level causal autonomy, strong emergence, or a new fundamental geometry.

## Phase 4 software verification

The merged $M_{FP}$ slice verifies:

- explicit $F_0$, $F_F$, and $F_0+F_F$ decomposition;
- radial node-feedback annihilation by projection;
- same-state identity $f_{FP}=f_P$;
- retained $s/q$ feedback;
- projected RK4 stages and mandatory retraction;
- fail-closed target and singular handling;
- permutation equivariance;
- production/reference derivative and projected-step parity;
- exact zero-feedback reduction to $M_P$;
- decreasing one-step raw drift and retraction magnitude under refinement;
- retention of every prior regression.

Verification record:

- PR `#7`;
- squash merge `205fb8c5bf1b832e241af230612e3d7056be05f5`;
- GitHub Actions run `30718821666`;
- **51 tests passed** on Python 3.10;
- **51 tests passed** on Python 3.12.

These are software and local mathematical-contract tests, not scientific observations.

## What this project is—and is not

This project is:

- a candidate synthesis of established mathematical ideas;
- an executable four-model family separating local dynamics, feedback, projection, and their combination;
- a phase-gated program for fair mechanism comparison;
- a source of explicit proof obligations, diagnostics, baselines, and falsification tests.

This project is not presently:

- evidence that feedback and projection are equivalent;
- evidence that same-state node equality implies trajectory equality;
- validation that any mechanism improves prediction;
- validation of macro-level causal autonomy or strong emergence;
- a claim of a new fundamental geometry;
- a completed physical theory;
- evidence that reality literally is a graph, manifold, constraint surface, or computational structure.

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

### Implementation and tests

- `src/apophatic_geometry/model.py` — legacy $M_F$ equation path retained for regression stability.
- `src/apophatic_geometry/models.py` — canonical four-model dispatch, projection, diagnostics, and RK4.
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
python -m apophatic_geometry.simulate --model mfp --steps 2000 --dt 0.005 --output mfp.csv
```

## Roadmap position

**Phases 0–4 are complete. Phase 5 is in progress.**

The active gate is the frozen four-model comparative experiment protocol. No development pilot is authorized until its hypotheses, observation maps, manifests, metrics, refinement rules, stop rules, and provenance policy are fixed.

## Research maxim

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

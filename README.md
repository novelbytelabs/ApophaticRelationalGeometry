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
\qquad
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

The implementation projects every RK4 stage, applies mandatory radial retraction, fails closed near rank loss, exposes mechanism diagnostics, and agrees with an independently written software reference at tested cases.

### $M_{FP}$ — feedback followed by projection

$$
F_{\mathrm{proposal}}=F_0+F_F
$$

is followed by the same node projection and retraction policy as $M_P$. At the same regular full state,

$$
\boxed{f_{FP}=f_P},
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

## Frozen protocol and verified pilot-only runner

Protocol `ARG-P5-COMP-v1` was frozen before trajectory generation. It fixes the hypotheses, effect and equivalence thresholds, direction-level inferential units, deterministic pilot/confirmatory split, fixed parameters, RK4 refinement, DOP853 replication, numerical floors, exclusions, stop rules, provenance, executable decision logic, and critical-file lock.

Phase 6 now implements and software-verifies a fail-closed runner for exactly the 50 frozen pilot configurations. The runner:

- verifies the Phase 5 lock before loading configurations;
- rejects confirmatory and mixed batches before integration;
- rejects confirmatory input independently in RK4, DOP853, and archive paths;
- runs all four models under the frozen numerical policy;
- implements the frozen controls and all six node-relabeling tripwires;
- writes a checksummed, write-once archive;
- requires a separate committed execution authorization naming a previously verified runner commit.

Hosted verification reported **100 passing tests** on Python 3.10 and **100 passing tests** on Python 3.12.

Current execution state:

$$
\boxed{
\text{runner verified};
\quad
\text{development pilot not executed};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

The verification slice contains no execution authorization, pilot trajectory, pilot result, pilot archive, or confirmatory artifact.

## What this project is—and is not

ARG is:

- a candidate synthesis of established mathematical ingredients;
- an executable family separating local dynamics, feedback, projection, and their combination;
- a phase-gated research program with explicit proof obligations and falsification criteria;
- a preregistered mechanism-comparison framework with a verified pilot-only runner.

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
- `docs/19_phase5_protocol_verification.md`
- `docs/20_phase6_runner_design.md`
- `docs/21_phase6_runner_verification.md`
- `protocol/phase5_v1/` — frozen protocol bundle and lock.
- `protocol/phase6_runner_v1/` — runner authorization boundary; no execution authorization is present.

### Implementation and tests

- `src/apophatic_geometry/model.py` — legacy $M_F$ equation path retained for regression stability.
- `src/apophatic_geometry/models.py` — canonical four-model equations, projection, diagnostics, and RK4.
- `src/apophatic_geometry/protocol.py` — frozen metrics, bootstrap, validation, hashing, and decisions.
- `src/apophatic_geometry/pilot.py` — gated pilot-only orchestration.
- `src/apophatic_geometry/pilot_*` — split authorization, integration, gates, controls, and archive modules.
- `tests/reference_equations.py` and `tests/reference_pilot.py` — independent verification paths.

## Data-free validation commands

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
arg-pilot validate --repo-root .
arg-pilot plan --repo-root .
```

`validate` and `plan` do not execute trajectories. `arg-pilot execute` fails closed because the separate execution authorization is intentionally absent.

## Roadmap position

**Phases 0–5 are complete. The Phase 6 runner gate has passed; pilot execution is the next separate gate.**

No development-pilot result or confirmatory result exists.

## Research maxim

> Separate the mechanisms. Freeze the contracts. Test the alternatives. Reify nothing.

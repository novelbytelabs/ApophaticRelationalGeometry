# Apophatic Relational Geometry

> **Status: candidate synthesis — not a claim of a new fundamental geometry.**

ARG investigates whether established results concerning nonlinear dynamics, adaptive relations, state-dependent geometry, collective feedback, constraints, persistence, scale, and representation can be organized into a coherent and scientifically useful synthesis. Mathematical novelty, physical relevance, explanatory value, and ontological implications remain open.

The governing research order is:

$$
\boxed{
\text{research first}
\;\longrightarrow\;
\text{synthesize second}
\;\longrightarrow\;
\text{formalize third}
\;\longrightarrow\;
\text{experiment only on the unresolved remainder}.
}
$$

## Two governed research tracks

### Consensus synthesis track

ARG now maintains a phenomenon-first cross-disciplinary program to determine what is already established, what is representation- or perspective-relative, where accepted evidence permits several interpretations, and what precise unresolved remainder—if any—still requires a theorem or experiment.

The first active slice is:

> **State, structure, representation, and persistence: a consensus synthesis.**

This track must not convert familiar dynamical results into ARG novelty claims. It produces a Consensus Atlas, Concept Translation Dictionary, Minimal ARG Core, Disagreement and Boundary Map, and Residual Research Agenda.

### Four-model implementation and experiment track

The existing executable family remains separately governed by frozen contracts, proof obligations, software tests, audit gates, and execution authorization.

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

## Frozen protocol and pilot-only runner

Protocol `ARG-P5-COMP-v1` was frozen before trajectory generation. It fixes the hypotheses, effect and equivalence thresholds, direction-level inferential units, deterministic pilot/confirmatory split, fixed parameters, RK4 refinement, DOP853 replication, numerical floors, exclusions, stop rules, provenance, executable decision logic, and critical-file lock.

Phase 6 implements a fail-closed runner for exactly the 50 frozen pilot configurations. The runner:

- verifies the Phase 5 lock before loading configurations;
- rejects confirmatory and mixed batches before integration;
- rejects confirmatory input independently in RK4, DOP853, and archive paths;
- runs all four models under the frozen numerical policy;
- implements the frozen controls and all six node-relabeling tripwires;
- writes a checksummed, write-once archive;
- requires a separate committed execution authorization naming a previously verified runner commit.

The original software gate reported 100 passing tests on Python 3.10 and 100 passing tests on Python 3.12. A later independent audit placed the runner track into Phase 6A.1 integrity remediation. The original test result does not override that stop-ship gate.

Current execution state:

$$
\boxed{
\text{Phase 6A.1 integrity remediation STOP-SHIP};
\quad
\text{development pilot not authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

No execution authorization, pilot trajectory, pilot result, pilot archive, or confirmatory artifact exists.

## What this project is—and is not

ARG is:

- a candidate convergence synthesis of established mathematical, scientific, and philosophical constraints;
- a disciplined program for translating perspectives without erasing their differences;
- an executable family separating local dynamics, feedback, projection, and their combination;
- a phase-gated research program with explicit proof obligations, claim ceilings, audits, and falsification criteria;
- a preregistered mechanism-comparison framework whose execution remains blocked.

ARG is not presently:

- evidence that feedback and projection are equivalent;
- validation that any mechanism improves prediction;
- evidence of macro-level causal autonomy or strong emergence;
- a completed physical theory;
- proof that reality literally is a graph, manifold, constraint surface, or computational structure;
- a claim that general state–structure dependence, transport, persistence, or relationality was discovered by ARG;
- permission to run experiments before checking whether their questions are already answered by established research.

## Repository map

### Foundations

- `docs/00_scope_and_status.md`
- `docs/01_apophatic_meta_axiom.md`
- `docs/02_design_requirements.md`
- `docs/03_formalism.md`
- `docs/04_minimal_model.md`
- `docs/05_proof_obligations.md`
- `docs/06_experimental_plan.md`

### Research grounding, consensus, and execution

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
- `docs/22_consensus_synthesis_program.md`
- `research/consensus/` — consensus workspace, active scopes, source notes, translations, and residual agendas.
- `protocol/phase5_v1/` — frozen protocol bundle and lock.
- `protocol/phase6_runner_v1/` — runner authorization boundary; no execution authorization is present.

### Papers

- `papers/persistence_without_substance.md` — Structured Becoming working paper.
- `papers/` — rendered working papers and diagrams; these remain working interpretations subject to the claim ledger and consensus audit.

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

- **Four-model track:** Phase 6A.1 integrity remediation is STOP-SHIP; pilot and confirmatory execution are blocked.
- **Consensus track:** CS0 governance is under review; CS1 state–structure–persistence literature audit is active.

Clearing software integrity would not by itself justify execution. The consensus and novelty audits may narrow or eliminate the scientific motivation for a proposed experiment.

## Research maxim

> Establish what is known. Translate without erasing differences. Preserve disagreement where evidence underdetermines interpretation. Formalize only the invariant core. Experiment only on the unresolved remainder. Reify nothing.

# Apophatic Relational Geometry

> **Status: candidate synthesis — not a claim of a new fundamental geometry.**

ARG investigates whether nonlinear local dynamics, adaptive relations, state-dependent geometry, endogenous collective feedback, and explicit admissibility projection can form a coherent and scientifically useful framework. Mathematical novelty, physical relevance, and explanatory value remain open.

## Consensus-led research program

ARG now follows this order:

$$
\boxed{
\text{research first}
\to
\text{synthesize second}
\to
\text{formalize third}
\to
\text{experiment only on the unresolved remainder}.
}
$$

The active CS1 audit studies state, structure, representation, and persistence across mathematics, dynamical systems, control, adaptive networks, evolving spaces, and philosophy.

The first three source baskets indicate that the following are established neighboring results rather than ARG discoveries:

- state- and initial-condition-dependent dynamics;
- nonmodal amplification and cancellation;
- coevolving state and topology;
- basin, invariant-manifold, metastable, and structural persistence;
- controllability, observability, balanced state importance, viability, and controlled invariance;
- explicit transport on smoothly evolving spaces;
- multiple inequivalent criteria of representation equivalence.

Current evidence supports a **typed family of relations**, not one universal `state–structure compatibility` scalar.

Scientific claims may require a context broader than a bare pair $(B,x)$, including the transition law, input map, output map, constraints, admissible controls, disturbances, measured functional, and horizon.

See:

- `docs/22_consensus_synthesis_program.md`
- `research/consensus/01_consensus_table.md`
- `research/consensus/01_translation_dictionary.md`

No persistence experiment is authorized by this research track.

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

## Frozen protocol and integrity stop-ship

Protocol `ARG-P5-COMP-v1` was frozen before trajectory generation. It fixes hypotheses, thresholds, direction-level inferential units, the pilot/confirmatory split, parameters, numerical replication, exclusions, stop rules, provenance, executable decision logic, and the critical-file lock.

The Phase 6A pilot-only runner passed its original software gate, but an independent audit identified integrity defects outside and around the nominal equations.

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

Passing the integrity gate would establish software trustworthiness only. It would not establish that the experiment remains scientifically necessary after the consensus audit.

## What this project is—and is not

ARG is:

- a candidate synthesis of established mathematical, scientific, and philosophical constraints;
- an executable family separating local dynamics, feedback, projection, and their combination;
- a phase-gated research program with explicit proof obligations and falsification criteria;
- a consensus-led audit designed to prevent rediscovery and reification.

ARG is not presently:

- evidence that feedback and projection are equivalent;
- validation that any mechanism improves prediction;
- evidence of macro-level causal autonomy or strong emergence;
- a completed physical theory;
- proof that reality literally is a graph, manifold, constraint surface, or computational structure;
- evidence that persistence is one universal quantity;
- evidence that a structure–state pair is a representation-independent ontology.

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
- `docs/22_consensus_synthesis_program.md`
- `protocol/phase5_v1/` — frozen protocol bundle and lock.
- `protocol/phase6_runner_v1/` — runner authorization boundary; no execution authorization is present.

### Consensus workspace

- `research/consensus/01_state_structure_persistence_scope.md`
- `research/consensus/01_consensus_table.md`
- `research/consensus/01_translation_dictionary.md`
- `research/consensus/source_note_template.md`
- `research/consensus/sources/`

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

`validate` and `plan` do not execute trajectories. Execution remains blocked by the Phase 6A.1 stop-ship state and the absent scientific authorization.

## Roadmap position

Two governed tracks are active:

1. **software integrity:** Phase 6A.1 STOP-SHIP;
2. **consensus synthesis:** CS1 active, with three source baskets entered.

The next CS1 basket covers transport and structural change: connections, reset maps, remeshing, graph correspondence, and noninvertible transitions.

## Research maxim

> Establish what is known. Translate without erasing. Preserve disagreement. Test only the remainder. Reify nothing.

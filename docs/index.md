# Apophatic Relational Geometry

ARG is a candidate synthesis of nonlinear local dynamics, adaptive relational geometry, endogenous collective feedback, and projected constraint mechanisms.

It is not a claim of a new fundamental geometry or a description of absolute reality.

## Implemented prototypes

### $M_0$

Local/adaptive baseline with no collective-statistic transition path.

### $M_F$

Endogenous collective feedback:

$$
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

Only $M_F$ supports the narrow description:

> **implemented prototype-level downward feedback/constraint**

### $M_P$

Constant-amplitude projection sandbox:

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
\qquad
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

### $M_{FP}$

Feedback followed by projection:

$$
F_{\mathrm{proposal}}=F_0+F_F.
$$

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

while feedback remains in $s$ and $q$. Same-state node identity therefore does not imply trajectory identity.

The projected models use projected RK4 stages, mandatory radial retraction, fail-closed singular handling, separate diagnostics, and independent software-reference parity. They are mechanism sandboxes, not validated physical laws.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Frozen comparative protocol

Phase 5 froze protocol `ARG-P5-COMP-v1` before generating trajectories. It fixes hypotheses, effect and equivalence thresholds, observation maps, 24 direction-level units, pilot/confirmatory separation, parameters, RK4 refinement, DOP853 replication, exclusions, stop rules, provenance, executable metrics, and a SHA-256 lock.

Hosted verification reported **65 passing tests** on Python 3.10 and **65 passing tests** on Python 3.12.

Current authorization:

$$
\boxed{
\text{development pilot authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

No pilot has been executed.

## Foundations

- [Scope and status](00_scope_and_status.md)
- [Apophatic meta-axiom](01_apophatic_meta_axiom.md)
- [Design requirements](02_design_requirements.md)
- [Formalism and mechanism split](03_formalism.md)
- [Original minimal model: $M_F$](04_minimal_model.md)
- [Proof obligations](05_proof_obligations.md)
- [Experimental plan](06_experimental_plan.md)

## Research grounding and execution

- [Research grounding plan](07_research_grounding_plan.md)
- [Claim ledger](08_claim_ledger.md)
- [Novelty matrix](09_novelty_matrix.md)
- [Literature landscape](10_literature_landscape.md)
- [Benchmark specification](11_benchmark_specification.md)
- [Falsification criteria](12_falsification_criteria.md)
- [Canonical alignment and claim ceiling](13_alignment_and_claim_ceiling.md)
- [Phase-gated roadmap](14_roadmap.md)
- [Four-model design contract v1.0](15_four_model_design_contract.md)
- [Phase 3 $M_P$ verification record](16_phase3_mp_verification.md)
- [Phase 4 $M_{FP}$ verification record](17_phase4_mfp_verification.md)
- [Phase 5 comparative protocol v1.0](18_phase5_comparative_protocol.md)

## Current roadmap position

**Phases 0–5 are complete. Phase 6 is active.**

Phase 6 must implement and independently verify the pilot-only runner and immutable archival pipeline. Confirmatory configurations remain inaccessible and no pilot has run.

> Separate the mechanisms. Freeze the contracts. Test the alternatives. Reify nothing.

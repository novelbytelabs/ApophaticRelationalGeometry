# Apophatic Relational Geometry

ARG is a candidate synthesis of nonlinear local dynamics, adaptive relational geometry, collective feedback, and projected constraint mechanisms.

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

Software-verified constant-amplitude projection sandbox:

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
$$

$$
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

### $M_{FP}$

Software-verified feedback-followed-by-projection prototype:

$$
F_{\mathrm{proposal}}=F_0+F_F.
$$

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

while $M_{FP}$ retains collective feedback in $s$ and $q$. The same-state identity therefore does not imply identical trajectories.

The projected models use projected RK4 stages, mandatory radial retraction, fail-closed singular handling, separate diagnostics, and independent software-reference parity.

They are not the completed relational-admissibility geometry and have not been scientifically validated.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Foundations

- [Scope and status](00_scope_and_status.md)
- [Apophatic meta-axiom](01_apophatic_meta_axiom.md)
- [Design requirements](02_design_requirements.md)
- [Formalism and mechanism split](03_formalism.md)
- [Original minimal model: $M_F$](04_minimal_model.md)
- [Proof obligations](05_proof_obligations.md)
- [Four-model experimental plan](06_experimental_plan.md)

## Research grounding and execution

- [Research grounding plan](07_research_grounding_plan.md)
- [Claim ledger](08_claim_ledger.md)
- [Novelty matrix](09_novelty_matrix.md)
- [Literature landscape](10_literature_landscape.md)
- [Benchmark specification](11_benchmark_specification.md)
- [Falsification criteria](12_falsification_criteria.md)
- [Canonical alignment and claim ceiling](13_alignment_and_claim_ceiling.md)
- [Phase-gated roadmap](14_roadmap.md)
- [Frozen four-model design contract v1.0](15_four_model_design_contract.md)
- [Phase 3 $M_P$ verification record](16_phase3_mp_verification.md)
- [Phase 4 $M_{FP}$ verification record](17_phase4_mfp_verification.md)

## Current roadmap position

**Phases 0–4 are complete. Phase 5 is in progress.**

Phase 4 merged through PR `#7`. GitHub Actions reported **51 passing tests** on both Python 3.10 and Python 3.12.

The active task is to freeze the comparative experiment protocol. No development pilot is authorized until the hypotheses, observation maps, manifests, metrics, solver/refinement policy, stop rules, and provenance requirements are fixed.

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

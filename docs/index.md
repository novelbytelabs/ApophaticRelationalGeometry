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

It uses projected RK4 stages, mandatory radial retraction, fail-closed singular handling, and independent software-reference parity.

It is not the completed relational-admissibility geometry and has not been scientifically validated.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP}\ \text{and }M_F\equiv M_P\ \text{unverified}.
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

## Current roadmap position

**Phases 0–3 are complete. Phase 4 is in progress.**

Phase 3 merged the $M_P$ implementation through PR `#5`. GitHub Actions reported **35 passing tests** on both Python 3.10 and Python 3.12.

The active target is

$$
M_{FP}:\quad
F_{\mathrm{proposal}}=F_0+F_F,
$$

followed by the existing projection. Contract v1.0 predicts

$$
\boxed{f_{FP}=f_P}
$$

for node derivatives, while $s$ and $q$ retain collective-feedback terms.

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

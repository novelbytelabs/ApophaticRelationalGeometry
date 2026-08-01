# Apophatic Relational Geometry

ARG is a candidate research synthesis of nonlinear local dynamics, adaptive relational geometry, collective feedback, and projected constraint mechanisms.

It is not presently a claim of a new fundamental geometry or a description of absolute reality.

## Current executables

### $M_0$

A local/adaptive baseline with no collective statistic in its transition equations.

### $M_F$

A matched collective-feedback prototype:

$$
c(x)=\frac13\sum_i x_i^2,
$$

$$
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

Only $M_F$ supports the narrow label:

> **implemented prototype-level downward feedback/constraint**

Neither model implements $\Gamma/H$ admissibility projection.

## Binding claim ceiling

$$
\boxed{
M_0,M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Canonical model family

- $M_0$: implemented local/adaptive no-feedback baseline.
- $M_F$: implemented endogenous collective-feedback prototype.
- $M_P$: frozen constant-amplitude projection sandbox; Phase 3 implementation target.
- $M_{FP}$: feedback plus projection; unimplemented.

## Foundations

- [Scope and status](00_scope_and_status.md)
- [Apophatic meta-axiom](01_apophatic_meta_axiom.md)
- [Design requirements](02_design_requirements.md)
- [Target formalism and mechanism split](03_formalism.md)
- [Original minimal model: $M_F$](04_minimal_model.md)
- [Model-specific proof obligations](05_proof_obligations.md)
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

## Phase 2 software result

The merged $M_0$ slice added:

- canonical dispatch;
- exact no-feedback equations;
- shared RK4;
- independent derivative and integrator references;
- exact reduction and regression tests;
- fail-closed projected-model dispatch;
- model and contract labels in outputs.

A clean local reconstruction passed 20 software tests. No hosted check run was attached at merge time. This is not a scientific result.

## Current roadmap position

**Phases 0–2 are complete. Phase 3 is in progress.**

The active task is implementation and independent verification of

$$
M_P:\qquad
\Gamma(Z)=c(x)-c_0=0,
\qquad
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

The gate requires projection identities, tangent preservation, mandatory radial retraction, singular fail-closed behavior, independent parity, and step-refinement evidence.

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

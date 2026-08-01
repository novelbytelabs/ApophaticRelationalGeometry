# Apophatic Relational Geometry

ARG is a candidate research synthesis of nonlinear local dynamics, adaptive relational geometry, collective feedback, and projected constraint mechanisms.

It is not presently a claim of a new fundamental geometry or a description of absolute reality.

## Current executable

The current three-node implementation is the collective-feedback prototype $M_F$:

$$
c(x)=\frac13\sum_i x_i^2,
$$

$$
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

It supports the narrow label:

> **implemented prototype-level downward feedback/constraint**

It does not yet implement $\Gamma/H$ admissibility projection.

## Binding claim ceiling

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Canonical model family

- $M_0$: local/adaptive baseline without collective feedback or projection.
- $M_F$: endogenous collective feedback; current executable.
- $M_P$: explicit projected admissibility; unimplemented.
- $M_{FP}$: feedback plus projection with separate diagnostics; unimplemented.

## Foundations

- [Scope and status](00_scope_and_status.md)
- [Apophatic meta-axiom](01_apophatic_meta_axiom.md)
- [Design requirements](02_design_requirements.md)
- [Target formalism and mechanism split](03_formalism.md)
- [Current minimal model: $M_F$](04_minimal_model.md)
- [Model-specific proof obligations](05_proof_obligations.md)
- [Four-model experimental plan](06_experimental_plan.md)

## Research grounding

- [Research grounding plan](07_research_grounding_plan.md)
- [Claim ledger](08_claim_ledger.md)
- [Novelty matrix](09_novelty_matrix.md)
- [Literature landscape](10_literature_landscape.md)
- [Benchmark specification](11_benchmark_specification.md)
- [Falsification criteria](12_falsification_criteria.md)
- [Canonical alignment and claim ceiling](13_alignment_and_claim_ceiling.md)
- [Phase-gated roadmap](14_roadmap.md)

## Decisions and history

- [Separate mathematics from ontology](adr/0001-separate-math-from-ontology.md)
- [Archived negation-operator path](history/negation_operator_path.md)

## Current roadmap position

ARG is at **Phase 0: alignment and claim control**.

Immediate priorities:

1. complete documentation alignment;
2. rerun and record existing software tests;
3. freeze the four-model design contract;
4. implement the true $M_0$ baseline;
5. design and prove $M_P$ before production implementation.

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Reify nothing.

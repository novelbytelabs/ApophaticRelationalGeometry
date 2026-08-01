# Apophatic Relational Geometry

ARG is a candidate synthesis of nonlinear local dynamics, adaptive relational geometry, endogenous collective feedback, and projected constraint mechanisms. It is not a claim of a new fundamental geometry or a description of absolute reality.

## Implemented prototypes

- $M_0$: local/adaptive baseline with no collective-statistic transition path.
- $M_F$: endogenous collective feedback through $x\to c(x)\to(\dot x,\dot s,\dot q)$.
- $M_P$: constant-amplitude projection sandbox on $\Gamma(Z)=\frac13x^Tx-c_0=0$.
- $M_{FP}$: feedback followed by projection, retaining feedback in $s$ and $q$.

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

but this does not imply trajectory identity.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Frozen protocol and verified runner

Protocol `ARG-P5-COMP-v1` was frozen before trajectory generation. Phase 6A now implements a fail-closed runner for exactly the 50 pilot configurations, with all-model RK4/DOP853 replication, H5/H6 gates, frozen controls, all six relabelings, independent references, and a write-once checksummed archive.

Hosted verification reported **100 passing tests** on Python 3.10 and **100 passing tests** on Python 3.12.

$$
\boxed{
\text{runner verified};
\quad
\text{development pilot not executed};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

No execution authorization, pilot trajectory, pilot result, pilot archive, or confirmatory artifact is present.

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
- [Phase 3 $M_P$ verification](16_phase3_mp_verification.md)
- [Phase 4 $M_{FP}$ verification](17_phase4_mfp_verification.md)
- [Phase 5 comparative protocol](18_phase5_comparative_protocol.md)
- [Phase 5 protocol verification](19_phase5_protocol_verification.md)
- [Phase 6 runner design](20_phase6_runner_design.md)
- [Phase 6 runner verification](21_phase6_runner_verification.md)

## Current roadmap position

**The Phase 6A runner gate has passed. Phase 6B pilot execution is the next separate gate.**

The execution slice must name the verified runner commit and may not alter protected protocol or runner files. Confirmatory configurations remain inaccessible.

> Separate the mechanisms. Freeze the contracts. Test the alternatives. Reify nothing.

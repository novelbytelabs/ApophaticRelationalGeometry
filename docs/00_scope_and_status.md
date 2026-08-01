# Scope and Status

## Research question

Can a system be modeled as one globally organized process and many locally real processes at the same time, without treating the whole as an external controller or the parts as independently fundamental?

## Candidate synthesis

ARG investigates combinations of

$$
\text{local nonlinear dynamics}
+
\text{adaptive relations}
+
\text{state-dependent metric}
+
\text{collective feedback}
+
\text{global admissibility projection}.
$$

These ingredients are distinct mechanisms and must be tested separately.

## Implemented mechanism split

### $M_0$: local/adaptive baseline

Local nonlinear dynamics, neighborhood coupling, adaptive edge activation, and metric deformation. The collective statistic may be logged but does not enter any transition equation.

### $M_F$: collective feedback

$$
c(x)=\frac13\sum_i x_i^2,
$$

$$
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

Licensed description:

> **implemented prototype-level downward feedback/constraint**

This does not establish macro-level causal autonomy.

### $M_P$: projected-admissibility sandbox

Contract v1.0 implements

$$
\Gamma(Z)=c(x)-c_0
=\frac13x^Tx-c_0=0,
$$

with

$$
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

The implementation projects every RK4 derivative stage, retracts each completed step radially to the manifold, records mechanism diagnostics, and fails closed near rank loss.

### $M_{FP}$: feedback followed by projection

The model constructs

$$
F_{\mathrm{proposal}}=F_0+F_F
$$

and projects the node proposal using the same $M_P$ policy.

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

because the node-feedback term is radial. $M_{FP}$ nevertheless retains collective feedback in $s$ and $q$, so its later trajectory need not equal $M_P$.

Both projected models are constant-amplitude mechanism sandboxes. They are not the final relational geometry and are not validated physical models.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## What is currently claimed

- All four contract-v1.0 prototypes are implemented through canonical dispatch.
- $M_0$ implements the no-feedback local/adaptive baseline.
- $M_F$ implements endogenous collective feedback through an explicit substrate path.
- $M_P$ implements the frozen constant-amplitude tangent projection and numerical retraction policy.
- $M_{FP}$ implements an explicit feedback proposal followed by node projection, with retained $s/q$ feedback.
- The declared reduction paths, projector identities, tangency, retraction, singular handling, permutation equivariance, and independent software-reference parity are unit-tested.
- Intrinsic edge lengths and graph distances are state dependent in all four prototypes.

## What is not currently claimed

- That collective feedback is dynamically or observationally equivalent to tangent-space projection.
- That same-state node equality implies trajectory equality.
- That prototype-level feedback or projection establishes macro-level causal autonomy.
- That any mechanism improves predictive performance.
- That constant amplitude is physically fundamental.
- That any implemented model defeats scientific alternatives.
- That organization dependence, counterfactual adequacy, transport, or empirical emergence has been demonstrated.
- That ARG is mathematically novel or a new fundamental geometry.
- That the universe literally is a graph, constraint manifold, or computational structure.
- That the implemented prototypes reproduce known physical laws.
- That the apophatic principle proves any religion or metaphysics.

## Verification scope

Phase 2 passed 20 local software tests for $M_0/M_F$.

Phase 3 passed 35 hosted tests on Python 3.10 and Python 3.12 for $M_0/M_F/M_P$.

Phase 4 passed 51 hosted tests on Python 3.10 and Python 3.12 for the complete four-model implementation.

These validate software and local mathematical contracts, not a scientific hypothesis. No comparative scientific experiment has been executed.

## Standard of progress

Progress requires:

- precise mechanism definitions;
- code-equation parity;
- mathematical proofs or explicit domain restrictions;
- matched baselines and ablations;
- independent reference implementations;
- falsifiable predictions;
- primary-source comparison;
- fail-closed claim control.

The binding alignment statement is `13_alignment_and_claim_ceiling.md`. The execution plan is `14_roadmap.md`.
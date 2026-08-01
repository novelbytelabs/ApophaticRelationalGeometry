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
\qquad
c_0=c(x(0))\ge10^{-6},
$$

with

$$
\boxed{
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The implementation projects every RK4 derivative stage, retracts each completed step radially to the manifold, records mechanism diagnostics, and fails closed near rank loss.

This is a constant-amplitude projection-mechanism sandbox. It is not the final relational geometry and is not a validated physical model.

### $M_{FP}$: combined target

Feedback followed by projection remains unimplemented and unverified.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP}\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## What is currently claimed

- $M_0$ implements the no-feedback local/adaptive baseline.
- $M_F$ implements endogenous collective feedback through an explicit substrate path.
- $M_P$ implements the frozen constant-amplitude tangent projection and numerical retraction policy.
- $M_F(\chi=\eta_2=\rho=0)=M_0$ is unit-tested.
- The $M_P$ projector identities, tangency, retraction, singular handling, permutation equivariance, and independent software-reference parity are unit-tested.
- Intrinsic edge lengths and graph distances are state dependent in all three implemented prototypes.

## What is not currently claimed

- That collective feedback is equivalent to tangent-space projection.
- That $M_{FP}$ is implemented.
- That prototype-level feedback or projection establishes macro-level causal autonomy.
- That projection improves predictive performance.
- That constant amplitude is physically fundamental.
- That any implemented model defeats scientific alternatives.
- That organization dependence, counterfactual adequacy, transport, or empirical emergence has been demonstrated.
- That ARG is mathematically novel or a new fundamental geometry.
- That the universe literally is a graph, constraint manifold, or computational structure.
- That the implemented prototypes reproduce known physical laws.
- That the apophatic principle proves any religion or metaphysics.

## Verification scope

Phase 2 passed 20 local software tests for $M_0/M_F$.

Phase 3 passed 35 hosted tests on Python 3.10 and the same 35 tests on Python 3.12 for $M_0/M_F/M_P$. These validate software and local mathematical contracts, not a scientific hypothesis.

No comparative scientific experiment has been executed.

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

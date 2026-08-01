# Scope and Status

## Research question

Can a system be modeled as one globally organized process and many locally real processes at the same time, without treating the whole as an external controller or the parts as independently fundamental?

## Candidate synthesis

ARG investigates a family built from some combination of:

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

These ingredients must not be treated as one mechanism merely because they are described with similar whole-part language.

## Implemented mechanism split

### $M_0$: local/adaptive baseline

The implementation contains local nonlinear node dynamics, neighborhood coupling, adaptive edge activation, and metric deformation. The collective statistic may be logged, but it does not enter any $M_0$ transition equation.

### $M_F$: collective feedback

The matched feedback prototype computes

$$
c(x)=\frac13\sum_i x_i^2
$$

and feeds it into constituent transitions through

$$
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

This is **implemented prototype-level downward feedback/constraint**.

### $M_P$: target projected variant

Contract v1.0 defines

$$
\Gamma(Z)=c(x)-c_0=0,
\qquad
c_0=c(x(0))>0,
$$

and target projected motion

$$
\dot Z=\Pi_{T_Z\mathcal M}F_{\mathrm{local}}(Z).
$$

This mechanism is not yet implemented or verified.

## Current claim ceiling

$$
\boxed{
M_0,M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## What is currently claimed

- $M_0$ implements the frozen no-feedback local/adaptive baseline.
- $M_F$ implements the matched endogenous collective-feedback prototype.
- The $M_F$ substrate path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is explicit.
- Intrinsic edge lengths and graph distances are state dependent in both implemented prototypes.
- $M_F(\chi=\eta_2=\rho=0)=M_0$ is unit-tested for the frozen equations.
- Production and independently written derivative/RK4 paths agree at tested cases.
- The projected-admissibility formalism remains a target mathematical and software-verification program.

## What is not currently claimed

- That either executable implements $\Gamma/H$ projection.
- That collective feedback is equivalent to tangent-space projection.
- That prototype-level feedback establishes macro-level causal autonomy.
- That $M_0$ or $M_F$ defeats scientific alternatives.
- That organization dependence, counterfactual adequacy, transport, or alternative-model defeat has been demonstrated.
- That ARG is mathematically novel or a new fundamental geometry.
- That the universe literally is a graph, constraint manifold, or computational structure.
- That either prototype reproduces known physical laws.
- That the apophatic principle proves any religion or metaphysics.
- That primes, emptiness, computation, or coherence are established as ultimate substances.

## Verification scope

Phase 2 merged with 20 passing software tests in a clean local reconstruction. No hosted check run was attached at merge time. This validates software contracts only; no scientific experiment has been executed.

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

The binding alignment statement is `13_alignment_and_claim_ceiling.md`. The phase-gated execution plan is `14_roadmap.md`.

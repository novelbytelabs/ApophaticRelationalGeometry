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

## Mechanism split

### Current executable: $M_F$

The three-node implementation computes an endogenous collective statistic

$$
c(x)=\frac13\sum_i x_i^2
$$

and feeds it into constituent transition equations.

This is **implemented prototype-level downward feedback/constraint**.

### Target projected variant: $M_P$

The general formalism also proposes an admissible set

$$
\mathcal M=\{Z:\Gamma(Z)=0,\ H(Z)\geq0\}
$$

and projected motion

$$
\dot Z=\Pi_{T_Z\mathcal M}F_{\mathrm{local}}(Z).
$$

This mechanism is not yet implemented or verified.

## Current claim ceiling

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## What is currently claimed

- The current code implements a three-node nonlinear adaptive relational model with endogenous collective feedback.
- The substrate path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is explicit.
- Intrinsic edge lengths and graph distances are state dependent in the implemented prototype.
- Software unit tests can check equations, invariance properties, numerical sanity, and implementation contracts.
- The projected-admissibility formalism is a target mathematical model and proof program.

## What is not currently claimed

- That the executable implements $\Gamma/H$ projection.
- That collective feedback is equivalent to tangent-space projection.
- That prototype-level feedback establishes macro-level causal autonomy.
- That organization dependence, counterfactual adequacy, transport, or alternative-model defeat has been demonstrated.
- That ARG is mathematically novel or a new fundamental geometry.
- That the universe literally is a graph, constraint manifold, or computational structure.
- That the prototype reproduces known physical laws.
- That the apophatic principle proves any religion or metaphysics.
- That primes, emptiness, computation, or coherence are established as ultimate substances.

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

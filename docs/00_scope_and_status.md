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

These are distinct mechanisms and must be defined, implemented, and tested separately.

## Implemented mechanism split

### $M_0$: local/adaptive baseline

Local nonlinear dynamics, neighborhood coupling, adaptive edge activation, and metric deformation. The collective statistic may be logged but does not enter any transition equation.

### $M_F$: collective feedback

$$
c(x)=\frac13\sum_i x_i^2,
\qquad
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

Licensed description:

> **implemented prototype-level downward feedback/constraint**

This does not establish macro-level causal autonomy.

### $M_P$: projected-admissibility sandbox

Contract v1.0 implements

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
$$

$$
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

Every RK4 derivative stage is projected, each completed step is radially retracted, mechanism diagnostics are recorded, and near-rank-loss paths fail closed.

### $M_{FP}$: feedback followed by projection

$$
F_{\mathrm{proposal}}=F_0+F_F
$$

is projected using the same $M_P$ policy. At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

because the node-feedback term is radial. Feedback remains in $s$ and $q$, so later trajectories need not agree.

Both projected models are constant-amplitude mechanism sandboxes. They are not the final relational geometry and are not validated physical models.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Protocol and execution status

Phase 5 froze protocol `ARG-P5-COMP-v1` before any trajectory generation. The human-readable protocol and machine-readable bundle fix:

- primary and secondary hypotheses;
- observation maps and decision thresholds;
- direction-level inferential units;
- deterministic pilot/confirmatory separation;
- parameters and initial conditions;
- RK4 refinement and alternate-integrator replication;
- exclusions, stop rules, failure retention, and provenance;
- executable metric, bootstrap, hashing, validation, and decision code.

Hosted verification reported 65 passing tests on Python 3.10 and 65 on Python 3.12.

Current authorization is:

$$
\boxed{
\text{development pilot authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

The development pilot has not run. Authorization is not execution.

## What is currently claimed

- All four contract-v1.0 prototypes are implemented through canonical dispatch.
- $M_0$ implements the no-feedback local/adaptive baseline.
- $M_F$ implements endogenous collective feedback through an explicit substrate path.
- $M_P$ implements the frozen constant-amplitude tangent projection and retraction policy.
- $M_{FP}$ implements feedback followed by projection with retained $s/q$ feedback.
- Declared reductions, projector identities, tangency, retraction, singular handling, permutation equivariance, and independent software-reference parity are unit-tested.
- The Phase 5 protocol is frozen, machine-readable, executable at the metric/decision level, and locked before data generation.

## What is not currently claimed

- That collective feedback is dynamically or observationally equivalent to tangent-space projection.
- That same-state node equality implies trajectory equality.
- That prototype-level feedback or projection establishes macro-level causal autonomy.
- That any mechanism improves prediction or defeats scientific alternatives.
- That constant amplitude is physically fundamental.
- That a pilot or confirmatory experiment has been executed.
- That organization dependence, transport, strong emergence, or physical adequacy has been demonstrated.
- That ARG is mathematically novel or a new fundamental geometry.
- That reality literally is a graph, constraint manifold, or computational structure.

## Verification scope

- Phase 2: 20 local software tests for $M_0/M_F$.
- Phase 3: 35 hosted tests in each configured Python environment for $M_0/M_F/M_P$.
- Phase 4: 51 hosted tests in each configured environment for the four-model implementation.
- Phase 5: 65 hosted tests in each configured environment for models plus frozen protocol and decision machinery.

These validate software and local mathematical/protocol contracts, not a scientific hypothesis.

The binding alignment statement is `13_alignment_and_claim_ceiling.md`. The active roadmap is `14_roadmap.md`.

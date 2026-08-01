# Canonical Alignment and Claim Ceiling

## Purpose

This document fixes the relationship between the general ARG formalism, the current executable prototypes, and the claims presently licensed by the evidence.

It is binding on the README, documentation, implementation, experiments, and external descriptions of the project.

## Mechanism distinction

ARG studies two different whole-to-part mechanisms.

### Collective feedback

A collective statistic is computed from the substrate and enters constituent transition equations.

For the three-node $M_F$ prototype,

$$
c(x)=\frac{1}{3}\sum_{i=1}^{3}x_i^2,
$$

and the substrate path is

$$
x\longrightarrow c(x)\longrightarrow (\dot x,\dot s,\dot q).
$$

### Global admissibility projection

An unconstrained proposal is projected onto the tangent space of an explicitly defined admissible set:

$$
\mathcal M=\{Z:\Gamma(Z)=0,\ H(Z)\geq0\},
$$

$$
\dot Z
=
\Pi_{T_Z\mathcal M}F_{\mathrm{local}}(Z).
$$

These mechanisms are not assumed equivalent.

$$
F_{\mathrm{feedback}}
\not\equiv
\Pi_{T_Z\mathcal M}F_{\mathrm{local}}
$$

unless an explicit derivation and code-level equivalence test establish otherwise.

## Canonical model family

### $M_0$ — local/adaptive substrate baseline

- local nonlinear node dynamics;
- neighborhood coupling;
- adaptive edge activation and metric deformation;
- no collective statistic in transition equations;
- no admissibility projection.

$M_0$ is implemented and unit-tested.

### $M_F$ — collective-feedback prototype

- the $M_0$ substrate;
- endogenous collective statistic $c(x)$;
- explicit feedback from $c(x)$ into node, edge, and metric transitions;
- no $\Gamma/H$ admissibility projection.

$M_F$ is implemented and unit-tested.

### $M_P$ — projected-admissibility prototype

Contract v1.0 freezes:

$$
\Gamma(Z)=c(x)-c_0=0,
\qquad
c_0=c(x(0))>0,
$$

with no inequality constraints in this first sandbox.

$M_P$ is not yet implemented or verified.

### $M_{FP}$ — combined feedback and projection

- collective feedback as in $M_F$;
- admissibility projection as in $M_P$;
- separately measurable feedback and projection contributions.

$M_{FP}$ is not yet implemented or verified.

## Current claim ceiling

$$
\boxed{
M_0,M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

The strongest presently licensed descriptions are:

> ARG implements a unit-tested local/adaptive no-feedback baseline $M_0$.

> ARG implements a unit-tested prototype of endogenous collective downward feedback/constraint $M_F$ with adaptive relational geometry.

> The stronger global-admissibility projection mechanism remains unimplemented and unverified.

## Meaning of “downward” at the current stage

Only $M_F$ supports the label:

> **implemented prototype-level downward feedback/constraint**

because its substrate path is explicit and system-derived information modifies constituent transitions.

$M_0$ is the matched no-feedback baseline and carries no downward-feedback claim.

Neither implemented model establishes:

- validated macro-level causal autonomy;
- organization-dependent causal power beyond the encoded statistic;
- counterfactual adequacy;
- invariance across all admissible presentations;
- transport to other systems or scales;
- defeat of simpler alternative models;
- empirical strong emergence.

## Fail-closed projected-claim gate

A projected-geometry claim is licensed only when all conditions pass:

$$
\operatorname{PROJECTED\_CLAIM}
=
D_{\Gamma,H}
\land_{FC}
I_{\Pi}
\land_{FC}
T_{\mathrm{preserve}}
\land_{FC}
E_{\mathrm{code}}
\land_{FC}
S_{\mathrm{path}}.
$$

Where:

- $D_{\Gamma,H}$ — $\Gamma$ and $H$ are explicitly defined;
- $I_{\Pi}$ — the projection is implemented;
- $T_{\mathrm{preserve}}$ — constraint preservation is tested;
- $E_{\mathrm{code}}$ — code and equations are shown equivalent;
- $S_{\mathrm{path}}$ — the substrate mechanism is identified.

Current gate state:

$$
D_{\Gamma,H}=\text{PASS AT CONTRACT LEVEL},
$$

$$
I_{\Pi}=T_{\mathrm{preserve}}=E_{\mathrm{code}}=S_{\mathrm{path}}=\text{UNVERIFIED}.
$$

Therefore:

$$
\operatorname{PROJECTED\_CLAIM}=\text{UNVERIFIED}.
$$

## NeoEmergenics relationship

NeoEmergenics is an independent harness and fail-closed claim evaluator. It neither validates ARG nor requires ARG.

ARG owns:

- the four-model implementation;
- mathematical proofs;
- code-equation parity;
- comparative experiments;
- claim-ledger maintenance.

NeoEmergenics may enforce the claim ceiling, but it supplies no scientific evidence for ARG.

## Phase 2 verification scope

The merged Phase 2 implementation established only software-level facts:

- $M_0$ exists as code;
- its transition path does not call the collective statistic;
- $M_F$ remains regression-compatible at the frozen reference state;
- $M_F(\chi=\eta_2=\rho=0)=M_0$ in the frozen equations;
- production and independently written derivative/RK4 paths agree at tested cases;
- 20 tests passed in a clean local reconstruction.

No hosted check run was attached at merge time. No scientific experiment has been executed.

## Change-control rule

No document, issue, paper, release note, or experiment report may describe the current executables as projected geometry unless the projected-claim gate has passed.

# Canonical Alignment and Claim Ceiling

## Purpose

This document fixes the relationship between the ARG formalism, the implemented prototypes, and the strongest claims licensed by current evidence.

It is binding on documentation, code, experiments, releases, and external descriptions.

## Mechanism distinction

ARG studies two distinct whole-to-part mechanisms.

### Collective feedback

A substrate-computed statistic enters constituent transition equations:

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

This is implemented by $M_F$ and retained inside $M_{FP}$.

### Global admissibility projection

A proposed vector field is projected onto the tangent space of an explicit admissible manifold:

$$
\dot Z=\Pi_{T_Z\mathcal M}F(Z).
$$

Contract v1.0 implements the minimal constant-amplitude sandbox

$$
\Gamma(Z)=c(x)-c_0=\frac13x^Tx-c_0=0,
$$

$$
P_T=I-\frac{xx^T}{x^Tx}.
$$

This is implemented by $M_P$ and $M_{FP}$.

The mechanisms are not assumed equivalent:

$$
M_F\not\equiv M_P
$$

unless a scoped mathematical or observational equivalence is independently established.

## Canonical model family

### $M_0$

Implemented and unit-tested local/adaptive baseline with no collective-statistic transition path and no projection.

### $M_F$

Implemented and unit-tested endogenous collective-feedback prototype.

Licensed description:

> implemented prototype-level downward feedback/constraint

This does not establish macro-level causal autonomy.

### $M_P$

Implemented and unit-tested contract-v1.0 constant-amplitude projected-admissibility sandbox.

It includes an explicit equality constraint, Euclidean tangent projection, projected RK4 stages, mandatory radial retraction, fail-closed singular handling, separate projection diagnostics, and independent reference parity.

### $M_{FP}$

Implemented and unit-tested feedback-followed-by-projection prototype.

It exposes separately:

- the local/adaptive proposal $F_0$;
- the feedback vector $F_F$;
- the combined proposal $F_0+F_F$;
- the projection correction;
- the projected derivative;
- the numerical retraction.

For the same regular full state, contract v1.0 satisfies

$$
\boxed{f_{FP}=f_P}
$$

because the node-feedback term is radial and $P_Tx=0$.

This same-state identity is not trajectory equivalence. $M_{FP}$ retains feedback in $s$ and $q$, which can change later conductances and node proposals.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Implementation gates

### $M_P$ v1.0

| Gate | Status |
|---|---|
| Explicit $\Gamma/H$ definition | PASS — $\Gamma=c(x)-c_0$, $H=\varnothing$ |
| Projection implementation | PASS |
| Constraint-preservation tests | PASS at software/mechanism level |
| Code-equation equivalence | PASS at tested cases against an independent reference path |
| Substrate path | PASS — proposal, correction, projected derivative, and retraction are explicit |

Therefore:

$$
\operatorname{MP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

### $M_{FP}$ v1.0

| Gate | Status |
|---|---|
| Feedback proposal $F_0+F_F$ | PASS |
| Projection after feedback | PASS |
| Same-state identity $f_{FP}=f_P$ | PASS at tested regular states |
| Retained $s/q$ feedback | PASS |
| Exact zero-feedback reduction to $M_P$ | PASS |
| Independent derivative and step parity | PASS at tested cases |
| Constraint preservation and singular handling | PASS at software/mechanism level |

Therefore:

$$
\operatorname{MFP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

The broader scientific claim remains:

$$
\operatorname{ARG\_COMPARATIVE\_SCIENTIFIC\_CLAIM}=\text{UNVERIFIED}.
$$

## Current non-claims

ARG has not established:

- that $M_F$ and $M_P$ are dynamically or observationally equivalent;
- that same-state node identity implies trajectory identity;
- that any mechanism defeats simpler scientific alternatives;
- that projection or feedback improves prediction;
- that constant amplitude is a law of nature;
- that the v1.0 sandbox is the final relational geometry;
- that the four-model comparative experiment has been run;
- that macro-level causal autonomy or strong emergence has been demonstrated;
- that ARG is a fundamental physical theory.

## Verification references

- Phase 3 record: `16_phase3_mp_verification.md`
- Phase 4 record: `17_phase4_mfp_verification.md`
- Frozen equations and policies: `15_four_model_design_contract.md`
- Current execution plan: `14_roadmap.md`

## NeoEmergenics relationship

NeoEmergenics remains an independent fail-closed harness and claim evaluator. It may enforce this ceiling but supplies no scientific evidence for ARG.

## Change-control rule

Every claim must name the model and evidence level. “Projected geometry” must be qualified as **constant-amplitude**, **prototype**, and **software-verified** when scientific or ontological interpretation could otherwise be inferred.
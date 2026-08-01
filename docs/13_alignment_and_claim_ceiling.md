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

This is implemented by $M_F$.

### Global admissibility projection

A proposed vector field is projected onto the tangent space of an explicit admissible manifold:

$$
\dot Z=\Pi_{T_Z\mathcal M}F_0(Z).
$$

Contract v1.0 implements the minimal constant-amplitude sandbox

$$
\Gamma(Z)=c(x)-c_0=\frac13x^Tx-c_0=0,
$$

$$
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

This is implemented by $M_P$.

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

It includes:

- an explicit equality constraint;
- Euclidean tangent projection;
- projected RK4 stages;
- mandatory radial retraction;
- fail-closed singular handling;
- independent reference parity;
- constraint, tangency, correction, denominator, and retraction diagnostics.

It is a projection-mechanism sandbox, not ARG's completed relational-admissibility geometry and not a validated physical law.

### $M_{FP}$

Feedback followed by projection remains unimplemented and unverified.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP}\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Projected-implementation gate

For the specific $M_P$ v1.0 implementation:

| Gate | Status |
|---|---|
| Explicit $\Gamma/H$ definition | PASS — $\Gamma=c(x)-c_0$, $H=\varnothing$ |
| Projection implementation | PASS |
| Constraint-preservation tests | PASS at software/mechanism level |
| Code-equation equivalence | PASS at tested cases against an independent reference path |
| Substrate path | PASS — $F_0\to$ normal correction $\to f_P$, followed by numerical retraction |

Therefore:

$$
\operatorname{MP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

This does **not** promote the broader scientific claim:

$$
\operatorname{PROJECTED\_GEOMETRY\_SCIENTIFIC\_CLAIM}=\text{UNVERIFIED}.
$$

The implementation gate establishes that the declared mechanism exists in code and satisfies its frozen software contracts. It does not establish predictive utility, physical adequacy, novelty, transport, or macro-level causal autonomy.

## Current non-claims

ARG has not established:

- that $M_F$ and $M_P$ are dynamically or observationally equivalent;
- that either mechanism defeats simpler scientific alternatives;
- that projection improves prediction;
- that constant amplitude is a law of nature;
- that $M_P$ is the final relational geometry;
- that $M_{FP}$ is implemented;
- that the four-model comparative experiment has been run;
- that macro-level causal autonomy or strong emergence has been demonstrated;
- that ARG is a fundamental physical theory.

## Verification references

- Phase 2 record: `08_claim_ledger.md`
- Phase 3 record: `16_phase3_mp_verification.md`
- Frozen equations and policies: `15_four_model_design_contract.md`
- Current execution plan: `14_roadmap.md`

## NeoEmergenics relationship

NeoEmergenics remains an independent fail-closed harness and claim evaluator. It may enforce this ceiling but supplies no scientific evidence for ARG.

## Change-control rule

Every claim must name the model and evidence level. “Projected geometry” may now refer to the implemented $M_P$ v1.0 sandbox, but must not be used without the qualifiers **constant-amplitude**, **prototype**, and **software-verified** when scientific or ontological interpretation could otherwise be inferred.

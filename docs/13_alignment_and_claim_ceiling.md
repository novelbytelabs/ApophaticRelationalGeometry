# Canonical Alignment and Claim Ceiling

## Purpose

This document fixes the relationship between the ARG formalism, implemented prototypes, frozen experiment protocol, and strongest currently licensed claims. It is binding on documentation, code, experiments, releases, and external descriptions.

## Mechanism distinction

### Collective feedback

A substrate-computed statistic enters constituent transition equations:

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

This is implemented by $M_F$ and retained within $M_{FP}$.

### Global admissibility projection

A proposed vector field is projected onto the tangent space of an explicit admissible manifold:

$$
\dot Z=\Pi_{T_Z\mathcal M}F(Z).
$$

Contract v1.0 implements

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

| Model | Software status | Licensed description |
|---|---|---|
| $M_0$ | Implemented and unit-tested | Local/adaptive baseline with no collective-statistic transition path and no projection. |
| $M_F$ | Implemented and unit-tested | Endogenous collective-feedback prototype; implemented prototype-level downward feedback/constraint. |
| $M_P$ | Implemented and unit-tested | Constant-amplitude projected-admissibility sandbox with projected RK4, retraction, fail-closed singular handling, and separate diagnostics. |
| $M_{FP}$ | Implemented and unit-tested | Feedback proposal followed by node projection and retraction, with retained $s/q$ feedback and separate mechanism diagnostics. |

For the same regular full state,

$$
\boxed{f_{FP}=f_P}
$$

because the node-feedback term is radial and $P_Tx=0$. This identity is local to the same-state node derivative. It does not imply trajectory identity because $M_{FP}$ retains feedback in $s$ and $q$.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Protocol status and authorization

Phase 5 froze comparative protocol `ARG-P5-COMP-v1` before trajectory generation. The protocol fixes its hypotheses, observation maps, thresholds, inferential units, deterministic pilot/confirmatory split, parameters, initial conditions, numerical replication, exclusions, stop rules, archive requirements, executable metrics, decision logic, and lock manifest.

Therefore the execution authorization is:

$$
\boxed{
\text{development pilot authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

This authorization does not imply that a pilot has run. No Phase 5 trajectory was generated or inspected.

## Implementation gates

### $M_P$ version 1.0

| Gate | Status |
|---|---|
| Explicit $\Gamma/H$ definition | PASS — $\Gamma=c(x)-c_0$, $H=\varnothing$ |
| Projection implementation | PASS |
| Constraint-preservation tests | PASS at software/mechanism level |
| Code-equation parity | PASS at tested cases against an independent path |
| Substrate path | PASS — proposal, correction, projected derivative, and retraction are explicit |

$$
\operatorname{MP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

### $M_{FP}$ version 1.0

| Gate | Status |
|---|---|
| Feedback proposal $F_0+F_F$ | PASS |
| Projection after feedback | PASS |
| Same-state identity $f_{FP}=f_P$ | PASS at tested regular states |
| Retained $s/q$ feedback | PASS |
| Zero-feedback reduction to $M_P$ | PASS |
| Independent derivative and step parity | PASS at tested cases |
| Constraint preservation and singular handling | PASS at software/mechanism level |

$$
\operatorname{MFP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

### Phase 5 protocol version 1.0

| Gate | Status |
|---|---|
| Human-readable protocol | PASS |
| Machine-readable hypotheses and manifests | PASS |
| Pilot/confirmatory separation | PASS — direction-level deterministic hash split |
| Executable metric and decision rules | PASS |
| Numerical, exclusion, stop, and provenance policies | PASS |
| Critical-file lock | PASS |
| Hosted verification | PASS — 65 tests on Python 3.10 and 65 on Python 3.12 |
| No-data condition | PASS — no Phase 5 trajectory generated |

$$
\operatorname{PHASE5\_PROTOCOL\_FREEZE}=\text{PASS}.
$$

The comparative scientific claim remains:

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
- that the version-1.0 sandbox is the final relational geometry;
- that the development pilot has been executed;
- that the confirmatory experiment is authorized;
- that macro-level causal autonomy or strong emergence has been demonstrated;
- that ARG is a fundamental physical theory.

## Verification references

- `16_phase3_mp_verification.md`
- `17_phase4_mfp_verification.md`
- `18_phase5_comparative_protocol.md`
- `protocol/phase5_v1/`
- `15_four_model_design_contract.md`
- `14_roadmap.md`

## NeoEmergenics relationship

NeoEmergenics remains an independent fail-closed harness and claim evaluator. It may enforce this ceiling but supplies no scientific evidence for ARG.

## Change-control rule

Every claim must name the model, evidence level, observation map, domain, and protocol version where applicable. “Projected geometry” must be qualified as **constant-amplitude**, **prototype**, and **software-verified** when scientific or ontological interpretation could otherwise be inferred.

Any substantive change to a Phase 5 metric, threshold, parameter, configuration, or split creates a new protocol version and requires a fresh, unexecuted confirmatory set.

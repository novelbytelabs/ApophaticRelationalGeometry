# Canonical Alignment and Claim Ceiling

## Purpose

This document fixes the relationship between the ARG formalism, implemented prototypes, frozen experiment protocol, verified runner, and strongest currently licensed claims. It is binding on documentation, code, experiments, releases, and external descriptions.

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
\qquad
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

because the node-feedback term is radial and $P_Tx=0$. This identity is local to the same-state node derivative and does not imply trajectory identity.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Protocol, runner, and execution status

Phase 5 froze comparative protocol `ARG-P5-COMP-v1` before trajectory generation. Phase 6A implemented and software-verified a runner for exactly the frozen pilot set.

Current execution state:

$$
\boxed{
\text{pilot-only runner verified};
\quad
\text{development pilot not executed};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

A development pilot is authorized in principle by the Phase 5 gate, but execution remains blocked until a separate committed authorization names the verified runner commit. Authorization is not execution.

## Passed implementation gates

### $M_P$ version 1.0

Explicit equality constraint, projection, constraint-preservation tests, independent code-equation parity, diagnostics, and fail-closed singular handling: **PASS at software/mechanism level**.

$$
\operatorname{MP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

### $M_{FP}$ version 1.0

Feedback proposal, projection ordering, same-state identity, retained $s/q$ feedback, reduction paths, independent parity, and constraint handling: **PASS at software/mechanism level**.

$$
\operatorname{MFP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

### Phase 5 protocol version 1.0

Human- and machine-readable protocol, deterministic split, executable metrics/decisions, numerical and provenance policies, critical-file lock, hosted verification, and no-data condition: **PASS**.

$$
\operatorname{PHASE5\_PROTOCOL\_FREEZE}=\text{PASS}.
$$

### Phase 6A pilot-only runner version 1.0

| Gate | Status |
|---|---|
| Lock-first manifest loading | PASS |
| Exact 50-configuration pilot reconstruction | PASS |
| Mixed/confirmatory batch rejection | PASS |
| Direct RK4/DOP853 confirmatory rejection | PASS |
| All-model RK4 and DOP853 decision paths | PASS |
| H5/H6, refinement, endpoint, and alternate-integrator gates | PASS at tested cases |
| Frozen controls and all six relabelings | PASS at tested cases |
| Write-once checksummed archive | PASS at tested cases |
| Independent membership, trajectory, and checksum references | PASS |
| Separate execution-authorization boundary | PASS |
| Hosted verification | PASS — 100 tests on Python 3.10 and 100 on Python 3.12 |
| No-pilot-data condition | PASS |

$$
\operatorname{PHASE6\_RUNNER\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

The comparative scientific claim remains:

$$
\operatorname{ARG\_COMPARATIVE\_SCIENTIFIC\_CLAIM}=\text{UNVERIFIED}.
$$

## Current non-claims

ARG has not established:

- that $M_F$ and $M_P$ are dynamically or observationally equivalent;
- that same-state node identity implies trajectory identity;
- any pilot effect size or numerical mechanism result;
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
- `19_phase5_protocol_verification.md`
- `20_phase6_runner_design.md`
- `21_phase6_runner_verification.md`
- `protocol/phase5_v1/`
- `protocol/phase6_runner_v1/`

## NeoEmergenics relationship

NeoEmergenics remains an independent fail-closed harness and claim evaluator. It may enforce this ceiling but supplies no scientific evidence for ARG.

## Change-control rule

Every claim must name the model, evidence level, observation map, domain, and protocol version where applicable. “Projected geometry” must be qualified as **constant-amplitude**, **prototype**, and **software-verified** when scientific or ontological interpretation could otherwise be inferred.

Any substantive change to a frozen metric, threshold, parameter, configuration, split, protected runner file, or decision rule requires a new version and renewed pre-execution review.

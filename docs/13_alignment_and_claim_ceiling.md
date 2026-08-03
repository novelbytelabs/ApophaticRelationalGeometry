# Canonical Alignment and Claim Ceiling

## Purpose

This document fixes the relationship among the ARG formalism, implemented prototypes, frozen protocol, audited runner, consensus program, and strongest licensed claims. It is binding on documentation, code, experiments, releases, and external descriptions.

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

## Binding software claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Binding execution ceiling

Phase 5 froze comparative protocol `ARG-P5-COMP-v1` before trajectory generation. Phase 6A implemented a pilot-only runner, but an independent audit found integrity defects outside and around the nominal equations.

Current execution state:

$$
\boxed{
\text{Phase 6A.1 integrity remediation STOP-SHIP};
\quad
\text{development pilot not authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

The earlier statement that a pilot was “authorized in principle” is superseded. A pilot can be considered only after both:

1. Phase 6A.1 passes external re-audit;
2. the consensus program isolates a precise unresolved scientific residual that the frozen pilot actually discriminates.

Authorization is not execution, and passing either gate alone is insufficient.

## Binding consensus ceiling

The first three CS1 source baskets support the following scoped conclusions:

- trajectories depend on dynamics and initial condition;
- different states can amplify, decay, or cancel differently under one operator;
- state and topology can coevolve;
- nonlinear persistence has multiple inequivalent forms;
- controllability, observability, balanced input/output importance, nonlinear accessibility, viability, and invariant-set preservation are established;
- smoothly evolving state spaces can be related by explicit pushforward and pullback maps when a compatible map family is supplied;
- representation equivalence is criterion-dependent.

These are established neighboring results, not ARG discoveries.

The current consensus ceiling is:

$$
\boxed{
\text{typed family of state–system relations};
\quad
\text{no universal compatibility or persistence scalar established};
\quad
\text{no ARG-specific residual established}.
}
$$

## Typed scientific-context rule

A scoped autonomous model may use

$$
Q_t=(B_t,x_t),
\qquad
x_{t+1}=F_{B_t}(x_t).
$$

But intervention, observation, viability, robustness, invariance, or recoverability claims may require a context such as

$$
\mathcal S=
(\mathcal X,F,B_{\mathrm{in}},C_{\mathrm{out}},K,\mathcal U,\mathcal W,\Phi,T).
$$

No input map, output map, control class, constraint, disturbance class, measured functional, or horizon may be omitted when it changes the claim.

This tuple is a methodological typing requirement, not a final ontology.

## Persistence language

Bare `persistence` is prohibited in scientific claims when a typed predicate is available.

Current distinctions include:

$$
P_{\mathrm{norm}},
P_{\mathrm{basin}},
P_{\mathrm{manifold}},
P_{\mathrm{retain}},
P_{\mathrm{structural}},
P_{\mathrm{viable}},
P_{\mathrm{invariant}},
P_{\mathrm{robust}},
P_{\mathrm{controlled}}.
$$

Related state–system quantities that are not themselves identical persistence predicates include:

$$
R_{\mathrm{reachable}},
\qquad
O_{\mathrm{observable}},
\qquad
I_{\mathrm{balanced}}.
$$

## Structure–state language

The pair $Q_t=(B_t,x_t)$ may remain a scoped autonomous-model factorization.

It may not be presented as:

- a representation-independent ontology;
- sufficient for intervention, observation, control, viability, robustness, or information claims;
- a discovery unique to ARG.

The state–structure boundary remains a modeling factorization unless an invariant distinction is proved.

## Licensed project description

Permitted:

> Apophatic Relational Geometry is a candidate convergence synthesis and executable research framework combining established ingredients from nonlinear dynamics, adaptive networks, constrained systems, control, evolving spaces, and apophatic non-reification. Its novelty, scientific utility, and physical adequacy remain under audit.

Not permitted:

- new fundamental geometry;
- discovery that state and structure jointly determine behavior;
- discovery that persistence depends on compatibility;
- universal state–structure compatibility law;
- universal persistence scalar;
- validated theory of physical identity;
- proof of pluralistic monism;
- proof that reality is computational or graph-like;
- scientifically validated mechanism based on software tests.

## Mathematical claims currently licensed

- the declared model equations are definitions;
- radial projector identities hold under stated regularity conditions;
- same-state node equality $f_{FP}=f_P$ holds under the frozen assumptions;
- software agrees with independent reference implementations at tested cases;
- node-relabeling equivariance is locally unit-tested, not generally proved.

## Scientific claims currently unlicensed

- feedback improves performance;
- projection improves any typed persistence measure;
- ARG predicts a physical system better than established alternatives;
- feedback establishes autonomous downward causation;
- coevolving geometry produces an irreducible mechanism;
- the four-model experiment establishes a mechanism result;
- any ARG compatibility quantity exceeds modal, nonmodal, basin, control, viability, transport, or invariant-set methods.

## Current non-claims

ARG has not established:

- that $M_F$ and $M_P$ are dynamically or observationally equivalent;
- that same-state node identity implies trajectory identity;
- any pilot effect size or numerical mechanism result;
- that any mechanism defeats simpler scientific alternatives;
- that projection or feedback improves prediction;
- that constant amplitude is a law of nature;
- that the version-1.0 sandbox is the final relational geometry;
- that the development pilot has been executed or authorized;
- that the confirmatory experiment is authorized;
- that macro-level causal autonomy or strong emergence has been demonstrated;
- that ARG is a fundamental physical theory.

## Verification and consensus references

- `07_research_grounding_plan.md`
- `08_claim_ledger.md`
- `09_novelty_matrix.md`
- `10_literature_landscape.md`
- `14_roadmap.md`
- `16_phase3_mp_verification.md`
- `17_phase4_mfp_verification.md`
- `18_phase5_comparative_protocol.md`
- `19_phase5_protocol_verification.md`
- `20_phase6_runner_design.md`
- `21_phase6_runner_verification.md`
- `22_consensus_synthesis_program.md`
- `research/consensus/01_consensus_table.md`
- `research/consensus/01_translation_dictionary.md`
- `research/consensus/01_disagreement_map.md`

## Change-control rule

Every claim must name the model, evidence level, observation map, domain, scientific context, and protocol version where applicable. “Projected geometry” must be qualified as **constant-amplitude**, **prototype**, and **software-verified** when scientific or ontological interpretation could otherwise be inferred.

Any substantive change to a frozen metric, threshold, parameter, configuration, split, protected runner file, or decision rule requires a new version and renewed pre-execution review.

## Immediate next action

Complete the CS1 transport-and-structural-change basket and associated representation audit. Do not revise the ontology or authorize execution.

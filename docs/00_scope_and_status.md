# Scope and Status

## Research question

Can a system be modeled as one globally organized process and many locally real processes at the same time, without treating the whole as an external controller or the parts as independently fundamental?

## Candidate synthesis

ARG investigates combinations of local nonlinear dynamics, adaptive relations, state-dependent metric, collective feedback, and global admissibility projection. These are distinct mechanisms and must be defined, implemented, and tested separately.

## Implemented mechanism split

- $M_0$: local/adaptive baseline without a collective-statistic transition path.
- $M_F$: endogenous collective feedback through
  $$x\to c(x)\to(\dot x,\dot s,\dot q).$$
- $M_P$: constant-amplitude projection sandbox on
  $$\Gamma(Z)=\frac13x^Tx-c_0=0.$$
- $M_{FP}$: $F_0+F_F$ followed by node projection, retaining feedback in $s$ and $q$.

Only $M_F$ supports the narrow description:

> **implemented prototype-level downward feedback/constraint**

This does not establish macro-level causal autonomy.

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

because radial node feedback is annihilated by the projector. This does not imply trajectory identity.

Both projected models are constant-amplitude mechanism sandboxes, not validated physical laws or the completed relational geometry.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Protocol and runner status

Protocol `ARG-P5-COMP-v1` was frozen before trajectory generation. Phase 6A now implements and software-verifies a pilot-only runner that:

- reconstructs exactly the frozen 50 pilot configurations;
- rejects confirmatory/mixed batches and direct confirmatory integration;
- implements all-model RK4/DOP853 decision paths;
- enforces H5/H6 and frozen numerical gates;
- runs declared controls and all six relabelings;
- writes a deterministic, checksummed, write-once archive;
- requires a separate committed execution authorization naming the verified runner commit.

The external report scored the pinned candidate 85/100 with a conditional pass. Its five demonstrated guardrail failures were remediated, after which one authorized exploratory pilot attempt began. The runner stopped fail closed after six H6 identity-gate failures exceeded the frozen 10% pause rule. Blinded analysis found absolute MP/MFP node-identity residuals below `2.8e-16` while the projected derivatives collapsed toward zero, exposing an ill-conditioned forward-relative validity metric rather than a broken identity.

Current execution state:

$$
\boxed{
\text{first pilot attempt stopped fail closed};
\quad
\text{no completed archive or scientific result};
\quad
\text{Phase 6B.2 H6 remediation active};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

## What is currently claimed

- All four contract-v1.0 prototypes are implemented and unit-tested.
- The feedback and projection mechanisms are represented separately.
- The Phase 5 protocol is frozen and executable at the metric/decision level.
- The runner correctly enforced its stop rule and preserved a partial failure archive when H6 exceeded its validity threshold.
- Blinded H6 diagnosis supports a conditioning failure in the metric, not a violation of the exact projected identity.
- Confirmatory access is blocked at planner, integrator, authorization, archive, and contamination-scan boundaries.

## What is not currently claimed

- That feedback and projection are dynamically or observationally equivalent.
- That same-state node equality implies trajectory equality.
- Any completed pilot or confirmatory effect size; the partial failed archive is not a result dataset.
- That any mechanism improves prediction or defeats scientific alternatives.
- That organization dependence, transport, macro-level causal autonomy, strong emergence, or physical adequacy has been demonstrated.
- That ARG is mathematically novel or a new fundamental geometry.
- That reality literally is a graph, constraint manifold, or computational structure.

## Verification scope

- Phase 2: 20 local software tests.
- Phase 3: 35 hosted tests in each configured Python environment.
- Phase 4: 51 hosted tests in each configured environment.
- Phase 5: 65 hosted tests in each configured environment.
- Phase 6A: 100 hosted tests in each configured environment.

These validate software and local mathematical/protocol contracts, not a scientific hypothesis.

The binding alignment statement is `13_alignment_and_claim_ceiling.md`. The active roadmap is `14_roadmap.md`.

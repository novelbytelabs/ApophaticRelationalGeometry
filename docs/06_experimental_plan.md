# Experimental Plan

## Status

All four contract-v1.0 models are implemented and unit-tested:

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

Protocol `ARG-P5-COMP-v1` is frozen. The Phase 6A pilot-only runner is implemented and software-verified. The development pilot has not run. Confirmatory execution and comparative scientific claims remain blocked.

## Canonical models

- $M_0$: local/adaptive substrate without feedback or projection.
- $M_F$: $M_0$ plus endogenous collective feedback.
- $M_P$: $M_0$ projected onto $\Gamma(Z)=\frac13x^Tx-c_0=0$.
- $M_{FP}$: $F_0+F_F$ followed by node projection, retaining $s/q$ feedback.

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

but this does not imply identical trajectories.

## Experiment 0 — software, protocol, and runner integrity

Completed at software level:

- independent derivative and RK4 parity for all four models;
- declared mechanism reductions;
- projector, tangency, retraction, singular, and same-state identity checks;
- frozen human- and machine-readable Phase 5 protocol;
- executable metrics, bootstrap, validation, lock, and fail-closed decision rules;
- deterministic pilot/confirmatory split;
- pilot-only planner and batch authorization;
- direct confirmatory rejection in RK4, DOP853, and archive paths;
- all-model RK4/DOP853 decision paths;
- H5/H6, refinement, endpoint, and alternate-integrator gates;
- exogenous replay and frozen-$s/q$ controls;
- all six relabeling tripwires;
- write-once checksummed archive and independent checksum reconstruction;
- separate execution authorization with protected-file integrity.

Hosted verification: 100 tests passed on Python 3.10 and 100 on Python 3.12. No pilot trajectory or scientific result was generated.

## Frozen comparisons

### Primary — $M_F$ versus $M_P$

Tests dynamic distinguishability under

$$
O_{\mathrm{full}}=(x,s,q)
$$

using the frozen symmetric normalized RMS trajectory metric. Detection threshold: $0.02$. Scoped observational-equivalence margin: $0.002$. Positive direction effects must also exceed ten times their numerical floors.

### Secondary

- $M_0$ versus $M_F$: feedback effect under $O_{\mathrm{full}}$.
- $M_0$ versus $M_P$: projection effect under $O_{\mathrm{full}}$.
- $M_P$ versus $M_{FP}$: later node divergence under $O_x$ despite same-state derivative identity.

Secondary pilot results are developmental and cannot independently promote a scientific claim.

## Frozen domain

Twenty-four deterministic Fibonacci directions are crossed with

$$
c_0\in\{0.05,0.10,0.25,0.50,1.00\},
$$

yielding 120 configurations. A direction-level SHA-256 rule freezes:

- 10 pilot directions, 50 configurations;
- 14 held-out confirmatory directions, 70 configurations.

Confirmatory trajectories may not be generated during the pilot.

## Numerical policy

Reference integration uses fixed-step RK4 over $T=10$ with observations every $0.01$. Every decision-bearing model/map is evaluated at

$$
10^{-3},\quad5\times10^{-4},\quad2.5\times10^{-4}
$$

and under DOP853 with frozen tolerances. Projected models use segmented DOP853 with radial retraction at each segment boundary.

The primary configuration numerical floor is the maximum relevant refinement and alternate-integrator discrepancy over $M_F$ and $M_P$.

## Controls

- canonical feedback/projection removals through $M_0,M_F,M_P,M_{FP}$;
- exogenous replay of the paired fine-$M_F$ signal;
- frozen $s$;
- frozen $q$;
- frozen $(s,q)$;
- all six node permutations.

A graph-incidence intervention and soft-penalty control remain outside protocol v1.0.

## Failure and stop rules

- no imputation;
- all failures and singular runs retained;
- lock, split, H5, H6, parity, and permutation failure stop evaluation;
- more than 10% pilot numerical failures pause execution;
- thresholds, metrics, configurations, and held-out directions cannot change after viewing effects.

## Required archive

```text
RUN_MANIFEST.json
environment/
configs/
raw/
summaries/
failures.jsonl
checksums.sha256
```

Raw outputs are immutable, summaries name every raw input hash, and finalization changes the archive to read-only.

## Execution authorization

Current state:

- model implementation: verified;
- comparative protocol: frozen and verified;
- pilot-only runner/archive: verified;
- development-pilot execution: not performed;
- confirmatory execution: blocked;
- scientific feedback-versus-projection claims: blocked;
- $M_F\equiv M_P$: unverified;
- physical, emergence, novelty, and ontological claims: not authorized.

A separate Phase 6B slice must commit the fixed execution authorization naming the verified runner commit without changing protected files. Only then may the 50 pilot configurations execute.

See `18_phase5_comparative_protocol.md`, `20_phase6_runner_design.md`, and `21_phase6_runner_verification.md`.

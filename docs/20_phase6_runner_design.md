# Phase 6 Pilot-Only Runner Design

## Status

Phase 6A implements and software-verifies the execution and archival machinery for the frozen Phase 5 protocol. This document describes the runner gate; it does not report pilot data.

$$
\boxed{
\text{pilot-only runner verified};
\quad
\text{development pilot not executed};
\quad
\text{confirmatory execution blocked}.
}
$$

No frozen pilot configuration is integrated by the software test suite. Tests use only the manifest-declared smoke state or synthetic arrays excluded from inference.

## Security boundary

The runner is pilot-only by construction:

1. `LOCK.json` is verified before any configuration-bearing manifest is loaded.
2. Only directions labeled `pilot` are reconstructed.
3. Batch authorization rejects empty, duplicate, mixed, or confirmatory batches before integration.
4. RK4 and DOP853 reject a confirmatory configuration directly.
5. The archive rejects non-pilot configurations and trajectories.
6. A structured archive scan rejects confirmatory direction or configuration identifiers.
7. No override flag, environment variable, alternate authorization path, or silent fallback exists.

## Source integrity

Execution requires a full Git history and a clean tracked tree. The runner verifies that

```text
src/apophatic_geometry/model.py
src/apophatic_geometry/models.py
```

remain unchanged from the Phase 4 model baseline

```text
205fb8c5bf1b832e241af230612e3d7056be05f5
```

before execution can proceed.

A later execution authorization must name a previously verified `runner_source_commit`. The authorization may be committed afterward without creating a self-referential commit hash, but all protected model, protocol, runner, analysis, and split-control files must remain unchanged between that runner commit and the execution commit.

## Numerical implementation

For every accepted pilot configuration, the future execution path is fixed to:

- all four models $M_0,M_F,M_P,M_{FP}$;
- RK4 at $10^{-3}$, $5\times10^{-4}$, and $2.5\times10^{-4}$;
- 1001 observations over $T=10$;
- DOP853 replication for every model used by H1–H4;
- segmented DOP853 with radial retraction every $10^{-3}$ for projected models;
- H5 constraint-preservation gates;
- H6 same-state $f_{FP}=f_P$ gates;
- refinement, endpoint, and alternate-integrator acceptance rules for every decision-bearing observation map.

The runner computes the frozen primary configuration-level numerical floor

$$
\nu_{\mathrm{config}}
=
\max_{m\in\{M_F,M_P\}}
\left\{
D(m_{\Delta t/2},m_{\Delta t/4}),
D(m_{\Delta t/4},m_{\mathrm{DOP853}})
\right\}.
$$

## Controls and tripwires

The implementation includes:

- canonical feedback and projection removals through the four-model family;
- exogenous replay of the paired fine-$M_F$ collective signal;
- frozen-$s$, frozen-$q$, and frozen-$(s,q)$ controls;
- all six node relabelings for every canonical model;
- independent smoke-trajectory reconstruction;
- independent pilot-membership and configuration-hash reconstruction;
- independent archive checksum reconstruction.

The independent test path does not call the production planner, archive writer, checksum writer, or summary function it checks.

## Archive and provenance

Each raw trajectory directory contains immutable metadata plus arrays for:

- observation times and indices;
- full states and intrinsic geometry;
- local proposal, feedback, combined proposal, and projection correction;
- constraint, tangency, denominator, and retraction diagnostics;
- numerical segment/step times and indices.

Configuration summaries name every raw input hash and include primary/secondary effects, numerical floors, mechanism ratios, numerical acceptance results, and permutation tripwire results.

## Execution separation

This implementation slice intentionally omits

```text
protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json
```

and therefore cannot execute the frozen pilot. After hosted verification and merge, a separate execution issue must create that record without changing the runner, protocol, metrics, thresholds, configurations, or held-out set.

## Maximum licensed result

> The pilot-only runner and archival pipeline implement the frozen Phase 5 protocol and prevent confirmatory access at tested cases.

This does not license any scientific conclusion.

# Phase 6 Pilot-Only Runner Verification Record

## Status

The Phase 6 pilot-only runner and archival pipeline are implemented and software-verified for protocol `ARG-P5-COMP-v1`.

This result verifies runner behavior at tested cases. It is not a development-pilot result, a confirmatory experiment, or scientific evidence for any ARG mechanism.

## Implemented boundary

The runner:

- verifies `protocol/phase5_v1/LOCK.json` before loading configuration-bearing manifests;
- reconstructs exactly 10 pilot directions and 50 pilot configurations;
- rejects empty, duplicate, mixed, and confirmatory batches before integration;
- rejects confirmatory input independently in RK4, DOP853, and archive paths;
- requires a separately committed execution authorization naming a previously verified runner commit;
- protects model, protocol, runner, analysis, and split-control files after authorization;
- exposes no override flag, environment variable, alternate authorization path, or fallback bypass.

The execution authorization file is intentionally absent from this verification slice. Therefore the frozen pilot cannot execute from this commit.

## Numerical implementation

The verified runner implements:

- all four models at the three frozen RK4 resolutions;
- DOP853 replication for every model used by H1–H4;
- segmented DOP853 plus radial retraction for projected models;
- the frozen observation schedule over $T=10$;
- refinement, endpoint, and alternate-integrator acceptance rules for every decision-bearing map;
- configuration-level primary numerical floors;
- H5 constraint-preservation gates;
- H6 same-state node-identity gates;
- exogenous replay and frozen-$s$, frozen-$q$, and frozen-$(s,q)$ controls;
- all six node relabeling tripwires.

## Archive implementation

The future execution path writes a new immutable archive containing:

```text
RUN_MANIFEST.json
environment/
configs/
raw/
summaries/
failures.jsonl
checksums.sha256
```

Raw trajectory records include full state, node state, adaptive substrate, intrinsic geometry, mechanism decomposition, constraint/tangency diagnostics, denominator, and retraction data. Summaries name every raw input hash. Finalization hashes all files and changes the archive to read-only.

## Independent verification boundary

The test-only reference path independently reconstructs:

- pilot membership and expected count;
- configuration hashes;
- smoke-only trajectories for all four models;
- archive file hashes;
- the no-confirmatory invariant.

It does not call the production planner, archive writer, checksum writer, or summary function it checks.

## Hosted verification

Pull request:

```text
#11
```

Final GitHub Actions run:

```text
30723005085
```

Environments:

- Python 3.10 — **100 passed**;
- Python 3.12 — **100 passed**.

These are 100 unique software tests executed in two Python environments, not 200 independent experimental observations.

## No-pilot-data verification

The final pull-request file list contains source code, tests, protocol documentation, and package/workflow configuration only. It contains no:

- `EXECUTION_AUTHORIZATION.json`;
- pilot trajectory;
- pilot raw archive;
- pilot effect summary;
- pilot failure archive;
- confirmatory trajectory or artifact.

Therefore:

$$
\boxed{
\operatorname{PHASE6\_NO\_PILOT\_DATA}=\text{PASS}.
}
$$

## Licensed result

> ARG implements and software-verifies a fail-closed pilot-only runner and immutable archival pipeline for the frozen Phase 5 protocol, including independent pilot-membership, trajectory, checksum, and confirmatory-lockout checks at tested cases.

## Current execution state

$$
\boxed{
\text{runner verified};
\quad
\text{development pilot not executed};
\quad
\text{confirmatory execution blocked}.
}
$$

## Non-claims

This verification does not establish:

- that $M_F$ and $M_P$ differ or agree;
- any numerical effect size;
- that $M_P$ and $M_{FP}$ trajectories diverge;
- that feedback or projection improves prediction;
- physical adequacy, macro-level causal autonomy, or strong emergence;
- mathematical novelty or a fundamental geometry.

## Next gate

A separate execution slice must commit the fixed authorization record naming the verified runner commit, rerun hosted verification without changing protected files, and only then execute the 50 frozen pilot configurations. Confirmatory access remains blocked.

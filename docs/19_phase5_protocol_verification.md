# Phase 5 Comparative Protocol Verification Record

## Status

Phase 5 is complete. Protocol `ARG-P5-COMP-v1`, version `1.0.0`, was frozen and software-verified before trajectory generation.

This is a preregistration and software-verification result. It is not a pilot, confirmatory experiment, numerical mechanism result, or scientific validation of ARG.

## Frozen primary question

The primary comparison is

$$
M_F\leftrightarrow M_P
$$

under the full-state observation map

$$
O_{\mathrm{full}}=(x,s,q).
$$

The protocol freezes the symmetric normalized RMS trajectory distance

$$
D(A,B)
=
\sqrt{
\frac{2\sum_k\|a_k-b_k\|_2^2}
{\sum_k\|a_k\|_2^2+\sum_k\|b_k\|_2^2+10^{-30}}
},
$$

a detection threshold of `0.02`, and a scoped observational-equivalence margin of `0.002`.

The fail-closed decision rule permits four states:

- `DETECTED`;
- `EQUIVALENT_WITHIN_PROTOCOL_MARGIN`;
- `INCONCLUSIVE`;
- invalid/blocked by integrity or numerical gates.

## Frozen design

The protocol includes:

- 24 deterministic Fibonacci directions on the $z>0$ hemisphere;
- five repeated amplitude conditions per direction;
- 120 total configurations;
- 10 pilot directions and 14 held-out confirmatory directions;
- a public SHA-256 direction-level split rule;
- fixed parameters with no fitting or tuning;
- direction-level inferential units;
- 50,000 deterministic percentile-bootstrap resamples;
- RK4 at three resolutions;
- segmented DOP853 replication for projected models;
- numerical-floor, missing-run, exclusion, and stop rules;
- feedback-removal, projection-removal, exogenous-replay, frozen-$s/q$, and relabeling controls;
- immutable provenance and archive requirements;
- a SHA-256 lock over critical protocol and executable-analysis files.

## Executable protocol machinery

`src/apophatic_geometry/protocol.py` implements:

- symmetric normalized RMS trajectory distance;
- maximum absolute discrepancy;
- mechanism energy ratios;
- deterministic percentile-bootstrap intervals;
- the complete primary decision rule;
- canonical JSON and file hashing;
- protocol and initial-condition validation;
- lock verification.

The tests include known-answer cases for positive, equivalence, and inconclusive outcomes, invalid-input tripwires, deterministic bootstrap behavior, manifest reconstruction, pilot/confirmatory non-overlap, and lock verification.

## Hosted verification

Pull request:

```text
#9
```

Squash merge:

```text
d60bb3e618c590e0c994188cebf060bd4b347903
```

GitHub Actions run:

```text
30720596773
```

Environments:

- Python 3.10 — **65 passed**;
- Python 3.12 — **65 passed**.

These are 65 unique software/protocol tests executed in two Python environments, not 130 independent scientific observations.

## No-data verification

The Phase 5 pull request changed only:

- documentation and metadata;
- machine-readable protocol manifests;
- executable metric, validation, hashing, bootstrap, and decision code;
- protocol unit tests.

It introduced no trajectory, raw-output, summary, result, failure-log, or confirmatory artifact. Therefore:

$$
\boxed{
\operatorname{PHASE5\_NO\_DATA}=\text{PASS}.
}
$$

## Licensed result

The strongest licensed statement is:

> ARG froze and software-verified a falsification-oriented four-model comparative protocol before trajectory generation. The protocol authorizes a development pilot only; confirmatory execution and scientific claims remain blocked.

## Current ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

Current execution authorization:

$$
\boxed{
\text{development pilot authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

Authorization is not execution. No development pilot has run.

## Non-claims

Phase 5 does not establish:

- that $M_F$ and $M_P$ differ;
- that $M_F$ and $M_P$ are observationally equivalent;
- that $M_P$ and $M_{FP}$ trajectories diverge;
- that feedback or projection improves prediction;
- that any ARG mechanism is physically adequate;
- macro-level causal autonomy or strong emergence;
- mathematical novelty;
- a fundamental geometry.

## Next gate

Phase 6 must implement and independently verify the pilot-only runner, archive pipeline, numerical replication, control schedule, and confirmatory-access tripwires before the authorized development pilot is executed.

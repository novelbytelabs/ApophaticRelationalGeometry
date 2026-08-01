# Legacy Euler `run.csv` — Rejected as Current Evidence

## Status

The `run.csv` contained in the 2026-08-01 delivered audit bundle is **rejected** as evidence for the current ARG implementation or any Phase-5/Phase-6 result.

The independent audit established that the file reproduced the legacy explicit-Euler path, not the current RK4 simulator. It also lacked the protocol, split, configuration, integrator, source, environment, and completion attestations required for a trustworthy result.

## Binding rule

No ARG document, release, audit bundle, result package, or scientific statement may cite that file as:

- current simulator output;
- four-model experiment output;
- Phase-5 or Phase-6 data;
- evidence for feedback, projection, equivalence, emergence, or physical adequacy.

## Current output requirements

A standalone exploratory output must include:

- explicit protocol and integrator identifiers;
- scientific configuration hash;
- source-bound execution hash;
- Git-derived source commit and tracked-tree hash;
- protocol-lock and runtime-environment fingerprints;
- expected and actual row counts;
- final output SHA-256;
- a separate `COMPLETE` manifest;
- atomic final-file publication.

A pilot archive must additionally include a cleared execution policy, committed authorization, complete attestation, run identity, immutable checksums, and zero confirmatory access.

Any future audit-bundle builder must reject unclassified `run.csv` files and any generated result lacking a valid completion record.

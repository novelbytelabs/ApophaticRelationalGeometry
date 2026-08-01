# ARG Phase 5 frozen protocol bundle

This directory is the machine-readable companion to
`docs/18_phase5_comparative_protocol.md`.

Files:

- `protocol.json` — hypotheses, metrics, thresholds, numerical policy, decisions, exclusions, provenance, and claim control.
- `parameters.json` — frozen parameter values and no-tuning policy.
- `initial_conditions.json` — deterministic 24-direction design, five amplitudes, and direction-level pilot/confirmatory split.
- `interventions.json` — mechanism removals, exogenous replay, adaptive-substrate ablations, relabeling tripwires, and excluded contract changes.
- `LOCK.json` — SHA-256 hashes for the critical protocol and executable-analysis files.

The status `FROZEN_NO_DATA` means no trajectory has been authorized or produced
as part of Phase 5. The protocol bundle may authorize only a development pilot
after all lock and software gates pass. Confirmatory execution remains blocked.

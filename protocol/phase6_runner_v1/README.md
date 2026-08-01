# Phase 6 pilot-only runner v1

## Status

**Runner implementation exists, but Phase 6A.1 is STOP-SHIP. No pilot has been executed and no execution authorization may be added.**

An independent audit identified integrity defects in the delivered bundle and supporting code paths. Phase 6B remains blocked until:

1. the Phase 6A.1 adversarial remediation suite passes;
2. the frozen protocol lock is remediated through an explicit versioned record;
3. source, runtime, integrator, and archive provenance are hash-bound;
4. a fresh audit bundle validates itself after clean extraction; and
5. an external Auditor AI reports no remaining STOP-SHIP finding.

The runner implements protocol `ARG-P5-COMP-v1` for the 50 frozen pilot configurations. Confirmatory trajectory generation remains blocked in planning, batch authorization, RK4, DOP853, archive writing, and contamination scanning.

## Current permitted commands

```bash
arg-pilot validate --repo-root .
arg-pilot plan --repo-root .
```

These commands are data-free. They do not execute trajectories.

## Prohibited command

```bash
arg-pilot execute --repo-root . --archive <path>
```

Execution is prohibited while Phase 6A.1 is open. `EXECUTION_AUTHORIZATION.json` must remain absent.

## Environment policy

`EXECUTION_ENVIRONMENT.json` freezes the intended future Phase 6B execution environment and fingerprint policy. It is not an authorization record.

## Claim ceiling

The runner and its tests do not establish a numerical mechanism result, feedback–projection equivalence, predictive superiority, physical adequacy, causal autonomy, emergence, novelty, or ontology.

# Phase 6 pilot-only runner v1

## Status

**The external Phase 6A.2 report assigned 85/100 with a conditional pass. Its five demonstrated guardrail failures have now been remediated and the supplied external tripwire reports 19 PASS / 0 FAIL / 0 INCONCLUSIVE. No execution authorization exists and no pilot has been executed.**

The audited candidate was:

```text
17a17398808cae1befe85e795d371012fe999f03
```

and it merged as:

```text
4fb987b34220927466812f0276e10bb0776c28fd
```

The accepted re-audit packet SHA-256 is:

```text
5d524253f24f31893ce44e1be4a0de1fa3ab9ae2f87812ee2d35416ac5ca84fd
```

The runner implements protocol `ARG-P5-COMP-v1` for the 50 frozen pilot configurations. Confirmatory trajectory generation remains blocked in planning, batch authorization, RK4, DOP853, archive writing, and contamination scanning.

## Data-free commands

```bash
arg-pilot validate --repo-root .
arg-pilot plan --repo-root .
```

These commands do not execute trajectories.

## Execution command

```bash
arg-pilot execute --repo-root . --archive <new-empty-path>
```

The command remains fail-closed while `EXECUTION_AUTHORIZATION.json` is absent. After the remediated runner is merged, exactly one authorization-only commit must bind the final runner Git tree, report and tripwire SHA-256 values, frozen execution scope, and archive destination.

## Environment policy

`EXECUTION_ENVIRONMENT.json` accurately records the 85/100 conditional verdict and the post-report remediation state. It permits pilot execution only through a separate committed execution record. It does not authorize execution by itself.

## Claim ceiling

The runner and its tests do not establish a numerical mechanism result, feedback–projection equivalence, predictive superiority, physical adequacy, causal autonomy, emergence, novelty, or ontology.

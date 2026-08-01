# Phase 6 pilot-only runner v1

## Status

**Runner implementation and software verification passed. No pilot has been executed.**

The runner implements protocol `ARG-P5-COMP-v1` for the 50 frozen pilot configurations. Confirmatory trajectory generation is blocked in the planner, batch authorizer, RK4 path, DOP853 path, archive writer, execution authorization, and archive contamination scan.

Hosted verification:

- GitHub Actions run `30722763003`;
- Python 3.10: 100 passed;
- Python 3.12: 100 passed.

## Data-free commands

```bash
arg-pilot validate --repo-root .
arg-pilot plan --repo-root .
```

Both commands verify the Phase 5 lock, reconstruct only the pilot plan, and check that the Phase 4 model files are unchanged. They generate no trajectory.

The command

```bash
arg-pilot execute --repo-root . --archive artifacts/phase6_pilot
```

fails closed unless a later execution slice commits the fixed file:

```text
protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json
```

There is no command-line flag, environment variable, alternate path, or fallback that bypasses this gate.

## Future authorization record

The authorization file must name:

- protocol and runner identifiers;
- the previously hosted-verified `runner_source_commit`;
- an execution identifier and UTC timestamp;
- split `pilot`;
- `confirmatory_execution: BLOCKED`.

The execution commit may add the authorization file, but protected model, protocol, runner, analysis, and split-control files must remain equivalent to the authorized runner commit.

## Archive layout

A successful future pilot execution writes a new, empty destination containing:

```text
RUN_MANIFEST.json
environment/
configs/
raw/
summaries/
failures.jsonl
checksums.sha256
```

Raw arrays and metadata are write-once. Finalization hashes every file and changes the archive to read-only. Failed and singular runs are retained without imputation.

## Non-claims

Passing the runner gate establishes software behavior only. It does not establish a numerical mechanism result, feedback–projection equivalence, physical adequacy, causal autonomy, strong emergence, mathematical novelty, or ontology.

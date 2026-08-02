# Phase 6B.0 Clearance Integration and Pilot Authorization Freeze

## Status

Phase 6A.2 passed external re-audit. The audited candidate

```text
17a17398808cae1befe85e795d371012fe999f03
```

was merged as

```text
4fb987b34220927466812f0276e10bb0776c28fd
```

The accepted re-audit packet SHA-256 is

```text
5d524253f24f31893ce44e1be4a0de1fa3ab9ae2f87812ee2d35416ac5ca84fd
```

This closes the STOP-SHIP remediation gate. It does **not** itself authorize or execute the development pilot.

## Current execution boundary

$$
\boxed{
\text{execution substrate externally cleared};
\quad
\text{execution authorization absent};
\quad
\text{pilot not executed};
\quad
\text{confirmatory execution blocked}.
}
$$

The environment policy now permits execution only through the separately committed authorization path. `EXECUTION_AUTHORIZATION.json` remains absent.

## Required authorization record

The next commit may add exactly one execution record only after every required value is known. It must bind:

- authorization ID, protocol ID/version, runner ID/version, and pilot split;
- the verified Phase 6B runner-source commit;
- a unique execution ID and UTC timestamp;
- exact protocol-lock, integrity-baseline, environment-policy, pilot-membership, integrator-suite, archive-schema, configuration-count, trajectory-count, and summary-count scope;
- exact SHA-256 values for the accepted re-audit packet, accepted external audit report, and frozen tripwire;
- confirmatory execution as `BLOCKED`;
- a new empty archive destination dedicated to this execution.

No placeholder, synthetic digest, narrative substitute, or self-authored replacement for the external audit report is permitted.

## Slice exit gate

Phase 6B.0 passes when:

1. the environment policy records external clearance while requiring a separate execution record;
2. the integrity baseline and all protected hashes are consistent;
3. the ordinary suite, hardened tripwire, and full-horizon gate pass;
4. no execution authorization or trajectory artifact exists; and
5. the exact accepted external audit report SHA-256 is available for the authorization commit.

## Claim ceiling

This slice establishes only that the runner remediation gate was externally cleared and that the repository is authorization-ready. It provides no pilot result and no scientific evidence for or against the ARG hypotheses.

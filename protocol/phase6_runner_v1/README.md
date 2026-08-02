# Phase 6 pilot-only runner v1

## Status

**Runner version 1.1.0 is under Phase 6B.2 external review. No execution authorization exists and no completed pilot result exists.**

The first authorized runner-1.0 attempt stopped fail closed in GitHub Actions run `30763372785` after six H6 same-state identity failures exceeded the frozen 10% pause rule. The partial archive is preserved as evidence; it contains zero completed summaries and licenses no scientific conclusion.

Blinded diagnosis established that the exact identity

$$
f_{FP}(Z)=f_P(Z)
$$

remained intact to machine precision. The legacy H6 forward-relative diagnostic became ill-conditioned as both projected node derivatives approached zero near a projected equilibrium.

## H6 policy v2

Runner `1.1.0` binds H6 policy `ARG-H6-CONDITION-AWARE-v2`:

- retain the `1e-12` forward-relative tolerance when the projected signal is well-conditioned;
- use a `128 * eps64` backward-error bound when the projected signal is cancellation dominated;
- independently require the MFP node-feedback vector to remain radial within the same FP64 bound;
- record absolute error, forward-relative error, backward error, radiality error, signal scale, input scale, and conditioning ratio;
- reject deliberate non-radial or tangent mismatches;
- require an all-50, pilot-only H6 diagnostic before reauthorization.

This is a versioned numerical-validity repair. Model equations, parameters, initial conditions, pilot/confirmatory membership, scientific effect thresholds, and decision rules are unchanged.

## Data-free commands

```bash
arg-pilot validate --repo-root .
arg-pilot plan --repo-root .
python tools/h6_conditioning_diagnostic.py --repo-root . --output h6.json
```

The H6 diagnostic integrates only the 50 frozen pilot `MP` trajectories at the reference RK4 step. It does not compute the primary `MF` versus `MP` effect and does not access the confirmatory split.

## Execution boundary

`EXECUTION_AUTHORIZATION.json` is absent. The failed authorization is consumed and cannot be reused. A new authorization requires external audit clearance of the exact runner-1.1.0 commit and a new empty archive destination.

Confirmatory execution remains blocked at every layer.

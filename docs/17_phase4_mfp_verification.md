# Phase 4 MFP Verification Record

## Status

Phase 4 is complete for the contract-v1.0 combined feedback-plus-projection model $M_{FP}$.

This is a software and mathematical-mechanism verification result. It is not a comparative scientific experiment, a validation of physical adequacy, or evidence that $M_F$ and $M_P$ are equivalent.

## Implemented ordering

The model first constructs the explicit feedback proposal

$$
F_{\mathrm{proposal}}=F_0+F_F,
$$

then projects the node component onto the tangent space of

$$
\Gamma(Z)=c(x)-c_0=\frac13x^Tx-c_0=0.
$$

The node derivative is

$$
f_{FP}
=
P_T\left(f_0-\chi c(x)x\right),
\qquad
P_T=I-\frac{xx^T}{x^Tx}.
$$

Because the node-feedback term is radial and $P_Tx=0$,

$$
\boxed{f_{FP}=f_P}
$$

at the same regular full state.

The equality is a same-state vector-field identity. It does not imply identical $M_P$ and $M_{FP}$ trajectories, because $M_{FP}$ retains feedback in the adaptive substrate:

$$
\tau_s\dot s_{ij}^{(FP)}
=
\eta_0-\eta_1(x_i-x_j)^2+\eta_2c(x)-s_{ij},
$$

$$
\tau_q\dot q_{ij}^{(FP)}
=
-\gamma q_{ij}+\kappa(x_i-x_j)^2-\rho c(x).
$$

Those $s/q$ differences can alter later conductances and therefore later node proposals.

## Mechanism decomposition

The production path exposes separately:

- the local/adaptive proposal $F_0$;
- the collective-feedback vector $F_F$;
- the combined unprojected proposal $F_0+F_F$;
- the node-space projection correction;
- the projected derivative;
- the feedback and correction norms;
- the constraint and tangency residuals;
- the projection denominator;
- the raw and post-retraction residuals;
- the retraction magnitude.

## Numerical implementation

The implementation uses:

- the same fixed-step classical RK4 policy as the other models;
- projection at all four derivative stages;
- the same mandatory radial retraction as $M_P$;
- the same frozen singular threshold;
- fail-closed behavior with no silent pseudoinverse, denominator clipping, or fallback projection;
- model, contract, source-commit, and configuration-hash output fields.

## Verification coverage

The verification suite checks:

- the unprojected $M_{FP}$ proposal reconstructs $M_F$;
- removing all feedback recovers $M_0$ before projection;
- radial node feedback is annihilated by projection;
- $f_{FP}=f_P$ at matched regular states;
- the $s/q$ feedback terms remain present;
- proposal plus correction equals the projected derivative;
- $M_{FP}(\chi=\eta_2=\rho=0)=M_P$;
- target omission or mismatch fails closed;
- node-permutation equivariance;
- production/reference derivative parity;
- production/reference projected-RK4 and retraction parity;
- post-retraction constraint preservation;
- decreasing raw constraint drift and retraction magnitude under the frozen one-step refinement test;
- retention of every prior $M_0$, $M_F$, and $M_P$ regression;
- finite, labeled $M_{FP}$ simulation diagnostics.

## Hosted verification

Pull request:

```text
#7
```

Squash merge:

```text
205fb8c5bf1b832e241af230612e3d7056be05f5
```

GitHub Actions run:

```text
30718821666
```

Environments:

- Python 3.10 — PASS;
- Python 3.12 — PASS.

Each environment reported:

```text
51 passed
```

These are 51 unique software tests executed in two Python environments, not 102 independent scientific observations.

## Licensed claim

The strongest licensed statement is:

> ARG implements and unit-tests all four contract-v1.0 prototypes. $M_{FP}$ implements an explicit collective-feedback proposal followed by node-state tangent projection and mandatory retraction, with separate mechanism diagnostics and independent software-reference parity.

## Current ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Non-claims

This result does not establish:

- that $M_F$ and $M_P$ are dynamically or observationally equivalent;
- that identical same-state node derivatives imply identical trajectories;
- that feedback or projection improves scientific prediction;
- that constant node amplitude is physically correct;
- that $M_{FP}$ represents macro-level causal autonomy or strong emergence;
- that the four-model comparative experiment has been executed;
- that ARG is a new fundamental geometry.

## Next gate

Phase 5 must freeze the comparative experiment protocol before any development pilot is run. The protocol must specify hypotheses, observation maps, parameter and initial-condition manifests, inferential units, solver/refinement rules, exclusions, stop rules, and raw-output provenance.
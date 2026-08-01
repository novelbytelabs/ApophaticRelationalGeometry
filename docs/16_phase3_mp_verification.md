# Phase 3 MP Verification Record

## Status

Phase 3 completed the contract-v1.0 constant-amplitude projected-admissibility sandbox $M_P$.

This is a software and mathematical-mechanism verification result. It is not a scientific validation of ARG, a proof of physical adequacy, or evidence that $M_F$ and $M_P$ are equivalent.

Phase 4 subsequently implemented $M_{FP}$. The present project ceiling is maintained in `13_alignment_and_claim_ceiling.md`; this document preserves the Phase 3 verification record.

## Implemented constraint

$$
\Gamma(Z)=c(x)-c_0=\frac13x^Tx-c_0=0,
\qquad
c_0=c(x(0))\ge 10^{-6}.
$$

The tangent projector is

$$
P_T(x)=I_3-\frac{xx^T}{x^Tx},
$$

and the projected node derivative is

$$
\boxed{
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The $s$ and $q$ derivatives remain the $M_0$ proposal equations.

## Numerical implementation

The implementation includes:

- projection at every classical RK4 derivative stage;
- mandatory post-step radial retraction;
- fail-closed behavior at or below the frozen norm threshold;
- no silent pseudoinverse, denominator clipping, or fallback projection;
- explicit proposal, correction, projected derivative, denominator, tangency, constraint, and retraction diagnostics;
- model, contract, source-commit, and configuration-hash output fields.

The retraction is

$$
x^+\leftarrow \sqrt{3c_0}\frac{x^+}{\|x^+\|}.
$$

## Verification coverage

The verification suite checks:

- $P_T^T=P_T$;
- $P_T^2=P_T$;
- $P_Tx=0$;
- $x^Tf_P=0$;
- the continuous-time constraint derivative vanishes;
- a hand-computed projection case;
- retraction restores $c(x)=c_0$;
- retraction is null up to roundoff on an admissible state;
- zero and near-singular states fail closed;
- invalid or mismatched $c_0$ fails closed;
- node-permutation equivariance;
- production/reference derivative parity;
- production/reference projected-RK4 and retraction parity;
- decreasing raw constraint drift and retraction magnitude under step refinement;
- retention of all prior $M_0/M_F$ regressions;
- finite, labeled MP simulation diagnostics.

## Hosted verification

Pull request: `#5`

Squash merge:

```text
97a9f6b7222b4543ee8184fb8e42b47b53ddf92c
```

GitHub Actions run:

```text
30717582276
```

Environments:

- Python 3.10 — PASS;
- Python 3.12 — PASS.

Each environment reported:

```text
35 passed
```

These are 35 unique tests executed in two Python environments, not 70 independent scientific observations.

## Licensed claim

The strongest Phase 3 statement is:

> ARG implements and unit-tests the contract-v1.0 $M_P$ constant-amplitude projection sandbox, including stage projection, mandatory retraction, fail-closed singular handling, and independent software-reference parity.

## Non-claims

This result does not establish:

- that constant node amplitude is a law of nature;
- that the sandbox is ARG's completed relational-admissibility geometry;
- that projection improves scientific prediction;
- that feedback and projection are equivalent;
- that macro-level causal autonomy or strong emergence has been demonstrated;
- that the four-model comparative experiment has been executed.

## Subsequent gate

Phase 4 implemented $M_{FP}$ and verified the same-state node identity

$$
\boxed{f_{FP}=f_P}
$$

while retaining feedback in $s$ and $q$.

See `17_phase4_mfp_verification.md`. The active gate is now the Phase 5 comparative experiment protocol.

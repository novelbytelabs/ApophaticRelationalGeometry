# Phase 6B.1 H6 Failure Analysis

## Status

The first authorized development-pilot attempt stopped correctly after six H6 failures exceeded the frozen 10% pause rule. The resulting archive is partial and cannot support a scientific conclusion.

The failed execution is preserved as evidence:

- GitHub Actions run: `30763372785`;
- authorized commit: `e8c5467cd0a3ddd35c07489c55b4fa6dfa987388`;
- audited runner parent: `92884777c1e9f10f7c2732f4d86e9ac966ca51ad`;
- handoff ZIP SHA-256: `42d27f5c63fbedc32f925649f92f3816b49b3f7c5f873e2cc5d3e4e4bed93b8b`;
- partial archive TAR SHA-256: `2c5e6ed1473303e382d49413857c2aa89f394ada44e739403dffded8b395ecc9`;
- completed summaries: zero;
- confirmatory execution: blocked.

No primary `MF` versus `MP` effect was inspected during diagnosis.

## Observed failure pattern

The legacy H6 diagnostic was

$$
E_{\mathrm{forward}}
=
\frac{\lVert f_P-f_{FP}\rVert_2}
{\lVert f_P\rVert_2+\lVert f_{FP}\rVert_2+10^{-30}}.
$$

All five amplitudes for direction `d03` failed, followed by `d11-c005`. The largest reported value was approximately

$$
1.32\times10^{-7}.
$$

A blinded reconstruction showed that the corresponding absolute discrepancy was only

$$
\lVert f_P-f_{FP}\rVert_2
\approx3.93\times10^{-17},
$$

while both projected derivatives had norm about

$$
1.30\times10^{-10}.
$$

Across the six failed configurations, the maximum reproduced absolute discrepancy was below

$$
2.8\times10^{-16}.
$$

At the worst state, 100-decimal-digit arithmetic reduced the projected identity residual to approximately $7.8\times10^{-102}$.

## Diagnosis

The exact structural identity remains valid:

$$
f_{FP}(Z)=f_P(Z)
$$

at the same regular state, because the MFP node-feedback term is radial and the tangent projector annihilates it.

The failed diagnostic was not uniformly well-conditioned. As trajectories approached a projected equilibrium, both legitimate projected derivatives approached zero. Dividing a binary64 cancellation residual by that vanishing signal amplified roundoff into an apparent identity violation.

Therefore:

$$
\boxed{
\text{the mathematical identity was not falsified};
\quad
\text{the legacy forward-relative H6 measurement was falsified}.
}
$$

## Condition-aware H6 policy

Runner version `1.1.0` introduces policy `ARG-H6-CONDITION-AWARE-v2`.

Let

$$
A=\lVert f_P-f_{FP}\rVert_2,
$$

$$
S=\lVert f_P\rVert_2+\lVert f_{FP}\rVert_2,
$$

and let $I$ be the maximum node-proposal scale among the local, feedback, and combined proposals.

The gate records:

$$
E_f=A/S,
\qquad
E_b=A/I,
\qquad
\kappa^{-1}=S/I.
$$

The binary64 backward-error allowance is

$$
B=128\,\epsilon_{64},
$$

and the existing forward-relative tolerance remains

$$
R=10^{-12}.
$$

The forward-relative criterion is used only when

$$
\frac{S}{I}\ge\frac{B}{R}.
$$

Otherwise, the state is classified as cancellation dominated and must satisfy the backward-error bound $E_b\le B$. Independently, the node-feedback vector must remain radial within the same machine-precision bound.

This is not a scientific effect-threshold change. It is a versioned repair of a numerically singular implementation-validity measurement. The old authorization is consumed and cannot be reused.

## Falsification protection

The new gate must still fail when:

- a genuine tangent discrepancy is injected into $f_{FP}$;
- the MFP feedback vector is made non-radial;
- a well-conditioned forward-relative discrepancy exceeds $10^{-12}$.

A dedicated diagnostic integrates all 50 frozen pilot `MP` trajectories at the reference RK4 step and reports H6 quantities only. It does not compute the primary hypothesis effect and does not access the confirmatory split.

## Current boundary

No pilot result exists. Before any reauthorization:

1. all ordinary tests must pass;
2. the hardened tripwire must pass;
3. the all-50 H6 diagnostic must pass in the exact environment;
4. the full-horizon numerical gate must pass;
5. an external auditor must clear the exact runner `1.1.0` artifact.

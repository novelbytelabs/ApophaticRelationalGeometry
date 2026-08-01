# Dynamic Relational Constraint Geometry

## Status of this document

This document specifies the ARG model family and distinguishes implemented mechanisms from broader targets.

Current executable status:

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

The projected models are contract-v1.0 constant-amplitude mechanism sandboxes. They are not the completed relational-admissibility geometry and have not been validated as physical models.

## 1. Provisional presentation

Let

$$
\bar G=(V,\bar E)
$$

be a potential undirected graph. A general target state may be written

$$
Z=(x,s,q,\theta,c).
$$

For node $i$ and edge $e$:

$$
x_i\in M_i,
\qquad
s_e,q_e\in\mathbb R.
$$

The active edge strength is

$$
a_e=\sigma(s_e)=\frac{1}{1+e^{-s_e}}.
$$

The implemented three-node specialization uses

$$
Z=(x,s,q)\in\mathbb R^9.
$$

## 2. Relational mismatch

For $e=(i,j)$, define endpoint maps into a shared comparison space $Y_e$:

$$
\rho_{ie}:M_i\times\Theta_i\times C\to Y_e,
$$

$$
\rho_{je}:M_j\times\Theta_j\times C\to Y_e.
$$

Where subtraction is defined, a residual may be written

$$
\delta_e(Z)=\rho_{ie}(x_i,\theta_i,c)-\rho_{je}(x_j,\theta_j,c).
$$

Otherwise an explicit discrepancy map into a normed residual space must be supplied.

A candidate coherence energy is

$$
\mathcal E_{\mathrm{coh}}(Z)
=
\frac12\sum_{e\in\bar E}a_e\delta_e^{\mathsf T}W_e\delta_e.
$$

This richer compatibility structure is not implemented in contract v1.0.

## 3. Intrinsic geometry

Define positive intrinsic edge length

$$
\ell_e(Z)
=
\frac{e^{q_e}}{a_e}\psi_e\bigl(\delta_e(Z)\bigr),
\qquad
\psi_e>0.
$$

The intrinsic distance is

$$
d_Z(i,j)
=
\inf_{\gamma:i\rightsquigarrow j}
\sum_{e\in\gamma}\ell_e(Z).
$$

The implemented scalar specialization is

$$
\ell_{ij}
=
\frac{e^{q_{ij}}}{\sigma(s_{ij})}
\sqrt{\epsilon^2+(x_i-x_j)^2}.
$$

For the complete undirected three-node graph with finite positive edge lengths, shortest-path distance is a metric.

## 4. $M_0$: local/adaptive proposal

$M_0$ defines the shared proposal field

$$
\dot Z_0=F_0(Z).
$$

For node $i$:

$$
\dot x_i^{(0)}
=
\alpha x_i-
\beta x_i^3+
\sum_{j\ne i}w_{ij}(x_j-x_i),
$$

where

$$
w_{ij}=\sigma(s_{ij})e^{-q_{ij}}.
$$

For edge $(i,j)$:

$$
\tau_s\dot s_{ij}^{(0)}
=
\eta_0-\eta_1(x_i-x_j)^2-s_{ij},
$$

$$
\tau_q\dot q_{ij}^{(0)}
=
-\gamma q_{ij}+\kappa(x_i-x_j)^2.
$$

No value computed from

$$
c(x)=\frac13x^Tx
$$

enters an $M_0$ transition equation.

## 5. $M_F$: collective feedback

Define

$$
F_F(Z)
=
\left(
-\chi c(x)x,
\frac{\eta_2c(x)}{\tau_s}\mathbf 1,
-\frac{\rho c(x)}{\tau_q}\mathbf 1
\right).
$$

Then

$$
\dot Z_F=F_0(Z)+F_F(Z).
$$

The exact frozen-equation reduction

$$
M_F(\chi=\eta_2=\rho=0)=M_0
$$

is implemented and unit-tested.

This is collective feedback. It is not tangent-space projection.

## 6. General projected admissibility

A general projected model requires

$$
\Gamma(Z)=0,
\qquad
H(Z)\ge0,
$$

with admissible set

$$
\mathcal M=\{Z:\Gamma(Z)=0,\ H(Z)\ge0\}.
$$

A proposal field $F$ is mapped to admissible motion:

$$
\dot Z=\Pi_{T_Z\mathcal M}F(Z).
$$

For smooth equality constraints and positive-definite state metric $G(Z)$, the regular equality-only expression is

$$
\dot Z
=
F
-
G^{-1}J_\Gamma^{\mathsf T}
\left(J_\Gamma G^{-1}J_\Gamma^{\mathsf T}\right)^{-1}
J_\Gamma F,
$$

when the indicated matrix is invertible. Inequality constraints require tangent-cone or active-set treatment and are not implemented in version 1.0.

## 7. Implemented $M_P$ version 1.0

### Constraint

$$
\Gamma(Z)
=
c(x)-c_0
=
\frac13x^Tx-c_0=0,
$$

where

$$
c_0=c(x(0))\ge10^{-6},
\qquad
H=\varnothing.
$$

### Jacobian and regularity

$$
J_\Gamma(Z)
=
\left(\frac23x^T,0,0\right).
$$

On the declared manifold,

$$
J_\Gamma J_\Gamma^T
=
\frac49x^Tx
=
\frac43c_0>0.
$$

Thus the rank-one equality projection is regular on the declared domain.

### Tangent projection

With $G=I_9$, projection acts only on the node derivative:

$$
P_T(x)=I_3-\frac{xx^T}{x^Tx},
$$

$$
\boxed{
f_P=P_Tf_0
=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The $s$ and $q$ derivatives remain their $M_0$ proposal values.

Tangency follows algebraically:

$$
x^Tf_P=0,
$$

and therefore

$$
\frac{d}{dt}\Gamma(Z(t))
=
\frac23x^Tf_P=0.
$$

## 8. Implemented $M_{FP}$ version 1.0

The combined model first constructs

$$
F_{\mathrm{proposal}}=F_0+F_F,
$$

then projects the node component.

The node derivative is

$$
f_{FP}=P_T\left(f_0-\chi c(x)x\right).
$$

Since

$$
P_Tx=0,
$$

the radial node-feedback term is annihilated:

$$
P_T[-\chi c(x)x]=0.
$$

Therefore, at the same regular full state,

$$
\boxed{f_{FP}=f_P}.
$$

The $s$ and $q$ derivatives retain the feedback terms:

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

Thus, in general,

$$
\dot s^{(FP)}\ne\dot s^{(P)},
\qquad
\dot q^{(FP)}\ne\dot q^{(P)}.
$$

The same-state node identity does not imply trajectory identity. Divergent $s/q$ states can change later conductances and later node proposals.

The production implementation exposes separately $F_0$, $F_F$, $F_0+F_F$, the projection correction, and the projected derivative.

## 9. Numerical preservation for projected models

Every classical RK4 stage evaluates the applicable projected vector field. After each complete step, the node state is retracted:

$$
x_{n+1}
=
\sqrt{3c_0}\frac{x_{n+1}^{\mathrm{raw}}}
{\|x_{n+1}^{\mathrm{raw}}\|}.
$$

The implementation records:

- local proposal;
- feedback vector where applicable;
- combined proposal where applicable;
- projection correction;
- projected derivative;
- constraint residual;
- normalized tangency residual;
- projection denominator;
- pre- and post-retraction residual;
- retraction magnitude.

It fails closed if a projected stage or retraction reaches the frozen near-singular threshold. No silent pseudoinverse, denominator clipping, or fallback projection is used.

## 10. Dynamic topology and metric

A broader system may include

$$
\dot x_i=f_i(x_i,x_{\mathcal N_i},s,q,c),
$$

$$
\dot s_e=g_e(s_e,\delta_e,x_i,x_j,c),
$$

$$
\dot q_e=h_e(q_e,\delta_e,x_i,x_j,c),
$$

$$
\dot c=R(c,\Psi(Z)).
$$

Whether $c$ is algebraically derived or independently dynamical must be declared per model. In contract v1.0 it is algebraically derived.

## 11. Non-collapse barrier

A future variant may define

$$
U_{\mathrm{barrier}}(Z)
=
\sum_e\frac{B_e}{\ell_e(Z)^{p_e}},
\qquad B_e,p_e>0.
$$

The implication from divergent potential to an unreachable finite-energy boundary remains conditional on a suitable conserved or coercive energy bound. The barrier is not implemented in the four contract-v1.0 models.

## 12. Equivariance

For admissible presentation transformation $g$, the target requirement is

$$
F(g\cdot Z)=Dg_ZF(Z).
$$

Permutation equivariance is unit-tested for all four models. General coordinate and presentation invariance remains a proof obligation.

## 13. Claim boundary

The statements

> ARG implements the contract-v1.0 constant-amplitude projection sandbox

and

> ARG implements feedback followed by projection with separate mechanism diagnostics

are licensed at the software-verification level.

The broader statements

> ARG has validated a physical projected geometry

or

> collective feedback and projection are equivalent

remain unverified.
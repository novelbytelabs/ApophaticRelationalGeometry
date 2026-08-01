# Dynamic Relational Constraint Geometry

## Status of this document

This document specifies the **target ARG model family**, including projected-admissibility variants. It is not a claim that every mechanism is currently implemented.

Current executable status:

$$
M_0,M_F\ \text{implemented and unit-tested};
\qquad
M_P,\ M_{FP},\ M_F\equiv M_P\ \text{unverified}.
$$

The implemented three-node models contain adaptive relations and state-dependent intrinsic distance. $M_0$ has no collective transition path. $M_F$ adds endogenous collective feedback. Neither implements the $\Gamma/H$ projection defined below.

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
a_e=\sigma(s_e)=\frac{1}{1+\exp(-s_e)}.
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

Where subtraction is defined, a mismatch residual may be written

$$
\delta_e(Z)=\rho_{ie}(x_i,\theta_i,c)-\rho_{je}(x_j,\theta_j,c).
$$

Otherwise an explicit discrepancy map must be supplied.

A candidate coherence energy is

$$
\mathcal E_{\mathrm{coh}}(Z)
=
\frac{1}{2}
\sum_{e\in\bar E}
a_e\delta_e^{\mathsf T}W_e\delta_e.
$$

This compatibility structure belongs to the target family and is not yet implemented in the three-node code.

## 3. Intrinsic geometry

Define positive intrinsic edge length

$$
\ell_e(Z)
=
\frac{\exp(q_e)}{a_e}
\psi_e\bigl(\delta_e(Z)\bigr),
$$

with $\psi_e>0$. A simple choice is

$$
\psi_e(\delta)=\sqrt{\epsilon^2+\|\delta\|^2}.
$$

The intrinsic distance is

$$
d_Z(i,j)
=
\inf_{\gamma:i\rightsquigarrow j}
\sum_{e\in\gamma}\ell_e(Z).
$$

The implemented models use the scalar specialization

$$
\ell_{ij}
=
\frac{e^{q_{ij}}}{\sigma(s_{ij})}
\sqrt{\epsilon^2+(x_i-x_j)^2}.
$$

## 4. Implemented $M_0$ mechanism

$M_0$ contains local nonlinear dynamics, neighbor coupling, adaptive edge activation, and metric deformation:

$$
\dot Z_0=F_0(Z).
$$

No value computed from

$$
c(x)=\frac13x^Tx
$$

enters an $M_0$ transition equation. The statistic may be logged only as an observation.

## 5. Implemented $M_F$ mechanism

$M_F$ adds the feedback vector

$$
F_F(Z)
=
\left(
-\chi c(x)x,
\frac{\eta_2c(x)}{\tau_s}\mathbf 1,
-\frac{\rho c(x)}{\tau_q}\mathbf 1
\right),
$$

so that

$$
\dot Z_F=F_0(Z)+F_F(Z).
$$

The exact frozen-equation reduction

$$
M_F(\chi=\eta_2=\rho=0)=M_0
$$

is implemented and unit-tested.

## 6. Target projected-admissibility mechanism

A projected variant requires explicit equality and inequality constraints:

$$
\Gamma(Z)=0,
\qquad
H(Z)\geq0.
$$

Then

$$
\mathcal M
=
\{Z:\Gamma(Z)=0,\ H(Z)\geq0\}.
$$

A local model proposes velocity $F_{\mathrm{local}}(Z)$. The target velocity is

$$
\dot Z
=
\Pi_{T_Z\mathcal M}F_{\mathrm{local}}(Z).
$$

For smooth equality constraints and a positive-definite state metric $G(Z)$, a candidate expression is

$$
\dot Z
=
F_{​\mathrm{local}}
-
G^{-1}J_{\Gamma}^{\mathsf T}
\left(
J_{\Gamma}G^{-1}J_{\Gamma}^{\mathsf T}
\right)^{\dagger}
J_{\Gamma}F_{\mathrm{local}}.
$$

This expression requires rank, regularity, domain, and numerical-preservation analysis.

## 7. Frozen $M_P$ version 1.0 sandbox

The first projection contract fixes

$$
\Gamma(Z)=c(x)-c_0
=
\frac13x^Tx-c_0=0,
$$

where

$$
c_0=c(x(0))>0,
\qquad
H=\varnothing.
$$

With the Euclidean metric, the frozen projected node derivative is

$$
\boxed{
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The constraint acts only on $x$; $s$ and $q$ retain their $M_0$ proposal equations. This is the Phase 3 implementation target and remains unverified in code.

## 8. Combined mechanism

A combined model must retain separate feedback and projection contributions:

$$
\dot Z
=
F_0(Z)
+
F_F(Z)
+
F_P\bigl(Z,F_0+F_F\bigr).
$$

Removing $F_F$ must recover $M_P$. Removing $F_P$ must recover $M_F$. Removing both must recover $M_0$.

No equivalence

$$
F_F\equiv F_P
$$

is assumed.

For the frozen constant-amplitude sandbox, the radial node feedback satisfies

$$
P_T[-\chi c(x)x]=0,
$$

so version 1.0 predicts

$$
f_{FP}=f_P
$$

for node derivatives, while $s$ and $q$ feedback may still distinguish the models.

## 9. Dynamic topology and metric

A general system may include

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

Whether $c$ is algebraically derived or dynamically independent must be declared separately for each model. In $M_0$ and $M_F$, it is algebraically derived.

## 10. Non-collapse barrier

A target variant may define

$$
U_{\mathrm{barrier}}(Z)
=
\sum_e\frac{B_e}{\ell_e(Z)^{p_e}},
\qquad B_e,p_e>0.
$$

Then

$$
\ell_e\to0^+
\quad\Longrightarrow\quad
U_{\mathrm{barrier}}\to+\infty.
$$

The implication from divergent potential to an unreachable finite-energy boundary remains a proof obligation under explicit energy assumptions. The barrier is not implemented in $M_0$ or $M_F$.

## 11. Equivariance

For an admissible presentation transformation $g$, the target dynamics should satisfy

$$
F(g\cdot Z)=Dg_ZF(Z),
$$

and every invariant observable $Q$ should satisfy

$$
Q(g\cdot Z)=Q(Z).
$$

Permutation equivariance is unit-tested for $M_0$ and $M_F$. General equivariance remains a proof obligation.

## 12. Fail-closed projected claim

The label “projected geometry” is licensed only after explicit constraints, projection implementation, preservation tests, code-equation parity, and substrate-path identification all pass.

At present the constraint definition is frozen, but implementation and verification are absent. Therefore:

$$
\operatorname{PROJECTED\_CLAIM}=\text{UNVERIFIED}.
$$

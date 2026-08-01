# Dynamic Relational Constraint Geometry

## 1. Provisional presentation

Let

$$
\bar G=(V,\bar E)
$$

be a potential undirected graph. The complete state is

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

## 2. Relational mismatch

For $e=(i,j)$, define endpoint maps into a shared comparison space $Y_e$:

$$
\rho_{ie}:M_i\times\Theta_i\times C\to Y_e,
$$

$$
\rho_{je}:M_j\times\Theta_j\times C\to Y_e.
$$

The mismatch is

$$
\delta_e(Z)=\rho_{ie}(x_i,\theta_i,c)-\rho_{je}(x_j,\theta_j,c).
$$

A coherence energy is

$$
\mathcal E_{\mathrm{coh}}(Z)
=
\frac{1}{2}
\sum_{e\in\bar E}
a_e\delta_e^{\mathsf T}W_e\delta_e.
$$

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

## 4. Admissible configurations

Let

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

The local model proposes velocity $F(Z)$. The actual velocity is the admissible component

$$
\dot Z
=
\Pi_{T_{\mathcal M}(Z)}F(Z).
$$

For equality constraints and a positive-definite state metric $G(Z)$,

$$
\dot Z
=
F
-
G^{-1}J_{\Gamma}^{\mathsf T}
\left(
J_{\Gamma}G^{-1}J_{\Gamma}^{\mathsf T}
\right)^{\dagger}
J_{\Gamma}F.
$$

The local system proposes motion. The global geometry removes the incoherent component.

## 5. Dynamic topology and metric

A general system includes

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

## 6. Non-collapse barrier

Define

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

## 7. Equivariance

For an admissible presentation transformation $g$,

$$
F(g\cdot Z)=Dg_ZF(Z),
$$

and every observable $Q$ must satisfy

$$
Q(g\cdot Z)=Q(Z).
$$

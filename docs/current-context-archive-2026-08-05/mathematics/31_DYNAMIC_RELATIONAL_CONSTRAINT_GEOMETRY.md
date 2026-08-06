# Dynamic Relational Constraint Geometry

## 1. Objective

Construct a nonlinear, dynamic geometry that operationalizes:

- genuine local multiplicity;
- dynamic global coherence;
- local dominance under ordinary conditions;
- global exclusion of incoherent motion;
- state-dependent geometry;
- no privileged coordinate presentation.

## 2. Local proposed evolution

Let:

$$
Z=(x,s,q,\theta,c).
$$

The unconstrained local vector field is:

$$
F_{\mathrm{local}}(Z)
=
\begin{pmatrix}
F_x(Z)\\
F_s(Z)\\
F_q(Z)\\
F_\theta(Z)\\
F_c(Z)
\end{pmatrix}.
$$

For node $i$:

$$
\boxed{
F_{x_i}
=
f_i(x_i,\theta_i,c)
+
\sum_{j\in\mathcal N_i}
a_{ij}
K_{ij}(x_i,x_j,q_{ij},c).
}
$$

The direct dependence is local except for explicitly admitted collective variables.

## 3. Global admissibility

Let:

$$
\Gamma(Z)=0
$$

define equality constraints.

At a regular point:

$$
J_\Gamma(Z)
=
\frac{\partial\Gamma}{\partial Z}.
$$

Let $G(Z)$ be a positive-definite metric on presentation space.

The tangent space is:

$$
T_Z\mathcal M
=
\left\{
v:
J_\Gamma(Z)v=0
\right\}.
$$

## 4. Projection

The metric-orthogonal projection of $F$ onto the tangent space is:

$$
\boxed{
\dot Z
=
F
-
G^{-1}J_\Gamma^{\mathsf T}
\left(
J_\Gamma G^{-1}J_\Gamma^{\mathsf T}
\right)^\dagger
J_\Gamma F.
}
$$

Here $\dagger$ denotes a pseudoinverse when required.

Define:

$$
F_{\mathrm{whole}}
=
-
G^{-1}J_\Gamma^{\mathsf T}
\left(
J_\Gamma G^{-1}J_\Gamma^{\mathsf T}
\right)^\dagger
J_\Gamma F.
$$

Then:

$$
\boxed{
\dot Z
=
F_{\mathrm{local}}
+
F_{\mathrm{whole}}.
}
$$

## 5. Interpretation

The local rules propose motion.

The whole is not another object that issues commands. The whole is represented by the geometry of admissible configurations. The projection removes the component normal to that geometry.

Thus:

$$
\boxed{
\text{actual evolution}
=
\text{local proposal}
-
\text{globally incompatible component}.
}
$$

## 6. Constraint preservation

For time-independent equality constraints:

$$
\Gamma(Z)=0,
$$

the projected dynamics satisfy:

$$
\frac{d}{dt}\Gamma(Z)
=
J_\Gamma(Z)\dot Z
=
0
$$

under the regularity assumptions required by the projection.

For time-dependent constraints:

$$
\Gamma(Z,t)=0,
$$

the condition becomes:

$$
J_\Gamma\dot Z
+
\frac{\partial\Gamma}{\partial t}
=
0.
$$

The projection formula must then include the explicit time term.

## 7. Inequalities

For:

$$
H_\beta(Z)\geq0,
$$

the correct object at an active boundary is a tangent cone rather than an ordinary tangent space.

The actual motion should satisfy:

$$
\dot Z\in T_{\mathcal M}(Z).
$$

A projected differential inclusion may be required when active constraints switch.

## 8. Dynamic constraints

Let:

$$
Z=(z,c)
$$

and:

$$
\Gamma(z,c)=0.
$$

Local and collective proposals are:

$$
\dot z^{\mathrm{prop}}=F(z,c),
$$

$$
\dot c^{\mathrm{prop}}
=
R(c,\Psi(z)).
$$

The joint projection preserves the coupled admissibility relation.

This avoids treating $c$ as an external controller.

## 9. Relational geometry

For edge $e$:

$$
\ell_e(Z)
=
\frac{\exp(q_e)}{a_e}
\psi_e(\delta_e).
$$

Distance is:

$$
d_Z(i,j)
=
\inf_{\gamma:i\rightsquigarrow j}
\sum_{e\in\gamma}\ell_e(Z).
$$

The local vector field depends on edge lengths or conductances:

$$
w_e(Z)=\frac{1}{\ell_e(Z)}.
$$

Therefore:

$$
Z
\rightarrow
\ell
\rightarrow
F
\rightarrow
\dot Z
\rightarrow
Z'.
$$

The state generates the next geometry.

## 10. Nonlinearity

Even if the raw local rule is linear, the total dynamics are generally nonlinear because:

$$
a_e=\sigma(s_e),
$$

$$
\ell_e\propto\exp(q_e)\psi_e(\delta_e),
$$

the projection depends on $Z$, and the admissibility manifold may be curved.

## 11. Persistence and memory

The geometry stores history in $s$, $q$, $\theta$, and $c$.

Two systems with identical current $x$ but different relation or metric histories may evolve differently.

This directly supports the claim that state alone does not determine behavior.

## 12. Global coherence functional

A soft alternative to hard projection uses:

$$
\mathcal E_{\mathrm{coh}}(Z)
=
\frac{1}{2}
\sum_e
a_e\delta_e^{\mathsf T}W_e\delta_e.
$$

Gradient dynamics can include:

$$
-\lambda\nabla_Z\mathcal E_{\mathrm{coh}}.
$$

The project must compare hard constraints, penalties, and Lagrange-multiplier formulations rather than assume they are equivalent.

## 13. The one and many in the equations

$$
\boxed{
\begin{aligned}
\text{Many}
&=
F_{\mathrm{local}}(Z),\\
\text{One}
&=
\mathcal M
\text{ and the induced correction},\\
\text{Geometry}
&=
\ell_e(Z),d_Z,\text{ and }G(Z),\\
\text{Computation}
&=
Z\mapsto Z',\\
\text{Memory}
&=
\text{persistent components of }Z.
\end{aligned}
}
$$

## 14. What the equation does not prove

The projection equation does not establish:

- that reality is a graph;
- that global constraints are fundamental;
- that the whole is ontologically prior;
- that local/global duality is unique;
- that the model differs empirically from known constrained adaptive networks;
- that primes generate the graph.

## 15. Canonical equation

$$
\boxed{
\dot Z
=
\underbrace{F_{\mathrm{local}}(Z)}_{\text{many}}
-
\underbrace{
\Pi_{N_Z\mathcal M}
F_{\mathrm{local}}(Z)
}_{\text{whole excludes incoherence}}.
}
$$

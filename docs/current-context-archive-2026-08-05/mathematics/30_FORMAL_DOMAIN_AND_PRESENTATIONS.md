# Formal Domain and Presentations

## 1. Purpose

This document defines the provisional mathematical objects used by Dynamic Relational Constraint Geometry. None is ontologically privileged.

## 2. Potential relational support

Let:

$$
\bar G=(V,\bar E)
$$

be a potential graph.

- $V$ is a finite or countable collection of provisional local sites.
- $\bar E$ contains every relation permitted to become active in the chosen model.

A model may later generalize to hypergraphs, simplicial complexes, sheaves, categories, or continuous spaces. The initial graph is chosen for tractability, not ontological priority.

## 3. Local state spaces

For each node $i\in V$, let:

$$
x_i(t)\in M_i,
$$

where $M_i$ is a smooth manifold, vector space, discrete state space, or other specified local domain.

The aggregate local state is:

$$
x(t)=\prod_{i\in V}x_i(t).
$$

When all $M_i=\mathbb R^d$:

$$
x(t)\in\mathbb R^{N d}.
$$

## 4. Relation variables

For each potential edge $e\in\bar E$, introduce:

$$
s_e(t)\in\mathbb R.
$$

The active strength is:

$$
a_e(t)=\sigma(s_e(t))
=
\frac{1}{1+\exp(-s_e(t))}.
$$

This gives:

$$
0<a_e<1.
$$

A hard-topology model may use:

$$
a_e\in\{0,1\}.
$$

The soft version is preferable for differentiability.

## 5. Metric deformation variables

For each edge:

$$
q_e(t)\in\mathbb R.
$$

The factor:

$$
m_e(t)=\exp(q_e(t))
$$

is strictly positive and can expand or contract intrinsic edge length.

## 6. Local rule variables

Each node may have adaptive parameters:

$$
\theta_i(t)\in\Theta_i.
$$

The local rule is:

$$
f_i:
M_i\times
\prod_{j\in\mathcal N_i}M_j
\times\Theta_i\times C
\to
T_{x_i}M_i.
$$

Rule adaptation is optional. Fixed-rule models set $\dot\theta_i=0$.

## 7. Collective variables

Let:

$$
c(t)\in C
$$

represent collective observables, modes, or constraint parameters.

The whole is not identified with $c$ alone. The whole is represented by the jointly admissible relation:

$$
\Gamma(z,c)=0,
$$

where:

$$
z=(x,s,q,\theta).
$$

## 8. Complete provisional state

The working state is:

$$
\boxed{
Z(t)
=
\bigl(x(t),s(t),q(t),\theta(t),c(t)\bigr).
}
$$

This is a coordinate presentation.

## 9. Relational comparison maps

For edge $e=(i,j)$, introduce a comparison space $Y_e$ and maps:

$$
\rho_{ie}:M_i\times\Theta_i\times C\to Y_e,
$$

$$
\rho_{je}:M_j\times\Theta_j\times C\to Y_e.
$$

Define mismatch:

$$
\boxed{
\delta_e(Z)
=
\rho_{ie}(x_i,\theta_i,c)
-
\rho_{je}(x_j,\theta_j,c).
}
$$

When $Y_e$ is not a vector space, replace subtraction with a suitable discrepancy map.

## 10. Coherence functional

Let $W_e$ be positive semidefinite. Define:

$$
\boxed{
\mathcal E_{\mathrm{coh}}(Z)
=
\frac{1}{2}
\sum_{e\in\bar E}
a_e
\delta_e^{\mathsf T}W_e\delta_e.
}
$$

This measures relation-weighted mismatch. It is not necessarily physical energy.

## 11. Admissibility

Let equality constraints be:

$$
\Gamma_\alpha(Z)=0.
$$

Let inequality constraints be:

$$
H_\beta(Z)\geq0.
$$

The admissible set is:

$$
\boxed{
\mathcal M
=
\left\{
Z:
\Gamma_\alpha(Z)=0,\;
H_\beta(Z)\geq0
\right\}.
}
$$

When constraints depend explicitly on time:

$$
\mathcal M_t
=
\left\{
Z:
\Gamma_\alpha(Z,t)=0,\;
H_\beta(Z,t)\geq0
\right\}.
$$

## 12. Proposed dynamics

An unconstrained vector field proposes motion:

$$
F(Z,t)\in T_Z\mathcal P,
$$

where $\mathcal P$ is the presentation space.

Actual motion is restricted to the tangent cone:

$$
\boxed{
\dot Z
=
\Pi_{T_{\mathcal M_t}(Z)}F(Z,t).
}
$$

For smooth equality constraints and regular points, the tangent cone reduces to the tangent space.

## 13. Presentation transformations

Let $\mathcal G$ be a group or groupoid of admissible transformations.

A transformation:

$$
g:Z\mapsto g\cdot Z
$$

may represent:

- node relabeling;
- coordinate change;
- gauge transformation;
- equivalent parameterization;
- observationally irrelevant redundancy.

Dynamics should be equivariant:

$$
F(g\cdot Z)
=
Dg_ZF(Z).
$$

Observables should be invariant:

$$
Q(g\cdot Z)=Q(Z).
$$

## 14. Observational equivalence

For a family of admissible observations $\mathscr O$, define:

$$
Z\sim_{\mathscr O}Z'
$$

if:

$$
O(Z)=O(Z')
$$

for every:

$$
O\in\mathscr O.
$$

The equivalence class is a useful structural construction, not underlying reality.

A richer observation family may refine equivalence:

$$
\mathscr O\subseteq\mathscr O'
\quad\Rightarrow\quad
[Z]_{\mathscr O'}
\subseteq
[Z]_{\mathscr O}.
$$

## 15. Source of nonlinearity

Nonlinearity can arise from:

- nonlinear $f_i$;
- nonlinear comparison maps $\rho_{ie}$;
- sigmoid edge activation;
- exponential metric deformation;
- state-dependent constraints;
- projection onto a curved manifold;
- topology-state feedback;
- adaptive rules.

## 16. Source of memory

Memory may reside in:

- persistent state $x$;
- relation state $s$;
- metric state $q$;
- adaptive parameters $\theta$;
- collective state $c$;
- explicit history variables $M$.

## 17. Formal caution

The tuple $Z$ is a chosen formal domain. The apophatic schema prohibits:

$$
Z=\text{reality itself}.
$$

The valid claim is:

$$
Z
\text{ is one candidate presentation of selected relational observables}.
$$

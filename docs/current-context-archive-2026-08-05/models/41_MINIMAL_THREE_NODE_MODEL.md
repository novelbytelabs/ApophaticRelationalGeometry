# Minimal Three-Node Model

## 1. Objective

Construct the smallest nontrivial system that contains:

- local nonlinear state;
- neighborhood coupling;
- dynamic edges;
- dynamic metric deformation;
- a collective variable;
- global admissibility;
- intrinsic path geometry.

Three nodes are chosen because two nodes cannot exhibit nontrivial alternative paths or triangle-level relational structure.

## 2. State

For:

$$
i\in\{1,2,3\},
$$

let:

$$
x_i\in\mathbb R.
$$

For each undirected edge $(i,j)$, let:

$$
s_{ij}=s_{ji},
$$

$$
q_{ij}=q_{ji}.
$$

Let:

$$
c\in\mathbb R.
$$

The state is:

$$
Z=
(x_1,x_2,x_3,s_{12},s_{23},s_{31},q_{12},q_{23},q_{31},c).
$$

## 3. Collective mode

Define:

$$
\boxed{
c
=
\frac{1}{3}
\sum_{i=1}^{3}x_i^2.
}
$$

The constraint is:

$$
\boxed{
\Gamma(x,c)
=
c-\frac{1}{3}
\sum_i x_i^2
=
0.
}
$$

This $c$ is a simple collective amplitude, not “the whole” itself.

## 4. Edge activation

$$
a_{ij}
=
\sigma(s_{ij})
=
\frac{1}{1+\exp(-s_{ij})}.
$$

## 5. Intrinsic length

$$
\boxed{
\ell_{ij}
=
\frac{\exp(q_{ij})}{a_{ij}}
\sqrt{\epsilon^2+(x_i-x_j)^2}.
}
$$

Conductance:

$$
w_{ij}
=
\frac{1}{\ell_{ij}}.
$$

## 6. Local nonlinear proposal

$$
\boxed{
\dot x_i^{\mathrm{prop}}
=
\alpha x_i
-
\beta x_i^3
+
\sum_{j\neq i}
w_{ij}(x_j-x_i)
-
\chi c x_i.
}
$$

Interpretation:

- $\alpha x_i-\beta x_i^3$ gives local nonlinear growth and saturation;
- the coupling term aligns or diffuses neighboring states;
- $-\chi c x_i$ supplies collective feedback.

The sign and parameter ranges are assumptions.

## 7. Relation dynamics

$$
\boxed{
\tau_s\dot s_{ij}
=
\eta_0
-
\eta_1(x_i-x_j)^2
+
\eta_2c
-
s_{ij}.
}
$$

This provisional rule strengthens compatible edges and relaxes $s_{ij}$.

## 8. Metric dynamics

$$
\boxed{
\tau_q\dot q_{ij}
=
-\gamma q_{ij}
+
\kappa(x_i-x_j)^2
-
\rho c.
}
$$

This allows mismatch and collective state to deform distance.

## 9. Constraint-compatible collective evolution

If $c$ is treated as a derived variable, compute it directly from $x$ and do not integrate a separate equation.

If $c$ is integrated independently, preserve:

$$
\Gamma(x,c)=0.
$$

Differentiating:

$$
\dot c
=
\frac{2}{3}
\sum_i x_i\dot x_i.
$$

This is the exact compatible derivative.

## 10. Projection alternative

Let the raw proposal include an independent $\dot c^{\mathrm{prop}}$.

With Euclidean state-space metric, project the joint vector:

$$
F=
(\dot x_1^{\mathrm{prop}},
\dot x_2^{\mathrm{prop}},
\dot x_3^{\mathrm{prop}},
\dot c^{\mathrm{prop}})
$$

onto the tangent space of $\Gamma=0$.

The constraint gradient is:

$$
\nabla\Gamma
=
\left(
-\frac{2x_1}{3},
-\frac{2x_2}{3},
-\frac{2x_3}{3},
1
\right).
$$

The projection is:

$$
\dot Z
=
F
-
\frac{
\nabla\Gamma\cdot F
}{
\|\nabla\Gamma\|^2
}
\nabla\Gamma.
$$

This gives an exactly testable implementation.

## 11. Path distances

Direct distance:

$$
d(1,2)
=
\min
\left\{
\ell_{12},
\ell_{13}+\ell_{32}
\right\}.
$$

Similarly for the other pairs.

This permits a relation to become effectively closer through an indirect path.

## 12. Optional barrier

$$
U_{\mathrm{barrier}}
=
\sum_{i<j}
\frac{B_{ij}}{\ell_{ij}^{p_{ij}}}.
$$

A gradient or Hamiltonian version can be introduced only after specifying whether the model is dissipative, conservative, or mixed.

## 13. Persistence definition for the prototype

One provisional viability condition is:

$$
|x_i|\leq X_{\max},
$$

$$
\ell_{ij}\in[\ell_{\min},\ell_{\max}],
$$

$$
\mathcal E_{\mathrm{coh}}\leq E_{\max}.
$$

Persistence duration is the first exit time from the viability set.

The thresholds must be preregistered or sensitivity-tested.

## 14. Required baselines

1. Fixed $s,q$, no collective term.
2. Fixed $s,q$, collective term.
3. Dynamic $s$, fixed $q$.
4. Fixed $s$, dynamic $q$.
5. Dynamic $s,q$, no projection.
6. Full model.
7. State-permuted alignment.
8. Edge-permuted structure.
9. Matched random parameters.

## 15. Initial analysis

Before simulation, analyze:

- equilibria;
- linear stability;
- symmetry under node permutation;
- boundedness conditions;
- singularities;
- timescale separation;
- parameter identifiability.

## 16. Prototype claim

The model is not a model of objective reality. It is the smallest test of whether:

$$
\boxed{
\text{local nonlinear motion}
+
\text{dynamic relational geometry}
+
\text{global admissibility}
}
$$

produces robust behavior not present in simpler baselines.

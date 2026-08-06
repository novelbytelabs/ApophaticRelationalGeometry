# Proof Obligations

## 1. Purpose

No simulation result should be interpreted before the mathematical object is shown to be well-defined under stated assumptions.

## 2. Domain and regularity

Specify:

- state-space domain;
- parameter domain;
- differentiability class;
- bounded or unbounded variables;
- allowed graph changes;
- active constraint regularity.

Prove or assume explicitly that vector fields are locally Lipschitz where existence and uniqueness are claimed.

## 3. Edge-length positivity

For:

$$
\ell_e
=
\frac{\exp(q_e)}{a_e}
\psi_e(\delta_e),
$$

show:

$$
\ell_e>0.
$$

With sigmoid activation and $\psi_e\geq\epsilon>0$, positivity follows for finite $s_e,q_e$.

## 4. Metric validity

For finite connected undirected graphs with symmetric positive edge lengths, prove that shortest-path distance satisfies:

1. non-negativity;
2. identity of indiscernibles;
3. symmetry;
4. triangle inequality.

State exceptions:

- disconnected graph gives extended metric;
- directed graph may give quasi-metric;
- zero-length edges produce pseudometric.

## 5. Constraint preservation

For smooth equality constraints:

$$
\Gamma(Z)=0,
$$

verify:

$$
J_\Gamma\dot Z=0.
$$

For time-dependent constraints verify:

$$
J_\Gamma\dot Z+\partial_t\Gamma=0.
$$

For numerical integration, measure drift and use a projection or constraint-preserving integrator.

## 6. Projection well-definedness

Study:

$$
J_\Gamma G^{-1}J_\Gamma^{\mathsf T}.
$$

Require rank conditions or define pseudoinverse behavior.

Identify singular configurations where the constraint manifold is not regular.

## 7. Inequality constraints

For active inequalities, formulate a tangent cone or complementarity problem.

Prove existence of projected solutions or state the differential-inclusion theorem used.

## 8. Local existence and uniqueness

For smooth fixed topology, establish local existence and uniqueness.

For switching topology or nonsmooth projection, determine whether solutions are:

- classical;
- Carathéodory;
- Filippov;
- set-valued.

## 9. Global existence or blow-up

Determine whether trajectories remain bounded.

Analyze:

- cubic local terms;
- exponential metric factors;
- sigmoid saturation;
- barrier gradients;
- constraint singularities.

## 10. Non-collapse

If a barrier is used, prove:

$$
\inf_t\ell_e(t)>0
$$

under finite-energy assumptions.

A proof must exclude cancellation by unbounded negative energy terms.

## 11. Energy or Lyapunov structure

If $\mathcal E$ is called energy, show conservation or a physical derivation.

If it is a Lyapunov function, show:

$$
\frac{d\mathcal E}{dt}\leq0.
$$

Otherwise call it a score or functional.

## 12. Symmetry and equivariance

Prove:

$$
F(\pi\cdot Z)=\pi\cdot F(Z)
$$

for node permutations when parameters transform consistently.

Prove corresponding invariance of observables.

## 13. Locality

Compute Jacobian blocks:

$$
\frac{\partial F_i}{\partial x_j}.
$$

Direct local coupling should vanish for:

$$
j\notin\mathcal N_i,
$$

except through explicitly identified collective variables or constraint projection.

## 14. Nontrivial global influence

Show that:

$$
F_{\mathrm{whole}}\neq0
$$

on a nonempty set.

Show that the effect is not algebraically equivalent to a reparameterized local coupling in the tested regime.

## 15. Structure–state identifiability

Define compatibility $\kappa(B,x)$.

Show it is not reducible to:

- state norm;
- graph degree;
- edge count;
- spectral gap alone;
- initial energy alone.

## 16. Timescale limits

Analyze:

$$
\tau_s\to0,
\quad
\tau_s\to\infty,
\quad
\tau_q\to0,
\quad
\tau_q\to\infty.
$$

These limits may reduce the model to known fixed or slaved systems.

## 17. Three-node equilibria

Solve or characterize:

$$
\dot x_i=0,
\qquad
\dot s_{ij}=0,
\qquad
\dot q_{ij}=0.
$$

Include symmetric equilibria:

$$
x_1=x_2=x_3.
$$

Test symmetry-breaking branches.

## 18. Numerical convergence

Demonstrate:

- timestep convergence;
- solver agreement;
- constraint error convergence;
- stable handling of barriers;
- deterministic reproducibility.

## 19. Status tracking

Every obligation should carry one status:

- open;
- assumed;
- proved;
- proved under conditions;
- numerically verified only;
- failed;
- superseded.

## 20. Gate

No claim of new geometry should proceed until obligations 3, 4, 5, 6, 8, 12, and 18 are satisfied for the minimal model.

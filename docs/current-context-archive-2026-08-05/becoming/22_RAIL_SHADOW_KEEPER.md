# RAIL, SHADOW, KEEPER, and Delta

## Status

These terms arose as an operational metaphor for self-correcting persistence. They must be translated into explicit variables before they are treated as a mechanism.

## 1. RAIL

RAIL denotes the corridor in which computation or evolution is simplest, viable, low-error, or dynamically stable.

A mathematical representation could be:

$$
\mathcal R
=
\{Q:\mathcal L(Q)\leq\tau_{\mathcal R}\},
$$

where $\mathcal L$ is an error, energy, inconsistency, or description-length functional.

Being “on the RAIL” means:

$$
Q_t\in\mathcal R.
$$

The project must specify which definition is used. Simplicity, optimality, stability, and viability are not automatically equivalent.

## 2. SHADOW

SHADOW denotes residual information generated when the current trajectory deviates from the RAIL.

Let the proposed prediction be:

$$
\widehat Q_{t+1}
=
F(Q_t).
$$

Let the realized or admissible next condition be $Q_{t+1}$. A residual is:

$$
e_t
=
Q_{t+1}-\widehat Q_{t+1},
$$

when subtraction is defined.

A memory-bearing SHADOW may be:

$$
S_{t+1}
=
\lambda S_t+\phi(e_t),
$$

where $\phi$ extracts structured residual information.

The conversation emphasized that errors can accumulate structure and become useful correction signals.

## 3. KEEPER

KEEPER is the policy that converts SHADOW into corrective action.

A generic form is:

$$
\Delta_t
=
K(Q_t,S_t,C_t).
$$

Then:

$$
Q_{t+1}
=
\mathcal U(Q_t,\Delta_t).
$$

The KEEPER may be:

- a controller;
- an optimizer;
- a projection onto constraints;
- an error-correcting rule;
- a learned policy;
- a selection mechanism.

No single interpretation has been fixed.

## 4. Delta

Delta is the correction applied to preserve or improve the trajectory.

The stronger “least information” version can be formulated as:

$$
\Delta_t^\ast
=
\arg\min_{\Delta}
\operatorname{Cost}(\Delta)
$$

subject to:

$$
\mathcal U(Q_t,\Delta)
\in
\mathcal V.
$$

This is a concrete research direction.

## 5. Shadow collapse

The conversation said the SHADOW “collapses” when computation is on the perfect RAIL.

A precise version is:

$$
Q_t\in\mathcal R
\quad\Rightarrow\quad
e_t=0
$$

and, under decay:

$$
S_{t+k}\to0.
$$

This need not mean information is physically destroyed. It means the corrective residual becomes unnecessary under the chosen error model.

## 6. Relation to projected dynamics

In Dynamic Relational Constraint Geometry:

$$
F_{\mathrm{local}}
$$

proposes motion, while:

$$
-\Pi_{N_Z\mathcal M}F_{\mathrm{local}}
$$

removes the incoherent component.

This correction can function as a mathematically explicit KEEPER:

$$
\Delta_{\mathrm{whole}}
=
-\Pi_{N_Z\mathcal M}F_{\mathrm{local}}.
$$

The normal component is a candidate SHADOW:

$$
S
=
\Pi_{N_Z\mathcal M}F_{\mathrm{local}}.
$$

The tangent admissible trajectory is the RAIL:

$$
T_Z\mathcal M.
$$

This mapping is promising but remains provisional.

## 7. Required disambiguations

Before implementation, choose exactly one meaning for each:

- RAIL: viability manifold, attractor, geodesic, optimum, or low-complexity path;
- SHADOW: residual, normal force, prediction error, latent memory, or accumulated defect;
- KEEPER: projection, controller, optimizer, or learned rule;
- delta: additive update, transformation, or compressed instruction.

## 8. Testable proposition

A viable first test is:

$$
\boxed{
\text{structured residual feedback increases persistence under
perturbation compared with memoryless correction}.
}
$$

This can be tested independently of metaphysical claims.

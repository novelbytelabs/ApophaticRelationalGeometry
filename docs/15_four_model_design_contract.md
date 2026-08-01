# Four-Model Design Contract

**Status:** Phase 1 draft, version 0.1. Not frozen for confirmatory experimentation.

## Purpose

This contract defines the first directly comparable ARG model family:

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

The design is intentionally minimal. Its purpose is to separate endogenous collective feedback from explicit global-admissibility projection while holding the local adaptive substrate fixed.

## Shared graph and state

All four models use the complete undirected graph on three nodes with edge order

$$
E=((0,1),(0,2),(1,2)).
$$

The state is

$$
Z=(x,s,q)\in\mathbb R^9,
$$

where

$$
x=(x_1,x_2,x_3),
\qquad
s=(s_{01},s_{02},s_{12}),
\qquad
q=(q_{01},q_{02},q_{12}).
$$

Edge activation and conductance are

$$
a_{ij}=\sigma(s_{ij}),
$$

$$
w_{ij}=a_{ij}e^{-q_{ij}}.
$$

The shared collective diagnostic is

$$
c(x)=\frac13\sum_{i=1}^{3}x_i^2.
$$

In $M_0$ and $M_P$, $c(x)$ is a diagnostic or constraint function only; it does not enter the proposal equations as feedback.

## Shared parameters

All models use the same parameter namespace:

$$
\alpha,\beta,\chi,
\tau_s,\eta_0,\eta_1,\eta_2,
\tau_q,\gamma,\kappa,\rho,
\epsilon.
$$

Feedback parameters $\chi,\eta_2,\rho$ are inactive in $M_0$ and $M_P$.

The projection target $c_0$ is derived from the initial state and is not a fitted parameter:

$$
c_0=c(x(0)).
$$

## Shared intrinsic geometry

For edge $(i,j)$,

$$
\ell_{ij}(Z)
=
\frac{e^{q_{ij}}}{\sigma(s_{ij})}
\sqrt{\epsilon^2+(x_i-x_j)^2}.
$$

The intrinsic node distance is the shortest-path distance induced by these positive edge lengths.

This geometry is diagnostic in the first four-model comparison. It does not itself define the v0.1 projection constraint.

---

# $M_0$: Local/adaptive substrate baseline

## Definition

$M_0$ contains local nonlinear dynamics, neighborhood coupling, adaptive edge activation, and metric deformation, but no collective feedback and no admissibility projection.

For node $i$:

$$
\dot x_i^{(0)}
=
\alpha x_i
-
\beta x_i^3
+
\sum_{j\ne i}w_{ij}(x_j-x_i).
$$

For edge $(i,j)$:

$$
\tau_s\dot s_{ij}^{(0)}
=
\eta_0
-
\eta_1(x_i-x_j)^2
-
s_{ij},
$$

$$
\tau_q\dot q_{ij}^{(0)}
=
-\gamma q_{ij}
+
\kappa(x_i-x_j)^2.
$$

Define the complete proposal vector

$$
F_0(Z)
=
\left(
\dot x^{(0)},
\dot s^{(0)},
\dot q^{(0)}
\right).
$$

## Required invariant

No value computed from $c(x)$ may enter an $M_0$ transition equation.

Computing $c(x)$ for logging is permitted, but the dependency audit must prove

$$
\frac{\partial F_0}{\partial c}=0
$$

in the implementation graph.

---

# $M_F$: Endogenous collective-feedback prototype

## Definition

$M_F$ is the current executable model.

The feedback vector is

$$
F_F(Z)
=
\left(
-\chi c(x)x,
\frac{\eta_2c(x)}{\tau_s}\mathbf 1_3,
-\frac{\rho c(x)}{\tau_q}\mathbf 1_3
\right).
$$

Therefore

$$
\dot Z_F
=
F_0(Z)+F_F(Z).
$$

Expanded node equation:

$$
\dot x_i^{(F)}
=
\alpha x_i
-
\beta x_i^3
+
\sum_{j\ne i}w_{ij}(x_j-x_i)
-
\chi c(x)x_i.
$$

Expanded edge and metric equations:

$$
\tau_s\dot s_{ij}^{(F)}
=
\eta_0
-
\eta_1(x_i-x_j)^2
+
\eta_2c(x)
-
s_{ij},
$$

$$
\tau_q\dot q_{ij}^{(F)}
=
-\gamma q_{ij}
+
\kappa(x_i-x_j)^2
-
\rho c(x).
$$

## Exact reduction

Setting

$$
\chi=\eta_2=\rho=0
$$

must recover $M_0$ exactly.

## Licensed claim

$M_F$ implements prototype-level downward feedback/constraint through

$$
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

It does not yet establish macro-level causal autonomy.

---

# $M_P$: Constant-amplitude projected-admissibility prototype

## Design rationale

The first projection prototype should be explicit, state-dimension matched, analytically tractable, and directly comparable with the radial node-feedback term in $M_F$.

The v0.1 candidate therefore constrains the collective amplitude:

$$
\Gamma(Z)
=
c(x)-c_0
=
\frac13x^Tx-c_0
=0,
$$

where

$$
c_0=c(x(0))>0.
$$

There are no inequality constraints in v0.1:

$$
H=\varnothing.
$$

The admissible manifold is

$$
\mathcal M_{c_0}
=
\left\{Z:\frac13x^Tx=c_0\right\}.
$$

The constraint acts only on $x$. The adaptive variables $s$ and $q$ retain their $M_0$ proposal equations.

## Constraint Jacobian

In the full state order $(x,s,q)$,

$$
J_\Gamma(Z)
=
\left(
\frac23x^T,
0_{1\times3},
0_{1\times3}
\right).
$$

For $c_0>0$, the manifold excludes $x=0$, so

$$
J_\Gamma J_\Gamma^T
=
\frac49x^Tx
=
\frac43c_0
>0.
$$

The rank-one projection is therefore well defined on the declared manifold.

## State-space metric

Version 0.1 uses the Euclidean metric on the complete state:

$$
G=I_9.
$$

Because $\Gamma$ depends only on $x$, the projection changes only the node-state derivative.

## Continuous-time projection

Let

$$
f_0(Z)=\dot x^{(0)}
$$

be the node part of $F_0$.

The projected node derivative is

$$
f_P
=
f_0
-
J_x^T(J_xJ_x^T)^{-1}J_xf_0,
$$

where

$$
J_x=\frac23x^T.
$$

Equivalently,

$$
\boxed{
f_P
=
f_0
-
x\frac{x^Tf_0}{x^Tx}.
}
$$

The complete $M_P$ dynamics are

$$
\dot Z_P
=
\left(
f_P,
\dot s^{(0)},
\dot q^{(0)}
\right).
$$

## Tangency condition

$$
\frac{d}{dt}\Gamma(Z(t))
=
\frac23x^Tf_P
=0.
$$

This proves continuous-time preservation provided the solution remains in the declared regular domain.

## Singular policy

- Require $c_0>0$.
- Reject an initial condition with $x=0$.
- Fail closed if numerical state norm falls below a declared threshold.
- Do not silently replace the inverse with an arbitrary correction at rank loss.

## Numerical preservation contract

A derivative-level projection alone does not make an arbitrary discrete integrator preserve a curved manifold exactly.

The first implementation must use one of:

1. a constraint-preserving integrator;
2. a post-step retraction;
3. both, with the retraction magnitude recorded.

The reference retraction candidate is

$$
x^+
\leftarrow
\sqrt{3c_0}\frac{x^+}{\|x^+\|},
$$

valid when $\|x^+\|>0$.

The exact numerical method is not frozen by this draft.

---

# $M_{FP}$: Feedback followed by projection

## Ordering convention

Version 0.1 proposes feedback first and projection second:

$$
F_{\mathrm{proposal}}
=
F_0+F_F,
$$

$$
\dot Z_{FP}
=
\Pi_{T_Z\mathcal M_{c_0}}
F_{\mathrm{proposal}}.
$$

Because the constraint depends only on $x$, the node derivative is

$$
f_{FP}
=
P_T\left(f_0-\chi c(x)x\right),
$$

where

$$
P_T
=
I_3-\frac{xx^T}{x^Tx}.
$$

The edge and metric derivatives retain their $M_F$ feedback terms.

## Important exact consequence

Since

$$
P_Tx=0,
$$

the radial node-feedback term is annihilated:

$$
P_T\left(-\chi c(x)x\right)=0.
$$

Therefore, under the v0.1 sphere constraint and project-after-feedback ordering,

$$
\boxed{
f_{FP}=f_P.
}
$$

This equality applies only to the node-state derivative. In general,

$$
\dot s^{(FP)}\ne\dot s^{(P)},
\qquad
\dot q^{(FP)}\ne\dot q^{(P)},
$$

because $M_{FP}$ retains the $\eta_2c(x)$ and $-\rho c(x)$ feedback terms in $s$ and $q$.

This is a preregistered structural prediction, not a post hoc interpretation.

## Exact reductions

The implementation must satisfy:

- $M_{FP}$ with projection disabled equals $M_F$;
- $M_{FP}$ with $\chi=\eta_2=\rho=0$ equals $M_P$;
- disabling projection and setting $\chi=\eta_2=\rho=0$ equals $M_0$.

---

# Mechanism diagnostics

## Feedback vector

Record

$$
F_F(Z)
$$

before projection.

## Projection correction

For proposal $F_*$, record

$$
F_P(Z;F_*)
=
\Pi_{T_Z\mathcal M}F_*-F_*.
$$

## Feedback ratio

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

## Projection ratio

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)+F_{F,i}(t)\|+\epsilon}.
$$

## Constraint residual

$$
\epsilon_\Gamma(t)
=
|c(x(t))-c_0|.
$$

## Retraction magnitude

For numerical retraction, record

$$
r(t_n)
=
\|x_n^{\mathrm{retracted}}-x_n^{\mathrm{raw}}\|.
$$

---

# Fairness contract

- All models use the same graph, local parameters, initial $x,s,q$, and observation schedule.
- $c_0$ is derived from the shared initial condition.
- Projection adds no fitted parameter in v0.1.
- Feedback parameters are fit or selected only for $M_F$ and $M_{FP}$, with parameter-count differences reported.
- The same integration accuracy targets apply to all models.
- $M_P$ and $M_{FP}$ must report projection condition numbers and retraction magnitudes.
- $M_0$ must not contain hidden collective paths.
- Model labels are attached to raw outputs and configuration hashes.

# Required unit tests before freeze

## $M_0$

- exact no-feedback equations;
- no dependency from $c$ into transitions;
- reduction from $M_F$ at zero feedback coefficients.

## $M_F$

- existing five tests;
- direct known-answer test for all three feedback paths;
- mutation tests that fail when each feedback path is removed or sign-flipped.

## $M_P$

- known-answer projection on a hand-computed state;
- $x^Tf_P=0$ within tolerance;
- continuous-time constraint derivative equals zero;
- fail-closed zero-norm test;
- permutation equivariance;
- retraction restores $c(x)=c_0$;
- convergence under step refinement.

## $M_{FP}$

- exact reductions to $M_0,M_F,M_P$;
- node radial-feedback annihilation test;
- retained $s/q$ feedback test;
- separate feedback and projection diagnostics.

# Open design decisions before version 1.0 freeze

1. Select the reference integration method and tolerance policy.
2. Decide whether post-step retraction is mandatory or only a reference control.
3. Define the near-singular norm threshold.
4. Decide whether $M_P$ projects only $x$ permanently or whether later versions introduce constraints involving $s$ and $q$.
5. Decide whether a second projection prototype with a dynamic or state-dependent target is required.
6. Define the initial-condition family with $c_0>0$.
7. Define parameter ranges and boundedness checks.
8. Specify the independent implementation language or module boundary.
9. Freeze observation maps for full-state and partial-state equivalence tests.
10. Decide whether the soft-penalty control belongs in the first comparative experiment.

# Draft acceptance decision

Version 0.1 is accepted as the starting mathematical design only if review confirms that:

- $M_0$ is a true no-feedback baseline;
- $M_F$ exactly matches the existing executable;
- $M_P$ is a genuine explicit projection and not feedback relabeled;
- $M_{FP}$ retains mechanism separability;
- the sphere constraint is scientifically modest and presented as a mechanism test, not a law of reality;
- the exact radial-annihilation consequence is understood before implementation.

Until this contract is frozen and implemented:

$$
M_P=M_{FP}=\text{UNVERIFIED}.
$$

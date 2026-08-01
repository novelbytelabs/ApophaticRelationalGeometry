# Four-Model Design Contract

**Status:** Frozen for implementation, version 1.0.

**Scientific status:** This contract freezes definitions and numerical policies. It does not establish that $M_P$ or $M_{FP}$ is implemented, validated, physically adequate, or equivalent to $M_F$.

## Purpose

This contract defines the first directly comparable ARG model family:

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

Its purpose is to separate endogenous collective feedback from explicit global-admissibility projection while holding the local adaptive substrate fixed.

The constant-amplitude manifold used in version 1.0 is a deliberately minimal projection-mechanism sandbox. It is not presented as the completed relational-admissibility geometry of ARG.

## Binding claim ceiling

Until implementation and verification gates pass:

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

---

# 1. Shared substrate

## 1.1 Graph and state

All four models use the complete undirected graph on three nodes with fixed edge order

$$
E=((0,1),(0,2),(1,2)).
$$

The dynamical state is

$$
Z=(x,s,q)\in\mathbb R^9,
$$

with

$$
x=(x_0,x_1,x_2),
\qquad
s=(s_{01},s_{02},s_{12}),
\qquad
q=(q_{01},q_{02},q_{12}).
$$

The collective statistic is

$$
c(x)=\frac13x^Tx.
$$

In $M_0$ and $M_P$, $c(x)$ may be computed for diagnostics or constraint evaluation but may not enter the proposal equations as feedback.

## 1.2 Edge activation and conductance

For edge $(i,j)$,

$$
a_{ij}=\sigma(s_{ij})
=\frac{1}{1+e^{-s_{ij}}},
$$

$$
w_{ij}=a_{ij}e^{-q_{ij}}.
$$

## 1.3 Intrinsic geometry

For edge $(i,j)$,

$$
\ell_{ij}(Z)
=
\frac{e^{q_{ij}}}{\sigma(s_{ij})}
\sqrt{\epsilon^2+(x_i-x_j)^2}.
$$

The intrinsic distance $d_Z(i,j)$ is the shortest-path distance induced by these positive edge lengths.

In the first four-model comparison, this geometry is an observable. It does not define the version 1.0 projection constraint.

## 1.4 Fixed reference parameter set

The first implementation and software-verification slice uses the existing defaults without fitting:

$$
\begin{aligned}
\alpha&=1.0,&\beta&=1.0,&\chi&=0.35,\\
\tau_s&=1.0,&\eta_0&=0.25,&\eta_1&=1.0,&\eta_2&=0.2,\\
\tau_q&=1.0,&\gamma&=0.8,&\kappa&=0.4,&\rho&=0.15,\\
\epsilon&=10^{-6}.&&
\end{aligned}
$$

No parameter sweep is licensed by this contract. Any exploratory or confirmatory range must be frozen in a later experiment protocol.

Implementation validation requires all parameters to be finite and

$$
\beta,\tau_s,\eta_1,\tau_q,\gamma,\epsilon>0,
$$

$$
\chi,\eta_0,\eta_2,\kappa,\rho\geq0.
$$

---

# 2. $M_0$: local/adaptive substrate baseline

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

Define

$$
F_0(Z)
=
\left(
\dot x^{(0)},
\dot s^{(0)},
\dot q^{(0)}
\right).
$$

## $M_0$ dependency invariant

No value computed from $c(x)$ may enter an $M_0$ transition equation.

Logging $c(x)$ is allowed. Transition dependence is not.

---

# 3. $M_F$: endogenous collective feedback

$M_F$ is the current executable prototype.

Define the feedback vector

$$
F_F(Z)
=
\left(
-\chi c(x)x,
\frac{\eta_2c(x)}{\tau_s}\mathbf 1_3,
-\frac{\rho c(x)}{\tau_q}\mathbf 1_3
\right).
$$

Then

$$
\dot Z_F=F_0(Z)+F_F(Z).
$$

Expanded equations are

$$
\dot x_i^{(F)}
=
\alpha x_i
-
\beta x_i^3
+
\sum_{j\ne i}w_{ij}(x_j-x_i)
-
\chi c(x)x_i,
$$

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

## Licensed description

$M_F$ implements prototype-level downward feedback/constraint through

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

It does not establish macro-level causal autonomy, transport, counterfactual adequacy, or alternative-model defeat.

---

# 4. $M_P$: projected admissibility

## 4.1 Constraint

Version 1.0 constrains collective node amplitude:

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

There are no inequality constraints in version 1.0:

$$
H=\varnothing.
$$

The admissible manifold is

$$
\mathcal M_{c_0}
=
\left\{Z:\frac13x^Tx=c_0\right\}.
$$

The constraint acts only on $x$. The $s$ and $q$ proposal equations are those of $M_0$.

## 4.2 Constraint Jacobian and regularity

In full state order $(x,s,q)$,

$$
J_\Gamma(Z)
=
\left(
\frac23x^T,
0_{1\times3},
0_{1\times3}
\right).
$$

On the declared manifold,

$$
J_\Gamma J_\Gamma^T
=
\frac49x^Tx
=
\frac43c_0>0.
$$

Thus the rank-one projection is regular whenever $c_0>0$.

## 4.3 State-space metric

Version 1.0 uses the Euclidean metric

$$
G=I_9.
$$

Because $\Gamma$ depends only on $x$, projection changes only the node-state derivative.

## 4.4 Continuous-time projection

Let

$$
f_0(Z)=\dot x^{(0)}.
$$

The tangent projector is

$$
P_T(x)
=
I_3-rac{xx^T}{x^Tx}.
$$

The projected node derivative is

$$
\boxed{
f_P=P_Tf_0
=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The complete dynamics are

$$
\dot Z_P
=
\left(
f_P,
\dot s^{(0)},
\dot q^{(0)}
\right).
$$

Tangency follows exactly:

$$
\frac{d}{dt}\Gamma(Z(t))
=
\frac23x^Tf_P
=0.
$$

This is a continuous-time result. Discrete preservation requires the numerical policy below.

---

# 5. $M_{FP}$: feedback followed by projection

Version 1.0 fixes the ordering

$$
F_{\mathrm{proposal}}=F_0+F_F,
$$

followed by node-state projection.

The node derivative is

$$
f_{FP}
=
P_T\left(f_0-\chi c(x)x\right).
$$

The $s$ and $q$ derivatives retain the $M_F$ feedback terms.

Since

$$
P_Tx=0,
$$

the radial node-feedback term is annihilated:

$$
P_T[-\chi c(x)x]=0.
$$

Therefore version 1.0 requires the exact structural identity

$$
\boxed{
f_{FP}=f_P.
}
$$

This applies only to node derivatives. In general,

$$
\dot s^{(FP)}\ne\dot s^{(P)},
\qquad
\dot q^{(FP)}\ne\dot q^{(P)}.
$$

## Exact reductions

The implementation must satisfy:

- $M_{FP}$ with projection disabled equals $M_F$;
- $M_{FP}$ with $\chi=\eta_2=\rho=0$ equals $M_P$;
- disabling projection and setting $\chi=\eta_2=\rho=0$ equals $M_0$.

---

# 6. Numerical policy

## 6.1 Shared integrator

All four models use classical fixed-step fourth-order Runge--Kutta as the reference integrator:

$$
\begin{aligned}
k_1&=F(Z_n),\\
k_2&=F\left(Z_n+\frac{\Delta t}{2}k_1\right),\\
k_3&=F\left(Z_n+\frac{\Delta t}{2}k_2\right),\\
k_4&=F\left(Z_n+\Delta t\,k_3\right),\\
Z_{n+1}^{\mathrm{raw}}&=Z_n+\frac{\Delta t}{6}(k_1+2k_2+2k_3+k_4).
\end{aligned}
$$

The software-reference configuration is

$$
\Delta t=10^{-3},
\qquad
T=10.
$$

Later experiment protocols may change these values only by an explicit versioned amendment.

## 6.2 Projected stages

For $M_P$ and $M_{FP}$, every RK4 stage evaluates the projected vector field using the same run-level constant $c_0$.

## 6.3 Mandatory retraction

After every full RK4 step in $M_P$ and $M_{FP}$, retract the raw node state:

$$
x_{n+1}
=
\sqrt{3c_0}
\frac{x_{n+1}^{\mathrm{raw}}}
{\|x_{n+1}^{\mathrm{raw}}\|}.
$$

The $s$ and $q$ components are not retracted.

Record both the pre-retraction residual and

$$
r_n
=
\|x_{n+1}-x_{n+1}^{\mathrm{raw}}\|.
$$

$M_0$ and $M_F$ use the same RK4 integrator but no retraction.

## 6.4 Singular and nonfinite policy

Require

$$
c_0\geq10^{-6}.
$$

Let

$$
r_*=\sqrt{3c_0},
\qquad
r_{\min}=\max(10^{-12},10^{-8}r_*).
$$

Fail closed if, at any projected stage or retraction:

$$
\|x\|\leq r_{\min},
$$

or if any state, derivative, projection, distance, or diagnostic is nonfinite.

No silent pseudoinverse replacement, denominator clipping, or arbitrary projection fallback is permitted.

## 6.5 Numerical tolerances

Algebraic projector checks use

$$
\text{atol}=\text{rtol}=10^{-12}.
$$

The normalized tangency residual must satisfy

$$
\frac{|x^Tf_P|}
{\|x\|\,\|f_P\|+10^{-30}}
\leq10^{-12}.
$$

After retraction,

$$
|c(x)-c_0|
\leq10^{-12}\max(1,c_0).
$$

Before scientific use, every reported configuration must be rerun at

$$
\Delta t,
\qquad
\frac{\Delta t}{2},
\qquad
\frac{\Delta t}{4}.
$$

For every frozen observation map, the endpoint discrepancy at $\Delta t/2$ versus $\Delta t/4$ must be smaller than at $\Delta t$ versus $\Delta t/2$ and must satisfy

$$
\|O_{\Delta t/2}-O_{\Delta t/4}\|_\infty
\leq10^{-6}+10^{-5}\|O_{\Delta t/4}\|_\infty.
$$

Failure blocks the run rather than being averaged away.

---

# 7. Initial-condition contract

## 7.1 Reference smoke state

The existing reference state remains

$$
x_0=(0.8,-0.25,0.45),
$$

$$
s_0=(0.2,-0.1,0.1),
\qquad
q_0=(0,0.05,-0.05).
$$

For projected models,

$$
c_0=c(x_0).
$$

## 7.2 Frozen development family

For mechanism-development runs, use

$$
x_0=\sqrt{3c_0}\,u,
\qquad
\|u\|=1,
$$

with

$$
c_0\in\{0.05,0.25,1.0\}
$$

and normalized directions generated from

$$
\begin{aligned}
v_1&=(1,1,1),\\
v_2&=(1,-1,0),\\
v_3&=(1,2,-3),\\
v_4&=(0.8,-0.25,0.45),\\
v_5&=(2,-1,1),\\
v_6&=(1,0.2,-0.4).
\end{aligned}
$$

Use the same $s_0$ and $q_0$ above for each model. Permutation-equivariance tests generate consistent permutations of $x,s,q$ separately from this family.

This is a development family, not a confirmatory sample.

---

# 8. Observation maps

Every comparison must state the observation map under which equivalence or difference is claimed.

## Full state

$$
O_{\mathrm{full}}(Z)=(x,s,q)\in\mathbb R^9.
$$

## Node state

$$
O_x(Z)=x\in\mathbb R^3.
$$

## Adaptive substrate

$$
O_{sq}(Z)=(s,q)\in\mathbb R^6.
$$

## Intrinsic geometry

$$
O_d(Z)=(d_{01},d_{02},d_{12})\in\mathbb R^3.
$$

## Mechanism diagnostics

Record:

- the local proposal $F_0$;
- the feedback vector $F_F$;
- the projection correction;
- the pre- and post-retraction constraint residual;
- retraction magnitude;
- normalized tangency residual;
- projection denominator $x^Tx$.

No unqualified claim of model equivalence is permitted. It must specify both the observation map and tolerance.

---

# 9. Independent reference boundary

The production implementation may share state and parameter data structures, but the independent reference path must:

- live in a separate module or test-only module;
- write the equations directly from this contract;
- not call production derivative, feedback, projector, retraction, or integrator helpers;
- compare complete derivatives and one-step updates against production;
- use separately written edge loops or explicit formulas.

Agreement with code that calls the same helpers is not an independent reference test.

---

# 10. Fairness and control policy

- All models use the same graph, local parameters, initial $x,s,q$, observation schedule, and RK4 accuracy policy.
- $c_0$ is derived from the shared initial state and is not fitted.
- Projection adds no fitted parameter in version 1.0.
- Feedback parameters are active only in $M_F$ and $M_{FP}$; parameter-count differences must be reported.
- $M_0$ must contain no hidden collective transition path.
- $M_P$ version 1.0 projects only $x$.
- A later projection involving $s$, $q$, mismatch, or intrinsic geometry must receive a new versioned contract.
- The soft-penalty control is excluded from the first four-model experiment. It may be introduced later as a separately preregistered comparison.
- Raw outputs must contain the model identifier, source commit, configuration hash, and contract version.

---

# 11. State-safety tripwires

A run fails if any condition occurs:

- nonfinite state or derivative;
- projected-stage norm at or below $r_{\min}$;
- post-retraction constraint residual above tolerance;
- normalized tangency residual above tolerance;
- $|s_e|>50$ or $|q_e|>50$;
- $\|x\|_\infty>10^6$;
- integration refinement criterion fails;
- production/reference parity fails.

These are software-safety bounds, not physical laws.

---

# 12. Required verification gates

## $M_0$

- direct known-answer derivative test;
- proof by dependency audit that $c(x)$ does not enter transitions;
- exact reduction from $M_F$ at $\chi=\eta_2=\rho=0$;
- permutation equivariance;
- production/reference parity.

## $M_F$

- preservation of the existing five tests;
- direct known-answer test for all three feedback paths;
- mutation tests for removed or sign-flipped feedback paths;
- production/reference parity.

## $M_P$

- hand-computed projection test;
- $P_T^T=P_T$ and $P_T^2=P_T$;
- tangency test;
- fail-closed singular test;
- permutation equivariance;
- mandatory retraction test;
- step-refinement test;
- production/reference parity.

## $M_{FP}$

- exact reductions to $M_0$, $M_F$, and $M_P$;
- exact node radial-feedback annihilation test;
- retained $s/q$ feedback test;
- separate feedback and projection diagnostics;
- production/reference parity.

---

# 13. Frozen Phase 1 decisions

Version 1.0 resolves the former open questions as follows:

1. **Integrator:** fixed-step classical RK4 for all models.
2. **Retraction:** mandatory after every full $M_P$ and $M_{FP}$ step.
3. **Near singularity:** relative norm threshold with fail-closed behavior.
4. **Projection scope:** $x$ only in version 1.0.
5. **Second projection prototype:** deferred; any relational constraint receives a new contract.
6. **Initial conditions:** reference state plus the frozen development family above.
7. **Parameters:** existing defaults fixed for the first implementation; no sweep yet.
8. **Independent implementation:** separate code path with no production equation helpers.
9. **Observation maps:** full, node, adaptive-substrate, geometry, and mechanism maps frozen above.
10. **Soft penalty:** excluded from the first comparison.
11. **Interpretive scope:** sphere projection is a mechanism sandbox, not a claim about physical reality.

## Phase 1 exit decision

**PASS — contract frozen for implementation.**

The next implementation gate is $M_0$.

The scientific claim ceiling remains unchanged until later gates pass.

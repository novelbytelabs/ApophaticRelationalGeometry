# Four-Model Design Contract

**Contract status:** Frozen, version 1.0.

**Implementation status:** All four models are implemented and unit-tested.

**Scientific status:** The contract fixes definitions, ordering, numerical policies, diagnostics, and software-verification requirements. It does not establish physical adequacy, scientific superiority, macro-level causal autonomy, or equivalence between collective feedback and projection.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

The constant-amplitude manifold in this contract is a deliberately minimal projection-mechanism sandbox. It is not the completed relational-admissibility geometry of ARG.

---

# 1. Purpose

This contract defines the first directly comparable ARG model family:

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

Its purpose is to separate:

1. local/adaptive substrate dynamics;
2. endogenous collective feedback;
3. explicit tangent-space projection;
4. feedback followed by projection;

while holding the graph, state representation, local parameters, observation schedule, and reference integrator policy fixed.

---

# 2. Shared substrate

## 2.1 Graph and state

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

## 2.2 Edge activation and conductance

For edge $(i,j)$,

$$
a_{ij}=\sigma(s_{ij})
=\frac{1}{1+e^{-s_{ij}}},
$$

$$
w_{ij}=a_{ij}e^{-q_{ij}}.
$$

## 2.3 Intrinsic geometry

For edge $(i,j)$,

$$
\ell_{ij}(Z)
=
\frac{e^{q_{ij}}}{\sigma(s_{ij})}
\sqrt{\epsilon^2+(x_i-x_j)^2}.
$$

The intrinsic distance $d_Z(i,j)$ is the shortest-path distance induced by these positive edge lengths.

In contract v1.0, intrinsic geometry is an observable. It does not define the projection constraint.

## 2.4 Reference parameter set

The software-reference parameters are

$$
\begin{aligned}
\alpha&=1.0,&\beta&=1.0,&\chi&=0.35,\\
\tau_s&=1.0,&\eta_0&=0.25,&\eta_1&=1.0,&\eta_2&=0.2,\\
\tau_q&=1.0,&\gamma&=0.8,&\kappa&=0.4,&\rho&=0.15,\\
\epsilon&=10^{-6}.&&
\end{aligned}
$$

Implementation validation requires all parameters to be finite and

$$
\beta,\tau_s,\eta_1,\tau_q,\gamma,\epsilon>0,
$$

$$
\chi,\eta_0,\eta_2,\kappa,\rho\ge0.
$$

No scientific parameter sweep is licensed by this contract. Exploratory and confirmatory manifests belong to a later experiment protocol.

---

# 3. $M_0$: local/adaptive baseline

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

## Dependency invariant

No value computed from $c(x)$ may enter an $M_0$ transition equation. Logging $c(x)$ is allowed; transition dependence is not.

---

# 4. $M_F$: endogenous collective feedback

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

recovers $M_0$ exactly for the frozen equations.

## Licensed description

$M_F$ implements prototype-level downward feedback/constraint through

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

It does not establish macro-level causal autonomy, transport, counterfactual adequacy, or alternative-model defeat.

---

# 5. $M_P$: projected admissibility

## 5.1 Constraint

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

There are no inequality constraints:

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

## 5.2 Jacobian and regularity

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

On the manifold,

$$
J_\Gamma J_\Gamma^T
=
\frac49x^Tx
=
\frac43c_0>0.
$$

Thus the rank-one projection is regular whenever $c_0>0$.

## 5.3 State-space metric and projector

Version 1.0 uses

$$
G=I_9.
$$

The node tangent projector is

$$
P_T(x)
=
I_3-\frac{xx^T}{x^Tx}.
$$

Let

$$
f_0(Z)=\dot x^{(0)}.
$$

Then

$$
\boxed{
f_P=P_Tf_0
=f_0-x\frac{x^Tf_0}{x^Tx}.
}
$$

The complete derivative is

$$
\dot Z_P
=
\left(
f_P,
\dot s^{(0)},
\dot q^{(0)}
\right).
$$

Tangency follows:

$$
x^Tf_P=0,
$$

$$
\frac{d}{dt}\Gamma(Z(t))
=
\frac23x^Tf_P
=0.
$$

This is a continuous-time result. Discrete preservation follows the numerical policy below.

---

# 6. $M_{FP}$: feedback followed by projection

Version 1.0 fixes the ordering

$$
F_{\mathrm{proposal}}=F_0+F_F,
$$

followed by node-state projection.

The node proposal is

$$
f_0-\chi c(x)x,
$$

and the projected node derivative is

$$
f_{FP}
=
P_T\left(f_0-\chi c(x)x\right).
$$

The $s$ and $q$ derivatives retain the $M_F$ feedback terms.

Because

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

This identity applies only to the node derivative at the same full state. In general,

$$
\dot s^{(FP)}\ne\dot s^{(P)},
\qquad
\dot q^{(FP)}\ne\dot q^{(P)}.
$$

Consequently, the $M_P$ and $M_{FP}$ trajectories need not remain equal: different $s/q$ trajectories can alter later conductances and node proposals.

## Reduction requirements

The implementation must establish:

- the unprojected $F_0+F_F$ proposal agrees with $M_F$;
- $M_{FP}$ with $\chi=\eta_2=\rho=0$ equals $M_P$;
- removing feedback and projection recovers $M_0$.

These requirements are unit-tested at the software level.

---

# 7. Numerical policy

## 7.1 Shared integrator

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

Later experiment protocols may change these values only through an explicit versioned amendment.

## 7.2 Projected stages

For $M_P$ and $M_{FP}$, every RK4 stage evaluates the applicable projected vector field using the same run-level constant $c_0$.

## 7.3 Mandatory retraction

After every complete $M_P$ or $M_{FP}$ RK4 step, retract the raw node state:

$$
x_{n+1}
=
\sqrt{3c_0}
\frac{x_{n+1}^{\mathrm{raw}}}
{\|x_{n+1}^{\mathrm{raw}}\|}.
$$

The $s$ and $q$ components are not retracted.

Record the pre-retraction constraint residual, post-retraction residual, and

$$
r_n
=
\|x_{n+1}-x_{n+1}^{\mathrm{raw}}\|.
$$

$M_0$ and $M_F$ use the same RK4 integrator without retraction.

## 7.4 Singular and nonfinite policy

The executable domain requires

$$
c_0\ge10^{-6}.
$$

Let

$$
r_*=\sqrt{3c_0},
\qquad
r_{\min}=\max(10^{-12},10^{-8}r_*).
$$

Fail closed if, at any projected stage or retraction,

$$
\|x\|\le r_{\min},
$$

or if any state, derivative, projection, distance, or diagnostic is nonfinite.

No silent pseudoinverse replacement, denominator clipping, or arbitrary projection fallback is permitted.

## 7.5 Tolerances

Algebraic projector checks use

$$
\mathrm{atol}=\mathrm{rtol}=10^{-12}.
$$

The normalized tangency residual must satisfy

$$
\frac{|x^Tf|}
{\|x\|\,\|f\|+10^{-30}}
\le10^{-12}.
$$

After retraction,

$$
|c(x)-c_0|
\le10^{-12}\max(1,c_0).
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
\le10^{-6}+10^{-5}\|O_{\Delta t/4}\|_\infty.
$$

Failure blocks the run rather than being averaged away.

---

# 8. Initial-condition contract

## 8.1 Reference state

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

## 8.2 Frozen development family

For mechanism-development runs,

$$
x_0=\sqrt{3c_0}\,u,
\qquad
\|u\|=1,
$$

with

$$
c_0\in\{0.05,0.25,1.0\},
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

Use the same $s_0$ and $q_0$ for each model. Permutation-equivariance tests generate consistent permutations of $x,s,q$.

This is a development family, not a confirmatory sample.

---

# 9. Observation maps

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

Record, where applicable:

- local proposal $F_0$;
- feedback vector $F_F$;
- combined proposal $F_0+F_F$;
- projection correction;
- projected derivative;
- feedback and correction norms;
- pre- and post-retraction constraint residuals;
- retraction magnitude;
- normalized tangency residual;
- projection denominator $x^Tx$.

No unqualified claim of model equivalence is permitted. It must specify the observation map, domain, and tolerance.

---

# 10. Independent reference boundary

The production implementation may share immutable state, parameter, and target containers with the reference path. The reference path must:

- live in a separate test-only module;
- write the equations directly from this contract;
- not call production derivative, feedback, projector, retraction, or integrator helpers;
- compare complete derivatives and one-step updates against production;
- use separately written edge loops or explicit formulas.

Agreement with code that calls the same production helpers is not an independent reference test.

---

# 11. Fairness and control policy

- All models use the same graph, local parameters, initial $x,s,q$, observation schedule, and RK4 accuracy policy.
- $c_0$ is derived from the shared initial state and is not fitted.
- Projection adds no fitted parameter in version 1.0.
- Feedback parameters are active only in $M_F$ and $M_{FP}$; parameter-count differences must be reported.
- $M_0$ contains no hidden collective transition path.
- $M_P$ version 1.0 projects only $x$.
- $M_{FP}$ applies feedback before projection.
- A later projection involving $s$, $q$, mismatch, intrinsic geometry, or inequality constraints requires a new versioned contract.
- The soft-penalty control is excluded from the first four-model experiment unless separately preregistered.
- Raw outputs contain the model identifier, source commit, configuration hash, and contract version.

---

# 12. State-safety tripwires

A run fails if any condition occurs:

- nonfinite state or derivative;
- projected-stage norm at or below $r_{\min}$;
- post-retraction constraint residual above tolerance;
- normalized tangency residual above tolerance;
- $|s_e|>50$ or $|q_e|>50$;
- $\|x\|_\infty>10^6$;
- integration-refinement criterion fails;
- production/reference parity fails.

These are software-safety bounds, not physical laws.

---

# 13. Verification gates

## $M_0$

- known-answer derivative;
- no-$c(x)$ dependency tripwire;
- exact zero-feedback reduction from $M_F$;
- permutation equivariance;
- production/reference parity.

## $M_F$

- fixed regression derivative;
- all three feedback paths;
- zero-feedback reduction to $M_0$;
- production/reference parity.

## $M_P$

- hand-computed projection;
- $P_T^T=P_T$ and $P_T^2=P_T$;
- $P_Tx=0$ and tangency;
- fail-closed singular behavior;
- permutation equivariance;
- mandatory retraction;
- step refinement;
- production/reference parity.

## $M_{FP}$

- explicit $F_0$, $F_F$, and $F_0+F_F$ decomposition;
- radial node-feedback annihilation;
- same-state identity $f_{FP}=f_P$;
- retained $s/q$ feedback;
- zero-feedback reduction to $M_P$;
- no-feedback/no-projection recovery of $M_0$;
- separate feedback and projection diagnostics;
- permutation equivariance;
- fail-closed singular behavior;
- retraction and refinement;
- production/reference parity.

All four software gates have passed. Their verification records are in `16_phase3_mp_verification.md`, `17_phase4_mfp_verification.md`, and the claim ledger.

---

# 14. Implementation records and scientific boundary

## Implementation records

- Phase 2: $M_0/M_F$ baseline and parity suite.
- Phase 3: $M_P$, PR `#5`, merge `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`, 35 tests on Python 3.10 and 3.12.
- Phase 4: $M_{FP}$, PR `#7`, merge `205fb8c5bf1b832e241af230612e3d7056be05f5`, 51 tests on Python 3.10 and 3.12.

## Scientific boundary

The passed software gates establish that the declared mechanisms exist in code and satisfy the frozen implementation contracts at tested cases.

They do not establish:

- that feedback and projection are scientifically equivalent;
- that same-state node identity implies trajectory identity;
- that any model predicts a physical system;
- that the constant-amplitude constraint is physically correct;
- that ARG defeats simpler alternatives;
- that macro-level causal autonomy or strong emergence has been demonstrated.

The next gate is the frozen Phase 5 comparative experiment protocol. No development pilot is authorized before that protocol passes review.

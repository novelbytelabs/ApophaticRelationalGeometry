# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism.

A phase is complete only when its exit criteria are satisfied and the claim ledger is updated. Failed results narrow or stop the program; they do not automatically trigger a more complicated model.

## Current position

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

The project is entering **Phase 0: alignment and claim control**.

---

## Phase 0 — Alignment and claim control

### Objective

Make every public and internal project description agree with the executable evidence.

### Deliverables

- canonical mechanism definitions;
- canonical model family $M_0,M_F,M_P,M_{FP}$;
- explicit claim ceiling;
- README and documentation split between target formalism and current implementation;
- claim-ledger entries for feedback, projection, equivalence, and downward-causation scope;
- prohibition against calling $M_F$ projected geometry.

### Exit criteria

- every core document uses the same model names and statuses;
- no current-code description implies that $\Gamma/H$ projection is implemented;
- the current executable is labeled $M_F$;
- projected claims remain fail-closed and unverified;
- existing unit tests still pass.

### Claim ceiling after completion

Unchanged:

$$
M_F\ \text{implemented and unit-tested only}.
$$

---

## Phase 1 — Freeze the four-model design contract

### Objective

Define the models precisely enough that implementation choices cannot move after results are seen.

### Deliverables

#### $M_0$ contract

Define the local/adaptive substrate with every collective-feedback term removed. This includes deciding whether $c(x)$ is absent entirely or computed only for diagnostics.

#### $M_F$ contract

Freeze the current equations and identify every path through which $c(x)$ affects $\dot x$, $\dot s$, and $\dot q$.

#### $M_P$ contract

Specify:

- complete state vector;
- explicit $\Gamma(Z)$ and any $H(Z)$;
- proposal field $F_{\mathrm{local}}$;
- state-space metric used by the projection;
- rank and regularity assumptions;
- continuous-time projection equation;
- numerical retraction or constraint-preserving integration method;
- measurable projection contribution.

#### $M_{FP}$ contract

Specify how feedback and projection coexist without being merged into one unnamed collective term.

### Exit criteria

- equations for all four models are frozen in one versioned document;
- state dimensions and observables are explicit;
- parameter-sharing and fairness rules are fixed;
- singular and rank-deficient cases have declared behavior;
- an independent reviewer can implement each model from the contract alone.

### Stop condition

Do not implement $M_P$ if no nontrivial, coherent admissible manifold can be defined without merely restating the feedback equation.

---

## Phase 2 — Baseline normalization and $M_0$ implementation

### Objective

Create a genuine mechanism-free comparison substrate.

### Deliverables

- executable $M_0$;
- exact mapping between $M_0$ and $M_F$ parameters;
- tests proving that collective paths are absent from $M_0$;
- matched initial-condition generator;
- deterministic configuration and seed manifests;
- independently written right-hand side for $M_0$ and $M_F$.

### Required tests

- code-equation parity;
- finite-value tripwires;
- permutation equivariance;
- time-step convergence;
- deterministic replay;
- parameter validation;
- diagnostic proof that setting feedback coefficients to zero reproduces $M_0$.

### Exit criteria

- $M_0$ and $M_F$ differ only by declared feedback paths;
- all tests pass under at least two integration methods;
- no hidden collective statistic influences $M_0$ transitions.

---

## Phase 3 — $M_P$ mathematical specification and proofs

### Objective

Establish that the projected model is mathematically coherent before treating numerical output as evidence.

### Core prototype

A candidate equality constraint may begin with an independent collective state $c$:

$$
\Gamma(Z)
=
c-\frac13\sum_{i=1}^{3}x_i^2
=0,
$$

but this is only a candidate. The phase must determine whether it yields a meaningful projection mechanism rather than an artificial bookkeeping identity.

### Proof obligations

- regularity of $\Gamma$ and $H$;
- rank conditions for the constraint Jacobian;
- existence and uniqueness of the projected vector field;
- tangency:

$$
J_\Gamma(Z)\dot Z=0;
$$

- preservation of equality constraints in continuous time;
- treatment of active inequality constraints;
- permutation equivariance;
- behavior at singular or disconnected states;
- distinction from feedback and penalty dynamics.

### Exit criteria

- a checked derivation of the projection equation;
- explicit domain of validity;
- counterexamples or excluded regimes documented;
- no claim of global well-posedness beyond the proved domain;
- projection is mathematically nontrivial and distinguishable from $M_F$ by construction.

### Stop condition

If $M_P$ is provably equivalent to $M_F$ only by defining the constraint from the already chosen feedback field, record circularity and reject that equivalence route.

---

## Phase 4 — $M_P$ implementation and verification

### Objective

Implement projection with fail-closed code-equation parity.

### Deliverables

- explicit projection operator;
- diagnostic decomposition

$$
F_{\mathrm{local}}
=
F_{\mathrm{tangent}}+F_{\mathrm{normal}};
$$

- constraint-preserving integrator or documented projection/retraction step;
- independent reference implementation;
- constraint-error and condition-number traces;
- tests for active inequality constraints if $H$ is used.

### Required gates

$$
D_{\Gamma,H}=\text{PASS},
$$

$$
I_{\Pi}=\text{PASS},
$$

$$
T_{\mathrm{preserve}}=\text{PASS},
$$

$$
E_{\mathrm{code}}=\text{PASS},
$$

$$
S_{\mathrm{path}}=\text{PASS}.
$$

Only then may

$$
\operatorname{PROJECTED\_CLAIM}=\text{IMPLEMENTED\_PROTOTYPE}.
$$

This still does not establish scientific usefulness.

### Exit criteria

- constraint drift meets declared tolerance across solver refinement;
- the independent implementation agrees within tolerance;
- singular cases fail closed;
- permutation equivariance passes;
- the projection contribution is separately recorded.

---

## Phase 5 — $M_{FP}$ implementation

### Objective

Combine feedback and projection without losing mechanism identifiability.

### Deliverables

- executable $M_{FP}$;
- separate feedback vector $F_F$;
- separate projection correction $F_P$;
- explicit ordering convention if feedback changes the proposal before projection;
- alternative ordering test where mathematically meaningful;
- interaction diagnostic.

A minimal decomposition is

$$
\dot Z
=
F_0(Z)+F_F(Z)+F_P\bigl(Z,F_0+F_F\bigr).
$$

### Exit criteria

- removing $F_F$ recovers $M_P$;
- removing $F_P$ recovers $M_F$;
- removing both recovers $M_0$;
- mechanism contributions remain separately measurable;
- no double-counting of the same collective term.

---

## Phase 6 — Comparative mechanism experiment

### Objective

Determine whether feedback and projection are distinct, equivalent in a restricted regime, complementary, or redundant.

### Core comparisons

$$
M_0,
\qquad
M_F,
\qquad
M_P,
\qquad
M_{FP}.
$$

Secondary controls may include a matched soft-penalty model, but it does not replace the four canonical models.

### Primary questions

1. Does $M_F$ differ materially from $M_0$?
2. Does $M_P$ differ materially from $M_0$?
3. Does $M_{FP}$ contain nonadditive interaction behavior?
4. Can $M_F$ and $M_P$ be discriminated from observed trajectories?
5. Is any apparent equivalence global, local, asymptotic, parameter-specific, or merely observational under limited measurements?

### Required measurements

Feedback ratio:

$$
\chi_i^{F}(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

Projection ratio:

$$
\chi_i^{P}(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)+F_{F,i}(t)\|+\epsilon}.
$$

Constraint error:

$$
\epsilon_\Gamma(t)=\|\Gamma(Z(t))\|.
$$

Additional outputs:

- trajectory distance;
- intrinsic metric evolution;
- structural-transition timing;
- perturbation recovery;
- stability and boundedness;
- computational cost;
- parameter sensitivity;
- identifiability under partial observation.

### Equivalence standard

Do not claim $M_F\equiv M_P$ from similar plots.

An equivalence claim requires one of:

- an exact mathematical conjugacy or reparameterization;
- a proved approximation with error bounds;
- a clearly scoped observational equivalence under a declared observation map.

### Exit criteria

- preregistered protocol executed;
- all four models evaluated under matched conditions;
- alternative models tested;
- raw artifacts and configuration hashes retained;
- claim ledger updated whether the result is positive, null, or negative.

---

## Phase 7 — Research grounding and known-system anchors

### Objective

Determine whether ARG is merely a repackaging, a useful synthesis, or a broader formalism.

### Workstreams

- projected dynamical systems and differential-algebraic equations;
- adaptive and coevolving networks;
- cellular sheaves and compatibility systems;
- dynamic metric graphs and discrete curvature;
- singular barriers and noncollision;
- gauge, groupoid, and equivariant descriptions.

### Anchor systems

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

### Exit criteria

At least one of the following is established:

- a new theorem;
- a strict generalization of an established model family;
- a useful invariant or decomposition;
- a robust dynamical signature unavailable to matched alternatives;
- improved performance on an established physical problem.

Otherwise, ARG remains a documented candidate synthesis.

---

## Phase 8 — Scientific evaluation

### Objective

Test a narrow domain-specific scientific hypothesis without promoting prototype behavior into a theory of reality.

### Entry requirements

- Phases 0–7 passed or explicitly narrowed;
- primary-source novelty audit complete;
- selected domain and dataset justified;
- development and confirmatory protocols separated;
- independent audit of code, configuration, and statistics;
- claim ceiling fixed before confirmatory execution.

### Possible outcomes

- **Supported within domain** — a narrow predictive or explanatory claim survives.
- **Equivalent to established method** — novelty claim withdrawn; synthesis value may remain.
- **No advantage** — scientific claim rejected for the tested domain.
- **Mathematical failure** — affected formalism narrowed or rejected.

No outcome establishes an absolute ontology.

---

## Immediate execution queue

1. Complete Phase 0 documentation alignment.
2. Run the existing unit suite and record the commit and result.
3. Write the Phase 1 four-model design contract.
4. Implement $M_0$ as a true no-collective baseline.
5. Freeze $M_F$ equations and substrate paths.
6. Design $M_P$ mathematically before writing its production implementation.
7. Do not execute a comparative scientific experiment until Phases 1–5 pass.

## Roadmap maxim

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Raise the claim only after the gate passes.

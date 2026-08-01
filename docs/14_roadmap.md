# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism.

A phase is complete only when its exit criteria are satisfied and the claim ledger is updated. Failed results narrow or stop the program; they do not automatically trigger a more complicated model.

## Current claim ceiling

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Current position

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Core docs, metadata, model labels, claim ledger, benchmark plan, and falsification rules now use the same $M_0/M_F/M_P/M_{FP}$ split. |
| Phase 1 — Four-model design contract | IN PROGRESS | Draft v0.1 created in `15_four_model_design_contract.md`. |
| Phase 2 onward | BLOCKED | Await Phase 1 freeze. |

Verification note: the five existing software tests passed in a clean local run using the current source logic. This is a software verification result, not a scientific result or hosted-CI attestation.

---

## Phase 0 — Alignment and claim control

### Objective

Make every public and internal project description agree with the executable evidence.

### Completed deliverables

- canonical mechanism definitions;
- canonical model family $M_0,M_F,M_P,M_{FP}$;
- explicit claim ceiling;
- README and documentation split between target formalism and current implementation;
- claim-ledger entries for feedback, projection, equivalence, and downward-causation scope;
- prohibition against calling $M_F$ projected geometry;
- package and citation metadata aligned with the $M_F$ prototype;
- software test rerun: five tests passed.

### Exit decision

**PASS.**

The claim ceiling remains unchanged.

---

## Phase 1 — Freeze the four-model design contract

### Objective

Define all four models precisely enough that implementation choices cannot move after results are seen.

### Active artifact

`15_four_model_design_contract.md`

### Current v0.1 proposal

- $M_0$: exact no-feedback local/adaptive baseline.
- $M_F$: current feedback implementation, expressed as $F_0+F_F$.
- $M_P$: constant-amplitude projection on

$$
\Gamma(Z)=c(x)-c_0=0,
\qquad
c_0=c(x(0))>0.
$$

- $M_{FP}$: feedback proposal followed by projection.

The v0.1 projection is deliberately minimal, state-dimension matched, and analytically tractable.

### Preregistered structural consequence

For the node-state projection

$$
P_T=I-\frac{xx^T}{x^Tx},
$$

the radial node-feedback term satisfies

$$
P_T\left(-\chi c(x)x\right)=0.
$$

Therefore, under the v0.1 constraint and project-after-feedback ordering,

$$
f_{FP}=f_P
$$

for node-state derivatives, while $s$ and $q$ feedback may still distinguish $M_{FP}$ from $M_P$.

This consequence must be understood and accepted before implementation.

### Remaining design decisions

1. Select the reference integrator and tolerance policy.
2. Decide whether post-step retraction is mandatory.
3. Freeze the near-singular norm threshold and fail-closed behavior.
4. Confirm that $M_P$ v0.1 projects only node states.
5. Define the initial-condition family with $c_0>0$.
6. Freeze parameter ranges and boundedness checks.
7. Define the independent reference implementation boundary.
8. Freeze full-state and partial-observation comparison maps.
9. Decide whether the soft-penalty control is included in the first experiment.
10. Review whether the constant-amplitude manifold is sufficiently nontrivial for the intended mechanism test.

### Exit criteria

- equations for all four models are frozen;
- state dimensions and observables are explicit;
- exact reductions are specified;
- fairness and parameter-sharing rules are fixed;
- singular cases have declared behavior;
- the numerical preservation method is selected;
- an independent reviewer can implement each model from the contract alone;
- the contract is explicitly versioned as frozen.

### Stop condition

Do not implement $M_P$ if review finds that the selected constraint is circular, trivial for the research question, or incapable of distinguishing projection from feedback.

---

## Phase 2 — Implement and verify $M_0$

### Objective

Create a genuine no-collective comparison substrate.

### Deliverables

- executable $M_0$;
- exact mapping between $M_0$ and $M_F$ parameters;
- tests proving that $c(x)$ does not enter $M_0$ transitions;
- deterministic initial-condition and configuration manifests;
- independently written right-hand sides for $M_0$ and $M_F$;
- exact reduction test from $M_F$ at $\chi=\eta_2=\rho=0$.

### Exit criteria

- $M_0$ and $M_F$ differ only by declared feedback paths;
- all software tests pass under at least two appropriate integration methods;
- deliberate feedback mutations trip the relevant tests;
- no hidden collective path exists in $M_0$.

---

## Phase 3 — Prove the $M_P$ prototype

### Objective

Establish mathematical coherence before treating numerical output as evidence.

### Obligations

- regularity and rank of $\Gamma$;
- existence and uniqueness of projection on the declared domain;
- continuous-time tangency and constraint preservation;
- permutation equivariance;
- explicit singularity exclusions;
- distinction from feedback and soft penalties;
- boundedness or continuation conditions where possible.

### Exit criteria

- checked derivation of the projector;
- explicit domain of validity;
- counterexamples and excluded regimes documented;
- no claim beyond the proved domain.

---

## Phase 4 — Implement and verify $M_P$

### Objective

Implement projection with fail-closed code-equation parity.

### Required gate

$$
\operatorname{PROJECTED\_CLAIM}
=
D_{\Gamma,H}
\land_{FC}
I_{\Pi}
\land_{FC}
T_{\mathrm{preserve}}
\land_{FC}
E_{\mathrm{code}}
\land_{FC}
S_{\mathrm{path}}.
$$

All terms must pass before the label `IMPLEMENTED_PROTOTYPE` is permitted.

### Deliverables

- tangent and normal decomposition;
- constraint-preserving integrator or declared retraction;
- independent projector implementation;
- constraint-error, condition-number, and retraction traces;
- singular cases that fail closed;
- permutation and convergence tests.

---

## Phase 5 — Implement and verify $M_{FP}$

### Objective

Combine feedback and projection without losing mechanism identifiability.

### Deliverables

- separate $F_0$, $F_F$, and $F_P$ outputs;
- frozen ordering convention;
- exact reductions to $M_0$, $M_F$, and $M_P$;
- radial node-feedback annihilation test for v0.1;
- retained $s/q$ feedback tests;
- no double counting.

---

## Phase 6 — Comparative mechanism experiment

### Objective

Determine whether feedback and projection are distinct, restrictedly equivalent, complementary, or redundant.

### Canonical comparison

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

### Primary diagnostics

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon},
$$

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)+F_{F,i}(t)\|+\epsilon},
$$

$$
\epsilon_\Gamma(t)=\|\Gamma(Z(t))\|.
$$

### Equivalence standard

Similar plots do not establish

$$
M_F\equiv M_P.
$$

An equivalence claim requires exact mathematics, a bounded approximation, or a precisely scoped observational equivalence.

### Exit criteria

- preregistered protocol executed;
- all four models evaluated fairly;
- structural and exogenous controls completed;
- raw outputs and hashes retained;
- claim ledger updated for positive, null, or negative results.

---

## Phase 7 — Research grounding and known-system anchors

### Objective

Determine whether ARG is a repackaging, useful synthesis, or broader formalism.

### Anchor systems

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

### Continuation gate

At least one of:

- a new theorem;
- strict generalization of an established family;
- a useful invariant or decomposition;
- a robust signature unavailable to matched alternatives;
- improved performance on an established physical problem.

Otherwise ARG remains a documented candidate synthesis.

---

## Phase 8 — Narrow scientific evaluation

### Entry requirements

- Phases 0–7 passed or explicitly narrowed;
- primary-source novelty audit complete;
- domain-specific hypothesis and data justified;
- development and confirmatory protocols separated;
- independent audit of code, configuration, and statistics;
- claim ceiling fixed before confirmatory execution.

### Possible outcomes

- supported within a narrow domain;
- equivalent to an established method;
- no advantage over alternatives;
- mathematical or numerical failure requiring claim reduction.

No outcome establishes an absolute ontology.

## Immediate execution queue

1. Review the v0.1 design contract.
2. Resolve its ten open decisions.
3. Freeze Phase 1 as version 1.0 or reject the sphere-constraint prototype.
4. Implement $M_0$ only after contract freeze.
5. Do not implement or test $M_P$ scientifically before its mathematical obligations pass.

## Roadmap maxim

> Separate the mechanisms. Freeze the contracts. Prove the projection. Test the alternatives. Raise the claim only after the gate passes.

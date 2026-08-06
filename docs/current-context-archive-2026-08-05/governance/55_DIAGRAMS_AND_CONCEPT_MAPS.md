# Diagrams and Concept Maps

## 1. Developmental sequence

```mermaid
flowchart LR
    A[Pre-determinate condition / apeiron-like source]
    B[Prime distinctions]
    C[Composite relations]
    D[Stable identities]
    E[Formal logic]
    A --> B --> C --> D --> E
```

Status: philosophical-developmental hypothesis.

## 2. Pluralistic monism

```mermaid
flowchart TB
    W[Dynamic whole: global coherence and constraints]
    L1[Local state and rules]
    L2[Local state and rules]
    L3[Local state and rules]
    W <--> L1
    W <--> L2
    W <--> L3
    L1 <--> L2
    L2 <--> L3
    L3 <--> L1
```

Status: central model architecture.

## 3. Structured Becoming

```mermaid
flowchart LR
    A[Structure B_t]
    B[State x_t]
    C[Constraints and dependencies]
    D[Memory M_t]
    E[Delta]
    F[Next structure B_t+1]
    G[Next state x_t+1]
    A --> E
    B --> E
    C --> E
    D --> E
    E --> F
    E --> G
```

Status: persistence framework.

## 4. Geometry–state feedback

```mermaid
flowchart LR
    X[Local states x]
    D[Relational mismatch delta]
    S[Edge activation s]
    Q[Metric deformation q]
    L[Intrinsic lengths ell]
    W[Conductances w]
    F[Local dynamics]
    X --> D
    D --> S
    D --> Q
    S --> L
    Q --> L
    L --> W
    W --> F
    F --> X
```

Status: mathematical proposal.

## 5. Local proposal and global exclusion

```mermaid
flowchart LR
    L[Local nonlinear proposal F_local]
    P[Projection onto admissible tangent directions]
    A[Actual evolution]
    N[Rejected incoherent component / SHADOW candidate]
    L --> P
    P --> A
    P --> N
```

Equation:

$$
\dot Z
=
F_{\mathrm{local}}
-
\Pi_{N_Z\mathcal M}F_{\mathrm{local}}.
$$

## 6. RAIL, SHADOW, KEEPER

```mermaid
flowchart LR
    P[Proposed trajectory]
    S[SHADOW: residual or normal component]
    K[KEEPER: correction policy]
    R[RAIL: admissible viable trajectory]
    P --> S
    S --> K
    K --> R
```

Status: provisional operational mapping.

## 7. Apophatic discipline

```mermaid
flowchart TB
    M[Math model]
    T[Theorems and invariants]
    E[Empirical adequacy]
    O[Claim of absolute reality]
    M --> T
    T --> E
    E -. does not license .-> O
```

Equation:

$$
\text{formal success}
\not\Rightarrow
\text{ontological identity}.
$$

## 8. Infinity barrier

```mermaid
flowchart LR
    D[Intrinsic distance decreases]
    U[Barrier energy increases]
    B[Finite-energy lower bound]
    C[Contact remains unreachable]
    D --> U --> B --> C
```

## 9. Research program

```mermaid
flowchart LR
    A[Definitions]
    B[Minimal model]
    C[Proofs]
    D[Implementation parity]
    E[Tripwires and nulls]
    F[Alignment test]
    G[Dynamic geometry]
    H[Prime substrate]
    A --> B --> C --> D --> E --> F --> G --> H
```

## 10. Document dependency map

```mermaid
flowchart TB
    S[Candidate Synthesis]
    A[Apophatic Meta-Axiom]
    P[Pluralistic Monism]
    B[Structured Becoming]
    G[Dynamic Relational Constraint Geometry]
    M[Minimal Model]
    X[Falsification Program]
    C[Claims Ledger]
    S --> A
    S --> P
    S --> B
    P --> G
    B --> G
    G --> M
    M --> X
    X --> C
```

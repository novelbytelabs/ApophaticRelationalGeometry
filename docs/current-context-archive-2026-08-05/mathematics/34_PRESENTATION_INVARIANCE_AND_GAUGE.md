# Presentation Invariance and Gauge

## 1. Apophatic motivation

A presentation may be useful without being privileged.

The operational form of that discipline is to identify transformations that change representation without changing structural or observable content.

## 2. Presentation space

Let:

$$
\mathcal P
$$

be the space of provisional presentations.

Let:

$$
\mathcal G
$$

be a group or groupoid of admissible transformations.

A transformation is written:

$$
g:P\to P'.
$$

## 3. Node relabeling

For a graph with $N$ nodes, a permutation:

$$
\pi\in S_N
$$

acts on:

- node states;
- edge indices;
- local parameters;
- constraint matrices.

A valid observable satisfies:

$$
Q(\pi\cdot Z)=Q(Z).
$$

The dynamics must satisfy equivariance:

$$
F(\pi\cdot Z)
=
D\pi_ZF(Z).
$$

## 4. Coordinate transformations

Suppose each local state is reparameterized:

$$
x_i'
=
\phi_i(x_i).
$$

The vector field transforms by pushforward:

$$
\dot x_i'
=
D\phi_i(x_i)\dot x_i.
$$

Comparison maps, local metrics, and constraints must be transformed consistently.

A coordinate-dependent quantity is not automatically meaningless, but it cannot be treated as presentation-invariant.

## 5. Gauge transformations

Some variables may contain redundancy. If:

$$
Z\sim g\cdot Z
$$

for all $g$ in a gauge group, then physical claims should descend to gauge orbits:

$$
[Z]_{\mathcal G}.
$$

The quotient is a structural construction, not reality itself.

## 6. Observational equivalence

For observation family $\mathscr O$:

$$
Z\sim_{\mathscr O}Z'
$$

iff:

$$
O(Z)=O(Z')
$$

for every $O\in\mathscr O$.

A richer observation family can distinguish previously equivalent presentations.

Therefore objecthood is relative to admissible distinctions.

## 7. Invariants

Define:

$$
\operatorname{Inv}_{\mathcal G}(\mathcal P)
=
\{Q:Q(g\cdot P)=Q(P)\}.
$$

The key principle is:

$$
\boxed{
\text{There is no invariant without a specified class of admissible variation.}
}
$$

Change $\mathcal G$, and the invariant content may change.

## 8. Structural descent

A claim $Q$ descends to the quotient when there exists $\bar Q$ such that:

$$
Q
=
\bar Q\circ\pi,
$$

where:

$$
\pi:\mathcal P\to\mathcal P/\mathcal G.
$$

This distinguishes presentation-level variables from structural observables.

## 9. Contextual invariance

An invariant under $\mathcal G$ is not necessarily invariant under a larger transformation class $\mathcal G'$.

Thus:

$$
Q\in\operatorname{Inv}_{\mathcal G}
$$

does not imply:

$$
Q\in\operatorname{Inv}_{\mathcal G'}.
$$

This is the mathematical counterpart of apophatic restraint.

## 10. Required invariants for the prototype

The three-node model should test:

- invariance under node permutation when parameters are permuted consistently;
- independence from arbitrary edge ordering;
- coordinate covariance under affine state reparameterization where supported;
- invariance of persistence statistics under equivalent presentations;
- invariance of path distances under graph isomorphism.

## 11. Symmetry versus empirical identity

Symmetry is part of a model.

Empirical indistinguishability is part of an observation protocol.

They may coincide but should not be conflated.

## 12. Failure modes

The model is presentation-dependent if:

- predictions change under node renaming;
- a local/global ratio changes due only to coordinate scale;
- a claimed geometric effect disappears under equivalent parameterization;
- constraints privilege a node without explicit physical reason;
- numerical implementation breaks an intended symmetry.

## 13. Apophatic clause

Even the quotient or invariant structure cannot be promoted into absolute ontology:

$$
\boxed{
\operatorname{Inv}_{\mathcal G}(\mathcal P)
\not\Rightarrow
\text{ultimate reality}.
}
$$

It is the content stable under the selected transformations.

## 14. Canonical hierarchy

$$
\boxed{
\begin{aligned}
\text{presentation}&:P\in\mathcal P,\\
\text{structural content}&:\operatorname{Inv}_{\mathcal G}(P),\\
\text{apophatic restraint}&:
\operatorname{Inv}_{\mathcal G}(P)
\neq
\text{absolute reality}.
\end{aligned}
}
$$

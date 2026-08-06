# Residual Continuation States in Apophatic Relational Geometry

## A Candidate Synthesis of Relational Dynamics, Future Possibility, and Persistent Identity

**Recommended repository path:** `docs/RESIDUAL_CONTINUATION_STATES.md`  
**Project:** Apophatic Relational Geometry  
**Status:** Candidate Synthesis  
**Document type:** Formal integration note  
**Scope:** Mathematical bridge between constrained relational dynamics and operational persistence  
**Epistemic status:** Established mathematical components combined into an ARG-specific synthesis  
**Non-reification constraint:** No formal state, quotient, graph, or continuation space defined here is identified with absolute reality.

---

## 1. Purpose

Apophatic Relational Geometry currently models a system through relational structure, realized state, dependencies, constraints, and transformation. It also proposes that stable identity is not an intrinsic substance but a persistence relation sustained through organized change.

A missing formal bridge remains:

> Which part of the present organization contains exactly the distinctions that matter for the system's possible future behavior?

This document supplies that bridge through the concept of a **residual continuation state**.

The central proposal is:

$$
\boxed{
\text{Operational identity is the minimal present organization that preserves all distinctions relevant to admissible future behavior.}
}
$$

This statement does not define an intrinsic essence. It defines identity relative to a declared system boundary, continuation law, observation map, scale, and criterion of relevance.

The construction connects four ARG concerns:

$$
\boxed{
\text{relational organization}
\longrightarrow
\text{admissible continuation}
\longrightarrow
\text{persistence}
\longrightarrow
\text{stable identity}.
}
$$

---

## 2. Status of the contribution

The underlying mathematical ingredients are established.

They include:

- residual languages and the Myhill-Nerode equivalence;
- state minimization in automata theory;
- behavioral equivalence and bisimulation;
- predictive-state and computational-mechanics constructions;
- symbolic dynamics and cylinder sets;
- coalgebraic unfolding of state-based systems;
- finite approximants and directed completion;
- continuous symbolic coding and localization.

The ARG contribution is not the claim that these results are new.

The contribution is the following synthesis:

1. use residual behavior to define the future-relevant part of a relational history;
2. use the resulting quotient state as an operational identity;
3. embed that identity inside ARG's local-global constraint dynamics;
4. define persistence as lawful continuity of residual behavior through transformation;
5. preserve the apophatic rule that no operational identity is an absolute ground.

Accordingly, this document must remain classified as a **Candidate Synthesis** unless ARG later proves a new theorem, establishes a new invariant, or validates a distinct empirical prediction.

---

## 3. The problem

Let a system evolve through relational configurations:

$$
Z_0,Z_1,Z_2,\ldots
$$

A configuration may be represented schematically as:

$$
Z_t=(\mathcal R_t,x_t,D_t,\Gamma_t),
$$

where:

- $\mathcal R_t$ is the current relational structure;
- $x_t$ is the current realized state;
- $D_t$ is the set of relevant dependencies and environmental conditions;
- $\Gamma_t$ is the current admissibility or constraint structure.

A complete history through time $t$ is:

$$
H_t=(Z_0,e_0,Z_1,e_1,\ldots,e_{t-1},Z_t),
$$

where each $e_i$ is an event, control, observation, or transition input.

The full history generally contains more information than is required to determine future behavior. Two different histories may lead to exactly the same future possibilities and the same future manifestations.

ARG therefore requires an equivalence relation that removes historical detail that no longer makes a behavioral difference.

The target object is not:

$$
\text{the complete past},
$$

and not merely:

$$
\text{the instantaneous state}.
$$

It is:

$$
\boxed{
\text{the minimal quotient of history that remains sufficient for future-relevant behavior}.
}
$$

---

## 4. Formal domain

Let $\Sigma$ be the event or control alphabet.

Let $\Sigma^*$ be the set of finite event histories.

Let $\Sigma^{\mathbb N}$ be the set of complete infinite event continuations.

Let:

$$
Y\subseteq\Sigma^{\mathbb N}
$$

be the globally admissible continuation space.

The set $Y$ represents the whole-system constraint. It specifies which complete continuations are possible under the declared model.

Let:

$$
\pi:Y\to\mathcal O
$$

be an outcome or behavior map into an outcome space $\mathcal O$.

The map $\pi$ may represent:

- a complete observable trajectory;
- a terminal outcome;
- a persistence profile;
- an output stream;
- a macroscopic manifestation;
- a probability law over future observations;
- another declared behavioral object.

The choice of $\pi$ is part of the model. It must not be hidden.

---

## 5. Residual behavior

For a finite admissible history:

$$
h\in\operatorname{Pref}(Y),
$$

define the admissible tail space:

$$
G_h
=
\left\{
\tau\in\Sigma^{\mathbb N}:h\tau\in Y
\right\}.
$$

Define the residual behavior map:

$$
R_h:G_h\to\mathcal O
$$

by:

$$
\boxed{
R_h(\tau)=\pi(h\tau).
}
$$

The residual map records two things simultaneously:

1. which futures remain admissible after $h$;
2. how each admissible future manifests.

The domain alone describes future possibility:

$$
\operatorname{dom}(R_h)=G_h.
$$

The full map describes future possibility together with consequence.

---

## 6. Behavioral equivalence

Define two finite histories as equivalent when they induce the same residual behavior:

$$
\boxed{
h\sim_{\pi}h'
\quad\Longleftrightarrow\quad
R_h=R_{h'}.
}
$$

Equality here requires:

$$
G_h=G_{h'}
$$

and:

$$
R_h(\tau)=R_{h'}(\tau)
$$

for every admissible tail $\tau$.

The resulting equivalence class is:

$$
\boxed{
F_h=[h]_{\sim_{\pi}}.
}
$$

This is the **residual continuation state**.

It is the finite organizer in the refined ARG formulation.

The complete node is:

$$
\boxed{
W_h=(F_h,G_h).
}
$$

This gives precise meanings to the earlier finite-infinite pair:

$$
\begin{aligned}
F_h
&=
\text{minimal future-relevant organization},\\
G_h
&=
\text{space of admissible complete continuations}.
\end{aligned}
$$

---

## 7. Minimality

The residual state is minimal relative to the declared outcome map.

Suppose another representation:

$$
S:\operatorname{Pref}(Y)\to Q
$$

is behaviorally sufficient, meaning:

$$
S(h)=S(h')
\quad\Longrightarrow\quad
R_h=R_{h'}.
$$

Then $S$ cannot identify two histories that belong to different residual classes.

Therefore $S$ factors through the residual quotient:

$$
\operatorname{Pref}(Y)
\longrightarrow
\operatorname{Pref}(Y)/{\sim_{\pi}}
\longrightarrow
Q.
$$

The residual quotient contains no distinction that is irrelevant to future behavior, and every exact sufficient representation must preserve all distinctions retained by it.

Accordingly:

$$
\boxed{
F_h
=
\text{the coarsest exact future-sufficient representation relative to }(Y,\pi).
}
$$

This is not an intrinsic essence theorem.

Minimality is relative to:

- the system boundary;
- the admissible language $Y$;
- the outcome map $\pi$;
- the temporal resolution;
- the transformation class;
- the equivalence tolerance;
- the declared identity question.

---

## 8. Transition structure

Let:

$$
A(h)
=
\left\{
a\in\Sigma:G_{ha}\neq\varnothing
\right\}
$$

be the admissible next-event set.

The update rule is:

$$
\boxed{
\delta(F_h,a)=F_{ha}.
}
$$

This is well-defined when behavioral equivalence is a right congruence:

$$
h\sim_{\pi}h'
\quad\Longrightarrow\quad
ha\sim_{\pi}h'a
$$

for every event $a$ admissible from both histories.

The continuation space decomposes as:

$$
\boxed{
G_h
=
\bigsqcup_{a\in A(h)}
aG_{ha}.
}
$$

Each child is:

$$
W_{ha}=(F_{ha},G_{ha}).
$$

The raw history space forms a tree.

The residual quotient generally forms a directed graph because distinct histories may merge into the same future-relevant state:

$$
\boxed{
\text{history tree}
\longrightarrow
\text{minimal continuation-state graph}.
}
$$

The quotient graph may contain branches, merges, cycles, recurrent components, absorbing states, terminal states, and transient regions.

This is more general than the earlier recursive tree model.

---

## 9. Parent, sibling, child, and self

The earlier four node relations remain useful, but they require refinement.

### Child

$F_{ha}$ is a child of $F_h$ when $a$ is admissible and:

$$
\delta(F_h,a)=F_{ha}.
$$

### Sibling

$F_{ha}$ and $F_{hb}$ are siblings when they arise from distinct admissible events from the same parent state.

### Parent

A parent of $F'$ is any state $F$ for which:

$$
\delta(F,a)=F'
$$

for some admissible event $a$.

The quotient graph may give a state more than one parent.

### Self

A node is the complete relational pair:

$$
W=(F,G),
$$

consisting of current future-relevant organization and its admissible continuation space.

The quotient construction therefore corrects the earlier assumption that every node has one unique parent. Unique parenthood belongs to the raw history tree, not necessarily to the minimal behavioral graph.

---

## 10. Integration with ARG local-global dynamics

ARG proposes a dynamic relation between local state and global admissibility.

The residual-state construction makes that relation explicit.

Let $Y$ represent the global admissibility structure.

Let $F_t$ represent the current local future-relevant state.

Let $A(F_t)$ be the locally available next-event set induced by the global constraint.

Let $\delta(F_t,e_t)$ be the realized local transition.

Then:

$$
\boxed{
\begin{aligned}
\text{global whole}
&\longrightarrow
Y,\\
\text{local present}
&\longrightarrow
F_t,\\
\text{possible next distinctions}
&\longrightarrow
A(F_t),\\
\text{realized becoming}
&\longrightarrow
F_{t+1}=\delta(F_t,e_t).
\end{aligned}
}
$$

The whole is not modeled as a second object that externally pushes the local state.

The whole is represented through the admissibility structure that determines which transitions and continuations exist.

The local state does not independently generate every possibility. It occupies one position inside the global continuation structure.

Thus:

$$
\boxed{
\text{global structure constrains what can continue;}
\qquad
\text{local organization determines which admissible transition is realized}.
}
$$

This is the precise systems-theoretic form of ARG's one-many relation.

---

## 11. Relation to dynamic relational geometry

The residual-state construction does not replace ARG's dynamic geometry.

They answer different questions.

### Dynamic relational geometry

Dynamic relational geometry describes:

- how relational structure changes;
- how state moves through that structure;
- how dependencies alter admissibility;
- how local proposals interact with global constraints;
- how compatibility, projection, correction, and viability operate.

### Residual continuation theory

Residual continuation theory describes:

- which distinctions in the current history remain future-relevant;
- which continuations remain admissible;
- when two histories are behaviorally equivalent;
- when identity persists through transformation;
- when a bounded finite organizer exists.

The combined architecture is:

$$
\boxed{
\text{relational geometry}
\longrightarrow
\text{transition dynamics}
\longrightarrow
\text{residual behavior}
\longrightarrow
\text{operational identity}.
}
$$

The geometry determines the evolution law.

The residual quotient determines which aspects of that evolution matter to the declared identity question.

---

## 12. Operational identity

An operational identity is a residual state relative to a declared behavioral question.

At time $t$:

$$
\boxed{
I_t=F_{H_t}.
}
$$

This means:

> The identity at time $t$ is the equivalence class of all histories that leave exactly the same relevant future possibilities and consequences.

Identity is therefore neither an unchanging material core, an isolated state vector, the entire historical record, an intrinsic name, nor a metaphysical substance.

It is a relational invariant under future-behavior equivalence.

---

## 13. Persistence through change

Exact identity persistence is too strong for many changing systems.

A system may persist even though its future capacities transform.

Let:

$$
\Psi_t:R_{H_t}\to R_{H_{t+1}}
$$

be a declared lineage transformation.

Exact persistence may be defined as:

$$
\boxed{
R_{H_{t+1}}
=
\Psi_t(R_{H_t}).
}
$$

Approximate persistence may be defined using a behavioral distance:

$$
d_{\mathcal R}(R_{H_{t+1}},\Psi_t(R_{H_t}))
\leq\varepsilon.
$$

A persistence predicate can then be written:

$$
\boxed{
P_t^{(\varepsilon)}
=
\mathbf 1
\left[
d_{\mathcal R}
\left(
R_{H_{t+1}},
\Psi_t(R_{H_t})
\right)
\leq\varepsilon
\right].
}
$$

The complete lineage over $t=0,\ldots,T-1$ is:

$$
\boxed{
\mathcal P_{0:T}^{(\varepsilon)}
=
\prod_{t=0}^{T-1}P_t^{(\varepsilon)}.
}
$$

This yields a stronger ARG persistence statement:

$$
\boxed{
\text{Persistence is the lawful continuity of future-relevant relational capacities through transformation.}
}
$$

Structure, state, and dependencies are the current realization of those capacities.

Residual behavior expresses what that realization still permits, supports, or predicts.

---

## 14. Compatibility

ARG previously proposed that persistence depends on compatibility between structure and state.

The residual formulation sharpens this.

Let:

$$
B_t=(\mathcal R_t,D_t,\Gamma_t)
$$

denote the relational and constraint background.

Let $x_t$ be the realized state.

Define $R_{B_t,x_t}$ as the residual behavior generated by their joint organization.

A compatibility functional may be defined as:

$$
\kappa(B_t,x_t)
=
\mathcal Q(R_{B_t,x_t}),
$$

where $\mathcal Q$ measures a declared property such as:

- viable continuation measure;
- survival probability;
- retained behavioral dimension;
- reachable-set volume;
- predictive stability;
- resistance to perturbation;
- distance from constraint failure.

This avoids treating compatibility as an unexplained scalar.

The definition of $\kappa$ must state which property of residual behavior it measures.

---

## 15. Finite organizer existence

A bounded finite organizer does not exist for every system.

Let:

$$
Q_{\pi}
=
\operatorname{Pref}(Y)/{\sim_{\pi}}.
$$

Then:

$$
\boxed{
|Q_{\pi}|<\infty
}
$$

means that the exact future-relevant continuation structure can be represented by finitely many residual states.

If:

$$
|Q_{\pi}|=\infty,
$$

then exact future prediction requires an unbounded family of distinct states, even if every individual state has a finite description.

If residual equivalence is not computable, no effective algorithm can construct the exact organizer in general.

Therefore ARG must distinguish:

$$
\boxed{
\begin{aligned}
\text{finite-state organization}
&:\ |Q_{\pi}|<\infty,\\
\text{finitely describable but unbounded organization}
&:\ |Q_{\pi}|=\infty\text{ with computable states},\\
\text{noncomputable organization}
&:\ \sim_{\pi}\text{ is not effectively decidable}.
\end{aligned}
}
$$

This blocks the universal claim that every infinity has a bounded finite organizer.

---

## 16. Localization of possible outcomes

The continuation space and the outcome space must remain distinct.

For a residual state $F_h$, define the compatible outcome set:

$$
C_h
=
R_h(G_h)
=
\left\{
\pi(h\tau):\tau\in G_h
\right\}.
$$

When $ha$ extends $h$:

$$
G_{ha}\subseteq G_h
$$

after prefix identification, and:

$$
C_{ha}\subseteq C_h.
$$

Nestedness alone does not imply a unique outcome.

A unique actuality requires an additional separation condition, such as:

$$
\operatorname{diam}(C_{h_n})\to0.
$$

Under compactness and continuity assumptions:

$$
C_{h_0}
\supseteq
C_{h_1}
\supseteq
C_{h_2}
\supseteq\cdots
$$

may satisfy:

$$
\bigcap_{n=0}^{\infty}C_{h_n}
=
\{o\}.
$$

This yields:

$$
\boxed{
\text{finite information restricts continuation;}
\quad
\text{coding regularity determines whether outcomes localize}.
}
$$

Localization is not a consequence of determinism alone.

---

## 17. Potential and actual infinity

The framework distinguishes two mathematically different objects.

### Potential infinity

Potential infinity is the absence of a terminal continuation stage:

$$
\boxed{
\forall n\ \exists h_{n+1}\text{ extending }h_n.
}
$$

It belongs to the ongoing availability of another admissible transition.

### Actual infinity

Actual infinity is the complete mathematical object formed by the entire path space, behavior space, completion, or attractor:

$$
\boxed{
Y,\qquad
\partial\mathcal G,\qquad
\nu P,\qquad
\varprojlim X_n,
}
$$

depending on the selected formalism.

The distinction is:

$$
\boxed{
\text{potential infinity}
=
\text{indefinite extension},
}
$$

$$
\boxed{
\text{actual infinity}
=
\text{the completed space of extensions}.
}
$$

ARG must not infer from this mathematical distinction that physical reality literally contains one or both forms.

---

## 18. Closure

Closure should not be defined as the elimination of continuation.

Closure is global organization of continuation.

The residual-state graph supports several forms.

### Terminal closure

A state has no admissible continuation:

$$
A(F)=\varnothing.
$$

### Cyclic closure

A sequence returns to a prior residual state:

$$
F_{t+k}=F_t.
$$

### Recurrent closure

A trajectory repeatedly returns to a recurrent class.

### Attractor closure

Trajectories remain in or converge toward an invariant region.

### Constraint closure

The global admissibility structure remains internally consistent under every allowed transition.

Accordingly:

$$
\boxed{
\text{closure can terminate, recur, contain, or stabilize continuation}.
}
$$

It does not merely oppose infinity.

---

## 19. Non-reification conditions

The residual state is not an intrinsic nature.

It depends on the model tuple:

$$
\boxed{
\mathfrak M
=
(\Sigma,Y,\pi,\mathcal O,\mathcal T,\varepsilon),
}
$$

where:

- $\Sigma$ defines possible events;
- $Y$ defines admissible continuations;
- $\pi$ defines relevant outcomes;
- $\mathcal O$ defines the outcome space;
- $\mathcal T$ defines admissible transformations or presentations;
- $\varepsilon$ defines any approximation tolerance.

Changing this tuple can change the residual partition.

Therefore:

$$
\boxed{
F_h^{\mathfrak M}
\neq
F_h^{\mathfrak M'}
}
$$

may hold without contradiction.

The apophatic rule is:

$$
\boxed{
T\vdash\varphi(F_h)
\not\Longrightarrow
F_h=\text{absolute identity}.
}
$$

A residual state is the strongest identity justified by the declared relational question.

It is not the thing as it exists independently of every relation, scale, observer, or formalization.

---

## 20. Presentation invariance

ARG requires protection against results caused by arbitrary notation.

Let:

$$
\chi:\mathfrak M\to\mathfrak M'
$$

be an admissible presentation transformation.

Examples include simultaneous relabeling of nodes, coordinate changes, state-space isomorphisms, bounded-block recodings, graph isomorphisms, and conjugacies preserving the declared behavior.

A valid operational identity should transform covariantly:

$$
\boxed{
\chi(F_h^{\mathfrak M})
=
F_{\chi(h)}^{\mathfrak M'}.
}
$$

The residual-state graph should be preserved up to the selected equivalence:

$$
Q_{\pi}
\cong
Q_{\pi'}.
$$

Raw history length, raw alphabet size, and raw state labels are not invariant and must not be treated as intrinsic quantities.

More defensible quantities include:

- behavioral equivalence class;
- predictive information;
- residual entropy;
- geometric diameter under a declared metric;
- computational complexity under a fixed machine model;
- control energy under a specified physical model;
- graph invariants of the quotient transition structure.

---

## 21. Established substrate and ARG-specific claims

### Established substrate

The following are established mathematical patterns:

1. histories can be quotiented by equality of residual future behavior;
2. finite residual quotients correspond to finite-state recognizability in standard settings;
3. state minimization removes future-irrelevant distinctions;
4. symbolic prefixes define continuation cylinders;
5. continuous compact codings localize compatible outcomes;
6. unrestricted recursive systems may make reachability and equivalence undecidable;
7. recoding can change raw depth and alphabet size without changing behavior.

### ARG-specific synthesis

The following are project proposals:

1. use the residual quotient as ARG's operational identity layer;
2. define persistence through lawful transformation of residual behavior;
3. use global admissibility as the formal expression of whole-system constraint;
4. interpret structure-state compatibility through properties of joint residual behavior;
5. integrate presentation invariance with apophatic non-reification;
6. test whether residual-state variables add predictive value beyond state-only, structure-only, and history-only baselines.

### Claims not established

This document does not establish that:

- reality is fundamentally symbolic;
- every natural system has a finite residual organizer;
- the universe is a coalgebra or automaton;
- the global whole is a separate causal agent;
- operational identity is intrinsic identity;
- infinity is physically created by finite information;
- ARG supplies a new fundamental geometry;
- the residual quotient is unique without fixing the model tuple.

---

## 22. Falsification program

The synthesis becomes scientifically useful only if it outperforms simpler alternatives.

For a selected empirical or computational system, freeze:

$$
(\Sigma,Y,\pi,\mathcal O,\varepsilon).
$$

Construct candidate predictors using:

1. instantaneous state only;
2. relational structure only;
3. full finite history;
4. hand-designed state and memory;
5. estimated residual continuation state.

Evaluate predictive accuracy, calibration, state complexity, out-of-sample robustness, intervention response, invariance under simultaneous relabeling, failure under one-sided structure or state perturbation, and stability across scale and boundary choices.

The residual-state proposal loses support if:

1. it provides no predictive compression beyond simpler models;
2. its classes are unstable under admissible presentation changes;
3. estimated residual states fail under controlled interventions;
4. persistence criteria can be chosen only after observing the outcome;
5. state partitions change arbitrarily under minor boundary choices;
6. structure-state compatibility does not predict continuation viability;
7. the residual construction merely reproduces the full history without compression.

A falsification is a successful scientific result.

---

## 23. Minimal computational experiment

The first ARG-specific residual-state experiment should use the existing minimal three-node dynamic system rather than another continued-fraction model.

### Frozen system

Use the established three-node equations and constraint rules.

### Interventions

Generate histories under:

- fixed structure with varied initial state;
- fixed initial state with structural permutations;
- simultaneous structure-state relabeling;
- state-only relabeling;
- structure-only relabeling;
- matched null structures;
- admissibility perturbations;
- dependency perturbations.

### Outcome map

Freeze one behavior map before execution, such as:

$$
\pi(H_t\tau)
=
\left(
\text{viability time},
\text{persistence class},
\text{terminal basin},
\text{constraint violations}
\right).
$$

### Residual partition

Two histories are equivalent when their continuation response agrees for every frozen admissible intervention word within the declared horizon, or within a certified infinite-horizon abstraction when available.

### Primary test

Compare the residual-state representation against:

$$
\boxed{
\text{state only},
\quad
\text{structure only},
\quad
\text{state plus structure},
\quad
\text{full history}.
}
$$

The primary result is not whether the system is deterministic.

The primary result is whether the residual quotient provides a smaller representation with equal or better future-behavior discrimination.

---

## 24. Repository integration

This document should be integrated into ARG in the following location:

$$
\boxed{
\text{constrained local-global dynamics}
\longrightarrow
\text{residual continuation states}
\longrightarrow
\text{persistence and compatibility}.
}
$$

Recommended changes:

1. add this document under `docs/`;
2. link it from the README and roadmap;
3. add glossary entries for residual behavior, continuation state, and behavioral equivalence;
4. update the paper outline so the residual-state construction appears before persistence;
5. register the synthesis in the claims ledger as established substrate plus ARG-specific integration;
6. add presentation-invariance obligations to every residual-state experiment;
7. archive the continued-fraction experiments as illustrations and software validation, not as ARG's foundational proof.

Suggested paper section:

> **Residual Continuation States and Operational Identity**

Suggested subsection order:

1. admissible continuation space;
2. residual behavior;
3. behavioral quotient;
4. minimality;
5. transition graph;
6. persistence through transformation;
7. presentation invariance;
8. apophatic non-reification;
9. falsification design.

---

## 25. Immediate research tasks

### Task 1 — Formal consistency

Prove that $\sim_{\pi}$ is an equivalence relation.

Prove conditions under which it is a right congruence.

Specify when $\delta$ is well-defined on quotient states.

### Task 2 — ARG mapping

Map the current ARG variables:

$$
Z=(x,s,q,\theta,c)
$$

or their latest replacements into:

$$
(\Sigma,Y,\pi,\mathcal O).
$$

Do not introduce duplicate names for existing concepts.

### Task 3 — Persistence metric

Define:

$$
d_{\mathcal R}
$$

between residual behaviors.

Test exact, probabilistic, geometric, and intervention-based forms.

### Task 4 — Compatibility functional

Replace an abstract $\kappa(B,x)$ with a quantity derived from the joint residual behavior.

### Task 5 — Minimal model

Apply the construction to the three-node model.

Compute or approximate the quotient transition graph.

### Task 6 — Presentation audit

Test simultaneous relabeling, coordinate transformation, and alternative history encodings.

### Task 7 — Literature map

Compare the exact formulation with:

- Myhill-Nerode equivalence;
- bisimulation minimization;
- predictive-state representations;
- computational mechanics;
- coalgebraic behavioral equivalence;
- causal-state reconstruction;
- viability theory;
- symbolic abstractions in control.

### Task 8 — Claims ledger

Record separately:

- established theorem;
- ARG definition;
- ARG conjecture;
- computational result;
- philosophical interpretation;
- rejected overclaim.

---

## 26. Core propositions for the ARG paper

### Proposition 1 — Residual-state sufficiency

For fixed $(Y,\pi)$, the residual state $F_h$ determines the admissible continuation set and the outcome associated with every admissible continuation.

### Proposition 2 — Minimality

Every exact future-sufficient state representation refines the residual-behavior quotient.

### Proposition 3 — Transition well-definedness

If residual equivalence is a right congruence, event transitions descend to the quotient state graph.

### Proposition 4 — Finite organizer criterion

A bounded exact finite-state organizer exists if and only if the residual quotient contains finitely many equivalence classes.

### Proposition 5 — Localization under continuous coding

If the admissible path space is compact and the outcome map is continuous, sufficiently long common histories produce uniformly small compatible outcome sets.

### Proposition 6 — Non-intrinsic identity

Residual identity changes when the declared boundary, outcome map, admissibility structure, scale, or equivalence tolerance changes.

The first five propositions are grounded in established mathematical frameworks under their stated assumptions.

The sixth records the ARG interpretation and model dependence.

---

## 27. Central ARG formulation

The integrated framework can be stated as:

$$
\boxed{
\begin{aligned}
Z_t
&=
\text{current relational realization},\\
Y
&=
\text{global admissible continuation structure},\\
R_{H_t}
&=
\text{future behavior remaining after the current history},\\
F_t
&=
[H_t]_{\sim_{\pi}},\\
G_t
&=
\operatorname{dom}(R_{H_t}),\\
W_t
&=
(F_t,G_t),\\
F_{t+1}
&=
\delta(F_t,e_t).
\end{aligned}
}
$$

Persistence is:

$$
\boxed{
\text{lawful continuity of }R_{H_t}\text{ through transformation}.
}
$$

Operational identity is:

$$
\boxed{
\text{the minimal present distinction required to preserve relevant future behavior}.
}
$$

Apophatic restraint is:

$$
\boxed{
\text{operational identity is not absolute identity}.
}
$$

---

## 28. Plain-English conclusion

A thing does not persist because an invisible substance remains unchanged.

It persists when its changing relational organization continues to preserve the capacities, constraints, and possible behaviors that define the identity question being asked.

The finite organizer is not the whole past. It is the smallest present summary that retains everything from the past that can still make a difference to the future.

The infinite side is not an object stored inside that organizer. It is the complete field of continuations still permitted from it.

Apophatic Relational Geometry can therefore connect becoming to identity without reifying either one:

> A present relational state is an operational identity only relative to the futures it can still sustain, and no such operational identity is the final nature of the thing.

---

## 29. Recommended project decision

Adopt residual continuation states as the formal bridge between ARG dynamics and ARG persistence.

Do not present the construction as a new foundational mathematics of infinity.

Use it to:

- remove future-irrelevant historical detail;
- define operational identity;
- formalize persistence through change;
- connect local state to global admissibility;
- enforce presentation invariance;
- design discriminating experiments;
- preserve the apophatic refusal to identify a successful model with ultimate reality.

The strongest justified project statement is:

$$
\boxed{
\begin{gathered}
\text{A dynamic relational system may admit a minimal future-relevant quotient state.}\\
\text{That state can operationalize identity and persistence relative to declared}\\
\text{continuation, outcome, scale, and transformation structures.}
\end{gathered}
}
$$

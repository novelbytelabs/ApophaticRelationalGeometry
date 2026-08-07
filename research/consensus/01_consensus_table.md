# CS1 Preliminary Consensus Table

## Status

> **THREE SOURCE BASKETS ENTERED — not a completed consensus determination.**

This table records conclusions supported by the first thirteen source notes. Grades may be revised after broader primary-source coverage, counterexample review, equation-level comparison, and independent audit.

## Preliminary findings

| Claim ID | Scoped statement | Preliminary grade | Evidence entered | ARG implication | Residual |
|---|---|---:|---|---|---|
| CS1-C01 | In a specified dynamical model, the realized trajectory depends on the transition law or propagator and the initial condition. | C4 | Schmid 2007; Kalman 1963; standard initial-value formulation | Not novel. Replace broad discovery language with established terminology. | Nonlinear, changing-structure predictors must still be compared with standard methods. |
| CS1-C02 | The same operator can amplify, suppress, or transform different initial states; in non-normal systems finite-time behavior may not be inferred from eigenvalues alone. | C4 | Schmid 2007 | ERO cancellation and state-dependent persistence are established neighboring mechanisms, not a general ARG discovery. | Determine whether ARG adds a predictor beyond propagator, singular-vector, pseudospectral, basin, transfer-operator, or control analysis. |
| CS1-C03 | Linear finite-time amplification, control energy, and output sensitivity can be expressed through propagators and controllability or observability Gramians relative to a specified norm, input map, output map, and horizon. | C4 | Schmid 2007; Kalman 1963; Moore 1981 | “Compatibility” must be mapped to standard modal, nonmodal, controllability, and observability quantities before new terminology is retained. | Compare any ARG quantity directly with finite-horizon propagator and Gramian measures. |
| CS1-C04 | In nonlinear systems, long-term or finite-time persistence may depend on basin location, invariant-manifold organization, metastable-set retention, structural stability, accessibility geometry, observability geometry, and viable or invariant sets. These are established but distinct mechanisms. | C4 within their scoped mathematical domains | Menck et al. 2013; Fenichel 1971/72; Froyland and Padberg 2009; Smale 1967; Hermann and Krener 1977; Saint-Pierre 1994; Blanchini 1999 | The broad claim is not novel. ARG must specify which nonlinear mechanism it means rather than treating “compatibility” as one undifferentiated cause. | Slow manifolds, bifurcation, noise-driven escape, stochastic control, and topology-changing cases require additional sources. |
| CS1-C05 | State–system interaction is already decomposed into reachability, observability, joint controllability–observability importance, accessibility, viability, and controlled invariance. These quantities can predict behavior beyond state-only or autonomous-operator-only summaries, but they answer different questions. | C4 for scoped linear and control-theoretic results; C3–C4 for nonlinear local criteria | Kalman 1963; Moore 1981; Hermann and Krener 1977; Saint-Pierre 1994; Blanchini 1999 | The general interaction principle is established. ARG must not rename these quantities as one new law. | Determine whether a useful cross-framework schema survives without falsely collapsing the distinctions. |
| CS1-C06 | The placement and number of internal state variables can vary between realizations; unreachable and unobservable variables may be representational redundancy for a declared input/output question. The wider boundary among state, structure, parameters, rules, and environment remains criterion-dependent. | C4 for linear minimal realization; C3 for the broader cross-field statement | Kalman 1963; Moore 1981; Weatherall 2019; adaptive-network augmentation issue | The state–structure split must be presented as a modeling factorization unless an invariant distinction is proved. | Define admissible formulations and preserved content for concrete ARG models. |
| CS1-C07 | Empirical equivalence, minimal input/output realization, balanced similarity, definitional equivalence, categorical equivalence, interpretational equivalence, and dynamical conjugacy are different claims. | C3–C4 | Kalman 1963; Moore 1981; Weatherall 2019; Smale 1967 | ARG must not treat equal outputs, minimal realization, coordinate balancing, conjugacy, and ontological identity as interchangeable. | Select appropriate equivalence criteria and preserved observables for each ARG claim. |
| CS1-C08 | A representation-robust claim must specify admissible transformations and preserved structure. Topological conjugacy, similarity transformations, and balanced input/output invariants preserve different content and do not license arbitrary nonlinear recoding. | C3–C4 | Moore 1981; Weatherall 2019; Smale 1967 | “No privileged presentation” requires formal invariance or covariance statements, not a slogan. | Add gauge, quotient, symplectic, measure-preserving, and observational-equivalence sources before freezing the ARG criterion. |
| CS1-C09 | When state spaces vary through a specified compatible family, pushforward and pullback maps provide explicit cross-time transport and support material derivatives. | C4 | Alphonse, Elliott, and Stinner 2015 | The general transport requirement and composition law are established mathematics. | Abrupt, noninvertible, dimension-changing, and semantically ambiguous changes require other frameworks. |
| CS1-C10 | Source and destination spaces do not by themselves supply the particular pushforward family, control policy, output map, or constraint semantics needed to compare and preserve states. | C3–C4 within audited frameworks | Alphonse, Elliott, and Stinner 2015; Kalman 1963; Saint-Pierre 1994; Blanchini 1999 | ARG must specify transport and scientific context as model structure rather than imply they follow automatically from the fibers. | Add connection, hybrid-reset, remapping, graph-correspondence, and gauge sources. |
| CS1-C11 | Modal energy growth, basin return, invariant-manifold continuation, metastable-set retention, structural stability, reachability, observability, viability, positive invariance, and controlled invariance are mathematically inequivalent notions of persistence, access, or preservation. | C4 within audited mathematics; C3 as a cross-field generalization | All thirteen source notes | ARG must stop using “persistence” or “compatibility” without a typed predicate, observable, control context, equivalence criterion, and horizon. | Information, recoverability, function, biological identity, and lineage persistence remain to be audited. |
| CS1-C12 | A persistence or continuation criterion is relative to declared observables, norms or measures, input and output maps, admissible controls, constraints, disturbance classes, equivalence relations, perturbation classes, and time horizons. | C3–C4 | Schmid 2007; nonlinear basket; Kalman 1963; Moore 1981; Hermann and Krener 1977; Saint-Pierre 1994; Blanchini 1999; Weatherall 2019 | No single unqualified persistence score is licensed. The bare pair $(B,x)$ is insufficient for many scientific questions. | Determine a minimal typed context schema and which dependencies can be invariantly abstracted. |
| CS1-C13 | “State–structure compatibility” may be useful as an umbrella schema for several relational quantities, but current evidence supports a typed family rather than one established invariant or scalar across fields. | C1 | Synthesis inference from thirteen notes | Retain only as provisional synthesis language; never present it as one discovered law. | Test whether a common categorical or operational schema exists after information, biology, philosophy, gauge, and hybrid-system baskets. |
| CS1-C14 | No ARG-specific representation-robust theorem, prediction, control law, invariant set, or model-reduction result has yet been isolated beyond established neighboring frameworks. | C0 / unverified | Current source baskets | No novelty language licensed. | Complete CS1 and direct equation/equivalence comparisons. |

## Consensus extraction after three baskets

The entered evidence supports the following minimal statements:

1. **Realized behavior is model-and-state relative.** A transition law defines possible evolution, while a particular initial condition selects a realized trajectory.
2. **Finite-time behavior can be strongly state-dependent.** In non-normal systems, disturbance orientation and mode interference can dominate short-horizon amplification or decay.
3. **Nonlinear outcome depends on global and local phase-space organization.** Basin geometry, invariant manifolds, metastable sets, accessibility distributions, and viability regions answer distinct questions.
4. **Organization can persist without pointwise state preservation.** Invariant manifolds, almost-invariant sets, and invariant regions formalize different forms of organized continuation.
5. **Intervention is relational.** Controllability and accessibility depend jointly on dynamics, state, available input directions, constraints, and horizon.
6. **Observation is relational.** Observability depends jointly on dynamics, state distinctions, output maps, and horizon.
7. **Joint state importance is established in scoped settings.** Balanced realization ranks directions by joint controllability and observability rather than by coordinate magnitude or state membership alone.
8. **Constrained continuation is policy-relative.** Viability and controlled invariance ask whether an admissible trajectory or control can keep a state within a declared set.
9. **Autonomous and corrected persistence differ.** Positive invariance, robust invariance, and controlled invariance must not be conflated.
10. **State and relational structure may coevolve.** This is standard in adaptive-network science and does not by itself distinguish ARG.
11. **Changing state spaces require explicit identification machinery.** Compatible pushforward and pullback maps are one established solution for smoothly evolving spaces.
12. **Representation equivalence is not one relation.** Input/output realization, balancing, conjugacy, formal equivalence, and interpretive equivalence preserve different content.
13. **Persistence is a family, not a primitive scalar.** The audited literature distinguishes norm retention, basin return, invariant-set continuation, ensemble retention, qualitative conjugacy, viability, and invariance under control.
14. **No universal ARG compatibility scalar has been established.** The evidence supports a typed family of mathematical relations, not one field-independent invariant.

## Typed quantity discipline

Until CS1 is complete, project documents should use typed terms wherever possible:

$$
P_{\mathrm{norm}},\quad
P_{\mathrm{basin}},\quad
P_{\mathrm{manifold}},\quad
P_{\mathrm{retain}},\quad
P_{\mathrm{structural}},\quad
R_{\mathrm{reachable}},\quad
O_{\mathrm{observable}},\quad
I_{\mathrm{balanced}},\quad
P_{\mathrm{viable}},\quad
P_{\mathrm{invariant}},\quad
P_{\mathrm{controlled}}.
$$

These labels do not assert commensurability. They prevent accidental movement between distinct scientific claims.

## Preliminary formalism impact

For a purely autonomous trajectory question, a model may be written schematically as

$$
Q_t=(B_t,x_t),
\qquad
x_{t+1}=F_{B_t}(x_t).
$$

But many scientific questions require an extended typed context such as

$$
\mathcal S=
(\mathcal X,F,B_{\mathrm{in}},C_{\mathrm{out}},K,\mathcal U,\mathcal W,\Phi,T),
$$

where $B_{\mathrm{in}}$ is an input map, $C_{\mathrm{out}}$ an output map, $K$ a constraint set, $\mathcal U$ admissible controls, $\mathcal W$ disturbances, $\Phi$ the measured persistence or performance functional, and $T$ the horizon.

This is a preliminary methodological correction, not a final ARG ontology.

## Prohibited inference from this table

This preliminary synthesis does **not** establish that:

- reality is fundamentally a structure–state pair;
- all persistence is spectral, basin-based, manifold-based, probabilistic, viable, invariant, or controlled persistence;
- controllability implies observability, or either implies identity;
- balanced state importance is metaphysical importance;
- one compatibility measure unifies linear, nonlinear, biological, informational, and philosophical persistence;
- an invariant manifold or controlled-invariant set is an enduring physical object;
- topological conjugacy or input/output equivalence establishes physical or ontological equivalence;
- transport is unique;
- adaptive networks or control theory prove a relational ontology;
- ARG has no possible contribution after the full audit.

## Next source baskets

1. connections and parallel transport;
2. hybrid resets, noninvertible morphisms, remeshing, and graph matching;
3. dynamical conjugacy, gauge, quotient, and surplus structure;
4. information preservation, sufficient statistics, causal states, and recoverability;
5. biological organizational persistence and turnover;
6. philosophical identity through change, structural realism, and process ontology;
7. remaining nonlinear gaps: slow manifolds, bifurcation, local contraction, stochastic viability, and noise-driven escape.

## Promotion rule

No row may enter the Minimal ARG Core until its primary-source base, exceptions, cross-field translation, and representation audit have been independently reviewed.

## Basket completion record

CS1 basket 3 was completed on branch `agent/consensus-synthesis-roadmap` with source notes for Kalman 1963, Moore 1981, Hermann and Krener 1977, Saint-Pierre 1994, and Blanchini 1999. No experiment was run or authorized.

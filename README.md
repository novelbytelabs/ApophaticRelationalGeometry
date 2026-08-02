# Apophatic Relational Geometry

> **Status: candidate synthesis — not a claim of a new fundamental geometry.**

> **Phase 6B.0:** Phase 6A.2 passed external re-audit and the defensive-hardening candidate was merged. The execution substrate is cleared, but the development pilot remains unexecuted and blocked until a separate committed authorization binds the exact accepted audit-report SHA-256. Confirmatory execution remains blocked.

ARG investigates whether nonlinear local dynamics, adaptive relations, state-dependent geometry, endogenous collective feedback, and explicit admissibility projection can form a coherent and scientifically useful framework. Mathematical novelty, physical relevance, and explanatory value remain open.

## Implemented four-model family

### $M_0$ — local/adaptive baseline

Local nonlinear dynamics, neighbor coupling, adaptive edge activation, and metric deformation, with no collective statistic entering a transition equation.

### $M_F$ — collective feedback

$$
c(x)=\frac13\sum_{i=1}^{3}x_i^2,
\qquad
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

Licensed description:

> **implemented prototype-level downward feedback/constraint with adaptive relational geometry**

This does not establish macro-level causal autonomy.

### $M_P$ — projected admissibility

Contract v1.0 implements

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
\qquad
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

### $M_{FP}$ — feedback followed by projection

$$
F_{\mathrm{proposal}}=F_0+F_F
$$

is followed by the same node projection and retraction policy as $M_P$. At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

because the node-feedback term is radial and $P_Tx=0$. This is not trajectory equivalence: $M_{FP}$ retains feedback in $s$ and $q$, which can change later conductances and node proposals.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

No implemented result establishes scientific superiority, physical adequacy, strong emergence, macro-level causal autonomy, mathematical novelty, or a fundamental geometry.

## Audit status

Phase 6A.2 closed the material defensive-integrity defects found by the earlier audit. The exact candidate `17a17398808cae1befe85e795d371012fe999f03` passed the ordinary suite, hardened tripwire, full-horizon numerical gate, and external re-audit, then merged as `4fb987b34220927466812f0276e10bb0776c28fd`.

The accepted re-audit packet SHA-256 is:

```text
5d524253f24f31893ce44e1be4a0de1fa3ab9ae2f87812ee2d35416ac5ca84fd
```

This clears the runner remediation gate. It does not create a pilot result or authorize confirmatory access.

## Current execution state

$$
\boxed{
\text{Phase 6A.2 externally cleared};
\quad
\text{development pilot not executed};
\quad
\text{execution authorization absent};
\quad
\text{confirmatory execution blocked}.
}
$$

The next authorization commit must bind the exact accepted external audit-report SHA-256. No placeholder or self-authored substitute is permitted.

## Integrity rules

- no oracles, hardcoded scientific outputs, golden trajectory replay, hidden fixtures, or test-mode model branches;
- no threshold, parameter, configuration, split, or outcome-rule change after outcome inspection;
- tests must target invariants, independent references, metamorphic properties, failure behavior, and provenance;
- failed runs remain failures and are never imputed;
- a fresh audit bundle must validate itself after clean extraction;
- execution requires a separate committed record binding the accepted external audit report, exact runner source, frozen scope, and archive destination.

## Repository map

### Foundations

- `docs/00_scope_and_status.md`
- `docs/01_apophatic_meta_axiom.md`
- `docs/02_design_requirements.md`
- `docs/03_formalism.md`
- `docs/04_minimal_model.md`
- `docs/05_proof_obligations.md`
- `docs/06_experimental_plan.md`

### Research grounding and execution

- `docs/07_research_grounding_plan.md`
- `docs/08_claim_ledger.md`
- `docs/09_novelty_matrix.md`
- `docs/10_literature_landscape.md`
- `docs/11_benchmark_specification.md`
- `docs/12_falsification_criteria.md`
- `docs/13_alignment_and_claim_ceiling.md`
- `docs/14_roadmap.md`
- `docs/15_four_model_design_contract.md`
- `docs/16_phase3_mp_verification.md`
- `docs/17_phase4_mfp_verification.md`
- `docs/18_phase5_comparative_protocol.md`
- `docs/19_phase5_protocol_verification.md`
- `docs/20_phase6_runner_design.md`
- `docs/21_phase6_runner_verification.md`
- `docs/22_phase6a1_integrity_remediation.md`
- `docs/23_phase6b_clearance_and_authorization.md`

### Implementation and tests

- `src/apophatic_geometry/model.py` — core state, geometry, and original $M_F$ path.
- `src/apophatic_geometry/models.py` — canonical four-model equations and RK4.
- `src/apophatic_geometry/protocol.py` — metrics, strict manifest loading, root-confined locks, and decisions.
- `src/apophatic_geometry/attestation.py` — source/runtime attestation derived from the execution substrate.
- `src/apophatic_geometry/simulate.py` — exploratory simulator with atomic completion-attested output.
- `src/apophatic_geometry/pilot.py` and `pilot_*` — gated pilot-only machinery; execution requires a hash-bound authorization record.

## Data-free validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
arg-pilot validate --repo-root .
arg-pilot plan --repo-root .
```

These commands do not establish a scientific result.

## Research maxim

> Separate the mechanisms. Freeze the contracts. Test the alternatives. Reify nothing.

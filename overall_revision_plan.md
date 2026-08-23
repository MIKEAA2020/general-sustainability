# Overall Revision Plan
## Integrating the revised big-picture architecture and both parallel architectural audits

**Project:** *Toward a General Theory of Sustainability*  
**Date:** 14 August 2026

## 1. Revision objective

The revision should preserve the manuscript’s scientific ambition and top-down method. It need not solve every domain model, prove every conjecture, compute every viability kernel, or supply a universal moral theory. It must, however, stabilize the interfaces to which those future developments will attach.

The revised manuscript will therefore present:

> **A candidate architectural kernel and composition language for a general theory of sustainability.**

Its contribution is to identify the objects, judgment types, operators, interfaces, transformation mechanisms, and proof obligations that a mature general theory would require. Established mathematics, architectural commitments, conjectures, templates, placeholders, and open problems will be visibly distinguished.

The title *Toward a General Theory of Sustainability* remains appropriate. “Toward” communicates that this is an ambitious research programme rather than a completed universal law.

---

## 2. Revised central thesis

The current slogan—“sustainability is robust controlled invariance of an explicitly valued, causally closed, augmented state space”—is too narrow and contains a category error. Controlled invariance applies within a fixed architecture; transformation changes the architecture. Causal adequacy concerns a model boundary and its interfaces, not a state space.

The replacement thesis is:

> **Sustainability concerns the continued availability of physically feasible, functionally viable, normatively admissible, and relationally responsible trajectories within and across the possible transformations of interdependent systems, under declared boundaries, disturbances, horizons, and implementable actions.**

In compressed architectural form:

\[
\boxed{
\begin{aligned}
\text{Sustainability architecture}
={}&\text{typed admissible viability}\
&+\text{within-architecture invariance}\
&+\text{between-architecture transformation}\
&+\text{interdependent and commons-aware composition}\
&+\text{boundary-interface adequacy}\
&+\text{prospectively specified identity and legitimacy}.
\end{aligned}}
\]

Controlled invariance remains the mathematical core of within-architecture functional viability. It is no longer presented as the entire theory.

---

## 3. The stable formal spine

### 3.1 Frozen sustainability specification

Every assessment begins with a prospectively declared specification:

\[
\Omega=(S,z_0,I^H,I^L,\mathcal V,B,\mathscr C,W,T,\mathcal N,\mathcal R_A),
\]

where:

- \(S\): focal system;
- \(z_0\): actual initial state or initial-state uncertainty set;
- \(I^H\): protected higher-order identity predicates;
- \(I^L\): lower-level identity features that may change under declared conditions;
- \(\mathcal V\): protected functions and values;
- \(B\): provisional model boundary;
- \(\mathscr C\): typed constraint registry;
- \(W\): disturbance and uncertainty class;
- \(T\): assessment horizon;
- \(\mathcal N\): normative authority, procedure, and provenance;
- \(\mathcal R_A\): permitted architecture-change and specification-revision rules.

The specification is observer- and purpose-relative by design. The architecture makes those choices explicit and auditable rather than pretending to eliminate them.

#### Specification locking rule

The principal identity predicates, normative authority, horizon, and protected values must be frozen before the assessment result is known. Revising them creates a new specification \(\Omega'\); it cannot retroactively change the result obtained under \(\Omega\).

This does not prevent legitimate learning. It prevents after-the-fact retargeting.

---

### 3.2 Architecture registry

A system architecture is

\[
\mathcal A_q=(Z_q,F_q,U_q^{\mathrm{impl}},B_q,I_q,\mathscr C_q,\partial_q),
\]

where:

- \(Z_q\): state space;
- \(F_q\): dynamics or transition correspondence;
- \(U_q^{\mathrm{impl}}\): actually implementable action set;
- \(B_q\): architecture-specific boundary;
- \(I_q\): architecture-specific identity realization;
- \(\mathscr C_q\): applicable constraints;
- \(\partial_q\): boundary interfaces.

Let

\[
\mathbb A=\{\mathcal A_q:q\in Q\}
\]

be the registry of recognized or conjectured architectures. The registry is an explicit placeholder: it need not be complete in the first manuscript.

---

### 3.3 One typed constraint registry

The manuscript should not maintain two unexplained decompositions of \(K\). It should maintain one source of truth:

\[
\mathscr C=\{c_1,\ldots,c_m\}.
\]

Each constraint is a structured record:

\[
c_j=(p_j,\tau_j,s_j,\rho_j,\nu_j,\kappa_j,g_j,h_j),
\]

where:

- \(p_j\): predicate or bound;
- \(\tau_j\): physical, functional, normative, relational, or epistemic type;
- \(s_j\): subject—state, capacity, supporting system, distribution, liability, or interface;
- \(\rho_j\): provenance and evidential status;
- \(\nu_j\): substitutability rule;
- \(\kappa_j\): reversibility, criticality, and priority;
- \(g_j\): affected group or system;
- \(h_j\): applicable horizon.

Typed projections are derived from this registry:

\[
K_P=\bigcap_{\tau_j=P}\{z:p_j(z)\},
\qquad
K_F=\bigcap_{\tau_j=F}\{z:p_j(z)\},
\]

with corresponding \(K_N\) and \(K_R\). A combined target geometry can remain:

\[
K^*=K_P\cap K_F\cap K_N\cap K_R,
\]

but its components remain semantically typed.

Physical constraints, functional thresholds, rights, and relational obligations may all constrain a final judgment without being treated as the same kind of fact.

---

### 3.4 Typed judgment vector

The framework should return a typed result rather than only “inside” or “outside” \(K^*\):

\[
\mathbf J_\Omega(\tau)
=
\bigl(P_\Omega(\tau),F_\Omega(\tau),N_\Omega(\tau),R_\Omega(\tau)\bigr),
\]

where:

- \(P\): physical feasibility;
- \(F\): functional viability;
- \(N\): normative admissibility;
- \(R\): relational responsibility and non-displacement.

Qualified sustainability is the conjunction

\[
\operatorname{QSust}_\Omega(\tau)
=
P_\Omega(\tau)
\land F_\Omega(\tau)
\land N_\Omega(\tau)
\land R_\Omega(\tau).
\]

This preserves a unified assessment while distinguishing impossibility, collapse, injustice, and externalization.

Physical feasibility may partly be enforced by the domain of \(F_q\) itself. Physical constraints remain in the register for model validation, approximate coupling, data consistency, and explicit provenance.

---

## 4. Two official operators

### 4.1 Operator I: within-architecture viability

For a fixed architecture \(\mathcal A_q\), define the viability kernel over horizon \(T\):

\[
\operatorname{Viab}_{\mathcal A_q}(K^*,W,T;U_q^{\mathrm{impl}}).
\]

The actual assessment is

\[
z_0\in
\operatorname{Viab}_{\mathcal A_q}(K^*,W,T;U_q^{\mathrm{impl}}),
\]

not merely that the kernel is nonempty. Kernel non-emptiness means some initial condition is viable; current-state membership means the focal system is viable from its actual condition.

Operator I covers:

- regulation;
- buffering;
- ordinary maintenance;
- restoration within the same architecture;
- parameter adaptation;
- robust control.

### 4.2 Operator II: architecture transformation

Let \(E_A\subseteq Q\times Q\) be permitted architecture transitions. A transition has the form

\[
(q,z)
\longrightarrow
\left(q',R_{qq'}(z)\right),
\]

where \(R_{qq'}\) translates:

- physical stocks;
- capacities;
- liabilities;
- obligations;
- affected populations;
- protected functions;
- identity predicates.

A transformation is a hybrid reach–avoid–maintain problem whose destination is a viable region of \(\mathcal A_{q'}\). It must satisfy:

- transition constraints;
- cumulative-harm budgets;
- irreversibility restrictions;
- identity-continuity predicates;
- normative and procedural requirements.

Kernel emptiness in \(\mathcal A_q\) establishes only that Operator I cannot succeed under the frozen specification. It does not prove that transformation is possible. The remaining outcomes are:

1. a valid transformation exists;
2. no valid transformation is currently known;
3. sustainability is impossible within the recognized architecture registry;
4. the specification is legitimately revised, creating a new assessment.

### 4.3 Local versus structural corridor failure

If

\[
a_{\min}(z)>a_{\max}(z)
\]

at the present state, the result is local infeasibility. Architectural transformation is required only when no admissible within-architecture path can reach a state with a nonempty corridor before a forbidden state is entered.

---

## 5. Identity continuity and legitimacy

### 5.1 Identity hierarchy

Higher-order identity \(I^H\) is frozen under \(\Omega\). Lower-order identity \(I^L\) may change through predeclared transition rules.

A transformation must satisfy

\[
\mathcal C_I(q,z;q',z')=1,
\]

where \(\mathcal C_I\) is the prospectively declared continuity relation.

The theory does not determine the universally correct identity. It requires that the identity, authority, and revision process be explicit.

### 5.2 Normative authority

The slot \(\mathcal N\) records:

- who selected the normative constraints;
- which procedure was used;
- which populations were represented;
- which rights are non-revisable;
- how disputes and revisions are handled.

The framework does not solve the dictatorship example by deriving justice from dynamics. It makes clear whether an assessment uses the dictator’s specification, a constitutional specification, a human-rights standard, or another declared authority. Competing specifications can then be compared rather than conflated.

---

## 6. Boundary-interface adequacy

“Causal closure” and “causally closed state space” should be removed.

The replacement is:

> **Boundary-interface adequacy:** Every decision-relevant influence crossing the model boundary is internalized, represented by a typed interface assumption, bounded by a disturbance or scenario envelope, or accompanied by an explicit negligibility claim and sensitivity bound.

Each interface may be represented as

\[
C_e=(A_e,G_e,W_e,\epsilon_e,E_e),
\]

where \(A_e\) is an assumption, \(G_e\) a possible guarantee, \(W_e\) a disturbance envelope, \(\epsilon_e\) accepted error or failure probability, and \(E_e\) supporting evidence.

Not every environment supplies a guarantee. Boundary records may instead contain adversarial bounds, scenarios, or explicit unknowns.

Boundary adequacy is a proof obligation relative to a proposition and confidence level. It is not a claim of metaphysical completeness.

---

## 7. Typed dependency hypergraph and commons

A dyadic graph is insufficient. Use a typed directed hypergraph whose edge classes include:

1. obligatory support;
2. optional or substitutable support;
3. harmful impact;
4. mere nesting;
5. shared-source dependence;
6. shared-sink contribution.

This resolves the apparent conflict between recursion and sacrifice. Mere inclusion of subsystem \(B\) inside \(A\) does not automatically protect \(B\). An obligatory, impact, or normative edge creates a declared constraint or interface obligation.

### 7.1 Commons node

For shared commons \(C\), aggregate burden is

\[
L_C
=
\mathcal L_C\bigl(\{z_i,a_i\}_{i\in N_C}\bigr),
\]

where \(\mathcal L_C\) may be nonlinear. The commons constraint is

\[
L_C\le C_C.
\]

A normative or institutional allocation procedure assigns actor budgets \(b_i\). An actor may be relationally noncompliant when

\[
l_i>b_i
\]

even if its individual contribution is not threshold-pivotal.

Possible allocation principles—equality, historical responsibility, capacity, benefit, need, vulnerability, or negotiated rules—remain explicit normative placeholders.

---

## 8. Typed contract architecture

Contract modality attaches to individual relations, not entire domains. The registry supports:

### Deterministic

\[
A\Rightarrow_{det}G.
\]

### Robust or set-valued

\[
A\Rightarrow_{rob}G(W).
\]

### Probabilistic

\[
A\Rightarrow_{prob}
\Pr(G\mid A,M)\ge1-\epsilon.
\]

### Strategic

\[
A\Rightarrow_{strat}
G\in\operatorname{Eq}(A,\Theta).
\]

### Scenario-only

An assumption or scenario is recorded without claiming a guarantee.

Compatibility is type-aware. A deterministic downstream requirement cannot silently rely on a probabilistic upstream relation. A buffer, redundancy, fallback, or accepted failure probability must bridge the modalities.

The first manuscript need not solve general contract synthesis. It should state a **Compositional Sustainability Conjecture**:

> Under identifiable compatibility, timing, robustness, and boundary-interface conditions, locally verified typed contracts can establish a jointly viable system behavior without complete monolithic verification.

The compositional object should be an invariant set, viable tube, compatible behavior, or strategy profile—not necessarily a stationary fixed point.

---

## 9. Time, control, and resilience

### 9.1 Horizon typing

Every primary claim is indexed by \(T\). Infinite-horizon claims use a distinct object:

\[
\operatorname{Sust}_\infty.
\]

Average-balance and indefinite-growth lemmas apply only to that object or to sufficiently large finite horizons under explicit additional assumptions.

Latent liabilities are a modelling device for some deferred harms. They are not presumed to reduce all intergenerational obligations to one scalar.

### 9.2 One control hierarchy

Define once:

\[
U_{\mathrm{impl}}
\subseteq
U_{\mathrm{inst}}
\subseteq
U_{\mathrm{tech}}
\subseteq
U_{\mathrm{theor}}.
\]

Operator I uses \(U_{\mathrm{impl}}\). Operator II may change that set. Strategic actors, power, authority, and legitimacy help determine why technically possible actions are not implementable.

### 9.3 Two resilience terms

To avoid overwriting established ecological usage:

- **Dynamical/ecological resilience:** persistence of a regime or declared functional identity under disturbance.
- **Sustainability robustness:** persistence of the complete typed sustainability judgment under disturbance.

An undesirable regime may possess dynamical resilience but not sustainability robustness.

---

## 10. Official box taxonomy

The manuscript should visibly distinguish:

### Definition

An official meaning used throughout.

### Well-formedness rule

A requirement for a valid sustainability claim.

### Interface principle

A rule governing boundaries, contracts, controls, or dependency edges.

### Conditional lemma

A consequence under an explicit stock, delay, intensity, capacity, or topology signature.

### Conjecture

An open formal or empirical claim.

### Template

A reusable specification, contract, certificate, substitution test, or diagnostic form.

### Placeholder module

A required component whose internal theory is intentionally unresolved.

### Proof obligation

A condition future work must discharge before a stronger claim can be asserted.

### Instantiation sketch

A domain example used to display interfaces and possible mechanisms, not to demonstrate validation.

### Limitation

A declared boundary on current claims.

Under this taxonomy:

- the present Axioms 2 and 4 merge into Operator I’s definition;
- Axiom 1 becomes a well-formedness rule;
- Axiom 3 becomes the boundary-interface principle;
- stock, rate, buffer, delay, and growth results become conditional lemmas;
- the canonical ODE system becomes an instantiation sketch;
- contract composition remains a conjecture and proof obligation;
- certification Levels 0–2 become assessment-maturity or preflight levels.

---

## 11. Output portfolio

The framework should produce a portfolio rather than only one binary verdict:

1. physical-feasibility result;
2. functional viability result;
3. normative-admissibility result;
4. relational and commons-allocation result;
5. current-state viability-kernel membership;
6. robustness margin;
7. transformation-path status;
8. boundary-interface adequacy statement;
9. unresolved assumptions and proof obligations;
10. evidence and confidence grade.

Possible overall classifications include:

- sustainable within the current architecture;
- viable but normatively inadmissible;
- physically feasible but functionally nonviable;
- relationally noncompliant;
- transitionally sustainable through a declared architecture path;
- locally infeasible but recoverable within the architecture;
- structurally infeasible within known architectures;
- indeterminate because of unresolved interfaces or evidence.

---

## 12. Revised manuscript structure

### Part I — The architectural problem

1. Motivation and scope
2. Existing traditions and the missing architecture
3. Contribution type and epistemic discipline

### Part II — The formal spine

4. Sustainability specification \(\Omega\)
5. Architecture registry \(\mathbb A\)
6. Typed constraint registry \(\mathscr C\)
7. Typed judgment vector
8. Operator I: within-architecture viability
9. Operator II: transformation

### Part III — Composition and embeddedness

10. Boundary-interface adequacy
11. Typed dependency hypergraphs
12. Commons nodes and allocation
13. Typed contracts
14. Compositional Sustainability Conjecture

### Part IV — Derived diagnostics

15. Capacity, load, slack, buffers, and delay
16. Conditional stock and growth lemmas
17. Adaptation, restoration, transition, and transformation
18. Dynamical resilience and sustainability robustness
19. Scale and horizon typing

### Part V — Templates and research programme

20. Canonical instantiation sketch
21. Certificate and assessment-maturity templates
22. Proof obligations and conjectures
23. Empirical programme
24. AI-assisted theory-development protocol
25. Limitations and research agenda

### Appendices

- constraint-register template;
- specification template;
- typed contract template;
- identity-continuity template;
- boundary-interface register;
- commons-allocation template;
- claim ledger;
- diagnostic workflow.

Traceability remains a separate companion document.

---

## 13. Revision sequence

### Phase 1 — Rebuild the spine

- Replace the original slogan.
- Introduce \(\Omega\), \(\mathbb A\), and \(\mathscr C\).
- Establish the typed judgment vector.
- Define the two operators.
- Freeze identity and control at official layers.

### Phase 2 — Reconnect existing material

- Attach stocks, capacities, distributions, and liabilities to the constraint registry.
- Convert causal closure into boundary-interface adequacy.
- Convert dependency graphs into typed hypergraphs.
- Add commons nodes.
- Type all module contracts.

### Phase 3 — Reclassify claims

- Remove redundant axioms.
- Relabel elementary results as conditional lemmas.
- Relabel the composition statement as an interface principle and conjecture.
- Distinguish templates, placeholders, and proof obligations.
- Apply epistemic tags consistently.

### Phase 4 — Preserve and discipline anticipation

- Retain uncalibrated domain models as instantiation sketches.
- Retain conjectures in designated boxes.
- Retain social, governance, power, observability, and measurement modules as placeholders.
- State what future work must prove, estimate, or validate.

### Phase 5 — Later validation

- Prove at least one sound composition result under restricted conditions.
- Develop one hybrid architecture-change example.
- Compute one viability kernel or approximation.
- Test one commons-allocation case.
- Compare predictive or diagnostic performance with simpler models.

Only Phase 5 requires low-level development. Phases 1–4 are the immediate architectural revision.

---

## 14. Permissible present claims and deferred claims

### The revised manuscript may claim

- a candidate architecture for a general theory;
- a unifying and typed formal vocabulary;
- a distinction between within-architecture viability and architecture transformation;
- a compositional language accommodating unlike domain mechanisms;
- a formal place for diffuse commons, strategic behavior, legitimacy, and boundary assumptions;
- an organized programme of conjectures and proof obligations.

### It should defer

- a completed universal explanatory theory;
- a general solution to compositional verification;
- a universal normative criterion;
- universal computability;
- a proven cross-domain empirical law;
- validated sustainability conclusions from the canonical sketch.

This division preserves ambition without confusing architecture with completed proof.

---

## 15. Final integrated decision

The big-picture response and both audits jointly support the same overall direction:

> Establish one frozen specification, one typed constraint registry, two operators, explicit boundary interfaces, typed dependencies and commons nodes, relation-level contract modalities, and a disciplined hierarchy of definitions, conjectures, templates, placeholders, and proof obligations.

The manuscript should remain broad, anticipatory, and architecturally ambitious. Its immediate task is not to fill every box. It is to ensure that every future box attaches to the same formal spine and that no later development must choose between incompatible definitions of the theory’s primitive object.

# Joint Evaluation of the Two Architectural Audits
## Architectural decisions for *Toward a General Theory of Sustainability*

**Date:** 14 August 2026

## Overall judgment

The two audits are strongly complementary rather than opposed. Both accept a top-down manuscript containing conjectures, templates, and unresolved modules. Both argue that incompleteness is acceptable but ambiguity at the load-bearing interfaces is not. Their combined recommendation is sound: preserve the scientific ambition while replacing the current parallel formulations with one stable architectural spine.

The first audit is strongest on the kinds of boxes the architecture must support: stratified constraints, a meta-space of architectures, typed contracts, commons nodes, and explicit boundary interfaces. The second is strongest on how those boxes must connect: one constraint registry, two official operators, typed dependency edges, frozen identity, horizon typing, a single implementable control set, and disciplined claim labels.

Neither should be adopted literally in every detail. The best architecture is a synthesis.

---

## 1. Constraints: one registry, typed semantics, derived projections

The apparent disagreement is resolvable.

- The first audit proposes stratified physical, functional, and normative constraint boxes.
- The second warns against creating rival constraint geometries and proposes one tagged \(K^*\).

The correct synthesis is **one constraint registry**, not one semantically flat verdict.

Let

\[
\mathscr C=\{c_1,\ldots,c_m\}
\]

be the official constraint register. Each entry is a typed object:

\[
c_j=(p_j,\tau_j,s_j,\rho_j,\nu_j,\kappa_j,g_j,h_j),
\]

where:

- \(p_j\): predicate or bound;
- \(\tau_j\): physical, functional, normative, relational, or epistemic type;
- \(s_j\): system, stock, capacity, population, or interface to which it applies;
- \(\rho_j\): provenance and evidence status;
- \(\nu_j\): substitutability rule;
- \(\kappa_j\): reversibility or criticality status;
- \(g_j\): affected group;
- \(h_j\): applicable horizon.

Typed projections are derived from the registry:

\[
K_P=\bigcap_{\tau_j=P}\{z:p_j(z)\},\qquad
K_F=\bigcap_{\tau_j=F}\{z:p_j(z)\},
\]

with corresponding normative and relational projections. The combined geometry may still be written

\[
K^*=K_P\cap K_F\cap K_N\cap K_R,
\]

but the assessment must return a typed judgment vector rather than an unqualified outside/inside result:

\[
\mathbf J_\Omega(\tau)=(P_\Omega,F_\Omega,N_\Omega,R_\Omega).
\]

This preserves one source of truth while distinguishing physical impossibility, functional failure, normative inadmissibility, and relational externalization. Tags are therefore not decorative metadata; they determine failure semantics and permissible operators.

### Qualification to the first audit

A physical boundary is not always best described as a “controlled target.” When the dynamics are physically valid, impossible trajectories should already be excluded from the model domain. Physical constraints can nevertheless remain in the register for model validation, data consistency, and coupling to approximate modules.

---

## 2. One specification, one architecture registry, two official operators

This is the strongest shared recommendation.

Let the frozen assessment specification be

\[
\Omega=(S,z_0,I^{H},I^{L},B,\mathscr C,W,T,\mathcal N),
\]

where \(I^{H}\) contains protected higher-order identity predicates and \(I^{L}\) contains lower-level features that may change under declared conditions.

Let an architecture be

\[
\mathcal A_q=(Z_q,F_q,U^{\mathrm{impl}}_q,B_q,I_q,\mathscr C_q,\partial_q).
\]

Here \(\partial_q\) is the set of boundary interfaces.

### Operator 1: within-architecture sustainability

For current state \(z_0\), the correct condition is not merely that the kernel is nonempty. It is

\[
z_0\in\operatorname{Viab}_{\mathcal A_q}(K^*,W,T;U^{\mathrm{impl}}_q).
\]

A nonempty kernel proves that some state is viable; it does not prove that the actual state is viable. This correction is necessary to the second audit’s proposed formula.

Operator 1 covers regulation, restoration, buffering, and adaptation that do not change the architecture.

### Operator 2: transformation between architectures

Let

\[
\mathbb A=\{\mathcal A_q:q\in Q\}
\]

be an architecture registry and \(E_A\) the set of permitted architecture transitions. A transition has the form

\[
(q,z)\longrightarrow(q',R_{qq'}(z)),
\]

where the reset or translation map carries stocks, liabilities, obligations, affected populations, and identity predicates across architectures.

Transformation sustainability is a hybrid reach–avoid–maintain property whose target is the viable kernel of a destination architecture. It requires a predeclared identity-continuity test and transition constraints.

Kernel emptiness in \(\mathcal A_q\) does not prove that a sustainable transformation exists. It establishes only that, under frozen \(\Omega\), within-architecture control cannot succeed. The remaining possibilities are transformation, acknowledged impossibility, or creation of a new specification. Revising \(I^H\) or the normative standard creates a new claim and cannot retroactively validate the old one.

### Informal definition

The manuscript may retain an informal paraphrase, but it must be explicitly identified as an interpretation of the two operators—not a competing definition.

---

## 3. Replace causal closure with boundary-interface adequacy

Both audits are correct that “causally closed state space” is the wrong expression. A state space is a set; closure concerns the model cut and its interfaces.

The replacement principle should be:

> **Boundary-interface adequacy:** Every decision-relevant influence crossing the model boundary is internalized, represented by a typed interface assumption, or accompanied by an explicit negligibility claim and sensitivity bound.

For interface \(e\), record:

\[
C_e=(A_e,G_e,W_e,\epsilon_e,\text{evidence}_e).
\]

A certificate must discharge each boundary obligation at its declared confidence. This is property-relative adequacy, not metaphysical completeness.

### Qualification to the first audit

The environment need not literally “guarantee” every boundary condition. Some interfaces are assumptions, disturbance envelopes, scenarios, or adversarial bounds. The general interface type should allow each of these.

---

## 4. Typed dependency hypergraph and commons nodes

The recommendations are complementary:

- The first audit adds many-to-one commons nodes.
- The second adds typed dependency edges.

The appropriate structure is a **typed directed hypergraph**, not merely a dyadic graph. Edge or hyperedge types include:

1. obligatory support;
2. optional or substitutable support;
3. harmful impact;
4. mere nesting;
5. shared-source dependence;
6. shared-sink contribution.

A commons node \(C\) receives aggregate load

\[
L_C=\mathcal L_C(\{z_i,a_i\}_{i\in N_C}),
\]

where \(\mathcal L_C\) need not be additive. The simple sum is a special case. The capacity condition is

\[
L_C\le C_C.
\]

An allocation procedure assigns actor budgets or obligations \(b_i\). An actor may violate relational sustainability by exceeding its justified allocation even when its contribution is not individually threshold-pivotal.

This architecture permits scale, recursion, sacrifice, substitution, and diffuse responsibility to coexist without using one untyped arrow for all relations.

---

## 5. Contract typing should attach to relations, not entire domains

The first audit’s deterministic, probabilistic, and strategic modalities are essential. They should not be rigidly assigned by domain. Ecological relations can be stochastic; social rules can occasionally be deterministic; economic accounting identities differ from behavioral responses.

The contract registry should support:

- deterministic contracts \(A\Rightarrow_{det}G\);
- robust or set-valued contracts \(A\Rightarrow_{rob}G(W)\);
- probabilistic contracts \(A\Rightarrow_{prob}\Pr(G\mid A)\ge1-\epsilon\);
- strategic contracts \(A\Rightarrow_{strat}G\in\operatorname{Eq}(A,\Theta)\);
- scenario assumptions without guarantees.

Compatibility must be type-aware. A deterministic downstream requirement cannot silently rely on a probabilistic upstream contract; a buffer, fallback, or acceptable failure probability must bridge the types.

The composition claim should remain a conjecture or interface principle until a sound theorem is supplied. Sustainable composition should be expressed through a jointly viable behavior, invariant set, tube, or strategy—not necessarily a stationary fixed point.

---

## 6. Time, control, identity, and resilience require one official layer each

### Time

All primary claims are indexed by horizon \(T\). Infinite-horizon results belong to a distinct operator \(\operatorname{Sust}_\infty\) or are explicitly conditional large-horizon lemmas. Latent liabilities are a finite-horizon modelling device, not a universal scalar representation of future generations.

### Control

Define once:

\[
U_{\mathrm{impl}}\subseteq U_{\mathrm{inst}}\subseteq U_{\mathrm{tech}}\subseteq U_{\mathrm{theor}}.
\]

Within-architecture viability uses \(U_{\mathrm{impl}}\). Transformation may change the implementable set. Strategic behavior explains part of the gap between theoretical and implementable action and may later be filled by game-theoretic modules.

### Identity

Freeze \(I^H\) prospectively. Permit change in \(I^L\) only through declared transition rules. Revision of \(I^H\) creates a new specification. The framework need not solve legitimacy; it must record whose normative authority \(\mathcal N\) is being applied.

### Resilience

The second audit recommends defining resilience relative to a declared \(K^*\). That is internally clean but departs from value-neutral ecological usage. The manuscript should avoid overwriting established meanings by distinguishing:

- **dynamical or ecological resilience:** persistence of a regime or identity under disturbance;
- **sustainability robustness:** persistence of the full typed sustainability judgment under disturbance.

An undesirable regime can possess the first but not the second.

---

## 7. Separate definition, principles, lemmas, conjectures, and templates

Both audits correctly support placeholders but oppose mislabeled restatements.

The manuscript should use the following box taxonomy:

- **Definition:** official meaning used by the framework.
- **Well-formedness rule:** requirements for a valid sustainability claim.
- **Interface principle:** requirements imposed on boundaries, edges, contracts, and controls.
- **Conditional lemma:** consequence under an explicit stock, delay, intensity, or capacity signature.
- **Conjecture:** open formal or empirical claim.
- **Template:** specification, contract, ledger, certificate, substitution test, or diagnostic workflow.
- **Placeholder:** required module whose internal theory remains open.
- **Proof obligation:** condition that future work must discharge.
- **Instantiation sketch:** example used to exhibit interfaces rather than prove performance.

Axioms 2 and 4 should merge into the official definition. Axiom 1 becomes a well-formedness rule. Axiom 3 becomes the boundary-interface principle. Stock balance, delay, zero-slack, and growth statements become conditional lemmas.

Certification Levels 0–2 should be renamed assessment-maturity or preflight levels because they do not establish sustainability.

---

## 8. Positioning and permissible ambition

The audits agree that the absence of computed kernels, calibrated social models, a universal moral theory, or general contract-synthesis algorithms is not presently fatal. Those are legitimate open boxes.

The manuscript should position itself consistently as:

> **a candidate architectural kernel and composition language for a general theory of sustainability.**

This allows the title *Toward a General Theory of Sustainability* to remain. “Toward” signals a research programme rather than a completed universal law.

The canonical model may remain an instantiation sketch. Conjectures may remain unproved. Templates may remain empty. The non-negotiable requirement is that all future modules attach to one stable spine.

---

## 9. Adjudication of the two audits

### Adopt from both

- typed constraint semantics;
- architecture registry and transformation operator;
- typed contracts;
- explicit boundary interfaces;
- frozen higher-order identity;
- clear distinction between scaffolding and results.

### Add from the first audit

- commons/shared-sink nodes;
- contract modality checking;
- explicit accommodation of diffuse aggregate burdens.

### Add from the second audit

- one constraint registry rather than parallel geometries;
- typed dependency edges;
- horizon-indexed operators;
- one official implementable control set;
- replacement of fixed points by jointly viable behaviors;
- rigorous box taxonomy and contribution positioning.

### Modify rather than adopt literally

- Use typed projections and a typed verdict vector, not merely tags on a flat intersection.
- Require current-state membership \(z_0\in\operatorname{Viab}\), not only a nonempty kernel.
- Attach contract type to each relation, not to ecological/social domains wholesale.
- Allow nonlinear aggregate commons functions, not only sums.
- Distinguish established ecological resilience from sustainability robustness.
- Keep one official formal definition while allowing a clearly subordinate informal explanation.

---

## Final architectural spine

The stable top-down structure is:

1. a frozen sustainability specification \(\Omega\);
2. a registry of system architectures \(\mathbb A\);
3. one typed constraint registry \(\mathscr C\) with derived projections and a typed verdict vector;
4. within-architecture viability evaluated at the actual initial state;
5. a separate hybrid transformation operator between architectures;
6. boundary-interface adequacy rather than causal closure;
7. a typed dependency hypergraph with commons nodes;
8. deterministic, robust, probabilistic, and strategic contract modalities;
9. horizon-indexed claims using the implementable action set;
10. explicit boxes for definitions, interface principles, conditional lemmas, conjectures, templates, placeholders, and proof obligations.

This architecture preserves the manuscript’s ambition and anticipatory scope while preventing future work from being built on incompatible primitives.

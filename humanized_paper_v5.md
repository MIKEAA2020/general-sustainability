# The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment

**Amin Abaee**
Independent Researcher
ORCID: 0000-0002-0019-1842 · amin_abaee@ut.ac.ir

September 10, 2026

---

## Abstract

Sustainability assessments routinely aggregate heterogeneous capital stocks and floors into single indices, on the premise that a deficit in one dimension can be compensated by a surplus in another. This paper proves a separation result for a typed transition datum — per-moiety floors and an action menu — under exact-tube semantics: a transition is safe only if every state along the path, not merely the endpoint, satisfies the constraints.

On an explicit rational witness, for every nonnegative scalarization weight there is some action that keeps the aggregate floor nonnegative along its worst-case tube, while no single action keeps all typed floors nonnegative along theirs. The per-weight accepted state set strictly contains the common-plan accepted set. The discrepancy region splits by a resource threshold into a rescue set and an impossibility region, whose states admit no typed-safe transition under any weight and can be bridged only by resource augmentation at a defined cost. The genuine acceptance gap FP_agg = V_weak \ V_typ is exactly this impossibility region, with nonempty relative interior.

Two further results bound the separation: a two-stage datum on which a later interval erases the gap, and a blend theorem under which menu convexification — convexified actions whose worst-case tubes are convex combinations of the primitive ones — closes the gap exactly on the compensatory region. A converse delimits mixing: under discrete time-sharing, whose visited set is the union of the action tubes, the gap survives on the impossibility region, so the separation's structural character is a property of the convexity of the action space, not of temporal sharing. Within the deterministic menu the separation is structural, not an artifact of weight choice. Continuum statements are proved analytically, and the rational instance is checked by exact-integer computation.

**Keywords:** sustainability assessment; weak and strong sustainability; compensatory aggregation; scalarization; viability theory; composite indicators; capital substitution

**Mathematics Subject Classification:** 49J53; 93B03; 91B76; 90B50

---

## 1. Introduction

### 1.1 Two failure modes

Sustainability assessment sits on a fault line that has structured the field since its foundation. The weak-sustainability tradition, formalized in the genuine-savings and inclusive-wealth frameworks (World Bank, 2011; Boos, 2015; Neumayer, 2013), treats distinct capital forms as substitutable through prices: a decline in one stock is consistent with sustainability if the aggregate value of the capital base does not decline. The strong-sustainability tradition holds, in contrast, that certain stocks and services are separately binding — critical natural capital whose loss cannot be compensated at any price (Daly, 1990; Ekins et al., 2003). Its foundation statement in ecological economics is the thesis of weak comparability: values relevant to environmental decisions may not be commensurable in a single metric at all (Martinez-Alier, Munda, and O'Neill, 1998). The debate is mature in the policy and multi-criteria decision literatures (Cinelli, Coles, and Kirwan, 2014; Schär, Pohl, and Geldermann, 2025; Hanley et al., 1999; Usubiaga-Liaño, 2025), and the theory of sustainability indicators is correspondingly well developed (Martinet, 2011; Cairns and Martinet, 2014), including the maximin formulation in which strong sustainability emerges from the viability of the constraints rather than from an optimality criterion (Solow, 1974; Doyen and Gajardo, 2020).

Read in this paper's terms, the two traditions are distinguished by whether compensatory substitution keeps pace with depletion. The material-cycle reading of that distinction — waste as a relational status, the closure of the material cycle at the rate of use, substitution against deep-time renewal — is developed in the companion ledger study (Abaee, 2026a) and is not re-argued here; no theorem of this paper concerns material cycles. The doctrines this paper does compare are the operators formalized in §3.1 and read doctrinally in §5.1.

The assessment question here is the certification form of that distinction. The blend-collapse result (Theorem 8) closes the acceptance gap exactly on the compensatory region where convexified substitution — fractional allocation of control flows — keeps pace, and the impossibility region of Theorem 5(4) marks where substitution, even under discrete time-sharing, does not. Substitution is admissible only through an identified physical pathway, and no compensation is assumed merely because a weighted aggregate permits it. The aggregate question — whether total capital can be maintained — is ambiguous between the two quantifier orders made precise in Remark 1 and §4.5.

This paper addresses a question that the indicator literature has left comparatively open: the dynamic question. During a sustainability transition, when can a compensatory aggregate certify a trajectory that a noncompensatory assessment rejects? Two failure modes motivate the question.

The first is commensurability drift. Assessments aggregate stocks, services, liabilities, and floors into single indices whose compensation principles are rarely stated as explicit mathematics. Composite indices are routinely criticized on exactly this ground: the weights they embed are value judgements presented as measurement (Hickel, 2020; Martinez-Alier, Munda, and O'Neill, 1998). The critique typically targets the choice of weights. The stronger possibility, established here, is that no choice of weights repairs the difficulty: the failure is structural, lying in the logic of aggregation itself.

The second is the circulation of conditional results as unconditional ones. Each result below therefore states its assumptions and status explicitly.

The masking formalized here is the following: an aggregate of two typed floors can stay nonnegative along its worst-case tube while each floor in turn takes a dip that no common plan accepts. It is distinct from the productivity illusion — adequate delivery from a reduced productive base — treated in Abaee (2026a). On the witness constructed below the aggregate is taken over the two service floors s₁, s₂ themselves; what it does not detect is the individual floor mid-interval — the compensatory form of the illusion in aggregation, the acceptance gap of Theorem 5(4).

### 1.2 The central result

The paper's organizing result is a quantifier noncommutation. Fix a typed transition datum: a state space carrying typed floors sᵢ ≥ 0 (normalized at zero), an action set, a disturbance set, and exact-tube semantics under which a transition is safe only if every state visited along it — not merely its endpoint — satisfies the constraints. For each nonnegative scalarization weight w in the full cone W₊ = ℝⁿ₊ \ {0}, let E_w(z) be the set of actions admissible at state z under the aggregate floor w·s ≥ 0, and let E_typ(z) be the set of actions admissible under the typed floors sᵢ ≥ 0 taken separately. Two acceptance criteria then differ by quantifier order:

- **Common-plan acceptance (noncompensatory).** There exists one action lying in every E_w(z):

  ∃a ∀w : a ∈ E_w(z).

- **Per-weight acceptance (compensatory).** For each weight there exists some admissible action, possibly depending on the weight:

  ∀w ∃a_w : a_w ∈ E_w(z).

The first implies the second; the converse fails. The failure is not a defect of any particular weight: it is the noncommutativity of the existential quantifier over actions with the universal quantifier over weights. The noncommutation is the assessment-theoretic instance of the strict minimax pattern of game theory — for the binary payoff "action a is admissible at z under w," the two quantifier orders are the two orders of the minimax interchange, and the witness of §4.5 exhibits the interchange failing strictly. Remark 1 states the always-valid inclusion; Proposition 3(ii) identifies the noncompensatory operator with the common-plan set over the full cone; and Theorem 5 exhibits an explicit rational witness on which the acceptance gap FP_agg = V_weak \ V_typ is a region with nonempty interior — the impossibility region (Theorem 5(4)). The witness further partitions the aggregate-versus-direct-floor discrepancy region Q by a resource threshold into the impossibility region and the rescue set, whose states are already typed-transformable through the resource-controlled action (Theorem 5(7)). The rescue operation of §5.5 — resource augmentation — acts on the impossibility region, not on the rescue set.

### 1.3 Contribution, scope, and reader's guide

**Contributions.** (i) The action-set identity E_typ(z) = ⋂_{w∈W₊} E_w(z), with the full-cone choice (the cone without the origin) isolating the separation as purely dynamic (Proposition 3(ii)). (ii) A general quantifier-separation remark (Remark 1). (iii) Monotonicity of the accepted-state hierarchy in the weight family (Proposition 4). (iv) An explicit rational witness with an open region of strict separation, the discrepancy-region split Q = R ∪ I, the identity FP_agg = I, the exact per-weight licensing thresholds (Theorem 5), and the closed form of the rescue threshold (Proposition, §5.5). (v) Persistence of the separation under hold-prefix extension of the horizon (Remark 6). (vi) An explicit two-stage erasure datum on which a later interval removes the gap (Theorem 7), delimiting the propagation claim. (vii) The blend-collapse theorem: menu convexification closes the acceptance gap exactly at the compensatory region (Theorem 8), while the converse delimitation (Proposition 9) shows that discrete time-sharing — whose visited set is the union of the action tubes — closes it only where both dips are independently subsumed, so the gap survives on the impossibility region.

**Scope.** No universal ranking of weak- and strong-sustainability doctrines; no proof that any particular set of environmental boundaries ought to be treated noncompensatorily; no empirical result about any specific resource system. The governance, intergenerational, and composition extensions are stated at partial status in the Supplementary Material.

To our knowledge, this provides an explicit exact-tube witness for this dynamic separation in a compensatory/noncompensatory assessment setting; the elementary quantifier fact behind it is standard, and §5.2 states the full novelty qualification.

**Reader's guide.** Formal statements are followed by a brief paraphrase ("In words"), so the results can be read at two levels of precision. The notation is collected in a glossary (§2.4), and the central witness is illustrated by a fully worked instance immediately after Theorem 5. The paper is organized as follows: §2 fixes the typed framework and notation; §3 defines the assessment operators; §4 states and proves the separation and its bounding results; §5 gives the interpretation, positioning, scope, and policy implications; §§6–7 discuss limitations and conclude.

---

## 2. A Typed Framework for Transition Assessment

### 2.1 Types and physical state

Physical state is typed. A state variable denotes a moiety — a named conserved substance — with a unit, and typed fluxes connect typed stocks. Conservation claims are per-moiety; the framework does not authorize adding biomass, money, and biodiversity into one conserved scalar. Services, thresholds, information states, and institutional variables are separate types. No statement combines quantities of different type except through an explicit bridge. Typing serves two purposes: it makes the domain of every conservation law explicit, and it records the provenance of every floor — physical, contractual, or normative — as part of the floor's type.

### 2.2 The assessment datum

The results use a typed exact-tube transition datum: a state space Z carrying typed floors sᵢ ≥ 0 (normalized at zero), an action set, a disturbance class D, a typed safe set S, a destination set G, and tube and successor maps Tube(a,d), Succ(a,d) as defined in §3.1. A transition is safe only if every state visited along it, not merely its endpoint, satisfies the constraints. The witness datum of §4.5 is an instance of this datum.

### 2.3 Quantifier discipline

Every assessment operator evaluates the disturbance quantifier innermost: admissibility of an action requires safety for every d ∈ D. The separation analysed in §3 concerns a second quantifier, over scalarization weights, placed outside it: the noncommutation studied is ∃a ∀w versus ∀w ∃a_w.

### 2.4 Glossary of notation

| Symbol | Meaning |
|---|---|
| z ∈ Z | a state; a: an action; d ∈ D: a disturbance |
| s = (s₁, …, sₙ) | the typed floors, normalized so that sᵢ ≥ 0 is the binding constraint |
| x | the reserve stock (bridge stock) on the witness |
| W₊ = ℝⁿ₊ \ {0} | the full nonnegative scalarization cone excluding the origin |
| w ∈ W₊ | a nonnegative scalarization weight; a subfamily is written W; r = w₂/w₁ the weight ratio |
| S, G | typed safe and destination sets: S = S^phys ∩ {sᵢ ≥ 0}, G = G^phys ∩ {s ≥ 0} |
| S^w, G^w | their scalarized counterparts at weight w: {w·s ≥ 0} in place of {sᵢ ≥ 0} |
| S^phys, G^phys | the purely physical safe and destination sets (floors ignored) |
| Tube(a,d) | the full set of states visited during the interval (the tube: the whole path) |
| End(a,d) | the endpoint values visited |
| Succ(a,d) | the successor set after any endpoint reset |
| E_typ, E_w, E_tube,phys, E_end, E_end,typ | the five assessment operators of §3.1 |
| V[E] = {z : E(z) ≠ ∅} | the accepted-state set of operator E; V_weak = ⋂_{w∈W₊} V_w |
| (q, x, s₁, s₂) | the phase state of the witness: mode q (0 = extraction, 1 = regeneration), reserve x, floors s₁, s₂ |
| e = (¼, ¼) | the gain vector applied to both floors at the destination; c = 1 the rescue cost; depth 2 the worst-case dip |
| Q, R, I | the discrepancy region, rescue set, and impossibility region of §4.6 |
| FP_agg = V_weak \ V_typ | the genuine acceptance gap |
| ρ₁, ρ₂ | the per-weight licensing thresholds of Theorem 5(6) |
| A, Aug_κ, κ\* | the action set; the resource-augmentation map; the minimal rescue threshold (§5.5) |

The gain vector e of the witness datum and the standard basis vector e_k in Remark 2 are distinct objects.

---

## 3. Assessment Operators

### 3.1 Five operators

Fix a typed exact-tube transition datum with transition-safe sets and a destination set. For a state z and action a, Tube(a,d) is the full set of states visited during the interval under disturbance d, End(a,d) the endpoint values visited, and Succ(a,d) the successor set after any endpoint reset. Five operators are distinguished. They share the same disturbance quantifier and differ in constraint structure, except that the endpoint operator also replaces tube evaluation by endpoint evaluation. The fifth is the typed-endpoint operator, used in §5.4.

The **noncompensatory typed** operator (each floor separately binding):

E_typ(z) = { a : ∀d, Tube(a,d) ⊆ S and Succ(a,d) ⊆ G },

where S = S^phys ∩ {sᵢ ≥ 0, i = 1..n} and G = G^phys ∩ {s ≥ 0}.

The **scalarized aggregate** operator at weight w ∈ W₊ = ℝⁿ₊ \ {0}:

E_w(z) = { a : ∀d, Tube(a,d) ⊆ S^w and Succ(a,d) ⊆ G^w },

where S^w = S^phys ∩ {w·s ≥ 0} and G^w = G^phys ∩ {w·s ≥ 0}.

The **exact-tube physical** operator (physical constraints only, full tube):

E_tube,phys(z) = { a : ∀d, Tube(a,d) ⊆ S^phys and Succ(a,d) ⊆ G^phys }.

The **endpoint-only physical** operator (physical constraints at endpoints only):

E_end(z) = { a : ∀d, End(a,d) ⊆ S^phys and Succ(a,d) ⊆ G^phys }.

The endpoint operator represents aggregated accounting evaluated on audited snapshots, while typed floors constrain the whole trajectory: evaluation on the full tube versus evaluation on endpoints only. The endpoints are the photograph; the tube is the trajectory. Endpoint values cannot in general certify the condition of the system that produced them (cf. the productivity-illusion analysis in Abaee, 2026a); the typed-endpoint operator below states the floor-level version of this observation exactly on the witness. Because End(a,d) ⊆ Tube(a,d), the endpoint operator is the weakest, and the chain

E_typ(z) ⊆ E_w(z) ⊆ E_tube,phys(z) ⊆ E_end(z)

holds for every w ∈ W₊ (Proposition 3(i)). The last inclusion is strict in general, though it collapses on the witness of §4.5 because on the witness the physical constraint involves only the monotone reserve stock.

**Definition (typed-endpoint operator).** The typed-endpoint operator evaluates typed floors at endpoints only:

E_end,typ(z) = { a : ∀d, End(a,d) ⊆ S and Succ(a,d) ⊆ G }.

It satisfies E_typ(z) ⊆ E_end,typ(z) ⊆ E_end(z), since End(a,d) ⊆ Tube(a,d), S ⊆ S^phys, and G ⊆ G^phys. On the witness datum of §4.5, FAST's endpoint values of s₁ equal the initial s₁ and its successor lies in G whenever x ≥ 0 (action table in §4.5; proof of Theorem 5(1)), so E_end,typ(z) ≠ ∅ at every z ∈ X₀, while E_typ(z) ≠ ∅ requires s₁ ≥ 2 (Theorem 5(1)). This observation follows by inspection of the action table and is not part of the machine-checked artifact of §4.9.

### 3.2 Accepted-state operators

For any operator E, write V[E] = { z : E(z) ≠ ∅ } for the set of states at which E admits at least one action. Thus V_typ = V[E_typ], V_w = V[E_w], V_phys = V[E_tube,phys], V_end = V[E_end], and the compensatory accepted set

V_weak = ⋂_{w∈W₊} V_w.

The central noncommutation is then:

{ z : ⋂_w E_w(z) ≠ ∅ }  ⊆  ⋂_w { z : E_w(z) ≠ ∅ },

i.e. the common-plan accepted set is contained in the per-weight accepted set; V_typ ⊆ V_weak.

---

## 4. Results: The Separation Theorem

### 4.1 A general quantifier-separation remark

**Remark 1.** Let {E_λ(z)}_{λ∈Λ} be a family of action sets. Then always

{ z : ⋂_λ E_λ(z) ≠ ∅ } ⊆ ⋂_λ { z : E_λ(z) ≠ ∅ }.

*In words.* If one action works for every member of a family at once, then something works for each member individually; the reverse requires the family to admit a single common action.

Equality holds exactly when, for every z in the right-hand set, the family {E_λ(z)}_λ admits a common selector. No topology on the action space is imposed. In finite menus the check is combinatorial: if the action set is finite, only finitely many distinct E_λ(z) occur and common-selector existence is a finite enumeration (on the witness of §4.5, |A| = 4). For infinite families, classical sufficient conditions — the finite-intersection property together with compactness/closedness in a specified topology — are available but not needed here.

**Proof.** If a ∈ ⋂_λ E_λ(z), then each E_λ(z) is nonempty, so z lies in the right-hand set. The inclusion fails at z precisely when each E_λ(z) is nonempty but ⋂_λ E_λ(z) = ∅, i.e. when no common selector exists; this is the stated equality condition. □

The separation in §4.5 is a strict instance of this inclusion, at states where the nonemptiness witnesses differ with the weight.

### 4.2 The full-cone identity

**Remark 2 (full-cone pointwise equivalence).** For v ∈ ℝⁿ,

v ≥ 0 componentwise  ⟺  w·v ≥ 0 for every w ∈ W₊ = ℝⁿ₊ \ {0}.

*In words.* Checking every nonnegative weighted sum is exactly equivalent to checking each coordinate separately.

**Proof.** (⇒) w ≥ 0, w ≠ 0, v ≥ 0 gives w·v = Σᵢ wᵢvᵢ ≥ 0. (⇐) If v_k < 0, take w = e_k ∈ W₊: then w·v = v_k < 0. □

At a fixed trajectory the full-cone aggregate is therefore lossless: nonnegativity of every weighted sum is equivalent to componentwise nonnegativity. The separation below is entirely dynamic — a matter of quantifier order — not static scalarization blindness.

### 4.3 The assessment identity and hierarchy

**Proposition 3 (assessment identity and hierarchy).**

(i) *Hierarchy.* For every w ∈ W₊ and every z,

E_typ(z) ⊆ E_w(z) ⊆ E_tube,phys(z) ⊆ E_end(z).

(ii) *Localization.* For every z,

E_typ(z) = ⋂_{w∈W₊} E_w(z).

Hence V_typ = { z : ⋂_w E_w(z) ≠ ∅ }.

*In words.* (i) The operators nest by strictness: the typed test is the most demanding, then the weighted-aggregate test, then the physical-tube test, then the endpoint test. (ii) Passing every weighted-aggregate test at a state is equivalent to passing the typed test there.

**Proof.** (i) Let a ∈ E_typ(z). For every disturbance d, Tube(a,d) ⊆ S = S^phys ∩ {s ≥ 0}. By Remark 2, every tube point satisfies w·s ≥ 0 for every w ∈ W₊, and likewise every successor state lies in G^w; hence a ∈ E_w(z). The remaining inclusions follow from S^w ⊆ S^phys, G^w ⊆ G^phys, and End(a,d) ⊆ Tube(a,d). (ii) The inclusion ⊆ is part (i) intersected over w. For the reverse inclusion, let a ∈ ⋂_{w∈W₊} E_w(z). For every d and every tube point p ∈ Tube(a,d), every w ∈ W₊ gives w·s(p) ≥ 0, so by Remark 2 s(p) ≥ 0 componentwise; hence Tube(a,d) ⊆ S. The same argument with Succ gives Succ(a,d) ⊆ G. Thus a ∈ E_typ(z). □

Part (i) is standard constraint-set monotonicity under nested safe sets (Aubin, 1991; Frankowska, 1989); part (ii) is proved above, and its strictness is witnessed in Theorem 5.

### 4.4 Weight-family monotonicity

**Proposition 4 (weight-family monotonicity).** For a weight family W ⊆ W₊ define V_W = ⋂_{w∈W} V_w. Then

V_typ ⊆ V_W ⊆ V_phys,

and if W₁ ⊆ W₂ then V_W₂ ⊆ V_W₁.

*In words.* Restricting the weight family enlarges the compensatory accepted set — fewer assessors to satisfy, more states accepted. The full cone is therefore the strictest compensatory reading, and any separation exhibited at the full cone persists for every restricted family.

**Proof.** For the second inclusion: by Proposition 3(i), E_w(z) ⊆ E_tube,phys(z) for every w, so V_w ⊆ V_phys, and intersecting over w ∈ W preserves the inclusion. For the first: if z ∈ V_typ, then by Proposition 3(ii) there exists a ∈ ⋂_{w∈W₊} E_w(z); this same a lies in ⋂_{w∈W} E_w(z), so E_w(z) ≠ ∅ for every w ∈ W, i.e. z ∈ V_W. Monotonicity: intersecting over a larger family can only shrink the intersection. □

### 4.5 The witness datum

The witness datum is the explicit typed transition datum on which the separation of Theorem 5 is exhibited. Two architectures — extraction (q = 0) and regeneration (q = 1) — share one review interval [0,1], with phase state (q, x, s₁, s₂): a physical reserve stock x and two typed floors s₁ (protected-group service surplus) and s₂ (remediation-liability coverage), both normalized to 0. The transition-safe set is S₀ = {x ≥ 0, s₁ ≥ 0, s₂ ≥ 0}; the destination set is G = {(1, x, s) : x ≥ 0, s ≥ 0}, with destination maintainability witnessed by the destination hold policy. The destination reset applies the gain vector e = (¼, ¼) componentwise to both typed floors; e is strictly positive, so successors are interior to G, and no inequality of Theorem 5 binds on its magnitude. The rescue cost is c = 1 (STAGED spends one unit of x).

**Disturbance convention (action-indexed).** The disturbance set is {β, α}, where α triggers the worst-case dip — of fixed depth 2, per the action table below — in the active action's characteristic coordinate (s₁ for FAST, s₂ for SLOW), and β is the analogous disturbance applied to the other coordinate; the two disturbances are never required to hit a coordinate the action does not move. Each action's worst-case tube is the tube under its own characteristic dip, which is the worst case for that action's constraint. A disturbance label shared across the two actions still takes effect only on the coordinate each action moves, so FAST's s₂-tube and SLOW's s₁-tube are unchanged, and the distinction does not affect the separations of Theorem 5.

The four actions available from any initial state (0, x, s) with x ≥ 0, s ≥ 0, written as piecewise-linear maps on the breakpoints {0, ½, 1}, monotone on each piece (so every tube is the exact visited set — there is no outer approximation):

| Action | Within-interval trajectory (worst case) | Successor |
|---|---|---|
| NO-SWITCH | state constant | {(0, x, s)} — misses G |
| FAST | s₁(t) = s₁ − 4t on [0,½], s₁ − 4(1−t) on [½,1]; s₂, x constant | {(1, x, s + e)} |
| SLOW | s₂(t) = s₂ − 4t on [0,½], s₂ − 4(1−t) on [½,1]; s₁, x constant | {(1, x, s + e)} |
| STAGED | x(t) = x − t on [0,1]; floors grow to s + e | {(1, x − 1, s + e)} |

The worst-case tube of FAST is thus [s₁ − 2, s₁] in the s₁ coordinate with s₂ and x constant; the worst-case tube of SLOW is symmetric; the worst-case tube of STAGED is [x − 1, x] in the x coordinate with both floors nondecreasing.

### 4.6 Witnessed separation

**Theorem 5 (witnessed separation).** On the witness datum of §4.5, over initial states X₀ = {(0, x, s) : x ≥ 0, s ≥ 0}, the following hold.

**(1)** V_typ = { x ≥ 1 } ∪ { s₁ ≥ 2 } ∪ { s₂ ≥ 2 }.

**(2)** V_weak = ⋂_{w∈W₊} V_w = { x ≥ 1 } ∪ { s₁ + s₂ ≥ 2 }.

**(3)** V_phys = V_end = X₀.

*In words.* (1) The strong test passes if the reserve covers a staged rescue (x ≥ 1) or some floor is deep enough to survive its own worst-case dip (sᵢ ≥ 2). (2) The weak test passes if the reserve covers the rescue or the two floors together total at least 2 — note how "each floor ≥ 2" has become "both floors sum to ≥ 2." (3) Ignoring the floors, every state is accepted.

Define: Q = {s₁ < 2, s₂ < 2, s₁ + s₂ ≥ 2} — the aggregate-versus-direct-floor discrepancy region, with x unrestricted (not entirely a false-positive set, because for x ≥ 1 the STAGED action is typed-admissible); R = Q ∩ {x ≥ 1} — the rescue set, the already-typed slice of the discrepancy region, typed-transformable at cost c = 1, witnessed by STAGED; I = Q ∩ {x < 1} — the impossibility region; FP_agg = V_weak \ V_typ — the genuine compensatory-versus-noncompensatory acceptance gap.

**(4)** FP_agg = I. The genuine acceptance gap is exactly the impossibility region; it is nonempty, and its relative interior (in the q = 0 slice) is {0 < x < 1, 0 < s₁ < 2, 0 < s₂ < 2, s₁ + s₂ > 2}. The rescue set R is a subset of V_typ, not of the gap: it is the part of Q that is not a false positive.

**(5)** Both hierarchy inclusions are strict: every point of I lies in V_weak \ V_typ, and the point (x, s₁, s₂) = (½, ⅒, ⅒) lies in V_phys \ V_weak.

**(6) Per-weight plan disagreement.** On the relative interior of Q (where s₂ > 0 and s₂ < 2), writing r = w₂/w₁, the FAST-certifying weight ratios are exactly {r ≥ ρ₁} and the SLOW-certifying ratios exactly {r ≤ ρ₂}, with

ρ₁ = (2 − s₁)/s₂,    ρ₂ = s₁/(2 − s₂),    ρ₂ ≥ ρ₁ ⟺ s₁ + s₂ ≥ 2.

*In words.* Assessors who put a lot of weight on s₂ (r > ρ₂) license FAST only; assessors who put little weight on s₂ (r < ρ₁) license SLOW only; intermediate assessors license both. On I no single action serves every weight — ⋂_w E_w(z) = E_typ(z) = ∅ by Proposition 3(ii) — while on R the STAGED action is typed-admissible and hence serves every weight.

**(7) The rescue split.** R is typed-transformable, witnessed by STAGED: bridging at physical cost c = 1 keeps both floors intact and lands in G. I is aggregate-feasible for every cone weight yet admits no typed-admissible action, with four exhibited violations: FAST violates the s₁ floor under the adverse disturbance; SLOW violates the s₂ floor; STAGED drives x negative; NO-SWITCH misses G.

**Proof.** **(1)** Typed admissibility requires the worst-case tube in S₀ and the successor in G. NO-SWITCH never reaches G (its successor retains q = 0), so it is never admissible. For FAST, the worst-case s₁-tube is [s₁ − 2, s₁], safe if and only if s₁ ≥ 2; its successor (1, x, s + e) lies in G given x ≥ 0. Hence FAST is typed-admissible exactly when s₁ ≥ 2. Symmetrically, SLOW is typed-admissible exactly when s₂ ≥ 2. For STAGED, the floors grow through the interval and the successor lies in G; the binding constraint is the x-tube [x − 1, x], safe if and only if x ≥ 1. Therefore E_typ(z) ≠ ∅ exactly on {x ≥ 1} ∪ {s₁ ≥ 2} ∪ {s₂ ≥ 2}.

**(2)** Fix w = (w₁, w₂) ∈ W₊. NO-SWITCH misses G^w and is never admissible. FAST is w-admissible if and only if its worst-case aggregate value stays nonnegative: w₁(s₁ − 2) + w₂s₂ ≥ 0, i.e. w₁s₁ + w₂s₂ ≥ 2w₁ (automatic when w₁ = 0). Symmetrically SLOW is w-admissible if and only if w₁s₁ + w₂s₂ ≥ 2w₂. STAGED is w-admissible if and only if x ≥ 1 (the physical constraint within S^w), since w·s ≥ 0 holds automatically along its tube. Hence z ∈ V_w whenever x ≥ 1; and if x < 1, then z ∈ V_w if and only if at least one of the two inequalities above holds.

Suppose first x ≥ 1: then z ∈ V_w for every w, so z ∈ V_weak. Suppose x < 1 and s₁ ≥ 2 or s₂ ≥ 2: say s₁ ≥ 2; then FAST is typed-admissible by (1), hence w-admissible for every w, so z ∈ V_weak. It remains to treat x < 1 with s₁ < 2 and s₂ < 2. For w₁ > 0, write r = w₂/w₁: FAST is w-admissible exactly when s₁ + rs₂ ≥ 2, i.e. r ≥ (2 − s₁)/s₂ = ρ₁ (using s₂ > 0; when s₂ = 0 the condition reduces to s₁ ≥ 2, which is excluded). SLOW is w-admissible exactly when s₁ + rs₂ ≥ 2r, i.e. r ≤ s₁/(2 − s₂) = ρ₂ (using s₂ < 2). The boundary weights are the same limiting cases: at w₁ = 0 (r → ∞) FAST is licensed provided s₂ ≥ 0, while SLOW is strictly rejected on the region s₂ < 2; symmetrically, at w₂ = 0 (r = 0) SLOW is licensed provided s₁ ≥ 0, while FAST is rejected on the region s₁ < 2. Therefore z ∈ V_w for every w ∈ W₊ if and only if the intervals {r ≥ ρ₁} and {r ≤ ρ₂} together cover all of [0, ∞], which holds exactly when ρ₂ ≥ ρ₁. Computing,

ρ₂ ≥ ρ₁ ⟺ s₁/(2 − s₂) ≥ (2 − s₁)/s₂ ⟺ s₁s₂ ≥ (2 − s₁)(2 − s₂) ⟺ s₁ + s₂ ≥ 2,

with both denominators positive in the present case. Hence, in this case, z ∈ V_weak if and only if s₁ + s₂ ≥ 2. Assembling the three cases, and noting {s₁ ≥ 2} ∪ {s₂ ≥ 2} ⊆ {s₁ + s₂ ≥ 2} under nonnegativity,

V_weak = { x ≥ 1 } ∪ { s₁ + s₂ ≥ 2 }.

**(3)** In the physical operators the only constraint is x ≥ 0 (with q = 1 at the destination). FAST and SLOW have tubes within S^phys and successors in G^phys for every z ∈ X₀ (their dips affect only s, which is unconstrained physically); STAGED does so exactly for x ≥ 1. Hence E_tube,phys(z) ≠ ∅ for every z ∈ X₀, so V_phys = X₀. For the endpoint operator, the endpoint values of FAST and SLOW lie in S^phys for every z ∈ X₀, so V_end = X₀ as well.

**(4)** By (1)–(2),

FP_agg = V_weak \ V_typ = [ {x ≥ 1} ∪ {s₁ + s₂ ≥ 2} ] \ [ {x ≥ 1} ∪ {s₁ ≥ 2} ∪ {s₂ ≥ 2} ] = { x < 1, s₁ < 2, s₂ < 2, s₁ + s₂ ≥ 2 } = I.

This set is nonempty (e.g. (x, s₁, s₂) = (½, 6/5, 6/5)), and its relatively open interior is the stated region.

**(5)** By (4), I = FP_agg = V_weak \ V_typ ≠ ∅, so the first inclusion is strict. For the second, the point (½, ⅒, ⅒) satisfies x < 1 and s₁ + s₂ = ⅕ < 2, so it lies outside V_weak by (2), while by (3) it lies in V_phys.

**(6)** The threshold characterization was derived in the proof of (2). On Q the inequality s₁ + s₂ ≥ 2 holds, so the two licensing intervals overlap and together cover all weights; strictly on the relative interior (s₁ + s₂ > 2) both thresholds are finite and the intervals overlap in a nondegenerate interval, with r > ρ₂ licensing FAST only and r < ρ₁ licensing SLOW only. On I (where x < 1), STAGED is inadmissible for every w, so E_typ(z) = ⋂_w E_w(z) = ∅ by Proposition 3(ii): no single action serves every weight. On R (where x ≥ 1), STAGED lies in E_typ(z) = ⋂_w E_w(z) and serves every weight.

**(7)** On R, STAGED's tube is [x − 1, x] × {s → s + e}: the x-tube stays nonnegative because x ≥ 1, the floors grow, and the successor (1, x − 1, s + e) ∈ G. On I, the four exhibited violations exhaust the action set and each violates a typed constraint: FAST's s₁-tube reaches s₁ − 2 < 0; SLOW's s₂-tube reaches s₂ − 2 < 0; STAGED's x-tube reaches x − 1 < 0; NO-SWITCH's successor misses G. □

**Boundary conventions.** The formulas for ρ₁, ρ₂ require s₂ > 0 and s₂ < 2. On the boundary faces (s₂ = 0, s₂ = 2, s₁ = 0, s₁ = 2, s₁ + s₂ = 2) the classification follows directly from the closed-set identities of (1)–(2); no interior formula is applied there.

**Remark.** The compensatory assessment's binding condition is the total budget s₁ + s₂ ≥ 2. The noncompensatory assessment requires either one floor to survive its own worst-case dip (sᵢ ≥ 2) or the bridge stock to cover the rescue cost (x ≥ 1). The region between the two conditions is where the compensatory doctrine certifies — per weight, with weight-dependent plans — transitions the noncompensatory doctrine rejects.

**Example (the witness point).** At (x, s₁, s₂) = (½, 6/5, 6/5), the interior witness of Figure 1, Panel A, the typed verdict is rejection: STAGED's x-tube reaches ½ − 1 = −½ < 0; FAST's worst-case s₁ dips to 6/5 − 2 = −4/5 < 0; SLOW's worst-case s₂ dips to −4/5 < 0; NO-SWITCH misses G. Yet s₁ + s₂ = 12/5 ≥ 2, so the state is in V_weak, with thresholds ρ₁ = (2 − 6/5)/(6/5) = 2/3 and ρ₂ = (6/5)/(2 − 6/5) = 3/2. FAST is licensed exactly for r ≥ 2/3 and SLOW exactly for r ≤ 3/2; the intervals overlap, so every weight ratio r ≥ 0 licenses at least one action, but the licensed action depends on r: r = 2 (heavy on s₂) licenses FAST only, r = ½ licenses SLOW only, r = 1 licenses both. The aggregate thus certifies this state under every weighting while no single plan passes every weighting. By contrast, (x, s₁, s₂) = (½, ⅒, ⅒) has s₁ + s₂ = ⅕ < 2 and x < 1, so it fails even the weak test while remaining in V_phys — the point that makes the second inclusion strict. At (x, s₁, s₂) = (1, 6/5, 6/5), x ≥ 1 with the same floors, STAGED's x-tube is [0, 1], the floors grow, and the successor (1, 0, s + e) ∈ G, so the state is typed-accepted, as R promises.

### 4.7 Figure 1

The discrepancy region Q is the portion of the square 0 ≤ s₁, s₂ ≤ 2 lying on or above s₁ + s₂ = 2: the closed upper-right triangle with vertices (0,2), (2,0), (2,2), minus the two legs s₁ = 2 and s₂ = 2 (strict boundaries); the vertices themselves are outside Q, and the axis vertices (0,2), (2,0) are not even limit points of it along the axes. Its interior is 0 < s₁, s₂ < 2 with s₁ + s₂ > 2. **Panel A (x < 1, shown at x = 0):** the region is the genuine impossibility region I = FP_agg; the interior witness (s₁, s₂) = (6/5, 6/5) is marked. **Panel B (x ≥ 1, shown at x = 1):** the same aggregate-versus-floor region is the rescue set R, witnessed by STAGED. The threshold curves ρ₁, ρ₂ are drawn only on the open subregion where s₁ > 0, s₂ > 0 and s₂ < 2 (ρ₂ = 0 when s₁ = 0). The point (x, s₁, s₂) = (½, ⅒, ⅒), which lies outside the s-plane section, is annotated in Panel A. The region is the rescue set at x ≥ 1 and the impossibility region at x < 1; only the latter is a false positive.

### 4.8 Propagation under hold-prefix extension

This subsection asks whether the one-interval separation survives when the horizon is lengthened by prepending hold intervals. Remark 6 establishes persistence under a precisely specified hold-prefix extension; Theorem 7 exhibits a two-stage datum on which the gap is erased, showing the persistence claim is architecture-conditional.

**Remark 6 (propagation).** Extend the witness datum to m ≥ 2 review intervals by prepending hold intervals (sole action HOLD: constant tube {z}, successor {z}, safe set S₀; the final interval carries the witness). Assume: (H1) HOLD is available at every prefix state; (H2) the hold tube is exactly {z}; (H3) the prefix safe sets contain the witness states; (H4) terminal and successor architecture labels are unchanged; (H5) no additional reset or disturbance branches are introduced. Then:

(i) *Hierarchy.* For every stage j,

V^typ_j ⊆ ⋂_{w∈W₊} V^w_j ⊆ V^phys_j.

This inclusion holds for every multi-interval typed exact-tube datum; it is constraint monotonicity under backward induction.

(ii) *Persistence of strictness.* The stage-0 accepted regions are the witness regions pulled back through the holds, so both strictness witnesses of Theorem 5 persist under this hold-prefix extension.

(iii) The displayed separation is not an artifact of the one-interval framing for the constructed hold-prefixed datum. Strictness for arbitrary multi-stage systems does not follow without a separate persistence theorem: a later stage can erase the gap if every aggregate-feasible state has a common typed-safe continuation, if the weak and typed terminal sets coincide on the reachable subset, or if actions couple across stages.

*In words.* Waiting periods prepended to the review do not remove the gap; but in general multi-stage settings a later stage can erase it by one of three mechanisms, so persistence is architecture-conditional.

**Proof.** (i) Backward induction on stages. Base: at the final stage the terminal sets satisfy G ⊆ G^w ⊆ G^phys by Remark 2 and the definition of the terminal sets. Step: the accepted set of a stage is the set of states from which some action keeps the tube in the safe set and the successor in the next-stage accepted set; applying Proposition 3(i) to the stage's action sets and the induction hypothesis to the next-stage accepted sets preserves the three-way inclusion at the stage level. (ii) With HOLD the unique prefix action, a prefix state is accepted exactly when it lies in the prefix safe set and in the next-stage accepted set; the stage-0 regions are therefore the witness regions of Theorem 5 pulled back through the (identity) holds, and the strictness witnesses (I ≠ ∅ and the point (½, ⅒, ⅒)) persist. (iii) The three listed mechanisms are each sufficient to erase the gap in a multi-stage setting, so no unconditional generalization is asserted. □

**Theorem 7 (erasure witness).** The propagation claim of Remark 6 is architecture-conditional: there is a two-interval datum whose single-interval truncation exhibits the acceptance gap and whose two-stage extension erases it, through the terminal-coincidence mechanism of Remark 6(iii).

*In words.* A later interval can erase the gap, provided its terminal sets coincide for every weight; the single-interval truncation of the same datum still exhibits the gap.

*Datum.* Two capital forms, floors at zero, the bridge stock absent (x ≡ 0); states are pairs s = (s₁, s₂). Stage 2 (final interval): safe set S₀⁽²⁾ = ℝ² (no path constraint), terminal sets G⁽²⁾ = G^w,⁽²⁾ = G = {s ≥ 0} — coincident for every weight — and a single action REPAIR with tube {s} (safe trivially) and successor (1, 1) ∈ G. Stage 1: safe set S₀ = {s ≥ 0}; two actions with constant tubes, safe at every state of S₀: A1 with successor (s₁ − 1, s₂ + 1) and A2 with successor (s₁ + 1, s₂ − 1); the stage-1 terminal architecture is the stage-2 accepted sets. Initial state z\* = (⅖, ⅖).

In the two-stage datum the gap is erased: REPAIR is typed-admissible — hence w-admissible for every weight — from every state, so V_typ⁽²⁾ = V_w⁽²⁾ = ℝ² for every w; the stage-2 accepted sets coincide. Backward induction then admits both A1 and A2 at z\* (safe tubes; successors in V_typ⁽²⁾ = ℝ²), so z\* is typed-accepted at stage 0, and weak acceptance follows from typed acceptance.

In the single-interval truncation — the same stage-1 datum with the final interval collapsed to its terminal sets, G = {s ≥ 0} and G^w = {w·s ≥ 0} — the gap is present: both successors leave G (s₁ − 1 = −⅗ < 0 and s₂ − 1 = −⅗ < 0), so z\* is typed-rejected. For the weak doctrine, writing r = w₂/w₁ on the interior of the weight cone: A1 is w-admissible exactly when (s₁ − 1) + r(s₂ + 1) ≥ 0, i.e. r ≥ (1 − s₁)/(s₂ + 1) = 3/7; A2 exactly when (s₁ + 1) + r(s₂ − 1) ≥ 0, i.e. r ≤ (s₁ + 1)/(1 − s₂) = 7/3; the two intervals cover [0, ∞] because 3/7 < 7/3, and the boundary weights are covered directly (r = 0: A2 gives w₁(s₁ + 1) ≥ 0; r → ∞: A1 gives w₂(s₂ + 1) ≥ 0). Hence z\* ∈ V_weak in the truncation, and the gap V_weak \ V_typ contains z\*. □

The witness datum of §4.5 is not subject to this erasure. Its gap is tube-driven: on I every member of the four-action menu violates the stage-1 path constraint S₀ itself (the two dips and the bridge deficit of Theorem 5(7)), and a later stage cannot repair a violated tube — the stage-1 constraint is local to stage 1. Remark 6's safe direction is secured by exactly the assumptions the erasure datum violates (unchanged terminal architecture, no new branches). The two results together delimit the persistence claim: hold-prefix extension preserves the separation, arbitrary multi-stage extension does not, and the erasure mechanisms of Remark 6(iii) are realizable.

### 4.9 Machine verification

The continuum statements of Proposition 3, Proposition 4, Theorem 5, Remark 6, and Theorems 7–8 are established by the displayed proofs. An accompanying software artifact (deterministic exact-integer arithmetic; no floating point, tolerances, or randomness) checks the finite rational instance of Proposition 3, Proposition 4, Theorem 5, and Remark 6: the action classifications, the region identities, and the accepted-set identities on a 31³ = 29,791-state grid over (x, s₁, s₂), with a finite verification set containing the critical weight ratios ρ₁, ρ₂ and their midpoint for every enumerated grid state. All 25 checks pass and re-execution reproduces them exactly; they are enumerated in the Supplementary Material (S8).

| Claim layer | What is established | By what |
|---|---|---|
| Continuum statements | Exact identities and inequalities on the witness datum | Displayed proofs |
| Finite rational instance | Classifications on the enumerated grid | Deterministic computation |
| Empirical claims | None in this article | — |

The finite grid does not by itself prove the continuum identities; it validates the symbolic classification on the enumerated instance.

### 4.10 Menu convexification: the blend family

The action space is the finite menu {FAST, SLOW, STAGED, NO-SWITCH} of deterministic actions; fractional or alternating policies are not members of it. The convexification instrument is the blend family: for each δ ∈ (0,1), the action BLEND_δ is the convexified action obtained by fractional allocation of the primitive control flows, u_δ = δ·u_FAST + (1−δ)·u_SLOW. By linearity of the flow map its worst-case tube is the pointwise convex combination of the two primitive worst-case tubes and its successor the convex combination of the two successors. This is menu convexification at the level of control inputs — an explicit model assumption, not the time-sharing of discrete actions in alternation.

**Theorem 8 (blend collapse).** On the witness datum of §4.5, over initial states X₀:

(i) BLEND_δ is typed-admissible at z exactly when

δ ∈ [ 1 − s₂/2, s₁/2 ],

an interval nonempty exactly when s₁ + s₂ ≥ 2 (a singleton at equality), independent of x ≥ 0 and of the weight.

(ii) The typed acceptance set of the menu augmented by the blend family is exactly the compensatory region:

V_typ^blend = { x ≥ 1 } ∪ { s₁ + s₂ ≥ 2 } = V_weak.

Convexification of the menu collapses the acceptance gap: FP_agg vanishes under the augmented menu, and the blend family reaches exactly the compensatory region and nothing beyond — on V_phys \ V_weak no blend is typed-admissible.

(iii) The admissible window depends on the state through (s₁, s₂) alone: a single δ serves every weight w ∈ W₊. On the impossibility region the blend is therefore the common action that no member of the finite menu supplies — the acceptance gap is a property of the deterministic menu, not of the doctrines.

*In words.* A blend is safe exactly when its mixing fraction lies in a window determined solely by the two floors, nonempty exactly on the compensatory region s₁ + s₂ ≥ 2. Adding blends to the menu makes the typed accepted set coincide with the weak one; and a single blend serves every weighting, so the gap was an artifact of the finite menu.

**Proof.** (i) FAST's worst-case tube has s₁-coordinates [s₁ − 2, s₁] and s₂-coordinate {s₂}; SLOW's has s₁-coordinate {s₁} and s₂-coordinates [s₂ − 2, s₂]; both keep x nonnegative throughout (their dips affect only s). The blended tube therefore has s₁-coordinates [s₁ − 2δ, s₁], s₂-coordinates [s₂ − 2(1−δ), s₂], and nonnegative x-coordinates (convex combinations of nonnegative quantities). Typed admissibility requires the tube within S₀ = {x ≥ 0, s ≥ 0} and the successor in G. The tube condition is exactly the displayed window. The successor is the mixture of the two successors, which the datum fixes to the same value — the action table of §4.5 gives both FAST and SLOW the successor (1, x, s + e) — so the blended successor is (1, x, s + e) ∈ G: x ≥ 0 and the destination label is 1. The window is nonempty exactly when 1 − s₂/2 ≤ s₁/2, i.e. s₁ + s₂ ≥ 2; at equality it is the singleton δ = s₁/2 = 1 − s₂/2, feasible because S₀ is closed. On the boundary faces (s₁ = 0 or s₂ = 0) the window is closed at the corresponding endpoint, and the classification follows the boundary conventions of §4.6.

(ii) If s₁ + s₂ ≥ 2, (i) supplies a typed-admissible blend whatever the value of x ≥ 0; if s₁ + s₂ < 2, no blend is typed-admissible by (i), and the deterministic menu contributes exactly V_typ = {x ≥ 1} ∪ {s₁ ≥ 2} ∪ {s₂ ≥ 2} ⊆ {x ≥ 1} ∪ {s₁ + s₂ ≥ 2}. Hence the augmented typed set equals {x ≥ 1} ∪ {s₁ + s₂ ≥ 2} = V_weak by Theorem 5(2) — and nothing beyond, since every admissible blend satisfies s₁ + s₂ ≥ 2 and the deterministic actions stay within V_typ.

(iii) Immediate from the window's state dependence and from typed admissibility implying w-admissibility for every weight. □

**Remark.** The collapse is exact and weight-independent: a single convexified plan serves every assessor on I, where the per-weight plans of Theorem 5(6) necessarily differ. The nonconvexity at work is menu geometry — the finiteness and determinism of the action space — not the Pareto-frontier geometry under which weighted sums fail to reach nonconvex frontier parts (Das and Dennis, 1997); the two mechanisms are distinct. The structure is precisely that of pure-versus-mixed strategies in the assessor–planner game (von Neumann, 1928; Sion, 1958): with the planner picking an action, the assessor a weight, and the payoff the worst-case aggregate, common-plan acceptance is the pure-strategy value and per-weight acceptance the mixed value, the gap being the pure-strategy duality gap that the convex (mixed) extension closes. The two-player reach/avoid formulation of such games is the discriminating kernel of Cardaliaguet (1996), with numerical treatment in Cardaliaguet, Quincampoix, and Saint-Pierre (1999). This is also the here-and-now versus wait-and-see separation of adjustable robust optimization (Ben-Tal et al., 2004).

### 4.11 The converse: discrete time-sharing does not erase the gap

**Proposition 9 (sequential time-sharing does not erase the gap).** On the witness datum of §4.5, let a sequential time-shared policy alternate between FAST and SLOW over the interval, so the set of visited states is the union of the two primitive worst-case tubes. Then such a sequential policy is typed-admissible if and only if s₁ ≥ 2 and s₂ ≥ 2; on the impossibility region I (where s₁ < 2, s₂ < 2, s₁ + s₂ > 2) no such policy is typed-admissible, and the acceptance gap therefore survives discrete time-sharing.

*In words.* Alternating between FAST and SLOW over time is admissible only when each floor separately survives its own dip; the union of the two tubes stays safe exactly when both s₁ ≥ 2 and s₂ ≥ 2. On the impossibility region this never holds, so alternation does not remove the gap.

**Proof.** A sequential policy that spends any positive time on FAST visits every s₁ in [s₁ − 2, s₁] and any positive time on SLOW visits every s₂ in [s₂ − 2, s₂]; the union tube stays within S₀ = {x ≥ 0, s ≥ 0} exactly when both dips are nonnegative, i.e. s₁ ≥ 2 and s₂ ≥ 2. On I both coordinates are strictly below 2, so the union tube is never within S₀ and no sequential policy is typed-admissible; since every member of the finite deterministic menu is typed-admissible on I only in the per-weight sense of Theorem 5(6) (and never in the common sense), the noncompensatory accepted set does not extend to I under sequential time-sharing. □

**Remark.** Together Proposition 9 and Theorem 8 delimit the notion of mixing precisely: continuous convexification — fractional allocation of control flows — closes the acceptance gap exactly at the compensatory region s₁ + s₂ ≥ 2, whereas discrete time-sharing — alternation in time, whose visited set is the union of the action tubes — closes it only where the two dips are independently subsumed, s₁ ≥ 2 and s₂ ≥ 2. On the regime s₁ + s₂ ≥ 2 with min(s₁, s₂) < 2 (which contains the impossibility region) the gap survives sequential time-sharing and closes only under convexification, so the structural character of the gap is a property of the convexity of the action space, not of the assessment doctrine and not of temporal sharing as such.

---

## 5. Interpretation

### 5.1 The doctrinal reading

The scalarized operators {E_w}_{w∈W₊} formalize one compensatory assessment doctrine. The doctrine comprises: a single aggregate index w·s; nonnegative scalarization weights on capital forms; substitution across floors permitted at those weights; and disturbances respected. We refer to this as the scalarized aggregate doctrine as formalized here, not as "weak sustainability" simpliciter. The weak-sustainability literature is broader than this operator: it encompasses aggregate wealth, constant total capital, nondeclining comprehensive consumption, substitutability assumptions, discounting, shadow prices, and intertemporal investment conditions (Neumayer, 2013; World Bank, 2011; Boos, 2015; Dasgupta and Mäler, 2000; Asheim, 1994). Likewise, strong sustainability is not always equivalent to requiring every stock coordinate to remain nonnegative at every instant. Critical-natural-capital frameworks may use thresholds, safe operating spaces, irreversibility, resilience, or minimum-service conditions (Ekins et al., 2003; Doyen and Gajardo, 2020). The typed operator E_typ is a formal idealization of the separately-binding-floor reading, in the same sense that the scalarized operators idealize one aggregation doctrine.

Within this precise scope, Theorem 5 reads as follows. The two formalized doctrines can disagree on the same transition datum, with the same robustness standard and the same action set, in the direction compensatory-accepts / noncompensatory-rejects, on a relatively open region. The disagreement is not an artifact of one bad weight: every weight accepts, each licensing a different physical transition. The plans are genuinely different transitions (FAST and SLOW violate different floors at different times), which is the dynamic formalization of substitution across floors. By Proposition 3(ii), the precise seat of the disagreement is the noncommutativity of "choose an action" with "for all weights."

At the static level the full-cone aggregate is lossless (Remark 2), so the compensatory doctrine's limitation is not the existence of an aggregate index but the policy dependence of the aggregate-feasible transition: the index certifies a set of transitions, none of which the noncompensatory assessment accepts. The two quantifier orders also carry an information reading. ∃a ∀w is a commitment made before the weight is known — the strong doctrine's robustness demand — while ∀w ∃a_w lets the action be chosen after the weight is observed. On the witness, the acceptance gap between the two orders measures the value of information about the assessment weight. Theorem 8 qualifies this reading: a single convexified blend serves every weight on the impossibility region, so the value of information reflects the finite deterministic menu rather than the weight information itself. Proposition 9 sharpens the point: the value of information is removed by convexifying the action space, not by sharing actions in time — under discrete time-sharing the gap (and hence the value of information about the weight) survives on the impossibility region.

Throughout, we use "nonnegative scalarization weights" for elements of W₊ and reserve the word "prices" for the interpretive discussion. Actual prices may be strictly positive, endogenous, dynamically determined, state-dependent, or dimensionally heterogeneous, and the theorems require none of those properties. The operators are linear scalarizations with weights fixed over the review interval. Nonlinear aggregate indices — CES-type substitutability or endogenous, state-dependent weighting of the kind that diverges near zero-stock boundaries — are different assessment operators, and the theorems claim nothing for them.

### 5.2 Positioning against established theory

**Established.** The backward recursion of §3 is a typed instance of established robust-predecessor, reach-avoid, capture-basin, and hybrid-reachability constructions (Aubin, 1991; Aubin, Bayen, and Saint-Pierre, 2011; Saint-Pierre, 1994; Lygeros, Tomlin, and Sastry, 1999); the fixed-point and algebraic character of these objects is developed in Aubin and Catté (2002). Proposition 3(i) is constraint-set monotonicity of viability kernels and reachability sets (Aubin, 1991; Frankowska, 1989). The foundation statement that values may be only weakly comparable — and that this incommensurability is constitutive of ecological economics — is due to Martinez-Alier, Munda, and O'Neill (1998). Our operators give one formal model of the distinction that paper draws between strong and weak commensurability. The characterization of which sustainability criteria admit indicator representations, and the role of maximin and MSY-type reasoning in making strong sustainability operational, are developed in Martinet (2011), Cairns and Martinet (2014), and Doyen and Gajardo (2020). The latter in particular shows that the multicriteria maximin value is the solution of a static Pareto problem over the viability kernel, which is the strongest formal statement in the literature of the position — strong sustainability as constraint viability rather than optimality — that the typed operator formalizes here. Static scalarization limitations are established: weighted sums cannot reach nonconvex parts of Pareto fronts (Das and Dennis, 1997), a mechanism of frontier geometry under a single optimization, different from the action-quantifier mechanism of this paper. Compensability analysis is established in multi-criteria decision analysis, including the explicit mapping of compensatory aggregation to weak sustainability and outranking methods to strong sustainability (Cinelli, Coles, and Kirwan, 2014; Schär, Pohl, and Geldermann, 2025). Scalarization-dependent optimal policies are a staple of multi-objective optimization.

**Proved here.** (i) The action-set identity E_typ = ⋂_{w∈W₊} E_w with the full-cone choice isolating the separation as purely dynamic (Proposition 3(ii)). (ii) The general quantifier-separation remark (Remark 1). (iii) The weight-family monotonicity proposition (Proposition 4). (iv) The explicit exact-tube witness with a relatively open region of strict separation and the rescue/impossibility split (Theorem 5). (v) Persistence of the witness hierarchy under hold-prefix extension (Remark 6). (vi) The explicit two-stage erasure datum delimiting that persistence (Theorem 7). (vii) The blend-collapse theorem, under which menu convexification closes the gap exactly at the compensatory region (Theorem 8), while the converse delimitation (Proposition 9) shows that discrete time-sharing closes it only where both dips are independently subsumed, so the gap survives on the impossibility region.

**Novelty qualification.** To our knowledge, this paper provides an explicit exact-tube witness for this dynamic separation in a compensatory/noncompensatory assessment setting. We do not assert priority over the elementary quantifier fact ∃a ∀w ≠ ∀w ∃a_w, which is standard. Whether an equivalent dynamic separation appears in adjacent literatures (multi-objective robust control, viability theory, multi-criteria decision analysis) is a bounded absence in our review, not an established universal negative.

### 5.3 Scope delimitations

- **No aggregate blindness at fixed trajectories.** By Remark 2, at a fixed trajectory the full-cone aggregate is lossless.
- **No separation on every datum.** Where a single action is safe for all weights, the assessments coincide. The theorem is an existence separation with an open region, plus the always-valid hierarchy and localization.
- **No infinite-horizon, stochastic, partial-observation, or endogenous-event extension.** All statements are for finite-horizon exact-tube data with specified disturbance sets.
- **No claim that the full nonnegative cone is the only reasonable weight family.** Proposition 4 shows that restricting the family enlarges the compensatory accepted set, so the full cone is the strictest compensatory reading, and the separation persists a fortiori for restricted families.
- **No welfare claim about prices.** The weights model an assessment doctrine, not a normative endorsement.
- **No empirical transfer.** The theorems concern assessment operators on a specified datum and imply no empirical claim about any resource system.
- **No claim that V_weak is the genuine-savings or inclusive-wealth criterion.** The operator is the strictest compensatory reading (every weight, each licensing an action). The witness's reserve stock is excluded from the weighted aggregate by construction (§4.5), not by consequence of aggregation.
- **No absolute impossibility.** The impossibility region is a negative certificate relative to the specified four-action menu; with a larger menu it can shrink or vanish (see the completeness requirement in §5.5).
- **No universal doctrinal ranking.** The inclusion V_typ ⊆ V_weak ⊆ V_phys is a theorem about the defined operators under common action and disturbance classes, common safe-set inclusion, common horizon, common tube semantics, and common terminal condition. It does not establish a universal ranking of endpoint, weak, and strong sustainability doctrines.
- **No separation under coupled all-floor shocks.** The witness disturbance convention is action-indexed (§4.5): each action's worst case is its own characteristic dip. A datum whose disturbance class couples simultaneous dips across all floors of every action degenerates the per-weight licensing structure — the principal actions fail together and the compensatory/noncompensatory divergence collapses into universal rejection. The separation is exhibited for, and scoped to, the specified action-indexed class; that the coupled regime is not a remote possibility is indicated by evidence that planetary-boundary processes interact and amplify one another (Lade et al., 2020).
- **Convexification of the menu.** Fractional action policies are not members of the action space, and every stated separation is scoped to the finite deterministic menu. Theorem 8 resolves the convexification question: the blend family collapses the typed acceptance set exactly onto the compensatory region, so the separation is a property of the deterministic menu, not of the doctrines — menu geometry, distinct from the Pareto-frontier geometry of scalarization limits (Das and Dennis, 1997). The associated delimitation (Proposition 9) is that discrete time-sharing does not effect the same collapse: on the impossibility region the gap survives alternation in time, so the structural character of the separation is due to the convexity of the action space, not to temporal sharing.

### 5.4 Policy implications

The separation theorem has four implications.

**First.** Aggregate indices alone cannot certify noncompensatory transition safety under the present assessment semantics. A scalarized assessment can certify its own criterion — aggregate feasibility; what it cannot certify is typed safety unless an additional bridge theorem is supplied. This follows from Theorem 5: the compensatory accepted set strictly contains the noncompensatory accepted set, and the excess region is where the two criteria diverge.

**Second.** When the typed recursion identifies an admissible rescue action whose feasibility is controlled by a resource margin, investment in that margin is a candidate remedy; reweighting alone cannot substitute for it on the witness datum (§5.5). This applies where a resource-controlled rescue action exists; it is not a universal policy claim.

**Third.** Per-floor reporting alongside aggregate reporting is necessary for detecting this class of discrepancy. It is not universally necessary for every sustainability judgement; but where the question is whether a transition respects separately-binding floors, an aggregate index alone cannot distinguish the rescue region from the impossibility region. The same separately-checked-floor logic underlies the safe-and-just-space ("doughnut") literature, which evaluates social thresholds and biophysical ceilings independently, without cross-compensation, and reports that no country satisfies all floors within all ceilings (O'Neill et al., 2018; Fanning et al., 2022). A minimum report for such an assessment should include: (1) typed floors and their provenance; (2) aggregate weights or the weight family; (3) policy quantifiers; (4) the disturbance set; (5) the observation and implementation model; (6) exact versus conservative tube status; (7) terminal maintainability; (8) action-exhaustion status; (9) uncertainty and approximation bounds; (10) normative premises.

**Fourth.** Reporting regimes that evaluate endpoints only, as in audited annual snapshots, evaluate only the weakest operator of the chain of §3.1. Under those semantics they license transitions that violate typed floors mid-interval without detection (on the witness datum, FAST is typed-endpoint-admissible at every state of X₀ but typed-tube-admissible only for s₁ ≥ 2, by inspection of the action table in §4.5); the per-floor reporting of the third implication detects the discrepancy. No empirical claim about any particular reporting regime is made here.

### 5.5 Rescue as action synthesis, and data requirements

**Rescue as action synthesis.** Rescue is an operation on the impossibility region. Define a resource-augmentation map

Aug_κ : (x, s, A) ↦ (x + κ, s, A ∪ {STAGED_κ})

and the minimal rescue threshold

κ\* = inf{ κ : ∃a ∈ A_κ, a ∈ E_typ(z) },

where A_κ denotes the augmented menu.

**Proposition (rescue threshold).** On the witness datum, for every z ∈ X₀,

κ\*(z) = (1 − x)₊ · 1[x < 1, s₁ < 2, s₂ < 2] = (1 − x) · 1[z ∉ V_typ].

*In words.* The minimal augmentation is 1 − x exactly when the state is outside the typed accepted set (x < 1 and both floors below 2), and zero otherwise.

**Proof.** Among the augmented menu, only STAGED_κ depends on κ, and its typed-admissibility is independent of the floors: its x-tube is [x + κ − 1, x + κ], the floors are nondecreasing (they grow to s + e with e = (¼, ¼) > 0), and the successor (1, x + κ − 1, s + e) lies in G exactly when x + κ − 1 ≥ 0. Hence STAGED_κ ∈ E_typ(z) ⟺ x + κ ≥ 1, for every z. If z ∈ V_typ, some base action of A ⊆ A_κ is admissible at κ = 0, so κ\*(z) = 0. If z ∉ V_typ — that is, x < 1 and s₁ < 2 and s₂ < 2 — then NO-SWITCH, FAST, and SLOW all fail (Theorem 5(1)), the only admissible element of A_κ is STAGED_κ, and it is admissible exactly for κ ≥ 1 − x; hence κ\*(z) = 1 − x. □

On the impossibility region I, κ\*(z) = 1 − x > 0; on the rescue set R, and on all of V_typ, κ\*(z) = 0, matching the observation that states of R need no augmentation. Because STAGED_κ is admissible exactly when x + κ ≥ 1, independently of the floors, the resource route admits every state with x < 1 — including states outside V_weak, such as (½, ⅒, ⅒) — at cost 1 − x; the impossibility region is exactly the set on which the four-action menu fails yet resource augmentation succeeds at finite cost. The increment converts an impossibility-region state into a typed-transformable one.

**Remark (error-bound modulus).** Along the resource route the minimal increment is the affine function f(z) = (1 − x)₊, whose error-bound modulus (Fabian et al., 2010) is identically 1 on {x < 1}; the rescue threshold κ\* therefore coincides with the error-bound modulus along this route. The coincidence reflects the linearity of the route. On data with nonlinear resource dynamics the two quantities diverge, and the error-bound modulus governs only the scaling of distance-to-feasibility under unstructured perturbation, a regime outside the present scope (§6.2).

**Data requirements for empirical application.** The theorem is a result about assessment operators on a specified datum. Empirical application requires, in addition to the typed floors, disturbance set, action set, tube model, and destination maintainability witness of §4.5, the following additional specifications:

1. **Action-set completeness status.** A negative certificate over a finite action set proves impossibility only relative to that set. The application must state whether A is exhaustive, a listed policy menu, a sampled subset, or an inner approximation. If incomplete, the verdict is "no safe transition exists among the listed actions," not "no safe transition exists."
2. **Calibration and identifiability data.** Parameter estimates, uncertainty sets, structural alternatives, validation data, observation error, model discrepancy, missing-data treatment, disturbance dependence. A specified disturbance set is necessary but not sufficient; it must be justified, or the verdict marked conditional on model credibility.
3. **Policy and authority data.** Who may select each action, what information they possess, decision timing, enforcement assumptions, compliance uncertainty, strategic responses, resource and legitimacy constraints.
4. **Threshold-uncertainty semantics.** A physical or normative floor is rarely known exactly. Distinguish the deterministic floor sᵢ(z) ≥ 0 from robust threshold safety sᵢ(z; θ) ≥ 0 for all θ ∈ Θ, and from probabilistic or confidence-level versions if admitted.
5. **Destination maintainability status.** Whether the destination maintainability witness is established physically, by simulation, or by assumption.

---

## 6. Discussion

### 6.1 Negative certificates

A negative certificate — a rejection with an exhibited violated constraint for each action, exhausting the action set — is a complete verdict, not an inconclusive one. Theorem 5(7) is an instance: four actions, four exhibited violations, certifying impossibility on I together with the resource threshold of §5.5 and the per-weight licensing thresholds of Theorem 5(6). Related scored forecast-evaluation studies apply assessment discipline of the same kind to the Northern cod and Edwards Aquifer systems (Abaee, 2026b, 2026c); the separation results here rest on their displayed proofs and the machine-checked finite instance of §4.9.

### 6.2 Limitations

1. The separation theorem is an existence result with an open region; it does not imply the gap is large in any given application, and where the assessments coincide it yields nothing.
2. Novelty statements reflect bounded literature search (§5.2).
3. The operators cover finite horizons with exact tubes and specified disturbance sets; infinite horizons, partial observation, stochastic chance constraints, and endogenous event times are not treated.
4. No empirical claims are made.
5. The governance, intergenerational, and composition extensions are stated at partial status in the Supplementary Material and are not used in the proofs.
6. Computational tractability: on a finite explicit state–action–disturbance graph with constant-time predicate evaluation, the backward recursion is polynomial in the graph size and horizon. For continuous, hybrid, or belief-state models, the graph itself may be exponentially large, infinite, or only approximately representable; exact tube inclusion may be computationally hard or undecidable; and grid cardinality grows as N_grid = ∏ᵢ Nᵢ — exponentially in dimension when floors are coordinates. The witness is tractable because its datum is small, finite, and rational.

---

## 7. Conclusions

The weak-sustainability and strong-sustainability traditions are usually compared as doctrines — as different normative stances on substitutability. This paper shows that the divergence of the two doctrines as formalized here — the scalarized-aggregate and typed operators of §3.1 on a common action menu and disturbance class — survives translation into assessment mechanics, at the level of a theorem about those operators. The theorem establishes no ranking of doctrines: §5.1 delimits the formalizations, and by Theorem 8 the structural character of the separation is a property of the finite deterministic menu, not of either tradition (§§4.10–4.11). On a typed transition datum under exact-tube semantics, the compensatory reading (per-weight acceptance) and the noncompensatory reading (common-plan acceptance) are related by a quantifier commutation that can fail on an open region of state space. Where it fails, every scalarization weight certifies a transition, but no single transition is certified by all weights, and the certified set splits into states rescuable by a resource-controlled action and states that are impossible under every weight. The mechanism is not scalarization blindness — at fixed trajectories the full-cone aggregate is lossless — but the policy dependence of the aggregate-feasible transition.

For the construction of composite sustainability indices, the theorem has a concrete consequence. An index can be sound at the level of accounting and still over-certify at the level of assessment, because certification is a quantifier statement about transitions, not a property of a number. Where separately-binding floors matter, per-floor reporting is not a presentation preference but a detection requirement: the aggregate alone cannot distinguish the rescue region from the impossibility region. The bridge a composite index needs — some single transition that serves every admissible weight, i.e. membership in V_typ — is exactly what the frameworks' reporting conventions should be asked to exhibit. Theorem 8 qualifies this requirement: such a single transition is not, in general, a member of the specified deterministic menu but a convexified action, so the relevant question for a reporting convention is whether its action set admits the required menu convexification — and Proposition 9 shows that temporal alternation alone does not provide it.

---

## References

Abaee, A. (2026a). Typed flux ledgers and depletion arithmetic: conservation, componentwise diagnostics, and the semantics of depletion horizons. Zenodo. https://doi.org/10.5281/zenodo.22554177.

Abaee, A. (2026b). Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

Abaee, A. (2026c). Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

Asheim, G. B. (1994). Net national product as an indicator of sustainability. *Scandinavian Journal of Economics*, 96(2), 257–265.

Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser, Boston.

Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). *Viability Theory: New Directions*, 2nd ed. Birkhäuser, Boston.

Aubin, J.-P., and Catté, F. (2002). Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets. *Set-Valued Analysis*, 10(4), 379–416.

Ben-Tal, A., Goryashko, A., Guslitzer, E., and Nemirovski, A. (2004). Adjustable robust solutions of uncertain linear programs. *Mathematical Programming*, 99(2), 351–376.

Boos, A. (2015). Genuine savings as an indicator for "weak" sustainability: Critical survey and possible ways forward in measuring weak sustainability. *Sustainability*, 7(4), 4146–4163.

Cairns, R. D., and Martinet, V. (2014). An environmental-economic measure of sustainable development. *European Economic Review*, 69, 4–17.

Cardaliaguet, P. (1996). A differential game with two players and one target. *SIAM Journal on Control and Optimization*, 34(4), 1441–1460.

Cardaliaguet, P., Quincampoix, M., and Saint-Pierre, P. (1999). Set-valued numerical analysis for optimal control and differential games. In: *Stochastic and Differential Games: Theory and Numerical Methods*, Annals of the International Society of Dynamic Games, vol. 4, Birkhäuser, Boston, 177–247.

Cinelli, M., Coles, S. R., and Kirwan, K. (2014). Analysis of the potentials of multi criteria decision analysis methods to conduct sustainability assessment. *Ecological Indicators*, 46, 138–148.

Daly, H. E. (1990). Toward some operational principles of sustainable development. *Ecological Economics*, 2(1), 1–6.

Das, I., and Dennis, J. E. (1997). A closer look at drawbacks of minimizing weighted sums of objectives for Pareto set generation in multicriteria optimization problems. *Structural Optimization*, 14, 63–69.

Dasgupta, P., and Mäler, K.-G. (2000). Net national product, wealth, and social well-being. *Environment and Development Economics*, 5(1), 69–93.

Doyen, L., and Gajardo, P. (2020). Sustainability standards, multicriteria maximin, and viability. *Natural Resource Modeling*, 33(3), e12250.

Ekins, P., Simon, S., Deutsch, L., Folke, C., and De Groot, R. (2003). A framework for the practical application of the concepts of critical natural capital and strong sustainability. *Ecological Economics*, 44(2), 165–185.

Fabian, M. J., Henrion, R., Kruger, A. Y., and Outrata, J. V. (2010). Error bounds: necessary and sufficient conditions. *Set-Valued Analysis*, 18(2), 121–149.

Fanning, A. L., O'Neill, D. W., Hickel, J., and Roux, N. (2022). The social shortfall and ecological overshoot of nations. *Nature Sustainability*, 5(1), 26–36.

Frankowska, H. (1989). Optimal trajectories associated with a solution of contingent Hamilton–Jacobi equations. *Applied Mathematics and Optimization*, 19, 291–311.

Hanley, N., Moffatt, I., Faichney, R., and Wilson, M. (1999). Measuring sustainability: A time series of alternative indicators for Scotland. *Ecological Economics*, 28(1), 55–73.

Hickel, J. (2020). The sustainable development index: Measuring the ecological efficiency of human development in the Anthropocene. *Ecological Economics*, 167, 106331.

Lade, S. J., Steffen, W., de Vries, W., Carpenter, S. R., Donges, J. F., Gerten, D., Hoff, H., Newbold, T., Richardson, K., and Rockström, J. (2020). Human impacts on planetary boundaries amplified by Earth system interactions. *Nature Sustainability*, 3(2), 119–128.

Lygeros, J., Tomlin, C., and Sastry, S. (1999). Controllers for reachability specifications for hybrid systems. *Automatica*, 35(3), 349–370.

Martinez-Alier, J., Munda, G., and O'Neill, J. (1998). Weak comparability of values as a foundation for ecological economics. *Ecological Economics*, 26(3), 277–286.

Martinet, V. (2011). A characterization of sustainability with indicators. *Journal of Environmental Economics and Management*, 61(2), 183–197.

Neumayer, E. (2013). *Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms*, 4th ed. Edward Elgar, Cheltenham.

O'Neill, D. W., Fanning, A. L., Lamb, W. F., and Steinberger, J. K. (2018). A good life for all within planetary boundaries. *Nature Sustainability*, 1(2), 88–95.

Saint-Pierre, P. (1994). Approximation of the viability kernel. *Applied Mathematics and Optimization*, 29, 187–209.

Schär, S., Pohl, E., and Geldermann, J. (2025). Analysing the compensatory properties of the outranking approach PROMETHEE. *Journal of Multi-Criteria Decision Analysis*, 32, e70013.

Sion, M. (1958). On general minimax theorems. *Pacific Journal of Mathematics*, 8(1), 171–176.

Solow, R. M. (1974). Intergenerational equity and exhaustible resources. *Review of Economic Studies*, 41, 29–45.

Usubiaga-Liaño, A. (2025). Strong sustainability in the SEEA and the wider indicator debate. *One Ecosystem*, 10, e141086.

von Neumann, J. (1928). Zur Theorie der Gesellschaftsspiele. *Mathematische Annalen*, 100, 295–320.

World Bank. (2011). *The Changing Wealth of Nations: Measuring Sustainable Development in the New Millennium*. World Bank, Washington, D.C.

---

## Supplementary Material

Framework extensions (governance constructors, the implementability ladder, the commons obstruction, intergenerational structures, the nested-impossibility theorem, composition interfaces), the planetary-boundaries application note, the full framework definitions, and the conjectures are given in the accompanying Supplementary Material, which also enumerates the machine artifact's 25 checks (S8).

---

## Declarations

**Data availability statement.** The proofs are contained in this article. The verification code for the finite rational instance (all 25 checks; deterministic exact-integer arithmetic) is archived in a public repository; a link is provided with the submission.

**Declaration of competing interest.** None.

**AI declaration.** GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.

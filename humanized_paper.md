# The Limits of Compensatory Aggregation — A Plain-Language Reading

*A faithful, humanized version of "The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment" by Amin Abaee (2026).*

*Everything substantive in the original paper is preserved here. Nothing has been added or removed; the mathematics has simply been translated into everyday language, with the notation kept alongside so you can match it back to the original.*

---

## TL;DR

Sustainability assessments usually boil a lot of different things — natural resources, money, clean water, biodiversity — down into **one single number** (an "index" or "aggregate"), on the assumption that a shortfall in one area can be **paid for** by a surplus in another. This is the "weak sustainability" idea.

"Strong sustainability" says the opposite: some things are separately important and can't be traded against each other. Each of them must be kept above its own minimum, on its own.

The paper's key finding is about a subtle but real difference between two ways of asking "is this plan sustainable?":

1. **Is there one single plan that works no matter how the index is weighted?** *(the strong, noncompensatory question)*
2. **For each possible weighting, is there *some* plan that works — even if it's a different plan for each weighting?** *(the weak, compensatory question)*

These two questions are **not** equivalent. The paper builds a tiny, concrete example (a "witness") where every weighting individually accepts *some* plan, but **no single plan passes under all weightings at once**. So an aggregate index can look perfectly sound — every weighting says "fine!" — and yet certify transitions that a floor-by-floor (strong) assessment rejects.

The example also shows exactly where this happens (the "impossibility region"), how to fix it (spend a resource margin), and — crucially — that the whole problem disappears if you're allowed to run plans *simultaneously in fractional mixes*, but **not** if you merely *alternate* between them over time. The gap is a property of the limited menu of actions, not of the sustainability philosophies themselves.

---

## 1. Introduction

### 1.1 Two failure modes

Sustainability assessment has been split down the middle since the field began.

- **Weak sustainability** — the tradition behind "genuine savings" and "inclusive wealth" accounting (World Bank, 2011; Boos, 2015; Neumayer, 2013) — treats different forms of capital as **substitutable through prices**. A decline in one stock is fine as long as the *total* value of the capital base doesn't fall.
- **Strong sustainability** holds that some stocks and services are **separately binding** — "critical natural capital" whose loss can't be made up at any price (Daly, 1990; Ekins et al., 2003). Its foundation in ecological economics is the idea of **weak comparability**: the values relevant to environmental decisions may not be measurable on a single scale at all (Martinez-Alier, Munda, and O'Neill, 1998).

This debate is well developed in policy and multi-criteria decision research (Cinelli, Coles, and Kirwan, 2014; Schär, Pohl, and Geldermann, 2025; Hanley et al., 1999; Usubiaga-Liaño, 2025), and the theory of sustainability indicators is correspondingly mature (Martinet, 2011; Cairns and Martinet, 2014) — including the "maximin" view, where strong sustainability emerges from whether the constraints can be *survived*, not from any optimization target (Solow, 1974; Doyen and Gajardo, 2020).

**In this paper's terms**, the two traditions differ on one question: **does compensatory substitution keep pace with depletion?** (A companion study, Abaee 2026a, treats the "material-cycle" reading of that question — waste, closing material loops, deep-time renewal. This paper doesn't re-argue that; no theorem here concerns material cycles. The only doctrines compared here are the two formal *operators* defined in Section 3.1, discussed doctrinally in Section 5.1.)

The question asked here is the **certification** form of that distinction. The "blend-collapse" result (Theorem 8) closes the acceptance gap exactly on the *compensatory region* — where substitution via fractional splitting of control flows keeps pace. The "impossibility region" (Theorem 5(4)) marks where substitution doesn't keep pace, even under discrete time-sharing. Substitution is only allowed through an identified physical pathway; nothing is assumed to be compensable merely because a weighted total permits it. Whether "total capital can be maintained" is genuinely **ambiguous between two orders of the quantifiers** "for all" and "there exists" — made precise in Remark 1 and Section 4.5.

The paper targets a question the indicator literature has left open: the **dynamic** question. *During a sustainability transition, when can a compensatory aggregate certify a path that a noncompensatory assessment rejects?* Two failure modes motivate it.

**Failure mode 1: commensurability drift.** Assessments lump stocks, services, liabilities, and floors into single indices whose compensation rules are rarely stated as explicit mathematics. Composite indices are routinely criticized on exactly this ground: the weights they embed are value judgements dressed up as measurement (Hickel, 2020; Martinez-Alier, Munda, and O'Neill, 1998). That critique usually targets the *choice* of weights. The stronger finding here is that **no choice of weights fixes the problem**. The failure is structural — it lives in the logic of aggregation itself.

**Failure mode 2: conditional results circulating as unconditional ones.** So every result below states its assumptions and status explicitly.

**What the masking looks like, concretely.** A total of two "typed floors" (two separately-tracked minimum requirements) can stay nonnegative along its worst-case path while each floor *in turn* dips below zero in a way no common plan accepts. This is different from the "productivity illusion" — delivering adequately from a shrunken productive base — treated in Abaee (2026a). On the example below, the aggregate is taken over the two floors *s₁, s₂* themselves; what it fails to detect is the *individual floor mid-way through the interval* — the compensatory form of the illusion, i.e. the acceptance gap of Theorem 5(4).

### 1.2 The central result

The paper's organizing idea is a **quantifier noncommutation** — "there exists" and "for all" don't swap safely.

**The setup.** Fix a "typed transition datum": a state space with typed floors *sᵢ ≥ 0* (normalized so that zero is the binding limit), a set of actions, a set of disturbances, and **exact-tube semantics** — a transition counts as safe only if *every state visited along the way*, not just the endpoint, satisfies the constraints.

For each nonnegative weighting *w* in the "full cone" *W₊ = ℝⁿ₊ \ {0}* (all nonnegative weight vectors except the all-zero one):
- *E_w(z)* = the actions allowed at state *z* under the **aggregate** floor *w·s ≥ 0*.
- *E_typ(z)* = the actions allowed under the **typed** floors *sᵢ ≥ 0*, each taken separately.

Two acceptance criteria then differ **only by the order of the quantifiers**:

- **Common-plan acceptance (noncompensatory).** There exists *one* action lying in *every* *E_w(z)*:
  > ∃a ∀w : a ∈ E_w(z)
- **Per-weight acceptance (compensatory).** For each weight there exists *some* admissible action, possibly a different one for each weight:
  > ∀w ∃a_w : a_w ∈ E_w(z)

The first implies the second; **the reverse fails**. And the failure isn't the fault of any particular weight — it's the fact that "there exists an action" and "for all weights" don't commute. This is the assessment-theory version of the classic strict **minimax** pattern in game theory: for the yes/no question "is action *a* admissible at *z* under weight *w*?", the two quantifier orders are the two orders of the minimax interchange, and the example in Section 4.5 shows the interchange failing strictly.

- Remark 1 states the always-valid one-way inclusion.
- Proposition 3(ii) identifies the noncompensatory operator with the "common plan" set over the full cone.
- Theorem 5 exhibits an explicit, concrete example on which the acceptance gap *FP_agg = V_weak \ V_typ* is a region with nonempty interior — the **impossibility region** (Theorem 5(4)).
- The example also splits the aggregate-vs-direct-floor discrepancy region *Q* by a **resource threshold** into the impossibility region and the **rescue set** — states that are *already* transformable through the resource-controlled action (Theorem 5(7)). The rescue operation of Section 5.5 (resource augmentation) acts on the impossibility region, **not** on the rescue set.

### 1.3 Contribution and scope

**Contributions.** (i) The action-set identity *E_typ(z) = ⋂_{w∈W₊} E_w(z)* — with the full-cone choice (the cone *minus the origin*) isolating the separation as purely dynamic (Proposition 3(ii)). (ii) A general quantifier-separation remark (Remark 1). (iii) Monotonicity of the accepted-state hierarchy in the weight family (Proposition 4). (iv) An explicit rational example with an open region of strict separation, the discrepancy-region split *Q = R ∪ I*, the identity *FP_agg = I*, exact per-weight licensing thresholds (Theorem 5), and the rescue-threshold identity *κ\* = 1 − x* (Proposition, Section 5.5). (v) Persistence of the separation under "hold-prefix" extension of the horizon (Remark 6). (vi) An explicit two-stage example where a later interval *erases* the gap (Theorem 7), bounding the persistence claim. (vii) The blend-collapse theorem: "convexifying" the menu closes the gap exactly at the compensatory region (Theorem 8), while the converse (Proposition 9) shows that discrete time-sharing — where the visited set is the union of the action paths — closes it only where both dips are independently covered, so the gap survives on the impossibility region.

**Scope (what this paper does NOT claim).** No universal ranking of weak- vs. strong-sustainability doctrines; no proof that any particular set of environmental boundaries *ought* to be treated noncompensatorily; no empirical result about any specific resource system. The governance, intergenerational, and composition extensions are stated only at partial status in the Supplementary Material.

To the author's knowledge, this provides an explicit exact-tube example of this dynamic separation in a compensatory/noncompensatory assessment setting; the elementary quantifier fact behind it is standard, and Section 5.2 states the full novelty qualification.

---

## 2. A Typed Framework for Transition Assessment

This section fixes the definitions the theorems need.

### 2.1 Types and physical state

Physical state is **typed**. A state variable denotes a **moiety** — a named, conserved substance — with a unit, and typed fluxes connect typed stocks. Conservation is tracked **per-moiety**; the framework does *not* authorize adding biomass, money, and biodiversity into one conserved scalar. Services, thresholds, information states, and institutional variables are **separate types**. No statement combines quantities of different type except through an explicit bridge. Typing does two jobs: it makes the domain of every conservation law explicit, and it records the *provenance* of every floor — physical, contractual, or normative — as part of the floor's type.

### 2.2 The assessment datum

The results use a "typed exact-tube transition datum": a state space *Z* carrying typed floors *sᵢ ≥ 0* (normalized at zero), an action set, a disturbance class *D*, a typed safe set *S*, a destination set *G*, and tube/successor maps Tube(a,d) and Succ(a,d) as defined in Section 3.1. A transition is safe only if **every state visited along it**, not merely its endpoint, satisfies the constraints. The example of Section 4.5 is an instance of this datum.

### 2.3 Quantifier discipline

Every assessment operator evaluates the disturbance quantifier **innermost**: for an action to be admissible, it must be safe for *every* disturbance *d ∈ D*. The separation studied in Section 3 concerns a *second* quantifier — over scalarization weights — placed outside that one: the noncommutation under study is **∃a ∀w** versus **∀w ∃a_w**.

### 2.4 The characters in this story (notation)

- **z ∈ Z** — a state; **a** — an action; **d ∈ D** — a disturbance.
- **s = (s₁, …, sₙ)** — typed floors, normalized so that *sᵢ ≥ 0* is the binding constraint.
- **x** — the reserve stock ("bridge stock") on the example.
- **W₊ = ℝⁿ₊ \ {0}** — the full nonnegative scalarization cone, minus the origin; **w ∈ W₊** — a nonnegative weight; a subfamily is written *W*; **r = w₂/w₁** — the weight ratio used on the example (the resource increment of Section 5.5 is *κ*).
- **S** = physical safe set ∩ {sᵢ ≥ 0 for all i}; **G** = physical destination set ∩ {s ≥ 0} — the typed safe and destination sets; *S^w, G^w* their weighted ("scalarized") counterparts; on the example *S = S₀*.
- **Tube(a,d)** — the full set of states visited during the interval under action *a* and disturbance *d*; **End(a,d)** — the endpoint values; **Succ(a,d)** — the successor set after any endpoint reset.
- **E_typ, E_w, E_tube,phys, E_end, E_end,typ** — the assessment operators of Section 3.1.
- **V[E] = {z : E(z) ≠ ∅}** — the accepted-state set of operator *E*; in particular *V_typ, V_w, V_weak = ⋂_w V_w, V_phys, V_end*.
- **The example (Section 4.5):** phase state *(q, x, s₁, s₂)*; gain vector *e = (¼, ¼)*; rescue cost *c = 1*; depth of the worst-case dip = 2; menu {NO-SWITCH, FAST, SLOW, STAGED}.
- **Discrepancy sets (Section 4.6):** *Q* — the aggregate-vs-direct-floor discrepancy region; *R* — rescue set; *I* — impossibility region; *FP_agg = V_weak \ V_typ* — the genuine acceptance gap; *ρ₁, ρ₂* — the per-weight licensing thresholds.
- **A** — the action set; **Aug_κ** — the resource-augmentation map, with increment *κ* and minimal rescue threshold *κ\**.
- The gain vector *e* of the example and the standard basis vector *e_k* of Remark 2 are **distinct** objects.

---

## 3. Assessment Operators

### 3.1 Five operators

Fix a typed exact-tube transition datum with transition-safe sets and a destination set. Five operators are distinguished. They share the same disturbance quantifier and differ in constraint structure, except that the endpoint operator swaps tube evaluation for endpoint evaluation. The fifth is the typed-endpoint operator, used in Section 5.4.

**The noncompensatory (typed) operator** — each floor separately binding:
> E_typ(z) = { a : for all d, Tube(a,d) ⊆ S and Succ(a,d) ⊆ G },
where *S = S^phys ∩ {sᵢ ≥ 0, i = 1..n}* and *G = G^phys ∩ {s ≥ 0}*.

**The scalarized (aggregate) operator at weight w**:
> E_w(z) = { a : for all d, Tube(a,d) ⊆ S^w and Succ(a,d) ⊆ G^w },
where *S^w = S^phys ∩ {w·s ≥ 0}* and *G^w = G^phys ∩ {w·s ≥ 0}*.

**The exact-tube physical operator** (physical constraints only, full tube):
> E_tube,phys(z) = { a : for all d, Tube(a,d) ⊆ S^phys and Succ(a,d) ⊆ G^phys }.

**The endpoint-only physical operator** (physical constraints at endpoints only):
> E_end(z) = { a : for all d, End(a,d) ⊆ S^phys and Succ(a,d) ⊆ G^phys }.

The endpoint operator represents aggregated accounting evaluated on **audited snapshots**, while typed floors constrain the **whole trajectory**: evaluation on the full tube versus evaluation on endpoints only. *The endpoints are the photograph; the tube is the trajectory.* Endpoint values can't in general certify the condition of the system that produced them (cf. the productivity-illusion analysis in Abaee, 2026a); the typed-endpoint operator below states the floor-level version of this exactly on the example.

Because *End(a,d) ⊆ Tube(a,d)*, the endpoint operator is the weakest, and the chain
> E_typ(z) ⊆ E_w(z) ⊆ E_tube,phys(z) ⊆ E_end(z)

holds for every *w ∈ W₊* (Proposition 3(i) below). The last inclusion is strict in general, though it collapses on the example of Section 4.5 because there the physical constraint involves only the monotone reserve stock.

**Definition (typed-endpoint operator).** Evaluates typed floors at endpoints only:
> E_end,typ(z) = { a : for all d, End(a,d) ⊆ S and Succ(a,d) ⊆ G }.

It satisfies *E_typ(z) ⊆ E_end,typ(z) ⊆ E_end(z)*. On the example, FAST's endpoint values of *s₁* equal the initial *s₁* and its successor lies in *G* whenever *x ≥ 0*, so *E_end,typ(z) ≠ ∅* at every state of *X₀*, while *E_typ(z) ≠ ∅* requires *s₁ ≥ 2* (Theorem 5(1)). (This observation follows by inspection of the action table and is **not** part of the machine-checked artifact of Section 4.9.)

### 3.2 Accepted-state operators

For any operator *E*, write *V[E] = { z : E(z) ≠ ∅ }* for the set of states where *E* admits at least one action. The central noncommutation is then:

> { z : ⋂_w E_w(z) ≠ ∅ } *(the common plan)*  ⊆  ⋂_w { z : E_w(z) ≠ ∅ } *(per weight)*

i.e. *V_typ* ⊆ *V_weak*.

---

## 4. Results: The Separation Theorem

### 4.1 A general quantifier-separation remark

**Remark 1.** For any family of action sets {E_λ(z)}, it is *always* true that
> { z : ⋂_λ E_λ(z) ≠ ∅ } ⊆ ⋂_λ { z : E_λ(z) ≠ ∅ }.

**In plain terms:** if one action works for every λ at once, then certainly *something* works for each λ individually. **Equality holds exactly when** the family admits a "common selector" — one action that works for all of them. No topology on the action space is imposed. In finite menus the check is combinatorial: if the action set is finite, only finitely many distinct E_λ(z) occur and common-selector existence is a finite enumeration (on the example, there are 4 actions). For infinite families, classical sufficient conditions exist (the finite-intersection property plus compactness/closedness in a specified topology) but aren't needed here.

The separation in Section 4.5 is a **strict** instance of this inclusion, at states where the nonemptiness witnesses differ with the weight.

### 4.2 The full-cone identity

**Remark 2 (full-cone pointwise equivalence).** For a vector *v*:
> *v ≥ 0 componentwise* ⟺ *w·v ≥ 0 for every w ∈ W₊*.

**In plain terms:** if every nonnegative weighted sum of a vector is nonnegative, then every component is nonnegative — and vice versa. (The forward direction is obvious; for the reverse, if some component *v_k < 0*, take *w = e_k*, the weight that puts everything on that component, and the sum goes negative.)

So at a **fixed** trajectory the full-cone aggregate is **lossless**: requiring every weighted sum to be nonnegative is exactly the same as requiring each component to be nonnegative. The separation below is therefore **entirely dynamic** — a matter of quantifier order — **not** static "scalarization blindness."

### 4.3 The assessment identity and hierarchy

**Proposition 3 (assessment identity and hierarchy).**

- **(i) Hierarchy.** For every *w ∈ W₊* and every *z*:
  > E_typ(z) ⊆ E_w(z) ⊆ E_tube,phys(z) ⊆ E_end(z).
- **(ii) Localization.** For every *z*:
  > E_typ(z) = ⋂_{w∈W₊} E_w(z),  hence *V_typ = { z : ⋂_w E_w(z) ≠ ∅ }*.

**Why this is true.** (i) If an action keeps every floor nonnegative along the tube, then (by Remark 2) it keeps every weighted sum nonnegative too — so it passes the aggregate test; and the physical test is looser still, since the aggregate constraints are stricter than the purely physical ones, and the endpoint test is loosest since endpoints are a subset of the tube. (ii) If an action passes *every* weighted-aggregate test, then at every tube point every weighted sum is nonnegative, so (again by Remark 2) every floor is nonnegative — meaning the action passes the typed test.

Part (i) is standard constraint-set monotonicity under nested safe sets (Aubin, 1991; Frankowska, 1989); part (ii) is proved above, and its strictness is witnessed in Theorem 5.

### 4.4 Weight-family monotonicity

**Proposition 4.** For a weight family *W ⊆ W₊*, define *V_W = ⋂_{w∈W} V_w*. Then
> V_typ ⊆ V_W ⊆ V_phys,

and if *W₁ ⊆ W₂* then *V_W₂ ⊆ V_W₁*.

**In plain terms:** **restricting the weight family enlarges the compensatory accepted set.** The full cone is therefore the *strictest* compensatory reading, and any separation exhibited at the full cone persists for every restricted family. (Intuition: if you only have to satisfy a smaller set of assessors, more states look acceptable.)

### 4.5 The witness datum

This is the paper's concrete example — a small, explicit "typed transition datum" on which the separation of Theorem 5 is shown.

Two architectures — **extraction** (*q = 0*) and **regeneration** (*q = 1*) — share one review interval [0, 1], with phase state *(q, x, s₁, s₂)*:

- **x** — a physical reserve stock.
- **s₁** — a "protected-group service surplus" floor.
- **s₂** — a "remediation-liability coverage" floor.

Both floors are normalized to 0. The transition-safe set is *S₀ = {x ≥ 0, s₁ ≥ 0, s₂ ≥ 0}*; the destination set is *G = {(1, x, s) : x ≥ 0, s ≥ 0}*, with destination maintainability witnessed by a "destination hold policy." The destination reset applies the gain vector *e = (¼, ¼)* to both floors; since *e* is strictly positive, successors are interior to *G*, and no inequality in Theorem 5 depends on its exact size. The **rescue cost** is *c = 1* (STAGED spends one unit of *x*).

**Disturbance convention (action-indexed).** The disturbance set is {β, α}, where α triggers the worst-case dip — of fixed depth 2 — in the *active action's characteristic coordinate* (*s₁* for FAST, *s₂* for SLOW), and β is the analogous disturbance on the other coordinate. The two disturbances are never required to hit a coordinate the action doesn't move. Each action's worst-case tube is the tube under its own characteristic dip. A disturbance label shared across the two actions still only takes effect on the coordinate each action moves, so FAST's *s₂*-tube and SLOW's *s₁*-tube are unchanged, and this convention doesn't affect the separations of Theorem 5.

**The four actions** (piecewise-linear maps on the breakpoints {0, ½, 1}, monotone on each piece — so every tube is the exact visited set, with no outer approximation):

| Action | Within-interval trajectory (worst case) | Successor |
|---|---|---|
| **NO-SWITCH** | state constant | {(0, x, s)} — misses *G* |
| **FAST** | *s₁* falls at rate 4 to its lowest point at *t = ½*, then rises back to its start; *s₂, x* constant | {(1, x, s + e)} |
| **SLOW** | symmetric: *s₂* dips the same way; *s₁, x* constant | {(1, x, s + e)} |
| **STAGED** | *x* falls from *x* to *x − 1* over [0,1]; floors grow to *s + e* | {(1, x − 1, s + e)} |

So FAST's worst-case tube spans *[s₁ − 2, s₁]* in the *s₁* coordinate (with *s₂, x* constant); SLOW's is symmetric; STAGED's is *[x − 1, x]* in the *x* coordinate (with both floors nondecreasing).

### 4.6 Witnessed separation

**Theorem 5 (witnessed separation).** On the example above, over initial states *X₀ = {(0, x, s) : x ≥ 0, s ≥ 0}*:

1. **V_typ = {x ≥ 1} ∪ {s₁ ≥ 2} ∪ {s₂ ≥ 2}.** *(The strong test passes if the reserve can cover a staged rescue, or if either floor is deep enough to survive its own worst-case dip.)*

2. **V_weak = ⋂_{w∈W₊} V_w = {x ≥ 1} ∪ {s₁ + s₂ ≥ 2}.** *(The weak test passes if the reserve covers the rescue, or if the two floors *together* total at least 2.)*

3. **V_phys = V_end = X₀.** *(Ignoring the floors, everything is fine.)*

Define:
- **Q = {s₁ < 2, s₂ < 2, s₁ + s₂ ≥ 2}** — the aggregate-vs-direct-floor discrepancy region (*x* unrestricted). This is **not** entirely a false-positive set: for *x ≥ 1*, STAGED is typed-admissible.
- **R = Q ∩ {x ≥ 1}** — the **rescue set**: the already-typed slice of the discrepancy region, transformable at cost *c = 1* via STAGED.
- **I = Q ∩ {x < 1}** — the **impossibility region**.
- **FP_agg = V_weak \ V_typ** — the genuine compensatory-vs-noncompensatory acceptance gap.

4. **FP_agg = I.** The genuine acceptance gap is exactly the impossibility region; it is nonempty, and its relative interior (in the *q = 0* slice) is {0 < x < 1, 0 < s₁ < 2, 0 < s₂ < 2, s₁ + s₂ > 2}. The rescue set *R* is a subset of *V_typ*, **not** of the gap — it's the part of *Q* that is *not* a false positive.

5. **Both hierarchy inclusions are strict.** Every point of *I* lies in *V_weak \ V_typ* (so the first inclusion is strict), and the point *(x, s₁, s₂) = (½, ⅒, ⅒)* lies in *V_phys \ V_weak* (so the second is strict too).

6. **Per-weight plan disagreement.** On the relative interior of *Q* (where 0 < s₂ < 2), writing *r = w₂/w₁*, the FAST-certifying weight ratios are exactly {r ≥ ρ₁} and the SLOW-certifying exactly {r ≤ ρ₂}, with
   > ρ₁ = (2 − s₁)/s₂,  ρ₂ = s₁/(2 − s₂),  and ρ₂ ≥ ρ₁ ⟺ s₁ + s₂ ≥ 2.

   Assessors who put a lot of weight on *s₂* (*r > ρ₂*) license **FAST only**; assessors who put little weight on *s₂* (*r < ρ₁*) license **SLOW only**; intermediate assessors license both. On *I*, no single action serves every weight — *⋂_w E_w(z) = E_typ(z) = ∅* — while on *R*, STAGED is typed-admissible and hence serves every weight.

7. **The rescue split.** *R* is typed-transformable via STAGED: bridging at physical cost *c = 1* keeps both floors intact and lands in *G*. *I* is aggregate-feasible for every cone weight yet admits **no** typed-admissible action, with four exhibited violations: **FAST** violates the *s₁* floor under the adverse disturbance; **SLOW** violates the *s₂* floor; **STAGED** drives *x* negative; **NO-SWITCH** misses *G*.

**Proof sketch.** (1) NO-SWITCH never reaches *G*, so it's never admissible. FAST is admissible exactly when *s₁ ≥ 2* (its dip must stay nonnegative), SLOW exactly when *s₂ ≥ 2*, and STAGED exactly when *x ≥ 1* (its *x*-tube must stay nonnegative). (2) Fix *w*. FAST is *w*-admissible exactly when *w₁(s₁ − 2) + w₂s₂ ≥ 0*; SLOW exactly when *w₁s₁ + w₂s₂ ≥ 2w₂*; STAGED exactly when *x ≥ 1*. Assembling the three cases (x ≥ 1; or one floor ≥ 2; or both floors < 2, where the two licensing intervals must jointly cover all weights — which happens exactly when s₁ + s₂ ≥ 2) gives the formula. (3) Physically, only *x ≥ 0* matters, and FAST/SLOW keep *x* constant and nonnegative everywhere in *X₀*. (4)–(7) follow by set arithmetic and inspection of the four actions.

**Boundary conventions.** The formulas for ρ₁, ρ₂ require *s₂ > 0* and *s₂ < 2*. On boundary faces (s₂ = 0, s₂ = 2, s₁ = 0, s₁ = 2, s₁ + s₂ = 2), the classification follows directly from the closed-set identities of (1)–(2); no interior formula is applied there.

**The takeaway in one sentence.** The compensatory assessment's binding condition is the **total budget** *s₁ + s₂ ≥ 2*; the noncompensatory assessment requires either **one floor to survive its own worst-case dip** (*sᵢ ≥ 2*) or **the bridge stock to cover the rescue cost** (*x ≥ 1*). The region between the two conditions is where the compensatory doctrine certifies — per weight, with weight-dependent plans — transitions the noncompensatory doctrine rejects.

### 4.7 Figure 1 (described)

The discrepancy region *Q* is the part of the square 0 ≤ s₁, s₂ ≤ 2 on or above the line s₁ + s₂ = 2: the closed upper-right triangle with vertices (0,2), (2,0), (2,2), minus its two legs s₁ = 2 and s₂ = 2 (strict boundaries). Its interior is 0 < s₁, s₂ < 2 with s₁ + s₂ > 2.

- **Panel A (x < 1, shown at x = 0):** the region is the genuine impossibility region *I = FP_agg*; the interior witness (s₁, s₂) = (6/5, 6/5) is marked.
- **Panel B (x ≥ 1, shown at x = 1):** the same region is the rescue set *R*, witnessed by STAGED.

The threshold curves ρ₁, ρ₂ are drawn only on the open subregion where s₁ > 0, s₂ > 0, s₂ < 2. The point (x, s₁, s₂) = (½, ⅒, ⅒) — which lies outside the s-plane section — is annotated in Panel A. The region is the rescue set at x ≥ 1 and the impossibility region at x < 1; **only the latter is a false positive.**

### 4.8 Propagation under hold-prefix extension

This subsection asks: does the one-interval separation survive if the horizon is lengthened by **prepending hold intervals** (waiting periods)? Two results bound the answer. Remark 6 establishes persistence under a precisely specified hold-prefix extension; Theorem 7 exhibits a two-stage datum where the gap is **erased**, showing the persistence claim is architecture-conditional.

**Remark 6 (propagation).** Extend the example to m ≥ 2 review intervals by prepending hold intervals (sole action HOLD: constant tube {z}, successor {z}, safe set S₀; the final interval carries the witness). Assume:
- (H1) HOLD is available at every prefix state;
- (H2) the hold tube is exactly {z};
- (H3) the prefix safe sets contain the witness states;
- (H4) terminal and successor architecture labels are unchanged;
- (H5) no additional reset or disturbance branches are introduced.

Then:
- **(i) Hierarchy.** At every stage *j*, V_typ_j ⊆ ⋂_{w∈W₊} V^w_j ⊆ V_phys_j. (This holds for *every* multi-interval typed exact-tube datum; it's constraint monotonicity under backward induction.)
- **(ii) Persistence of strictness.** The stage-0 accepted regions are the witness regions pulled back through the holds, so both strictness witnesses of Theorem 5 persist.
- **(iii)** The displayed separation is **not** an artifact of the one-interval framing for this constructed datum. But strictness for *arbitrary* multi-stage systems does **not** follow without a separate persistence theorem: a later stage can erase the gap if (a) every aggregate-feasible state has a common typed-safe continuation, (b) the weak and typed terminal sets coincide on the reachable subset, or (c) actions couple across stages.

**Theorem 7 (erasure witness).** The propagation claim of Remark 6 is architecture-conditional: there is a two-interval datum whose single-interval truncation exhibits the acceptance gap, and whose two-stage extension **erases** it (through the terminal-coincidence mechanism).

- **Datum.** Two capital forms, floors at zero, no bridge stock (*x ≡ 0*); states are pairs *s = (s₁, s₂)*. **Stage 2 (final interval):** safe set = ℝ² (no path constraint), terminal sets coincide for every weight (all equal {s ≥ 0}), and a single action REPAIR with tube {s} and successor (1, 1) ∈ G. **Stage 1:** safe set {s ≥ 0}; two actions with constant tubes: **A1** → successor (s₁ − 1, s₂ + 1), **A2** → successor (s₁ + 1, s₂ − 1). Initial state z\* = (⅖, ⅖).
- **Two-stage: gap erased.** REPAIR is typed-admissible from every state, so the stage-2 accepted sets coincide; backward induction then admits both A1 and A2 at z\*, so z\* is typed-accepted at stage 0.
- **Single-interval truncation: gap present.** Both successors leave G (s₁ − 1 = −⅗ < 0 and s₂ − 1 = −⅗ < 0), so z\* is typed-rejected. But per weight, A1 is admissible exactly when r ≥ 3/7 and A2 exactly when r ≤ 7/3, and these intervals cover all weights — so z\* ∈ V_weak in the truncation. The gap therefore contains z\*.

**Why the main example is immune to this erasure.** Its gap is **tube-driven**: on *I*, every member of the four-action menu violates the stage-1 path constraint *S₀* itself (the two dips and the bridge deficit of Theorem 5(7)), and a later stage cannot repair a violated tube — the stage-1 constraint is local to stage 1. Remark 6's safe direction is secured by exactly the assumptions the erasure datum violates. Together the two results bound the persistence claim: hold-prefix extension preserves the separation; arbitrary multi-stage extension does not; and the erasure mechanisms of Remark 6(iii) are realizable.

### 4.9 Machine verification

The continuum statements (Proposition 3, Proposition 4, Theorem 5, Remark 6, Theorems 7–8) are established by the displayed proofs. An accompanying software artifact — **deterministic exact-integer arithmetic; no floating point, tolerances, or randomness** — checks the finite rational instance of Proposition 3, Proposition 4, Theorem 5, and Remark 6: the action classifications, region identities, and accepted-set identities on a **31³ = 29,791-state grid** over *(x, s₁, s₂)*, with a finite verification set containing the critical weight ratios ρ₁, ρ₂ and their midpoint for every enumerated grid state. **All 25 checks pass**, and re-execution reproduces them exactly; they're enumerated in the Supplementary Material (S8).

| Claim layer | What is established | By what |
|---|---|---|
| Continuum statements | Exact identities and inequalities on the witness datum | Displayed proofs |
| Finite rational instance | Classifications on the enumerated grid | Deterministic computation |
| Empirical claims | None in this article | — |

The finite grid does not by itself prove the continuum identities; it validates the symbolic classification on the enumerated instance.

### 4.10 Menu convexification: the blend family

The action space is the finite menu {FAST, SLOW, STAGED, NO-SWITCH} of deterministic actions; fractional or alternating policies are **not** members of it. The "convexification" instrument is the **blend family**: for each δ ∈ (0,1), the action **BLEND_δ** is the *convexified action* obtained by fractional allocation of the primitive control flows, *u_δ = δ·u_FAST + (1−δ)·u_SLOW*. By linearity, its worst-case tube is the pointwise convex combination of the two primitive worst-case tubes, and its successor the convex combination of the two successors. This is menu convexification at the level of **control inputs** — an explicit model assumption, **not** the time-sharing of discrete actions in alternation.

**Theorem 8 (blend collapse).** On the example, over initial states *X₀*:

- **(i)** BLEND_δ is typed-admissible at *z* exactly when
  > δ ∈ [1 − s₂/2, s₁/2],
  an interval nonempty exactly when **s₁ + s₂ ≥ 2** (a singleton at equality), independent of *x ≥ 0* and of the weight.
- **(ii)** The typed acceptance set of the menu augmented by the blend family is exactly the compensatory region:
  > V_typ^blend = {x ≥ 1} ∪ {s₁ + s₂ ≥ 2} = V_weak.

  **Convexifying the menu collapses the acceptance gap:** FP_agg vanishes under the augmented menu, and the blend family reaches exactly the compensatory region and nothing beyond — on V_phys \ V_weak no blend is typed-admissible.
- **(iii)** The admissible window depends on the state through *(s₁, s₂)* alone: **a single δ serves every weight w ∈ W₊.** On the impossibility region the blend is therefore the common action that no member of the finite menu supplies — **the acceptance gap is a property of the deterministic menu, not of the doctrines.**

**Why.** The blended tube has s₁-coordinates [s₁ − 2δ, s₁] and s₂-coordinates [s₂ − 2(1−δ), s₂], with x staying nonnegative (convex combinations of nonnegative quantities). Typed admissibility needs the tube in S₀ and the successor in G; the tube condition is exactly the displayed window, and the successor is the mixture of two identical successors, (1, x, s + e) ∈ G. The window is nonempty exactly when s₁ + s₂ ≥ 2.

**Remark.** The collapse is exact and weight-independent: a single convexified plan serves every assessor on *I*, where the per-weight plans of Theorem 5(6) necessarily differ. The nonconvexity at work is **menu geometry** — the finiteness and determinism of the action space — *not* the Pareto-frontier geometry under which weighted sums fail to reach nonconvex frontier parts (Das and Dennis, 1997); the two mechanisms are distinct. The structure is precisely that of **pure-versus-mixed strategies** in the assessor–planner game (von Neumann, 1928; Sion, 1958): with the planner picking an action and the assessor a weight, common-plan acceptance is the pure-strategy value and per-weight acceptance the mixed value — the gap being the pure-strategy duality gap that the convex (mixed) extension closes. It is also the here-and-now versus wait-and-see separation of adjustable robust optimization (Ben-Tal et al., 2004).

### 4.11 The converse: discrete time-sharing does not erase the gap

**Proposition 9 (sequential time-sharing does not erase the gap).** On the example, let a sequential time-shared policy alternate between FAST and SLOW over the interval, so the set of visited states is the **union** of the two primitive worst-case tubes. Then such a policy is typed-admissible if and only if **s₁ ≥ 2 and s₂ ≥ 2**. On the impossibility region *I* (where s₁ < 2, s₂ < 2, s₁ + s₂ > 2), no such policy is typed-admissible, and the acceptance gap therefore survives discrete time-sharing.

**Why.** A sequential policy that spends any positive time on FAST visits every s₁ in [s₁ − 2, s₁], and any positive time on SLOW visits every s₂ in [s₂ − 2, s₂]; the union tube stays in S₀ exactly when both dips are nonnegative.

**Remark — the precise boundary between two kinds of mixing.** Continuous convexification — fractional allocation of control flows — closes the acceptance gap exactly at the compensatory region s₁ + s₂ ≥ 2; discrete time-sharing — alternation in time, whose visited set is the **union** of the action tubes — closes it only where the two dips are independently subsumed (s₁ ≥ 2 and s₂ ≥ 2). On the regime s₁ + s₂ ≥ 2 with min(s₁, s₂) < 2 (which contains the impossibility region), the gap survives sequential time-sharing and closes only under convexification. **The structural character of the gap is a property of the convexity of the action space, not of the assessment doctrine and not of temporal sharing as such.**

---

## 5. Interpretation

### 5.1 The doctrinal reading

The scalarized operators {E_w} formalize **one** compensatory assessment doctrine: a single aggregate index w·s; nonnegative weights on capital forms; substitution across floors permitted at those weights; disturbances respected. The paper calls this *the scalarized aggregate doctrine as formalized here* — **not** "weak sustainability" simpliciter. The weak-sustainability literature is broader (aggregate wealth, constant total capital, nondeclining consumption, discounting, shadow prices, intertemporal investment conditions — Neumayer 2013; World Bank 2011; Boos 2015; Dasgupta and Mäler 2000; Asheim 1994). Likewise, strong sustainability is not always equivalent to "every stock stays nonnegative at every instant" — critical-natural-capital frameworks may use thresholds, safe operating spaces, irreversibility, resilience, or minimum-service conditions (Ekins et al. 2003; Doyen and Gajardo 2020). The typed operator E_typ is a formal idealization of the separately-binding-floor reading, in the same sense the scalarized operators idealize one aggregation doctrine.

**Within this precise scope, Theorem 5 reads as follows.** The two formalized doctrines can disagree on the same transition datum — with the same robustness standard and the same action set — in the direction *compensatory-accepts / noncompensatory-rejects*, on a relatively open region. The disagreement is not an artifact of one bad weight: **every weight accepts, each licensing a different physical transition.** The plans are genuinely different transitions (FAST and SLOW violate different floors at different times) — the dynamic formalization of substitution across floors. By Proposition 3(ii), the precise seat of the disagreement is the noncommutativity of "choose an action" with "for all weights."

At the **static** level the full-cone aggregate is lossless (Remark 2), so the compensatory doctrine's limitation is **not** the existence of an aggregate index but the **policy dependence** of the aggregate-feasible transition: the index certifies a *set* of transitions, none of which the noncompensatory assessment accepts.

The two quantifier orders also carry an **information reading.** ∃a ∀w is a commitment made **before** the weight is known — the strong doctrine's robustness demand — while ∀w ∃a_w lets the action be chosen **after** the weight is observed. On the witness, the acceptance gap measures the **value of information about the assessment weight**. Theorem 8 qualifies this: a single convexified blend serves every weight on the impossibility region, so the value of information reflects the finite deterministic menu rather than the weight information itself. Proposition 9 sharpens the point: the value of information is removed by convexifying the action space, **not** by sharing actions in time — under discrete time-sharing the gap survives on the impossibility region.

Throughout, "nonnegative scalarization weights" means elements of W₊; the word "prices" is reserved for interpretive discussion. Actual prices may be strictly positive, endogenous, dynamically determined, state-dependent, or dimensionally heterogeneous — the theorems require none of those. The operators are linear scalarizations with weights fixed over the review interval. Nonlinear aggregate indices (CES-type substitutability, or state-dependent weighting that diverges near zero-stock boundaries) are **different** assessment operators, and the theorems claim nothing for them.

### 5.2 Positioning against established theory

**Established (not new here).** The backward recursion is a typed instance of established robust-predecessor, reach-avoid, capture-basin, and hybrid-reachability constructions (Aubin 1991; Aubin, Bayen, and Saint-Pierre 2011; Saint-Pierre 1994; Lygeros, Tomlin, and Sastry 1999). Proposition 3(i) is constraint-set monotonicity of viability kernels and reachability sets. The foundation statement that values may be only weakly comparable — and that this incommensurability is constitutive of ecological economics — is due to Martinez-Alier, Munda, and O'Neill (1998). The characterization of which sustainability criteria admit indicator representations, and the role of maximin and MSY-type reasoning, are developed in Martinet (2011), Cairns and Martinet (2014), and Doyen and Gajardo (2020) — the last showing that the multicriteria maximin value is the solution of a static Pareto problem over the viability kernel, the strongest formal statement of "strong sustainability as constraint viability rather than optimality." Static scalarization limitations are established (weighted sums can't reach nonconvex parts of Pareto fronts — Das and Dennis 1997), a mechanism of frontier geometry different from this paper's action-quantifier mechanism. Compensability analysis is established in multi-criteria decision analysis (Cinelli, Coles, and Kirwan 2014; Schär, Pohl, and Geldermann 2025).

**Proved here.** (i) The action-set identity E_typ = ⋂_w E_w with the full-cone choice isolating the separation as purely dynamic (Prop 3(ii)). (ii) The general quantifier-separation remark (Remark 1). (iii) Weight-family monotonicity (Prop 4). (iv) The explicit exact-tube witness with a relatively open region of strict separation and the rescue/impossibility split (Theorem 5). (v) Persistence under hold-prefix extension (Remark 6). (vi) The explicit two-stage erasure datum (Theorem 7). (vii) The blend-collapse theorem (Theorem 8) plus the converse delimitation (Proposition 9).

**Novelty qualification.** To the author's knowledge, this provides an explicit exact-tube witness for this dynamic separation in a compensatory/noncompensatory assessment setting. No priority is asserted over the elementary quantifier fact ∃a ∀w ≠ ∀w ∃a_w, which is standard. Whether an equivalent dynamic separation appears in adjacent literatures (multi-objective robust control, viability theory, multi-criteria decision analysis) is a **bounded absence in the review, not an established universal negative**.

### 5.3 Scope delimitations

- **No aggregate blindness at fixed trajectories.** By Remark 2, at a fixed trajectory the full-cone aggregate is lossless.
- **No separation on every datum.** Where a single action is safe for all weights, the assessments coincide. The theorem is an existence separation with an open region, plus the always-valid hierarchy and localization.
- **No infinite-horizon, stochastic, partial-observation, or endogenous-event extension.** All statements are for finite-horizon exact-tube data with specified disturbance sets.
- **No claim that the full nonnegative cone is the only reasonable weight family.** Proposition 4 shows restricting the family enlarges the compensatory accepted set; the full cone is the strictest compensatory reading, and the separation persists *a fortiori* for restricted families.
- **No welfare claim about prices.** The weights model an assessment doctrine, not a normative endorsement.
- **No empirical transfer.** The theorems concern assessment operators on a specified datum and imply no empirical claim about any resource system.
- **No claim that V_weak is the genuine-savings or inclusive-wealth criterion.** The operator is the strictest compensatory reading (every weight, each licensing an action). The witness's reserve stock is excluded from the weighted aggregate **by construction**, not by consequence of aggregation.
- **No absolute impossibility.** The impossibility region is a negative certificate *relative to the specified four-action menu*; with a larger menu it can shrink or vanish (see the completeness requirement in Section 5.5).
- **No universal doctrinal ranking.** The inclusion V_typ ⊆ V_weak ⊆ V_phys is a theorem about the defined operators under common action and disturbance classes, common safe-set inclusion, common horizon, common tube semantics, and common terminal condition. It does not establish a universal ranking of endpoint, weak, and strong sustainability doctrines.
- **No separation under coupled all-floor shocks.** The witness disturbance convention is action-indexed (Section 4.5): each action's worst case is its own characteristic dip. A datum whose disturbances couple simultaneous dips across all floors of every action degenerates the per-weight licensing structure — the principal actions fail together and the divergence collapses into universal rejection. The separation is exhibited for, and scoped to, the specified action-indexed class.
- **Convexification of the menu.** Fractional action policies are not members of the action space; every stated separation is scoped to the finite deterministic menu. Theorem 8 resolves the convexification question: the blend family collapses the typed acceptance set exactly onto the compensatory region — menu geometry, distinct from the Pareto-frontier geometry of scalarization limits. Proposition 9's delimitation: discrete time-sharing does **not** effect the same collapse — on the impossibility region the gap survives alternation in time.

### 5.4 Policy implications

**First.** Aggregate indices alone **cannot** certify noncompensatory transition safety under these assessment semantics. A scalarized assessment can certify its own criterion — aggregate feasibility; what it cannot certify is typed safety unless an additional bridge theorem is supplied.

**Second.** When the typed recursion identifies an admissible **rescue action** whose feasibility is controlled by a **resource margin**, investment in that margin is a candidate remedy; reweighting alone cannot substitute for it on the witness datum (Section 5.5). (This applies where a resource-controlled rescue action exists; it is not a universal policy claim.)

**Third.** **Per-floor reporting alongside aggregate reporting is necessary for detecting this class of discrepancy.** It is not universally necessary for every sustainability judgement; but where the question is whether a transition respects separately-binding floors, an aggregate index alone cannot distinguish the rescue region from the impossibility region. A minimum report for such an assessment should include: (1) typed floors and their provenance; (2) aggregate weights or the weight family; (3) policy quantifiers; (4) the disturbance set; (5) the observation and implementation model; (6) exact versus conservative tube status; (7) terminal maintainability; (8) action-exhaustion status; (9) uncertainty and approximation bounds; (10) normative premises.

**Fourth.** Reporting regimes that evaluate **endpoints only** (e.g. audited annual snapshots) evaluate only the weakest operator in the chain of Section 3.1. Under those semantics they license transitions that violate typed floors mid-interval **without detection** (on the witness, FAST is typed-endpoint-admissible at every state of X₀ but typed-tube-admissible only for s₁ ≥ 2); the per-floor reporting of the third implication detects the discrepancy. No empirical claim about any particular reporting regime is made here.

### 5.5 Rescue as action synthesis, and data requirements

**Rescue as action synthesis.** Rescue is an operation on the impossibility region. Define a resource-augmentation map
> Aug_κ : (x, s, A) ↦ (x + κ, s, A ∪ {STAGED_κ})

and the minimal rescue threshold
> κ\* = inf{ κ : ∃a ∈ A_κ with a ∈ E_typ(z) },

where A_κ is the augmented menu.

**Proposition (rescue threshold).** On the witness datum, for the STAGED action and x < 1, **κ\* = 1 − x**. *(STAGED is typed-admissible exactly when its x-tube stays nonnegative, i.e. x + κ ≥ 1; the least such increment is 1 − x.)* The increment converts an impossibility-region state into a typed-transformable one. States of the rescue set *R* need no augmentation — STAGED is typed-admissible there; this is why *R* is not part of the acceptance gap.

**Data requirements for empirical application.** The theorem is a result about assessment operators on a specified datum. Empirical application requires, in addition to the typed floors, disturbance set, action set, tube model, and destination-maintainability witness of Section 4.5:

1. **Action-set completeness status.** A negative certificate over a finite action set proves impossibility only relative to that set. The application must state whether A is exhaustive, a listed policy menu, a sampled subset, or an inner approximation. If incomplete, the verdict is "no safe transition exists *among the listed actions*," not "no safe transition exists."
2. **Calibration and identifiability data.** Parameter estimates, uncertainty sets, structural alternatives, validation data, observation error, model discrepancy, missing-data treatment, disturbance dependence. A specified disturbance set is necessary but not sufficient; it must be justified, or the verdict marked conditional on model credibility.
3. **Policy and authority data.** Who may select each action, what information they possess, decision timing, enforcement assumptions, compliance uncertainty, strategic responses, resource and legitimacy constraints.
4. **Threshold-uncertainty semantics.** A physical or normative floor is rarely known exactly. Distinguish the deterministic floor sᵢ(z) ≥ 0 from robust threshold safety sᵢ(z; θ) ≥ 0 for all θ ∈ Θ, and from probabilistic or confidence-level versions if admitted.
5. **Destination maintainability status.** Whether the destination-maintainability witness is established physically, by simulation, or by assumption.

---

## 6. Discussion

### 6.1 Negative certificates

A **negative certificate** — a rejection with an exhibited violated constraint for each action, exhausting the action set — is a **complete** verdict, not an inconclusive one. Theorem 5(7) is an instance: four actions, four exhibited violations, certifying impossibility on *I* together with the resource threshold of Section 5.5 and the per-weight licensing thresholds of Theorem 5(6). Related scored forecast-evaluation studies apply the same kind of assessment discipline to the Northern cod and Edwards Aquifer systems (Abaee, 2026b, 2026c); the separation results here rest on their displayed proofs and the machine-checked finite instance of Section 4.9.

### 6.2 Limitations

1. The separation theorem is an existence result with an open region; it does **not** imply the gap is large in any given application, and where the assessments coincide it yields nothing.
2. Novelty statements reflect bounded literature search (Section 5.2).
3. The operators cover finite horizons with exact tubes and specified disturbance sets; infinite horizons, partial observation, stochastic chance constraints, and endogenous event times are **not** treated.
4. **No empirical claims are made.**
5. The governance, intergenerational, and composition extensions are stated at partial status in the Supplementary Material and are **not** used in the proofs.
6. **Computational tractability.** On a finite explicit state–action–disturbance graph with constant-time predicate evaluation, the backward recursion is polynomial in the graph size and horizon. For continuous, hybrid, or belief-state models, the graph itself may be exponentially large, infinite, or only approximately representable; exact tube inclusion may be computationally hard or undecidable; and grid cardinality grows as N_grid = ∏ᵢ Nᵢ — exponentially in dimension when floors are coordinates. The witness is tractable because its datum is small, finite, and rational.

---

## 7. Conclusions

The weak- and strong-sustainability traditions are usually compared as **doctrines** — different normative stances on substitutability. This paper shows that the divergence of the two doctrines *as formalized here* — the scalarized-aggregate and typed operators of Section 3.1 on a common action menu and disturbance class — **survives translation into assessment mechanics**, at the level of a theorem about those operators.

The theorem establishes **no ranking** of doctrines: Section 5.1 delimits the formalizations, and by Theorem 8 the structural character of the separation is a property of the finite deterministic menu, not of either tradition (Sections 4.10–4.11).

On a typed transition datum under exact-tube semantics, the compensatory reading (per-weight acceptance) and the noncompensatory reading (common-plan acceptance) are related by a quantifier commutation that **can fail on an open region of state space**. Where it fails: every scalarization weight certifies a transition, but no single transition is certified by all weights; and the certified set splits into states rescuable by a resource-controlled action and states that are impossible under every weight. The mechanism is **not** scalarization blindness — at fixed trajectories the full-cone aggregate is lossless — but the **policy dependence** of the aggregate-feasible transition.

**For composite sustainability indices, the concrete consequence:** an index can be sound at the level of *accounting* and still over-certify at the level of *assessment*, because certification is a quantifier statement about transitions, not a property of a number. Where separately-binding floors matter, **per-floor reporting is not a presentation preference but a detection requirement**: the aggregate alone cannot distinguish the rescue region from the impossibility region. The bridge a composite index needs — some single transition that serves every admissible weight, i.e. membership in V_typ — is exactly what reporting conventions should be asked to exhibit. Theorem 8 qualifies this: such a single transition is not, in general, a member of the specified deterministic menu but a **convexified action**, so the relevant question for a reporting convention is whether its action set admits the required menu convexification — and Proposition 9 shows that temporal alternation alone does not provide it.

---

## References

*(Kept as in the original.)*

- Abaee, A. (2026a). Typed flux ledgers and depletion arithmetic: conservation, componentwise diagnostics, and the semantics of depletion horizons. Zenodo. https://doi.org/10.5281/zenodo.22554177
- Abaee, A. (2026b). Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609
- Abaee, A. (2026c). Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680
- Asheim, G. B. (1994). Net national product as an indicator of sustainability. *Scandinavian Journal of Economics*, 96(2), 257–265.
- Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser, Boston.
- Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). *Viability Theory: New Directions*, 2nd ed. Birkhäuser, Boston.
- Ben-Tal, A., Goryashko, A., Guslitzer, E., and Nemirovski, A. (2004). Adjustable robust solutions of uncertain linear programs. *Mathematical Programming*, 99(2), 351–376.
- Boos, A. (2015). Genuine savings as an indicator for "weak" sustainability: Critical survey and possible ways forward in measuring weak sustainability. *Sustainability*, 7(4), 4146–4163.
- Cairns, R. D., and Martinet, V. (2014). An environmental-economic measure of sustainable development. *European Economic Review*, 69, 4–17.
- Cinelli, M., Coles, S. R., and Kirwan, K. (2014). Analysis of the potentials of multi criteria decision analysis methods to conduct sustainability assessment. *Ecological Indicators*, 46, 138–148.
- Daly, H. E. (1990). Toward some operational principles of sustainable development. *Ecological Economics*, 2(1), 1–6.
- Das, I., and Dennis, J. E. (1997). A closer look at drawbacks of minimizing weighted sums of objectives for Pareto set generation in multicriteria optimization problems. *Structural Optimization*, 14, 63–69.
- Dasgupta, P., and Mäler, K.-G. (2000). Net national product, wealth, and social well-being. *Environment and Development Economics*, 5(1), 69–93.
- Doyen, L., and Gajardo, P. (2020). Sustainability standards, multicriteria maximin, and viability. *Natural Resource Modeling*, 33(3), e12250.
- Ekins, P., Simon, S., Deutsch, L., Folke, C., and De Groot, R. (2003). A framework for the practical application of the concepts of critical natural capital and strong sustainability. *Ecological Economics*, 44(2), 165–185.
- Frankowska, H. (1989). Optimal trajectories associated with a solution of contingent Hamilton–Jacobi equations. *Applied Mathematics and Optimization*, 19, 291–311.
- Hanley, N., Moffatt, I., Faichney, R., and Wilson, M. (1999). Measuring sustainability: A time series of alternative indicators for Scotland. *Ecological Economics*, 28(1), 55–73.
- Hickel, J. (2020). The sustainable development index: Measuring the ecological efficiency of human development in the Anthropocene. *Ecological Economics*, 167, 106331.
- Lygeros, J., Tomlin, C., and Sastry, S. (1999). Controllers for reachability specifications for hybrid systems. *Automatica*, 35(3), 349–370.
- Martinez-Alier, J., Munda, G., and O'Neill, J. (1998). Weak comparability of values as a foundation for ecological economics. *Ecological Economics*, 26(3), 277–286.
- Martinet, V. (2011). A characterization of sustainability with indicators. *Journal of Environmental Economics and Management*, 61(2), 183–197.
- Neumayer, E. (2013). *Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms*, 4th ed. Edward Elgar, Cheltenham.
- Saint-Pierre, P. (1994). Approximation of the viability kernel. *Applied Mathematics and Optimization*, 29, 187–209.
- Schär, S., Pohl, E., and Geldermann, J. (2025). Analysing the compensatory properties of the outranking approach PROMETHEE. *Journal of Multi-Criteria Decision Analysis*, 32, e70013.
- Sion, M. (1958). On general minimax theorems. *Pacific Journal of Mathematics*, 8(1), 171–176.
- Solow, R. M. (1974). Intergenerational equity and exhaustible resources. *Review of Economic Studies*, 41, 29–45.
- Usubiaga-Liaño, A. (2025). Strong sustainability in the SEEA and the wider indicator debate. *One Ecosystem*, 10, e141086.
- von Neumann, J. (1928). Zur Theorie der Gesellschaftsspiele. *Mathematische Annalen*, 100, 295–320.
- World Bank. (2011). *The Changing Wealth of Nations: Measuring Sustainable Development in the New Millennium*. World Bank, Washington, D.C.

---

## Supplementary Material

Framework extensions (governance constructors, the implementability ladder, the commons obstruction, intergenerational structures, the nested-impossibility theorem, composition interfaces), the planetary-boundaries application note, the full framework definitions, and the conjectures are given in the accompanying Supplementary Material, which also enumerates the machine artifact's 25 checks (S8).

---

## Declarations

**Data availability statement.** The proofs are contained in this article. The verification code for the finite rational instance (all 25 checks; deterministic exact-integer arithmetic) is archived in a public repository; a link is provided with the submission.

**Declaration of competing interest.** None.

**AI declaration.** GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.

---

*End of plain-language version. This document is a faithful humanization of the original LaTeX paper; for formal statements, proofs, and citation details, refer to the original.*

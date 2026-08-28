# A Typed Architecture for Sustainability: Claim Statuses, Transformation Operators, and the Separation of Assessment Doctrines

**Manuscript:** P1-DRAFT-1 (Paper 1 of the adjudicated publication architecture)
**Series:** general-sustainability programme, A001–A025
**Draft date:** 2026-08-28
**Status:** DRAFT — the independent-result gate is closed at the internal level (theorem file + exact-integer machine witness + search-level novelty pass, 2026-08-28); statements frozen against the row-closed concordance; this paper's own theorems carry complete proofs

---

## Abstract

Sustainability claims travel badly. A statement about a fish stock, an aquifer, a liability regime, and an intergenerational floor uses different state spaces, different proof obligations, and different failure modes, yet policy discourse treats them as one currency. This article states the typed, domain-agnostic architecture a research programme has frozen for such claims: a canonical system schema with declared types; four uncertainty levels with a fixed quantifier discipline; three policy questions; four model maps that license every cross-model claim; diagnostic claim types with a no-transfer rule; a transformation operator for changes of system architecture; constructors for governance instruments; intergenerational viability structures; restricted composition interfaces; and the admission standards that decide when complexity is earned. The architecture's discipline is that every claim carries a status (axiom, identity, theorem, conditional theorem, conjecture, counterexample) and that negative results are first-class content. The paper's independent mathematical contribution is a theorem about *assessment doctrines* on this architecture: an exact-tube separation showing that endpoint-only accounting, scalarized aggregate assessment (the weak-sustainability doctrine: one index, prices on capital forms, compensation across floors), and noncompensatory typed assessment (the strong-sustainability doctrine: each floor separately binding) form a strictly nested hierarchy — and that the gap between the aggregate family and the noncompensatory assessment is *exactly* the failure of "a plan exists for each price vector" to commute to "one plan exists for all price vectors". On an explicit two-architecture datum the gap is a region with interior in which every price vector certifies its own transition and no transition respects the floors; the typed recursion splits this false-positive set into a fundable rescue set and a certified impossibility region. The separation is machine-witnessed in exact integer arithmetic and propagates through the backward induction. The paper closes with the research architecture itself: how a 409-row source-to-canonical-to-publication concordance, a claim-status discipline, scored negative certificates, and independent reruns make a cross-domain corpus auditable — and what the architecture deliberately does not claim.

---

## 1 Introduction

### 1.1 The question this paper answers

**What is the typed, domain-agnostic architecture of sustainability, viability, observation, governance, transformation, and composition — and what does that architecture prove about the assessment doctrines used to judge sustainability transitions?**

Two failure modes motivate the question. The first is *commensurability drift*: sustainability assessments aggregate stocks, services, liabilities, and floors into single indices whose compensations are never declared as mathematics. The second is *status drift*: conceptual frameworks state hopes as theorems, conditional results circulate as unconditional ones, and negative findings disappear. The programme whose architecture this paper states was built against both failures: every object is typed, every claim carries a status, every cross-model statement is a declared map, and negative certificates are published with the same discipline as positive results.

### 1.2 What enters this paper

Paper 1 is the architecture paper of a five-paper series. Its retained set consists of the 21 concordance rows routed to it by the programme's destination pass (definitions and structures of the canonical framework; the governance constructors; the intergenerational structures; the restricted-composition interfaces; the research-architecture material), plus this paper's own independent result — the assessment-separation theorem with its complete instantiation — which closed the independent-result gate on 2026-08-28. The full proof corpus (viability calculus, conservation, noncompensation algebra, sampled kernels, projectability) belongs to Paper 2, the theorem atlas; the ledger, delay-dynamics, and empirical-identification applications belong to Papers 3–5. Where this paper needs an atlas result, it states the canonical form once, cross-references the owning paper, and never transfers a status. Per-row provenance identifiers (`CC-A00X-YYY`) link every statement to the 409-row concordance inventory (source location, canonical module, mapping type, evidence status, destination).

### 1.3 Claim-status discipline

Every statement below carries a status label from the programme's hierarchy (the A002 source's own table, adopted programme-wide):

| Status | Admission rule |
|---|---|
| Axiom/definition | Declares an object, domain, type, or convention; asserts no empirical truth |
| Identity | Follows by construction or direct algebra |
| Theorem | Complete proof under explicit mathematical assumptions |
| Conditional theorem | Complete implication whose hypotheses are not established for every intended application |
| Conjecture | Precise unproved statement with a declared proof gap and disproof route |
| Counterexample/limit | An explicit construction establishing that an implication fails |

Two rules govern this article. **No promotion:** a conditional theorem is never stated as a theorem; conditionality is part of the mathematical content. **No silent transfer:** a status proven for one model class does not transfer to extensions, reductions, or applications without a declared map (§2.7) and, where the map crosses modules, the interface contract recorded per row.

### 1.4 Provenance and auditability

Eighteen of this paper's 21 concordance rows are row-closed at content level (`row_verified`, dated scientific passes over full source reads: A001, A002, A006, A012, A018 closed 2026-08-27/28); three (CC-A003-006, CC-A016-001, CC-A016-010) are `requires_row_level_verification` — their sources are not yet in the closure campaign's closed set — and they are stated below at exactly that status, not promoted. Content-level acceptance means the row's existence, kind, proof presence, module, and mapping type were verified against the source; it is not a theorem-status promotion, and the cross-module interface contract remains an open obligation recorded per row. This paper's own theorems (§4) are manuscript-native: their proofs are complete here, and their machine witness is a committed deterministic artifact.

### 1.5 Relationship to the programme

This is Paper 1 of five assured papers (plus two scored-forecast papers already drafted, a conditional Paper 6, and a monograph after external scrutiny). Paper 2 carries the mathematics that survives without the architecture narrative; Papers 3–5 carry the applications; the monograph reintegrates at full length. No paper depends on another for a locally load-bearing definition: each carries a Minimal Working Realization of the canonical objects it needs, and §2 is this paper's.

---

## 2 The typed canonical framework (Minimal Working Realization)

The framework of this section is the A002 source's canonical layer [CC-A002-001, CC-A002-003, CC-A002-004, CC-A002-005, CC-A002-006, CC-A002-019, CC-A002-035 — all axiom/definition, row-verified]. Paper 2's atlas restates the same definitions in its preliminaries; the canonical forms are stated once here, and the atlas cross-references this paper as the architecture owner.

### 2.1 Type system and physical state [CC-A002-001 · axiom/definition]

Physical state is typed: a state variable denotes a *moiety* (a named conserved material substance) carrying a *unit*, and typed fluxes connect typed stocks. Conservation claims are per-moiety; the framework does not authorize adding biomass, money, biodiversity indices, and exergy into one conserved scalar. Services, thresholds, information states, and institutional variables are separate types with their own domains — the architecture's first discipline is that no claim mixes types without a declared bridge.

### 2.2 The canonical system [CC-A002-003 · axiom/definition]

The canonical object is a tuple `S` with thirteen declared slots spanning: the typed physical state; the admissible action correspondence; the dynamics (continuous, sampled, hybrid, or delayed as declared per instance); the observation map; the information pattern; the constraint sets (physical, service, liability, obligation, identity, cumulative-harm); the disturbance class; the policy class; the claim-status table; the destination structure; and the declared model map to any other object. A *model* in this programme is a fully specified tuple; a *claim* is a statement about a tuple with a status; an *application* is a tuple plus data. The schema is frozen as TCS-1.0 (the controlling version; the TCS-1.1 diff is frozen but deliberately non-controlling pending migration).

### 2.3 Four uncertainty levels [CC-A002-004 · axiom/definition]

Uncertainty is stratified into four declared levels — a fixed parameter; a bounded disturbance set with a declared signal space; a set of candidate models; and an information state describing what the policy can observe — with a fixed quantifier discipline per level. The levels do not collapse: a robust-viability claim quantifies over the disturbance set, a diagnostic claim quantifies over the model set, and an epistemic claim quantifies over information states, each with its own proof obligations.

### 2.4 Diagnostic types and the no-transfer rule [CC-A002-005 · axiom/definition]

Diagnostic claims come in five types (conservation check, positivity check, deficit diagnostic, first-passage diagnostic, horizon diagnostic), and the no-transfer rule is axiomatic: **a diagnostic is not a causal claim**. A componentwise deficit identifies where a floor is violated; it does not establish the mechanism. First-passage diagnostics carry timing semantics; they do not establish predictability. This typing is what keeps the empirical layers (Paper 5) honest.

### 2.5 Threshold and intergenerational types [CC-A002-006 · axiom/definition]

Thresholds are declared data with provenance (physical, contractual, or normative — the provenance is part of the type), and intergenerational safety is defined by a recursive criterion: each generation's viability is relative to the constraint sets it inherits and the sets it must leave. The intergenerational structures of §7 instantiate this criterion.

### 2.6 Three policy questions and the quantifier discipline [CC-A002-019 · axiom/definition]

Every application in the programme poses its safety question in one of three fixed forms. Let `z^{π,d}(t; z_0)` be the trajectory under causal policy `π` and disturbance signal `d ∈ D`:

1. **Actual-policy safety:** does the *specified* pair `(π_0, d_0)` keep the trajectory in the constraint set `K`?
2. **Viability:** does *some* `π ∈ P` keep the trajectory in `K`?
3. **Robust viability:** does *one admissible causal policy* work for *every* disturbance in `D`?

The quantifier order is fixed and load-bearing: `∃π ∀d`, not `∀d ∃π`. The policy may react causally to observations; what is excluded is a policy chosen with foreknowledge of the realized disturbance. Section 4's theorem is, at bottom, a theorem about what happens when a *second* quantifier — over assessment weights — is interleaved with this one.

### 2.7 Four model maps [CC-A002-035 · axiom/definition]

Cross-model claims are licensed only by four declared maps: a **specialisation** (fix parameters or restrict to an invariant subset); an **exact projection** (a semiconjugacy of full and reduced flows); an **approximation** (a declared residual or error bound); and a **singular reduction** (a small parameter, a limiting invariant object, and convergence on a stated time domain). The terms are not interchangeable: "special case", "projection", "approximation", and "singular limit" name different mathematics with different proof obligations, and the concordance records which map every cross-model row uses. The projectability criterion (a `C¹` map `p` carries the flow to a reduced system iff `Dp·F = G∘p`, with uniqueness) is the atlas's to state and prove [Paper 2, family F06]; this paper needs only the map taxonomy and the discipline it enforces.

---

## 3 The three operators at architecture level

The architecture organizes sustainability mathematics under three operators. Their full theorem families are the atlas's (Paper 2); this section fixes the architecture-level reading and states the transformation operator this paper owns.

### 3.1 Maintenance (Operator I)

The maintenance question — can the system be kept inside its constraint sets indefinitely under the declared policy and disturbance classes? — is classical viability [cite: Aubin; Frankowska; Saint-Pierre]. The programme's contribution at this level is not a new kernel construction (the standing adjudication is explicit: the kernel calculus is established mathematics) but the *typing*: constraint sets are typed (physical floors, service floors, liability, obligation, identity, cumulative harm), the kernel is computed per typed question, and the three policy questions of §2.6 fix which kernel (actual-policy, existential, or robust) a claim refers to. The atlas carries the kernel calculus, the obstruction calculus (epistemic kernels can be empty while physical kernels are full; observation fibres can defeat any exact safety certificate), and the recovery/irreversibility family.

### 3.2 Observation

Observation is an operator, not a passive input: it thins the policy class (information contraction) and its timing changes kernels. The observation-fibre machinery — including the counterexamples that defeat exact safety certification — belongs to the atlas [Paper 2, families F03/F05]; the architecture-level statement is the interface rule: **an observation claim and a control claim never share a status**; a claim about what can be known is a different type from a claim about what can be done, and the bridge is an explicit theorem, not a verbal slid.

### 3.3 Transformation (Operator II): the finite-architecture recursion [programme infrastructure, stated as typed instance of established constructions]

The transformation question — can the system be moved *between architectures* (extraction to regenerative; one governance regime to another) while every transition-safe constraint holds throughout and a maintainable destination is reached? — is formalized by a restricted finite-architecture, fixed-review, exact-tube backward recursion. The data: a finite architecture set `Q`; fixed review times `t_0 < … < t_m`; a disjoint phase state; per-stage admissible meta-actions (causal within-interval control rules plus, when permitted, one architecture transition/reset rule at the interval endpoint); declared disturbance sets; **exact** tubes (the set of phase points visited by every solution branch the declared solution concept admits); successor sets after the permitted endpoint reset; transition-safe sets `S_k` (physical, functional, identity, liability, obligation, and cumulative-harm constraints, conjunctive — noncompensatory); and a destination set `G` whose membership includes the destination architecture's maintainability condition.

The robust predecessor is

```
RPre_k(W) = {(q,x) ∈ S_k : ∃a ∈ A_k(q,x) ∀d ∈ D_k(q,x,a):
             Tube_k(q,x,a,d) ⊆ S_k  and  Succ_k(q,x,a,d) ⊆ W},
```

and `W_m = G`, `W_k = RPre_k(W_{k+1})`. The recursion's theorem — `W_k` is exactly the set of states robustly transformable from stage `k` to `G`; the characterization is a backward induction — is *proved* in the programme's theorem file, and the adjudicated position is stated without embellishment: **the recursion and the backward-induction theorem are a typed instance of established discrete viability/capture-basin/robust-predecessor/hybrid-reachability constructions, not new mathematics.** [Cite: Aubin–Bayen–Saint-Pierre; Saint-Pierre; Aubin capture basins; Lygeros–Tomlin–Sastry.] What the typing adds — transition safety checked on full within-interval tubes rather than endpoints; architecture resets that translate identity, liability, and obligations through typed successor states; noncompensatory conjunctive safety; arrival separated from post-arrival maintainability; exact versus conservative-tube conclusions — is modeling semantics with proof obligations, and the paper's independent result (§4) is where those semantics earn mathematical content: a theorem the untyped constructions do not state.

---

## 4 The independent result: the assessment hierarchy and its separation

This section is the paper's citable contribution. Proofs are complete; the machine witness is a committed deterministic artifact (`research_program/paper1_instantiation/`, exact integer arithmetic, 25/25 checks).

### 4.1 Three assessments on one datum

Fix a typed exact-tube datum as in §3.3 whose transition-safe registry and destination set are typed noncompensatory: `S_k = S_k^phys ∩ {s_i ≥ 0, i = 1..n}` and `G = G^phys ∩ {s ≥ 0}`, with `s = (s_1,…,s_n)` the typed floors (normalized to 0 by translation). Let

```
C = R^n_+ \ {0}
```

be the **closed nonnegative cone** of aggregate weight vectors. The closed cone — not the strictly positive orthant — is the right model of the aggregate assessment for three reasons: zero prices are the honest weak-assessment semantics (aggregate indices routinely price a capital form at zero); on the closed cone the pointwise aggregate is lossless (Lemma 4.2), which isolates the entire assessment gap in the dynamic quantifier structure; and the closed cone is the *most permissive* natural family, so every separation proved against it holds a fortiori for any subfamily, including all strictly positive price vectors.

For a state `z` and stage `k`, define three admissible-action sets:

- **endpoint-only physical:** `E_phys(z) = {a : ∀d, Tube(a,d) ⊆ S^phys and Succ(a,d) ⊆ G^phys}` — the endpoint-accounting audit (physical coordinates only);
- **scalarized aggregate at weight `w`:** `E_w(z) = {a : ∀d, Tube(a,d) ⊆ S^phys ∩ {w·s ≥ 0} and Succ(a,d) ⊆ G^phys ∩ {w·s ≥ 0}}` — the weak-sustainability index (one floor, prices `w`, compensation across floors, disturbances respected);
- **noncompensatory typed:** `E_typ(z) = {a : ∀d, Tube(a,d) ⊆ S_k and Succ(a,d) ⊆ G}` — the strong-sustainability registry (each floor separately binding).

All three retain the same disturbance quantifier; the assessments differ *only* in constraint structure. The assessment predecessors are `{z : E(z) ≠ ∅}` respectively.

### 4.2 Lemma (closed-cone pointwise equivalence) [manuscript-native · identity]

For `v ∈ R^n`: `v ≥ 0` componentwise ⟺ `w·v ≥ 0` for every `w ∈ C`.

*Proof.* (⇒) `w ≥ 0`, `w ≠ 0`, `v ≥ 0` gives `w·v = Σ w_i v_i ≥ 0`. (⇐) Contrapositive: if `v_k < 0`, take `w = e_k ∈ C`: `w·v = v_k < 0`. ∎

The companion static fact — that for *strictly positive* weights `w·Δ ≥ 0` does not imply `Δ ≥ 0` — is the atlas's Proposition 5.1 [CC-A002-007, Paper 2 family F02]: the open cone's static compensation failure. The two statements are complementary: on the closed cone, at a fixed point or along a fixed trajectory, the aggregate with all cone weights is *exactly* as informative as the vector of floors. Every dynamic gap in this section is therefore attributable to the quantifier structure alone — not to static scalarization blindness.

### 4.3 Theorem A (assessment hierarchy and quantifier noncommutativity) [manuscript-native · theorem]

**(i) Hierarchy.** For every weight `w ∈ C`: `E_typ(z) ⊆ E_w(z) ⊆ E_phys(z)`; hence `{P_typ} ⇒ {∀w: P_w} ⇒ {P_phys}`.

**(ii) Localization.** For every state `z`: `E_typ(z) = ⋂_{w∈C} E_w(z)`. The two assessment predecessors therefore differ exactly by the order of "there exists a plan" and "for all weights": `{P_typ} = {z : ⋂_w E_w(z) ≠ ∅}` (one plan serves every price vector) versus `{∀w: P_w} = {z : ∀w, E_w(z) ≠ ∅}` (every price vector has its own plan). Existential choice of plan does not commute with the universal quantifier over weights.

**(iii) Strictness.** Both inclusions can be strict simultaneously on one datum with two architectures, two typed floors, four meta-actions, and a two-point disturbance set (Theorem B).

*Proof.* (i) Let `a ∈ E_typ(z)`. For every `d`, `Tube(a,d) ⊆ S_k = S^phys ∩ {s ≥ 0}`, and by Lemma 4.2 (⇒) every tube point satisfies `w·s ≥ 0` for every `w ∈ C`; likewise successors lie in `G ⊆ G^w`. So `a ∈ E_w(z)`. The inclusion `E_w ⊆ E_phys` is immediate from `S^phys ∩ {w·s ≥ 0} ⊆ S^phys` and `G^phys ∩ {w·s ≥ 0} ⊆ G^phys`. (ii) `⊆` by (i). `⊇`: if `a ∈ ⋂_w E_w(z)`, then for every `d` and every tube point `p`, every `w ∈ C` gives `w·s(p) ≥ 0`, so `s(p) ≥ 0` by Lemma 4.2 (⇐); hence `Tube ⊆ S_k`, and the same argument over successors gives `Succ ⊆ W`. (iii) is Theorem B. ∎

**Corollary A.1 (no price vector rescues the assessment).** On the datum of Theorem B, `⋂_{w∈C}{P_w} ⊋ {P_typ}` with nonempty interior. Since intersecting the scalarized assessments over *any* subfamily of `C` gives a superset of the full intersection, no choice of prices — and no family of price vectors — recovers the noncompensatory predecessor on that datum. The noncompensatory assessment is not the limit of weak assessments.

**Concession (stated here, per the novelty audit).** Theorem A(i) is standard mathematics: it is constraint-set monotonicity of viability kernels/reachability sets [cite: Aubin; Frankowska] applied to `S_typ ⊆ S_w ⊆ S_phys`. The claim of this paper is (ii)–(iii): the localization and the witnessed separation.

### 4.4 The witness datum [manuscript-native · axiom/definition]

Two architectures — extraction `q=0`, regenerative `q=1` — one review interval `[0,1]`, phase state `(q, x, s_1, s_2)`: a physical reserve stock `x` and two typed floors — protected-group service surplus `s_1` and remediation-liability coverage surplus `s_2` (floors normalized to 0). `S_0 = {x ≥ 0, s_1 ≥ 0, s_2 ≥ 0}`; `G = {(1,x,s) : x ≥ 0, s ≥ 0}` (the destination maintainability condition is witnessed by the destination hold policy, under which `G` is robustly invariant — declared datum). Disturbance set `{β, α}` scales dip depth (worst-case dip 2); destination reset gains 1/4; rescue cost `c = 1`. The four meta-actions, from any initial `(0, x, s)` with `x ≥ 0, s ≥ 0`:

| action | within-interval trajectory | successor |
|---|---|---|
| `NO-SWITCH` | state constant | `{(0,x,s)}` — misses `G` |
| `FAST` | `s_1` dips to `s_1 − 2` mid-interval (adverse disturbance); `s_2`, `x` constant | `{(1, x, s+e)}` |
| `SLOW` | `s_2` dips to `s_2 − 2` mid-interval; `s_1`, `x` constant | `{(1, x, s+e)}` |
| `STAGED` | floors grow; `x` spends linearly to `x − 1` | `{(1, x−1, s+e)}` |

Reading: `FAST` is the immediate full switch (deployment gap dips protected service; escrow continues); `SLOW` is the phased switch (service maintained; the liability handover window dips coverage); `STAGED` rents temporary capacity and bridges the escrow — no typed dip — at physical cost `c`; `NO-SWITCH` is transit-safe but lands outside the destination. Every trajectory is piecewise linear on breakpoints `{0, ½, 1}` and monotone per piece, so all tubes below are the **exact** visited sets — no outer approximation anywhere in the datum or its machine verification.

### 4.5 Theorem B (false positives, blindness levels, disagreement, rescue, impossibility) [manuscript-native · theorem]

On the witness datum, over initial states `X_0 = {(0,x,s) : x ≥ 0, s ≥ 0}`:

**(1)** `{P_typ} = {x ≥ 1} ∪ {s_1 ≥ 2} ∪ {s_2 ≥ 2}` — one floor survives its own worst-case dip, or the bridge is funded.

**(2)** `⋂_{w∈C}{P_w} = {x ≥ 1} ∪ {s_1 + s_2 ≥ 2}` — the aggregate family's binding condition (at the worst weight `w = (1,1)` both plans need the same budget) is the **total-capital budget** `s_1 + s_2 ≥ 2`.

**(3)** `{P_phys} = X_0` — endpoint-only accounting admits every state (the physical endpoint is always reachable).

**(4)** The **false-positive set** `FP = {x < 1, s_1 < 2, s_2 < 2, s_1+s_2 ≥ 2}` — the triangle between the coordinate thresholds and the budget line — is nonempty with interior.

**(5)** Both hierarchy inclusions are strict on this one datum: every point of `FP` lies in `⋂_w {P_w} \ {P_typ}`, and the point `(½, 1/10, 1/10)` lies in `{P_phys} \ ⋂_w{P_w}` (endpoint-feasible while *no* action is aggregate-safe at `w = (1,1)`).

**(6)** **Per-weight plan disagreement.** On the triangle interior, the FAST-certifying weights are exactly `{r = w_2/w_1 ≥ ρ_1}`, the SLOW-certifying weights exactly `{r ≤ ρ_2}`, with `ρ_1 = (2−s_1)/s_2`, `ρ_2 = s_1/(2−s_2)`, and `ρ_2 ≥ ρ_1 ⟺ s_1+s_2 ≥ 2`, strict on the interior. Low-`s_2`-price assessors license `FAST` only; high-`s_2`-price assessors license `SLOW` only; **no single action serves every price vector** — which is exactly `E_typ = ⋂_w E_w = ∅` (Theorem A(ii)).

**(7)** **The rescue split.** With `FP_0` the triangle (x unrestricted): the **rescue set** `R = FP_0 ∩ {x ≥ 1}` is typed-transformable, witnessed by `STAGED` — the bridging plan at physical cost `c` keeps both floors intact and lands in `G`; the **impossibility region** `I = FP_0 ∩ {x < 1}` is aggregate-feasible for every cone weight yet admits *no* typed-admissible action, with four exhibited violations: `FAST` violates the protected-service floor under the adverse disturbance; `SLOW` violates the liability-coverage floor; `STAGED` drives the physical stock negative; `NO-SWITCH` misses the destination architecture.

*Proof.* (1) `NO-SWITCH` fails `G`; `FAST`'s worst-case `s_1`-tube is `[s_1−2, s_1]`, safe iff `s_1 ≥ 2`; `SLOW` symmetrically iff `s_2 ≥ 2`; `STAGED`'s `x`-tube is `[x−1, x]`, safe iff `x ≥ 1`. (2) For `x ≥ 1`, `STAGED` is aggregate-safe for every `w` (tubes monotone; the aggregate of nonnegative coordinates with nonnegative gains stays nonnegative). For `s_1+s_2 ≥ 2` with `s_1, s_2 < 2`: both floors are then strictly positive; `FAST` is aggregate-safe iff `w_1(s_1−2) + w_2 s_2 ≥ 0`, i.e. `r ≥ ρ_1`; `SLOW` iff `w_1 s_1 + w_2(s_2−2) ≥ 0`, i.e. `r ≤ ρ_2`; and `ρ_2 ≥ ρ_1` ⟺ `s_1s_2 ≥ (2−s_1)(2−s_2)` ⟺ `s_1+s_2 ≥ 2`, so every `r ∈ [0, ∞]` is covered (`w = e_1`, `e_2` always covered by `SLOW`, `FAST` respectively; endpoints in `C`). Conversely, if `x < 1` and `s_1+s_2 < 2`: at `w = (1,1)`, `FAST` and `SLOW` both need `s_1+s_2 ≥ 2`; `STAGED` violates the physical tube (and `S^w ⊆ S^phys`, so no aggregate floor compensates a physical violation); `NO-SWITCH` misses `G^w`. (3) `FAST` is always physically admissible. (4)–(5) follow from (1)–(3); `(½, 6/5, 6/5)` is an interior point of `FP` since `6/5 + 6/5 = 12/5 > 2` with both coordinates below 2. (6) is the two computations of (2) with `w_1, w_2 > 0`; a single action serving every weight would lie in `⋂_w E_w = E_typ`, contradicting (1). (7) `STAGED`'s tubes on `R`: floors grow from `s ≥ 0`, `x`-tube `[x−1, x] ⊆ [0, ∞)`; successor in `G`. On `I` the four violations are the four computations above, one exhibited violated constraint per action, the actions exhausting `A_0`. ∎

**Reading.** The aggregate assessment's binding condition is the total-capital budget; the noncompensatory assessment requires one floor to survive its own worst-case dip or the bridging resource to be funded. The triangle between them is exactly where the weak doctrine certifies a transition — per price vector, with price-dependent plans — that the strong doctrine rejects. And the typed recursion does not merely reject: it names the binding resource (`x` at cost `c`) and the exact subregion where funding the bridge converts the false positive into a certified transformation.

### 4.6 Theorem C (propagation through the backward induction) [manuscript-native · theorem]

Extend the datum to `m ≥ 2` intervals by prepending hold intervals (sole action `HOLD`: constant tube `{z}`, successor `{z}`, safe set `S_0`; the last interval carries the witness datum). Define each assessment's backward recursion with its own terminal set (`G`, `G^w`, `G^phys`) and safe sets. Then: (i) for every stage `j`, `W^typ_j ⊆ ⋂_{w∈C} W^w_j ⊆ W^phys_j` — and this hierarchy holds for *every* multi-interval typed exact-tube datum, hold-prefixed or not; (ii) the stage-0 regions are the witness regions pulled back through the holds, so both strictness witnesses persist; (iii) the separation is not an artifact of the one-interval framing.

*Proof.* (i) Downward induction. Base: `G = G^phys ∩ {s ≥ 0} ⊆ G^phys ∩ {w·s ≥ 0} ⊆ G^phys` by Lemma 4.2. Step: a typed-admissible action's tube lies in `S_j ⊆ S^w_j` (Lemma 4.2, ⇒) and its successors in `W^typ_{j+1} ⊆ W^w_{j+1}`; the second inclusion is identical with `S^w_j ⊆ S^phys_j`. (ii) `HOLD` is the unique action and is assessment-admissible iff `z ∈ S^·_j` and `z ∈ W^·_{j+1}`. (iii) The strictness witnesses lie in `S_0` (their floors are met initially), so they hold through the prefix. ∎

### 4.7 The machine witness [artifact]

Every claim of Theorems A/B/C is machine-checked by a committed deterministic artifact: `research_program/paper1_instantiation/typed_false_positive_instantiation.py` — exact integer arithmetic (scale 40; no floats, no tolerances, no randomness, no outer tube approximation) — over a 29,791-state grid with dense critical weight sets including the exact boundary weights `ρ_1`, `ρ_2` and the adversarial midpoint `(ρ_1+ρ_2)/2`: the three region identities, the hierarchy, the false-positive set (1,900 grid states) with its interior witness, both strictness witnesses, the plan disagreement at named weights (`r = ½` SLOW-only, `r = 1` both, `r = 2` FAST-only), `E_typ = ⋂_w E_w = ∅` verified over the full critical weight set, the rescue split with the four exhibited violations, and Theorem C through two prepended hold intervals. 25/25 checks pass; re-runs are byte-identical; the JSON results and the human-readable report are committed alongside the runner.

---

## 5 Weak and strong sustainability as assessment doctrines

### 5.1 The reading of Theorem B

The scalarized assessments are the weak-sustainability doctrine in exact robust form: one index `w·s`, prices on capital forms (zero prices allowed — uncosted ecosystem services are the canonical case), floors substitutable at those prices, disturbances respected. The typed registry is the strong-sustainability doctrine: each critical floor separately binding. Theorem B then reads: *the two doctrines can disagree on the same transition system with the same robustness standard and the same action set, in the direction weak-accepts/strong-rejects, on a set with interior — and the disagreement is not an artifact of one bad price vector: every price vector accepts, each licensing a different physical transition.* The plans are genuinely different transitions (`FAST` and `SLOW` violate different floors at different times — asynchronous dips), which is the dynamic formalization of compensation across incommensurable capitals. By Theorem A(ii) the disagreement's precise seat is the noncommutativity of "choose a plan" with "for all prices": at the static level the closed-cone aggregate is lossless (Lemma 4.2), so the weak doctrine's blind spot is not the existence of an aggregate index but the *policy dependence of the aggregate-feasible transition*. Endpoint-only accounting is a third, strictly weaker audit level — blind even to aggregate transit dips (Theorem B(5)).

### 5.2 Positioning against established theory [per the search-level novelty audit, 2026-08-28]

**Conceded as established (cited, never claimed).** The backward recursion of §3.3 is a typed instance of established robust-predecessor/reach-avoid/capture-basin/hybrid-reachability constructions [Aubin–Bayen–Saint-Pierre; Saint-Pierre; Aubin; Lygeros–Tomlin–Sastry]. Theorem A(i) is viability-kernel constraint monotonicity [Aubin; Frankowska]. The static scalarization limitations are established: weighted sums cannot reach nonconvex parts of Pareto fronts [Das–Dennis 1997/1998] — a different mechanism (frontier geometry under a single optimization, not the action quantifier under per-weight feasibility). Compensability analysis is established in MCDA, including the explicit mapping of compensatory aggregation to weak and outranking methods to strong sustainability [Cinelli et al. 2014; Schär et al. 2025]. Multiple-barrier composition and compatibility is an active control literature. Scalarization-dependent optimal policies are a staple of multi-objective RL. The weak/strong sustainability debate and the genuine-savings indicator line are mature [Neumayer; World Bank; Boos 2015; Hanley et al.; Usubiaga-Liaño et al. 2025] — cited as motivation, not as prior art for the theorem form.

**Claimed as this paper's contribution (bounded-search deltas, honestly labelled).** (i) Theorem A(ii): the per-state identity `E_typ = ⋂_{w∈C} E_w` and the quantifier-order characterization — with the closed-cone choice making the separation purely dynamic. (ii) Theorem B: the closed-form witness with per-weight plan disagreement and the rescue/impossibility split — the negative-certificate form applied to assessment doctrines. (iii) Theorem C: the propagation. (iv) The interpretation: the first formal dynamic separation of the two assessment doctrines on one transition system with one robustness standard. The full novelty map, with queries and raw search records, is committed at `research_program/paper1_full_text_novelty_pass.md`; its no-match-found verdicts are bounded absences, and the manuscript's claims are conditioned accordingly.

**Claim rejected.** "The first general theorem for robust transformation between system architectures" — not supported; robust reach-avoid with resets is established. The supported claim is the assessment-doctrine separation.

### 5.3 What the theorem does not say

No claim of aggregate blindness at fixed trajectories (Lemma 4.2 is the opposite). No separation on every datum (where a single plan is safe for all weights, the assessments coincide — the theorem is an existence separation with interior, plus the always-valid hierarchy and localization). No infinite-horizon, stochastic, partial-observation, or endogenous-event extension. No claim that the closed cone is the only reasonable aggregate family (it is the most permissive; subfamily separations follow a fortiori). No welfare claim about prices: the weights model assessment doctrines, not normative endorsement. No transfer to empirical systems: the theorem is about assessment operators on a declared datum; it asserts nothing about any fishery or aquifer — those questions belong to Papers 3–5 with their own data and status discipline.

---

## 6 Governance, authority, and implementation

### 6.1 Constructors [CC-A001-077 · axiom/definition, row-verified]

Governance instruments enter the architecture as *constructors*: a constructor is a map on the system data `(X, U, F, I, π)` that changes **exactly one named component and introduces no new state space**. The primitives [A001 §13.6]: `Cap(Q)` (an upper harvest bound), `Floor(H_min)` (an output floor), `Tax(τ)` (a price entry in the effort law), `Excl` (excluding a competing predator), `Leak(h)` (unreported/illegal harvest added to realized take), `Obs(I, Ψ)` (replacing the observation map and feedback law), and `Rest(·)` (any other restriction of the control correspondence). Implementation sets admit a lattice structure — the viable restrictions are downward closed, and the invariant-generating restrictions form a sublattice — carried by the atlas's institutional family [Paper 2, §12]; observation is not in either lattice: it thins the policy class rather than the action correspondence, a separation of axes the architecture treats as the formal content of "governance restricts".

### 6.2 Management vocabularies are rewrites, not theorems [CC-A001-081 · theorem (verified present; summary)]

A total allowable catch is `Cap`; a harvest control rule is `Obs`; a landing subsidy is `Tax(−σ)`; unreported harvest is `Leak`; a closed season is a periodic `Cap`; an open-access rent dynamic is a restriction of the effort law entering `F`. Each common instrument is a word in the constructor algebra and introduces no new mathematical content beyond the constructor it reduces to. *Proof (verified present; summary):* each instrument is realized as a single constructor on the tuple; by invariance under irrelevant structure (a proposed addition that changes no component of the tuple does not change the kernel), each changes the problem class only through its one component. This is the architecture's formal completion rule: **new content requires a new constructor, a new physical type, or the resolution of a residual** — not a new name for an old restriction. ∎

The research-architecture consequence is the one this paper lives by: management vocabulary inflation is not theory growth, and the constructor algebra is the check.

### 6.3 The commons obstruction [CC-A001-069 · theorem (verified present; summary)]

If the non-cooperative (Nash) harvest level exceeds the safe level at *every* state of the relevant viable set, then the viability kernel is empty under non-cooperative play. *Mechanism (verified present; summary):* the kernel-emptiness machinery applied with the Nash harvest as the realized disturbance — the obstruction is a *governance* fact: no admissible policy exists because the play structure, not the physics, exhausts the constraint set. The obstruction is removable by constructors in the institutional direction (graduated sanctions prevent the over-extraction; monitoring bounds the observation error so state feedback applies) — the architecture's reading of why institutional and physical variables belong to one typed system. The full institutional implementation family is the atlas's [Paper 2, §12].

### 6.4 The institutional interface [CC-A003-006 · definition, requires_row_level_verification; CC-A006-010 · conditional theorem, row-verified]

The institutional-feedback model class carries a declared scope restriction — *weak viability coupling*: use has limited or indirect effect on reproduction [CC-A003-006, source inventory verified, row-level content verification pending]. The composition interface is honestly conditional: compositional safety across coupled subsystems holds *conditional on the interface contracts; separate subsystem certificates alone do not imply network safety* — stated without proof in its source and carried at exactly that status [CC-A006-010, conditional theorem]. The architecture's rule for both: the conditionality and the scope restriction are part of the content, stated on the line, never laundered by restatement.

---

## 7 Intergenerational structures

### 7.1 Generation structure [CC-A001-082 · axiom/definition, row-verified]

A *generation structure* is a sequence `0 = t_0 < t_1 < ⋯ → ∞` of generation boundaries with closed per-generation constraint sets `V^(k)`; *intergenerational viability* requires `x(t) ∈ V^(k)` for `t ∈ [t_k, t_{k+1})` — each generation's trajectory segment must respect that generation's floors. The structure instantiates the recursive intergenerational safety criterion of the threshold types [CC-A002-006]: safety is relative to inherited sets and constrains bequeathed sets.

### 7.2 The stationary equivalence [CC-A001-083 · theorem (verified present; no separate proof — immediate)]

If `V^(k) = V` for all `k` — the stationary case — intergenerational viability *equals* ordinary viability. The theorem is an immediate equivalence; its content is the reminder that intergenerational content begins exactly when the generation sets are *not* stationary: floors tighten, degrade, or shift across generations.

### 7.3 The nested-impossibility theorem [CC-A001-084 · theorem (verified present; summary)]

Assume trajectories are confined to a compact set (verified per instance via dissipativity). If the generation sets are nested decreasing with empty intersection — each generation's floors strictly harder, collectively unsatisfiable — then **no intergenerationally viable path exists**. *Proof (verified present; summary):* a viable path would be a trajectory forever inside a nested family of closed sets with empty intersection inside a compact set — impossible by compactness: the trajectory has limit points, and every limit point would have to lie in every `V^(k)`. ∎ This is the architecture's canonical intergenerational negative result: sustainability can fail *generation-structurally*, with every finite segment satisfiable, and the failure is a theorem, not a scenario.

---

## 8 Restricted composition and model transformations

### 8.1 Effort-scale invariance [CC-A012-009 · theorem (verified present; summary)]

In the registered delay-dynamics family, the effort-scale transformation — `E' = aE`, `E'_max = aE_max`, `q' = q/a`, `δ_0' = aδ_0`, with correspondingly scaled effort histories — leaves the `(N, Z)` trajectories invariant. The transformation is exact (a `TRANSFORMATION`-typed map in the concordance's four-map taxonomy), and its architecture role is identifiability discipline: effort scales are not separately identifiable from the stock dynamics, so calibration claims must quotient by the transformation. Paper 4 owns the family; this paper states the map and the discipline.

### 8.2 Yield-gap soft-minimum and weak coupling [CC-A018-009 · theorem (verified present; summary)]

At the Liebig (most-limiting) limit, the yield gap obeys the soft-minimum bound `π_j ≤ w_min^{-1} e^{−ρΔ_y}` and the coupled system decouples with error `‖X − X^k‖ ≤ C_T ε_c`, `ε_c = C e^{−ρΔ_y} + ε_phys` — weak coupling is *quantified*, not assumed: the decoupling error is a proved function of the yield gap and the physical error bound. This is the architecture's model for how composition claims should be licensed: an explicit error bound on a declared map, the approximation taxonomy of §2.7 doing its work. Paper 4/6 own the applications.

### 8.3 Coupling creates viability [CC-A001-056 · example (verified present; status crosswalk recorded)]

An explicit two-factor example (`g_i(s) = s(1−s)`, coupling `d = 0.2`, equilibrium-defined harvest floors) in which *coupling creates viability that is absent in a factor*: the coupled system's kernel is nonempty while a decoupled factor's is not. Together with the atlas's coupling-destroys-viability results [Paper 2, family F10], the architecture's composition lesson is two-sided: composition is neither safe nor unsafe in general — each direction is a theorem with its own witness, and unrestricted composition is not licensed (the restricted-composition contracts and their counterexamples are the atlas's).

### 8.4 Exergy, quality grades, and nonsmooth transformation feasibility [CC-A002-049 · research programme, row-verified]

The transformation operator's open extension: transformation feasibility under exergy and quality-grade constraints, where the feasible set is nonsmooth (grades induce kinks). The source registers this as a research programme, not a theorem set; the architecture carries it as the declared frontier of the transformation operator — typed, with the nonsmoothness named as the obstruction class. No status is asserted beyond programme.

---

## 9 Negative results as first-class content

### 9.1 The negative-certificate methodology

The architecture treats a *negative certificate* — a rejection with an exhibited violated constraint, per action, exhausting the action set — as a first-class result, not a failure to be spun. Theorem B(7) is the assessment-side instance: four actions, four exhibited violations, a certified impossibility *plus* the resource and price at which the impossibility dissolves. The programme's scored-forecast layers instantiate the same methodology empirically: both scored gates returned negative certificates (benchmark persistence was not defeated on either system, under the preregistered scoring), and the one structural win was declined on class grounds — published with the same discipline as a win would have been. The methodology's content: **complexity is retained only on scored evidence**; an unfalsified model class is not an achievement, and a rejected complexity is a finding.

### 9.2 The admission discipline

Modules enter the architecture through an admission standard (preregistered scoring against declared baselines; held-out defect audits; frozen retention rules), and the architecture's claim about itself is deliberately modest: the integration — typed schema, claim statuses, model maps, certificate/status layer, negative-certificate methodology — is the contribution; the component mathematics retains its established provenance, and the integration does not establish universality.

### 9.3 Normative premises in the typed registry [CC-A016-001, CC-A016-010 · registry entries, requires_row_level_verification]

The typed registry carries *tagged normative premises*: e.g. the adaptive-capacity material registers "B6 is a normative premise" as a tagged registry row, and proposed floors (participation/recruitment non-decline) as normative and unoperationalized research-programme items [both rows pending row-level content verification, stated at that status]. The architecture-level rule these rows instantiate: **normative content is tagged, never formalized covertly** — a floor's provenance (physical, contractual, normative) is part of its type (§2.5), and a normative floor that has not been operationalized says so on the line. Negative-lesson sources (institutional-solvency failures, distributive-barrier impossibilities, rejected multidomain syntheses, institutional-index negatives) are routed into Papers 1–2 and the traceability archive under the same rule: no separate paper, no deletion, status intact.

---

## 10 The research architecture

### 10.1 The publication architecture

The programme's content allocation is a five-paper assured core — this paper (architecture and assessment); the theorem atlas (the proof corpus); the conserved-material ledgers and componentwise depletion diagnostics; the delay-driven capital-liquidation and nonlinear institutional dynamics; the sampled governance, empirical identification, and falsification designs — plus two drafted scored-forecast papers, a conditional RFDE extensions paper, and a monograph that reintegrates at full length only after the principal papers receive external scrutiny. Every valid source proposition maps to a paper section, an appendix, a conditional docket, or an explicit negative record; the non-loss rule is checkable row by row against the concordance.

### 10.2 The concordance and its closure campaign

The 409-row canonical concordance links every source proposition to canonical notation, assumptions, proof/evidence status, mapping type, destination paper, and monograph chapter. Its machine layer (quotes, coverage, vocabulary, closure-record shape) is fully executed; its scientific layer — full source reads, per-row verification of kind, proof presence, module, and mapping — has closed 239 rows across seven sources (A001, A002, A011, A006, A012, A014, A018), covering this paper's and the atlas's primary sources; 136+6 rows remain open across 15 sources and are being closed source by source. The campaign's found-and-repaired defect classes (intake row corruption, keyword false-positives, pre-repair register misalignment) are themselves part of the architecture's evidence that machine verification alone is not content verification.

### 10.3 Reproducibility and the certification hierarchy

Computational claims carry a certification hierarchy — nominal result, rerun-verified (byte-identical on fresh execution), independently rerun (second agent/toolchain), certified (interval/rigorous arithmetic) — and the hierarchy is *stated per claim*, never implied. The programme's validated computations are rerun-verified; the interval-certified layer carries its own manifest; the compendium is versioned with a register of record. The reproducibility rule for this paper's own witness: exact integer arithmetic, committed artifact, deterministic re-execution — the certification level is *exact*, the strongest tier available to a finite discrete verification.

---

## 11 Status ledger

| ID | statement | status | evidence | destination |
|---|---|---|---|---|
| CC-A002-001 | Type system and physical state | axiom/definition | row-verified 2026-08-27 | Paper 1 (monograph restates) |
| CC-A002-003 | Canonical system (13-slot tuple) | axiom/definition | row-verified 2026-08-27 | Paper 1 |
| CC-A002-004 | Four uncertainty levels | axiom/definition | row-verified 2026-08-27 | Paper 1 |
| CC-A002-005 | Diagnostic types + no-transfer rule | axiom/definition | row-verified 2026-08-27 | Paper 1 |
| CC-A002-006 | Threshold and intergenerational types | axiom/definition | row-verified 2026-08-27 | Paper 1 |
| CC-A002-019 | Three policy questions | axiom/definition | row-verified 2026-08-27 | Paper 1 |
| CC-A002-035 | Four model maps | axiom/definition | row-verified 2026-08-27 | Paper 1 |
| CC-A002-049 | Exergy/quality-grades programme | research programme | row-verified 2026-08-27 | Paper 1 (programme) |
| CC-A001-056 | Coupling creates viability (example) | example | row-verified 2026-08-27 | Paper 1 §8.3 |
| CC-A001-069 | Commons obstruction | theorem (verified present) | row-verified 2026-08-27 | Paper 1 §6.3 (gate closed) |
| CC-A001-077 | Constructors | axiom/definition | row-verified 2026-08-27 | Paper 1 §6.1 |
| CC-A001-081 | Management vocabularies are rewrites | theorem (verified present) | row-verified 2026-08-27 | Paper 1 §6.2 |
| CC-A001-082 | Generation structure | axiom/definition | row-verified 2026-08-27 | Paper 1 §7.1 |
| CC-A001-083 | Stationary equivalence | theorem (immediate) | row-verified 2026-08-27 | Paper 1 §7.2 |
| CC-A001-084 | Nested-impossibility | theorem (verified present) | row-verified 2026-08-27 | Paper 1 §7.3 |
| CC-A003-006 | Weak viability coupling scope | definition (scope) | **requires_row_level_verification** | Paper 1 §6.4 |
| CC-A006-010 | Conditional compositional safety | **conditional theorem** | row-verified 2026-08-28 | Paper 1 §6.4 |
| CC-A012-009 | Effort-scale invariance | theorem (verified present) | row-verified 2026-08-28 | Paper 1 §8.1 (Paper 4 owns family) |
| CC-A016-001 | Typed registry (normative premise tag) | registry entry | **requires_row_level_verification** | Paper 1 §9.3 |
| CC-A016-010 | Research programme (proposed floors) | research programme | **requires_row_level_verification** | Paper 1 §9.3 |
| CC-A018-009 | Yield-gap soft-minimum/decoupling | theorem (verified present) | row-verified 2026-08-28 | Paper 1 §8.2 (Papers 4/6 apply) |
| MS-Native-1 | Lemma 4.2 (closed-cone pointwise equivalence) | identity | proved here (two lines) | Paper 1 §4.2 |
| MS-Native-2 | Theorem A (hierarchy + localization) | theorem | proved here; machine-witnessed | Paper 1 §4.3 |
| MS-Native-3 | Theorem B (false positives/rescue/impossibility) | theorem | proved here; machine-witnessed | Paper 1 §4.5 |
| MS-Native-4 | Theorem C (propagation) | theorem | proved here; machine-witnessed | Paper 1 §4.6 |
| Infra-1 | Finite-architecture robust transformation (recursion) | theorem (typed instance of established constructions — standing adjudication) | proved in `paper1_finite_architecture_transformation_theorem.md` | Paper 1 §3.3 (infrastructure) |

No status is promoted anywhere in this ledger; the three open rows are stated at their open status; the manuscript-native results are this paper's own, with artifact provenance.

---

## 12 Provenance, reproducibility, and limits

**Provenance.** Every concordance-sourced statement carries its `CC` identifier; the concordance row links to source location, module, mapping type, evidence status, and destination. The manuscript-native theorems (§4) are complete in this paper; their full development, proofs, and machine witness are the committed files `research_program/paper1_typed_false_positive_theorem.md` and `research_program/paper1_instantiation/` (runner, JSON results, report, raw novelty-search records).

**Reproducibility.** The witness artifact is deterministic, exact-integer (scale 40), and idempotent across re-execution (25/25 checks; byte-identical outputs). The programme-level battery (validated-computation reruns, wave-E reproduction, concordance machine layer, consistency suite at its documented baseline) runs clean on the tree containing this manuscript.

**Limits.** (i) The assessment-separation theorem is an existence result with interior, not a claim that the gap is always large; on dominated-action data the assessments coincide. (ii) Its novelty verdicts at no-match-found are bounded-search absences, conditioned per §5.2; if external review overturns a verdict, the fallback destination is the monograph's series introduction — the publication architecture's standing rule, not a demotion. (iii) The three open rows (§11) await their sources' closure passes; nothing in this paper depends on their closure. (iv) The architecture covers no infinite horizons, no partial observation, no stochastic chance constraints, and no endogenous event times at the transformation-operator level; each exclusion is recorded in the theorem files and inherited here. (v) The empirical layers of the programme (Papers 3–5) own every data-bearing claim; this paper asserts nothing empirical.

---

## References (to be completed at camera-ready)

Established mathematics cited: Aubin (viability theory; viability kernels and capture basins); Aubin–Bayen–Saint-Pierre (*Viability Theory: New Directions*); Frankowska (viability kernels of differential inclusions); Saint-Pierre (kernel approximation); Lygeros–Tomlin–Sastry (hybrid reachability controllers); Das–Dennis (weighted-sum drawbacks); Cinelli et al. 2014 (MCDA for sustainability assessment); Schär et al. 2025 (outranking compensability); the multiple-CBF composition line; the MORL scalarization line. Sustainability economics cited as motivation: Neumayer (weak/strong sustainability); the genuine-savings line (World Bank; Boos 2015; Hanley et al.; Usubiaga-Liaño et al. 2025); critical-natural-capital literature (Ekins et al.). Full bibliographic data per the programme's shared bibliography register at camera-ready.

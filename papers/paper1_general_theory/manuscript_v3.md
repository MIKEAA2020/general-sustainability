# A Typed Architecture for Sustainability: Claim Statuses, Transformation Operators, and the Separation of Assessment Doctrines

**Paper 1 of the programme's publication architecture (general-sustainability, A001–A025).**

*Third edition (journal-facing edition, 2026-08-29): the external style review's accepted findings are implemented — the abstract and introduction reposition the formal vocabulary as this paper's analytical framework rather than as a description of field practice; the statement-level inventory moves from the body to Appendix A in two-table form with concrete bases and a stipulation/validity legend; the research-architecture section is restructured as a concrete reproducibility statement and a condensed future-directions section; publication roadmaps and internal process vocabulary are removed from the body. No theorem, proof, number, or claim status is changed; the second edition remains the programme-internal record.*

---

## Abstract

Sustainability claims are difficult to compare across domains. Statements about a fish stock, an aquifer, a liability regime, and an intergenerational floor rest on different mathematical structures, require different forms of evidence, and fail in different characteristic ways, yet policy discourse frequently treats them as commensurable. This paper introduces a typed, domain-agnostic architecture that formalizes these differences as explicit state spaces, proof obligations, and failure modes, and makes them auditable: a canonical system schema with declared types; four uncertainty levels with a fixed quantifier discipline; three policy questions; four model maps that license every cross-model claim; diagnostic claim types with a no-transfer rule; a transformation operator for changes of system architecture; constructors for governance instruments; intergenerational viability structures; restricted composition interfaces; and admission standards governing the retention of additional structure. The architecture's central discipline is that every claim carries an explicit status — axiom, identity, theorem, conditional theorem, conjecture, or counterexample — and that negative results are first-class content. The paper's principal mathematical contribution is a separation theorem for assessment doctrines: endpoint-only accounting, scalarized aggregate assessment (the weak-sustainability doctrine: one index, prices on capital forms, compensation across floors), and noncompensatory typed assessment (the strong-sustainability doctrine: each floor separately binding) form a strictly nested hierarchy, and the gap between the aggregate family and the noncompensatory assessment is exactly the failure of "a plan exists for each price vector" to commute to "one plan exists for all price vectors". On an explicit two-architecture datum the gap is a region with interior in which every price vector certifies its own transition and no single transition respects the floors; the typed recursion splits this false-positive set into a fundable rescue set and a certified impossibility region. The separation is machine-witnessed in exact integer arithmetic and propagates through the backward induction. The architecture is operationalized in a source-to-canonical-to-publication concordance of 409 mappings, provided with the verification artifacts to support independent re-execution.

**Keywords:** sustainability assessment; viability theory; weak and strong sustainability; typed systems; claim status; reproducibility

---

## 1 Introduction

### 1.1 The question this paper answers

**What is the typed, domain-agnostic architecture of sustainability, viability, observation, governance, transformation, and composition — and what does that architecture prove about the assessment doctrines used to judge sustainability transitions?**

Two failure modes motivate the question. The first is *commensurability drift*: sustainability assessments aggregate stocks, services, liabilities, and floors into single indices whose compensation principles are rarely stated as explicit mathematics. The second is *status drift*: conceptual frameworks state aspirations as theorems, conditional results circulate as unconditional ones, and negative findings disappear from the literature. The programme whose architecture this paper states was built against both failures, and this paper makes the motivating differences precise rather than assumed: it assigns every object a type, every claim a status, and every cross-model statement a declared map — formalizing as distinct state spaces, proof obligations, and failure modes what assessment practice tends to treat as one currency.

### 1.2 What enters this paper

Paper 1 is the architecture paper of the series. Its retained set consists of the twenty-one concordance rows routed to it by the programme's destination pass (definitions and structures of the canonical framework; the governance constructors; the intergenerational structures; the restricted-composition interfaces; the research-architecture material), plus this paper's own independent result — the assessment-separation theorem with its complete instantiation. The full proof corpus (viability calculus, conservation, noncompensation algebra, sampled kernels, projectability) belongs to Paper 2, the theorem atlas; the ledger, delay-dynamics, and empirical-identification applications belong to Papers 3–5. Where this paper needs an atlas result, it states the canonical form once, cross-references the owning paper, and never transfers a status. Per-statement provenance keys link every concordance-sourced statement to the 409-row inventory; the complete inventory is Appendix A.

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

Twenty-one of this paper's statements are drawn from the programme's source corpus through the concordance of §10; each was verified against its source in a dated closure campaign (full-source reads with per-statement confirmation of existence, kind, proof presence, module, and mapping type; sources A001, A002, A003, A006, A012, A016, A018 closed 2026-08-27/28), and each is stated below at exactly its source-declared status, with no promotion. Content-level verification of provenance is not a theorem-status promotion, and the cross-module interface contract remains an open obligation recorded per row. The complete statement-level inventory, with the per-statement provenance keys, is Appendix A. This paper's own theorems (§4) are complete here, and their machine witness is a committed deterministic artifact.

### 1.5 Relationship to the companion papers

This paper is the first of a series of companion papers: a theorem collection (the atlas) carrying the proof corpus; three application papers (material ledgers, delay dynamics, and sampled governance with empirical identification); and four scored empirical studies on two resource systems, each reporting its own negative certificates. A monograph reintegrates the material at full length after the papers receive external scrutiny. No paper depends on another for a locally load-bearing definition: each carries a Minimal Working Realization of the canonical objects it needs, and §2 is this paper's. Where a result's full development or named instantiations belong elsewhere, the ownership is declared on the line.

---

## 2 The typed canonical framework (Minimal Working Realization)

The framework of this section is the canonical layer of the programme's source corpus (A002): seven stipulated definitions whose per-statement inventory, with provenance keys, is Appendix A (rows CC-A002-001, -003, -004, -005, -006, -019, -035). Paper 2's atlas restates the same definitions in its preliminaries; the canonical forms are stated once here, and the atlas cross-references this paper as the architecture owner.

### 2.1 Type system and physical state

Physical state is typed: a state variable denotes a *moiety* (a named conserved material substance) carrying a *unit*, and typed fluxes connect typed stocks. Conservation claims are per-moiety; the framework does not authorize adding biomass, money, biodiversity indices, and exergy into one conserved scalar. Services, thresholds, information states, and institutional variables are separate types with their own domains — the architecture's first discipline is that no claim mixes types without a declared bridge.

### 2.2 The canonical system

The canonical object is the thirteen-slot tuple `S = (T, Z, S_st, B_out, V, Γ, O, A, C, R, D, K, P)` of the source's canonical form (the atlas's §2.3 states the same tuple): a type system `T`; a state space `Z`; the typed stock–flux structure `S_st`; the boundary interface `B_out`; the class `V` of admissible constitutive laws (declared flux and boundary-rate pairs); the service/technology possibility correspondence `Γ`; the observation operator `O`; the assessment operator `A`; the command architecture `C`; the deployment/reset architecture `R`; the disturbance class `D` with its declared signal space; the safe-and-just set `K`; and the policy class `P`. A *model* in this programme is a fully specified tuple; a *claim* is a statement about a tuple with a status; an *application* is a tuple plus data. The controlling schema version is TCS-1.0 (a TCS-1.1 diff exists but is non-controlling pending migration).

### 2.3 Four uncertainty levels

Uncertainty is stratified into four declared levels — parameter uncertainty within a fixed constitutive model; observation and assessment uncertainty; process disturbances and boundary forcing; and structural uncertainty over a declared model class — with a fixed quantifier discipline per level. The levels do not collapse: a robust-viability claim quantifies over the disturbance set, a diagnostic claim quantifies over the model set, and an epistemic claim quantifies over information states, each with its own proof obligations.

### 2.4 Diagnostic types and the no-transfer rule

A diagnostic claim must declare which of five types it measures — throughput excess (a comparison of typed inflow, extraction, consumption, or waste rates), stock drawdown (a negative stock derivative or integrated typed loss), threshold proximity (a signed margin to a declared boundary), resilience loss (a decline in a declared recovery property), or service or welfare shortfall (failure of a group-specific service or entitlement constraint) — and the no-transfer rule is axiomatic: **a diagnostic is not a causal claim**, and no type name transfers to another without a proved implication on the declared model class. A componentwise deficit identifies where a floor is violated; it does not establish the mechanism. First-passage diagnostics carry timing semantics; they do not establish predictability. This typing governs the empirical layers (Paper 5): diagnostic results carry their declared type and no more.

### 2.5 Threshold and intergenerational types

Thresholds are declared data with provenance (physical, contractual, or normative — the provenance is part of the type), and intergenerational safety is defined by a recursive criterion: each generation's viability is relative to the constraint sets it inherits and the sets it must leave. The intergenerational structures of §7 instantiate this criterion.

### 2.6 Three policy questions and the quantifier discipline

Every application in the programme poses its safety question in one of three fixed forms. Let `z^{π,d}(t; z_0)` be the trajectory under causal policy `π` and disturbance signal `d ∈ D`:

1. **Actual-policy safety:** does the *specified* pair `(π_0, d_0)` keep the trajectory in the constraint set `K`?
2. **Viability:** does *some* `π ∈ P` keep the trajectory in `K`?
3. **Robust viability:** does *one admissible causal policy* work for *every* disturbance in `D`?

The quantifier order is fixed and load-bearing: `∃π ∀d`, not `∀d ∃π`. The policy may react causally to observations; what is excluded is a policy chosen with foreknowledge of the realized disturbance. Section 4's theorem concerns what happens when a *second* quantifier — over assessment weights — is interleaved with this one.

### 2.7 Four model maps

Cross-model claims are licensed only by four declared maps: a **specialisation** (fix parameters or restrict to an invariant subset); an **exact projection** (a semiconjugacy of full and reduced flows); an **approximation** (a declared residual or error bound); and a **singular reduction** (a small parameter, a limiting invariant object, and convergence on a stated time domain). The terms are not interchangeable: "special case", "projection", "approximation", and "singular limit" name different mathematics with different proof obligations, and the concordance records which map every cross-model row uses. The projectability criterion (a `C¹` map `p` carries the flow to a reduced system iff `Dp·F = G∘p`, with uniqueness) is the atlas's to state and prove [Paper 2, family F06]; this paper needs only the map taxonomy and the discipline it enforces.

---

## 3 The three operators at architecture level

The architecture organizes sustainability mathematics under three operators. Their full theorem families are the atlas's (Paper 2); this section fixes the architecture-level reading and states the transformation operator this paper owns.

### 3.1 Maintenance (Operator I)

The maintenance question — can the system be kept inside its constraint sets indefinitely under the declared policy and disturbance classes? — is classical viability (Aubin 1991; Frankowska 1989; Saint-Pierre 1994). The programme's contribution at this level is not a new kernel construction (the standing adjudication is explicit: the kernel calculus is established mathematics) but the *typing*: constraint sets are typed (physical floors, service floors, liability, obligation, identity, cumulative harm), the kernel is computed per typed question, and the three policy questions of §2.6 fix which kernel (actual-policy, existential, or robust) a claim refers to. The atlas carries the kernel calculus, the obstruction calculus (epistemic kernels can be empty while physical kernels are full; observation fibres can defeat any exact safety certificate), and the recovery/irreversibility family.

### 3.2 Observation

Observation is an operator, not a passive input: it thins the policy class (information contraction) and its timing changes kernels. The observation-fibre machinery — including the counterexamples that defeat exact safety certification — belongs to the atlas [Paper 2, families F03/F05]; the architecture-level statement is the interface rule: **an observation claim and a control claim never share a status**; a claim about what can be known is a different type from a claim about what can be done, and the bridge is an explicit theorem, not a verbal slide.

### 3.3 Transformation (Operator II): the finite-architecture recursion

The transformation question — can the system be moved *between architectures* (extraction to regenerative; one governance regime to another) while every transition-safe constraint holds throughout and a maintainable destination is reached? — is formalized by a restricted finite-architecture, fixed-review, exact-tube backward recursion. The data: a finite architecture set `Q`; fixed review times `t_0 < … < t_m`; a disjoint phase state; per-stage admissible meta-actions (causal within-interval control rules plus, when permitted, one architecture transition/reset rule at the interval endpoint); declared disturbance sets; **exact** tubes (the set of phase points visited by every solution branch the declared solution concept admits); successor sets after the permitted endpoint reset; transition-safe sets `S_k` (physical, functional, identity, liability, obligation, and cumulative-harm constraints, conjunctive — noncompensatory); and a destination set `G` whose membership includes the destination architecture's maintainability condition.

The robust predecessor is

```
RPre_k(W) = {(q,x) ∈ S_k : ∃a ∈ A_k(q,x) ∀d ∈ D_k(q,x,a):
             Tube_k(q,x,a,d) ⊆ S_k  and  Succ_k(q,x,a,d) ⊆ W},
```

and `W_m = G`, `W_k = RPre_k(W_{k+1})`. The recursion's theorem — `W_k` is exactly the set of states robustly transformable from stage `k` to `G`; the characterization is a backward induction — is *proved* in the programme's theorem file, and the adjudicated position is: **the recursion and the backward-induction theorem are a typed instance of established discrete viability/capture-basin/robust-predecessor/hybrid-reachability constructions, not new mathematics.** (Aubin 1991; Aubin, Bayen, and Saint-Pierre 2011; Saint-Pierre 1994; Lygeros, Tomlin, and Sastry 1999.) What the typing adds — transition safety checked on full within-interval tubes rather than endpoints; architecture resets that translate identity, liability, and obligations through typed successor states; noncompensatory conjunctive safety; arrival separated from post-arrival maintainability; exact versus conservative-tube conclusions — is modeling semantics with proof obligations, and the paper's independent result (§4) is where those semantics earn mathematical content: a theorem the untyped constructions do not state.

### 3.4 Typed failure classes

Sustainability failure is not one predicate: the typed distinctions of §§2–3 diagnose distinct failure classes, and an assessment verdict must name the class it establishes. The taxonomy:

| Failure class | Meaning |
|---|---|
| Material inconsistency | Balance, unit, donor, or reset equations are internally invalid |
| Physical infeasibility | No physically admissible trajectory satisfies the declared constraints |
| Epistemic/common-prescription infeasibility | Latent states may be viable individually but no observation-based common prescription is safe |
| Authority infeasibility | A saving action exists physically but no authorized prescription can select it |
| Implementation infeasibility | An authorized prescription exists but compliance, enforcement, resources, or actuator deployment cannot realize it robustly |
| Temporal infeasibility | Observation, decision, deployment, or effect arrives after the relevant safety window |
| Recovery failure | The current state cannot reach the target kernel inside the authorized emergency envelope |
| Architecture-transition failure | No registered translation-safe path reaches a viable destination architecture |
| Model-credibility failure | Data, closure, identifiability, approximation, or interface evidence cannot support the claimed verdict |
| Normative incompatibility | Adopted rights, floors, burdens, identities, or authorities cannot be jointly satisfied under the frozen specification |

The classes can coexist, and the assessment rule is to identify the earliest discharged obstruction rather than relabel an epistemic or institutional failure as physical impossibility. The taxonomy is definitional — it fixes what a failure verdict must name, not when failure occurs (programme manuscript §24.1; module-family origin A007 §6, whose nine-class form the architecture-transition class of the transformation operator extends).

---

## 4 The independent result: the assessment hierarchy and its separation

This section is the paper's citable contribution. Proofs are complete; the machine witness is a committed deterministic artifact (`research_program/paper1_instantiation/`, exact integer arithmetic, 25/25 checks).

### 4.1 Three assessments on one datum

Fix a typed exact-tube datum as in §3.3 whose transition-safe registry and destination set are typed noncompensatory: `S_k = S_k^phys ∩ {s_i ≥ 0, i = 1..n}` and `G = G^phys ∩ {s ≥ 0}`, with `s = (s_1,…,s_n)` the typed floors (normalized to 0 by translation). Let

```
C = R^n_+ \ {0}
```

be the **nonzero nonnegative orthant** (the closed cone `R^n_+` minus the origin, which is vacuous as a price vector) of aggregate weight vectors. The full nonnegative cone — not the strictly positive orthant — is the right model of the aggregate assessment for three reasons: zero prices are admitted by the weak-assessment semantics (aggregate indices routinely price a capital form at zero); on the full cone the pointwise aggregate is lossless (Lemma 4.2), which isolates the entire assessment gap in the dynamic quantifier structure; and intersecting the scalarized assessments over the full cone is the *strictest* aggregate reading — the intersection over any subfamily, including all strictly positive price vectors, is a superset — so the separation of Theorem B and the nonemptiness of its gap persist under every restriction of the price family.

For a state `z` and stage `k`, define three admissible-action sets:

- **endpoint-only physical:** `E_phys(z) = {a : ∀d, Tube(a,d) ⊆ S^phys and Succ(a,d) ⊆ G^phys}` — the endpoint-accounting audit (physical coordinates only);
- **scalarized aggregate at weight `w`:** `E_w(z) = {a : ∀d, Tube(a,d) ⊆ S^w and Succ(a,d) ⊆ G^w}` — the weak-sustainability index (one floor, prices `w`, compensation across floors, disturbances respected), where `S^w := S^phys ∩ {w·s ≥ 0}` and `G^w := G^phys ∩ {w·s ≥ 0}` are the scalarized safe and destination sets;
- **noncompensatory typed:** `E_typ(z) = {a : ∀d, Tube(a,d) ⊆ S_k and Succ(a,d) ⊆ G}` — the strong-sustainability registry (each floor separately binding).

All three retain the same disturbance quantifier; the assessments differ *only* in constraint structure. The assessment predecessors are `{z : E(z) ≠ ∅}` respectively.

### 4.2 Lemma (closed-cone pointwise equivalence)

For `v ∈ R^n`: `v ≥ 0` componentwise ⟺ `w·v ≥ 0` for every `w ∈ C`.

*Proof.* (⇒) `w ≥ 0`, `w ≠ 0`, `v ≥ 0` gives `w·v = Σ w_i v_i ≥ 0`. (⇐) Contrapositive: if `v_k < 0`, take `w = e_k ∈ C`: `w·v = v_k < 0`. ∎

The companion static fact — that for *strictly positive* weights `w·Δ ≥ 0` does not imply `Δ ≥ 0` — is the atlas's Proposition 5.1 [CC-A002-007, Paper 2 family F02]: the open cone's static compensation failure. The two statements are complementary: on the closed cone, at a fixed point or along a fixed trajectory, the aggregate with all cone weights is *exactly* as informative as the vector of floors. Every dynamic gap in this section is therefore attributable to the quantifier structure alone — not to static scalarization blindness.

### 4.3 Theorem A (assessment hierarchy and quantifier noncommutativity)

**(i) Hierarchy.** For every weight `w ∈ C`: `E_typ(z) ⊆ E_w(z) ⊆ E_phys(z)`; hence `{P_typ} ⇒ {∀w: P_w} ⇒ {P_phys}`.

**(ii) Localization.** For every state `z`: `E_typ(z) = ⋂_{w∈C} E_w(z)`. The two assessment predecessors therefore differ exactly by the order of "there exists a plan" and "for all weights": `{P_typ} = {z : ⋂_w E_w(z) ≠ ∅}` (one plan serves every price vector) versus `{∀w: P_w} = {z : ∀w, E_w(z) ≠ ∅}` (every price vector has its own plan). Existential choice of plan does not commute with the universal quantifier over weights.

**(iii) Strictness.** Both inclusions can be strict simultaneously on one datum with two architectures, two typed floors, four meta-actions, and a two-point disturbance set (Theorem B).

*Proof.* (i) Let `a ∈ E_typ(z)`. For every `d`, `Tube(a,d) ⊆ S_k = S^phys ∩ {s ≥ 0}`, and by Lemma 4.2 (⇒) every tube point satisfies `w·s ≥ 0` for every `w ∈ C`; likewise successors lie in `G ⊆ G^w`. So `a ∈ E_w(z)`. The inclusion `E_w ⊆ E_phys` is immediate from `S^phys ∩ {w·s ≥ 0} ⊆ S^phys` and `G^phys ∩ {w·s ≥ 0} ⊆ G^phys`. (ii) `⊆` by (i). `⊇`: if `a ∈ ⋂_w E_w(z)`, then for every `d` and every tube point `p`, every `w ∈ C` gives `w·s(p) ≥ 0`, so `s(p) ≥ 0` by Lemma 4.2 (⇐); hence `Tube ⊆ S_k`, and the same argument over successors gives `Succ ⊆ G`. (iii) is Theorem B. ∎

**Corollary A.1 (no price vector rescues the assessment).** On the datum of Theorem B, `⋂_{w∈C}{P_w} ⊋ {P_typ}` with nonempty interior. Since intersecting the scalarized assessments over *any* subfamily of `C` gives a superset of the full intersection, no choice of prices — and no family of price vectors — recovers the noncompensatory predecessor on that datum. The noncompensatory assessment is not the limit of weak assessments.

**Position.** Theorem A(i) is standard mathematics: it is constraint-set monotonicity of viability kernels/reachability sets (Aubin 1991; Frankowska 1989) applied to `S_typ ⊆ S_w ⊆ S_phys`. The claim of this paper is (ii)–(iii): the localization and the witnessed separation.

### 4.4 The witness datum

Two architectures — extraction `q=0`, regenerative `q=1` — one review interval `[0,1]`, phase state `(q, x, s_1, s_2)`: a physical reserve stock `x` and two typed floors — protected-group service surplus `s_1` and remediation-liability coverage surplus `s_2` (floors normalized to 0). `S_0 = {x ≥ 0, s_1 ≥ 0, s_2 ≥ 0}`; `G = {(1,x,s) : x ≥ 0, s ≥ 0}` (the destination maintainability condition is witnessed by the destination hold policy, under which `G` is robustly invariant — declared datum). Disturbance set `{β, α}` scales dip depth (worst-case dip 2); destination reset gains `e = (1/4, 1/4)` on the two floors; rescue cost `c = 1`. The four meta-actions, from any initial `(0, x, s)` with `x ≥ 0, s ≥ 0`:

| action | within-interval trajectory | successor |
|---|---|---|
| `NO-SWITCH` | state constant | `{(0,x,s)}` — misses `G` |
| `FAST` | `s_1` dips to `s_1 − 2` mid-interval (adverse disturbance); `s_2`, `x` constant | `{(1, x, s+e)}` |
| `SLOW` | `s_2` dips to `s_2 − 2` mid-interval; `s_1`, `x` constant | `{(1, x, s+e)}` |
| `STAGED` | floors grow; `x` spends linearly to `x − 1` | `{(1, x−1, s+e)}` |

Interpretation: `FAST` is the immediate full switch (deployment gap dips protected service; escrow continues); `SLOW` is the phased switch (service maintained; the liability handover window dips coverage); `STAGED` rents temporary capacity and bridges the escrow — no typed dip — at physical cost `c`; `NO-SWITCH` is transit-safe but lands outside the destination. Every trajectory is piecewise linear on breakpoints `{0, ½, 1}` and monotone per piece, so all tubes below are the **exact** visited sets — no outer approximation anywhere in the datum or its machine verification.

### 4.5 Theorem B (false positives, blindness levels, disagreement, rescue, impossibility)

On the witness datum, over initial states `X_0 = {(0,x,s) : x ≥ 0, s ≥ 0}`:

**(1)** `{P_typ} = {x ≥ 1} ∪ {s_1 ≥ 2} ∪ {s_2 ≥ 2}` — one floor survives its own worst-case dip, or the bridge is funded.

**(2)** `⋂_{w∈C}{P_w} = {x ≥ 1} ∪ {s_1 + s_2 ≥ 2}` — the aggregate family's binding condition (at the worst weight `w = (1,1)` both plans need the same budget) is the **total-capital budget** `s_1 + s_2 ≥ 2`.

**(3)** `{P_phys} = X_0` — endpoint-only accounting admits every state (the physical endpoint is always reachable).

**(4)** The **false-positive set** `FP = {x < 1, s_1 < 2, s_2 < 2, s_1+s_2 ≥ 2}` — the triangle between the coordinate thresholds and the budget line — is nonempty with interior.

**(5)** Both hierarchy inclusions are strict on this one datum: every point of `FP` lies in `⋂_w {P_w} \ {P_typ}`, and the point `(½, 1/10, 1/10)` lies in `{P_phys} \ ⋂_w{P_w}` (endpoint-feasible while *no* action is aggregate-safe at `w = (1,1)`).

**(6)** **Per-weight plan disagreement.** On the triangle interior, the FAST-certifying weights are exactly `{r = w_2/w_1 ≥ ρ_1}`, the SLOW-certifying weights exactly `{r ≤ ρ_2}`, with `ρ_1 = (2−s_1)/s_2`, `ρ_2 = s_1/(2−s_2)`, and `ρ_2 ≥ ρ_1 ⟺ s_1+s_2 ≥ 2`, strict on the interior. High-`s_2`-price assessors (`r > ρ_2`: the priced form `s_2` is expensive relative to `s_1`) license `FAST` only; low-`s_2`-price assessors (`r < ρ_1`) license `SLOW` only; assessors at intermediate prices (`ρ_1 ≤ r ≤ ρ_2`) license both — and **no single action serves every price vector** — which is exactly `E_typ = ⋂_w E_w = ∅` (Theorem A(ii)).

**(7)** **The rescue split.** With `FP_0` the triangle (x unrestricted): the **rescue set** `R = FP_0 ∩ {x ≥ 1}` is typed-transformable, witnessed by `STAGED` — the bridging plan at physical cost `c` keeps both floors intact and lands in `G`; the **impossibility region** `I = FP_0 ∩ {x < 1}` is aggregate-feasible for every cone weight yet admits *no* typed-admissible action, with four exhibited violations: `FAST` violates the protected-service floor under the adverse disturbance; `SLOW` violates the liability-coverage floor; `STAGED` drives the physical stock negative; `NO-SWITCH` misses the destination architecture.

*Proof.* (1) `NO-SWITCH` fails `G`; `FAST`'s worst-case `s_1`-tube is `[s_1−2, s_1]`, safe iff `s_1 ≥ 2`; `SLOW` symmetrically iff `s_2 ≥ 2`; `STAGED`'s `x`-tube is `[x−1, x]`, safe iff `x ≥ 1`. (2) For `x ≥ 1`, `STAGED` is aggregate-safe for every `w` (tubes monotone; the aggregate of nonnegative coordinates with nonnegative gains stays nonnegative). For `s_1+s_2 ≥ 2` with `s_1, s_2 < 2`: both floors are then strictly positive; `FAST` is aggregate-safe iff `w_1(s_1−2) + w_2 s_2 ≥ 0`, i.e. `r ≥ ρ_1`; `SLOW` iff `w_1 s_1 + w_2(s_2−2) ≥ 0`, i.e. `r ≤ ρ_2`; and `ρ_2 ≥ ρ_1` ⟺ `s_1s_2 ≥ (2−s_1)(2−s_2)` ⟺ `s_1+s_2 ≥ 2`, so every `r ∈ [0, ∞]` is covered (`w = e_1`, `e_2` always covered by `SLOW`, `FAST` respectively; endpoints in `C`). Conversely, if `x < 1` and `s_1+s_2 < 2`: at `w = (1,1)`, `FAST` and `SLOW` both need `s_1+s_2 ≥ 2`; `STAGED` violates the physical tube (and `S^w ⊆ S^phys`, so no aggregate floor compensates a physical violation); `NO-SWITCH` misses `G^w`. (3) `FAST` is always physically admissible. (4)–(5) follow from (1)–(3); `(½, 6/5, 6/5)` is an interior point of `FP` since `6/5 + 6/5 = 12/5 > 2` with both coordinates below 2. (6) is the two computations of (2) with `w_1, w_2 > 0`; a single action serving every weight would lie in `⋂_w E_w = E_typ`, contradicting (1). (7) `STAGED`'s tubes on `R`: floors grow from `s ≥ 0`, `x`-tube `[x−1, x] ⊆ [0, ∞)`; successor in `G`. On `I` the four violations are the four computations above, one exhibited violated constraint per action, the actions exhausting `A_0`. ∎

**Remark.** The aggregate assessment's binding condition is the total-capital budget; the noncompensatory assessment requires one floor to survive its own worst-case dip or the bridging resource to be funded. The triangle between them is exactly where the weak doctrine certifies a transition — per price vector, with price-dependent plans — that the strong doctrine rejects. And the typed recursion does not merely reject: it names the binding resource (`x` at cost `c`) and the exact subregion where funding the bridge converts the false positive into a certified transformation.

### 4.6 Theorem C (propagation through the backward induction)

Extend the datum to `m ≥ 2` intervals by prepending hold intervals (sole action `HOLD`: constant tube `{z}`, successor `{z}`, safe set `S_0`; the last interval carries the witness datum). Define each assessment's backward recursion with its own terminal set (`G`, `G^w`, `G^phys`) and safe sets. Then: (i) for every stage `j`, `W^typ_j ⊆ ⋂_{w∈C} W^w_j ⊆ W^phys_j` — and this hierarchy holds for *every* multi-interval typed exact-tube datum, hold-prefixed or not; (ii) the stage-0 regions are the witness regions pulled back through the holds, so both strictness witnesses persist; (iii) the separation is not an artifact of the one-interval framing.

*Proof.* (i) Downward induction. Base: `G = G^phys ∩ {s ≥ 0} ⊆ G^phys ∩ {w·s ≥ 0} ⊆ G^phys` by Lemma 4.2. Step: a typed-admissible action's tube lies in `S_j ⊆ S^w_j` (Lemma 4.2, ⇒) and its successors in `W^typ_{j+1} ⊆ W^w_{j+1}`; the second inclusion is identical with `S^w_j ⊆ S^phys_j`. (ii) `HOLD` is the unique action and is assessment-admissible iff `z ∈ S^·_j` and `z ∈ W^·_{j+1}`. (iii) The strictness witnesses lie in `S_0` (their floors are met initially), so they hold through the prefix. ∎

### 4.7 The machine witness

Every claim of Theorems A/B/C is machine-checked by a committed deterministic artifact: `research_program/paper1_instantiation/typed_false_positive_instantiation.py` — exact integer arithmetic (scale 40; no floats, no tolerances, no randomness, no outer tube approximation) — over a 29,791-state grid with dense critical weight sets including the exact boundary weights `ρ_1`, `ρ_2` and the adversarial midpoint `(ρ_1+ρ_2)/2`: the three region identities, the hierarchy, the false-positive set (1,900 grid states) with its interior witness, both strictness witnesses, the plan disagreement at named weights (`r = ½` SLOW-only, `r = 1` both, `r = 2` FAST-only), `E_typ = ⋂_w E_w = ∅` verified over the full critical weight set, the rescue split with the four exhibited violations, and Theorem C through two prepended hold intervals. 25/25 checks pass; re-execution reproduces the outputs exactly; the JSON results and the human-readable report are committed alongside the runner.

---

## 5 Weak and strong sustainability as assessment doctrines

### 5.1 The reading of Theorem B

The scalarized assessments are the weak-sustainability doctrine in exact robust form: one index `w·s`, prices on capital forms (zero prices allowed — uncosted ecosystem services are the canonical case), floors substitutable at those prices, disturbances respected. The typed registry is the strong-sustainability doctrine: each critical floor separately binding. Theorem B then reads: *the two doctrines can disagree on the same transition system with the same robustness standard and the same action set, in the direction weak-accepts/strong-rejects, on a set with interior — and the disagreement is not an artifact of one bad price vector: every price vector accepts, each licensing a different physical transition.* The plans are genuinely different transitions (`FAST` and `SLOW` violate different floors at different times — asynchronous dips), which is the dynamic formalization of compensation across incommensurable capitals. By Theorem A(ii) the disagreement's precise seat is the noncommutativity of "choose a plan" with "for all prices": at the static level the closed-cone aggregate is lossless (Lemma 4.2), so the weak doctrine's blind spot is not the existence of an aggregate index but the *policy dependence of the aggregate-feasible transition*. Endpoint-only accounting is a third, strictly weaker audit level — blind even to aggregate transit dips (Theorem B(5)).

### 5.2 Positioning against established theory

**Conceded as established (cited, never claimed).** The backward recursion of §3.3 is a typed instance of established robust-predecessor/reach-avoid/capture-basin/hybrid-reachability constructions [Aubin–Bayen–Saint-Pierre; Saint-Pierre; Aubin; Lygeros–Tomlin–Sastry]. Theorem A(i) is viability-kernel constraint monotonicity [Aubin; Frankowska]. The static scalarization limitations are established: weighted sums cannot reach nonconvex parts of Pareto fronts [Das–Dennis 1997] — a different mechanism (frontier geometry under a single optimization, not the action quantifier under per-weight feasibility). Compensability analysis is established in MCDA, including the explicit mapping of compensatory aggregation to weak and outranking methods to strong sustainability [Cinelli et al. 2014; Schär et al. 2025]. Multiple-barrier composition and compatibility is an active control literature. Scalarization-dependent optimal policies are a staple of multi-objective RL. The weak/strong sustainability debate and the genuine-savings indicator line are mature [Neumayer; World Bank; Boos 2015; Hanley et al.; Ekins et al. 2003; Usubiaga-Liaño 2025] — cited as motivation, not as prior art for the theorem form.

**Claimed as this paper's contribution.** (i) Theorem A(ii): the per-state identity `E_typ = ⋂_{w∈C} E_w` and the quantifier-order characterization — with the closed-cone choice making the separation purely dynamic. (ii) Theorem B: the closed-form witness with per-weight plan disagreement and the rescue/impossibility split — the negative-certificate form applied to assessment doctrines. (iii) Theorem C: the propagation. (iv) The interpretation: the first formal dynamic separation of the two assessment doctrines on one transition system with one robustness standard. The full novelty map, with queries and raw search records, is committed at `research_program/paper1_full_text_novelty_pass.md`; its no-match-found verdicts are bounded absences, and the manuscript's claims are conditioned accordingly.

**Not claimed.** A general theorem for robust transformation between system architectures is not asserted here; robust reach-avoid with resets is established. The supported claim is the assessment-doctrine separation.

### 5.3 What the theorem does not say

No claim of aggregate blindness at fixed trajectories (Lemma 4.2 is the opposite). No separation on every datum (where a single plan is safe for all weights, the assessments coincide — the theorem is an existence separation with interior, plus the always-valid hierarchy and localization). No infinite-horizon, stochastic, partial-observation, or endogenous-event extension. No claim that the full nonnegative cone is the only reasonable aggregate family (intersecting over the full cone is the strictest aggregate reading; restricting the price family enlarges the intersection, so the separation persists under any restriction). No welfare claim about prices: the weights model assessment doctrines, not normative endorsement. No transfer to empirical systems: the theorem is about assessment operators on a declared datum; it asserts nothing about any fishery or aquifer — those questions belong to Papers 3–5 with their own data and status discipline.

---

## 6 Governance, authority, and implementation

### 6.1 Constructors

Governance instruments enter the architecture as *constructors*: a constructor is a map on the system data `(X, U, F, I, π)` that changes **exactly one named component and introduces no new state space**. The primitives [A001 §13.6]: `Cap(Q)` (an upper harvest bound), `Floor(H_min)` (an output floor), `Tax(τ)` (a price entry in the effort law), `Excl` (excluding a competing predator), `Leak(h)` (unreported/illegal harvest added to realized take), `Obs(I, Ψ)` (replacing the observation map and feedback law), and `Rest(·)` (any other restriction of the control correspondence). Restriction of the action correspondence obeys a one-sided monotonicity: enlarging the correspondence preserves existential viability — `U_1(x) ⊆ U_2(x)` for every `x` implies `Viab(V; U_1, F) ⊆ Viab(V; U_2, F)` — so the family of action correspondences with a nonempty existential viability kernel is upward closed and closed under unions, while intersections (meets) are not generally preserved: intersecting two viable correspondences can remove the distinct selectors that witness each kernel, and a smaller correspondence remains viable only when it retains a viable selector — an additional fact, not downward lattice monotonicity [A001 §13.6]. Universal-action invariance has the opposite monotonic tendency and is named separately. Observation is not on this axis: it thins the policy class rather than the action correspondence, a separation of axes the architecture treats as the formal content of "governance restricts".

**The implementability ladder.** The action correspondence is itself layered: `U_impl(z) ⊆ U_inst(z) ⊆ U_tech(z) ⊆ U_theor(z)` — actions actually executable given incentives, power, legitimacy, compliance, and enforcement, within institutionally authorized and resourced actions, within technically feasible actions, within the actions an abstract equation permits — with the parallel policy-class ladder `P_impl ⊆ P_inst ⊆ P_tech ⊆ P_theor` for causal policies mapping information histories to actions (a decentralized or strategic implementation may use a policy profile, its membership in the implementable class depending on the applicable equilibrium, enforcement, and information conditions). The definitional point is load-bearing: within-architecture viability quantifies over the implementable class `P_impl`, and a viability result established over a technological or theoretical class does not transfer downward — restriction of the correspondence can empty the kernel even where enlargement preserves it. The architecture fixes where domain-specific institutional, political, and game-theoretic models of executability enter, without claiming a universal equilibrium theory (programme manuscript §5.3).

### 6.2 Management vocabularies are rewrites, not theorems

A total allowable catch is `Cap`; a harvest control rule is `Obs`; a landing subsidy is `Tax(−σ)`; unreported harvest is `Leak`; a closed season is a periodic `Cap`; an open-access rent dynamic is a restriction of the effort law entering `F`. Each common instrument is a word in the constructor algebra and introduces no new mathematical content beyond the constructor it reduces to. *Proof (summary of the source's proof):* each instrument is realized as a single constructor on the tuple; by invariance under irrelevant structure (a proposed addition that changes no component of the tuple does not change the kernel), each changes the problem class only through its one component. This is the architecture's formal completion rule: **new content requires a new constructor, a new physical type, or the resolution of a residual** — not a new name for an old restriction. ∎

The research-architecture consequence: management vocabulary growth is not theory growth, and the constructor algebra is the check.

### 6.3 The commons obstruction

The safe aggregate-harvest capacity is declared first: at a stock boundary or on a declared safe strip, `H_safe(S)` is defined through the tangent requirement `g(S) − H ≥ 0`, or the equivalent drift condition is stated directly [A001 §12.3, Definition 12.2]. The obstruction is a **finite-time** result. Suppose that under the implemented Nash feedback there exist `a > 0` and `ε > 0` such that

```
g(S) − H^Nash(S) ≤ −ε    for every S ∈ [S_min, S_min + a],
```

and every relevant trajectory is either initially in this strip or is proved to reach it. Then each such trajectory exits below `S_min` within at most `a/ε` time units after entering the strip. *Mechanism (summary of the source's proof):* inside the strip the drift is at most `−ε`, so integration reaches the floor in bounded time — the obstruction is a *governance* fact: the play structure, not the physics, exhausts the constraint set. The uniform margin is load-bearing: strictly negative drift without a uniform margin does not by itself imply finite-time exit. The obstruction is removable by constructors in the institutional direction (graduated sanctions prevent the over-extraction; monitoring bounds the observation error so state feedback applies) — the architecture's reading of why institutional and physical variables belong to one typed system. The full institutional implementation family is the atlas's [Paper 2, §12].

### 6.4 The institutional interface

The institutional-feedback model class carries a declared scope restriction — *weak viability coupling*: use has limited or indirect effect on reproduction (Appendix A, CC-A003-006). The composition interface is conditional: compositional safety across coupled subsystems holds *conditional on the interface contracts; separate subsystem certificates alone do not imply network safety* — stated without proof in its source and carried at exactly that conditional status. The architecture's rule for both: the conditionality and the scope restriction are part of the content, stated on the line, and are not weakened by restatement.

---

## 7 Intergenerational structures

### 7.1 Generation structure

A *generation structure* is a sequence `0 = t_0 < t_1 < ⋯ → ∞` of generation boundaries with closed per-generation constraint sets `V^(k)`; *intergenerational viability* requires `x(t) ∈ V^(k)` for `t ∈ [t_k, t_{k+1})` — each generation's trajectory segment must respect that generation's floors. The structure instantiates the recursive intergenerational safety criterion of the threshold types [CC-A002-006]: safety is relative to inherited sets and constrains bequeathed sets.

### 7.2 The stationary equivalence

If `V^(k) = V` for all `k` — the stationary case — intergenerational viability *equals* ordinary viability. The theorem is an immediate equivalence; its content is the reminder that intergenerational content begins exactly when the generation sets are *not* stationary: floors tighten, degrade, or shift across generations.

### 7.3 The nested-impossibility theorem

Assume trajectories are confined to a compact set (verified per instance via dissipativity). If the generation sets are nested decreasing with empty intersection — each generation's floors strictly harder, collectively unsatisfiable — then **no intergenerationally viable path exists**. *Proof (summary of the source's proof):* a viable path would be a trajectory forever inside a nested family of closed sets with empty intersection inside a compact set — impossible by compactness: the trajectory has limit points, and every limit point would have to lie in every `V^(k)`. ∎ This is the architecture's canonical intergenerational negative result: sustainability can fail *generation-structurally*, with every finite segment satisfiable, and the failure is a theorem, not a scenario.

---

## 8 Restricted composition and model transformations

### 8.1 Effort-scale invariance

In the registered delay-dynamics family, the effort-scale transformation — `E' = aE`, `E'_max = aE_max`, `q' = q/a`, `δ_0' = aδ_0`, with correspondingly scaled effort histories — leaves the `(N, Z)` trajectories invariant. The transformation is exact (a `TRANSFORMATION`-typed map in the concordance's four-map taxonomy), and its architecture role is identifiability discipline: effort scales are not separately identifiable from the stock dynamics, so calibration claims must quotient by the transformation. Paper 4 owns the family; this paper states the map and the discipline.

### 8.2 Yield-gap soft-minimum and weak coupling

At the Liebig (most-limiting) limit, the yield gap obeys the soft-minimum bound `π_j ≤ w_min^{-1} e^{−ρΔ_y}` and the coupled system decouples with error `‖X − X^k‖ ≤ C_T ε_c`, `ε_c = C e^{−ρΔ_y} + ε_phys` — weak coupling is *quantified*, not assumed: the decoupling error is a proved function of the yield gap and the physical error bound. This is the architecture's model for how composition claims should be licensed: an explicit error bound on a declared map, the approximation taxonomy of §2.7 doing its work. Paper 4/6 own the applications.

### 8.3 Coupling creates viability

An explicit two-factor example (`g_i(s) = s(1−s)`, coupling `d = 0.2`, equilibrium-defined harvest floors) in which *coupling creates viability that is absent in a factor*: the coupled system's kernel is nonempty while a decoupled factor's is not. Together with the atlas's coupling-destroys-viability results [Paper 2, family F10], the architecture's composition lesson is two-sided: composition is neither safe nor unsafe in general — each direction is a theorem with its own witness, and unrestricted composition is not licensed (the restricted-composition contracts and their counterexamples are the atlas's).

### 8.4 Exergy, quality grades, and nonsmooth transformation feasibility

The transformation operator's open extension: transformation feasibility under exergy and quality-grade constraints, where the feasible set is nonsmooth (grades induce kinks). The source registers this as a research programme, not a theorem set; the architecture carries it as the declared frontier of the transformation operator — typed, with the nonsmoothness named as the obstruction class. No status is asserted beyond programme.

---

## 9 Negative results as first-class content

### 9.1 The negative-certificate methodology

The architecture treats a *negative certificate* — a rejection with an exhibited violated constraint, per action, exhausting the action set — as a first-class result. Theorem B(7) is the assessment-side instance: four actions, four exhibited violations, a certified impossibility *plus* the resource and price at which the impossibility dissolves. The programme's scored-forecast layers instantiate the same methodology empirically: both scored evaluations returned negative certificates (no module constituting additional structure was admitted on either system, under the preregistered scoring — on the cod series the persistence benchmark was not defeated; on the aquifer it was beaten at the one-year horizon by the univariate AR(1), retained at a 0.39 ft margin as output-only, and by causal variants that reduce to that AR(1), all declined on class grounds). The methodology's content: **complexity is retained only on scored evidence**; an unfalsified model class is not an achievement, and a rejected complexity is a finding.

### 9.2 The admission discipline

Modules enter the architecture through an admission standard (preregistered scoring against declared baselines; held-out defect audits; frozen retention rules), and the architecture's claim about itself is limited: the integration — typed schema, claim statuses, model maps, certificate/status layer, negative-certificate methodology — is the contribution; the component mathematics retains its established provenance, and the integration does not establish universality.

### 9.3 Normative premises in the typed registry

The typed registry carries *tagged normative premises*: e.g. the adaptive-capacity material registers "B6 is a normative premise" as a tagged registry row, and proposed floors (participation/recruitment non-decline) as normative and unoperationalized research-programme items (Appendix A, CC-A016-001 and CC-A016-010). The architecture-level rule these rows instantiate: **normative content is tagged, never formalized covertly** — a floor's provenance (physical, contractual, normative) is part of its type (§2.5), and a normative floor that has not been operationalized says so on the line. Negative-lesson sources (institutional-solvency failures, distributive-barrier impossibilities, rejected multidomain syntheses, institutional-index negatives) are routed into the paper set, the monograph, and the traceability archive under the same rule: no separate paper, no deletion, status intact — the solvency and institutional-index negatives into the atlas's institutional-implementation family (Paper 2, §12), the multidomain rejection's closing lesson into the empirical case synthesis (Paper 5, §6.3), the distributive-barrier redesign into the monograph's institutional and distributive operationalization.

---

## 10 Reproducibility and data availability

All computational results in this paper are verified by a committed deterministic artifact (`research_program/paper1_instantiation/`): exact integer arithmetic at scale 40 — no floating-point operations, tolerances, or randomness — over a 29,791-state grid with dense critical weight sets including the exact boundary weights and the adversarial midpoint; all 25 checks pass, and re-execution reproduces the outputs exactly. The runner, the JSON results, and the human-readable report are committed alongside the raw novelty-search records. The certification level of this verification is *exact* — the strongest tier available to a finite discrete verification. More generally, computational claims in the programme carry a declared certification level — nominal, re-execution-verified (outputs identical on fresh execution), independently re-executed (a second agent and toolchain), or certified (interval or rigorous arithmetic) — stated per claim and never implied; the present paper makes no computational claim beyond the exact witness above.

The architecture is operationalized in a source-to-canonical-to-publication concordance of 409 mappings, each linking a source proposition to canonical notation, assumptions, evidence status, mapping type, and destination. Of these, 354 have completed statement-level scientific verification across nineteen sources; the remainder are either adjudicated negative-register entries (28) or open rows attached to conditional results (27, exactly the three gated conditional-paper sources). The concordance, its machine layer, and the verification records are provided in the repository. Every valid source proposition in the corpus maps to a paper section, an appendix, a conditional docket, or an explicit negative record — the non-loss rule the concordance checks row by row. One finding of the verification campaign is part of the architecture's claim: machine verification of the concordance (quotes, coverage, vocabulary) is not content verification — the campaign's found-and-repaired defect classes (intake row corruption, keyword false positives, register misalignment) are the evidence.

## 11 Future directions

The architecture generates a set of falsifiable conjectures for future empirical work. None is executed here, and none carries an empirical finding; the full set, with the falsification test designs and candidate leading indicators and their architectural rationales, is provided in the supplementary material. The nine conjectures are: **compositional sustainability** — local typed contracts can establish jointly viable behaviour without monolithic verification, under identifiable compatibility, timing, robustness, and interface conditions; **transformability** — sustained contraction or emptiness of the viability kernel predicts the need for architecture change earlier than output failure; **capacity-leading failure** — declining regenerative, maintenance, or governance capacity predicts typed failure earlier than current output measures; **bottleneck–robustness** — smaller typed bottleneck margin predicts smaller estimated robustness margin after controls, within a preregistered system class and comparable disturbance geometry; **boundary-expansion reversal** — some favourable assessments reverse when imported resources, exported burdens, affected populations, and deferred liabilities enter through adequate boundary interfaces; **distributional dynamics** — unequal provision and burden can alter health, compliance, conflict, and governance enough to change the functional viability kernel; **correlated-disturbance amplification** — independence-assuming models underestimate joint failure where shocks share causes or reinforcing feedback; **maintenance suppression** — diverting maintenance toward present output raises visible performance while reducing future viability and transformability; and **efficiency–scale interaction** — efficiency gains do not reliably reduce total burden where scale and rebound exceed intensity reduction. Each candidate leading indicator's predictive advantage over simpler outcome indicators is an empirical requirement, not a guarantee of definition.

The conjectures are governed by preregistration restrictions: no conjecture is rescued by arbitrary post-hoc state augmentation; each study preregisters system class, specification, candidate indicators, excluded variables, predicted direction, acceptable model revisions, and the observations that count against the conjecture; and the unrestricted claim that every sustainability failure is representable at an "adequate scale and resolution" is excluded as too elastic to falsify. The mechanism-level hypotheses (observation aggregation, governance phase ordering, substitution certificates) and their declared tests belong to the empirical-identification companion paper and are complementary to, not duplications of, the conjectures above.

## 12 Provenance and limits

**Provenance.** Bracketed pointers of the form [A001 §13.6] reference the programme's source corpus — the manuscripts from which the concordance-sourced statements of this paper were verified — committed, together with the concordance itself, to the project repository (<https://github.com/MIKEAA2020/general-sustainability>). The manuscript-native theorems (§4) are complete in this paper; their full development, proofs, and machine witness are the committed files `research_program/paper1_typed_false_positive_theorem.md` and `research_program/paper1_instantiation/` (runner, JSON results, report, raw novelty-search records). Appendix A carries the statement-level inventory. The further manuscript-native entries (§3.4, §6.1, §11) restate programme-manuscript content at its declared statuses — the implementability ladder (programme manuscript §5.3), the typed failure taxonomy (programme manuscript §24.1; module-family origin A007 §6), and the architecture-level empirical conjectures, falsification tests, and leading indicators with their preregistration restrictions (programme manuscript §§27–29) — each restating its source at exactly the declared status.

**Limits.** (i) The assessment-separation theorem is an existence result with interior, not a claim that the gap is always large; on dominated-action data the assessments coincide. (ii) Its novelty verdicts at no-match-found are bounded-search absences, conditioned per §5.2; if external review overturns a verdict, the fallback destination is the monograph's series introduction — the programme's standing fallback rule, not a demotion. (iii) All concordance rows behind this paper (Appendix A) are content-verified against their sources; no statement depends on a pending verification. (iv) The architecture covers no infinite horizons, no partial observation, no stochastic chance constraints, and no endogenous event times at the transformation-operator level; each exclusion is recorded in the theorem files and inherited here. (v) The empirical layers of the programme (Papers 3–5) own every data-bearing claim; this paper asserts nothing empirical — the conjecture set, falsification tests, and leading indicators of §11 are declared at non-executed conjecture and design status and carry no empirical finding.

---

## Appendix A. Statement inventory and verification summary

This appendix inventories the formal statements of the paper in two tables. The **identifier** column carries the programme's concordance row codes (`CC-A0dd-ddd`) or manuscript-native keys (`MS-Native-n`, `Infra-1`); the codes key each statement to the source-to-canonical inventory committed in the repository and are provenance keys, not citations. Every concordance-sourced entry was verified against its source manuscript in the closure campaign of 2026-08-27/28 (full-source reads with per-statement confirmation of existence, kind, proof presence, module, and mapping type); this is content-level verification of provenance, not a promotion of any entry's mathematical status.

**Legend and disclaimer.** Entries categorized as *Definition*, *Axiom*, *Scope*, *Registry*, *Programme*, or *Registration* are stipulated or declared — they carry no empirical truth-value and need no proof. Entries categorized as *Theorem*, *Lemma*, *Identity*, or *Example* are established under the assumptions stated where they appear (proved in this paper, or summarized from the identified source's proof). Entries categorized as *Conditional theorem* retain their hypotheses as mathematical content. The formal validity of any entry within the declared framework does not by itself imply applicability to an empirical system (§12, Limits). No status is promoted anywhere in this inventory; the manuscript-native results MS-Native-1–4 are this paper's own, with artifact provenance, and MS-Native-5–8 restate programme-manuscript content that carries no concordance row, each at exactly its declared status.

**Table A1. Stipulated definitions, axioms, scope restrictions, and declared programme entries.**

| Identifier | Statement | Category | Basis |
|---|---|---|---|
| CC-A002-001 | Type system and physical state (§2.1) | Definition | Stipulated; restated from source A002 |
| CC-A002-003 | Canonical system, thirteen-slot tuple (§2.2) | Definition | Stipulated; source A002 |
| CC-A002-004 | Four uncertainty levels with fixed quantifier discipline (§2.3) | Definition | Stipulated; source A002 |
| CC-A002-005 | Diagnostic types and the no-transfer rule (§2.4) | Definition | Stipulated; source A002 |
| CC-A002-006 | Threshold and intergenerational types (§2.5) | Definition | Stipulated; source A002 |
| CC-A002-019 | Three policy questions (§2.6) | Definition | Stipulated; source A002 |
| CC-A002-035 | Four model maps (§2.7) | Definition | Stipulated; source A002 |
| CC-A001-077 | Governance constructors (§6.1) | Definition | Stipulated; source A001 §13.6 |
| CC-A001-082 | Generation structure (§7.1) | Definition | Stipulated; source A001 |
| CC-A003-006 | Weak viability coupling scope restriction (§6.4) | Definition (scope) | Stipulated; source A003 |
| CC-A016-001 | Typed registry with tagged normative premises (§9.3) | Registry entry | Source A016 |
| CC-A002-049 | Exergy and quality-grades transformation programme (§8.4) | Declared programme | Source A002 |
| CC-A016-010 | Proposed floors, normative and unoperationalized (§9.3) | Declared programme | Source A016 |
| MS-Native-5 | Implementability ladder, `U_impl ⊆ U_inst ⊆ U_tech ⊆ U_theor`, with the parallel policy-class ladder; within-architecture viability quantifies over the implementable class (§6.1) | Definition | Programme manuscript §5.3 (repository) |
| MS-Native-7 | Typed failure taxonomy, ten classes, with the earliest-discharged-obstruction rule (§3.4) | Definitional taxonomy | Programme manuscript §24.1; module-family origin A007 §6 |
| MS-Native-8 | Conditional stage-structured and spatial extensions paper, registered with conditional prerequisites | Registration (conditional) | Programme conditional-allocation design; A022/A023 conditional docket |
| MS-Native-6 | Nine empirical conjectures, eight falsification test designs, ten candidate leading indicators, with preregistration restrictions (§11) | Declared conjectures and test designs — not executed | Programme manuscript §§27–29 |

**Table A2. Theorems, lemmas, identities, and examples.**

| Identifier | Statement | Category | Basis |
|---|---|---|---|
| MS-Native-1 | Lemma 4.2, closed-cone pointwise equivalence (§4.2) | Identity | Proved here (two lines) |
| MS-Native-2 | Theorem A, assessment hierarchy and quantifier noncommutativity (§4.3) | Theorem | Proved here; machine-witnessed |
| MS-Native-3 | Theorem B, false positives, blindness levels, disagreement, rescue, impossibility (§4.5) | Theorem | Proved here; machine-witnessed |
| MS-Native-4 | Theorem C, propagation through backward induction (§4.6) | Theorem | Proved here; machine-witnessed |
| Infra-1 | Finite-architecture robust transformation recursion (§3.3) | Theorem — typed instance of established constructions | Proved in the programme's theorem file (repository) |
| CC-A001-069 | Finite-time commons obstruction, uniform strip-margin form (§6.3) | Theorem | Proof in source A001 §12.3; summarized in §6.3 |
| CC-A001-081 | Management vocabularies are constructor rewrites (§6.2) | Theorem | Proof in source A001; summarized in §6.2 |
| CC-A001-083 | Stationary-generation equivalence (§7.2) | Theorem (immediate) | Immediate equivalence; §7.2 |
| CC-A001-084 | Nested-impossibility theorem (§7.3) | Theorem | Proof in source A001; summarized in §7.3 |
| CC-A006-010 | Conditional compositional safety across coupled subsystems (§6.4) | Conditional theorem | Stated without proof in source A006; carried at that status |
| CC-A012-009 | Effort-scale invariance (§8.1) | Theorem | Proof in source A012; §8.1 |
| CC-A018-009 | Yield-gap soft-minimum and quantified decoupling (§8.2) | Theorem | Proof in source A018; §8.2 |
| CC-A001-056 | Coupling creates viability, two-factor example (§8.3) | Example | Constructed in source A001; §8.3 |

---

## References

Aubin, J.-P. 1991. *Viability Theory*. Birkhäuser, Boston.

Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. 2011. *Viability Theory: New Directions*. Second edition. Birkhäuser, Boston.

Boos, A. 2015. Genuine savings as an indicator for "weak" sustainability. Critical survey and possible ways forward in measuring weak sustainability. *Sustainability* 7: 4146–4163.

Cinelli, M., Coles, S. R., and Kirwan, K. 2014. Analysis of the potentials of multi criteria decision analysis methods to conduct sustainability assessment. *Ecological Indicators* 46: 138–148.

Das, I., and Dennis, J. E. 1997. A closer look at drawbacks of minimizing weighted sums of objectives for Pareto set generation in multicriteria optimization problems. *Structural Optimization* 14: 63–69.

Ekins, P., Simon, S., Deutsch, L., Folke, C., and De Groot, R. 2003. A framework for the practical application of the concepts of critical natural capital and strong sustainability. *Ecological Economics* 44: 165–185.

Frankowska, H. 1989. Optimal trajectories associated with a solution of contingent Hamilton–Jacobi equations. *Applied Mathematics and Optimization* 19: 291–311.

Hanley, N., Moffatt, I., Faichney, R., and Wilson, M. 1999. Measuring sustainability: a time series of alternative indicators for Scotland. *Ecological Economics* 28: 55–73.

Lygeros, J., Tomlin, C., and Sastry, S. 1999. Controllers for reachability specifications for hybrid systems. *Automatica* 35: 349–370.

Neumayer, E. 2013. *Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms*. Fourth edition. Edward Elgar, Cheltenham.

Saint-Pierre, P. 1994. Approximation of the viability kernel. *Applied Mathematics and Optimization* 29: 187–209.

Schär, S., Pohl, E., and Geldermann, J. 2025. Analysing the compensatory properties of the outranking approach PROMETHEE. *Journal of Multi-Criteria Decision Analysis* 32: e70013.

Usubiaga-Liaño, A. 2025. Strong sustainability in the SEEA and the wider indicator debate. *One Ecosystem* 10: e141086. <https://oneecosystem.pensoft.net/article/141086>

World Bank. 2011. *The Changing Wealth of Nations: Measuring Sustainable Development in the New Millennium*. World Bank, Washington, D.C.

Programme sources. The programme-internal documents named in this paper — the source corpus (A001–A025) and the 409-row concordance (§10); the full development and proofs of the manuscript-native theorems of §4 (`research_program/paper1_typed_false_positive_theorem.md`); and their machine witness (`research_program/paper1_instantiation/`: runner, JSON results, report, and raw novelty-search records) — are committed to the project repository at <https://github.com/MIKEAA2020/general-sustainability>.

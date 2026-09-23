# Verdict — "6 parallel mechanisms.txt" (selector-framework unification)
## Evaluated against paper 2 v17 under the same sharp merit test; merited subset implemented as v18.

**Attachment content.** A qwen+GPT synthesis proposing to unify the paper's six mechanisms as failures of a single *response correspondence* `Γ(B) = ⋂_{z∈B} Γ(z)`: viability under incomplete observation = existence of a common admissible, safe, recursively viable selector. It proposes a nested ladder, a blind-window threshold σ*, a unified meta-theorem, monotonicity results, and a layered architecture, plus cautions against over-unifying.

**Verdict: the unifying claim is correct and already half-built in v17 — but several of its concrete proposals are notation without a theorem, and the attachment re-derives work v17 already did.** The merited subset was implemented as **v18**.

---

## INCLUDED in v18 (merited, implemented)

| # | Item | Why it passes |
|---|---|---|
| 1 | **Selector framing paragraph** (end of §2.4) | The attachment's central "strongest defensible claim", converted into mathematics: each certificate empties one of four response correspondences (`U^B`, `R^B_V`, `A_tube`, recursive predecessor). Replaces any residual "necessity side" flavor with a precise, defensible architecture. |
| 2 | **Obstruction-ladder proposition** (new Prop 3) | `A_tube(B,Δ) ⊆ R^B_V(B) ⊆ U^B(B)`, proved in 6 lines, with the honest converse-failure caveat (instantaneously tangent ≠ tube-safe; the gap Prop 2's uniform margin closes). Answers the single most predictable referee question: "how do your mechanisms relate?". Also silently reclassifies Prop 1 (admissibility) as the base rung — the attachment's correct observation — *without* churning the abstract. |
| 3 | **σ* threshold form of the timing obstruction** (new Remark 2) | Genuine upgrade of Theorem 3: `σ*(B_0) = sup_u inf τ` (correct `sup_u inf` quantifier order, with the observation-equivalence constraint on branches) is the *sharp* criterion `σ* < T_obs ⟹ nonviable`, of which condition (4) is the sufficient upper bound `σ* ≤ inf q/ε`. Sharpens rather than restates — this is the "elevate, don't re-derive" move the non-decorative filter rewards. |
| 4 | **Label-selector bridge** (1 sentence after Prop 4) | The fibre criterion = zero-step label-valued selector; *kept distinct* from viability (certification ≠ control), exactly as the attachment's §7/§13 caution requires. |
| 5 | **Monotonicity proposition** (new Prop 5) | Formalizes the paper's informal "certificates tighten under restriction" claim and adds the information-refinement and policy-class monotonicities — four kernel inclusions with a two-line restriction proof. Theorem-izes a design consequence. |
| 6 | **Measurable-selection scope clause** (Sec 6.5) | The attachment's correct technical caution (pointwise nonemptiness ≠ measurable selector): completeness is claimed only where backward recursion is exact (finite systems); the continuous-time certificates exhibit explicit selections, so the caveat is stated, not papered over. |

---

## EXCLUDED (not merited — documented, not lost)

| Proposal | Why it fails the test |
|---|---|
| **Unified meta-theorem** `Γ_N(B; Π, ℐ, Δ, 𝒟)` | A definition ("obstruction = checkable condition implying Γ=∅"), not a theorem. Notation-for-notation — precisely the abstraction the non-decorative filter warns against. Its content is already carried by Prop 3 + Theorem 4. |
| **`Pre_blind` blind-window predecessor** | Continuous-time predecessor machinery duplicating the σ* remark (Remark 2), which already states "the threshold is the blind-window response correspondence." Adds a definition, no result. |
| **`Γ_Π(B) = Γ(B) ∩ Π` formalism** (certainty equivalence) | The paper's Remark 3 already states it in words ("empties by restriction of the policy class, not by loss of information"). Adding a new symbol is overhead. |
| **`Λ_K(F)` label correspondence** (fibre) | Prop 4 already states the iff with the measurability clause; the label-selector *reading* was added as item 4, but the formal correspondence is redundant. |
| **Computational-tools list** (LP / MILP / reachability / games / counterexample trees) | Pointers without development. The Farkas certificate (v17) already instantiates the one computational case the paper needs; the rest belong in a companion. |
| **Layered-architecture numbering** (Layers 1–6) | Organizational; the paper's section structure (§3 obstructions vs §4 certification limits vs §6.1 institutions) already encodes it. Adding a numbered layer list would be a reader's guide. |
| **Abstract reclassification** of the "six mechanisms" count | The ladder table achieves the reclassification internally; churning the 263-word abstract for a cosmetic count change is not merited. |

---

## Confirmed already-handled (no change needed)
- **"Don't over-unify / not all epistemic"**: the paper already separates dynamic exit (Thm 1: "closes the viability question without any observation-theoretic argument"), certification (Prop 4 in §4), and policy-class restriction (Remark 3: "by restriction of the policy class, not by loss of information").
- **Finite-horizon selector theorem**: the attachment's `W_N ⟺ Γ_N(B)≠∅` is exactly v17's Theorem 4 (soundness + completeness + obstruction tree).
- **Farkas / comparison-function / uniform-margin**: already in v17 (worked example, Remark 1, Prop 2).
- **Correct quantifier order** (`sup_u inf`): the attachment uses the corrected form, consistent with the paper's (H1.1)/(H4.2).

## Verified (v18)
24 pages; 0 unresolved refs; 3 embedded figures; all objects render: Thm 1–4, Prop 1–5 (ladder = Prop 3, fibre = Prop 4, monotonicity = Prop 5), Cor 1, Remark 1–3 (σ* = Remark 2, CE trap = Remark 3); abstract 263 words; no hardcoded numbered refs; only the pre-existing 57.86pt overfull box (unchanged since v15). Pushed: v18 tex/pdf + build script.

## Net
Of the attachment's ~15 concrete proposals, **6 passed and were implemented (v18)**; 7 were excluded (duplicative, notational, or already present); 4 were confirmed already handled by v16–v17. The unifying idea — observation-based viability as the existence of a common recursively safe selector — is now explicit in the paper at the level it deserves, without the meta-theorem's notation overhead.

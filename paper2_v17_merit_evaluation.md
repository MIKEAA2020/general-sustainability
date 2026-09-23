# Merit Evaluation — Paper 2 spine & computational items
## Applied the same sharp test as the approximate-certificate verdict; only passing items were implemented (v17).

**Test (per item):** (a) genuinely new — a theorem/upgrade, not re-derivation or restatement; (b) concrete payoff, not abstraction-for-its-own-sake; (c) interesting to *this paper's* human reviewers (SVVA / JOTA / European Journal of Control / EMA) — not the wrong audience.

---

## INCLUDED in v17 (implemented)

| Item | Why it passes |
|---|---|
| **Semantic conventions** (short ¶ in §2.3) | Not a theorem, but preempts the single most likely referee question ("what is the policy class / disturbance semantics / time model?"). Costs ~8 lines; the existing Definition 1 was under-specified. |
| **Comparison-function timing bound** (Remark 1) | Genuine standard upgrade of Theorem 4's constant-ε: `D⁺q ≤ −α(q) ⟹ t_exit ≤ ∫ ds/α(s)`, with the α(0)=0 caveat. Sharper, recognizable to control referees, and matches the paper's own "decline accelerates near thresholds" framing. |
| **Uniform-margin lemma** (Proposition 2) | Fixes a real gap a set-valued referee would flag: the instantaneous tangency condition and the tube form were asserted side by side but not linked. The lemma proves `⋂R_V(x)=∅` with a uniform gap ⟹ `A_tube(B,Δ)=∅` ∀Δ>0. |
| **Finite-horizon completeness + obstruction tree** (Theorem 4, §3.5) | The one genuinely new, provable-now theorem. Answers the #1 referee objection ("are your certificates complete anywhere?"). Honest scoping: it is the standard backward recursion specialized to belief spaces, *not* claimed as deep; it upgrades §6.5's "not complete" to "not complete in general, complete in finite systems." |
| **Farkas worked example** (§3.3) | Makes the already-present "finitely checkable" claim credible with a concrete two-floor certificate (λ=(½,½), λᵀb=−0.1). Doubles as the **minimal-refinement rule** ("any observation separating x₁,x₂ restores viability"). |
| **3 schematic figures** | The paper had **zero** figures; the three concepts (fibre crossing, disjoint safe-action sets, delayed information) are geometric. Highest interest-to-effort of the whole bucket; essential for the EMA/interdisciplinary path. |

---

## EXCLUDED (not implemented — would be decorative here)

| Item | Why it fails |
|---|---|
| **σ* value-function formalism** | Pure restatement of the existing H4.2 (which already has the correct `sup_u inf` quantifier order). Adds notation, no theorem. |
| **Full g(B) margin theory** (common-action gap, time-to-violation, rescue budget) | Duplicates quantitative content the paper already has (Thm 1 exit bound, Thm 4 timing bound, Farkas multiplier). Proof burden with no new payoff for *this* paper; belongs in a companion. (The multiplier-magnitude reading is a free one-liner and was not needed.) |
| **Bare cost-minimization design problem** `min_ℐ c(ℐ) s.t. B₀∈K_ℐ` | A *formulation* without a structure theorem — exactly the "we pose it, we don't prove it" pattern the test rejects. |
| **Distance-to-viability diagnostic suite** (T_max, minimal action expansion, minimal institutional relaxation) | Definitions without theorems; only T_max=σ* is clean and it depends on the excluded σ* apparatus. §6.4 already states the timing requirement in words. |
| **A–E taxonomy restructure** | Presentation-only; the contributions list already carries the hierarchy. |
| **Separate integrated multi-layer example** | The Farkas example already delivers the refinement-removes-obstruction payoff; a second multi-layer example adds length without a result. |

---

## Consistency patches applied with the inclusions
- Abstract: "…do not exhaust the complement… **; in finite systems backward recursion is complete**" (263 words).
- §1.2 contributions: three-direction refinement sentence added.
- §1.4 organization: "Theorem 1–4, Propositions 1–2, Example 1".
- §6.1 + §6.5: finite-horizon completeness cited so the "not complete" claim is qualified, not contradicted.

## Verified (v17)
22 pages; 0 unresolved refs; 3 embedded figures; all 4 theorems / 3 propositions / 2 remarks / 1 corollary render with correct auto-numbering; abstract 263 words; only the pre-existing 57.86pt overfull box remains (unchanged since v15).

## Net
Items 1–3 (prose) → **v16.2** (done). Of the spine + computational bucket, **6 items passed and were implemented in v17**; **6 items failed and were excluded** with reasons above. The excluded items remain available as companion-paper directions but are documented as not merited for this manuscript.

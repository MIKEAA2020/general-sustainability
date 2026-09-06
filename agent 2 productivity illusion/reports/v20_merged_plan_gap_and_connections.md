# Merged-plan line-level scan + strengthening the Lens ↔ AI-top-down connections

**Scope.** (1) A deep, systematic, granular scan of every source (Lens‑1/‑4 report, the AI corrected
top‑down Parts A–E, the adjoint‑code review, the first evaluation) against the merged plan, reporting
what is captured and what remains. (2) Concrete ways to **strengthen the connections** between the Lens
and the AI top‑down. Verified numbers come from `model_sims/topdown.py` + `data/topdown_results.json`.
**No mint, no push, no manuscript edit.**

---

## 1. Granular scan — source → plan coverage

Read line‑by‑line, every distinct point in the sources maps to a merged‑plan finding **F1–F13** (see the
merged plan §2). The **substantive content is complete** — nothing from the Lens or the corrected AI
top‑down is missing from the plan. What remains are **six refinements**, not content gaps:

| ID | Point | Where it lives | Gap / action |
|---|---|---|---|
| R1 | **F2 (typed‑vs‑aggregate gap)** is a *framing*, not a newly‑computed result | plan §2 F2 | It reuses the existing manuscript §10/§13 typed‑ledger point (P3). **Action:** mark as "leverage existing result"; add only the substitution‑buffer condition `B=bA+b_G G(A)`; do **not** present as a new verified computation. |
| R2 | The **exact tables** (onset `A₀/ψ/P₀/R_B/R_A`; family‑=‑separator `P₀=B(A₀)/e`; rescue‑set `τ_g`→`%`/A‑span; silent‑collapse `%`) are referenced, not carried | plan §2 refs | **Action:** reproduce or bind the exact numbers in the plan so the implementer embeds the verified figures, not placeholders. |
| R3 | **Leading‑indicator temporal lead**: `R_A`'s lead ≈ 0 in flow‑dominated systems, grows with increment‑dominance (`1/ψ`) | Lens report §5 row 3 | Not an explicit finding (implied by F4). **Action:** add a one‑line nuance in §4.5. |
| R4 | **Metric rule**: balanced accuracy (never raw accuracy) on the imbalanced long‑lag basin | adjoint review §4 | Plan mentions balanced accuracy but not the rule. **Action:** state "never report raw accuracy on the long‑lag basin; use balanced accuracy (optionally precision/recall)." |
| R5 | **Novelty framing**: A2 (neutral‑family separator) and F5 (`R_B=1`) are *re‑framings* of R2's existing result, not new discoveries | plan §5/§2 | **Action:** say "re‑frame/strengthen," not "advance," to avoid over‑claiming novelty. |
| R6 | The **genuinely new** part of A5 is the *full‑plane* sweep (0 crossings over both delays); single‑delay no‑Hopf was already R2 | A5 | **Action:** state this specificity (the new bit is full‑delay‑plane coverage). |

**Conclusion for Q1:** the merged plan **already incorporates all** lens/AI content; only the six
refinements R1–R6 should be applied for precision and honesty. No new analysis is required.

---

## 2. Strengthening the connections (Q2)

The merged plan's "unifying spine" (`R_B=1`) is right but thin. Six explicit connections make the Lens
and the AI top‑down one argument rather than two juxtaposed ones:

### C1. `ψ` (flow share) is the **master parameter** — one knob ties the two strands together
`ψ = bA/B` is the single quantity that links:
- the **fold/MSY regime boundary** (§4.1: `b_Gρ ⋚ b`, i.e. `ψ* = 2/(1+b_Gρ/b) ⋚ 1`);
- the **masking‑illusion visibility** (prediction #5: more visible in flow‑dominated, `ψ→1`);
- the **macro‑ratio separation** `R_A = R_B/ψ` and the closed form `R_A^eq = (1+b_Gρ/b)/2`;
- the **`R_A>1` sustainable operating point** (the regeneration buffer).

→ **Add a §4.5 remark:** "the flow share `ψ` is the master parameter; it locates the regime, the masking,
and the macro‑ratio separation from one closed form."

### C2. **`R_B=1` is the coordinate‑free common fixed point** (a single theorem)
Lens‑4 bookkeeping (the trigger), Lens‑1 (the operating boundary), AI‑A2 (the basin separator), and §4.2
(the fold threshold) **all say "`E = B`" in different coordinates.** Verified at the fold:
`E = B_max → R_B = 1.000`. → **State as one theorem:** "the balance point, the basin separator, and the
`§4.2` fold threshold are the same object `E=B` (`R_B=1`)."

### C3. **Two sides of one coin: `R_B=1` works short‑lag, fails long‑lag**
The Lens macro‑ratio boundary is exactly the AI basin separator at short lag (balanced **99%**), and its
failure at long lag (balanced **81%**, **silent collapse 37%**) is precisely the AI's basin‑boundary‑crisis
/ no‑CSD finding (A5, C6). → **Add a §4.5/§13(9) link:** "`R_B=1` is *necessary* for recovery but *not
sufficient* once the regeneration lag is too long — the operating boundary (Lens) and the basin crisis
(AI) are complementary statements about one object."

### C4. **Fold ↔ `R_B=1` two‑way linkage (§4.2 ↔ §4.5)**
The interior‑MSY fold threshold of §4.2 is the `R_B=1` boundary evaluated at `(A*, E=B_max)`; conversely
the macro ratios give the fold a "balance‑point" reading. → Add as a displayed link (and note this is the
**regime‑scoped** fold, only when `b_Gρ>b` — do not re‑assert a baseline fold).

### C5. **Dimensionless‑group scoping (§4.4 ↔ A1)**
The AI's `τ_g/τ_p`‑ratio refutation connects to §4.4's "complete dimensionless group set": the **operative
group is `b_Gρ/b`** (regime), **not** `τ_g/τ_p`. → One scoping sentence in §4.4/§8.

### C6. **One canonical metric (balanced accuracy)** across both strands
Use balanced accuracy (optionally precision/recall) for the Lens *silent‑collapse* claim **and** the AI
*separator* claim, so the honesty argument is uniform. → State as the metric rule (also R4).

### C7. **A single unifying headline** for the merged v20
> "The balance point is `R_B=1` (footprint = biocapacity = the neutral family = the fold threshold); the
> flow‑yield ratio `R_A` is a **leading, non‑causal** signal whose lead grows with the flow‑share
> separation `1/ψ`; and once the regeneration lag is too long **neither** ratio forecasts collapse
> (silent collapse, measure‑zero rescue set) — the **lag**, not the ratio, is the controlling variable."

---

## 3. Concrete edits to apply to the merged plan

1. **§1 (spine)** — add **C2** theorem + **C7** headline sentence.
2. **§2 mapped‑findings table** — for F2 add "*framing*, not new computation" (R1); for A2/F5 note
   "*re‑frame/strengthen R2*, not a new advance" (R5); for A5 note "*full‑delay‑plane* coverage is the
   new bit" (R6).
3. **§4.5** — add **C1** (`ψ` master parameter) remark; add **C3** (necessary‑not‑sufficient / two sides
   of one coin); add **C4** (fold ↔ `R_B=1` two‑way link, regime‑scoped); add **R3** (temporal‑lead nuance).
4. **§4.4 / §8** — add **C5** (operative group `b_Gρ/b`, not `τ_g/τ_p`).
5. **§8 / verification** — add **R4/C6** metric rule (balanced accuracy, never raw on the long‑lag basin).
6. **§2** — carry the exact verified tables (R2) (onset, family‑=‑separator, rescue‑set, silent‑collapse).

## 4. Summary
- **Q1:** No substantive content is missing; the merged plan is complete. Apply the six refinements
  R1–R6 for precision/honesty.
- **Q2:** Strengthen via **C1–C7** — chiefly (a) `ψ` as master parameter, (b) `R_B=1` as the single
  coordinate‑free fixed point (balance point = separator = fold), (c) the "necessary short‑lag /
  insufficient long‑lag" two‑sides‑of‑one‑coin link, and (d) the balanced‑accuracy metric rule.

---
**Files:** this report (`reports/v20_merged_plan_gap_and_connections.md`) + the plan
(`reports/v20_merged_implementation_plan.md`). No mint/push/manuscript edit made.

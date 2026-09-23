# Successor Paper — v1 Addendum (disposition record)

**Version:** `successor_five_layer_v1` (standalone lineage name from birth — carries no `paperN` prefix, per the naming lesson; it cannot be mistaken for any existing series, and the suite's `paper3_material_ledgers` numbering is untouched).
**Title:** *Five Layers of Obstruction: A Successor Architecture for Viability under Incomplete Observation*.
**Implements:** Track **C3** with **D2 (general information structures)** and **D3 (exit-time value functions)** absorbed, per owner directive.

## 1. Content mapping

| Item | Where |
|---|---|
| C3 five-layer architecture (dynamic → belief-action → timing → certification → policy-class), respecting the source's over-unification warning; strongest claim only at its supported precision | §2 (the layers, each with correspondence + certificate families + source pointers), §7 (the discipline: form not cause; no ranking; the measured claim) |
| **D2 general information structures** | §3: information structures as label maps with **read-then-act per-cell semantics**; refinement monotonicity (Prop. 1); **the lattice matters** (Prop. 2): the two-patch instance — aggregate reading nonviable vs z₁-only viable on the same belief, incomparable structures, opposite verdicts; erosion quantified (28 vs 26 viable pairs — the bridge's Γ_coarse ≥ Γ_fine on the viability side); scope: beyond exogenous structures, soundness-only, matching the bridge's oracle-recourse delimitation |
| **D3 exit-time value functions** | §4: guaranteed survival time T\*(B); **level sets are kernels** ({T\* ≥ T} = 𝒲_T) — Layer 1 exit = T\* < ∞ witnessed by drift; Layer 3 timing = T\* < deadline; verified identities: hidden-regime grid σ\*(z₀) = z₀−1 with {σ\* ≥ T} = {z₀ ≥ 1+T} (48 cells); contraction instance σ\*(z₀) = max{k : z₀ ≥ (10/9)ᵏ} with level sets = the bridge's LP feasibility thresholds; HJB/Isaacs characterization cited, not redeveloped; stochastic deficit reading linked to Abaee 2026d (Remark 1) |
| Layer separation | §5 Table 1: one verified instance per boundary (L2>L1 two-floor; L3>L2 timing cells; L4>L1–3 static index; L5>L1–4 CE trap) |

## 2. Verification record (`successor_five_layer_v1_verify.py`, stdlib, exact)
**7/7 checks pass** (E1 lattice + chain + incomparability; E2 erosion counts; E3 level-set identity on 48 cells; E4 contraction-instance values at exact rational powers with LP-threshold coincidence; E5 full-information branch viability; E6 the four boundary instances).
**Development defect, documented:** the first harness draft used blind semantics (one common action per belief) for *all* structures — a recursion crash surfaced it; corrected to read-then-act **per-cell** semantics with horizon bound + stability check, and an inverted refinement predicate was fixed. Manuscript statements unchanged; harness corrected before any record was archived.

## 3. Build
Tectonic 0.15.0; `main.pdf` 111,466 B, **4 pp**, **zero Overfull \hbox** on first build; pymupdf probes 0 unresolved `??` (two apparent probe misses were extraction artifacts — stacked `\tfrac` and a hyphenation break — confirmed present after normalization).

## 4. Files
- `successor_five_layer_v1.tex` / `.pdf`; `successor_five_layer_v1_verify.py`
- `successor_five_layer_v1_source.zip` (4 entries)
- Roadmap v9 records: C3 **DONE**, D2 **DONE** (absorbed), D3 **DONE** (absorbed); remaining programme: D4–D13 as they mature.
- Open item (owner decision pending, question skipped earlier): whether to rename the three 2026 lineages currently carrying the `paper2_` prefix (`paper2_viable_selector_*`, `paper2_stochastic_selector_*`, `paper2_companion_recourse_bridge_*`) to standalone names like this paper's; no rename was performed without the decision.

## 5. Programme status
Tracks A (paper 2 v48), B (companion v1), C1–C2 (viable-selector v2), C3 (this paper), D1 (stochastic selector v1) — all drafted and verified. The successor architecture completes the roadmap's mainline; what remains is the long tail (D4–D13) and the owner's submission/venue decisions.

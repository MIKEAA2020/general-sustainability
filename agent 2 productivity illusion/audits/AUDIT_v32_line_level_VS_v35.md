# Line-Level Audit (v32) re-checked against v35 — verdict + fixes applied

**Audit object:** `AUDIT_v32_line_level.md` (retrieved from GitHub
`MIKEAA2020/general-sustainability` → `agent 2 productivity illusion/audits/`). It read the
**one-stock v32** model. The current submission is **v35 (two-land)**, which **retains the
one-stock model in the SI as a designated comparator** — so the audit's one-stock findings were
re-checked against *both* the retained SI comparator and the two-land main text.

**Method:** every A/B/C finding was grepped against
`manuscript_ECOMOD_v35.tex` + `supplementary/SUPPLEMENTARY_information_v2.md`; every load-bearing
number was re-derived (sympy determinant; ψ split; registered `topdown_results.json` recover
fractions). Verdict below.

---

## FIXES APPLIED (in `supplementary/SUPPLEMENTARY_information_v2.md`, synced to `deliverables/03_*.md`)

| Audit item | Status | Fix |
|---|---|---|
| **A6** Neubauer reference wrong title+journal | **STILL HELD** → fixed | SI ref-list entry corrected to *"Resilience and recovery of overexploited marine populations. Science, 340(6130), 347–349"* (main-text entry was already correct). |
| **A1/A5** unreproducible coarse-grid recover-fraction sequence (0.54→0.21→0.00) + mis-quoted fine sequence (0.399→0.240→0.0529) | **STILL HELD** → fixed | Replaced with the registered fine-grid values `0.399 / 0.394 / 0.240 / 0.0529` (at τ_g ≤17 / 18 / 19 / ≥20, τ_p=25); flagged the coarse variant as **non-reproducing** and superseded; stated collapse is not total (≈5% recover, rescue strip at A₀=A_max). |
| **B1** `b_G ρ ⋚ b ⟺ ψ ⋚ 1/2` | **STILL HELD** → fixed | Corrected to `ψ = 1` (marginal/boundary); noted `ψ = 1/2` requires `b_G ρ = 3b`. Verified numerically (ψ=1 at b_Gρ=b; ψ=1/2 at b_Gρ=3b). |
| **B2** `det = r·ρ·A*/A_max > 0 (never a saddle)` | **STILL HELD** → fixed | Replaced with the neutral-continuum statement: `det = 0` on the σ=1 family `P=B(A)/e`; non-neutral root `a₁₁ − r`; "det>0" flagged as a gross-harvest-comparator leftover. Verified with sympy (`det J ≡ 0` on the family). |
| **B8** `σ·B` vs `σ·bA` conflation | **STILL HELD** → fixed | Reservation is on the **flow yield**: reserve `(1−σ)bA`, `E ≤ σ·bA`; a cap on `B` is a distinct policy. |
| **B10** `r_opt`/`χ`/`Λ` undefined (in SI symbol table) | **STILL HELD** → fixed | Added `r_opt` and `χ`/`Λ` rows to the SI symbol table (χ/Λ were defined inline at §S2 but absent from the table). |

### Reviewer-response fix (`reviews/RESPONSE_to_reviewer.md` → `deliverables/00_*.md`)
| **A3** "the anchored band brackets [the cliff]"; "critical time scale … *not fitted* from the model" | **STILL HELD** → fixed | Split into: the **≈18–20 yr threshold is a model output**; the **field-anchored band (≈25–33 yr) is the lag value** (not fitted). Replaced "brackets the cliff" with "lies entirely above it". |

---

## ALREADY RESOLVED in v35 (no action)

- **F1** `b_G=0.8` vs `V=20–100 yr` turnover / `γ=1/b_G=1/V`: **gone** (0 occurrences of "salvage", "V=", "1/V", "20–100").
- **B5** `t₅₀ ≈ 145/ρ` (factor-of-20): **gone** (0 occurrences); v35 uses raw-curve fits (t₅₀≈30 yr forest, 5.6 yr fishery; τ_r≈38/3.4 yr).
- **A2** "primary forests" / forest clause: **fixed in main text** ("secondary forests"; "66–95 yr tail lies beyond the core band").
- **B3** "collapse basin ≈5%" mislabel: **fixed** (now framed as "recover fraction ≈5%", collapse not total).
- **B4** "field band entirely in collapse regime": **fixed** (main text distinguishes the raw 10–40 yr band from the effective 25–33 anchored band).
- **B6** τ_p* 231 vs 225: **only 231 remains** (consistent); no conflicting 225.
- **B7** §8 flat vs §12.2 non-monotone recover curves: **reconciled** (SI now uses the single registered four-value table; no unreconciled second curve).
- **B9** dangling internal refs (Ω=0.575, "1961–2022 sentence"): **gone** from current text.
- **F6** `b = B/A`: present but **qualified** ("definable" preceded by the identifiability argument); lower severity, left as-is (the two-term decomposition framing is deliberate).
- **C3** ABSTRACT_submission stale (v30, 300-word): **resolved** — now v35, exact 245-word match to the manuscript abstract (verified word-for-word in prior turn).

## Still open (noted, not fixed — records/package hygiene, low priority for submission)

- **C1** live symlink `data/IMPLEMENTED_revision_ECOMOD.md` stale (VERSION says revision=32). Workspace-versioning matter, not a submission-content defect.
- **C2** CHANGELOG stops at v19. Records-only.
- **C4** `demo_unified.py`/`mask_rk4.py` named as drivers but absent. The v35 reproduction guide names different drivers that **do exist**; this was a v32-era reference that no longer appears in the v35 reproduction set.

---

## Bottom line

The audit's *scientific/structural* findings (F1, B5, A2, B3, B4, B6, B7) were already resolved by the
two-land rewrite. **Six concrete residual defects still held in v35 and were fixed this turn** —
all in the retained one-stock SI comparator + reviewer response: **A6 (citation), A1/A5 (data-integrity),
B1 (ψ), B2 (det), B8 (σ), B10 (symbols)**, plus **A3** in the reviewer response. The remaining open
items (C1–C4) are records/package hygiene, not content.

*All fixes re-synced to `deliverables/`; full 8-file parity confirmed; manuscript recompiled clean
(31 pp), rebuilt PDF text-identical to the deliverable.*

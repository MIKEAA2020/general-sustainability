# v15 — Empirical follow-up implementation + cross-version diff scan

Commit `ced12e0` (origin/main). `VERSION revision=15`. Live pointer → `data/revisions/IMPLEMENTED_revision_ECOMOD_v15.md`. v1–v14 preserved.

---

## 1. Empirical follow-up (`uploads/empirical follow-up.txt`) — implemented in v15

The note raised four concerns and one calibration-feasibility question. All were addressed; additions were kept short so the revision stays ECOMOD-first.

| # | Concern | What was done in v15 |
|---|---------|----------------------|
| 1 | "Coarse grid is suggestive, not decisive" | **Fine 1-yr-step `τ_g` sweep over [15,25] at `τ_p=25`** (11 pts) and an **extended `(τ_g,τ_p)` grid** `τ_g∈{10,15,18,19,20,30}` × `τ_p∈{10,20,25,30,40}` (30 pts). Recomputes + refigured `reports/empirical_tau_g_sweep.{json,png}`, `…_tau_p_grid.{json,png}`. |
| 1 (refine) | — | The sweep **resolves the cliff as a steep *transition band* ≈18–20 yr**, not a single hard edge: recover fraction `0.399 (τ_g ≲ 17) → 0.394 (18) → 0.240 (19) → 0.053 (τ_g ≳ 20)`. R2 leading `Re λ = +0.625` constant, **no Hopf**, for every `τ_g`. |
| 2 | "50 % threshold is arbitrary" | Added **"Why 50 %"** sentence: excludes the early-transient "green shoots" onset; matches the time to meaningful biomass/stock recovery in the cited field studies (forest AGB ≈50 % at ≈20 yr; soil SOC equilibrium ≈20–23 yr). Declared a **conservative definitional threshold, not a fitted value** (the cliff is `τ_g ≳ 20` either way). |
| 3 | "`τ_p` insensitivity may mask interactions" | Added a **"Conditional on baseline parameters"** note: results hold at the baseline `(b_G, A_ref, ρ, A_max, e, r)` + documented IC grid; R1 robust to `b_G` (§13(6)); a **full global sensitivity analysis is not performed**. |
| 4 | "Figure should link the field band to the cliff" | Added an explicit **figure caption** stating *"The field-supported band lies entirely in the collapse regime for the baseline parameter set"* (and describing the fine-sweep band). |
| — | Section 2 (full calibration?) | Added a **"Calibration outlook"** paragraph: a formal calibration is **feasible but not required** for the paper's qualitative/regime claims; weak delay identifiability may not sharpen conclusions; left to **future/companion work**; plan Step 1a (per-study curve extraction) is its prerequisite and still pending. |

**Bonus correction (see §2):** reconciled the stale R2 leading-eigenvalue citation `≈ +0.59` → `≈ +0.62` (computed `+0.625` at every `A*`; the `+0.59` was left over from an earlier version), and added a short **point-estimate/interval discipline** note (frame from companion studies P3/E3) to the honesty caveat.

**Key new numbers (baseline `τ_p=25`, `A_ref=0.8, b0=0.5, bG=0.8, ρ=0.05, A_max=1.2, e=0.55, r=0.02`):**

| `τ_g` (yr) | 0–17 | 18 | 19 | 20–60 |
|:--|:--:|:--:|:--:|:--:|
| R2 leading Re λ | 0.608–0.625 | 0.625 | 0.625 | **0.625 (constant)** |
| R1 recover fraction | **0.399** | 0.394 | 0.240 | **0.0529** |

Extended-grid robustness: recover fraction = **0.399 at `τ_g=10–15`** and **0.053 at `τ_g=30`** for **every `τ_p`∈{10,20,25,30,40}**; at the transition the intermediate values move only slightly (0.399–0.394 at 18; 0.245–0.269 at 19; 0.053–0.058 at 20). So `τ_p` shifts the band by **<1 yr across a 4× range (10–40 yr)** — the cliff is **τ_g-controlled**, not a `τ_p` artefact.

**Verification run against v15 (live pointer):**
- scan `21 / 0 / 1 / 0 / 0` (covered / partial / superseded / ambiguous / missing)
- eval `R@1 0.82 / R@3 0.95` (BM25, n=22; recall-miss `12B.6`, gold score 0.074 — unchanged from v14)
- numeric verifiers `12A.3 / 12G.2 / 12G.4 / 12G.5` PASS; `12A.1 / 12G.7` SUPERSEDED (expected)
- `34` pytest pass

---

## 2. Deep sentence-level normalized diff scan (v1 → v14)

**Approach.** Two passes over all 14 immutable versions, each compared against v14's full text:
- **(a) token-set overlap** per line (flags reworded/relocated sentences); and
- **(b) content-word coverage** — the fraction of a line's *defining* content tokens (numerals, technical terms, proper nouns, minus generic stop-words) that appear somewhere in v14 — which isolates genuinely-dropped substance from harmless rewrites.

**Result: no substantive content loss from any earlier version.** v4–v13 show **zero** content-word losses; v1/v2/v3 and v6/v7 each show exactly one borderline fragment, both substantively covered in v14:
- v1–v3: the recommendation to verify R2 by "full-spectrum computation (DDE-BIFTOOL / Julia DelayDiffEq + spectral solver)" — **superseded** by the now-completed cross-checking-curve + full-spectrum computation, which v14 references explicitly.
- v6–v7: a reworded "formatting/editorial task, not an open risk" + original-model-provenance note — the provenance is stated in v14 (§13 scope note).

**The apparent "losses" on a naive token-overlap are all rewrites or deliberately-corrected phrasing**, confirmed present in v14:
- v9–v11 citation wording ("submitted / under review / in press") — correctly replaced in v10/v11 by the user-mandated **"Unpublished manuscript" / "Manuscript in preparation"**.
- The original-model χ-Hopf / "oscillation once lags are present" framing — correctly replaced by the R2 **"monotone, no-Hopf, neutral-continuum"** resolution (v8 onward).
- v13 empirical wording — **refined** in v14/v15 (not lost).
- Spot-checks of items the raw diff flagged as "missing": Brander–Taylor (1998) characterisation correction (§8), the `ρ/ν` "estimated indicator" caveat (§4.3), the full-spectrum notice (§8), the original-model provenance caveat (§13) — **all present in v14**.

**Conclusion.** No earlier-version content is worth re-incorporating: v14 (and therefore v15) is a clean substantive superset of v1–v13. The single "after correction" item surfaced was the stale R2 `≈ +0.59`, fixed in v15.

*No companion numerics, theorems, or named results were imported; all new values are ECOMOD's own sweep/grid results re-derived in the paper's `A`/`B`/`E`/`D`/`K` notation.*

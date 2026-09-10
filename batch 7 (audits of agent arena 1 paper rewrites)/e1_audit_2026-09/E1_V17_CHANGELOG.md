# E1 v16 → v17: Remaining Audit Items

**File:** `arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v17.tex`
**Compiles:** yes — `tectonic` produces `paperE1_cod_forecast_ladder_v17.pdf` (489 KB). Only cosmetic
overfull-`\hbox` warnings in the Table 9 longtable. v15 and v16 retained unmodified.

Second pass over all three audits after the v16 corrections, picking up items not previously incorporated.
Nine changes, all verified against `wave_e_cod/` data and `src/run_ladder.py`.

---

## Substantive

**1. "Unidentified modules increase error" — false as stated (qwen 1.9).** Appears in the **abstract**, the
Discussion and the Conclusion. Against each module's *declared H1 comparator* the claim fails in every case
checked:

| comparison | M2 | M3 | M3 better by |
|---|---|---|---|
| A coarse h=1 | 144 | 135 | 9 |
| A coarse h=5 | 398 | 366 | 32 |
| A annual h=1 | 160 | 154 | 6 |
| A annual h=5 | 394 | 352 | 42 |
| B h=1 | 166 | 127 | 39 |
| B h=5 | 1059 | 930 | 129 |

M3 beats M2 **six times out of six**; M1b beats M1 at h=1 on Spec A and on the fixed recovery window. The
claim is true only *against persistence*. Rewritten at all three sites to say the modules fail to close the
gap to persistence — H2, not always H1 — while stating the M3-over-M2 result openly.

**2. Table 2 said M1b estimates `C` (qwen 1.8) — it does not.** `run_ladder.py` packs `theta` as `(r, K, s)`
only; catch is always the plugged training mean (`catch_for_model`). `C` removed from M1b's free-parameter
list, matching M1's phrasing. This also repairs the §3.2 catch-file reconciliation, which depends on `C`
being plugged rather than fitted.

**3. Table 2 vs Table 10 contradicted each other on M4's parameters (qwen 1.7).** Table 10 said "no fitted
parameters"; Table 2 listed "M3". The code settles it: M4 calls the same `fit_params` as M3 and differs only
by `delay=1`. Both entries now state that `r`, `K`, `φ` are refitted exactly as for M3 and that M4 adds no
parameter of its own.

**4. Table 9's title overstated its scope (qwen 1.5).** Its Spec A rows reproduce Table 5 (annual landings),
not the frozen Table 4 (coarse). The disclosure existed in §3.5 prose but not on the table. Now annotated
directly in the caption.

**5. The freeze claim was overstated (qwen 1.6).** The abstract said the rule was "coded before the first
scoring pass and applied unchanged" while Definition 2.4 admits the tie band and comparator declarations were
recorded afterwards. Both the abstract and the Freeze-discipline paragraph now separate the pre-frozen
scoring core from the post-hoc completions, and state plainly that the rule as printed was not pre-frozen in
its entirety.

**6. HAC bandwidth and block-length sensitivity (gpt §5) — computed, not hand-waved.** GPT asked for this
before calling Specification B "decisive." Recomputed the M1-against-persistence margin over a grid:

- **DM `z` is fragile.** Spec A h=1: `1.14` (lag 0) → `2.30` (lag 3). Spec B h=1: `2.81` (lag 0) → `1.70`
  (lag 3) — it **crosses the conventional threshold** within the range of defensible bandwidths.
- **The bootstrap is stable.** Spec A `p` = 0.17–0.19 (h=1), 0.26–0.28 (h=5); Spec B `p` = 0.036–0.049 (h=1),
  0.008–0.026 (h=5), across block lengths 3–9.

The paper now reports this and states that the A-within-noise / B-separating reading is a **bootstrap** result
that survives the block choice, not a DM result. Also adds GPT's point that "within noise" means the analysis
does not resolve the difference, not that the models are equivalent.

**7. Stale-persistence control framed as descriptive (gpt §6).** The §4 decomposition now says these are
comparisons between two forecast rules, not a causal decomposition of the value of assessment timeliness —
the delayed control still reads off the same smoothed reconstruction.

**8. Floor-absorption counts labelled (qwen 6.6).** "22 of 59 and 24 of 59" → explicitly M1 and M1b.

---

## Repository repair (not a manuscript change)

**`figs_e1/` was missing from the local clone entirely** — E1 could not have compiled. All four figures
(`fig1_series`, `fig2_windows`, `fig3_rmse`, `fig4_xtencam`) recovered from the GitHub tree. This is the same
class of loss as the earlier E3/E4 figure deletion; the keep-rule again matched files *named* for a paper
rather than files a paper *references*. Now restored and pushed.

---

## Considered and not adopted

- **qwen 2.2** (Spec B decomposition mixes origin sets) — rejected in the joint evaluation; the arithmetic is
  internally consistent on mixed baselines throughout.
- **qwen 4.2, 6.1, 6.3, 6.7, 6.8; gpt §8 terminology** — these are the accessibility/de-jargoning cluster
  ("negative certificate", "observation fibre", terminology harmonisation, what "frozen" means). Deliberately
  deferred: they are a restructuring decision about what the paper claims to be, not defect fixes, and the
  three audits disagree about how far to go. Flagged as the highest-leverage remaining work if desk rejection
  was the failure mode.
- **gpt §2 profile-likelihood diagnostic for the Allee parameter** — would require new computation beyond a
  correction pass; the existing flat-valley sweep already carries the identification argument.

---

## Verification

Environments balanced, braces balanced, display math balanced, zero `\citep`, **compiles to PDF**. Numeric
claims introduced in v17 re-derived from source: the six M2/M3 comparisons, the `theta = (r, K, s)` packing,
M4's `delay=1` spec, and the full HAC-lag × block-length grid.

# E1 v37 — round-7 deferred items + data availability

**Base:** v36.

## Previously deferred items, now computed

| # | Change |
|---|---|
| **2.3** | The prey module's shortest fit is quantified. After dropping years with no carried index value, the minimum is **six** one-step transitions for three parameters (origin 1991 on Specification A, 1988 on Specification B) — worse than the seven implied by counting years, and matching the estimator's own `< 6` refusal guard. |
| **2.4** | The archived M2-against-M1b alternative-comparator rows are now **printed** on the primary passes: A h=1 +29.3 kt, z=0.91, [−67.6, +82.8]; A h=5 +109.7, z=0.98, [−77.1, +232.8]; B h=1 +14.4, z=0.51, [−67.5, +89.1]; B h=5 +613.4, z=1.93, [+170.9, +945.1]. All sixteen values machine-checked against the archive. |
| **2.6** | **Computed, not asserted.** Recomputing the log-RMSE column with the floor lowered to 1e−6 and 1e−9 leaves the ordering of the five modules unchanged at both horizons on both specifications. So no secondary ranking depends on the floor either — the paper previously stated this only for the retention score. |

## Data availability

Reduced from **359 words to 17**, as two links: the GitHub repository and the Zenodo
record `https://zenodo.org/records/22553609`.

**The section was not simply cut.** It mixed a pointer list with a substantive
reproducibility disclosure that appears **nowhere else in the manuscript** — the 29/29
checksum and 30/30 regeneration record, and the M1b environment-sensitivity note (h=1:
151.6 versus 153.2 kt; h=5: 445.5 versus 462.5 kt). Deleting it would have removed a
caveat that qualifies a printed result. It is relocated to a new **Reproducibility**
subsection, with the M1b note now cross-referenced to the identification fragility
reported in Section 3.1. The per-source citation list is dropped: DFO (2016), Regular et
al. (2025), Schijns et al. (2021) and Murphy et al. (2025) are all in the bibliography,
so the pointers were redundant.

## Gates

Compile clean; register 0/0; content guard **0 blockers**, 9 warnings; self-test 5/5;
title and `\thanks` byte-identical. `\url{}` verified safe — `hyperref` is loaded at
line 19.

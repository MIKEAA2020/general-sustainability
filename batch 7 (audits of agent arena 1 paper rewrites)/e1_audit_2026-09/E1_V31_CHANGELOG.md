# E1 v31 — round-5 correction pass

**Base:** v30. Corrections only. Every item below was verified by grepping the compiled
manuscript, not by consulting the evaluation document — the round-5 audit found four
round-4 items marked "accepted" that had never been applied.

## Tier 1

| # | Change |
|---|---|
| **G1** | **Allee/K bounds table.** v30 stated the scored `𝔰` bound as `[0, 81.10]` kt. The estimator uses `np.max(S0)` over **predictor** states, so the recovery-window bound is **40.83 kt** (twelve transitions, 1995–2006), not the 81.10 kt terminal 2007 state. `𝔰 = 50` kt is therefore **outside** the scored range, and v30's "a high threshold was not excluded" is withdrawn. Replaced with an explicit three-row bounds table separating `K`, the scored `𝔰`, and the profile `𝔰`. |
| **G2** | **Acoustic-index eligibility corrected.** Specification B is scored from **1988**, with three pre-break origins (`n=36/32`); Specification A from 1991 (`n=24/20`). Verified against `capelin_index_forecasts.csv`. The carry-forward resets at 1991 only when the last observation predates the break, which the previous description misstated. |
| **G3** | **Secondary scores matched.** Specification B persistence Brier was `0.06 = 4/63` — the unmatched baseline. On matched origins it is **4/59 = 0.07** at h=1 and **16/55 = 0.29** at h=5; both are now reported with counts and denominators, and the "M1 and M3 improve over 0.06" comparison is corrected to 0.07. |
| **G4** | **Introduction no longer asserts the structural bar** that Section 4 qualifies; the "scored test measures how severely that bar penalizes" sentence is deleted. |
| **G9** | **The two collapse experiments are separated.** Fixed-origin (pre-collapse fit, all models miss) and rolling-origin within 1991–1995 (some models win, n=5) answer different questions; the text now says so, including that a one-step forecast issued in 1993 from an already-collapsed state is not evidence a model predicted the collapse. A direct mechanism for the fixed-origin failure — stationary production plus the 1992 catch drop turns the models upward where the reconstruction turns down — replaces the "finite-sample face" link to Proposition 4.1. |

## Round-4 items accepted but never applied to v30 (now applied)

- **F15** event-type attribution replaced with "neither prescribed catch treatment reproduced the reconstructed decline; which process accounts for the shortfall is not identified."
- **F16** the "value of a timely assessment exceeds any structure tested" claim deleted; the arithmetic is kept as differences between forecast rules on a smoothed reconstruction.
- **F20** the theorem-penalty sentence deleted.
- **F21** "retention rule, coded before" → "retention rule whose **scoring core** was coded before".

## Tier 2

- **G5** orphan reference to "the 88 of Table 7" repointed to the Table 6 caption, where that value now lives.
- **G6** Table 8 bolds the **origin-matched** baseline (97/193, 79/288); mixed-origin rows are labelled and demoted to reference.
- **G7** sign-hit range restated as structural modules only, with NA for the baselines.
- **G15** "r, K, 𝔰 and C can compensate" → C is plugged for M1b; the profile re-optimises only r and K.

## Verification

Per the standing instruction, after every edit touching a number or table cell the whole
document was grepped for that value: `81.10, 40.83, 50.83, 9.68, 4/59, 16/55, 4/63,
16/59, 0.06, 0.07, 0.27, 0.29, 98, 265, 97, 193, 88, 318, 79, 288, 86.4, 11.1, 1988`.
Two surviving `81.10` occurrences were checked and are correct (the real 2007 SSB, and the
explicit contrast in the new bounds paragraph); the surviving `0.06`/`0.27` are the
labelled unmatched values and an unrelated bootstrap p-range.

A 16-point removed/present check was run against the compiled `.tex`: 9 items confirmed
**removed**, 7 confirmed **present**. Gates: compile clean, register 0/0, guard **0
blockers** (6 warnings), self-test 5/5, title and thanks byte-identical, abstract 250/250,
highlights ≤85.

## Not done

Primary-pass per-origin uncertainty and the two-regime capelin specification remain
delegated: both need a rerun that archives forecasts never written out, not a revision.

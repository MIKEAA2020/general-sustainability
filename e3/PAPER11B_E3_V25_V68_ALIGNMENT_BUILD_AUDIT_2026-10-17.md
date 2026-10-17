# E3 v25 → v26 alignment with Paper11 v68 and build audit

**Date:** 2026-10-17  
**Disposition:** E3 v26 and SI v4 were pushed to the established E3 filenames on `edwards-framework-e1-audit-implementation` and their remote bytes were verified. The preceding E3 v25/SI v3 files are preserved unchanged. This audit extends, and does not replace, the historical v24/SI v2 versus Paper11 v67/SI S15–S22 comparison.

## 1. Lineage and source basis

The dated crosswalk `PAPER11B_E3_V24_V67_CLAIM_CROSSWALK_2026-10-16.md` remains the record of the requested comparison: standalone E3 v24/SI v2 against the Edwards material in Paper11 v67/SI S15–S22. It also records why the standalone E3 line, recovered Paper11b line, and later merged Paper11 line are distinct; it is not replaced or silently rewritten here.

The 2026-10-17 base scan found:

- E3 v25/SI v3 on `edwards-framework-e1-audit-implementation`, branch tip `9f3a3842795df6bc34db379d797c46b01c8948f1` before this addition. The main and SI sources matched their remote blobs: `3b9380c6c35ec077c5943e47303fdf4ea2950bc2` and `5d9e3362a5fbecf5a2f5b37ff3b60c9f220ec52c`.
- Paper11 v68 main/SI on `main`, branch tip `1ba3d3c8a286a055b1342b5102731b601ec3d428`. Sources matched remote blobs `8908b04a28a988068a8f49a6f56c959adfcd8723` and `40045ff13a89b42f9ae645c73dfe486bf156f9a2`.
- Paper11 v68's expanded verifier recorded 237/237 checks passing. The current E3 build makes no claim that it reruns the archived forecasting pipeline.

The five E3 figure assets used in the build byte-match `e3/figs/` on the E3 branch: `edw_fig1_series.png` (`2a561e11597977c8697da3e4758c7f93fd6069c5`), `edw_fig2_windows.png` (`d98227cb30ad14db1b58567abb77dc876488aa73`), `edw_fig3_rmse.png` (`6c9603dd7c36499866fea8aff556506315d2c8d0`), `edw_fig4_pass2.png` (`09dc27de0700304130de2b560359389609d6fa25`), and `edw_fig5_fibre.png` (`3cf4fc675f22390bd098dbf87c93c25d7782cf3f`).

## 2. Targeted Paper11 v67 → v68 Edwards comparison

The comparison was limited to the Edwards portions and the changes that affect their interpretation; Paper11 v68's new cod operating-characteristic simulation is not imported into E3 and no cod/aquifer scores are pooled.

| Change in Paper11 v68 relative to v67 | E3 v26 / SI v4 disposition |
|---|---|
| The protocol account now names the H1/H2 point gates and distinguishes them from the broader M2m function-class clause. Pass 2 names persistence and M1; three climate variants pass that point gate and are later class-demoted, while using M2m as the alternative comparator yields no point passes. | Main text and SI state the H1/H2 gate, M2m class restriction, Pass-2 comparator, three point passes, and class demotion separately. They do not describe class demotion as a score-gate failure or retrofit uncertainty/five-year performance as a gate. |
| v67 used “nowcast” for the realized-future-flux result. v68 calls it an ex-post conditional diagnostic using target-year inputs unavailable at the origin. | E3 v26/SI v4 use conditional diagnostic/hindcast wording and exclude it from forecast retention. No “nowcast” claim remains. |
| The v68 Edwards mechanism discussion changes “near-white” to low-persistence language and cautions that the half-autocorrelation heuristic is not an exact numerical prediction for the fitted map, which has a state-dependent drain and a nonzero residual cross-term. | E3 v26 uses descriptive correlations (recharge lag-one 0.17; increment/same-year recharge 0.74; increment/previous-year recharge 0.06), without calling recharge white noise or applying the heuristic as an exact prediction. Its single-system identity is bounded to the fitted mechanism and observed origins. |
| The v68 rolling audit adds an exact 75-origin attribution: substitution term +76.028642 ft²; residual cross-term −27.490666 ft²; raw M2–persistence MSE gap +48.537976 ft²; after clipping, +40.988957 ft². | The rounded attribution is added to E3 v26 main text; SI v4 gives the precise values, distinguishes unclipped identity from clipped scoring, and points to the v68 Edwards audit script/outputs. It is explicitly not presented as a fresh E3 pipeline rerun. |
| v68 main/SI specifies the `[610,710]` ft output bound, emitted fixed-window values, the 1959 lower-floor binding, and the 1992 rolling upper clip. The v67 SI path printed `606.8 → 605.3 → 605.3` while describing clip binding, leaving raw proposals versus emitted forecasts ambiguous. | SI v4 labels both sequences: raw proposals `617.1 → 611.6 → 606.8 → 605.3 → 605.3`; clipped emissions `617.1 → 611.6 → 610 → 610 → 610`. It says the floor first binds for target 1959 and records the sole rolling h=1 hit as the 1992 upper clip, raw 719.1027 ft → 710 ft, with no lower clip. |
| The Comal paragraph no longer says its ranking “must” mirror J-17 under a linear transform; it calls the ordering broadly similar, not mathematically guaranteed. Pumpage scenarios are called illustrative simulations, not forecasts/policy estimates. The five-year result is record-specific, not a general planning rule. | E3 SI v4 likewise avoids the algebraic-necessity claim, labels scenario outputs non-forecast/non-policy estimates, and the main text limits five-year conclusions to this record and protocol. No management recommendation is made. |
| v68's added cod simulations and cross-system elaborations are outside the standalone aquifer scope. | E3 remains a one-system paper: no cod result, cross-system pooled statement, or transfer of cod conclusions is added. |

## 3. SI v3 defect and v4 correction

The published `supplement_v3.tex` was byte-matched to the remote v3 source and left unchanged. Its build fails at the longtable with `LaTeX Error: No counter 'none' defined.`, caused by `\def\LTcaptype{none}`. SI v4 removes that invalid longtable caption-type override and builds successfully. The fix is therefore a new SI version, not an overwrite of v3.

## 4. Build, static checks, and visual inspection

Built separately from the candidate source using official Tectonic 0.15.0 GNU x86_64, SHA-256 `f0b36e78c13dd75b821984830533f872c9a12c62957e51357bc16e65cdb71013`.

- Main source: 33,307 bytes; SHA-256 `482eb6b9b5a79b5e10beaaf6aab57864e3b2f83052bafca64c40ec6553965f25`.
- Main PDF: 10 pages, 270,335 bytes; SHA-256 `57dca5f056b3131e652441645b88c553de4ee52543b465c9ddf89b0ccf3131b5`; 4,392 extracted words, 26 annotations, no blank pages.
- SI source: 26,758 bytes; SHA-256 `a3d496a86cbcd23bf25d29593259639031b29d4fac7926762de8fe5e5b2bb0ef`.
- SI PDF: 8 pages, 348,186 bytes; SHA-256 `d80da9d30dec345a28175236e240cc23d2b2478fd7e4205088845029a1f7b09c`; 3,655 extracted words, 5 annotations, no blank pages.
- Static checks: one document class/body per file; 7 main labels and 15 SI labels, no duplicate labels or unresolved internal references; all referenced figures exist. Final TeX logs contain no LaTeX errors, unresolved references/citations, or overfull boxes.
- Remaining warnings are underfull only: main badness 10,000 at lines 239–240 and 1,688 at 259–260; SI badness 1,412 at lines 155–156.
- All 10 main pages and all 8 SI pages were rendered and visually inspected. The tables, figures, clip paragraph, new rolling attribution, references, and declarations show no clipping, collision, blank page, or float overflow. The Article Impact Statement now remains on the title/abstract page.

## 5. Version and disposition

E3 v26/SI v4 are based on the latest standalone E3 v25/SI v3 and current Paper11 v68 sources, not on Paper11b v2 or the historical v64 merged draft. The all-ref audit found no pre-existing E3 v26 or SI v4. The old E3 v25 and SI v3 are preserved. The target follows the current E3 filename lineage and branch: `e3/paperE3_edwards_forecast_ladder_v26.tex` / `.pdf` and `e3/paperE3_supplement_v4.tex` / `.pdf`, plus the dated audit notes, on `edwards-framework-e1-audit-implementation`.

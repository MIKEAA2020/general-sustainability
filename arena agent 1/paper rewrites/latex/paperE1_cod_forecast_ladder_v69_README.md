# Paper E1 v69 — assembly and compilation

**Edition note (numbering across branches).** This edition descends from `paperE1_cod_forecast_ladder_v59.tex` (`main`, `arena agent 1/paper rewrites/latex/`) and carries the two additions of the branch copy `paperE1_cod_forecast_ladder_v60.tex` (branches `e2-v3-source-year` and `lean-audit-v4`): the *Code availability* subsection and the extended generative-AI declaration. The branch `edwards-framework-e1-audit-implementation` holds a *parallel* E1 line in `e1/` (`paperE1_cod_forecast_ladder_v49` … `v68_submission`, 17–22 Sep 2026, a different manuscript titled “Does Structural Elaboration Improve Biomass Forecasts? …”). Nothing from that line is merged here; the number **v69** is used only so that no version number is reused anywhere in the repository (the earlier working label of this edition was v61).

## Repository layout (pushed 2026-10-15)
* `arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v69.tex` / `.pdf`, `paperE1_cod_forecast_ladder_v69_SI.tex` / `.pdf`, `paperE1_cod_forecast_ladder_v69_verification.py` (run from that folder: it reads `paperE1_calibration_data_v1_wave_e_cod/` and `paperE1_calibration_data_v1_ram_timeseries.csv` there) — flat, next to v59 (`main`) / v60 (branches).
* `arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v69_README.md` (this file), `paperE1_cod_forecast_ladder_v69_CHANGELOG_v59_v60_to_v69.md`, `paperE1_cod_forecast_ladder_v69_highlights.md`, `COVER_LETTER_paperE1_cod_forecast_ladder_FR_v69.md`.
* `arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v69_src/` — `parts/`, `si_parts/` (+ `gen/` tables), `figs/`, `assemble_si.py`, `work/` (new-quantity scripts and their CSV outputs, plus `work/rerun/` = data, pipeline copy and regenerated results; the scripts locate the repository root through `GS_REPO` or their standard nesting depth).
* The `.tex` files search `figs/` and `paperE1_cod_forecast_ladder_v69_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder.

Deliverables
* `paperE1_cod_forecast_ladder_v69.tex` / `.pdf` — main article (elsarticle, preprint 11pt, author-year; 33 pp.; 9 tables, 6 figures, Proposition 1 with proof in Appendix A)
* `paperE1_cod_forecast_ladder_v69_SI.tex` / `.pdf` — Supplementary Information S1–S14 (19 pp.; 17 tables, 3 figures)
* `paperE1_cod_forecast_ladder_v69_verification.py` — standard-library verification (76 checks; run from a directory containing the two .tex files, `paperE1_calibration_data_v1_wave_e_cod/` and `paperE1_calibration_data_v1_ram_timeseries.csv`, i.e. the repo's `arena agent 1/paper rewrites/latex/`)
* `CHANGELOG_v59_v60_to_v69.md`, `HIGHLIGHTS_v69.md`, `COVER_LETTER_paperE1_v69_FR.md`

Assembly (the .tex files are concatenations of the parts; edit the parts, then re-assemble):

    cat parts/0*.tex > paperE1_cod_forecast_ladder_v69.tex
    python3 assemble_si.py            # concatenates si_parts/si_0*.tex and inlines si_parts/gen/*.tex
    tectonic paperE1_cod_forecast_ladder_v69.tex          # or pdflatex ×2
    tectonic paperE1_cod_forecast_ladder_v69_SI.tex

Parts: `00_front` (preamble, title, abstract, keywords) · `01_intro` (§1) · `02_data` (§2) · `03_methods` (§3) · `04_results` (§4) · `05_discussion` (§5) · `06_conclusions` (§6) · `07_back` (Appendix A proof, declarations, data availability, references).
SI parts: `si_00_front` (preamble, S-numbering, abstract/contents) · `si_01_s1_s4` · `si_02_s5_s9` · `si_03_s11_s14` (S10–S14). Generated table bodies in `si_parts/gen/` (written by the scripts in `work/`).

Figures (`figs/`, PDF + PNG, all from `work/make_figures.py`): fig1_series · fig2_gaps · fig3_windows · fig4_period · fig5_production · fig6_operating · figS1_allee_profile · figS2_vintages · figS3_windows_annual.

Analysis scripts (`work/`; all read the archived per-origin result files and call the unmodified runner functions in `work/rerun/src/`): `paired_bootstrap.py` (shared-index paired MBB, pooled + per band → `paired_bootstrap_pooled.csv`, `paired_bootstrap_bands.csv`), `block_grid.py` (`block_grid.csv`), `post1995.py` (`post1995_margins.csv`), `catch_timing_sensitivity.py` (`catch_timing_sensitivity.csv`), `rolling_params_B.csv` (Specification B rolling parameter record), `make_figures.py`. `work/rerun/` holds a copy of `wave_e_cod/src` + data with the regenerated `results/` (third-environment re-execution: Python 3.13.16, numpy 2.3.5, scipy 1.17.1).

Requirements: a TeX distribution with elsarticle, amsmath/amsthm, booktabs, tabularx, enumitem, placeins, hyperref, graphicx (tectonic fetches them automatically); Python 3 + numpy + scipy + pandas + matplotlib only to regenerate the figures and the new tables.

Numbers policy: every main-text table value is the archived runner's value (`wave_e_cod/results/`, `batch 7 … /results/e1_dm_uncertainty_regime.csv`, `e1_audit_2026-09/`). The catch-timing correction (SI S14) is reported as a sensitivity and is not applied to the archived tables.

# paper11 v67 — assembly, compilation and verification

**Lineage.** `paper11_forecasting_baselines_v66.tex` (`e2-v3-source-year`, `arena agent 1/agent workspace/papers/`) → v67, with the cod half descending from `paperE1_cod_forecast_ladder_v69` (`main`, `arena agent 1/paper rewrites/latex/`, now in `superseded/`). See `paper11_forecasting_baselines_v67_CHANGELOG_v66_to_v67.md`.

## Deliverables
* `paper11_forecasting_baselines_v67.tex` / `.pdf` — main article (elsarticle, preprint 11pt, author-year; 49 pp.; 10 tables, 8 figures; Definitions 1–2, Propositions 1–2, Remarks 1–2, proofs in Appendix A; 60 references)
* `paper11_forecasting_baselines_v67_supplementary.tex` / `.pdf` — Supplementary Information S1–S24 (35 pp.; 25 tables, 7 figures): Part A cod S1–S14, Part B Edwards J-17 S15–S22, Part C cross-system S23–S24
* `paper11_forecasting_baselines_v67_verification.py` — standard-library verification (139 checks); run from a directory containing the two `.tex` files and either `work/` or `paper11_forecasting_baselines_v67_src/work/`; output archived as `paper11_forecasting_baselines_v67_verification_output.txt`
* `paper11_forecasting_baselines_v67_CHANGELOG_v66_to_v67.md`, `paper11_forecasting_baselines_v67_highlights.md`, `COVER_LETTER_paper11_v67_EMS.md`

## Source folder `paper11_forecasting_baselines_v67_src/`
* `parts/00_front.tex … 07_back.tex` — the main text in eight parts; `cat parts/0*.tex > paper11_forecasting_baselines_v67.tex`
* `si_parts/si_00_front.tex … si_05_s23_s24.tex` + `si_parts/gen/*.tex` (generated table bodies) — `python3 assemble_si.py` concatenates the parts, inlines the generated tables and writes `paper11_forecasting_baselines_v67_supplementary.tex`
* `figs/` — all figures (cod `fig1`–`fig6`, `figS1`–`figS3`; Edwards `edw_fig1_series`–`edw_fig5_fibre`; `fig7_mechanism` = main-text Fig. 8)
* `work/make_fig_mechanism.py` — Fig. 8; `work/horizon_profile.py` → `si_parts/gen/tabS23_*.tex` and `work/horizon_profile.json` (SI S23)
* `work/edw/data/annual_panel.csv` (registered twenty-column panel) and `work/edw/results/` — copies of `comp/wave_e_edwards/` result files read by the verifier; raw inputs and runner scripts remain at `comp/wave_e_edwards/{data,src}` (e2-v3-source-year) and `wave_e_edwards/` (main)
* `work/cod/` — the new-quantity scripts of the cod edition (`paired_bootstrap.py`, `post1995.py`, `catch_timing_sensitivity.py`, `block_grid.py`, `make_figures.py`) with their CSV outputs, and `work/cod/rerun/{data,results,src}` (registered cod data files, third-environment re-execution outputs, runner copies)

## Compilation
Both `.tex` files search `./`, `figs/` and `paper11_forecasting_baselines_v67_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder. Compiled with Tectonic 0.15.0 (XeTeX engine); one `tectonic <file>.tex` run per document suffices (two passes are run internally). No overfull box exceeds 12 pt in the main text; the SI has two inherited boxes under 10 pt.

## Rule of this edition
No forecast runner was re-executed and no archived score changed. New computations: SI S23 horizon profiles and autocorrelations, Fig. 8. The cross-system reading of v66 ("weakly autocorrelated surplus production") is withdrawn with the computed values (0.71–0.91); the verifier asserts the retraction.

# Paper 1 v64 — assembly and compilation

## Repository layout (pushed 2026-10-15)
* `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v64.tex` / `.pdf` and `paper1_assessment_separation_v64_supplementary.tex` / `.pdf` — flat, next to v60–v62 (`main`) / v63 (branches `e2-v3-source-year`, `lean-audit-v4`). Local working names were `manuscript_paper1_v64*`.
* `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v64_README.md` (this file), `paper1_assessment_separation_v64_CHANGELOG_v62_to_v64.md`, `paper1_assessment_separation_v64_highlights.md`, `COVER_LETTER_paper1_assessment_separation_JMCDA_v64.md`.
* `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v64_src/` — `parts/`, `figs/`, `work/make_fig_geometry.py`, `work/make_fig_ladder.py`.
* The `.tex` files search `figs/` and `paper1_assessment_separation_v64_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder.

Deliverables
* `manuscript_paper1_v64.tex` / `.pdf` — main article (elsarticle, preprint 11pt, author-year; 40 pp.)
* `manuscript_paper1_v64_supplementary.tex` / `.pdf` — Supplementary Information S1–S9 (30 pp.)
* `CHANGELOG_v62_to_v64.md`, `HIGHLIGHTS_v64.md`, `COVER_LETTER_paper1_v64_JMCDA.md`

Assembly (the .tex files are concatenations of the parts; edit the parts, then re-assemble):
    cat parts/0*.tex  > manuscript_paper1_v64.tex
    cat parts/si_0*.tex > manuscript_paper1_v64_supplementary.tex
    tectonic -X compile manuscript_paper1_v64.tex            # or pdflatex ×2
    tectonic -X compile manuscript_paper1_v64_supplementary.tex

Parts: 00_front (preamble, abstract, §1) · 01_setting (§2) · 02_general (§3) · 03_witness (§4) · 04_benchmark (§5) · 05_discussion (§6–§7) · 06_appendix (A–B) · 07_refs (declarations, bibliography) · si_00 … si_03.

Figures (`figs/`): fig_finite_menu_geometry (new; `work/make_fig_geometry.py`), fig_witness_triangle (= v62 fig1_witness_v40), fig_path_view (= v62 fig3_path_view_v31), fig_substitutability_ladder (new; `work/make_fig_ladder.py`), fig_benchmark (= v62 fig_benchmark_v44), figS_weight_intervals (= v62 fig2_weight_intervals_v35, SI only).

Requirements: a TeX distribution with elsarticle, amsmath/amsthm, booktabs, tabularx, enumitem, hyperref, graphicx (tectonic fetches them automatically); Python 3 + numpy + matplotlib only to regenerate the two new figures.

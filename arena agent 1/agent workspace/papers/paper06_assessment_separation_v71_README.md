# paper06_assessment_separation_v71 — assembly and compilation

Lineage: paper1 v62/v63 → paper06 v64…v70 (`arena agent 1/agent workspace/papers/`, branch `e2-v3-source-year`) → **v71** (this edition). The 2026-10-15 research-article rewrite `paper rewrites/latex/paper1_assessment_separation_v64*` was built on the stale v63 base; it is superseded by v71 and kept only under `paper rewrites/latex/superseded/`. See `CHANGELOG_v70_to_v71.md`.

## Repository layout
* `arena agent 1/agent workspace/papers/paper06_assessment_separation_v71.tex` / `.pdf` and `paper06_assessment_separation_v71_supplementary.tex` / `.pdf` — flat, next to v70.
* `…/papers/paper06_assessment_separation_v71_README.md` (this file), `paper06_assessment_separation_v71_CHANGELOG_v70_to_v71.md`, `paper06_assessment_separation_v71_highlights.md`, `COVER_LETTER_paper06_assessment_separation_JMCDA_v71.md`.
* `…/papers/paper06_assessment_separation_v71_src/` — `parts/`, `figs/`, `work/make_fig_geometry.py`, `work/make_fig_ladder.py`.
* The `.tex` files search `figs/` and `paper06_assessment_separation_v71_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder.

## Deliverables
* `paper06_assessment_separation_v71.tex` / `.pdf` — main article (elsarticle, preprint 11pt, author-year; 47 pp.)
* `paper06_assessment_separation_v71_supplementary.tex` / `.pdf` — Supplementary Information S1–S9 (39 pp.)
* `CHANGELOG_v70_to_v71.md`, `HIGHLIGHTS_v71.md`, `COVER_LETTER_paper06_v71_JMCDA.md`

## Assembly (the .tex files are concatenations of the parts; edit the parts, then re-assemble)
    cat parts/00_front.tex parts/01_setting.tex parts/02_general.tex parts/03_witness.tex \
        parts/04_benchmark.tex parts/04b_related.tex parts/05_discussion.tex \
        parts/06_appendix.tex parts/07_refs.tex > paper06_assessment_separation_v71.tex
    cat parts/si_0*.tex > paper06_assessment_separation_v71_supplementary.tex
    tectonic paper06_assessment_separation_v71.tex                 # or pdflatex ×2
    tectonic paper06_assessment_separation_v71_supplementary.tex

Parts: 00_front (preamble, abstract, §1) · 01_setting (§2) · 02_general (§3, incl. Lemma 3 and Remark 1) · 03_witness (§4) · 04_benchmark (§5) · 04b_related (§6 related work and claims) · 05_discussion (§7–§8) · 06_appendix (A–B) · 07_refs (declarations, bibliography) · si_00 … si_03 (S1–S9).

Figures (`figs/`): fig_finite_menu_geometry (`work/make_fig_geometry.py`), fig_witness_triangle, fig_path_view, fig_substitutability_ladder (`work/make_fig_ladder.py`), fig_benchmark, figS_weight_intervals — unchanged from v64 (no figure carries a result number that changed).

Requirements: a TeX distribution with elsarticle, amsmath/amsthm, booktabs, tabularx, enumitem, hyperref, graphicx (tectonic fetches them automatically); Python 3 + numpy + matplotlib only to regenerate the two generated figures.

## Verification
Exact-arithmetic verifiers (grid 25, benchmark 24, ladder 57, off-diagonal 50, continuum 44, common shock 77) and the Lean 4 module are unchanged from the report editions; v71 adds no new numerical claim (the two constants corrected in SI S3.4 — the harmonic-circle diagonal point φ and the θ = 2/3 flip total 2√(6√3 − 9) — are closed-form identities checked by hand in the text).

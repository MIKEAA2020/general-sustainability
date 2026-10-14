# Paper 01 v73 — Obstruction certificates for viability under incomplete observation

## Repository layout (pushed 2026-10-15)
* `arena agent 1/agent workspace/paper 2 family/01_obstruction/paper01_obstruction_calculus_v73.tex` / `.pdf` and `paper01_obstruction_calculus_v73_supplementary.tex` / `.pdf` — flat, next to v64–v72 (branch `e2-v3-source-year`; the same files are pushed to `main`).
* `.../01_obstruction/paper01_v73_verification.py` (30 exact-arithmetic checks; finds the Lean source in `paper01_obstruction_calculus_v73_src/code/`), `paper01_obstruction_calculus_v73_README.md` (this file), `paper01_obstruction_calculus_v73_CHANGELOG_v72_to_v73.md`, `paper01_obstruction_calculus_v73_HIGHLIGHTS.md`, `COVER_LETTER_paper01_obstruction_calculus_SVVA_v73.md`.
* `.../01_obstruction/paper01_obstruction_calculus_v73_src/` — `parts/`, `si_parts/`, `figs/` (11 PNG), `code/` (`P1_Obstruction.lean`, `counterexamples.py`, `coverage_v70.py`, `COVERAGE_RUN.md`, `LEAN_PROVENANCE.md` — verbatim copies of the branch files, see `code/` provenance below — and `make_figures_v73.py`).
* The `.tex` files resolve `figs/...` through `\graphicspath{{./}{paper01_obstruction_calculus_v73_src/}}`, so they compile unchanged in the repository folder and in a flat working folder.

## Deliverables
| File | Content |
|---|---|
| `paper01_obstruction_calculus_v73.pdf` / `.tex` | main article, 28 pp (assembled from `parts/0*.tex parts/1*.tex`) |
| `paper01_obstruction_calculus_v73_supplementary.pdf` / `.tex` | Supplementary Material S1–S9, 23 pp (assembled from `si_parts/0*.tex`) |
| `paper01_v73_verification.py` | exact-arithmetic verification record V1–V12 (30 checks) — `python3 paper01_v73_verification.py` |
| `code/P1_Obstruction.lean`, `code/LEAN_PROVENANCE.md` | Lean 4 development of the finite core (unchanged from v72) and its provenance note |
| `code/counterexamples.py` | control-affine recourse counterexample, support-only stochastic witness |
| `code/coverage_v70.py`, `code/COVERAGE_RUN.md` | the discrete coverage runner (48-cell hold-class audit) |
| `code/make_figures_v73.py` | regenerates the four v73 figures into `figs/` |
| `figs/` | all figures (5 main, 4 supplementary) |
| `CHANGELOG_v72_to_v73.md`, `HIGHLIGHTS_v73.md`, `COVER_LETTER_p01_v73_SVVA.md` | edition notes, highlights, cover letter |

## Build
```
cat parts/0*.tex parts/1*.tex > paper01_obstruction_calculus_v73.tex
tectonic paper01_obstruction_calculus_v73.tex
cat si_parts/0*.tex > paper01_obstruction_calculus_v73_supplementary.tex
tectonic paper01_obstruction_calculus_v73_supplementary.tex
```
Figures carry theorem numbers (Thm 4.1, Prop 4.2, Prop 4.5, Thm 4.6, Thm 4.10, Prop 4.12, Thm 3.1, Prop 5.2); if a numbered environment is inserted before them in §3–§5, edit `code/make_figures_v73.py` and rerun it.

## Numbering
Edition v73 because v72 was the latest Paper01 on **any** branch of the repository (`e2-v3-source-year`). Nothing has been pushed.

## Repository placement (suggested)
`arena agent 1/agent workspace/paper 2 family/01_obstruction/v73/` next to the v72 folder, with `src/` (the v72 inputs used here) omitted.

# ECOMOD v42 — research-article rewrite of `manuscript_ECOMOD_v41.tex`

## Repository layout (pushed 2026-10-15)
* `agent 2 productivity illusion/manuscript_ECOMOD_v42.tex` / `.pdf` and `manuscript_ECOMOD_v42_supplementary.tex` / `.pdf` — flat, next to `manuscript_ECOMOD_v41.*`.
* `agent 2 productivity illusion/manuscript_ECOMOD_v42_README.md` (this file), `manuscript_ECOMOD_v42_CHANGELOG_v41_to_v42.md`, `manuscript_ECOMOD_v42_HIGHLIGHTS.md`.
* `agent 2 productivity illusion/manuscript_ECOMOD_v42_src/` — `parts/`, `figures/` (SI comparator figures), the three main-text figure files, `assemble.py`, `make_fig_model.py`, `drawdown_depth.py`, `si_drawdown_depth.csv`, `twoland_fixed.py` (verbatim copy of `model_sims/twoland_fixed.py`, so the scripts run in place) and `twoland_fixed_delayed.py`.
* The `.tex` files search `figures/` and `manuscript_ECOMOD_v42_src/figures/`, so they compile unchanged both in the repository folder and in a flat working folder; the SI has the two generated tables inlined (`python3 assemble.py` re-assembles both files from `parts/`).

Deliverables
* `manuscript_ECOMOD_v42.tex` / `.pdf` — main text (elsarticle, preprint 12pt; 33 pp with references).
* `manuscript_ECOMOD_v42_supplementary.tex` / `.pdf` — Supplementary Information S1–S7 (17 pp).
* `fig1_model_dynamics.pdf` (+ `.png`), `fig2_nfa_aggregation_face.png`, `fig3_composition_attribution.png`.
* `figures/S5_*.png, S6_*.png, S7_*.png, S12_*.png` — one-stock comparator figures reproduced in SI S7
  (copied from `supplementary/FIGURES/` in the repository).
* `CHANGELOG_v41_to_v42.md`, `HIGHLIGHTS_v42.md`.

Sources (edit these, then re-assemble)
* `parts/00_front.tex 01_methods.tex 02_results.tex 03_discussion.tex 04_refs.tex` → main;
* `parts/si_00.tex si_01.tex si_02.tex si_refs.tex` (+ `si_tab_drawdown.tex`, `si_tab_recovery.tex`, inlined by `assemble.py`) → SI.

Assemble and compile
```
python3 assemble.py                           # writes manuscript_ECOMOD_v42.tex and _supplementary.tex from parts/ (SI tables inlined)
tectonic manuscript_ECOMOD_v42.tex            # or: latexmk -pdf (elsarticle, natbib, booktabs, tabularx, amsthm, hyperref)
tectonic manuscript_ECOMOD_v42_supplementary.tex
```

Recompute figures and SI tables
```
python3 make_fig_model.py       # Fig. 1 — reruns the demonstration and asserts every quoted number first
python3 drawdown_depth.py       # si_drawdown_depth.csv → Table 2b, Fig. 1c, Tables S4–S5
```
Both scripts import `twoland_fixed.py` from `model_sims/` (the deposited quality-based solver); `work/twoland_fixed_delayed.py`
is the one-line delayed-quality variant reported in Table S2.

Repository placement suggestion: `agent 2 productivity illusion/` alongside v41, with `VERSION` bumped to 42 and
`HIGHLIGHTS.md` replaced by `HIGHLIGHTS_v42.md`.

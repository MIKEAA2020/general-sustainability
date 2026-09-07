# Supplementary Package — Index

Companion to the manuscript **Emergent Carrying Capacity and the Composition Illusion: Two-Land Conversion and the Identifiability of Collapse** (Revision 34, *Ecological Modelling*).

This is the **bundled supplementary package**: documentation + supporting figures + reproducibility guidance accompanying the manuscript.

## Contents

| File | What it is |
|---|---|
| `SUPPLEMENTARY_information_v2.md` | **Supplementary Information (v2, aligned with v34).** Full model + symbol table, scaling, analytic derivations, scenario & parameter tables, sensitivity/robustness, the recovery metric `\mathcal{R}_c(T)` and gate-sign asymmetry, prediction→section map, supplementary references. |
| `FIGURES/` | **15 supporting figures** (S1–S15), each produced by a script in `model_sims/`, `graphical_abstract/`, or `reports/`. Captions in `FIGURE_CAPTIONS.md`. |
| `FIGURE_CAPTIONS.md` | Captions for S1–S15, linked to their generating script, with the one-stock-comparator vs two-land scope split made explicit. |
| `REPRODUCTION_GUIDE.md` | **Code map + reproduction guide.** Dependencies, file/folder structure, step-by-step commands to rebuild every numeric result and figure, output registry (figure ↔ script ↔ data), verification protocol. |
| `DATA_AVAILABILITY.md` | **Data & code availability statement**, including deposit/repository recommendation (Zenodo / GitHub release). |
| `ABSTRACT_submission.tex` | The abstract as LaTeX (mathematics kept as LaTeX for the submitted manuscript); self-contained; `\mathcal{R}_c`-consistent. |

## Figure set (S1–S15)

- **S1–S13** — **one-stock comparator** (single-capital `A`) limit, retained as the comparator the manuscript keeps as a limit: feedback loop, macro-ratio plane, flow-share separation, delay-boundary cliff, overshoot run, masking window, recovery vs collapse, recovery insight, characteristic spectrum, `a₁₁` vs delay, sustainable-yield regimes, basin heatmap, basin delay response.
- **S14** — Graphical abstract (two-land): the two books, the coupling, the composition illusion.
- **S15** — The **aggregation face** of the masking result (two-land, real data, 1961–2022). **This is main-text Figure 1**, embedded in §Discussion and referenced as `Figure~\ref{fig:aggregation}`; a publication-resolution copy (300 dpi PNG) for separate upload is in `reports/figures_for_submission/Figure1_aggregation_face.png`.

For submission (Elsevier convention, matching the original ECOMOD-26-1191 upload), upload each figure as a **separate file** and place the caption text in the manuscript's figure-caption list. Captions for all figures are collected in `FIGURE_CAPTIONS.md`.

## Relationship to the manuscript (v34)

- The **main text** is `manuscript_ECOMOD_v34.tex` (two-land).
- The **SI** is `SUPPLEMENTARY_information_v2.md` (v2); the older `SUPPLEMENTARY_information.md` (v33) is retained for reference and is **not** the live SI for v34.
- The **abstract** in the main text is the same as `ABSTRACT_submission.tex`, rendered in the manuscript's backtick-math notation.
- The **figures** here are the non-essential-to-the-main-text set; the manuscript cites the core results inline (5 tables in text; S15 is the recommended main-text figure for the real-series claim).

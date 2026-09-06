# Supplementary Package — Index

Companion to the manuscript *Emergent Carrying Capacity, the Biocapacity Ratio, and the Productivity Illusion: Deficit-Driven Collapse in a Delayed Coupled Human–Environment Model* (Revision 30, *Ecological Modelling*).

This is the **bundled supplementary package**: documentation + supporting figures + reproducibility guidance accompanying the manuscript.

## Contents

| File | What it is |
|---|---|
| `SUPPLEMENTARY_information.md` | **Supplementary Information.** Full model equations + symbol table, non-dimensionalisation/scaling, analytic derivations (MSY, fixed-liability threshold, equilibrium family `P = B(A)/e`, stability classification), scenario & parameter tables, sensitivity/robustness record, prediction→section map, supplementary references. |
| `FIGURES/` | **14 supporting figures** (S1–S14), each produced by a script in `model_sims/` or `graphical_abstract/`. Captions in `FIGURE_CAPTIONS.md`. |
| `FIGURE_CAPTIONS.md` | Captions for S1–S14, linked to their generating script. |
| `REPRODUCTION_GUIDE.md` | **Code map + reproduction guide.** Dependencies, file/folder structure, step-by-step commands to rebuild every numeric result and figure, output registry (figure ↔ script ↔ `data/*.json`), verification protocol. |
| `DATA_AVAILABILITY.md` | **Data & code availability statement**, including deposit/repository recommendation (Zenodo / GitHub release). |
| `ABSTRACT_submission.tex` | The abstract as LaTeX (mathematics kept as LaTeX for the submitted manuscript); 300 words. |

## Figure set (S1–S14)

- **S1** Feedback / causal-loop diagram
- **S2** Macro-ratio plane — `R_B` vs `R_A` (`τ_g = 10` and 30)
- **S3** Flow-share separation (generality of the `ψ`-regime closed form)
- **S4** Delay-boundary / `τ_g`-driven cliff
- **S5** Representative overshoot run (stock `A`, biocapacity `B`, population `P`)
- **S6** Productivity-illusion / masking window (B rising while A falls)
- **S7** Recovery vs collapse for the same initial condition
- **S8** Recovery insight (density-dependent sigmoidal recovery; rate vs lag)
- **S9** Characteristic spectrum (leading eigenvalue vs `τ_g`; always positive real)
- **S10** `a₁₁` vs delay (zero-delay condition violated everywhere)
- **S11** Sustainable-yield regimes (`B(A)` shape by regime)
- **S12** Basin heatmap (baseline delays)
- **S13** Basin recover-fraction vs regenerative delay
- **S14** Graphical abstract (three-panel banner)

## Relationship to the manuscript

- The **main text** is `data/revisions/IMPLEMENTED_revision_ECOMOD_v30.md`.
- The **abstract** in the main text is the same as `ABSTRACT_submission.tex`, rendered in the manuscript's backtick-math notation.
- The **SI** provides derivations/tables behind the main-text results.
- The **figures** here are the non-essential-to-the-main-text set; the manuscript cites the core figures inline.

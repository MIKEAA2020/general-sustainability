# ECOMOD v42 → v43

- **Date:** 2026-10-24
- **Base:** ECOMOD v42, `main`, `1ba3d3c8a286a055b1342b5102731b601ec3d428`

## Scope

Adopt the GFN/NFA-facing accounting and dimensional convention throughout the v42 manuscript/SI lineage. This is not a model recalibration: functional equations, numerical parameter values, and simulated trajectories are unchanged from v42.

## Changes

- State consistently that each annual NFA footprint/biocapacity account amount is reported in gha, not gha yr^-1. Distinguish the annual account amounts `B`, `E`, `Y_f`, `Y_c`, and `S` from the model-internal accumulated-shortfall liability `D` (gha yr), for which `dot D` and `eta D` are in gha.
- Complete and align unit annotations in the main parameter table, SI symbol table, derivations, empirical descriptions, and result captions. Preserve the distinction between the two-land quality index `q` and the one-stock comparator's rate coefficient `q`, and between comparator `kappa` and two-land `kappa_w`.
- Clarify per-capita quantities and dimensionless ratios/indices; keep physical crop-output observations distinct from GFN/NFA-valued yields until normalized or calibrated.
- Add unit-bearing drawdown CSV headers and clarify the units/vintage context of the main figures and comparator captions.
- Regenerate the one-stock comparator figure assets without changing their simulation inputs or trajectories. The compiled files remain SI Figures S1/S2 under existing numbering; the “boom: B & P rise” callout has two colour-matched pointers in whitespace, and the S2 mask-window label sits adjacent to the highlighted window.
- Compact the abstract and keyword typography so the complete abstract and keywords stay on the title page; abstract text and claims are unchanged.

## Numerical anchors retained

- Figure 1: strict composition-mask window `150.3 yr`; `E_ceil = 1.1384 gha`.
- Baseline account yields/parameters remain those of v42; the conversion, debt, quality, population, and land-allocation trajectories were not recalibrated.
- Comparator mask: `5.4 yr` representative window; critical initial deficit `0.075 gha`.

## Validation

The Python files were syntax-compiled; the drawdown CSV, Figure 1, and SI comparator figures were regenerated. `work/verify_tab_conv_basin.py`, `work/recovery_metric_and_tau_p_scan.py`, and the comparator RK4 check completed. Both assembled TeX documents compiled with Tectonic. The compiled symbol-table page, main Figures 1–3, and SI Figures S1–S2 were inspected. Non-fatal TeX box warnings remain; there were no build errors or missing figures.

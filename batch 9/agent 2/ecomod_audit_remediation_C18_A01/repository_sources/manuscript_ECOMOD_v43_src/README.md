# ECOMOD v43 source package

- **Version date:** 2026-10-24
- **Lineage:** direct successor to ECOMOD v42
- **Repository destination:** `agent 2 productivity illusion/manuscript_ECOMOD_v43_src/` on `main`

This release standardizes the manuscript and supplementary information on the Global Footprint Network / National Footprint and Biocapacity Accounts (GFN/NFA) accounting convention. It is a dimensional and presentation revision, not a recalibration. The two-land equations, numerical parameter values, and model trajectories are unchanged from v42. The separately published SI v3 artifact is preserved and is not overwritten by this package. The package includes the compiled 33-page main manuscript (`manuscript_ECOMOD_v43.pdf`) and 18-page SI (`manuscript_ECOMOD_v43_supplementary.pdf`) alongside the modular source.

## Accounting and model units

| Quantity | Unit / convention |
|---|---|
| Annual NFA account amounts: `B`, `E`, `Y_f`, `Y_c`, `S` | gha per annual account |
| `dot B`, `dot E`, `dot Y_f`, `dot Y_c`, `dot S` | gha yr^-1 (continuous-time rates of change) |
| `dot D`, `eta D` | gha |
| Leaky integrated-shortfall state `D` | gha yr |
| Per-hectare account yields `b_f`, `b_c`, `Upsilon`, `Delta b_conv` | gha ha^-1 |
| Capital regeneration-value coefficient `b_G,c` | gha yr ha^-1 |
| Degradation coefficient `alpha` | gha^-1 yr^-1 |
| Per-capita footprint `e` | gha cap^-1 |
| Restoration coefficient `chi_r` | gha^-1 yr^-1 |
| Land rates `u_c`, `R_rc` | ha yr^-1 |
| Population and carrying capacity `P`, `K` | cap |
| Two-land quality `q`, shares, ratios and normalized indices | dimensionless |
| Comparator logistic-wave steepness `kappa` and two-land steepness `kappa_w` | yr^-1; distinct parameters |

The one-stock comparator retains its own stock-unit system. Its feedback-rate coefficient `q` is not the two-land quality state `q`; the SI states this distinction explicitly.

## Rebuild

From this directory, with Python, NumPy, Matplotlib, and Tectonic available:

```sh
python assemble.py
python drawdown_depth.py
python make_fig_model.py
python figure_scripts/makefig_v43.py
python figure_scripts/make_maskfig_v43.py
tectonic -X compile --outdir build manuscript_working_main.tex
tectonic -X compile --outdir build manuscript_working_si.tex
```

The assembler reads the editable fragments in `parts/`, inlines the SI result tables, and writes the two `manuscript_working_*.tex` inputs. Figures and the drawdown CSV are generated beside the source. The working TeX filenames are intentionally neutral; the edition metadata is in the source parts and package documentation.

## Validation performed for v43

- Python syntax compilation passed for the assembly, model, figure, and validation scripts.
- `drawdown_depth.py` regenerated `si_drawdown_depth.csv`; `make_fig_model.py` regenerated Figure 1 and reported a 150.3 yr strict masking window and `E_ceil = 1.1384 gha`.
- The independent basin/conversion check reproduced the deficit-side eigenvalue `-0.05366 yr^-1` up to the demand ceiling and the listed floor-contact thresholds.
- The recovery/gate-sign scan completed, reported zero area-conservation residual, and kept its optional delay diagnostic separate from the manuscript's reported results.
- The one-stock comparator figures regenerated with unchanged trajectories: the masking-window figure reports `5.4 yr` and critical deficit `0.075 gha`.
- Both TeX documents compiled with Tectonic. The assembled SI pages for Figures S1/S2, the symbol table, and the main empirical/model figures were visually checked. Remaining TeX messages are non-fatal box warnings; no compilation error or missing-asset failure occurred.

For the currency decision and the v42 base SHA, see [`ECOMOD_VERSION_CURRENCY.md`](ECOMOD_VERSION_CURRENCY.md). The v42-to-v43 scope is recorded in [`CHANGELOG_v42_to_v43.md`](CHANGELOG_v42_to_v43.md).

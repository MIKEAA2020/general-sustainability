# ECOMOD v44 source package

- **Version date:** 2026-10-24
- **Lineage:** direct successor to ECOMOD v43; v43 remains unchanged
- **Repository destination:** `agent 2 productivity illusion/manuscript_ECOMOD_v44_src/` on `main`
- **Current release build:** `manuscript_ECOMOD_v44.pdf` and `manuscript_ECOMOD_v44_supplementary.pdf` (36 and 22 pages), with matching versioned TeX sources

V44 corrects the delayed-capacity history initialization and technology-wave bookkeeping, preserves both current-quality and delayed-quality solver variants, and reports a matched active-wave/no-wave debt experiment as a conditional diagnostic. The manuscript/SI use the GFN/NFA-facing convention for annual account amounts. The baseline discussion now distinguishes the capital-land area state `A_c` from its modeled contribution `Upsilon(q) A_c` to annual biocapacity `B`: the baseline area declines 46.16%, while the contribution declines 51.72%. This is a conditional model trajectory, not a measured global physical-stock trend. The SI also contains an explicit model-to-NFA mapping table and a component-level physical-stock scoreboard.

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
| Two-land quality `q`, shares, ratios, and normalized indices | dimensionless |
| Comparator logistic-wave steepness `kappa` and two-land steepness `kappa_w` | yr^-1; distinct parameters |

The one-stock comparator retains its own stock-unit system. Its feedback-rate coefficient `q` is not the two-land quality state `q`; the SI states this distinction explicitly.

## Rebuild

From this directory, with Python, NumPy, Matplotlib, and TeX Live (`pdflatex`) installed:

```sh
python drawdown_depth.py
python make_fig_model.py
python work/tb_wave_debt_scan.py
python figure_scripts/makefig_v43.py
python figure_scripts/make_maskfig_v43.py
python assemble.py
mkdir -p build
for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build manuscript_working_main.tex; done
for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build manuscript_working_si.tex; done
```

The assembler reads editable fragments in `parts/`, inlines the SI result tables, and writes neutral `manuscript_working_*.tex` inputs. `make_fig_model.py` checks the explicit manuscript baseline, including `Upsilon(q) A_c`, the fast-book contribution, the balance-point ceiling, and the floor-proximity window before writing Figure 1. `work/tb_wave_debt_scan.py` regenerates the controlled wave experiment's metrics, trajectories, and figure. Outputs are written beside the source or under `build/`.

## Validation completed for the current working build

- The explicit baseline run (`E=0.825` gha; `A_c(0)=1.5` ha; `A_f(0)=0.6` ha; `q(0)=0.9`; `dt=0.05` yr; `T=400` yr) passes the Figure 1 assertions. At the end of the joint `B`-rise / `A_c`-decline window (`t=150.3` yr), `Upsilon(q) A_c` is `0.08364 -> 0.04038` gha (51.72% decline), while `A_c` is `1.500 -> 0.807659` ha (46.16% decline). The fast-book contribution is `0.51000 -> 0.784617` gha; the exact endpoint `b_f` is `0.849974` gha ha^-1, so `A_f=0.923107` ha, which rounds to the manuscript's `0.923`.
- The generated drawdown figure labels thresholds as operational floor-proximity values; its text describes asymptotic approach, not finite-time floor contact.
- The model-to-NFA mapping table, the SI demonstration audit, and the controlled wave/no-wave comparison compile in the Supplementary Information.
- Main and SI PDFs compile successfully with pdfLaTeX (36 and 22 pages). The checked pages include the abstract/keywords, baseline result, revised boundedness heading, discussion passage, SI demonstration table, and model-to-NFA table. There are four nonfatal `hyperref` PDF-string warnings and underfull-box notices; no overfull boxes, unresolved references, or unresolved citations were found in the final pass.
- A source scan found no author-written British-English spellings beyond the official journal title *Ecological Modelling*; published source titles retain their original spelling. The main and SI bibliographies contain identical sets of 57 entries and matching entry text, with no duplicate keys, missing citations, or uncited entries.

For the version-currency decision, see [`ECOMOD_VERSION_CURRENCY_v44.md`](ECOMOD_VERSION_CURRENCY_v44.md). The revision history is recorded in [`CHANGELOG_v43_to_v44.md`](CHANGELOG_v43_to_v44.md). `SHA256SUMS.txt` records the package-file digests (excluding the checksum file itself); the v44 currency note records remote-tree/blob verification.

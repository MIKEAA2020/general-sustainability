# Reproduction guide — ECOMOD C20 A01

**Manuscript:** A rising biocapacity total can mask ecological-capital land drawdown: a two-land model
**Version:** ECOMOD C20 A01, 31 October 2026
**Preprint deposit:** https://doi.org/10.20944/preprints202611.0852.v1
**Reproduction package (data and code):** https://doi.org/10.5281/zenodo.24092131

This guide states what is needed to rebuild the submitted documents and to re-execute the numerical results.

## 1. Rebuilding the documents

The submitted LaTeX sources compile without BibTeX, Python or network access: both bibliographies are embedded `thebibliography` environments.

```sh
pdflatex ecomod_C20_A01_main.tex   # three passes
pdflatex ecomod_C20_A01_SI.tex     # three passes
```

Requirements: a TeX Live installation with `pdflatex`, `elsarticle`, `amsmath`, `amssymb`, `amsthm`, `booktabs`, `array`, `tabularx`, `graphicx`, `enumitem`, `xurl` and `hyperref` (Debian: `texlive-latex-base`, `texlive-latex-extra`, `texlive-publishers`). The build used TeX Live 2025/Debian.

Layout dependencies: Figures 1–3 and Figures S1–S5 must be present; the SI `\input` files are the table fragments supplied with the source archive. A complete, tested source-only archive is available from the corresponding author and at the repository path given in the Data availability statement.

Verified result: main 38 pages, SI 31 pages, zero LaTeX warnings, zero overfull boxes, no unresolved references or citations. A clean extraction of the source archive rebuilds both documents with identical extracted text.

## 2. Re-executing the numerical results

The Python pipelines require the pinned environment in the reproduction package (`code/requirements.txt`). Download the package from https://doi.org/10.5281/zenodo.24092131 and run from its root:

```sh
python code/reproduce_empirical_C18_A01.py     # NFA Edition 2026 endpoints, components, Divisia, proxy
python code/reproduce_two_land_C18_A01.py      # two-land baseline, budgets, refinement, ladders
python code/reproduce_comparator_C18_A01.py    # one-stock comparator (SI S7, Figs. S1-S4)
python code/verify_reproduction_C19_A01.py     # all three in a disposable copy
```

Absolute paths and the repository location are given in the manuscript's Data availability statement.

## 3. Reported values and their sources

| Quantity | Value | Source |
|---|---|---|
| Baseline model biocapacity | 0.594 → 0.825 gha (+38.97%, reported as 39%) | §3.1; Fig. 1a |
| Capital-land area | 1.500 → 0.808 ha (−46.16%) | §3.1; Fig. 1a |
| Capital-land account contribution Υ(q)A_c | −51.72% (per-hectare term −10.33%) | §3.1 |
| Masking interval | about 149 yr (98% of the B rise and 85% of the A_c fall within 25 yr) | §3.1; Fig. 1a |
| Demand ceiling | E_ceil ≈ 1.138 gha | §3.2; Fig. 1b |
| Conversion contribution, 100-yr fixed demand | +0.547925 gha; maintenance/retirement −0.311098; net +0.231310 gha | §3.6; SI S10 |
| Restoration contribution, 400-yr run | +0.016561 gha; conversion +0.513933; maintenance/retirement −0.218037 | §3.6; SI S10 |
| Closure error, Δt 0.05 → 0.00078 yr | 5.144e-3 → 8.040e-5 | SI S10 |
| NFA world biocapacity, 1961–2023 | 9.7254 → 12.1428 ×10^9 gha (+24.86%) | §3.7; Table 5 |
| NFA biocapacity per person | 3.17319 → 1.50065 gha cap⁻¹ (−52.71%) | §3.7; Table 5 |
| NFA production footprint per person | 2.19700 → 2.56462 gha cap⁻¹ (+16.73%) | §3.7; Table 5 |
| Component contributions | cropland +24.06, built-up +7.44, forest −5.95, fishing −0.42, grazing −0.27 pp | §3.7; Table 5 |

## 4. Units convention

Annual account amounts `B`, `E`, `Y_f`, `Y_c` and `S` are reported in gha with the annual basis implicit, following Global Footprint Network practice. The internal accumulated deficit `D` is the only stock-like quantity and is in gha·yr; `Ḋ` and `ηD` are in gha. Per-capita footprint `e` is in gha cap⁻¹. Areas are in ha; `q` is dimensionless. Full table: SI S1.

## 5. Data attribution

NFA inputs and NFA-derived data and figures retain CC BY-SA 4.0 attribution to Lo et al. (2026). OWID/FAOSTAT attribution and provider terms are retained. No provider endorsement is implied. No third-party restricted data are redistributed with the manuscript.

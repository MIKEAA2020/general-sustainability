# C13 validation and build report

**29 October 2026 — PASS within the stated M1/M2 scope.**

## New numerical calculations

- M1 bounds and feasible endpoint witnesses reproduce their recorded outputs. Known quality in the illustration is q=0.9; the non-injective yield readout is explicitly qualified.
- 1,000 independent scalar chain-rule/channel algebra checks: maximum discrepancy **5.55 × 10⁻¹⁷**.
- Four existing cases × seven timesteps = **28 integrations**; all 28 were additionally recomputed in memory with `python code/verify_c13.py --full`. Recorded numerical fields agreed within 1e-10 absolute tolerance.
- Independent trapezoidal RHS integrals were not changed to force closure. Absolute closure residuals decrease at every tested halving in each case. At the finest step, relative residuals are **0.0348%, 0.0628%, 0.0143%, 0.00380%**, all below 0.1%.
- Technology + debt integrals reproduce the fast-yield channel to floating-point tolerance. The near-zero signed debt totals in the wave pair do not imply absence of temporary debt peaks.
- Exported finest-step endpoints and cumulative integrals match the full quadrature outputs. Reporting-grid CSV has 20,004 data rows; it is not the grid used for the integration.
- No nonquality state-guard clips or conversion-availability limiter activations occur in these selected runs. All reconstructed reserve areas exceed 0.1 ha; total-area balance error is at most 4.44 × 10⁻¹⁶ ha.
- Each run has one finite-step quality-cap clipping event. The finest-step raw overshoot is 1.25 × 10⁻⁶; the cap kink is included in the measured residual, not removed by an adjustment.
- The reconstructed original 0.05 yr wave pair matches the C12 six-decimal printed debt peaks and reported times.

This is a numerical closure/refinement check, **not** a general convergence proof, rigorous trajectory error bound, empirical stock validation, or delay-history robustness test.

## Compilation and reference checks

| Check | Main | SI |
|---|---:|---:|
| Final PDF pages | 40 | 27 |
| Unresolved references/citations | 0 | 0 |
| Missing figure dependencies | 0 | 0 |
| Overfull boxes | 0 | 0 |
| Preexisting label numbers retained | 40 / 44 | 45 / 45 |

The four expected main renumberings are later result subsections 3.5→3.7 and 3.6→3.8, plus later original tables 3→5 and 4→6. Original equation/proposition/figure numbers remain unchanged. SI S1–S8 and all 45 existing SI label numbers are preserved. These checks compared auxiliary files from complete builds of the unchanged C12 source and new C13 source using the supplied figure dependencies; they do not verify legacy scientific results.

Four inherited, nonfatal `hyperref` author-metadata PDF-string warnings remain in the main build; the unchanged C12 build has the same warning class. Ordinary underfull paragraph-box diagnostics also remain. There are no unresolved citations/references or overfull boxes. PDFs use installed CM-Super text fonts; the source package contains all eight figure dependencies.

Targeted visual checks covered the newly added main proof/table/budget pages and the SI proof, budget and complete one-page refinement table. Figure identities were checked against the matching captions. This was not a page-by-page or pixel-level review of every inherited layout element.

## Provenance and preservation checks

The two exact C12 source Git blob IDs were independently recomputed from the source bytes and matched the pinned records. Their SHA-256 hashes and all figure origins are in `PROVENANCE.json`. Seven figures are inherited from exact repository/release sources; only the already specified technology-wave illustration is freshly rendered. Source-to-C13 patches are supplied. No earlier manuscript was edited, and no branch merge was performed.

## Environment and reproducibility

- Python 3.13.16; NumPy 2.3.5; Matplotlib 3.10.9.
- TeX Live 2025 / latexmk 4.86; `elsarticle` and recommended LaTeX packages; CM-Super fonts.
- `python code/compute_c13.py` regenerates new calculations, row fragments, and the wave plot.
- `python code/verify_c13.py --full` checks outputs and recomputes all 28 trajectories.
- `bash code/build.sh` compiles both manuscripts.
- Machine-readable checks: `data/c13_independent_checks.json`, `data/c13_validation_results.json`, `data/c13_build_checks.json`.

PDF byte hashes may change on recompilation because of timestamps or font/software versions. Numerical reproducibility is evaluated separately from the delivered-file manifest.

## Not validated or claimed

No M3 experiment was added. The inherited empirical NFA/OWID results, all original parameter grids, one-stock simulations, and other restoration experiments were not rerun. No empirical causal attribution, common-boundary physical-stock inventory, historical calibration, publication acceptance, or author approval is established. This remains a working revision for author verification before submission.

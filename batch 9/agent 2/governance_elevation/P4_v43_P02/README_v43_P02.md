# Governance P4 v43 / supplementary material v10

29 October 2026 · Amin Abaee · [ORCID](https://orcid.org/0000-0002-0019-1842)

This is an additive governance revision. ECOMOD C17, earlier governance packages, version-specific deposit citations and unrelated companions are not edited. No new deposit DOI is claimed.

## Read first

- **Main:** `manuscript/paper4_delay_dynamics_v43.pdf` (54 pages).
- **Supplement:** `manuscript/paper4_supplementary_v10.pdf` (20 pages).
- **Assessment:** `REVISION_ASSESSMENT_v43_P02.md` accounts for additions, replacements and remaining gaps.
- **Protocol:** `ANALYSIS_PROTOCOL_v43_P02.md`, including the explicitly post-inspection common-support correction and exploratory secondary tests.
- **Evidence summary:** `ELEVATION_REPORT_v43_P02.md`.

## What is actually established

1. **Complete protective basin under a sufficient nonlinear gain:** all positive-stock, nonsaturated-effort physical initial states and bounded nonnegative memory histories converge to the unique protective equilibrium. The excluded stock-zero and effort-cap faces are invariant. Covers fixed finite delay and arbitrary positive fixed native/exact-nonlinear review cadence. Point gain <0.475; declared-box gain <0.686294. Not a mobilising/mixed/Euler theorem.
2. **Complete equilibrium root count on all positive delays:** A has two stability windows for each gating variant; B has one. This is an analytic root-count theorem supported by interval Routh/crossing/event ordering, not a finite root search. It is not a full periodic Floquet certificate.
3. **Rigorous full infinite-Fourier fold residual bounds:** both orbit and fold-kernel equations, exact frozen decimal coefficients, interval FFT plus proved alias and tail estimates. Odd-grid augmented solves refine the approximations. **Continuum fold existence/nondegeneracy is still not certified.**
4. **Genuine quantitative field tests, mixed/negative:** a dimensionless ICES herring catch-intensity predictor gives a small protective advantage over AR(1); logistic/recruitment stock tests and recursive annual-surrogate stock forecasts fail baselines. **Joint dynamic field validation of the autonomous DDE is not achieved.** No causal deployment delay is identified.

## Reproduce

Python dependencies are in `requirements_v43.txt`; the executed environment is recorded in `data/environment_v43.json`. Set `OPENBLAS_NUM_THREADS=1`.

```bash
python src/global_protective_basin_v43.py
python src/global_equilibrium_spectrum_v43.py
# This recomputes six augmented folds and is the expensive nominal stage:
python src/fold_continuum_stage_v43.py
# Reads the FROZEN exact-decimal input polynomials; does not redefine them by FFT:
python src/interval_fourier_residual_v43.py
python src/field_response_test_v43.py
python src/field_stock_and_closed_loop_v43.py
python src/figures_v43.py
python src/build_manuscripts_v43.py
python src/build_pdfs_v43.py
python -m unittest discover -s src -p 'test_*v43.py' -v
python -O -m unittest discover -s src -p 'test_*v43.py' -v
python -m unittest discover -s inherited_v42/src -p 'test_*.py' -v
python -O -m unittest discover -s inherited_v42/src -p 'test_*.py' -v
```

The initial unequal-support field outputs are retained for disclosure, not used as the corrected primary analysis. Reproducing the amended response script produces only the corrected outputs. Execution-time fields can differ; valid interval endpoints are outward serialised. The whole-series certificate reads `data/fold_exact_fourier_inputs_v43.json` explicitly, so platform FFT changes do not silently redefine its polynomial inputs. Recomputing nominal folds does not replace these frozen validation inputs.

PDF production needs `pandoc`, `pdflatex`, and standard LaTeX packages. `mutool` supports PDF text/visual checks. Published PDF/source pairs and figures are supplied, so reading does not require these tools. Original v42 artifacts and proofs are preserved in `inherited_v42/`, with their original manifest; relevant legacy fold seeds/helpers are vendored in versioned files.

## Verification and publication

There are 49 new tests plus 64 inherited tests, all passed normally and with `python -O` (113 per mode). These are implementation, consistency and preservation checks, not a substitute for the analytic proofs or a new field replicate. `MANIFEST_GOVERNANCE_P4_v43_P02.json` hashes every deliverable except itself. The one-shot publisher refuses an existing target, reads a fresh remote HEAD, adds only this versioned package, checks every prior path/mode/blob, and verifies all new remote bytes before archiving a separate receipt. Never rerun the v42 publisher.

Public data: ICES SAG API stock `her.27.3a47d`, assessment key 19373, assessment year 2025, frozen on 29 October 2026. The full source URLs, raw responses and a raw-data hash are included. Total-biomass units are not imputed; separate normalisation defines the observation gauge. A single revised vintage is not a real-time historical forecast. Private full-text material, credentials, caches and TeX auxiliary files are not distributed.

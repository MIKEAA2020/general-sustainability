# Paper 09 v44 — build, contents and verification

**Lineage:** `paper09_cod_certification_v43` → **v44**. The v43 edition was the latest merged cod–Edwards manuscript in `e2-v3-source-year`, under `arena agent 1/agent workspace/papers/`; v44 continues that lineage and is stored in the same repository location. See `paper09_cod_certification_v44_CHANGELOG_v43_to_v44.md` for the substantive and editorial changes.

## Deliverables

- `paper09_cod_certification_v44.pdf` and `.tex` — main research article (25 pages).
- `paper09_cod_certification_v44_SI.pdf` and `_SI.tex` — Supplementary Information, Sections S1–S14 (18 pages).
- `paper09_cod_certification_v44_verification.py` — full, named-check verifier. The full run regenerates the results, tables and figures, performs the manuscript-PDF text checks, and writes `paper09_cod_certification_v44_verification_output.txt`.
- `paper09_cod_certification_v44_verification_output.txt` — shipped full-run record: **77/77 checks passed**. A `--quick` run performs 74 checks against the stored result record and does not overwrite this file.
- `paper09_cod_certification_v44_src/` — reproducible source bundle: editable article and SI parts, exact re-derivation core, generated results, table and figure generators, six vector figures (with PNG review copies), locked panels, frozen protocols and registered campaign artefacts.
- This README, the v43→v44 change log, highlights and cover letter.

## Scientific contribution in brief

The article develops closed-loop robust viability kernels for scalar threshold systems under floor classes and bounded model defects. For a monotone one-dimensional map, each finite-horizon kernel has a computable lower boundary; across horizons, the kernels are the whole safe set, converge to a half-line above a smallest fixed point, or become empty after finitely many steps. For Northern cod, the q10 floor gives a constructive bound of 91.6 kt, while the q05 and worst floors do not make the 884.6-kt LRP self-viable. Exact bounded-defect horizons range from 8–13 years under the worst/q05 floors and 12–28 years under q10, compared with 5–7 years under the registered Lipschitz certificate. For the Edwards Aquifer, a 7.2% flat cut secures 618 ft; no admissible rule secures 660 ft. At 618 ft the declared-defect horizon is three years for positive-pumping rules and four at zero pumping; the audited out-of-sample defect reduces those to two and three years. The exact recursion changes boundary locations in the aquifer, including the staged-rule and zero-pumping exceptions, but not those horizons.

The quantitative claims are independently re-derived from the locked panels and checked against 926 registered campaign comparisons. Stochastic and bootstrap layers are rerun with independent seeds. Tables and figures are generated from `work/results.json`; none of the reported table entries is manually typed.

## Source-bundle map

Within `paper09_cod_certification_v44_src/`:

- `parts/` and `si_parts/` — editable manuscript and supplementary sections; generated table fragments are marked `gen_*`.
- `assemble.py` — inlines the parts into the compiled `.tex` files and generates the SI main-label map from the main `.aux` file.
- `work/p09_core.py` — independent numerical re-derivation; `work/results.json` is its complete output record.
- `work/make_tables.py` and `work/make_figs.py` — deterministic generators for all main/SI tables and six figures.
- `paper09_cod_certification_v44_verification.py` — self-contained copy of the verifier, so the bundle can be checked after local compilation.
- `src/` — locked input data, provenance notes, frozen protocol files, source-year campaign scripts and the archived results used for comparison. The core's first source candidate is this folder's `src/`.
- `figs/` — six vector PDF figures plus PNG copies.

## Rebuild and verify

Use Python 3.10 or newer, NumPy and Matplotlib. PyMuPDF is used for the PDF text checks. Compile with Tectonic 0.15.0 (or a compatible XeTeX engine).

```sh
cd paper09_cod_certification_v44_src
python3 -m pip install numpy matplotlib PyMuPDF

# Build the main .tex and retain its .aux for SI cross-references.
python3 assemble.py --main-only
tectonic -X compile --keep-intermediates --keep-logs paper09_cod_certification_v44.tex

# Generate S0b_mainlabels.tex from the main .aux, then build and compile the SI.
python3 assemble.py
tectonic -X compile --keep-logs paper09_cod_certification_v44_SI.tex

# Full run: re-derive, regenerate tables/figures, check both PDFs, write the report.
python3 paper09_cod_certification_v44_verification.py

# Optional fast check: reuses work/results.json; does not overwrite the full report.
python3 paper09_cod_certification_v44_verification.py --quick
```

The full command runs three regeneration checks plus 74 data, theorem-instance, table, figure and PDF-text checks (77 total). The quick command skips the three regeneration checks (74 total). Both modes return a non-zero exit status if a check fails. If PyMuPDF is absent, the computation and archive-comparison checks still run, but compiled-PDF text checks are skipped; install PyMuPDF for the complete check.

## Protocol and data conventions

Both protocols were frozen on **2026-08-26** and are reproduced in SI Section S13 and in the source bundle. The cod fit uses 1983–2007; its out-of-sample audit is 2008–2015. The Edwards fit uses 1935–1990 transitions; its out-of-sample audit is 1991–2023 (33 transitions), with closed-loop out-of-sample replay started at the observed 1990 head. `first empty` denotes the first empty horizon, one year after `last nonempty`. In the identification sensitivity, λ is the share of residual variance attributed to observation error. The exact family-A fixed points are reported separately from the archived finite-horizon proxies; the latter can sit below the limiting fixed point.

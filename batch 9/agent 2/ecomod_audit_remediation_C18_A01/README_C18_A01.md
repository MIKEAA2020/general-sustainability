# ECOMOD C18 A01 — repository-first audit remediation

**Main:** [ecomod_C18_A01_main.pdf](ecomod_C18_A01_main.pdf) (41 pages)  
**Supplement:** [ecomod_C18_A01_SI.pdf](ecomod_C18_A01_SI.pdf) (31 pages)  
**Audit resolution and complete change account:** [AUDIT_RESOLUTION_C18_A01.md](AUDIT_RESOLUTION_C18_A01.md)

This is an additive revision, not an edit to C17. `inherited_C17/` is an exact preserved package. The main and SI retain the author, ORCID, bibliography, original section/claim labels and prior mathematics. Source diffs are in `evidence/`. Historical reference files under `repository_sources/` retain their original filenames and contents.

## What the repository search established

The artifacts absent from the C17 package were not all absent from the repository. Recovered sources include v42/v43/v44 drawdown CSVs and scripts; the NFA Edition 2026 workbook; OWID cropland-area and cereal-yield snapshots; empirical checkers; and historical gate-sign/comparator routines. The complete main tree was inspected at `d21febdf35aff3b2f38c4f61b1cdbd551a220373` (9,863 entries, not truncated). The recovery manifest records 189 byte-verified files, original repository paths and Git blobs.

Historical versions are not treated as interchangeable. The v42/v43 drawdown numerical data agree, but v44 recovery endpoints differ. A separately implemented current-quality loop reproduces v44 minima and final areas to approximately 1.5e-15; the selected delayed-quality loop is checked against C17's baseline solver and generates the C18 grid. Both the historical and selected outputs are retained distinctly. This is why the v42 CSV was not simply attached as an allegedly exact C17 result.

## Reproduce offline

Python dependencies are pinned in `requirements_C18_A01.txt`. Install them in your own environment, then:

```sh
python code/reproduce_empirical_C18_A01.py
python code/reproduce_two_land_C18_A01.py
python code/reproduce_comparator_C18_A01.py
python code/reproduce_baseline_budgets_C18_A01.py
bash code/build_documents_C18_A01.sh
python code/test_revision_C18_A01.py
python -O code/test_revision_C18_A01.py
```

The budget wrapper runs all 28 preserved baseline trajectories in a disposable copy and never writes inside `inherited_C17/`. The three new pipelines likewise do not modify recovered sources. Building the documents requires `pdflatex`, `elsarticle`, and the standard LaTeX packages used in the sources (`texlive-latex-extra` and `texlive-publishers` on Debian). PDF hashes can change across builds because TeX embeds build timestamps; numerical outputs and preserved originals have separate identity checks.

## Main outputs

- `data/empirical_annual_join_C18_A01.csv`: 63 annual world observations, 1961–2023; population in persons, NFA components, per-capita quantities, indices/log changes, OWID area/yield, crop proxy and explicitly empirical residual.
- `data/nfa_world_source_extraction_C18_A01.csv`: complete source world sheet; 2024–2025 estimates preserved for provenance but excluded from analysis.
- `data/empirical_{endpoints,components,LMDI_sensitivity,crop_calibration}_C18_A01.csv`: endpoint and proxy transformations, including nonpositive-residual level fallback.
- `data/si_drawdown_depth_C18_A01.csv`: 248 selected-model rows, four starting areas × 31 populations × two restoration settings; explicit positive distances above the floor.
- `data/proximity_*_C18_A01.csv`, `data/quality_law_comparison_C18_A01.csv`: bisections, delay and current-quality sensitivity.
- `data/si_gate_sign_C18_A01.csv`: nine policies at three timesteps, including full extrema and separate final B/E.
- `data/comparator_*_C18_A01.csv`: full trajectory, fixed-demand masking/sweep, delay pair/refinement, 416 grid cells, characteristic roots and full-run refinement.
- `figures/`: regenerated three main figures and four one-stock figures; the unchanged matched-wave figure remains in the preserved baseline package.
- `evidence/budget_rerun_C18_A01.json`: successful full 28-run budget check, not just inspection of earlier audit claims.
- `evidence/tests_{normal,optimized}_C18_A01.txt`: 40 tests passing in each Python mode.
- `metadata/source_provenance_C18_A01.json`: release, URL, archived source hashes, honest timestamp limits and software versions.
- `metadata/document_verification_C18_A01.json`: document hashes/pages and final build diagnostics.

## Scientific boundary

The NFA/OWID pipeline reproduces accounting results; it does not identify a global ecological-capital stock or validate the coupled ecological dynamics. SI S11 now specifies observables, independent calibration inputs, estimands, rejection outcomes, temporal resolution and uncertainty treatment for P1–P5. The 20/40-year equality is explicitly an imposed-cap consistency result, not a general ecological prediction. No field dataset, causal validation or parameter identification is fabricated.

NFA inputs and NFA-derived data/figures retain **CC BY-SA 4.0** attribution to Lo et al. (2026); OWID/FAOSTAT attribution and provider terms are retained. See [DATA_LICENSE_C18_A01.md](DATA_LICENSE_C18_A01.md). No provider endorsement is implied.

No cleanup, deletion, merge, or change to companion manuscripts/deposits is part of this revision. The publisher is a one-shot additive tool: **do not rerun it after successful publication**; the separately archived receipt is the publication record.

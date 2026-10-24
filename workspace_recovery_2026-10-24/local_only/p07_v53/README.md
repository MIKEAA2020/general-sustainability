# Paper07 v53 — reproducible source bundle

**Edition:** standalone Paper07 v53, based on Paper07 v52. Paper08 v48 remains a parallel combined manuscript and is not overwritten or merged here.  
**Build date:** 2026-10-16.  
**Status:** source, analysis records, and PDFs compile locally; the all-refs audit selected branch `e2-v3-source-year` in the public repository `MIKEAA2020/general-sustainability`. See `VERSION_AUDIT_2026-10-16.md`.

## Contents

- `paper07_v53.tex`, `parts/`: main manuscript.
- `paper07_v53_SI.tex`, `si_parts/`: 14-section supplementary information, with S-prefixed numbering.
- `figs/`: figures used by the two documents.
- `work/`: v53 scripts, retained analysis outputs, and logs. Preview renders and transient inspection text are omitted from the portable ZIP.
- `src/`: empirical inputs, archived scripts/results, and historical context notes used or cited by the paper. Older dated context notes are archival and are not a substitute for the final all-ref lineage audit.
- `source_material/`: a limited archive of v52 empirical inputs, figures, scripts, and tables; its predecessor PDF is omitted from the ZIP.
- `VERSION_AUDIT_2026-10-16.md`: all-branch/tag/release and split/merge lineage record.
- `paper07_sampled_governance_v53.pdf`, `paper07_sampled_governance_v53_SI.pdf`: compiled main and supplementary PDFs.
- The portable ZIP includes `MANIFEST.sha256`, with SHA-256 checksums for the packaged files (except the manifest itself).

The ZIP intentionally excludes credentials (including `.github_pat` and `uploads/github_pat.txt`), Git metadata, Python caches, and page-preview images.

## Build the documents

From the bundle root, with a recent TeX Live installation providing `pdflatex` and the packages used by the source:

```sh
pdflatex -interaction=nonstopmode -halt-on-error paper07_v53.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_v53.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_v53_SI.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_v53_SI.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_v53_SI.tex
```

The release build was A4, 14 pages main and 29 pages SI. The final main and SI logs contained no overfull boxes, unresolved references, changed-label warnings, or hyperref warnings.

## Reproduce principal calculations

Python 3.11+ with NumPy and SciPy is needed for the core and nonlinear checks; figure regeneration uses Matplotlib. Install the listed packages with `python3 -m pip install -r requirements.txt`.

```sh
# Baseline logistic core and the locally rerun one-at-a-time ±2% analysis
python3 work/p07_core.py --grid 4001 --output work/results.json

# Full joint-box scan (128 corners × 20,001 review intervals)
python3 work/p07_core.py --joint-only --grid 20001 --output work/joint_box_fullgrid.json

# Independent finite-difference audit of the full nonlinear flow
python3 work/nonlinear_flow_check_v53.py

# Rebuild supplement tables from their retained input records
python3 work/make_supplement_tables.py

# Regenerate the baseline multiplier figure
python3 work/make_rho_figure_v53.py
```

The empirical stock scripts use paths relative to `src/p7_empirical/`; run them from that directory, as stated in SI S3. The ADH/F verification scripts and the screen-battery script are documented in SI S3 and their retained logs are under `work/` or `src/p7_empirical/`.

## Interpretation and execution status

- SI S11 separates the locally rerun ±2% one-at-a-time table from the archived wider ±5%/±10% battery. The latter is summarized from `src/p7_empirical/recovered/sens_table.csv`; it is not represented as a fresh v53 rerun.
- The portable `screen_battery_v53.py` run did not finish within the 180-second execution window. `work/screen_battery_v53.log` is the restored archived record, not a completed fresh rerun.
- The 17-cell white-noise power table is assembled from archived output plus a two-cell follow-up; the full driver did not finish. Comparator records with missing noise/seed metadata are labeled as archived.
- Dense-grid non-crossing results are numerical classifications, not proofs between grid points. No invariant-circle continuation or nonlinear bifurcation theorem is claimed.

See `PROVENANCE.md` for the edition history and verification record, and `VERSION_AUDIT_2026-10-16.md` for the branch/tag/release and split-merge audit.

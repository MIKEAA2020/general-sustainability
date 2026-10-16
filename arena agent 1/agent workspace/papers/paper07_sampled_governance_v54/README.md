# Paper07 v54 — reproducible source bundle

- **Edition:** standalone Paper07 v54, based on Paper07 v53. Paper07 v52/v53 and parallel Paper08 v48 remain preserved.
- **Build date:** 2026-10-16.
- **Status:** new edition following the v52→v53 coverage crosswalk and correction of stale SI pointers; no numerical analysis was represented as a new rerun. The fresh all-ref lineage audit selected `e2-v3-source-year` in the public repository `MIKEAA2020/general-sustainability`. See `VERSION_AUDIT_2026-10-16.md` and `CROSSWALK_V52_TO_V53.md`.

## Contents

- `paper07_sampled_governance_v54.tex`, `parts/`: main manuscript.
- `paper07_sampled_governance_v54_SI.tex`, `si_parts/`: 14-section Supplementary Information, with S-prefixed numbering.
- `figs/`: figures used by the two documents; unchanged computational figures are retained from v53.
- `work/`: retained v53 analysis scripts, outputs, and logs. They are not described as new v54 reruns. Preview renders and transient inspection text are omitted from the portable ZIP.
- `src/`: empirical inputs, archived scripts/results, and historical context notes used or cited by the paper. Older dated context notes are archival and are not a substitute for the final all-ref lineage audit.
- `source_material/`: a limited archive of v52 empirical inputs, figures, scripts, and tables; the predecessor PDF is omitted from the portable ZIP.
- `CROSSWALK_V52_TO_V53.md`: recovered-content map, including explicit limits caused by the unrecovered v52 Supplementary file.
- `VERSION_AUDIT_2026-10-16.md`: all-branch/tag/release and split/merge lineage record for the v54 numbering decision.
- `VERSION_AUDIT_2026-10-16_v53.md`: preserved historical pre-v53 audit.
- `paper07_sampled_governance_v54.pdf`, `paper07_sampled_governance_v54_SI.pdf`: compiled main and Supplementary PDFs.
- `MANIFEST.sha256`: SHA-256 checksums for packaged files (except the manifest itself).

A compressed copy of this project is available beside this directory as `../paper07_sampled_governance_v54_source_bundle.zip`. The ZIP excludes credentials (including `.github_pat` and `uploads/github_pat.txt`), Git metadata, Python caches, and page-preview images.

## Build the documents

From the bundle root, with a recent TeX Live installation providing `pdflatex` and the packages used by the source:

```sh
pdflatex -interaction=nonstopmode -halt-on-error paper07_sampled_governance_v54.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_sampled_governance_v54.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_sampled_governance_v54_SI.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_sampled_governance_v54_SI.tex
pdflatex -interaction=nonstopmode -halt-on-error paper07_sampled_governance_v54_SI.tex
```

The final page counts, paper size, and clean-log checks are recorded in `PROVENANCE.md` after the release build.

## Reproduce principal calculations

Python 3.11+ with NumPy and SciPy is needed for the core and nonlinear checks; figure regeneration uses Matplotlib. Install the listed packages with `python3 -m pip install -r requirements.txt`.

```sh
# Baseline logistic core and the retained one-at-a-time ±2% analysis
python3 work/p07_core.py --grid 4001 --output work/results.json

# Full joint-box scan (128 corners × 20,001 review intervals)
python3 work/p07_core.py --joint-only --grid 20001 --output work/joint_box_fullgrid.json

# Independent finite-difference audit of the full nonlinear flow
python3 work/nonlinear_flow_check_v53.py

# Rebuild supplement tables from retained input records
python3 work/make_supplement_tables.py

# Regenerate the baseline multiplier figure
python3 work/make_rho_figure_v53.py
```

The empirical stock scripts use paths relative to `src/p7_empirical/`; run them from that directory, as stated in SI S3. The ADH/F verification scripts and the screen-battery script are documented in SI S3 and their retained logs are under `work/` or `src/p7_empirical/`.

## Interpretation and execution status

- SI S11.3 contains the rerun ±2% crossing table. SI S11.4 is a crossing-only summary of the archived ±5%/±10% battery; the full archived rows and fields remain in `src/p7_empirical/recovered/sens_table.csv`.
- V54 corrects section pointers to S7, S13, and S14; adds a bounded, non-prescriptive set of modelling implications in S7.6; and restores a general AI-use declaration.
- The portable screen-battery run did not finish within the 180-second execution window. Its retained log is archived output, not a completed fresh rerun.
- The 17-cell white-noise power table is assembled from archived output plus a two-cell follow-up; the full driver did not finish. Comparator records with missing noise/seed metadata are labelled as archived.
- Dense-grid non-crossing results are numerical classifications, not proofs between grid points. No invariant-circle continuation or nonlinear bifurcation theorem is claimed.
- The v52 PDF is 36 pages, but its final pages explicitly refer to a separate Supplementary file that is not present in any audited repository ref. The v52 source's final inventory says S1–S10 while its body also cites S11–S13.3. See the crosswalk; v54 does not claim complete equivalence to an unavailable SI or recreate its promised identifiability chart.

See `PROVENANCE.md` for the v54 change record and verification status, and `VERSION_AUDIT_2026-10-16.md` for the fresh branch/tag/release and split/merge audit.

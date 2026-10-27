# Paper06 v77 — local audit-repair package

- **Date:** 2026-10-27
- **Parent:** Paper06 v76, preserved unchanged.
- **Status:** Local-only derivative. No push, DOI deposit, or external release has been made or authorized.

## Contents

- `paper06_assessment_separation_v77.pdf` and `.tex` — assembled main article.
- `paper06_assessment_separation_v77_supplementary.pdf` and `.tex` — assembled Supplementary Information.
- `paper06_assessment_separation_v77_src/parts/` — modular TeX source; `assemble_v77.py` checks and regenerates both assemblies.
- `paper06_assessment_separation_v77_src/figs/` — figure assets, including preserved Figure 2 input `fig_witness_triangle_original_v72.png` and clean benchmark input `fig_benchmark_original_v76.png`.
- `paper06_assessment_separation_v77_src/work/` — reproducible Figure 2 and benchmark-axis edit scripts, figure makers, and archived v76 research passages explicitly marked not for submission.
- `build_v77.sh` — clean, ordered local TeX build; builds the main article before SI because SI imports main labels.
- `QA_v77/` — build transcripts, Tectonic logs, and QA record.
- `EDITORIAL_REVISION_PLAN_v77.md`, `CHANGELOG_v76_to_v77.md`, and `IMPLEMENTATION_RECORD_v77.md` — scope, changes, and validation.
- `checksum_v77.sh` and `SHA256SUMS_v77.txt` — a refresh script and checksums for the v77 deliverables and QA files.

## Rebuild and verify

Requirements: Python 3.10+ and Tectonic 0.17.0. The first Tectonic build may download its TeX bundle. From this directory, verify the delivered snapshot or rebuild it as follows:

```sh
# Verify the files as delivered
sha256sum -c SHA256SUMS_v77.txt

# Reassemble and rebuild (set TEX_ENGINE if Tectonic is not on PATH)
python3 assemble_v77.py --check
TEX_ENGINE=/path/to/tectonic-0.17.0 ./build_v77.sh

# Refresh the snapshot manifest after any intentional rebuild or edit
./checksum_v77.sh
sha256sum -c SHA256SUMS_v77.txt
```

PDF metadata and build logs may change on a rebuild, so refresh the manifest before using it to verify a rebuilt snapshot.

To regenerate the two edited raster figures from their preserved inputs, install Python with NumPy, OpenCV, Pillow, and Matplotlib, then run:

```sh
python3 paper06_assessment_separation_v77_src/work/edit_fig_witness_triangle_labels.py
python3 paper06_assessment_separation_v77_src/work/edit_fig_benchmark_unit_label.py
```

The first helper reads the preserved v72 Figure 2 input and places each equality label parallel and immediately adjacent to the diagonal, on the unhatched gray side with a visible non-overlap gap. The second reads the clean benchmark raster extracted from the preserved v76 PDF and changes only the quota-axis unit label to MBU/yr. Rebuild the PDFs after regenerating figures.

## Release boundary

V75 and earlier outputs, v76, ECOMOD c10 and its pins, c8/c9, `main`, checksums, and DOI deposits were not edited. V76 and v77 remain local pending separate authorization. The package does not claim a Lean build, new empirical fit, forecast, validation, or external reproducibility beyond the versioned artifacts described in the article and SI.
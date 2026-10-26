# Paper06 v73 — Figure 2 label correction

**Title:** *Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules*  
**Date:** 2026-10-26  
**Parent:** Paper06 v72, preserved unchanged. This derivative changes only the two Figure 2 equality-label placements and edition metadata; no substantive manuscript prose, mathematical claim, or numerical result is changed.

## Deliverables

- [`paper06_assessment_separation_v73.pdf`](paper06_assessment_separation_v73.pdf) — main article, 48 pages.
- [`paper06_assessment_separation_v73.tex`](paper06_assessment_separation_v73.tex) — assembled main source.
- [`paper06_assessment_separation_v73_supplementary.pdf`](paper06_assessment_separation_v73_supplementary.pdf) — Supplementary Information, 40 pages.
- [`paper06_assessment_separation_v73_supplementary.tex`](paper06_assessment_separation_v73_supplementary.tex) — assembled SI source.
- [`paper06_assessment_separation_v73_src/`](paper06_assessment_separation_v73_src/) — editable TeX parts and figures. The corrected `fig_witness_triangle.png` is accompanied by the unmodified v72 baseline and [`work/edit_fig_witness_triangle_labels.py`](paper06_assessment_separation_v73_src/work/edit_fig_witness_triangle_labels.py), which reproduces the label move.
- [`CHANGELOG_v72_to_v73.md`](CHANGELOG_v72_to_v73.md) — exact scope, image verification, and build checks.
- [`EDITORIAL_ASSESSMENT_AND_REVISION_PLAN.md`](EDITORIAL_ASSESSMENT_AND_REVISION_PLAN.md) — source-checked assessment of the supplied summaries/rewrites, the revision plan, and proposed §§1.1–1.2 copy. The proposed prose is not integrated into v73.
- [`CHANGELOG_v71_to_v72.md`](CHANGELOG_v71_to_v72.md) — inherited v72 audit record.

## Figure 2

In both panels, `s₁+s₂=2` is now horizontal, legible, and positioned above the diagonal rather than rotated across it. The figure remains 2165×1262 pixels at 200 dpi. The two label edits affect 5,128 RGB pixels in two local neighborhoods; the red arrows, hatch patterns, axes, witness markers, reserve bars, and lower weight-ratio strip are retained. The main PDF’s Figure 2 is on page 17.

## Build

From this folder, using Tectonic 0.17.0:

```sh
tectonic paper06_assessment_separation_v73.tex
tectonic paper06_assessment_separation_v73_supplementary.tex
```

The known overfull/underfull box warnings match the v72 baseline in count and content; no new citation/reference markers were introduced. Main and SI page counts remain 48 and 40.

## Release and citation discipline

This v73 package is a separate derivative; v72 remains unchanged. No DOI is claimed for this Paper06 edition. The version is pinned by the immutable archive commit and, when synchronized, by the exact-version companion reference. No DOI deposit, checksum, ECOMOD release, or `main` branch was changed.

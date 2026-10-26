# Paper06 v72 — verified audit revision

**Title:** *Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules*  
**Date:** 2026-10-26  
**Parent:** Paper06 v71, preserved unchanged. The documented research-line history is Paper1 v62/v63 → Paper06 v64–v71 → v72; this does not assert a direct Paper1 v31 → Paper06 v71 parentage.

## Deliverables

- [`paper06_assessment_separation_v72.pdf`](paper06_assessment_separation_v72.pdf) — main article, 48 pages.
- [`paper06_assessment_separation_v72.tex`](paper06_assessment_separation_v72.tex) — assembled main source.
- [`paper06_assessment_separation_v72_supplementary.pdf`](paper06_assessment_separation_v72_supplementary.pdf) — Supplementary Information, 40 pages.
- [`paper06_assessment_separation_v72_supplementary.tex`](paper06_assessment_separation_v72_supplementary.tex) — assembled SI source.
- [`paper06_assessment_separation_v72_src/`](paper06_assessment_separation_v72_src/) — editable TeX parts, unchanged figures, and the two unchanged figure-generation scripts.
- [`CHANGELOG_v71_to_v72.md`](CHANGELOG_v71_to_v72.md) — audit findings, supported edits, non-applied items, source checks, DOI-package inspection, and build verification.

## Build

From this folder, assemble the main and SI TeX from the corresponding `parts/` files as documented in the v71 README, then run:

```sh
tectonic paper06_assessment_separation_v72.tex
tectonic paper06_assessment_separation_v72_supplementary.tex
```

The figures are unchanged from v71 and resolve through `paper06_assessment_separation_v72_src/figs/`.

## Release and citation discipline

The exact v72 PDF, TeX, SI, and editable source are versioned separately in the companion archive branch. The exact version is identified by the immutable archive commit cited in the synchronized Paper3 v53 companion reference. No DOI is claimed for this Paper06 edition. The verification deposits and their actual contents are distinguished in the changelog; the inspected Figshare packages are related research-line artifacts, not the exact Paper06 v71/v72 manuscript.

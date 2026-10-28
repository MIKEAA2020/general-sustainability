# Paper06 v77 — current build and QA record

**Latest QA:** 2026-10-28  
**Scope:** local submission-text cleanup and rebuild of v77 only.  
**Release boundary:** current v77 package snapshot pushed on branch `agent/p06-ecomod-c11-local-draft-20261028`; no DOI deposit or publication was made. Earlier release history remains unchanged.

## Assembly and build

- `python3 assemble_v77.py` regenerated the main and SI from 9 main modules and 4 SI modules; `python3 assemble_v77.py --check` passes.
- `/usr/bin/pdflatex` (pdfTeX 3.141592653-2.6-1.40.26; TeX Live 2025/dev/Debian) was used because Tectonic was not available in this workspace. The updated `build_v77.sh` also retains Tectonic support when present.
- The script built the main article first and then SI, with three pdfLaTeX passes per document so citations and imported labels could resolve.
- Main and SI build logs, standard-output transcripts, and the engine record are retained in this directory. Pre-cleanup source modules and QA records remain intact under `pre_submission_cleanup_20261028/`.

## Current files and checks

| File | Pages | Page size | Bytes | SHA-256 |
|---|---:|---|---:|---|
| `paper06_assessment_separation_v77.pdf` | 46 | 612 × 792 pt | 1,271,305 | `99bbaf8060a1011736f30a92cb7c3a95826ff072dc26c3cedb6da862887a2bb1` |
| `paper06_assessment_separation_v77_supplementary.pdf` | 25 | 612 × 792 pt | 426,844 | `57499722233cf717bf73890ab8981a3f93b817f7114f32eb66194d39e5171ff5` |
| `paper06_assessment_separation_v77.tex` | — | — | — | `09df1eb44503a4a4825df472adfb32b8442c965e2511b56269d4c0cf0274d558` |
| `paper06_assessment_separation_v77_supplementary.tex` | — | — | — | `b365c7fe7f306bba79f97a499c2240308a64e73689855790eb9f1cd103ab8ae0` |

Final-pass logs contain no unresolved citations/references, duplicate-label errors, missing-file errors, or fatal TeX errors. Text extraction found 46 and 25 nonblank pages, respectively, and no visible internal release/build/version narration from the audited terms. The main title remains the previously authorized Paper06 v77 title.

Nonfatal layout warnings remain: several underfull boxes in both PDFs, repeated small-caps italic font substitutions, and `hyperref` PDF-string warnings for the corresponding-author note. The main has no overfull boxes. SI has one 1.72939 pt overfull line (assembled SI lines 151–166); it was checked in the rendered page and is not visibly clipped.

## Clickable contact links

`mutool show` confirmed URI annotations in both PDFs:

- Main: `mailto:amin_abaee@ut.ac.ir` (annotation object 144); `https://orcid.org/0000-0002-0019-1842` (object 145).
- SI: `mailto:amin_abaee@ut.ac.ir` (object 120); `https://orcid.org/0000-0002-0019-1842` (object 121).

The corresponding-author text is readable in both first pages, and the email and ORCID link text is visibly linked. The SI ORCID is present.

## Visual review

Rendered final-PDF pages inspected:

- Main p. 1: title, abstract, and linked email/ORCID; p. 18: Figure 2; p. 46: final references.
- SI p. 1: title, abstract, and linked email/ORCID; p. 6: dense proof/table page with the small overfull warning; p. 9: common-shock exposition; p. 21: data/code availability and literature positioning; p. 25: final references.
- Figure 2 was rendered at 500 dpi and both panels were enlarged. In each panel, the equality label `$s_1+s_2=2$` is parallel to and immediately adjacent to the diagonal on the unhatched gray side, with a visible raster gap and no contact or overlap.

The reviewed pages are retained as `review_*.png` in `QA_v77/`. No clipping, blank page, title mismatch, or footnote/link overlap was observed.

## Scientific and provenance scope

The cleaned article/SI continue to distinguish finite checks from proofs, delimited pointwise off-diagonal results from unsupported global claims, and historical DFO context from fit/forecast/validation. The benchmark units and scope, exact synchronization hypothesis for scalarized worst dips, margin-space convexification versus implementable control, and local-only verification limits remain as recorded in the v77 source modules and changelog. The removed unsupported/global material remains preserved separately and is not in the submission SI.

V75 and earlier outputs, v76, ECOMOD C10 and its pins, c8/c9, `main`, checksums, and DOI deposits were not edited. The pushed branch preserves this local package snapshot; no DOI deposit or publication was made.

## Reproduction

From the package directory:

```sh
sha256sum -c SHA256SUMS_v77.txt
python3 assemble_v77.py --check
./build_v77.sh
./checksum_v77.sh
sha256sum -c SHA256SUMS_v77.txt
```

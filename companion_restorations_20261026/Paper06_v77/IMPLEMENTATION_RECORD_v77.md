# Paper06 v77 — implementation record

- **Date:** 2026-10-27
- **Parent:** Paper06 v76 (preserved unchanged).
- **Status note (2026-10-28):** The v77 package and 2026-10-28 cleanup are pushed on branch `agent/p06-ecomod-c11-local-draft-20261028`; no DOI deposit or publication was made. The dated implementation details below describe the initial package build and the subsequent local QA record.
- **Plan:** `EDITORIAL_REVISION_PLAN_v77.md`.

## Source mapping

| Modular source | Implementation |
|---|---|
| `parts/00_front.tex` | Preserved the reader-facing opening; corrected static-versus-transition framing and bounded the contribution, verification, and artifact claims. |
| `parts/01_setting.tex` | Made normalized raw-margin scales explicit; retained exact-tube semantics; formatted operator definitions so each operator has one equation number. |
| `parts/02_general.tex` | Stated the finite-menu margin-first hypothesis and exact common-maximizer condition for scalarizing path maxima; restricted convexification claims to required-margin space unless separately implemented. |
| `parts/03_witness.tex` | Delimited physical blending and complete-excursion control; retained the safe three-switch counterexample to any broad switching-failure claim; bounded CES conclusions to proved diagonal results; framed common-shock consequences as model-relative rather than prescriptions. |
| `parts/04_benchmark.tex` | Used MBU and MBU/yr, separated normalized income and reserve coordinates, retained only the optional historical dimensional map, and disclaimed empirical calibration/forecasting. |
| `parts/04b_related.tex`, `parts/05_discussion.tex`, `parts/06_appendix.tex` | Corrected literature positioning, stated the static quantifier-gap mechanism, and aligned theorem/limitation language with the proofs. |
| `parts/07_refs.tex` | Updated local-only availability, version-mismatch, historical DFO, and v76/v77 status statements. |
| `parts/si_00_front_proofs.tex` | Updated the result map and Leontief full-support reasoning; removed an unsupported machine-verification claim from the common-shock proof; prefixed imported main-text labels to prevent duplicates and resolve SI cross-references. |
| `parts/si_01_extensions.tex` | Replaced unsupported global fixed-sum narrative with pointwise formulas and explicitly finite checks; removed the claim that coupled-shock readings bracket physical truth; labeled unlocated grid counts as historical finite reports; qualified benchmark implications as model-relative. |
| `parts/si_02_benchmark_practice.tex` | Rewrote benchmark interpretation and units; defined the acceptance gap as all-weight licensing without a common typed-feasible plan; used symbolic main-text references; split the practitioner terminology map to avoid an oversized float. |
| `parts/si_03_verification_positioning.tex` | Qualified Lean/artifact scope and updated the local-v77 edition statement and Data Availability cross-reference. |
| `work/edit_fig_witness_triangle_labels.py` | Reproducibly regenerated Figure 2 labels parallel to the diagonal, immediately adjacent on the unhatched gray side with a small visible gap and no overlap, from the preserved v72 input. |
| `work/edit_fig_benchmark_unit_label.py` | Reproducibly changed only the quota-axis unit from kt/yr to MBU/yr, from a clean benchmark raster extracted from the preserved v76 PDF. |
| `work/deferred_v76_material/` | Preserved the removed continuum-closure and framework-extension passages separately, marked not for submission. |

`assemble_v77.py` concatenates the 9 main modules and 4 SI modules. The checked-in assembled `.tex` files were regenerated from those modules and verified with `python3 assemble_v77.py --check`.

## Initial build and PDF validation (2026-10-27; superseded by the current QA record)

- **Engine:** Tectonic 0.17.0; main article built first, then SI with prefixed external labels imported from the fresh main `.aux` file.
- **Output:** main PDF 47 pages; supplementary PDF 29 pages. Both compiled successfully.
- **Reference/citation checks:** no unresolved references or citations, duplicate labels, missing-file errors, or fatal TeX errors in the retained logs. PDF text extraction found no `??` markers and no blank pages.
- **Layout warnings:** nonfatal underfull boxes remain. The logs retain one 2.43 pt overfull box in the main and SI builds and one additional 1.73 pt SI overfull box; there is no oversized-float warning after splitting the terminology map. Existing small-caps italic substitution and hyperref PDF-string warnings remain visible in the logs.
- **Visual review:** earlier full-pass pages were main 1, 7–9, 15, 18, 23, 29–30, 40–41, and 47; SI 2–3, 8, 14–19, 23–25, and 29. After the final edits, additionally reviewed main pp. 18 (Figure 2 at source and 4× PDF render), 26, and 47; SI pp. 7, 11–14, 18, and 29. Figure 2's equality labels are on the unhatched side, parallel and immediately adjacent to the diagonal with a small raster gap and no overlap. The benchmark image/caption use MBU/yr; references and final pages are nonblank.
- **Artifacts:** no v77 Lean build was run. Finite checks, unavailable historic scripts/logs, and DFO historical-vintage limitations are stated in SI S7 and Data Availability.
- **Hashes/logs:** `SHA256SUMS_v77.txt`; raw Tectonic transcripts and logs in `QA_v77/`.

## Current post-cleanup build (2026-10-28)

The current package was reassembled from the 9 main and 4 SI modules and rebuilt with pdfLaTeX (three passes each, main before SI). The final PDFs are 46 pages (main) and 25 pages (SI). There are no unresolved citations/references or fatal TeX errors. The final SI has one 1.72939 pt overfull line, visually checked and not clipped; remaining warnings are nonfatal. `mutool` verifies clickable `mailto:amin_abaee@ut.ac.ir` and ORCID links in both PDFs. Figure 2 equality labels were checked in 500 dpi renders in both panels and remain adjacent without touching or overlap. See `QA_v77/QA_RECORD_v77.md` for current hashes, logs, page checks, and contact-link annotations. The pre-cleanup modules and QA files are preserved in `QA_v77/pre_submission_cleanup_20261028/`.

## Preservation and release boundary

V76 and all earlier releases remain unchanged. ECOMOD C10 and its pins, c8/c9, `main`, checksums, and DOI deposits were not edited. No DOI deposit is recorded for v77. The current v77 snapshot is pushed on branch `agent/p06-ecomod-c11-local-draft-20261028`; no DOI deposit or publication was made. Any DOI deposit or publication requires separate authorization.
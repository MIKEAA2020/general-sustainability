# Paper06 v77 — implementation record

- **Date:** 2026-10-27
- **Parent:** Paper06 v76 (preserved unchanged).
- **Status:** Local-only derivative; no push, DOI deposit, or other external release.
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

## Build and PDF validation

- **Engine:** Tectonic 0.17.0; main article built first, then SI with prefixed external labels imported from the fresh main `.aux` file.
- **Output:** main PDF 47 pages; supplementary PDF 29 pages. Both compiled successfully.
- **Reference/citation checks:** no unresolved references or citations, duplicate labels, missing-file errors, or fatal TeX errors in the retained logs. PDF text extraction found no `??` markers and no blank pages.
- **Layout warnings:** nonfatal underfull boxes remain. The logs retain one 2.43 pt overfull box in the main and SI builds and one additional 1.73 pt SI overfull box; there is no oversized-float warning after splitting the terminology map. Existing small-caps italic substitution and hyperref PDF-string warnings remain visible in the logs.
- **Visual review:** earlier full-pass pages were main 1, 7–9, 15, 18, 23, 29–30, 40–41, and 47; SI 2–3, 8, 14–19, 23–25, and 29. After the final edits, additionally reviewed main pp. 18 (Figure 2 at source and 4× PDF render), 26, and 47; SI pp. 7, 11–14, 18, and 29. Figure 2's equality labels are on the unhatched side, parallel and immediately adjacent to the diagonal with a small raster gap and no overlap. The benchmark image/caption use MBU/yr; references and final pages are nonblank.
- **Artifacts:** no v77 Lean build was run. Finite checks, unavailable historic scripts/logs, and DFO historical-vintage limitations are stated in SI S7 and Data Availability.
- **Hashes/logs:** `SHA256SUMS_v77.txt`; raw Tectonic transcripts and logs in `QA_v77/`.

## Preservation and release boundary

V76 and all earlier releases remain unchanged. ECOMOD c10 and its pins, c8/c9, `main`, checksums, and DOI deposits were not edited. V77 has no DOI and has not been externally deposited; any release requires separate authorization after review.
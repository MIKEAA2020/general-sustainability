# Paper06 v76 — implementation and verification record

- **Date:** 2026-10-27
- **Parent:** Paper06 v75, archive commit `0208f8b1523446a32ef48cbfe50415fe7ec78947`.
- **Status:** New local-only derivative. V75 was read as the base and was not edited; no push or external deposit occurred.
- **Plan:** [`EDITORIAL_REVISION_PLAN_v76.md`](EDITORIAL_REVISION_PLAN_v76.md).

## Source mapping

| Source location | Implementation |
|---|---|
| `paper06_assessment_separation_v76.tex`; `paper06_assessment_separation_v76_src/parts/00_front.tex` | Updated edition metadata and abstract threshold comparison. |
| `paper06_assessment_separation_v76.tex`; `paper06_assessment_separation_v76_src/parts/03_witness.tex` | Replaced the literal tab after `r=` with `\tfrac12`; clarified Theorem 4’s deep-interior finite-rung scope and the `min(s_1,s_2) <= 1` case. |
| `paper06_assessment_separation_v76.tex`; `paper06_assessment_separation_v76_src/parts/04b_related.tex` | Added the concise five-contributions/four-claims bridge in §6.4. |
| `paper06_assessment_separation_v76.tex`; `paper06_assessment_separation_v76_src/parts/07_refs.tex` | Added the direct v75 archive locator at the recorded commit. |
| `paper06_assessment_separation_v76_supplementary.tex`; `paper06_assessment_separation_v76_src/parts/si_00_front_proofs.tex` | Matched the SI proof’s finite-rung and positive-tube scope to the deep interior; removed the misleading “boundary state” description for `min(s_1,s_2) <= 1`. |

Each edited assembled passage was checked against its modular counterpart. Active edition/file references are v76; the explicit v75 mention and URL in Data Availability are historical archive pointers.

## Build and PDF checks

- **Engine:** Tectonic 0.17.0, installed temporarily for the local build.
- **Output:** Main PDF, 49 pages; SI PDF, 40 pages. Both builds completed successfully.
- **Text/link audit:** Neither PDF contains `??` markers. TeX logs have no unresolved reference/citation messages, missing-file errors, or fatal build errors. The main PDF has 14 URI annotations (9 unique destinations), including the direct v75 archive link; the SI has 9 annotations (5 unique destinations).
- **Warnings:** Non-fatal TeX warnings remain, including underfull/overfull boxes, font/PDF-string warnings, and one SI float-size warning. They remain visible in the build output and were not suppressed; temporary build logs are not included in the package.
- **Visual inspection:** Main pages 1, 16, 24, 32–33, 42, and 49; SI pages 5 and 40. The corrected `1/2` renders as a proper fraction; the §6.4 bridge ends cleanly; the archive link, theorem scope, and SI proof render legibly. The last main and SI pages contain references and are not blank.
- **Figures:** All seven figure assets are byte-identical to v75, including Figure 2.
- **Source defect check:** No literal tab remains in active TeX sources; the corrected witness token appears in both assembled and modular main sources.

## Mathematical and release scope

No theorem math, assumptions, model, parameters, numerical results, citations, acknowledgment text, or artwork were changed. V75 and previous packages remain preserved. V76 has not been pushed to any branch and has not been deposited; any release action requires separate authorization after review.

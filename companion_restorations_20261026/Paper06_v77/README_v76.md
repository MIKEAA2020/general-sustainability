# Paper06 v76 — local source corrections

- **Date:** 2026-10-27
- **Parent:** Paper06 v75, archived at commit `0208f8b1523446a32ef48cbfe50415fe7ec78947` and preserved unchanged.
- **Status:** Local-only derivative. No push or external deposit has been made.

## Scope

V76 carries forward the v75 manuscript and applies only the source-verified corrections recorded in [`CHANGELOG_v75_to_v76.md`](CHANGELOG_v75_to_v76.md): restore the missing `\tfrac12` command in the witness, make the abstract’s comparison of `12/5` with the equal-weight licensing threshold 2 explicit, add a short §6.4 bridge explaining how four claims regroup the five §1.3 contributions, add a direct v75 archive locator, and correct Theorem 4/SI wording so the finite-rung conclusion is restricted to the deep interior where both floors exceed 1. The mathematical results and theorem conditions are unchanged.

## Deliverables

- [`paper06_assessment_separation_v76.pdf`](paper06_assessment_separation_v76.pdf) — main article, 49 pages.
- [`paper06_assessment_separation_v76.tex`](paper06_assessment_separation_v76.tex) — assembled main source.
- [`paper06_assessment_separation_v76_supplementary.pdf`](paper06_assessment_separation_v76_supplementary.pdf) — Supplementary Information, 40 pages.
- [`paper06_assessment_separation_v76_supplementary.tex`](paper06_assessment_separation_v76_supplementary.tex) — assembled SI source.
- [`paper06_assessment_separation_v76_src/`](paper06_assessment_separation_v76_src/) — modular TeX, figures, and scripts.
- [`CHANGELOG_v75_to_v76.md`](CHANGELOG_v75_to_v76.md) — changes and validation summary.
- [`IMPLEMENTATION_RECORD_v76.md`](IMPLEMENTATION_RECORD_v76.md) — source mapping, build and QA record.
- [`EDITORIAL_REVISION_PLAN_v76.md`](EDITORIAL_REVISION_PLAN_v76.md) — approved correction scope and acceptance checks.
- V75 and earlier plans, changelogs, and records are retained as historical documents.

## Build and validation

Both PDFs were built locally with Tectonic 0.17.0. The main PDF has 49 pages and the SI has 40. PDF text checks found no unresolved `??` markers; the TeX logs contain no unresolved references/citations, missing-file errors, or fatal build errors. Non-fatal TeX layout/font/hyperref warnings remain, including one SI float-size warning; they were not suppressed. Temporary build logs are not included in the package. The main PDF contains the v75 archive hyperlink. The assembled and modular versions of every edited passage were checked for synchronization, all seven figure assets are byte-identical to v75, and the relevant pages were visually reviewed.

## Preservation and release boundary

V75 and all earlier releases remain unchanged. V76 is a local derivative only: no archive branch, `main`, DOI deposit, checksum registry, ECOMOD c10 or its pins, c8/c9, or earlier release was changed. Any future publication requires separate authorization after review.

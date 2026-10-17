# E3 v25 → v26 / Supplement v3 → v4

**Edition date:** 2026-10-17  
**Status:** built and visually checked; not yet pushed at the time this changelog was drafted.

## Why a new main-text version was justified

This is not a bookkeeping-only increment. It aligns the standalone Edwards companion with Paper11 v68, repairs the visible main-text abstract/impact-statement page break, and clarifies the output-clip and rolling-origin decomposition record. No prior edition was overwritten: `v25.tex` and `supplement_v3.tex` remain intact.

## Changes

- Preserves the earlier claim-level comparison of E3 v24/SI v2 with Paper11 v67/SI S15–S22; that dated crosswalk remains unchanged. Adds a separate v25/v68 alignment record.
- Keeps the H1/H2 point-score gate distinct from the broader M2m function-class restriction. The three Pass-2 climate point-gate passes are reported separately from their subsequent class demotion; uncertainty and five-year results do not retroactively alter the gate.
- Uses conditional-diagnostic/hindcast language for realized target-year fluxes. They are unavailable at the forecast origin and are not forecast skill or a “nowcast.”
- Scopes the five-year training-mean result to the tested J-17 rolling origins; makes no general planning or policy recommendation. The protocol is described as frozen and archived before scoring, not prospectively registered.
- Adds the archived 75-origin increment-error attribution: substitution term +76.028642 ft², residual cross-term −27.490666 ft², raw M2–persistence MSE gap +48.537976 ft², and clipped gap +40.988957 ft². This is carried forward from the verified Paper11 v68 Edwards audit; this build does not claim a fresh rerun of the forecasting pipeline.
- Clarifies the fixed-window M2 path as raw proposals `617.1 → 611.6 → 606.8 → 605.3 → 605.3 ft` versus emitted clipped forecasts `617.1 → 611.6 → 610 → 610 → 610 ft`. The lower clip first binds for target 1959. For rolling h=1, the only bound hit is the 1992-origin upper clip (raw 719.1027 ft, emitted 710 ft); no lower clip occurs.
- Corrects the published SI v3 compile defect in the new SI v4 by removing the invalid `\LTcaptype` value before the longtable. The published v3 file is preserved unchanged.
- Improves reference/table wrapping and condenses the abstract so the Article Impact Statement stays on page 1. The reference list is set in a compact size to keep declarations with the final page.

## Build and inspection

Built separately with Tectonic 0.15.0 (official GNU x86_64 binary; SHA-256 `f0b36e78c13dd75b821984830533f872c9a12c62957e51357bc16e65cdb71013`).

- `v26.pdf`: 10 pages, 270,335 bytes, SHA-256 `57dca5f056b3131e652441645b88c553de4ee52543b465c9ddf89b0ccf3131b5`.
- `supplement_v4.pdf`: 8 pages, 348,186 bytes, SHA-256 `d80da9d30dec345a28175236e240cc23d2b2478fd7e4205088845029a1f7b09c`.
- Both PDFs extract text on every page. Main: 4,392 words, 26 annotations; SI: 3,655 words, 5 annotations.
- All pages of both PDFs were rendered and visually inspected. No clipped text, overlapping content, blank pages, or figure/table overflow was observed.
- Both builds complete with no LaTeX errors, unresolved references/citations, or overfull boxes. Remaining warnings are underfull boxes only: main badness 10,000 at source lines 239–240 and 1,688 at 259–260; SI badness 1,412 at 155–156.
- The five figure files used for the build byte-match the existing E3 branch figures.

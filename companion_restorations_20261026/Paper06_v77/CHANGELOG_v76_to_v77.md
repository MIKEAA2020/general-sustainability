# Paper06 v76 → v77 change log

**Date:** 2026-10-27  
**Status:** Local-only revision; no external release action.

V77 is a substantive audit-repair derivative, not an editorial-only refresh. V76 and all earlier releases remain untouched.

## Claim and proof scope

- Kept the Gemini-based reader-facing opening as the prose base, with source-checked surgical edits.
- Corrected the framing: the plan/weight quantifier gap can occur for static alternative margin vectors; transition paths and disturbances are the application setting, not a necessary source of the gap.
- Made the finite-menu theorem's margin-first assumption explicit. Added the exact synchronization condition: weighted per-coordinate worst dips equal the scalarized path worst dip exactly when a common maximizing time exists for all positively weighted coordinates. Physical convexification is distinguished from a realizable relaxed control.
- Delimited the common-shock and complete-excursion extensions; no general failure of finite-rate switching is claimed. The common-shock proof now uses both coordinate cuts as well as the sum cut and gives a counterexample to the sum-only condition.
- Replaced unsupported global fixed-sum CES claims in submission SI with the proved diagonal results, a pointwise off-diagonal geometric criterion, an exact harmonic specialization, and selected finite rational checks with explicit scope limits. The removed continuum-closure and framework-extension passages are archived separately under `paper06_assessment_separation_v77_src/work/deferred_v76_material/`, marked not for submission.
- Narrowed the Lean and verification statements to the pinned source's selected formalized components and available finite artifacts; no v77 Lean build is claimed.
- Removed the unsupported claim that two coupled-shock readings bracket a physical truth, and rewrote the management-action language as conditional, menu-relative feasibility results.
- Reconciled S4's 676-, 77-, and 5,000-state historical check claims with SI S7: the corresponding verifier/log files were not found, so those counts are not represented as reproducible v77 artifacts. Corrected the SI terminology-map definition of the acceptance gap to require every weight to license some plan while no single plan meets all typed floors.

## Benchmark and figures

- Recast biomass and quota in synthetic model biomass units (MBU and MBU/yr); retained the optional historical map `1 MBU = 442.3 kt`, so `B_lim = 2 MBU` maps to 884.6 kt.
- Kept `lambda = 1 + s_model`; did not substitute a physically scaled biomass margin into the index. Gave income its own positive reference scale and marked income/reserve paths as stipulated, not calibrated profit dynamics.
- Kept DFO values historical/contextual only; no fit, forecast, validation, or current-threshold claim is made.
- Figure 2's equality labels now sit parallel to and immediately beside the diagonal, on the unhatched gray side in both panels, with a visible raster gap and no contact/overlap. The benchmark quota axis is labeled MBU/yr. Both edits have reproducible scripts and preserved clean inputs.

## Assembly, references, and QA

- Updated the stale v76 edition references in SI S7 and Data Availability.
- Added a v77 assembly script and external-label handling so the main and SI sources stay synchronized and cross-references resolve in the ordered build.
- Rebuilt the main and supplementary PDFs with Tectonic 0.17.0; recorded logs, text/reference checks, visual QA, and checksums in `QA_v77/` and `SHA256SUMS_v77.txt`.

No theorem, artifact, or model claim is authorized for external release by this change log.
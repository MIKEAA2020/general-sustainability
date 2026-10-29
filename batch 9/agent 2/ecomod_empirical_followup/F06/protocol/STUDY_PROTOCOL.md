# Working empirical protocol

## Purpose and current scope

The forest–cropland study has two nested aims: estimate changes in specified physical assets, then test their agreement with biocapacity accounts and associations with independently observed conversion. The core estimands and measurement requirements are specified in the manuscript and SI. Fixed-boundary and bounded native-coverage screening are documented in `PHYSICAL_SUPPORT_F04.md`; F05 bounded Brazilian cover support is specified in `BRAZIL_SUPPORT_F05.md`; national forest-support matching, uncertainty calibration and country-level physical estimation remain outstanding; detailed work is listed in `REMAINING_EMPIRICAL_WORK.md`.

## Retained design choices

- Primary interval: 2015–2023. Secondary candidate interval: 2010–2020, conditional on endpoint/cross-sensor compatibility and change uncertainty.
- Account source: NEFBA Edition 2026 v1.0. Absolute total biocapacity is primary. Terrestrial, excluding-built-up, forest-component and separately labelled per-person comparisons are sensitivities.
- Account availability: all nine primary years, flags `+++`, `++` or `+`, required finite/nonnegative values and positive population, unique country–year records, and a five-component reconciliation tolerance of 3.000001 gha in code. The nominal scientific rounding limit is 3 gha; the small numerical allowance handles floating-point comparison.
- Countries: Brazil, Indonesia, Democratic Republic of the Congo, Cameroon, Canada, Finland, France and Australia. Selection is purposive and was not based on paired country outcome signs. Final physical eligibility remains conditional on matched territory, support, coverage and validation.
- Biomass source: ESA CCI Biomass v7.0, with exact retrieved source hashes in the registry. The coarse aggregate provides metadata/coordinate definitions, not validated national forest stocks or fine conversion transitions.
- No native-resolution global download. Preserve original source bytes and document transformations separately.

## Estimands and comparison rules

Stocks are density integrals with the correct area denominator and valid support. Positive-area extent–density contributions use the exact symmetric identity. Appearing/disappearing strata require a separately defined convention. Spatial compensation uses positive and negative local net changes, not gross biological flows. Its interpretation requires effective-support and error-model assessment.

Physical resolution requires justified covariance, bias and missingness assumptions. Provider quality flags derived from endpoint maps are not independent reference observations. Transition validation must be appropriate to forest-to-cropland conversion rather than generic disturbance.

Reporting comparisons use common cases and weights, report full and pairwise coverage, and distinguish independently observed features from target-derived or algebraically recoverable quantities. Calibration and threshold selection must not use held-out evaluation outcomes. Whole-pipeline assessment and uncertainty in error-rate estimates are required before reporting diagnostic performance.

## Outcomes and scope

All sign combinations, null, unresolved and unavailable cases remain admissible. Divergence is not itself proof of conversion, conversion association is not itself a causal effect, and biomass is not a complete measure of ecological condition. Separate quality/demographic modules require independent repeat observations. No global scalar ecological-capital aggregate or ECOMOD quality calibration is presumed.

## Prior information and registration

Existing plans, literature and world-level NFA audits were read. During source discovery, the source schema and earliest Afghan historical rows were inspected. No new paired country endpoint changes were computed before the original specification. The working protocol is not an externally registered preregistration or a claim of pristine prospective design.

F04 accesses native biomass arrays in sixteen deterministic bounded windows solely for valid/zero/missing support counts. Single-year 2015 account forest-area and population values were also inspected during territory checking, not used as independent physical validation. Those window distributions have been inspected; no national density/stock summaries, physical changes or account–asset signs are computed. The probe plan was frozen before payload requests; this is not a claim of pristine blinded validation or external registration. The original F01 protocol is preserved verbatim at `archive/PROTOCOL_F01.md`; its source-input provenance is retained at `metadata/F01_design_input_provenance.json` relative to the package root. The configuration restores the explicit prior-information disclosure. Neither the study windows, candidate countries nor numerical account-availability criteria have been changed.

Future departures from the retained design or calibration choices should be recorded with their timing and reasons before the relevant outcome analysis, and disclosed in Methods when they affect an inference or any claim of prespecification. Discovery chronology and implementation logs remain outside the journal narrative.

Later F04 source-discovery searches exposed published third-party country forest-trend headlines/statistics. They did not change the candidate countries or frozen native-window locations. At F04 discovery, MapBiomas Collection 11 endpoint metadata were only a candidate-source lead. F05 now uses the pinned two endpoint cover arrays for the fixed local Brazilian demonstration, not as a validated national forest-land-use mask. No outcome-naive source-selection claim is made.


## F05 local mapped-cover observations and target discipline

The original F04 protocol is archived verbatim at `archive/PROTOCOL_F04.md`. The bounded F05 configuration, official legend and supplementary protocol were frozen before land-cover array decoding; their hashes are verified at runtime. That local freeze is not independent registration or a claim of outcome-naive design. Both local cover arrays, class areas and spatial patterns have now been inspected. `physical_outcomes_estimated: true` in the current design configuration refers only to these bounded mapped-cover endpoint areas. National physical stock/change and account–asset outcomes remain unestimated.

Retain formations 3/5/6/49, savannas 4/7 and plantation 9 separately. Report formations-only and formations-plus-savanna without selecting a grouping for its sign. These describe different targets, not confidence bounds on the same target. Complete published labels may reflect temporal gap filling/filtering; do not infer direct synchronous observations or validated transitions.

CCI native AGB is a full-cell density, not a forest-only density. Exact fine forest fractions alone cannot identify within-forest biomass. A fraction-times-density calculation requires an explicit allocation model, and the existing extent–density decomposition requires matched forest stock and area. Whole-territory woody biomass is a distinct estimand, not a silently substituted primary forest stock. F05 estimates neither. All eight national physical admissions remain on hold.

The Collection 11 documentation and PUG review are targeted, not exhaustive; the public reference download inspected is Collection 9. Reference compatibility, training reuse, probability design and shared auxiliary lineage need examination before validation or error independence is asserted. No transition/change uncertainty model has been calibrated. The remaining work record and `metadata/brazil/source_review_F05.json` state the open tasks and precise reading scope.


## F06 reference-artifact audit

The F05 working protocol is archived verbatim at `archive/PROTOCOL_F05.md`. `REFERENCE_AUDIT_F06.md` and its hash freeze were fixed before either reference archive was downloaded/decoded. HEAD metadata and earlier F05 outcomes were known. This local specification is not external registration or a held-out design. The two sources are audited together without selecting a favourable representation. Their schema, completeness, role/weight and coordinate findings are now inspected; no map/reference class agreement, transition accuracy or stock change was computed.

CSV annual classes are textual, not the numeric codes suggested by the page description. The audit explicitly distinguishes textual labels, nonblank entries, numeric codes and missing fields. Both sources contain seven locations in the unchanged local footprint but no recorded paired 2015/2023 labels there. Reference absence is not ecological absence. Vector coordinates use the source WGS84 geometry, not its swapped LON/LAT attributes; the source bytes are not edited. A verified class crosswalk, role/inclusion design and compatible endpoint reference information remain necessary. All national admissions remain on hold.

Figure 1 is redrawn as horizontal stacked bars with wrapped region labels from the identical frozen account audit CSV. No availability criterion, regional count or account datum changes.

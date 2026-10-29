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


## F07 conditional allocation exercise and observed mass information

The F06 protocol is archived verbatim at `archive/PROTOCOL_F06.md`. `ALLOCATION_ENVELOPE_F07.md`, the configuration and source input hashes were fixed before computing F07 mass summaries or accessing XLSX ranges. Prior F04 support and F05/F06 local outcomes were known. The frozen supplementary rules are not external registration or held-out evaluation.

Both mapped domains are reported. Conditional on exact point maps/epochs, arbitrary nonnegative within-cell allocation and no finite component-density or temporal constraint, lower/upper aggregates are pure-cell/present-cell full masses. Integer positive-overlap counts, not ecological near-purity thresholds, classify support. All 65,536 cells remain in the fixed footprint. Auxiliary full-cell mass is not silently substituted for forest-only stock. Neither allocation-difference set excludes zero. Actual forest/land-use identity, density/classification error, spatial/temporal covariance and reference timing are not calibrated by these sets.

These computations expose actual local mass summaries and model-conditional difference ranges, so statements that no physical outcomes have ever been computed no longer describe current F07. Earlier records remain historical with their stated scope. No national forest/biomass change, validated local forest-stock change, account–asset sign or reporting performance is estimated. All national admissions remain on hold.

The Excel alternative is 33,714,740 bytes and its worksheet declares 371,343,772 uncompressed bytes. Standing caps were not increased: 160,308 distinct source bytes provide ZIP/workbook/shared-string metadata only. The worksheet was not opened/decoded. No populated-column, complete endpoint, file-equivalence or independent-reference claim is made from shared-string tokens.


## F08 author-requested metadata/declaration and complete Excel retry

The F07 active protocol is archived exactly at `archive/PROTOCOL_F07.md`. The author explicitly requests the ORCID already used in ECOMOD, 6–7 keywords, the exact declaration “Arena.ai Agent Mode was used to assist with computational methods and literature review.” and another Excel attempt with links for unavailable/unread inputs. F08 uses seven keywords emphasizing both field discovery and partial identification/subpixel allocation. The ORCID is 0000-0002-0019-1842 and is linked in main/SI. The declaration replacement is author-authorized, not an unapproved preservation claim. C17 and all earlier documents remain unchanged.

The pre-decoding F08 supplementary protocol/configuration records a workbook-only 40MB download / 400MB member exception, with 500MB total uncompressed guard. No raster/native limit changes. The full 33,714,740-byte workbook is downloaded and hashed, and every record in its sole worksheet is streamed without formula/macro execution. This supersedes the current XLSX-undecoded status, not the truth of the historical F07 metadata-only record.

There are 85,152 records and 135 fields. All 117 common annual CLASS/COUNT/BORDA payloads match the F06 CSV per TARGETID under stated serialization normalization; 2015/2023 tokens, coordinates and training-role tokens also agree. The workbook has the same 4,053 nonblank 2023 entries and none at the seven local reference positions. This does not establish Collection 11 reference independence or local change validation. Mass calculations, support and all eight national physical holds remain unchanged.

`INPUT_LINKS_F08.md` distinguishes successful downloads, documents still unread because of prior guards, obsolete 404 paths with working alternatives, and intentionally bounded country/global rasters. HEAD checks are not full document reads. No broader source completeness or scientific eligibility claim is made.

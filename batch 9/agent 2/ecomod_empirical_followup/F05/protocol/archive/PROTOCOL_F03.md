# Working empirical protocol

## Purpose and current scope

The forest–cropland study has two nested aims: estimate changes in specified physical assets, then test their agreement with biocapacity accounts and associations with independently observed conversion. The core estimands and measurement requirements are specified in the manuscript and SI. Physical matching, uncertainty calibration and country-level physical estimation remain outstanding; detailed work is listed in `REMAINING_EMPIRICAL_WORK.md`.

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

This revision does not inspect biomass pixel values or compute country account–asset change signs. The original F01 protocol is preserved verbatim at `archive/PROTOCOL_F01.md`; its source-input provenance is retained at `metadata/F01_design_input_provenance.json` relative to the package root. The configuration restores the explicit prior-information disclosure. Neither the study windows, candidate countries nor numerical account-availability criteria have been changed.

Future departures from the retained design or calibration choices should be recorded with their timing and reasons before the relevant outcome analysis, and disclosed in Methods when they affect an inference or any claim of prespecification. Discovery chronology and implementation logs remain outside the journal narrative.

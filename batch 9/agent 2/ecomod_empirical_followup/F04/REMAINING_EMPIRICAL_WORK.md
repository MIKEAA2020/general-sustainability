# Remaining empirical work

The intended paper remains **Ecological assets behind improving accounts: a boundary-matched test of composition masking**. This is a developing empirical study, not a completed physical account–asset test and not a replacement design-only publication. The manuscript reports account availability, product definitions, geographic-domain screening and analytical estimands. F04 additionally supplies fixed candidate boundaries and bounded native endpoint coverage observations; these do not finalize the forest sample. Its journal-facing text is kept separate from this implementation record.

## 1. Establish the physical analytical sample

- Resolve territorial definitions for the eight candidate countries, including overseas territories where relevant; record compatibility with national account boundaries.
- Select versioned forest/support observations at compatible endpoints and distinguish forest extent from tree cover, plantation dynamics and land use.
- Obtain bounded native-resolution biomass subsets or justified aggregates for the primary 2015–2023 interval. Do not download global native-resolution rasters or treat nominal raster spacing as measurement accuracy.
- Quantify valid observations, missing observations, observed zero values and converted land. Use the correct whole-cell or forest-area denominator and latitude-dependent area weights.
- Produce a country–interval support and exclusion table before estimating divergence prevalence. All eight candidates currently pass account availability; physical eligibility has **not** been established.

**Required output:** versioned boundaries/masks, observation crosswalk, coverage report and frozen physical sample with exclusions. Account availability alone does not satisfy this step.

**F04 status:** candidate boundary objects, a territorial crosswalk, geographic-domain report and sixteen bounded native endpoint coverage probes are complete. Canada has a documented high-Arctic domain truncation; the examined CDS land-cover source lacks a 2023 endpoint. Independently supported endpoint forest masks, definitive territory correspondence, full national valid-data coverage and the analytical physical sample remain unfinished. The complete evidence and next actions are in `PHYSICAL_SAMPLE_F04.md`. All eight candidates are on hold, not permanently excluded.

## 2. Establish change uncertainty and independent reference information

- Complete examination of product validation and uncertainty documentation for the chosen endpoints and support.
- Justify spatial and temporal covariance, systematic-bias scenarios, missing/converted-pixel treatment and effective spatial resolution.
- Identify independent reference observations appropriate to stock change, not only biomass levels.
- Keep endpoint-derived provider quality flags distinct from independent truth; one-standard-deviation processing rules are not calibrated 95% tests.

**Required output:** documented error/validation model and sensitivity cases. If change cannot be resolved, retain an unresolved outcome or narrow the analysis.

## 3. Calibrate the complete assessment before held-out evaluation

- Specify practical-change thresholds and classification rules without using held-out evaluation outcomes.
- Assess zero-change, covariance, bias, missingness and effective-support scenarios with separate tuning and evaluation.
- Calibrate the full reporting rule, not just individual features, and quantify uncertainty in estimated error rates.
- Define identical-case/weight comparisons, coverage summaries, simple account/endpoint/trend baselines and algebraic-redundancy checks.
- Record any protocol departures and their reasons in the external protocol record. Do not claim a registration or blinding procedure that did not occur.

**Required output:** frozen analysis configuration, calibration results and evaluation design.

## 4. Estimate physical asset changes and account–asset agreement

- Estimate forest extent and above-ground biomass stock changes on matched support, with uncertainty.
- Decompose stock change into extent and mean-density contributions where areas are positive; define treatment of appearing/disappearing strata separately.
- Estimate spatially offsetting local net changes only at a support justified by the error model.
- Compare physical changes with total, terrestrial, excluding-built-up and forest-component accounts, keeping per-person sensitivities separate.
- Retain increasing, decreasing, concordant, divergent, unresolved and unavailable cases. Do not select only increasing-account countries or presume asset decline.

**Required output:** uncertainty-aware physical results, account–asset comparisons, coverage/exclusion tables and sensitivity analyses. No such physical outcomes have been estimated in this revision.

## 5. Evaluate conversion associations and additional reporting information

- Obtain independently observed forest-to-cropland transitions with transition-specific validation; generic tree-cover loss is insufficient.
- Distinguish harvest, fire, regrowth and plantation dynamics. Estimate associations over the eligible sample rather than only preselected masking cases.
- Do not interpret overlays or associations as causal effects without a separate identification design.
- Evaluate additional asset/spatial information on identical cases and weights with held-out performance and full coverage reported.

**Required output:** supported conversion associations and calibrated reporting comparisons, or an explicit scientific limit if the data do not support them.

## 6. Complete the empirical manuscript from generated results

Generate the physical Results, corresponding Discussion, figures, tables, uncertainty statements and updated abstract from the actual estimates. Retain null and opposite outcomes. Complete source and declaration review, archive the analysis and compile main/SI together. Keep implementation history in this external record, not the journal article.

Soil, wetland, fisheries and independently observed demographic extensions remain conditional. A scalar global ecological-capital total, assumed global decline and calibration of ECOMOD's unmeasured quality index are not default deliverables.

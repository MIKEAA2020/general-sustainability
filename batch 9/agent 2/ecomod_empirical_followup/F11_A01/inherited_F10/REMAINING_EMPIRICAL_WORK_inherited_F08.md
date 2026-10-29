# Remaining empirical work

The intended paper remains **Ecological assets behind improving accounts: a boundary-matched test of composition masking**. This is a developing empirical study, not a completed physical account–asset test and not a replacement design-only publication. The manuscript reports account availability, product definitions, geographic-domain screening and analytical estimands. F04 additionally supplies fixed candidate boundaries and bounded native endpoint coverage observations; these do not finalize the forest sample. F05 additionally supplies bounded Brazilian mapped-cover endpoint observations and mixed-support descriptors; these are not national forest/biomass change. F06 corrects the account figure layout and audits actual public reference artifacts without treating them as independent validation. Its journal-facing text is kept separate from this implementation record.

## 1. Establish the physical analytical sample

- Resolve territorial definitions for the eight candidate countries, including overseas territories where relevant; record compatibility with national account boundaries.
- Select versioned forest/support observations at compatible endpoints and distinguish forest extent from tree cover, plantation dynamics and land use.
- Obtain bounded native-resolution biomass subsets or justified aggregates for the primary 2015–2023 interval. Do not download global native-resolution rasters or treat nominal raster spacing as measurement accuracy.
- Resolve whether stock observations identify the forest-only target: full-pixel CCI AGB cannot be allocated by forest fraction alone. Keep whole-territory woody biomass distinct; do not silently substitute targets or combine its stock with forest-only area in a decomposition.
- Quantify valid observations, missing observations, observed zero values and converted land. Use the correct whole-cell or forest-area denominator and latitude-dependent area weights.
- Produce a country–interval support and exclusion table before estimating divergence prevalence. All eight candidates currently pass account availability; physical eligibility has **not** been established.

**Required output:** versioned boundaries/masks, observation crosswalk, coverage report and frozen physical sample with exclusions. Account availability alone does not satisfy this step.

**F04 status:** candidate boundary objects, a territorial crosswalk, geographic-domain report and sixteen bounded native endpoint coverage probes are complete. Canada has a documented high-Arctic domain truncation; the examined CDS land-cover source lacks a 2023 endpoint. Independently supported endpoint forest masks, definitive territory correspondence, full national valid-data coverage and the analytical physical sample remain unfinished. The complete evidence and next actions are in `PHYSICAL_SAMPLE_F04.md`. All eight candidates are on hold, not permanently excluded.

**F05 status:** both Brazil Collection 11 endpoints are conservatively aligned on the unchanged local 256² native window; class groups and source hashes were fixed before cover decoding. Actual local cover endpoints have now been inspected and both formations-only and formations-plus-savanna are reported. Complete published-label coverage is not direct annual-observation completeness or validated change. Source lineage and targeted methods are reviewed, but compatible independent Collection 11 reference labels, local/transition accuracy, density allocation, national coverage and change uncertainty remain unresolved. See `BRAZIL_SUPPORT_RESULTS_F05.md` and the current F05 admission table.

**F06 status:** both inspected reference archives have 85,152 records and seven locations inside the fixed local footprint. The CSV has 4,053 nonblank 2023 classes nationally but none at these seven locations; the vector ends in 2022. Its coordinate attributes are reversed relative to its WGS84 point geometry. CSV class names are textual, not numeric; training flags and weight fields also differ between the artifacts. These findings rule out using these files as a local paired-endpoint validation sample, not all possible reference information. See `REFERENCE_AUDIT_RESULTS_F06.md`.

**F07 status:** the fixed Brazil window now has conditional map-domain biomass allocation/difference sets computed from hash-matched native densities and integer cover-overlap certificates. Both reported difference sets contain zero, even with point maps treated as exact. This is partial identification under a minimal allocation model, not a calibrated uncertainty interval or validated forest stock. All cells remain included; the primary forest target is not replaced by auxiliary whole-cell masses. The XLSX alternative received bounded ZIP metadata inspection only; its full reference population remains unaudited under the standing caps. See `ALLOCATION_RESULTS_F07.md`.

**F08 status:** author-requested ORCID, seven keywords and exact AI declaration are integrated. A narrowly scoped limit exception permits full Excel retrieval/streaming. The workbook matches the CSV on all 117 common annual payloads for all 85,152 shared IDs, as well as coordinates and training-role tokens, and supplies no extra local paired labels. The complete worksheet is now audited; earlier metadata-only descriptions remain historical. Access links/statuses are provided in `INPUT_LINKS_F08.md`.

## 2. Establish change uncertainty and independent reference information

- Obtain/audit compatible paired-endpoint Collection 11 reference information beyond the three examined public representations. F08 streams the complete XLSX and verifies the common annual reference fields against the CSV; it repeats the local paired-endpoint gap and is not an independent reference replication. Reconcile source-specific class names/codes, the 9,999 flagged training rows versus the documented approximately 10,000, sample reuse, coordinate attributes and zero/positive weight differences; do not infer design validity from field presence. Do not treat global overall accuracy as local change accuracy. Trace actual shared auxiliary inputs and their implications for dependence.
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

**Required output:** uncertainty-aware physical results, account–asset comparisons, coverage/exclusion tables and sensitivity analyses. No such national stock or account–asset outcomes have been estimated. F05 mapped-cover endpoints and F07 local auxiliary masses/conditional allocation sets are computed, but do not constitute validated or national forest-stock/change estimates.

## 5. Evaluate conversion associations and additional reporting information

- Obtain independently observed forest-to-cropland transitions with transition-specific validation; generic tree-cover loss is insufficient.
- Distinguish harvest, fire, regrowth and plantation dynamics. Estimate associations over the eligible sample rather than only preselected masking cases.
- Do not interpret overlays or associations as causal effects without a separate identification design.
- Evaluate additional asset/spatial information on identical cases and weights with held-out performance and full coverage reported.

**Required output:** supported conversion associations and calibrated reporting comparisons, or an explicit scientific limit if the data do not support them.

## 6. Complete the empirical manuscript from generated results

Generate the physical Results, corresponding Discussion, figures, tables, uncertainty statements and updated abstract from the actual estimates. Retain null and opposite outcomes. Complete source and declaration review, archive the analysis and compile main/SI together. Keep implementation history in this external record, not the journal article.

Soil, wetland, fisheries and independently observed demographic extensions remain conditional. A scalar global ecological-capital total, assumed global decline and calibration of ECOMOD's unmeasured quality index are not default deliverables.

# F09 revision and preservation account — 29 October 2026

## Authorization and scope

Continuation of the author's “go on” after ATBD review R01: review the uncertainty budget and validation report, consult validation/development plans, and integrate supported findings into a **new** follow-up version. This is not a revision of ECOMOD C17, F08, the standalone follow-up plan or any earlier companion package.

## Main manuscript changes

1. **Sources/methods:** extend the provider references beyond PUG to ATBD, E3UB and PVIR. Add the C-/L-band observation structure, 150 m C-band to 100 m output-grid resampling, interannual weight refinement, land-cover-dependent processing and distinction between published zero estimates and independently observed absence.
2. **Uncertainty methods:** retain all prior requirements and add explicit acknowledgment that the provider already models within-stack and spatial covariance. Distinguish the 0.5 L-band within-stack assumption from unknown final-map 2015–2023 endpoint covariance. Explain that omission of a cross-year term is not evidence of zero covariance.
3. **Provider evidence:** add current v7 stock-validation evidence, including the primary endpoint years and direct endpoint result tables, with withheld reference data, growth adjustment and small-plot harmonization. Distinguish these from local paired forest-change validation and calibrated coverage.
4. **Discussion:** add transport/selection and support limitations, including the no-deforestation screening condition and reference-error contribution to discrepancies. Explicitly reject the interpretation that v7 lacks stock validation.
5. **Bibliography/availability:** add three provider technical references and update the package URL from F08 to F09. Expand the nonredistribution statement from the guide to provider reports generally. No raw reports are redistributed.

## SI changes

1. Add normalized-average versus mass-total variance, systematic endpoint-error difference and the full fixed-support joint-endpoint covariance identity. Existing equations are retained; no covariance coefficients are supplied for the local footprint.
2. Explain the provider's within-stack/spatial covariance, nonrepresentative spatial reference ensemble and conditional treatment of bias-correction uncertainty. Warn against double-counting propagated components.
3. Add current stock-validation response-design limits and the distinction between variance consistency and interval coverage.
4. Identify repeated NFI/LiDAR change-reference leads and the PVP's candidate/current-use discrepancy for Brazil. Distinguish ADPC methods/plans from completed local validation; do not import its serial-independence assumption.
5. Add the distinction between plot-to-pixel forest-fraction harmonization and allocation of already full-cell map biomass. Retrieval maxima do not supply independently validated component-density bounds.
6. Replace the previous generic LiDAR-family paragraph with role-specific GLAS, ICESat-2, inventory/FRA and GEDI distinctions supported by R01. Keep the requirement to trace actual overlap; do not claim all inventory information is circular or that GEDI Level-4 biomass is ingested.
7. **Specific replacement/deletion account:** replace the sentence listing results as “account availability counts, product definitions and computational verification” with the actual scientific result categories: account availability, product definitions, territorial/observation screening, local mapped-cover endpoints and conditional allocation sets. The following exclusions remain. This removes implementation-verification framing from article Results scope; it does not remove any numerical result.
8. Add document-specific technical reference URLs; update the SI package-availability URL to F09 and extend the nonredistribution statement to provider technical reports.

## External additions, not journal narrative

- `SOURCE_REVIEW_F09.md` and `EVIDENCE_MATRIX_F09.csv`: page-addressed source review, 22 findings, implications and limits.
- Two **visually verified printed-equation inconsistencies** in E3UB: N versus N² average normalization and the increasing correlation expression versus the source's own decay equations/figures. These are not verified code defects. The record explicitly does not silently fix the source or recalculate released uncertainties.
- A limited derived numerical transcription of PVIR Tables 66 and 74: 16 stock-bin summaries, not paired observations or new local estimates.
- Full-source identity verification, review/visual-inspection scope, source hashes and reproducibility script. Full copyrighted PDFs, extracted text and rendered pages stay in excluded cache.
- Complete source diffs: `manuscript_main_F08_to_F09.diff` and `manuscript_SI_F08_to_F09.diff`. These are the exact insertion/deletion account; there is no undisclosed wholesale rollback or compression.

## Protected content

- All original numerical data and results, geographic selections, raster/download guards, mathematical kernels, scientific questions, comparison windows, mapped classes and corrected Figure 1 remain unchanged.
- All eight countries remain `hold_not_admitted`. No national physical stock changes, divergence prevalence, class-confusion results, local covariance estimates, bias corrections or confidence-interval coverage estimates are added.
- ORCID `0000-0002-0019-1842`, the seven keywords and the **exact approved** linked Arena.ai declaration remain unchanged. ECOMOD's separate declaration and all earlier manuscripts are untouched.
- `metadata/inherited_unchanged_files_F09.json` records 165 byte-identical inherited files. Historical F04–F08 notes, logs, designs and access status retain their historical version labels; they are not current F09 claims. The new version/scope file identifies the inherited scientific design explicitly rather than relabelling frozen history.
- The active build script and editorial tests are uniquely named for F09; the latter change only the manuscript filenames they examine. Legacy numerical/reference algorithms and their configurations are not changed.

## Validation language

The added tests verify analytic identities, preservation, metadata and manuscript scope. Source hash checks verify source identity. Neither type is called validation of ecological results. Provider stock validation is positive evidence about the observation system, not independent validation newly performed by this project.

# CCI companion-document review and scientific integration — F09

**Review date:** 29 October 2026. **Scope:** E3UB v7, PVIR v7, PVP v6 and ADPC v7, with the previously published ATBD review R01. All page references below are PDF page numbers. This is an external evidence/revision record, not manuscript prose.

## Decision

The new evidence **narrows the inferential gap; it does not close it**. CCI has an explicit uncertainty model and independent v7 **stock** validation, including 2015 and 2023. A claim that v7 is wholly unvalidated, that the provider ignores all covariance, or that every inventory reference is circular would be wrong. Conversely, the reviewed stock comparisons do not establish independently calibrated, forest-specific 2015–2023 change on our local mixed-cell support. No new physical observations, change estimates, local covariance estimates or country admissions are produced here.

F09 integrates supported ATBD and companion findings into a new main manuscript and SI. F08 remains unchanged. The account results, mapped-cover endpoints, conditional allocation sets, eight holds, author identity, seven keywords and exact approved AI sentence are preserved. Source access history, equation discrepancies and revision accounting remain outside the articles.

## 1. What the uncertainty budget already models

[E3UB v7](https://climate.esa.int/documents/3354/End-to-End_ECV_Uncertainty_Budget_E3B_V7.0.pdf), dated 17 December 2025:

- **Within-stack error covariance:** pp. 14–19 discuss correlations among C-band retrievals from monthly observations. The generic median correlation is 0.52 (p. 17). The L-band discussion uses individual backscatter observations and adopts a constant correlation of 0.5 after comparisons at reference sites (pp. 21–22).
- These are correlations among observations used to construct annual retrievals. **The L-band value 0.5 is not a measured correlation between the final 2015 and 2023 maps.** Reusing it as endpoint correlation would conflate different error structures; adding already propagated components again would double-count them.
- **Spatial aggregation:** pp. 23–27 describe spatial error covariance. Eight regional datasets are listed on p. 24; residual semivariograms were fitted in 142 one-degree cells. The source explicitly says the reference set is not representative of global forests (p. 23). The ensemble coefficient is 0.0445 and the implemented kernel is described as 301 × 301 pixels (p. 26). These are not locally fitted covariance parameters for our footprint.
- **Cross-year change:** p. 28, Eq. 3-20, sums the two endpoint variances without a cross-year covariance term. This omission is not empirical evidence that covariance is zero. The text adds uncertainty in an applied bias correction only at the bias-map scale of 0.1°. It does not supply a local bias correction for our analysis.

The general fixed-support identities now in SI distinguish normalized-average variance from mass-total variance, within-year/spatial propagation from joint endpoint covariance, and systematic endpoint differences from random precision. They do not estimate any of these unknown components.

## 2. Two visually confirmed printed-equation inconsistencies

These are **document-level findings, not verified defects in the provider's executable implementation**. No source was silently corrected, no literal inconsistent expression was adopted, and no empirical output was recalculated from either expression.

### 2.1 Normalization of the variance of an average

On **E3UB p. 23**, printed Eq. 3-13 divides the sum of individual variances by **N**, and Eq. 3-15 likewise uses **1/N** for the diagonal sum and **2/N** for the unordered covariance sum. Both the rendered page and extracted text show these denominators.

For an arithmetic mean, the general identity is instead

\[
\mathrm{Var}(\bar d)=N^{-2}\sum_i\sum_j\Sigma_{ij}.
\]

For N independent observations of equal variance σ² this becomes σ²/N, not σ². In contrast, **PVP v6 p. 26, Eq. 3**, correctly prints the double covariance sum divided by **n²**, and its prose says the same. Both pages were visually inspected. Thus the two documents are inconsistent in their displayed average-normalization equations. Provider code or clarification is needed to determine what was actually executed; the printed discrepancy alone cannot establish the magnitude or direction of error in released uncertainty layers.

### 2.2 Spatial correlation versus lag

On **E3UB pp. 24–25**, Eqs. 3-17 and 3-18 algebraically imply a decaying exponential correlation. Printed Eq. **3-19 on p. 25 is `r = 1 − exp(−kD)`**, which is zero at zero lag and increases with distance. This contradicts the stated unit zero-lag correlation, the description of decay, and the descending correlation curves on pp. 25–26. Those pages and Eq. 3-17 were visually inspected.

The deduction that Eqs. 3-17/18 imply `exp(−bD)` is algebra, **not confirmation of the provider's code, parameterization or intended repair**. Neither the literal increasing expression nor an inferred correction is used to generate local uncertainty estimates. The journal SI gives the general covariance identity without turning this external source discrepancy into an implementation diary.

## 3. Positive evidence: v7 stock validation exists

[PVIR v7](https://climate.esa.int/documents/3356/Product_Validation_Intercomparison_Report_PVIR_V7.0.pdf), cover last modified 24 April 2026:

- **pp. 11–12:** the report explicitly describes independent plot and LiDAR comparisons, stating that these reference data were not used to calibrate map production. This is consistent with the ATBD distinction between calibration statistics and a withheld validation-plot database. It does not establish independence of every possible additional benchmark.
- **p. 14, Table 1:** the listed total plot counts are 112,334 for 2015 and 52,428 for 2023. These are epoch-specific reference listings, **not a paired-change sample size**, not a count of new field observations in each map year, and not necessarily the counts retained in every later analysis table.
- **pp. 64 and 67, Tables 66 and 74:** direct quantitative stock-comparison results exist at 0.1° for 2015 and 2023. A small derived transcription of their reported bin summaries is supplied as `data/reference/provider_stock_examples_F09.csv` with table/page provenance. The rows are not paired across years and are not used to correct our maps.
- For example, in the 50–100 Mg/ha reference bin, Table 66 lists MD 9 and RMSD 34 Mg/ha over 2,231 cells in 2015; Table 74 lists MD 2 and RMSD 27 over 1,525 cells in 2023. The different sample/support composition prevents interpreting their difference as measured temporal bias drift. Other bins have negative mean differences. No uniform bias, preferred change sign or transferable local error rate is inferred.

This goes beyond the ATBD's mainly earlier-release change examples. The correct conclusion is **current stock validation with limits on transfer to our estimand**, not absence of v7 validation.

## 4. Reference response design and selection matter

- **PVIR p. 13:** the described eligibility criteria include no deforestation between inventory and map dates. Its examples retain older epoch wording, so the PDF alone does not verify the exact executable screening for every newer year. The condition nevertheless matters when considering transfer to converted land.
- **PVIR p. 18:** stock references can be adjusted using growth rates over temporal discrepancies of up to ten years. These are harmonized references, not necessarily contemporaneous repeated measurements. The source recognizes ambiguity between low-biomass mature forest and young stands.
- Small-plot AGB is multiplied by forest fraction for plot-to-pixel harmonization. At 0.1°, the Tier 1 comparison requires at least five plots per cell. This response design is distinct from multiplying an already full-cell-normalized map density by forest fraction to infer forest-only stock. The harmonization operation does not observe the unknown component densities inside a mixed map cell.
- **PVIR pp. 96–98:** within-pixel sampling examples show apparent low/high-bin bias even when pixel means are correctly specified. Conditioning/binning, support mismatch, reference error and map error must be distinguished. A plot–map discrepancy is not automatically pure map error.
- Stable-forest selection and growth-based harmonization do not by themselves invalidate stock validation. They constrain the population and temporal processes to which its error characteristics can defensibly be transported. They do not establish validation of converted pixels or our primary paired interval.

## 5. Random SE, RMSD and coverage are different quantities

**PVIR p. 19** says the delivered SE layer represents the random part of AGB error and that its 0.1° aggregate already accounts for spatial correlation. The comparison of reported variance against discrepancy variance omits positional error, within-pixel representation error and harmonization error. The report defines an `IVar` diagnostic and discusses when the reported SE would be pessimistic under its assumptions.

Therefore:

1. `IVar` is not an empirical coverage estimate for a 95% interval.
2. RMSD is not adopted wholesale as map-only error, much less as a local paired-change standard deviation.
3. Missing components do not prove that every delivered SE is too small; covariance, reference uncertainty and assumptions also affect the comparison.
4. A complete change-error model must address systematic endpoint differences as well as random covariance, classification/allocation and support uncertainty.

## 6. Brazilian NFI comparison: useful, but not the required pair

**PVIR pp. 85–88** presents a user-led comparison of the **2018 v7** stock map with Brazilian NFI data. The reference calculation uses tree measurements and a pan-tropical allometry with fixed wood density **0.632 g/cm³** (p. 86). It distinguishes subplot and plot support and averages map values over their corresponding extents. Plot/subplot size and spatial averaging affect agreement.

This is positive country-relevant stock evidence. It is not a direct 2015–2023 paired validation of our local forest groups. The reference assumptions and support must accompany any future use; neither the country name nor the word independent establishes exact compatibility with our target.

## 7. Plans identify leads, not completed local validation

[PVP v6](https://climate.esa.int/documents/3364/Product_Validation_Plan_PVP_V6.pdf), 22 December 2025:

- **pp. 17–18:** describes compilation of change references, including repeated NFI data and repeated LiDAR maps, predominantly for an earlier interval. Filtering can remove obsolete or subsequently deforested plots.
- **p. 22:** specifies aggregation and minimum-reference requirements for change comparisons; aggregation scale is part of the estimand/response design.
- **pp. 23–26:** distinguishes map, plot, geolocation, representation and harmonization errors and supplies the general spatial covariance sum. Planned model identification does not prove every component has been estimated for our setting.
- **p. 42, Appendix 2:** lists a potential Brazilian LiDAR reference dated **2011–2018**. However, p. 18's account of the current retained change-reference data does not include Brazil. This is a candidate/current-use discrepancy to resolve, not permission to assume an available eligible dataset. The dates also do not match 2015–2023.

[ADPC v7](https://climate.esa.int/documents/3371/Algorithm_Development_Plan_Change_ADPC_V7.0.pdf), cover last modified 29 April 2026:

- **pp. 9–18:** discusses implemented stock-difference/trend approaches, illustrative earlier-interval results and proposed further development.
- **p. 16:** its trend example assumes no serial correlation of annual AGB estimates. That assumption does not identify the endpoint covariance of our primary difference.
- **p. 18:** calls for further repeated-field/LiDAR validation. A listed activity is not a completed assessment. Trend agreement, plausibility and different publishers are not substitutes for compatible independent change reference measurements.

No candidate reference was downloaded or admitted as a result of this document review.

## 8. Provenance discrepancies retained, not repaired

- PVIR's cover identifies v7 and April 2026, while body headers include v3 and v1 labels and older dates. The body contains explicit v7/2023/2024 results. These headers do **not** justify relabelling the whole report as an older product assessment.
- PVIR's conclusion retains smaller tier-count ranges than its updated Table 1. We do not reconcile these into a fabricated common sample. Explicit table/section/page references are retained.
- PVP p. 15 and PVIR p. 18 give different biomass thresholds for age-category harmonization. Neither set is silently treated as the verified executable rule for both documents, and neither is applied to our estimates.
- ADPC's cover says version 7.0, its document reference includes `V6`, and body headers say v5/December 2023. Its older example epochs are not silently extended to 2023 or treated as newly validated merely because the cover was updated.
- E3UB's normalization and correlation-expression discrepancies are recorded in §2 above. They remain unresolved at implementation level.

## 9. Acquisition, review coverage and limits

Four complete official PDFs were acquired, individually below the standing **25,000,000-byte** guard: 30, 108, 42 and 22 pages, **202 pages acquired**, not 202 pages carefully reviewed. Full-file hashes, sizes, ETags, final URLs and page counts are recorded in `metadata/companion_review_F09/source_registry_F09.json`. Final media URLs were used for identity-pinned GETs because the redirect endpoint has a different ETag. No transfer or raster guard was increased.

The review is targeted: E3UB's core uncertainty/aggregation/change sections; PVIR's reference methods, selected endpoint result tables, Brazil comparison and support-error discussion; PVP's harmonization/change-reference/error-model sections and appendix; ADPC's change-method and development sections. Large early multi-page text outputs were truncated; they are not represented as complete close reading. Rendered pages actually opened for visual inspection were E3UB **23–26 and 28**, PVIR **18, 64, 67 and 86**, and PVP **26**. Rendering other pages is not counted as visual inspection. The formula findings were checked in page images, not inferred solely from extraction.

Raw PDFs, full extracted text and page images remain in excluded cache and are **not redistributed**. The package contains source metadata, our analysis, a limited derived numerical transcription and reproducibility code. Source review and mathematical/software checks do not validate our ecological estimates.

## 10. Consequences for the next empirical step

1. Verify the provider's actual aggregation/correlation implementation or obtain clarification of the printed discrepancies before adopting that model numerically.
2. Establish an eligible, accessible repeated biomass reference on the required dates/support, documenting measurement error and actual reuse. Candidate listings and growth-adjusted stock references are not enough.
3. Resolve the exact endpoint masks/converted-land handling and retrieve any needed native uncertainty observations only within unchanged bounded-access limits.
4. Estimate or justify joint endpoint and spatial covariance, systematic differences and support/allocation uncertainty before defining calibrated change-resolution rules.
5. Retain all eight admission holds until the existing scientific criteria are actually met. Do not infer national trends or divergence prevalence from this source review.

The complete manuscript change account is in `metadata/revision_record_F09.md` and the two versioned unified diffs. The source evidence matrix and source-scope register distinguish provider statements, mathematical deductions and unresolved empirical requirements.

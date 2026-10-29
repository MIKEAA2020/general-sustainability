# Proposed article text — R01 recommendations, not applied

These passages are proposed for a future uniquely versioned revision. F08 remains unchanged. They are scientific prose, not access logs or revision history. Add the ATBD to the bibliography with its document reference `CCI_BIOMASS_ATBD_V7`, internal issue date 17 December 2025 and official URL. The index's different date belongs in the external source register; it should not be silently substituted for the document's internal date.

## A. Main Methods: biomass observation system

The biomass observation system combines C- and L-band radar estimates with structural calibration and land-cover-dependent processing. The C-band branch is generated at 150 m spacing and resampled to the 100 m L-band grid. Merging weights are refined across years at an aggregated scale to improve interannual consistency, with separate treatment of tropical evergreen forest and cropland. Thus, common product version and nominal output spacing do not establish independent endpoint errors or independent 100 m observations. Temporal processing, shared calibration and changing observational coverage must be considered when assessing change uncertainty (CCI Biomass ATBD v7, §§3, 4.2 and 4.5.3).

## B. Main Methods or Discussion: support and the meaning of zero

CCI Biomass does not impose a forest mask over all vegetated land. Land-cover information nevertheless affects calibration, removal of erroneous assignments over selected nonvegetated classes, and some merging decisions. A user-defined forest domain must therefore be distinguished from the product's processing masks. Zero-valued published biomass estimates are retained separately from missing values, but they do not by themselves establish an independently observed absence of woody vegetation. The precise mask epochs and their treatment of converted land require verification for the selected endpoints (CCI Biomass ATBD v7, §§3.9–3.10, 4.3.3 and 4.5.3).

## C. SI: structural calibration and reference independence

The roles of auxiliary observations differ across model components and product versions. The documented canopy-density–height relationship uses ICESat GLAS observations, whereas ICESat-2 heights and national or subnational inventory-based biomass statistics support the current height–biomass relation. FAO Forest Resources Assessment statistics supplement countries without identified inventory support. Earlier versions used map-based biomass information. GEDI-derived structural comparisons and historical inputs should not be conflated with ingestion of GEDI Level-4 biomass, which the ATBD explicitly excludes. The ATBD also distinguishes calibration statistics from the inventory-plot database used for validation and states that the latter was not used to calibrate or fine-tune the height–biomass relationship. Independence of any additional benchmark must be assessed from its actual source observations and reuse, not its publisher or the general label “inventory” (CCI Biomass ATBD v7, §§3.5 and 3.13).

## D. SI: change uncertainty and systematic differences

For fixed geographic support, let an endpoint density estimate be expressed as the true density plus a systematic error term and a zero-mean random error. The error in an area-weighted biomass difference then contains both the difference of endpoint systematic errors and the difference of endpoint random errors. If \(\Sigma_{st}\) denotes the cross-covariance matrix of random errors at endpoints \(s\) and \(t\), the random-error variance of the total difference is

\[
\operatorname{Var}(\widehat{\Delta Q})
=\boldsymbol a^{\mathsf T}
(\Sigma_{11}+\Sigma_{00}-\Sigma_{10}-\Sigma_{01})
\boldsymbol a,
\]

conditional on the stated support and systematic terms. This expression does not remove endpoint-specific bias or account for uncertain classification, allocation, missingness or support. The provider's endpoint-interval reliability classes do not, by construction alone, establish a calibrated confidence level for the selected interval. The ATBD's illustrative change results mainly concern the preceding product release; their error characteristics cannot be transferred directly to the current release and the primary 2015–2023 comparison (CCI Biomass ATBD v7, §§5 and 6.2).

## E. Allocation interpretation

The maximum-biomass layers used to constrain product retrieval are model-derived, scale-dependent quantities. They are not automatically independently validated upper bounds on true forest-component density within a mixed cell. Consequently, these retrieval constraints do not by themselves justify narrowing the minimal within-cell allocation sets. Finite component-density bounds or temporal allocation restrictions would define additional models requiring separate justification and sensitivity analysis. Conditional allocation sets remain distinct from calibrated uncertainty intervals for actual forest biomass (CCI Biomass ATBD v7, §3.13.3).

## Editorial handling

- Retain the research questions, country choices, primary interval, fixed local footprint, account results and existing allocation results.
- Retain the distinction between full-pixel biomass, mapped-cover domains and forest-land-use stock.
- Do not insert a universal 40–60% error, covariance value, finite ecological ceiling or preferred change sign.
- Do not claim that all inventory data are circular, that GEDI Level-4 biomass is ingested, or that every local pixel undergoes the same temporal refinement.
- Keep document download history, source hashes, page-availability checks and this recommendation record outside the articles.
- The author-approved AI declaration and ORCID need no change as a result of this review.

# CCI Biomass ATBD v7: implications for the empirical follow-up

**Review R01 · 29 October 2026 · Baseline: follow-up F08**

## Overall assessment

The supplied document materially improves the methods review. It supports the existing separation of biocapacity accounts, mapped cover, full-pixel woody biomass and validated forest stock. It also supplies specific processing details that should replace generic discussion of possible dependence: **temporal refinement of merging weights, inventory-informed structural calibration, optical canopy-density inputs and land-cover masks.** These are reasons to describe the observation operator more accurately, not reasons to presume ecological decline or reject the product wholesale.

**The access/reading gap for this ATBD is resolved for the reviewed material. The empirical validation gap is not.** No new national physical stock, sign of change, class confusion, independent validation sample, change-error calibration or admission decision is established. The F08 conditional allocation results remain unchanged and conditional. All eight national physical admissions remain on hold. F08 itself has not been edited; this review supplies recommendations and proposed journal-facing wording separately.

### Source completeness and identity

The nine uploads omit PDF pages 106–120. The author's [release](https://github.com/MIKEAA2020/general-sustainability/releases/tag/external_pdf_follow_up_ecomod) supplies them as `106-110.pdf`, `111-115.pdf` and `116-120.pdf`. All **12 parts and 138 pages** are now available; every part matches its release SHA-256 digest. The missing range is consequential because it contains much of the change-results discussion, including the cautions on full-resolution differencing.

The title/header date inside the supplied ATBD is **17 December 2025**, whereas the [official document index](https://climate.esa.int/en/projects/biomass/key-documents/) lists ATBD v7 under **9 June 2026**. A bounded comparison against the currently served official 67,553,500-byte PDF found matching whitespace-normalized extracted text on **all 138 pages**. This supports textual correspondence despite the date-label discrepancy; it does not establish byte-for-byte PDF or figure equivalence. The original was not downloaded whole and has no complete-file SHA here. Its range reader accessed 24,955,100 distinct bytes under the unchanged 25 MB guard. The parser reported malformed cross-reference offsets and optional object reads denied at the guard; those limitations are recorded, not hidden behind the successful text comparison.

Reading was targeted to the empirical questions, with substantive methods/results passages examined and the temporal-weight equation, reliability diagrams and Annex D layout visually checked. All pages were text-extracted, but this is not an all-figure inspection, implementation reproduction or independent product validation. Source PDFs and full extracted text are not redistributed.

## 1. Annual maps form a jointly processed time series

**Source evidence:** §4.5.3, PDF pp **101–102**, describes refinement of C-/L-band merging weights across the 2005–2012 and 2015–2024 stacks. The cost function compares merged estimates with following one- or two-year estimates. Search is constrained to ±20% of the initial weights and performed at an aggregated 0.01° scale. Tropical evergreen forests are excluded from that refinement and assigned L-band weight; cropland has a further weight override. The results discussion on p **111** explains the interannual harmonization. [Source parts A, B, D below.]

**Implication:** a time series from one product release is not a sequence of entirely separate endpoint retrievals. Temporal processing is a documented dependency pathway, not merely a conjecture from a shared publisher. An uncertainty treatment must address it, together with shared calibration and changing observations. The source does **not** provide an estimated 2015–2023 error covariance for the fixed Brazilian window.

Avoid three overstatements:

- Harmonization does not prove that every local change is suppressed, or quantify its attenuation.
- The tropical-evergreen exception means a single uniform smoothing description is inaccurate. The applicable branch in the fixed local footprint has not been mapped in this review.
- Shared processing is not a numerical estimate, or a guaranteed sign, of error covariance. Positive covariance could reduce difference variance relative to an independence calculation, but systematic bias differences remain a separate issue.

**Recommended change:** add a concise description to main Methods §2.1 and an explicit processing-dependence qualification to SI S3. Preserve the primary interval and footprint. Do not infer a national trend from the newly read processing description.

## 2. Describe current calibration lineage, not just historical LiDAR use

**Source evidence:** pp **22–23** distinguish SAR predictors from LiDAR structural calibration and state that GEDI Level-4 AGB estimates are not ingested. The canopy-density/height relation on pp **62–64** is based on ICESat GLAS; GEDI comparisons are discussed, but p **55** says GEDI canopy-cover observations have not yet been implemented in CORE. The maximum-AGB discussion on pp **75–77** says ICESat-2 alone has supplied that layer since v5. These statements qualify the broad sensor list in Table 3-1; different LiDAR products have different roles.

The height-to-AGB relation changes in provenance across versions. Early versions used map-based AGB; **from v4**, pp **67–70** describe relationships fitted using ICESat-2 heights and national/subnational inventory-based AGB statistics, with FAO FRA 2020 averages supplementing gaps. Page **68** reports 992 subnational values and 83 national FRA values; these are calibration-support counts, not independent validation counts. [Source parts E, F, J.]

**Implication:** “CCI uses LiDAR” is insufficient, and “both products use GEDI, therefore their local errors are correlated” is not established. For the MapBiomas comparison, distinguish the Cerrado appendix's GEDI-derived training information from CCI's specifically documented current structural inputs, historical inputs and comparison-only datasets. Exact shared footprints, products, transformations and joint errors are not demonstrated here.

**Important counter-evidence against an indiscriminate circularity accusation:** pp **70–71** describe a comparison against inventory-plot aggregates and expressly say the plot database used for validation was not used to calibrate or fine-tune the height-to-AGB relation. Preserve that distinction. Calibration statistics and the provider's withheld plot database must not be conflated merely because both are called “inventory data.” A proposed external national inventory benchmark still needs its own overlap/provenance audit; it is neither automatically independent nor automatically invalid.

**Recommended change:** replace generic lineage statements with a version- and role-specific description. Do not label all NFI evidence circular or all sensor families independent.

## 3. Optical inputs and land-cover masks matter for support and conversion inference

**Source evidence:** pp **57–59** describe Landsat canopy-density and change inputs, CCI land-cover calibration masks and CGLS-LC100 v3.0.1 masking. Page **59** explicitly distinguishes the absence of a forest mask over vegetated land from removal of erroneous assignments over built-up, bare, snow/ice and water classes. Pages **87** and **95** describe excluding particular land-cover classes and changed areas during calibration. Pages **101–102** add land-cover-specific merging-weight decisions. [Source parts A, E, G.]

**Implication:** the product is neither a forest-only biomass census nor a completely land-cover-free SAR observation. Using a separately published cover map does not, by itself, establish independence of all support decisions. Conversely, calibration masking is not the same operation as restricting every output pixel to forest land use.

The stated CGLS-LC100 annual series is 2015–2019. The passage does not by itself identify the exact mask epoch/transfer used for every 2023 output cell. **That endpoint-mask detail remains to be checked**, especially for converted land. Do not assume the same mask, a contemporaneous 2023 mask or automatic tracking of conversion without evidence.

**Recommended change:** retain F08's forest-only versus whole-cell estimand distinction and the warning against multiplying density by forest fraction as if it identified forest biomass. Add a source-role table: calibration mask, output mask, merging override and user analysis support. Audit conversion jointly with these operations before estimating conversion associations.

## 4. Zero-valued outputs and nominal pixels are not direct ecological observations

**Source evidence:** p **91** describes assigning 0 or maximum AGB in parts of the single-image retrieval rule and discarding more extreme observations. This is an algorithm-level statement, not a diagnosis of each zero in the merged product. Pages **27**, **37** and **82–83** describe spatial averaging, the 150 m C-band branch resampled to the 100 m L-band/output geometry, and broader calibration/merging scales. [Source parts A, G, H.]

**Implication:** distinguish a valid **zero-valued published estimate**, a missing value and an independently observed absence of woody biomass. Do not retrospectively recode the Brazilian zeros or claim their individual causes have been identified. Retain them under the existing support rules. Prefer “zero-valued estimates” to unqualified “observed zeros” when discussing ecological meaning.

Likewise, 100 m output spacing does not establish 100 m independent information, effective ecological resolution or precise localization of biomass among intersecting 30 m cover pixels. The exact overlap calculation remains useful for geometric support, but exact geometry does not remove these observation limitations.

**Recommended change:** narrow the terminology and add the multiscale observation description. Do not alter arrays, the fixed footprint, cell counts or the conditional allocation calculation on the basis of this literature review alone.

## 5. Change uncertainty requires bias as well as covariance

**Source evidence:** §5, pp **102–103**, defines change through endpoint estimates with endpoint bias terms. The results on pp **112–116** are chiefly examples from **v6**, and p **113** explicitly states that global v7 change maps were not ready when the document was finalized. The provider's example uses 2010–2020, including a sensor-era contrast; it does not validate v7 change in 2015–2023. Page **114** describes endpoint ±1 SD overlap rules; p **116** says the reliability approach does not account for different endpoint biases and does not evaluate spatial averaging in that discussion. [Source parts B, C, D.]

**Implication:** F08's caution about an uncalibrated 95% interpretation is supported. Do not present the cited 40–60% typical endpoint SDs on p 114 as a universal/local calibrated uncertainty, a 95% interval or a measured error for the Brazilian window. Do not present a v6 illustrative change pattern as empirical evidence of the v7 national outcome.

For fixed support and area vector `a`, a useful **review-derived accounting identity**, not an estimate supplied by the ATBD, is:

\[
\widehat{\Delta Q}-\Delta Q
=\boldsymbol a^\mathsf T(\boldsymbol b_1-\boldsymbol b_0)
+\boldsymbol a^\mathsf T(\boldsymbol\varepsilon_1-\boldsymbol\varepsilon_0),
\]

where endpoint errors are split into systematic terms `b` and zero-mean random terms `ε`. The random-error variance is

\[
\boldsymbol a^\mathsf T
(\Sigma_{11}+\Sigma_{00}-\Sigma_{10}-\Sigma_{01})
\boldsymbol a.
\]

Uncertain masks, allocation, missingness and changing support require additional treatment. These expressions do not supply the unknown matrices or bias corrections.

**Recommended change:** retain the covariance formula, add the endpoint-bias distinction and specify release/interval-specific validation. Read the separate uncertainty budget and validation/intercomparison report before claiming calibrated change resolution. Do not choose covariance, thresholds or bias values to produce a desired sign.

## 6. The ATBD's maximum-AGB layer is not a free hard subpixel bound

**Source evidence:** pp **73–79** describe successive maximum-AGB layers, their inventory/map and later LiDAR basis, percentile/filtering choices and inherited uncertainty. Page **78** says direct accuracy of the layer cannot be quantified there; its performance is assessed indirectly through map validation. Pages **90–91** and **98** describe its retrieval constraint role. [Source parts A, F, G.]

**Implication:** a retrieval ceiling does not automatically become a validated upper limit on true forest-component density inside every mixed cell. Reusing it as an independent ecological bound would require additional scale, estimand, validity and dependence arguments. It is not permission to turn the F08 allocation sets into confidence intervals.

**Recommended change:** retain the minimal-model sets. If future work adds finite subcell-density or temporal constraints, label them as additional assumptions, justify them separately and report sensitivity without selecting the preferred sign. The new reading does not narrow the currently published intervals by itself.

## 7. Country-specific inventory lineage and next admission work

Annex D, PDF p **138**, identifies inventory-support entries relevant to six of the eight candidate countries. The table below is a factual lineage screen, **not a new set of eligible validation data**. Source documents have not been retrieved/read merely because their URLs appear in Annex D.

| Candidate | Annex D entry | Consequence for a proposed external benchmark |
|---|---|---|
| Brazil | Six ecoregions; AGB; 2018 | Audit the Brazilian Forest Service statistics and reuse before treating them as independent validation. |
| Indonesia | Seven islands; AGB; 2014 | Audit the FREL-based source, territorial support and model/calibration overlap. |
| Democratic Republic of the Congo | 26 provinces; AGB; 2011–2016 | Audit the cited reference-level source and Xu et al. lineage; do not treat the range as paired 2015/2023 observations. |
| Canada | Twelve ecozones; AGB; 2006–2017 | Audit the NFI support/overlap; the previously documented northern domain truncation remains unresolved. |
| Finland | Nineteen NFI units; AGB; 2016–2020 | Audit the inventory series and support before using it as an external benchmark. |
| Australia | Eight territories; AGB; 2016 | Audit the cited forest reporting and the account/boundary territorial match. |
| Cameroon | Not individually identified in Annex D | Non-listing does not establish absence from calibration/FRA supplementation or independence. Trace the actual support. |
| France | No separate metropolitan-France row identified; “French Guyana” is a separate listed entry | Do not use an overseas entry as evidence for metropolitan France or solve the account-territory crosswalk by name alone. |

The ATBD's explicit plot-validation separation remains relevant: an inventory-support entry is not proof that the provider's validation plots were used in calibration. Conversely, an overlapping national aggregate is not made independent by being downloaded through a different portal.

### Admission decision

No hold is lifted and no permanent exclusion is added. Territorial reconciliation, endpoint-compatible forest support, national valid/zero/missing/converted coverage, uncertainty calibration and independent reference provenance remain required. The local seven-point/zero-2023-label gap is not closed by this methods document.

## 8. Priority revisions and next source readings

| Priority | Location in a future revision | Action |
|---|---|---|
| High | Main Methods §2.1; SI S3 | Add cross-year weight refinement and land-cover-specific exceptions; do not assume independent endpoints. |
| High | SI S8.2 and source-role metadata | Distinguish current GLAS/ICESat-2 structural roles, historical/diagnostic GEDI use, NFI/FRA statistics and withheld validation plots. |
| High | SI S2/S7/S8; support definitions | Separate training masks, output masks, merging overrides and analytical forest support; resolve the endpoint-mask rule. |
| High | Main uncertainty discussion; SI S3 | Add endpoint-specific bias, current-release versus earlier-release evidence, and missing change calibration. |
| Medium | Native-support terminology | Use zero-valued mapped estimates without discarding or relabelling valid zeros as missing/nonforest. |
| Medium | Allocation interpretation | State why a product retrieval maximum is not an independently justified subcell ecological bound. |
| Administrative | New revision's access register only | Mark this ATBD as read under the stated scope; retain F08's historical unread record unchanged. |

Proposed conventional article paragraphs are supplied in `PROPOSED_ARTICLE_TEXT_R01.md`. This review does not insert them into F08 or create F09.

The official index identifies the following **next documents**; their bodies were not reviewed in this R01:

1. [End-to-End ECV Uncertainty Budget v7](https://climate.esa.int/documents/3354/End-to-End_ECV_Uncertainty_Budget_E3B_V7.0.pdf), listed 17 December 2025 — trace which uncertainties and dependencies are propagated.
2. [Product Validation & Intercomparison Report v7](https://climate.esa.int/documents/3356/Product_Validation_Intercomparison_Report_PVIR_V7.0.pdf), listed 24 April 2026 — assess current-release bias, support and change-validation evidence; do not substitute the ATBD's v6 examples.
3. [Product Validation Plan v6](https://climate.esa.int/documents/3364/Product_Validation_Plan_PVP_V6.pdf), listed 22 December 2025 — audit plot selection, independence, spatial support and reference uncertainty.
4. [Algorithm Development Plan Change v7](https://climate.esa.int/documents/3371/Algorithm_Development_Plan_Change_ADPC_V7.0.pdf), listed 29 April 2026 — check any later modifications relevant to the pinned data release.

These are actual hyperlinks extracted from the official index, not invented file paths. Index access is not a successful full-PDF retrieval or a completed review of these documents.

### Page-addressed source parts

Page numbers above are original PDF/header page numbers, not page indices within a split part. The source register provides the complete mapping and SHA-256 digests.

- **A:** [PDF pp 91–105](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/091-105.pdf).
- **B:** [PDF pp 111–115](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/111-115.pdf).
- **C:** [PDF pp 116–120](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/116-120.pdf).
- **D:** [PDF pp 106–110](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/106-110.pdf).
- **E:** [PDF pp 46–60](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/046-060.pdf).
- **F:** [PDF pp 61–75](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/061-075.pdf).
- **G:** [PDF pp 76–90](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/076-090.pdf).
- **H:** [PDF pp 31–45](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/031-045.pdf).
- **J:** [PDF pp 16–30](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/016-030.pdf).
- **I:** [PDF pp 136–138, including Annex D](https://github.com/MIKEAA2020/general-sustainability/releases/download/external_pdf_follow_up_ecomod/136-138.pdf).
- [Official original ATBD v7 PDF](https://climate.esa.int/documents/3351/Algorithm_Theoretical_Basis_Document_ATBD_V7.0.pdf); [official document index](https://climate.esa.int/en/projects/biomass/key-documents/).

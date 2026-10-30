# Five-route source follow-up: Brazil, Indonesia, Finland and Canada

**Date:** 30 October 2026  
**Scope:** additive follow-up to the published [four-country deeper source audit](https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/deeper_source_audit_2026-10-30). The earlier audit, F15 and F16 are unchanged.

## Bottom line

All five requested routes were investigated directly. They materially improve the map from **available implementation** to **missing calibration evidence**, but they do not justify a new calibrated national above-ground biomass (AGB) comparison.

| Route | What was retrieved or verified | What it changes | Remaining evidence boundary |
|---|---|---|---|
| **Brazil C11 Caatinga code** | Complete pinned repository tree and all three C11 accuracy scripts | A real GEE → CSV generation route uses the same 85k reference asset, annual `CLASS_YYYY` fields and `PESO_AMOS` | No generated C11 microdata are in the repository; the Caatinga metrics script drops the weights and does not implement design covariance |
| **Indonesia `user-toolkit`** | Complete pinned tree and every active Indonesia product/territory definition | Exact inventory: **16 product assets + 24 territory assets**; authenticated GEE map/area export is available | No TVI/reference-design dataset is exposed; LULC stops at C4.1, not C5 |
| **Luke Report 6/2026** | 69-page PDF, Jukuri item/bundles, Appendix A, and corrected Report 12/2026 for comparison | Current Repola et al. (2025) model uncertainty and NFI sampling-covariance methods are documented; an existing Monte Carlo pipeline is identified | A2–A5 are examples, not complete national outputs; no same-domain national NFI12/NFI13 AGB endpoint/cross-inventory covariance is published |
| **Canada Reports Generator** | Both candidate URLs checked; current generator evidence carried forward from the reproduced audit | `/en/customized_report` works and provides `var_biom`; `/en/reportgenerator` returns 404 | Current dynamic and static-report versions must not be mixed; the change-RSE/variance relationship remains unresolved |
| **Canada v1.13 + Process 11b** | 40-page v1.13 and 29-page Business Process v8.0 PDFs | Process 11b documents successive-period change, imputation and variance aggregation | v1.13 is the **2004 Process 11a** reference, not the later **2006 fixed-panel Process 11b** procedure; that change procedure/current implementation is still needed |

## 1. Brazil: C11 code accesses reference data, but does not release or propagate the full design

The complete `mapbiomas/brazil-caatinga` tree was enumerated at commit [`852c7d7d30a2479a9b540cb180f2cbdd83cedd1c`](https://github.com/mapbiomas/brazil-caatinga/tree/852c7d7d30a2479a9b540cb180f2cbdd83cedd1c): 2,850 entries, including 65 Collection 11 blobs. The C11 validation directory contains:

- [`getCSVsPointstoAccGlobarlBacia_2col.py`](https://github.com/mapbiomas/brazil-caatinga/blob/852c7d7d30a2479a9b540cb180f2cbdd83cedd1c/lulc_30m_landsat/collection_11/src/validation/acuracia/getCSVsPointstoAccGlobarlBacia_2col.py)
- [`runAll_accuracy.py`](https://github.com/mapbiomas/brazil-caatinga/blob/852c7d7d30a2479a9b540cb180f2cbdd83cedd1c/lulc_30m_landsat/collection_11/src/validation/acuracia/runAll_accuracy.py)
- [`newsMetrics_AccuracySamples.py`](https://github.com/mapbiomas/brazil-caatinga/blob/852c7d7d30a2479a9b540cb180f2cbdd83cedd1c/lulc_30m_landsat/collection_11/src/validation/acuracia/newsMetrics_AccuracySamples.py)

### What the implementation does

Both exporters load:

`projects/mapbiomas-workspace/VALIDACAO/mapbiomas_85k_col5_points_w_edge_and_edited_v3`

They filter the Caatinga, request `CLASS_1985` through `CLASS_2025`, retain `BIOMA_250K`, `CARTA_2`, `DECLIVIDAD`, `PESO_AMOS`, `LON` and `LAT`, sample C11 classification/filter images at 30 m by basin, and export mapped/reference tables to the Drive folder `ptosAccCol11`. The C11 README describes 49 basins and this GEE → CSV validation workflow.

This is stronger than merely finding an accuracy appendix: it identifies executable code that **accesses and generates reference/mapped samples**. Two limitations are decisive:

1. **Actual 2025 coverage is unverified.** One script comments that 2025 is the final year of available reference points, but missing values are remapped to class 27. Without retrieving the GEE feature collection, the requested field and comment do not prove non-null 2025 labels. This also needs reconciliation with the C11 appendix’s assessed period through 2024.
2. **The inspected Caatinga metrics are not design weighted.** The exporter carries `PESO_AMOS`, but `newsMetrics_AccuracySamples.py` subsequently keeps only annual reference/classification columns plus `bacia`. Its `confusion_matrix`, `accuracy_score` and related calls have no `sample_weight`; `PESO_AMOS` does not occur in executable metrics code. The file also retains legacy `ptosAccCol10`/`Collection10` paths and output labels. It therefore cannot be identified as the official national C11 design estimator.

The pinned C11 tree contains **no CSV, XLSX, RDS, RDA or Parquet reference/accuracy outputs**. Anonymous retrieval of the GEE reference asset previously returned 401, so the implementation is confirmed but the microdata were not retrieved. This is an access limitation, not proof that the reference panel does not exist.

**Conclusion:** use this code to specify an exact export/provider request, not as a substitute for reference microdata or design covariance. The separate national `brazil-accuracy` C110 workflow and this biome-level Caatinga workflow must not be conflated. Machine-readable audit: `evidence/brazil_caatinga_c11_code_audit.json`.

## 2. Indonesia: the toolkit exposes maps, transitions, fire layers and territories—not TVI reference data

The complete `mapbiomas/user-toolkit` tree was enumerated at commit [`332116ce61841f57b175f19ac78b6b0ef1d12c7f`](https://github.com/mapbiomas/user-toolkit/tree/332116ce61841f57b175f19ac78b6b0ef1d12c7f): 335 entries, not truncated. All active Indonesia definitions were extracted directly from `data/collections-lulc.js`, `data/collections-fire.js` and `data/territories.js`.

### Exact active inventory

| Product | Collections and assets | Periods defined in the toolkit |
|---|---|---|
| **LULC C1** | integration, transitions, quality | Coverage/quality 2000–2019; annual and multi-year transitions |
| **LULC C2** | integration, transitions, quality | Coverage/quality 2000–2022; annual and multi-year transitions |
| **LULC C3** | integration, transitions, quality | Coverage/quality 2000–2024; annual and multi-year transitions |
| **LULC C4.1** | one integration/coverage asset only: `projects/mapbiomas-public/assets/indonesia/lulc/collection4_1/mapbiomas_indonesia_collection41_coverage_v1` | 1988–2024; no C4.1 transitions or quality asset defined |
| **Fire C1** | annual burned, annual burned coverage, monthly burned, accumulated burned, accumulated burned coverage, fire frequency | Annual/monthly 2013–2023; accumulated/frequency periods through 2023 |
| **Territories** | 24 FeatureCollections: Country Limit, District, Forestry Concession, Indigenous Forest, Island Group, Key Biodiversity Area, Mining Concession, Moratorium Area, National Park, New National Capital, Oil Palm Concession, Orangutan Habitat, Other Conservation Area, Peatland Area, Province, Restoration Area, Rhino Habitat, Social Forestry Area, Sub-District, Sumatran Elephant Habitat, Sumatran Tiger Habitat, Village, Wallacea and Watershed | Region-of-interest summaries, not temporal reference labels |

That is **10 LULC + 6 Fire = 16 product assets**, plus **24 territory assets**. The toolkit’s test snapshots demonstrate 30 m GeoTIFF map export and CSV area export to Drive for the default Indonesia LULC C4.1 and Fire C1 flows. These are useful programmatic data-access routes.

The complete tree contains no path labelled accuracy, validation, reference, TVI, sample, weight, covariance, variance, design or stratification; the active Indonesia product definitions contain no such asset. **No C5 definition is present.** Thus the toolkit does not expose the independent TVI panel, reference weights or design covariance needed for C4.1/C5 calibration.

Two access distinctions matter:

- The toolkit’s `https://indonesia.mapbiomas.org/downloads/` hyperlink returns **404**. That is an outdated hyperlink, not evidence that the underlying map assets do not exist.
- Anonymous Earth Engine metadata retrieval for the C4.1 asset returned **401 credentials required**. The source files explicitly say listed assets are intended for public read access, but the REST route still requires authentication. This is not proof that the map is unavailable inside an authenticated Earth Engine session.

Full asset IDs and every period are in `evidence/indonesia_toolkit_inventory.csv` and `.json`.

## 3. Finland: Report 6/2026 identifies a current-model simulation route, not a published national endpoint matrix

The requested [Report 6/2026 PDF](https://jukuri.luke.fi/server/api/core/bitstreams/21079752-c79d-4e1b-aaf7-d83c35181d17/content) was retrieved successfully:

- 69 PDF pages; 4,368,237 bytes
- SHA-256 `6772ee26402835a2459223077d922d75e0327518b12ed722e868b6286c24a421`
- ISBN 978-952-419-152-4; [Jukuri record](https://jukuri.luke.fi/handle/11111/103795)

### Edition control: do not count the same analysis twice

[Report 12/2026](https://jukuri.luke.fi/handle/11111/103806) is the **corrected second edition of the same report**, not an independent source. Its notice says that it corrects the last-column values of Table 1 on printed page 9. A page-by-page text comparison found differences only on PDF pages 3, 5 and 10 after running-header normalization; **Appendix A on PDF pages 62–68 is text-identical**. The Appendix A evidence is therefore cited once, preferably to corrected Report 12/2026, while Report 6/2026 remains preserved as the user-supplied first edition.

### What Appendix A contributes

Appendix A updates the **mineral-soil litter-input uncertainty analysis** through 2023 using the new Repola et al. (2025) biomass models. It includes:

- **A1:** current model equations;
- **A2:** an illustrative pine model 2b parameter matrix, with diagonal `U,%` and off-diagonal correlations;
- **A3–A4:** illustrative pine model 2b stand random-component and tree-residual SD/correlation matrices;
- **A5:** an illustrative matrix for **one NFI13 sampling region**, covering above-ground BCEF and stem-volume estimates, again with diagonal `U,%` and off-diagonal correlations;
- **Figure A2:** graphical 95% biomass intervals for NFI13 sampling region 1 on mineral soils, separating model-parameter and NFI-sampling effects;
- **Figure A3:** extreme examples of simulated annual biomass time series, not a complete national output.

The text says corresponding uncertainty matrices **including below-ground components** were estimated separately for every VMI8–VMI13 cycle and sampling region on each Monte Carlo iteration, with corresponding harvest-removal and natural-mortality BCEF matrices. Steps 5–7 estimate sampling covariance, simulate biomass, interpolate NFI-cycle estimates annually and aggregate over South/North Finland sampling regions.

This is a substantive improvement over saying that current-model uncertainty information is unavailable. It also identifies a feasible provider-computed route: the existing pipeline may be able to supply machine-readable biomass simulations or the required endpoint covariance without releasing plot locations.

### What it still does not establish

Tables A2–A5 are explicitly **examples**. Their diagonal entries are `U,%` or SDs and their off-diagonal entries are correlations; they are not ready-made national covariance matrices and were not silently converted. Jukuri contains only the PDF, an extracted-text derivative and a thumbnail—no supplementary matrices or simulation files.

Most importantly, Appendix A’s target is mineral-soil litter-input uncertainty. It does **not** print a same-domain national NFI12/NFI13 AGB endpoint variance/cross-inventory covariance deliverable. Finnish volume uncertainty cannot substitute for biomass uncertainty, and the report’s Monte Carlo description cannot be treated as delivery of the national endpoint matrix.

All 174 printed lower-triangle cells from A2–A5 are preserved with value types in `evidence/finland_luke_appendix_A_examples_as_printed.csv`; an independent parser confirmed **174/174 exact matches against each edition’s extracted source text** (`evidence/finland_transcription_verification.json`). The edition and estimand assessment is in `evidence/finland_luke_report_assessment.json`.

## 4. Canada: the working generator is a valid `var_biom` route, with version boundaries

The supplied `https://nfi.nfis.org/en/reportgenerator` returns **404**. The working public Reports Generator is:

**https://nfi.nfis.org/en/customized_report**

The earlier reproduced audit already downloaded the current national/ecozone generator JSON containing `var_biom`. It found:

- all **58** national/ecozone `var_biom` sums matched exactly after correcting the ecozone index;
- current forest biomass-change point estimates sum to **19.066 million t**, not the static report’s 17.639 million t;
- `sep_biom` reproduces generator RSE within 0.02 percentage points in **53/57** stock cells but only **1/57** change cells;
- the change-cell `var_biom` sum is therefore a diagnostic input, not permission to choose between the printed RSE, interval and variance-derived uncertainty.

These results remain in the original audit’s `data/canada_wrt/` and `evidence/canada_generator_*` files. Current dynamic outputs and static-report versions must not be mixed. Table 17C.0/18C.0 discrepancies remain unresolved; no preferred SE is selected and no 95% interval is certified here.

## 5. Canada: v1.13 and Process 11b are different documents with different roles

The requested [Estimation Procedures v1.13](https://nfi.nfis.org/resources/estimation/Estimation_procedures_v1.13.pdf) was retrieved: 40 pages, dated **3 September 2004**, SHA-256 `abdb0b35d995dfd596941e0a9aaabba00091d41d3629e282378a58c1f609170a`. Its contents cover area/attribute totals and associated variances from photo, ground and combined plots, including ratio estimation and aggregation. It does not supply the fixed-panel biomass-change covariance implementation.

The [NFI Business Process v8.0](https://nfi.nfis.org/resources/general/NFI-Business-Process-Version-8.0.pdf), dated **31 March 2021**, was also retrieved (29 pages; SHA-256 `2658954ed468591fd56c7f247010b418fc4cf2892a320dd674de05df2715b55b`). It makes the roles explicit:

- **Process 11a** covers baseline/re-measurement attribute totals, averages and variances and cites **v1.13 (2004-09-03)**.
- **Process 11b** covers annual/periodic area, volume and biomass change from combined photo plots measured in successive periods (for example T0/T1). It describes a temporally indifferent ratio estimator, projection or multiple imputation for non-remeasured plots, and summation of AOI totals and associated variances. It cites **Change Estimation Procedures based on Fixed Annual Panels v1.08 (2006-08-08)** and Magnussen et al. (2017).
- **Process 12a** says static standard reports are pre-generated through the Published NFI Reporting Database and identifies `/en/customized_report` as the dynamic reporting tool.

Consequently, **v1.13 is earlier in time and is not a newer replacement for v1.08**, despite the higher version number. The missing fixed-panel document or its current superseding implementation, version-matched full-precision outputs and covariance rules remain necessary.

## Evidence use and next actions

The correct sequence remains:

**confirm product/reference version and estimand → obtain reference-design outputs or aggregate covariance → reproduce the provider estimator → only then attempt national AGB calibration.**

The narrowed, copy-ready provider requests are in `provider_requests_update.md`. They focus on existing implementation outputs rather than asking providers for unspecified new analyses:

- Brazil: the exact C11 reference export or provider-computed design matrices/covariance, actual year coverage and the official weighting workflow.
- Indonesia: C4.1/C5 reference-vintage statement and independent TVI/transition covariance, not more map downloads.
- Finland: existing full Appendix A matrices or step-7 simulations, and same-domain NFI12/NFI13 AGB endpoint/cross-inventory covariance.
- Canada: fixed-panel change implementation and version-matched `var_biom`/`sep_biom`/interval formulas and covariance rules.

No country is advanced to a new calibrated national AGB comparison by this follow-up alone.

## Package guide and local-only documents

- `evidence/retrieval_ledger.csv`: 20 retrieval, access and absence checks.
- `evidence/source_files.csv`: 44 pinned source files with URLs, byte counts and SHA-256 hashes.
- `evidence/local_source_documents.csv`: four preserved PDFs and their local-only status.
- `scripts/retrieve_followup_sources.py`: public retrieval at pinned versions.
- `scripts/audit_brazil_caatinga.py`: repeatable static C11 code audit.
- `scripts/extract_indonesia_toolkit_inventory.js`: exact active-asset extraction with count assertions.
- `scripts/build_finland_appendix_examples.py`: transcription builder preserving printed value types.
- `scripts/verify_finland_transcription.py`: independent 174-cell comparison with both editions’ extracted text.
- `scripts/validate_package.py`: offline package QA.
- `evidence/package_qa.json` and `evidence/package_manifest.csv`: validation and payload integrity.

The four requested/comparison PDFs are preserved in the separate local vault:

`/home/user/source_followup_documents_2026-10-30/`

They are **not redistributed to GitHub**. The public addendum contains only audit text, derived factual inventories/transcriptions, hashes and original reproduction scripts.

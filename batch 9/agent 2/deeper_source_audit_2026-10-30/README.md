# Deeper source audit: Brazil, Indonesia, Finland and Canada

**Search and retrieval completed:** 30 October 2026  
**Scope:** current reference-design data, Finnish biomass-design variance, and Canada’s uncertainty implementation  
**Manuscript impact:** none. Published F15/F16 remain untouched; this audit adds **zero calibrated national AGB comparisons**. The eight primary calibrated national AGB analyses remain incomplete.

## Executive finding

The deeper search retrieved substantial new official material, but it did not justify treating newer maps or higher reported accuracy as compatible calibration evidence.

| Country | What was actually retrieved | Status against the required estimand | Remaining provider-dependent item |
|---|---|---|---|
| **Brazil** | Current **Collection 11 Accuracy Assessment Appendix v1 (August 2026)**; current C110 code/design repository; all public validation downloads; a 2025 transition-quality article | Current methods are available, but public microdata remain **Collection 9**. No current C11 annual/transition design covariance was located | Exact C11 reference panel, design roles/weights and annual/adjacent-year covariance, or provider-computed equivalents |
| **Indonesia** | Current **Collection 4.1 ATBD v1 (February 2026)**; official accuracy page and Collection 2 Shiny app; C4 repository scripts; current C5 map platform | The only detailed independent annual TVI panel found is **12,957 samples, 2000–2022, first used for Collection 2**. C5 maps do not establish C5 reference data | Explicit C4.1/C5 reference-vintage statement and the independent TVI panel or annual/transition design covariance |
| **Finland** | Full **579-page March 2026 EU NID**; NFI13 design article/supplements; corrected Luke 12/2026 report | **Biomass-specific design evidence improved materially:** Table 6.4-13 gives 2014–2023 stock-change estimates with 95% NFI-sampling-only CIs. It is still an old-model annualized change estimand, not NFI12/NFI13 endpoint covariance | Same-domain NFI12/NFI13 AGB endpoint variances **and cross-inventory covariance**, plus current Repola et al. (2025) model/prediction covariance |
| **Canada** | All national and terrestrial-ecozone Tables 15C/17C/18C point/RSE/CI CSVs; Estimation Procedures v1.13; Business Process v8.0; live N3WRT point/RSE/CI/`var_biom` outputs | The issue is now isolated to **change-specific RSE/implementation fields**. Static CI rollups and stock controls work; static change RSEs do not. Current generator `var_biom` is additive but belongs to a different output version | Fixed-panel v1.08/current implementation and version-matched full-precision static/generator derivations; no authoritative repair yet |

**Bottom line:** no country should advance to a calibrated national AGB comparison on the currently retrieved evidence alone. Finland now has a legitimate biomass-design sensitivity source; Canada has a much sharper implementation diagnostic; Brazil and Indonesia still need version-matched reference-design outputs.

---

## 1. Brazil: current design documentation exists, but public reference files are older

### Retrieved current evidence

The official [**Accuracy Assessment Appendix, Collection 11, Version 1 (August 2026)**](https://brasil.mapbiomas.org/wp-content/uploads/sites/3/2026/08/Accuracy-Assessment-Appendix-Collection-11-v1.pdf) is a valid 19-page PDF:

- bytes: **2,094,356**;
- SHA256: `d7a8264b5a10f25eeec69ad5d90856922bf053059e3457a1804ee506cee97795`;
- scope: **85,152 annually interpreted samples**, including **10,000 Amazon training samples** and **75,152 accuracy samples per year**;
- design: **127 grouped-chart units × six slope strata**, with filtering, interpreter-agreement/missing-data weight adjustments and legend harmonization;
- results: annual class/biome accuracy for **1985–2024**.

This is the correct current methods document. It is not the underlying reference panel and does not provide the cross-year covariance required for endpoint or transition calibration.

The current implementation repository was also retrieved: [`mapbiomas/brazil-accuracy`, C110 at `c7a20e5…`](https://github.com/mapbiomas/brazil-accuracy/tree/c7a20e5e892495d98603183937a2e6926d558cfc/src/collection_110). The design files were introduced at commit `8cad5dbd80bb4aaae52e032213ff7d9b82aac56f`; the R accuracy script was last changed at `c7a20e5e892495d98603183937a2e6926d558cfc`. The repository has only `main`, with no tags or releases.

### What the public files actually contain

The [official validation-download page](https://brasil.mapbiomas.org/downloads/pontos-de-validacao/) now describes interpretation through 2024 in its narrative, but every listed downloadable item is explicitly labelled **Collection 9**:

- [CSV ZIP](https://brasil.mapbiomas.org/wp-content/uploads/sites/4/2024/08/mapbiomas_85k_col2_1_points_w_edge_and_edited_v1.csv_-1.zip);
- [XLSX](https://brasil.mapbiomas.org/wp-content/uploads/sites/4/2024/08/mapbiomas_85k_col2_1_points_w_edge_and_edited_v1-2.xlsx-2.xlsx);
- [vector ZIP](https://brasil.mapbiomas.org/wp-content/uploads/sites/3/2026/10/mapbiomas_85k_points_validation.zip).

Parsing the files, rather than relying on their descriptions, showed:

- **85,152 rows** and 135 CSV columns;
- `CLASS_2022` is populated for all 85,152 rows;
- only **4,053** rows have nonempty `CLASS_2023` and `ID_REVISAO`;
- the vector’s last annual class field is `CLASS_2022`;
- after parsing decimal commas, `PESO_AMOS × PROB_AMOS_ = 1` for all 85,152 rows to floating precision (maximum absolute deviation `7.44×10⁻¹³`);
- 9,999 rows carry the public training flag `AMOSTRA_AM = 1`.

The vector ZIP’s October 2026 web path does not make its content current: its internal shapefile/DBF timestamps are **30 August 2023**, and its fields end in 2022.

A naive reconstruction of strata from public `CARTA_2 + DECLIVIDAD` disagrees with the repository `points_strata.csv` for **25,793** samples. This does **not** propagate through the C110 R workflow, because that workflow joins the repository crosswalk. It does mean that the public fields must not be used to invent current strata.

### Access failure and compatible workaround

C110 names GEE asset [`projects/mapbiomas-workspace/VALIDACAO/mapbiomas_85k_col5_points_w_edge_and_edited_v3`](https://code.earthengine.google.com/?asset=projects/mapbiomas-workspace/VALIDACAO/mapbiomas_85k_col5_points_w_edge_and_edited_v3). Anonymous retrieval returned **HTTP 401**. That is a retrieval failure, not proof of private status; authenticated access and a field/version audit are still required.

[Matos et al. (2025)](https://doi.org/10.1080/17538947.2025.2528604) is a genuine transition-quality workaround, but it uses **Collection 9/public v2.1 reference data for 1985–2022**. It can support a historical sensitivity analysis, not current C11 calibration.

### Judgment

**Retrieved:** current methods, current code, older public microdata and a historical transition study.  
**Not retrieved:** complete current C11 reference labels, final design roles/weights and annual/transition covariance.  
**Required next evidence:** the exact C11 panel or provider-computed design-weighted annual and adjacent-year matrices with covariance. Overall, user or producer accuracy is insufficient. The copy-paste request is in `provider_requests.md`.

---

## 2. Indonesia: current ATBD retrieved; independent reference vintage remains unresolved

### Retrieved current evidence

The official [**ATBD MapBiomas Indonesia Collection 4.1, Version 1 (February 2026)**](https://landy.mapbiomas.id/assets/files/ATBD%20Mapbiomas%20ID%20Col%204.1%20EN.pdf) is a valid 31-page PDF:

- bytes: **7,025,035**;
- SHA256: `3f20e45951e154639b87eefdae120bb8a1df6c45348515b448d85ccf0630d074`;
- map scope: **1990–2024**;
- independent validation: described as periodic, **every two collections**;
- detailed sample evidence: **12,957 independent TVI samples**, first implemented in Collection 2 and labelled annually for **2000–2022**;
- design: seven geographic regions × six SRTM slope classes = **42 strata**, minimum 500 samples per region, 95% confidence and ±3% target margin with Bonferroni correction;
- interpretation: 15 three-person teams, at least two interpreters agreeing, followed by expert supervisor consolidation.

The phrase “every two collections” makes the reference vintage for C4/C4.1/C5 a real question; it does not prove that a new C4 or C5 panel exists. The [official accuracy page](https://landy.mapbiomas.id/en/accuracy-assessment) and its embedded [Collection 2 Shiny application](https://mapbiomas-network-accuracy.shinyapps.io/MapBiomas_Indonesia_Col2_Acc_EN/) still present Collection 2 accuracy for 2000–2022. The exposed interface provides annual overall/per-class accuracy, allocation/area disagreement and commission/omission summaries, not the required design covariance.

The [Landy repository at `a957d729…`](https://github.com/mapbiomas-indonesia/MapBiomas-Indonesia---Landy/tree/a957d72992d90ed5a4787ce13c8a36b7a1b48780) contains C4 accuracy scripts. Those scripts use static-reference classifier-validation assets. Two anonymous asset requests returned HTTP 401:

- [`mbi_c4_primary_sample_raw_IDN-points_v1`](https://code.earthengine.google.com/?asset=projects/mapbiomas-indonesia/COLLECTION4/Basic_Class_Col4/02_sample/01_primary_sample/01a_primary_sample_raw/mbi_c4_primary_sample_raw_IDN-points_v1);
- [`mbi_c4_primary_sample_raw_smaller_scope_IDN-points_v1`](https://code.earthengine.google.com/?asset=projects/mapbiomas-indonesia/COLLECTION4/Basic_Class_Col4/02_sample/01_primary_sample/01a_primary_sample_raw/mbi_c4_primary_sample_raw_smaller_scope_IDN-points_v1).

Even if authenticated access succeeds, those classifier-validation assets cannot replace independent annual TVI labels and design weights.

Finally, the [official platform](https://plataforma.mapbiomas.org/coverage/coverage_lclu?t%5BregionKey%5D=indonesia) serves **Collection 5 maps through 2025**. That establishes map availability only; no official C5/C4.1 independent reference-microdata release was located.

### Judgment

**Retrieved:** current C4.1 methods, aggregate C2 accuracy interface, C4 classifier-validation implementation and current C5 maps.  
**Not retrieved:** a version-matched C4.1/C5 independent annual TVI reference panel, design weights and transition/endpoint covariance.  
**Required next evidence:** first an explicit statement of which reference panel supports C4.1/C5, then that panel or provider-computed annual/transition design covariance. The exact request is in `provider_requests.md`.

---

## 3. Finland: biomass-design evidence found, but endpoint covariance is still missing

### Current official report retrieved

The full March 2026 EU NID was downloaded from EIONET:

- [EIONET envelope](https://cdr.eionet.europa.eu/fi/eu/govreg/inventory/envasbzqa/);
- [direct PDF](https://cdr.eionet.europa.eu/fi/eu/govreg/inventory/envasbzqa/FI_NID_EU_2024_2026_03-15.pdf);
- **579 pages, 13,479,206 bytes**;
- SHA256 `8f9a3b411183c9366df882fb8013000cff73e42b26c14fe52787b309c41be04c`.

This is a successful retrieval of current official evidence, not a provider referral.

### 3.1 Current biomass-change uncertainties

Section 6.4.3.1 and Tables 6.4-9–6.4-11 report for 2024:

| Component | Change | Uncertainty \(U\), twice relative SE |
|---|---:|---:|
| Increment | 69.796 Tg/a | 1.4% |
| Fellings | −57.684 Tg/a | 5.3% |
| Natural losses | −4.630 Tg/a | 9.9% |
| Net living-biomass change | 7.481 Tg | 43.1% |
| Model uncertainty for net change | 7.481 Tg | 3.83% |
| Combined sampling/model uncertainty | — | 43.3% |
| Tree-biomass carbon change in Table 6.4-11 | 2.893 Mt C | 43.3% |

Two qualifications are essential:

1. These are **change uncertainties**, not national AGB endpoint variances/covariances.
2. The 43.1% “sampling” uncertainty for net change includes an assumed **5% uncertainty in commercial-removal statistics**. It is therefore not a pure NFI design variance.

### 3.2 New biomass-specific design evidence: Table 6.4-13

Pages 352–354 state that 95% confidence intervals for annual stock-change estimates include **NFI sampling uncertainty and exclude other uncertainty sources**, using the standard Finnish NFI approach. Table 6.4-13 supplies 2014–2023 gain–loss values, stock-change values and lower/upper CIs.

For example, the 2023 row is transcribed exactly as:

- gain–loss: `7 292`;
- stock change: `3 644`;
- 95% CI: `−1 739` to `9 026`.

The heading says `Tg/a`, but `7 292` is exactly 1,000× the 2025 submission’s 7.292 Tg/a. This is a **printed-unit inconsistency to clarify**, not permission to rescale the table silently. All ten rows are preserved without unit conversion in `evidence/finland_nid_2026_table_6_4_13_as_printed.csv`.

This table is useful biomass-specific design evidence. It remains insufficient for the target comparison because the surrounding text says the stock-change estimates use the **old Repola (2008/2009) models**, the gain–loss values come from the **2025 submission**, and the estimand is annualized change—not NFI12/NFI13 endpoint covariance.

### 3.3 A feasible design route, without substituting volume SEs

The [NFI13 article, Korhonen et al. (2024)](https://www.silvafennica.fi/article/24045), §§2.3.2–2.3.3, documents biomass estimation and the sampling-variance approach: cluster-level ratio estimation, a modified Grafström–Schelin local/Voronoi-neighbour variance estimator, aggregation over regions/strata and delta-method total estimation. The supplements provide biomass point estimates, but no national biomass endpoint SE or cross-inventory covariance.

This creates a feasible provider-computed route that does not require exact plot locations: Luke can supply same-domain NFI12/NFI13 AGB estimates, their region/stratum design-variance contributions and the shared-permanent-panel covariance contributions. Two independent endpoint SEs would not be enough.

### 3.4 Current-model uncertainty remains version-mismatched

Current NID estimates use **Repola et al. (2025)**, cited on page 517 as:

> Repola, J., Heikkinen, J., Mehtätalo, L., Lehtonen, A., Kangas, A. & Sarkkola, S. 2025. *Tree level biomass models for Finland.* Manuscript.

No public manuscript/full covariance was located. Appendix 6d documents model forms, but §6.4.3.1 and Appendix 6g still calculate model uncertainty from the simplest **old Repola 2008/2009** models. A current national calibration therefore needs the 2025 model’s fixed-effect, random plot/tree and residual covariance, or provider-computed prediction covariance.

The [April UN NID landing page](https://unfccc.int/documents/656427) and [direct UN PDF](https://unfccc.int/sites/default/files/resource/FI_NID_UNFCCC_BTR2_2024_2026-04-15.pdf) remain separate identifiers. Direct retrieval was blocked by site protection; the March EU file must not be assumed byte-identical to the April UN version.

### Judgment

**Retrieved:** current official biomass-change uncertainties, biomass-specific NFI-sampling-only stock-change CIs, and the design estimator needed to formulate a precise aggregate request.  
**Not retrieved:** national same-domain NFI12/NFI13 AGB endpoint variances with cross-inventory covariance, or current Repola et al. (2025) full model/prediction covariance.  
**Required next evidence:** those exact outputs, with Table 6.4-13 units/version clarified if its CIs are used for sensitivity analysis. Volume SEs remain inadmissible substitutes.

---

## 4. Canada: the discrepancy is now isolated, not resolved

### 4.1 Static national/ecozone audit

All national (`CA`) and terrestrial-ecozone (`NFI`) point, RSE and interval CSVs for Tables 15C, 17C and 18C were retrieved from the [standard reports](https://nfi.nfis.org/en/standardreports). The file-level URLs and SHA256 hashes are in `evidence/canada_source_files.csv`.

For each table, national values were compared with root-sum-of-squares (RSS) rollups of the 12 ecozone subtotal rows. RSE-derived SEs use `abs(point) × RSE/100`; interval files contain half-widths.

| Table / estimand | National point | Published RSE | Ecozone RSE-derived rollup as % of national point | National CI half-width | Ecozone CI-halfwidth RSS | Implied national multiplier |
|---|---:|---:|---:|---:|---:|---:|
| 15C stock | 51,073.563 | 0.74% | 0.7348% | 738.088 | 738.0875 | 1.9529 |
| 15C change | 222.443 | 1.17% | **5.6655%** | 65.603 | 65.6030 | **25.2069** |
| 17C stock | 30,525.199 | 0.70% | 0.6978% | 418.4005 | 418.4007 | 1.9581 |
| 17C change | 17.639 | 1.16% | **26.7597%** | 38.918 | 38.9184 | **190.2035** |
| 18C stock | 30,525.199 | 0.68% | 0.6782% | 406.4745 | 406.4739 | 1.9582 |
| 18C change | 17.639 | 1.10% | **21.2970%** | 38.611 | 38.6105 | **198.9960** |

The interpretation is specific:

- point sums agree to rounding;
- **all six** ecozone CI-halfwidth RSS rollups reproduce the national interval to rounding;
- all three **stock** RSE rollups agree with national RSEs to rounding;
- all three **change** RSE rollups fail badly;
- therefore the problem is not a generic inability to aggregate NFI uncertainty; it is concentrated in the change-RSE implementation/fields.

For Table 17C.0, applying the published RSE to the published point gives SE `17.639 × 0.0116 = 0.2046124` million tonnes, whereas the interval half-width is 38.918. Their ratio is 190.203526, not a plausible normal/t multiplier. This does **not** justify selecting a different SE or declaring a confidence level.

### 4.2 Current N3WRT generator evidence

The public [Reports Generator](https://nfi.nfis.org/en/customized_report) exposes current class-35 outputs through N3WRT. Exact retrieval queries are preserved in `scripts/retrieve_canada_wrt.py`; snapshots and offline diagnostics are included in this package.

Results:

- **58 national class cells**, including **45 forest-land cells**;
- for every one of the 58 change cells, ecozone `var_biom` values sum to national `var_biom` to floating precision, with no missing keys;
- stock `sep_biom` agrees with `sqrt(var_biom)`-derived RSE in **53 of 57** nonzero cells within 0.02 percentage points;
- change `sep_biom` agrees in only **1 of 57**;
- generator CI endpoints imply an empirical multiplier around **1.965**, but this applies only to the generator output;
- current forest-land change points sum to **19.066 million tonnes**, not static Table 17C.0’s **17.639**;
- the current forest-cell `var_biom` sum implies SE **21.440613 million tonnes**, or **112.45%** of 19.066.

The additive `var_biom` field is therefore useful implementation evidence. It is **not** a version-matched repair for static Table 17C.0, and the 112.45% current-generator value must not be substituted for the static 1.16% or vice versa.

### 4.3 Missing implementation document

[Estimation Procedures v1.13](https://nfi.nfis.org/resources/estimation/Estimation_procedures_v1.13.pdf) supplies area-total formulas, not the current fixed-panel biomass-change implementation. [Business Process v8.0](https://nfi.nfis.org/resources/general/NFI-Business-Process-Version-8.0.pdf) cites the needed document exactly:

> *Change Estimation Procedures based on Fixed Annual Panels*, **Version 1.08, 2006-08-08**.

That document or its current superseding implementation was not located publicly. The provider request therefore asks for the document, version-matched full-precision outputs, the `sep_biom`/`var_biom`/interval formulas, the fixed-panel covariance rules and the documented 200% RSE cap.

### Judgment

**Retrieved:** enough public evidence to localize the problem and rule out a generic stock/aggregation failure.  
**Not retrieved:** an authoritative version-matched derivation that reconciles static change point/RSE/CI fields or permits transferring current generator variance to the static report.  
**Required next evidence:** fixed-panel implementation and provider reconciliation. The smaller uncertainty must not be chosen by convenience.

---

## 5. Which workarounds are admissible now?

| Candidate workaround | Admissible use | Not admissible for |
|---|---|---|
| Brazil Matos et al. (2025), public v2.1/C9 transitions | Historical transition-error sensitivity through 2022 | Claiming current C11 design calibration |
| Indonesia Collection 2 Shiny accuracy summaries | Descriptive checks of reported annual/per-class accuracy | C4.1/C5 endpoint or transition covariance |
| Finland NID Table 6.4-13 | Biomass-specific, old-model annual stock-change design sensitivity **after unit/version clarification** | NFI12/NFI13 national AGB endpoint covariance |
| Canada current generator `var_biom` | Generator-only internal consistency and implementation diagnostics | Certifying or repairing static Table 17C.0 across versions |
| Newer Brazil/Indonesia map releases or higher overall accuracy | Map-version description | Compatible reference-design calibration |

The correct topological sequence is: **confirm product/reference version and estimand → obtain design labels/weights or aggregate covariance → reproduce the provider estimator → only then attempt national AGB calibration**.

## 6. Package and reproduction

- `provider_requests.md`: exact copy-paste requests and links for provider-dependent items.
- `evidence/retrieval_ledger.csv`: 25 source-level retrieval/status/compatibility records.
- `evidence/canada_source_files.csv`: direct URLs, bytes and SHA256 for all 39 packaged Canada snapshots.
- `evidence/canada_static_rollup_summary.*`: six national/ecozone static diagnostics.
- `evidence/canada_generator_summary.json` and `canada_generator_cell_diagnostics.csv`: current generator results.
- `evidence/canada_ecozone_to_national_variance_rollup.csv`: all 58 key-level variance checks.
- `evidence/finland_nid_2026_table_6_4_13_as_printed.csv`: all ten printed rows without rescaling.
- `evidence/brazil_public_reference_audit.json`: parsed public-file diagnostics.
- `data/`: small public Canada CSV/JSON snapshots only; no copyrighted provider PDFs are redistributed.

Run the offline Canada verification:

```bash
python scripts/run_canada_diagnostics.py
```

Expected result: **11/11 assertions pass**. The network refresh is deliberately separate:

```bash
python scripts/retrieve_canada_wrt.py  # requires requests; live outputs can change
python scripts/run_canada_diagnostics.py
```

A refreshed live generator output must be treated as a new version, not silently substituted for the static tables or the snapshots used here.

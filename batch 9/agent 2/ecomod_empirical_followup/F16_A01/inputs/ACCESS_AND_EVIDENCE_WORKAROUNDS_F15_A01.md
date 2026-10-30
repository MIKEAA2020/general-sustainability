# Access routes and evidence-gap workarounds — F15 audit

Checked 30 October 2026. “Accessible” means a source or document can be obtained; it does not mean that its estimand, period, support and uncertainty are compatible with the primary 2015–2023 forest-AGB target. Provider files named here are not redistributed in this package.

## 1. Small files that can be fetched now

| Priority | Source and direct link | What it provides | What it does **not** establish |
|---|---|---|---|
| 1 | **JRC Tropical Moist Forest country CSV:** https://forobs.jrc.ec.europa.eu/static/tmf/JRC_TMF_EvolutionChanges_1990_2025_vFebruary2026.csv | Annual country statistics for 1990–2025: undisturbed/degraded tropical moist forest, deforestation, degradation and regrowth. Retrieved successfully: 661,961 bytes, 4,089 data rows, SHA-256 `4302f67b735bac39f2c038c1444018002a6983afe68a134b3cca00cfd461bd5f`. Units are Mha according to the official FAQ. | It covers the TMF domain, not all national forest or AGB. Annual disturbances are not unique endpoint conversion. Recent-year degradation/deforestation separation and valid-observation limitations remain. It is an additional physical source, not calibration of MapBiomas or a biomass change interval. |
| 1 | **Australia forest-attribute CSV:** https://data.gov.au/data/dataset/c426860e-9b55-404e-9892-e975794018d5/resource/849a0d00-577a-4eb2-b77f-4d63264201ae/download/aus_for23_attributes.csv | Official Data.gov.au mirror of the Forests of Australia (2023) raster attribute table: 45,329 bytes, 687 data rows, SHA-256 `ff44e7b815ac1a2f4ca7f181ef84e6664acfddc3c909fb71722f94660898743c`; fields include forest category/type, forest flag, state and pixel count. Retrieved successfully. | The dataset reference period is 2016–2021, not a 2015–2023 pair. Pixel counts require the raster grid/area definition for area conversion. It is not an AGB or independent change-validation product. |
| 1 | **Finland NFI12 supplement:** https://www.silvafennica.fi/supp_files/article10662/S2.xlsx and **NFI13 supplement:** https://www.silvafennica.fi/supp_files/article24045/S2.xlsx | Official workbooks retrieved successfully (540,761 and 457,259 bytes; SHA-256 `07dbb5f1c36b1611868785fa0111f6e417d5b5bdc3c68d11aee903a53227df31` and `2d43270c38a487dee504a09da2ea3b8c585a3bbaa0587769bb3a26003d0a51d5`). NFI12 sheet 27 and NFI13 Table 60 provide biomass by component/species/region; the volume sheets retain their standard errors. | The biomass tables have no biomass standard-error columns. Volume SEs cannot be transferred to biomass. These files do not supply exact annual 2015/2023 endpoints or remove cycle/target differences. |
| 2 | **France 2024 methodology:** https://inventaire-forestier.ign.fr/IMG/pdf/methodologie-2024.pdf | Retrieved successfully: 14,683,729 bytes, 44 pages, SHA-256 `4987b8dcf1b62679229f5fe02a98131741fe4d4f6225c0b11bfe0d7d3bba2f4f`. PDF p.17 confirms deduction of unusable wood in published results unless stated otherwise; p.5 explains pooled five-campaign windows and interpretation of changes. | This narrows a documentation question for the 2019–2023 edition; it does not prove identical retrospective cubage/protocol treatment across all four windows or bound differential bias. |
| 2 | **Cameroon 2026 forest reference-level submission:** https://redd.unfccc.int/media/cmr_nrf_zero_final_20janvier2026_f.pdf | The official document describes 29,409 Collect Earth Online plots on a systematic 4 km grid, annual land-use data through 2023, activity-data and emission-factor uncertainty tables, and a workbook with Monte Carlo sheets. Official country page: https://redd.unfccc.int/submissions/by-country/country_detail/cmr.html | The reported “zero” is a proposed accounting reference level under technical assessment, not an observed zero ecological change. Biomass factors include old national studies, Gabon/other international sources and IPCC defaults. The submission is not a calibrated 2015–2023 AGB comparison. |

## 2. Alternative routes around the identified access problems

### Australia: ABARES workbook

The original workbook remains the most direct file to try manually in a browser:

- https://www.agriculture.gov.au/sites/default/files/documents/Indicator_1_1a_iv_area_change_Data_Tables_2023.xlsx
- Landing page: https://www.agriculture.gov.au/abares/forestsaustralia/sofr/criterion-1/indicator-1.1a.iv-forest-area-change

A query-string request returned HTTP 403 in the present environment. That is not evidence that a browser download will fail or that the file is unavailable. If it fails locally, use the official alternatives:

1. **National Inventory Report 2023, Volume 1 DOCX (22 MB):** https://www.dcceew.gov.au/sites/default/files/documents/national-inventory-report-2023-volume-1.docx  
   PDF (18 MB): https://www.dcceew.gov.au/sites/default/files/documents/national-inventory-report-2023-volume-1.pdf  
   Landing page: https://www.dcceew.gov.au/climate-change/publications/national-inventory-report-2023  
   The report covers 1989–90 through 2022–23 and includes land-use area tables. A direct DOCX request timed out after 55 seconds here; no permanent-unavailability inference is made.
2. **Forests of Australia (2023) dataset:** https://data.gov.au/data/dataset/forests-of-australia-2023  
   It provides GeoTIFF/Esri Grid, metadata, lineage, lookup tables, a map and the successfully retrieved attribute CSV under CC BY 4.0.
3. **National Inventory by Economic Sector data tables:** https://www.dcceew.gov.au/sites/default/files/documents/national-inventory-by-economic-sector-2023-data-tables.xlsx  
   These are useful for emissions/economic-sector reconciliation, not a substitute for forest-area or AGB observations.

**Gap effect:** these routes can unblock an Australian physical source module. They do not automatically produce a common calendar-endpoint forest definition or calibrated 2015–2023 AGB change. Fiscal/reporting-year operators, external territories, source-method changes and carbon-model versus direct-stock distinctions must be registered before analysis.

### Cameroon: report available, underlying workbook still needed

The official country page exposes the PDF but not a separate workbook download. A direct automated PDF request returned an HTML anti-bot challenge, while the document was readable through the indexed/fetch route. A manual browser download is therefore worth trying.

For numerical reproduction, request the workbook or CEO export behind the PDF from MINEPDED/ONACC or the Coalition for Rainforest Nations. The important sheets named in the submission are:

- `DA_CEO database_Etape 1` — the 29,409 collected points;
- `DA_plot Count_Etape 2` and `DA_Terres_Etape 3` — annual point counts and area matrices;
- `DA_Erreur Aléatoire` and `DA_Terres_Etape3 Incertitudes` — activity-data uncertainty;
- `FE_Terres` and `FE_Terres Incertitudes` — biomass/emission factors and uncertainty;
- `Résultats_MC` and `Résumé_MC` — Monte Carlo outputs.

**Gap effect:** the PDF supplies a much better acquisition target and design description. Only the underlying points/workbook and a compatible uncertainty evaluation can support numerical checks. Default or foreign biomass factors must remain explicitly typed.

### Brazil: current map assets are accessible; compatible reference-vintage-3 evidence is the bottleneck

- Validation downloads: https://brasil.mapbiomas.org/downloads/pontos-de-validacao/
- Current product/GEE information: https://brasil.mapbiomas.org/iniciativas-e-produtos/cobertura-e-uso-da-terra/cobertura-30m/cobertura/
- Current C11 GEE asset identified by the provider: `projects/mapbiomas-public/assets/brazil/lulc/collection11/mapbiomas_brazil_collection11_coverage_v3`

The public page describes 85,152 samples interpreted for 1985–2024, but the currently linked public CSV/XLSX/vector representations examined earlier do not supply the required current reference-vintage-3 endpoint closure; the newly inspected vector table ends in 2022. Downloading those files again will not repair that mismatch.

**Most useful file/request:** reference-collection-3 labels for 2015 and 2023, inclusion probabilities/design weights, training/validation roles, boundary/sparse-class rules, interpreter harmonization and the exact Collection 11 crosswalk. A design-based marginal endpoint or transition error bound can be useful; an exact paired field census is not a universal prerequisite. Overall map accuracy alone does not supply the class-set symmetric-difference budget needed for conversion bounds.

### Indonesia: current reference/design information remains the bottleneck

- C4.1 ATBD: https://landy.mapbiomas.id/assets/files/ATBD%20Mapbiomas%20ID%20Col%204.1%20EN.pdf
- Method page: https://landy.mapbiomas.id/en/atbd
- Accuracy page: https://landy.mapbiomas.id/en/accuracy-assessment
- Statistics: https://landy.mapbiomas.id/en/statistics

The acquired C4.1 documentation describes independent annual references through 2022; the public accuracy page concerns an older collection. JRC TMF or GEE can provide an additional differently defined map series, but not C4.1 reference error or an independent calibration if source inputs/reference data overlap.

**Most useful file/request:** C4.1 2023 reference labels/design weights and class/transition confusion information, with training-role and support metadata. The required target is not only net-area error but initial-forest/final-destination class-set error for conversion transfer.

### DR Congo: JRC provides an additional physical series, not MapBiomas C1 validation

Use the JRC CSV above for a feasible national TMF analysis. For spatially explicit work, the official download/GEE page is https://forobs.jrc.ec.europa.eu/TMF/data and the version-pinned 2023 assets include `projects/JRC/TMF/v1_2023/AnnualChanges` and `TransitionMap_MainClasses`.

**Gap effect:** this can expand physical evidence beyond MapBiomas C1. It does not certify C1 class changes or produce AGB uncertainty. Keep the TMF definition/domain and its recent-year classification caveats separate.

### Canada: SCANFI v2 is downloadable, but its periods do not close the primary endpoint gap

- Dataset landing page: https://open.canada.ca/data/en/dataset/07653869-f303-46c2-a04e-9ab479b73cbf
- Download directory: https://ftp.maps.canada.ca/pub/nrcan_rncan/Forests_Foret/SCANFI/v2/
- Readme: https://ftp.maps.canada.ca/pub/nrcan_rncan/Forests_Foret/SCANFI/v2/_SCANFI_v2_read_me.txt
- NFI tables: https://nfi.nfis.org/en/resources

SCANFI v2 supplies 30 m maps at five-year intervals from 1985 to 2025. It therefore offers 2015, 2020 and 2025, not a 2023 map. The provider identifies temporal, extrapolation, pest, Yukon and other validation limitations. It can support matching five-year sensitivity analyses; it must not be interpolated and relabelled as an observed 2023 endpoint.

**Most useful provider clarification:** the exact implementation and confidence meaning of NFI v3.1 Table 17C.0 change RSE and interval exports. The point/RSE/CI discrepancy is not resolved by SCANFI or by selecting the smaller uncertainty. Current-period coverage and omitted-geography treatment remain separate tasks.

### ESA CCI Biomass v7: retrieval is easier than calibration

- Catalogue: https://climate.esa.int/en/catalogue/6429d1aafe1e43b9b414e4a5a7f8b903/
- CEDA record: https://catalogue.ceda.ac.uk/uuid/6429d1aafe1e43b9b414e4a5a7f8b903/
- THREDDS download catalogue: https://data.cci.ceda.ac.uk/thredds/catalog/esacci/biomass/data/agb/maps/v7.0/catalog.html
- CCI toolbox release with `agb_change`: https://github.com/esa-cci/esa-climate-toolbox/releases/tag/v1.7.1

The v7 series includes 2015 and 2023, 100 m maps and 1/10/25/50 km aggregates, plus a Python change-map tool. Bounded OPeNDAP queries or coarse aggregates can avoid a prohibited global native-resolution download. This is a practical retrieval workaround.

**Gap effect:** easier computation is not calibrated change uncertainty. The delivered change-SD example does not supply the required final-map cross-year covariance, differential-bias bound, forest allocation or complete-coverage treatment. A defensible joint error model or independent design-based inference is still required.

## 3. Work that deeper search cannot replace

1. **French retrospective bridge:** the 2024 methodology confirms the then-current unusable-wood convention, but a same-method backcast or explicit differential cubage/protocol bias bound is still needed for the long comparison.
2. **Finnish biomass precision:** the official biomass tables have no SE columns. Request design-based biomass totals/variances or appropriate microdata/design outputs from Luke; do not borrow volume SEs.
3. **Current map-reference calibration:** newer map downloads do not create missing reference years, sampling designs or class-set error budgets.
4. **Reporting-rule accuracy and conversion associations:** these require independent supported outcomes on common cases, a fixed evaluation design and uncertainty in estimated performance. Additional maps are not independent replicates, and subnational units cannot replicate a single national account outcome.
5. **All-eight primary AGB completion:** useful eligible subsets may proceed without waiting for all eight. Completion requires compatible observation operators and uncertainty/bias assessment, not necessarily sign resolution, exact paired censuses or known covariance.

## 4. Recommended fetch order

1. Fetch the JRC CSV, Australian attribute CSV, Finnish supplements and French methodology now; their access and identities were verified here.
2. Manually try the ABARES workbook, Australian NIR DOCX and Cameroon PDF. Preserve response headers, file hashes and reference-period metadata.
3. Request the Cameroon workbook/CEO export and the Brazil/Indonesia current reference/design files named above.
4. Ask Canada's NFI for the Table 17C.0 uncertainty implementation and Luke for biomass-specific design variance information.
5. Only after source/period/domain registration, execute the feasible Australia/Cameroon physical modules and eligible national AGB subsets. Keep unresolved signs and incomplete countries explicit rather than converting access success into unsupported completion.

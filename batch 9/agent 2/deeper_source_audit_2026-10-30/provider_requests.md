# Exact provider requests — 30 October 2026

These requests are limited to items that were not publicly retrievable, were access-restricted, or remain unpublished. Publicly fetchable sources were retrieved and are listed in `evidence/retrieval_ledger.csv`.

## 1. Brazil — MapBiomas

**To:** `contato@mapbiomas.org`  
**Subject:** Request for Collection 11 reference-design microdata and version-matched annual/transition covariance (C110)

I retrieved the **Accuracy Assessment Appendix, Collection 11, Version 1 (August 2026)** and the current `mapbiomas/brazil-accuracy` C110 implementation. The public validation-download page still lists **Collection 9** files. Those files have 85,152 rows, but only 4,053 have nonempty `CLASS_2023` and `ID_REVISAO`; the public vector ends at `CLASS_2022`. They therefore cannot reproduce the Collection 11 accuracy design through 2024.

Please provide the following, or provider-computed equivalents if sample-level release is not possible:

1. **Exact reference-panel version used for Collection 11 accuracy**, covering the assessed years **1985–2024**, with stable `TARGETID`/sample ID and one annual reference label per sample-year.
2. For each sample-year: original interpreted reference class; interpreter-agreement field (`COUNT_YYYY` or current equivalent); edge field (`BORDA_YYYY`); revision ID; missing/exclusion/filter flag; and a field distinguishing a newly interpreted label from a **carried-forward** label. The C110 code’s carry-forward behaviour must not be mistaken for independent reinterpretation.
3. Sample role and design: training versus independent accuracy sample (including the Amazon training role), biome, grouped-chart unit, slope class, and the **final `strata_id` actually used in C110**. Please include the versioned `points_strata.csv` and `strata.csv` if they differ from the files at commit `8cad5dbd80bb4aaae52e032213ff7d9b82aac56f`.
4. Design weights and population controls: inclusion probability (`PROB_AMOS_` or current equivalent), base weight (`PESO_AMOS`), final post-adjustment analysis weight, stratum population pixel/area total (`N_h`), and the agreement/missing-data adjustment components. Where used, please define the roles of `VOTOS`, `VAL_PESO`, `PESO_VOT`, `NEW_WEIGHT`, `NEW_PROB`, `REINSP`, and `AMOSTRA_AM`; these roles should not be inferred from their names.
5. The **Collection 11 mapped class for the same sample-year**, plus the legend-harmonization crosswalk used in the accuracy analysis.
6. For calibration rather than descriptive accuracy alone: design-weighted **annual error matrices and adjacent-year reference×mapped transition matrices**, with their design-based variances and cross-year/cross-endpoint covariances, at national and biome levels and at the available legend levels. If microdata cannot be released, provider-computed matrices and covariance outputs are sufficient; overall/user/producer accuracy alone is not.
7. Please confirm whether GEE asset `projects/mapbiomas-workspace/VALIDACAO/mapbiomas_85k_col5_points_w_edge_and_edited_v3` is the exact current C110 input and, if so, its access conditions and field definitions. Anonymous REST retrieval returned HTTP 401; this does not establish whether the asset is private. If it is not current, please provide the current asset/version ID.

**Relevant public links**

- C11 appendix: https://brasil.mapbiomas.org/wp-content/uploads/sites/3/2026/08/Accuracy-Assessment-Appendix-Collection-11-v1.pdf
- Public downloads (currently labelled Collection 9): https://brasil.mapbiomas.org/downloads/pontos-de-validacao/
- C110 implementation at pinned repository head: https://github.com/mapbiomas/brazil-accuracy/tree/c7a20e5e892495d98603183937a2e6926d558cfc/src/collection_110
- GEE asset link: https://code.earthengine.google.com/?asset=projects/mapbiomas-workspace/VALIDACAO/mapbiomas_85k_col5_points_w_edge_and_edited_v3

**Minimum sufficient response:** a version-matched C11 reference/design panel, or provider-computed annual and transition error matrices with design covariance and an explicit estimand/version statement.

---

## 2. Indonesia — MapBiomas

**To:** `contact@mapbiomas.id`  
**Subject:** Request for Collection 4.1/5 independent TVI reference-design data and annual/transition covariance

I retrieved **ATBD MapBiomas Indonesia Collection 4.1, Version 1 (February 2026)**, the official accuracy page/Shiny application, and the Landy C4 scripts. The ATBD says independent validation is periodic, every two collections, but its detailed independent-sample description identifies **12,957 TVI samples labelled annually for 2000–2022**, first implemented in Collection 2. The platform now serves Collection 5 maps through 2025. The C4 repository scripts instead use static-reference classifier-validation assets, which are not interchangeable with independent annual TVI labels.

Please clarify which reference panel supports **Collection 4.1 and Collection 5**: the Collection 2 panel, a Collection 4/4.1 update, or a new panel. Then please provide, or compute from that panel:

1. Exact reference-dataset name/version, collection applicability, sample count, and all assessed years, including whether labels extend beyond **2022** to **2024/2025**.
2. Stable sample ID; annual independent TVI reference class; mapped class for the corresponding collection/year; missing/exclusion/filter flag; and any carry-forward/revision indicator.
3. The actual design identifiers: seven geographic regions, six SRTM slope classes, and the resulting **42-region×slope strata**, with stratum population pixel/area totals (`N_h`), inclusion probabilities and final analysis weights.
4. Interpreter/reviewer information needed for the estimand: team/interpretation agreement indicator, the at-least-two-of-three agreement result, supervisor consolidation decision, and any weight adjustment. Personal interpreter identities are not requested.
5. Sample role, separating independent accuracy samples from classifier training or static-reference validation samples.
6. Design-weighted **annual error matrices and adjacent-year transition matrices**, with design-based variances and cross-year/endpoint covariances, nationally and by region/legend level. If microdata cannot be released, provider-computed matrices and covariance outputs are sufficient; overall, user/producer, commission/omission, allocation and area-disagreement summaries alone are not.
7. If no independent C4.1/C5 reference panel exists, please state that explicitly and identify the exact reference period/design that should be cited for the current maps.

**Relevant public links**

- C4.1 ATBD: https://landy.mapbiomas.id/assets/files/ATBD%20Mapbiomas%20ID%20Col%204.1%20EN.pdf
- Official accuracy page: https://landy.mapbiomas.id/en/accuracy-assessment
- Collection 2 aggregate Shiny app: https://mapbiomas-network-accuracy.shinyapps.io/MapBiomas_Indonesia_Col2_Acc_EN/
- C4 implementation repository: https://github.com/mapbiomas-indonesia/MapBiomas-Indonesia---Landy/tree/a957d72992d90ed5a4787ce13c8a36b7a1b48780
- Collection 5 map platform: https://plataforma.mapbiomas.org/coverage/coverage_lclu?t%5BregionKey%5D=indonesia

The two anonymous-401 C4 static-reference assets are recorded in `evidence/retrieval_ledger.csv`; they are **not** requested as substitutes for the independent TVI panel.

**Minimum sufficient response:** an explicit C4.1/C5 reference-vintage statement plus the independent annual panel or provider-computed annual/transition design covariance.

---

## 3. Finland — Luke / NFI and biomass-model teams

**To:** `kari.t.korhonen@luke.fi`, `juha.heikkinen@luke.fi`, `tietopalvelu@luke.fi`  
**Subject:** Request for NFI12/NFI13 above-ground biomass design covariance and Repola et al. (2025) model covariance

I retrieved the full **March 2026 EU NID** (`FI_NID_EU_2024_2026_03-15.pdf`, 579 pages), the NFI13 article/supplements, and the corrected Luke 12/2026 report. Table 6.4-13 now supplies 2014–2023 biomass stock-change estimates with 95% NFI-sampling-only confidence intervals. This is useful biomass-specific design information, but it is an annualized old-model change estimand—not the same-domain NFI12/NFI13 national above-ground biomass endpoint covariance required for our comparison. Volume standard errors cannot be substituted.

Provider-computed aggregates are welcome; exact plot coordinates and identifiable plot data are **not** required.

1. **National endpoint design outputs:** for the same explicitly defined domain, please provide NFI12 (2014–2018) and NFI13 (2019–2023) above-ground living-tree biomass estimates, their design-based variances/standard errors, and the **cross-inventory covariance**. Please supply South Finland, North Finland and whole-country values where available, and distinguish all Forest Land from Forest Land Remaining Forest Land. Preserve unrounded values and state dry-matter/carbon units and any carbon conversion.
2. **Change covariance:** the corresponding design variance of NFI13−NFI12, including the shared permanent-panel contribution and the treatment of temporary plots, rather than two independent endpoint SEs alone.
3. **Sufficient aggregate design components if microdata cannot be shared:** region/stratum variance contributions and cross-inventory covariance contributions under the modified Grafström–Schelin/ratio/delta-method estimator; domain/timing definitions; and the exact estimator/version used. Exact Voronoi geometry or coordinates are unnecessary if Luke supplies these aggregate contributions.
4. **Table 6.4-13 clarification and machine-readable output:** unrounded 2014–2023 gain–loss and stock-change values, both 95% CI endpoints, the exact interval multiplier/convention, and confirmation of the printed unit. The table heading says `Tg/a`, while the 2023 gain–loss entry is `7 292`, exactly 1,000× the 7.292 Tg/a value in the 2025 submission. Please confirm the intended unit rather than leaving users to rescale it.
5. **Version-matched recomputation:** Table 6.4-13 is described as using old Repola (2008/2009) models and 2025-submission gain–loss values. If these CIs are to support the current analysis, please provide the corresponding current-model/current-submission outputs or explain why the old-model values remain valid.
6. **Repola et al. (2025) model uncertainty:** the manuscript cited as *Repola, J., Heikkinen, J., Mehtätalo, L., Lehtonen, A., Kangas, A. & Sarkkola, S. 2025. Tree level biomass models for Finland. Manuscript*; model forms/parameters; fixed-effect covariance; plot- and tree-level random-effect covariance; residual covariance; and the propagation used for tree biomass and BCEF estimates. A full joint covariance or provider-computed national prediction covariance is preferred.
7. Please clarify why §6.4.3.1/Appendix 6g calculates model uncertainty from the simplest **old Repola 2008/2009** models although current estimates use **Repola et al. (2025)**, and supply the current-model uncertainty calculation if available.

**Relevant public links**

- March 2026 EU NID: https://cdr.eionet.europa.eu/fi/eu/govreg/inventory/envasbzqa/FI_NID_EU_2024_2026_03-15.pdf
- EIONET envelope: https://cdr.eionet.europa.eu/fi/eu/govreg/inventory/envasbzqa/
- NFI13 article and supplements: https://www.silvafennica.fi/article/24045
- Corrected Luke 12/2026 record: https://jukuri.luke.fi/items/a432e484-0102-4d4c-8919-2f070544c2b4
- April UN NID landing/direct PDF (not assumed identical to the March EU file): https://unfccc.int/documents/656427 and https://unfccc.int/sites/default/files/resource/FI_NID_UNFCCC_BTR2_2024_2026-04-15.pdf

**Minimum sufficient response:** same-domain NFI12/NFI13 national biomass endpoint variances and cross-inventory covariance, plus the current Repola et al. (2025) prediction/model covariance or provider-computed equivalent.

---

## 4. Canada — National Forest Inventory / NFIS

**To:** `nfisupport@nfis.org`  
**Attention:** Paul Boudewyn and Michael Smith  
**Subject:** Request for fixed-panel change implementation and reconciliation of Table 17C.0 RSE/variance/CI fields

I retrieved all Canada and terrestrial-ecozone point/RSE/CI CSVs for Tables 15C, 17C and 18C, Estimation Procedures v1.13, Business Process v8.0, and current N3WRT class-35 point/change outputs including `var_biom`.

The static stock controls are coherent, but the static change fields are not. For **Table 17C.0**, the national total is **17.639 million tonnes**, RSE **1.16%**, and CI half-width **38.918 million tonnes**. These imply a multiplier of **190.203526** if the RSE is applied to that point estimate. Table 18C.0 similarly implies **198.996026**. In contrast, ecozone CI half-widths aggregate to the national values by root-sum-of-squares, while change-RSE rollups do not. The current generator exposes a coherent additive `var_biom` field, but its forest-land change total is **19.066**, not the static **17.639**, so the two products cannot be mixed.

Please provide:

1. **Change Estimation Procedures based on Fixed Annual Panels, Version 1.08, dated 2006-08-08**, cited in Business Process v8.0, or the exact current superseding implementation. Estimation Procedures v1.13 supplies area-total formulas and does not resolve this fixed-panel biomass-change implementation.
2. The exact static-report **data snapshot/version and query/classifier definitions** for Tables 15C.0/17C.0/18C.0, and the corresponding current N3WRT dataset/version identifiers. Please explain the scope/version difference between static Table 17C.0 **17.639** and current class-35 forest-land output **19.066**.
3. Version-matched, unrounded national and terrestrial-ecozone outputs for stock and change: point estimate, absolute SE, RSE, variance, CI lower/upper or half-width, confidence level, and any degrees-of-freedom/multiplier used.
4. Exact formulas/source implementation for `sep_biom`, `var_biom`, `biomass_cll`, and `biomass_clu`, including units and scaling. In the current national class-35 snapshot, stock `sep_biom` agrees with variance-derived RSE in **53 of 57** nonzero cells within 0.02 percentage points, whereas change agrees in only **1 of 57**. Please identify which change field is authoritative and why they differ.
5. The intended interval convention for each product: static `intv` files appear to contain half-widths, whereas generator `biomass_cll`/`biomass_clu` are endpoints. The generator’s empirical multiplier is approximately **1.965**, but this must not be transferred to the static report without confirmation.
6. Aggregation and covariance rules for ecozone-to-national rollups, the fixed-panel change estimator, permanent/temporary-panel contributions, and the documented **200% RSE cap**. Please explain why static change ecozone RSEs do not reproduce national RSEs although CI half-width RSS rollups do reproduce national intervals.
7. If the static fields are erroneous, a corrected version-matched release or an authoritative erratum identifying the affected tables/cells and the correct values.

**Relevant public links**

- Standard reports: https://nfi.nfis.org/en/standardreports
- Resources: https://nfi.nfis.org/en/resources
- Estimation Procedures v1.13: https://nfi.nfis.org/resources/estimation/Estimation_procedures_v1.13.pdf
- Business Process v8.0: https://nfi.nfis.org/resources/general/NFI-Business-Process-Version-8.0.pdf
- Reports Generator: https://nfi.nfis.org/en/customized_report
- Table 17C.0 change point/RSE/CI direct CSVs:
  - https://nfi.nfis.org/resources/general/summaries/t1/en/CA/csv/ca_t17_forage20_biom_change_en.csv
  - https://nfi.nfis.org/resources/general/summaries/t1/en/CA/csv/ca_t17_forage20_biom_change_sep_en.csv
  - https://nfi.nfis.org/resources/general/summaries/t1/en/CA/csv/ca_t17_forage20_biom_change_intv_en.csv

**Minimum sufficient response:** the fixed-panel implementation plus version-matched full-precision static/generator outputs and an authoritative derivation of change RSE, variance and interval fields. Selecting the smaller uncertainty or assuming a 95% interval is not an acceptable resolution.

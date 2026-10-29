# Current input links and review scope — F09

All four companion PDFs below were successfully retrieved in full from the official site, individually under 25 MB, with complete SHA-256 identity verification. Close reading was targeted; full acquisition does not imply that every page was carefully reviewed. No raw report is redistributed.

| Document | Official direct link | Current scope |
|---|---|---|
| E3UB v7 | https://climate.esa.int/documents/3354/End-to-End_ECV_Uncertainty_Budget_E3B_V7.0.pdf | Full 30-page file acquired; uncertainty/covariance/aggregation/change sections reviewed; five pages visually inspected |
| PVIR v7 | https://climate.esa.int/documents/3356/Product_Validation_Intercomparison_Report_PVIR_V7.0.pdf | Full 108-page file acquired; targeted reference methods, endpoint stock tables, Brazil comparison and support discussion reviewed |
| PVP v6 | https://climate.esa.int/documents/3364/Product_Validation_Plan_PVP_V6.pdf | Full 42-page file acquired; harmonization, change-reference candidates, error model and covariance normalization reviewed |
| ADPC v7 | https://climate.esa.int/documents/3371/Algorithm_Development_Plan_Change_ADPC_V7.0.pdf | Full 22-page file acquired; change methods, assumptions and proposed validation activities reviewed |
| ATBD v7 | https://climate.esa.int/media/documents/Algorithm_Theoretical_Basis_Document_ATBD_V7.0.pdf | Previously completed R01 review: all release chunks/pages recovered and 138 normalized text-page matches to official source, not whole-PDF/image equivalence |
| PUG v7 | https://climate.esa.int/documents/3352/Product_User_Guide_PUG_V7.0.pdf | Inherited F08 targeted definition/denominator review |

[Official document index](https://climate.esa.int/en/projects/biomass/key-documents/) · [Published ATBD review R01](https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/ecomod_empirical_followup/ATBD_review_R01)

## Excel and original empirical sources

The [complete reference XLSX](https://brasil.mapbiomas.org/wp-content/uploads/sites/4/2024/08/mapbiomas_85k_col2_1_points_w_edge_and_edited_v1-2.xlsx-2.xlsx) was successfully retrieved and audited in F08. It is **not** a current access failure. Its equivalence to the CSV remains representation equivalence, not new independent validation. See [the unchanged F08 full audit/source links](INPUT_LINKS_F08.md) and [audit JSON](data/reference/xlsx_audit_F08.json).

Native country biomass/cover rasters were not fully downloaded; existing bounded-window guards and source registries remain unchanged. No eligible repeated local 2015–2023 biomass reference was newly acquired. PVP's potential Brazilian LiDAR reference is dated 2011–2018 and its current-use status is unresolved in the source; listing it is not evidence that an accessible compatible 2015–2023 sample exists.

The current evidence limits, equation/provenance discrepancies and required next measurements are in [SOURCE_REVIEW_F09.md](SOURCE_REVIEW_F09.md). Exact identities and visual-review coverage are recorded under `metadata/companion_review_F09/`. Older access notes retain their version dates and must not be read as the current F09 status.

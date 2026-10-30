# Content coverage audit — F16_A01

This audit supplements, rather than replaces, `inputs/F15_CONTENT_COVERAGE_AUDIT_F15_A01.md`.

## Main-text completeness

The main text independently states the estimand, actual period, numerical result and inferential qualification for each new module:

| Evidence | Main location | SI/workbook verification |
|---|---|---|
| Cameroon reported total forest area, 2015–2020 | Abstract; national Table 1; national-results paragraph; Figure 2a | SI Table S20; `CMR area 2000-2020` |
| Cameroon class changes and 1-ha source mismatch | National-results paragraph | SI S13 protocol and Table S20; annual CSV residual column |
| Cameroon net CO₂e flux and MC relative uncertainty | National-results paragraph; Figure 2b | SI Table S20; `CMR flux 2000-2020`; Table 31/37 checks |
| ABARES-adjusted Australian area, 2015–2021 | Abstract; Table 1; national-results paragraph; Figure 2c | SI Table S21; `AUS ABARES area 1989-2021` |
| Separate NIR2021 stock and gains/losses | National-results paragraph; Figure 2c | SI Table S21; `AUS NIR21 stock flows` |
| NIR2023 forest-land change through 2021–22 | Abstract qualification; Table 1; national-results paragraph; Figure 2c | SI Table S21; `AUS NIR23 forest land` |
| Documented 2022–23 carry-forward | Abstract; Table 1; results; Figure 2 caption/open endpoint | SI S13 protocol and Table S21; activity-status column |
| NIR2023 conversion/re-clearing/regrowth | National-results paragraph | SI Table S21; `AUS NIR23 clearing` |
| Forests of Australia (2023) exact snapshot and 2021 currency | National-results paragraph | SI Table S22; category/jurisdiction CSVs and workbook sheets |
| Rounding residuals and unallocated cells | Main reports the consequential Cameroon case; SI provides the full audit | Annual CSV residual columns; revision account |

## Editorial allocation

- Seven main figures and two main tables remain within the requested typical 4–8 key-figure range.
- Main contains the essential new findings, the source-period distinctions, carry-forward, area-versus-flux/AGB warning and all conclusions.
- SI contains source pages, exact annual endpoints, category/jurisdiction detail, rounding protocols and reproducibility information. It does not introduce a separate discussion, new ecological claim or work-plan narrative.
- All 30 SI figures/tables (two figures, 28 tables) are explicitly cited in main; `metadata/SI_linkage_F16.json` is generated from the compiled SI auxiliary file.
- All 31 inherited workbook sheets are preserved in value. Ten new sheets map directly to the new data and provenance.

## Inherited coverage checks retained

The F16 tests continue to check the complete eight-country case set; seven Indonesian/Brazilian cohort ranges; all five account-component contributions; three account windows; forest-account area/factor decomposition; direct forest-to-oil-palm hectare-events; regional compensation; Indonesian definition/support sensitivity; Finnish source cells, bias sensitivity and stock–flow ledger; French windows/contrasts; Canadian unresolved uncertainty; the exact AI declaration; hyperlinked ORCID; seven keywords; and the F06 separate-row/wrapped-LAC coverage figure. No inherited figure, table or supporting control was removed to make room for F16.

## Final scope check

“Completed module” means a numerical reported-area/flux analysis on the source's actual period. It does not mean calibrated national 2015–2023 forest-AGB completion or sign resolution. All eight primary AGB analyses remain incomplete. No mapped or reported area is converted into AGB, no CO₂e flux is called an AGB-stock change, and no source/vintage difference is presented as an uncertainty interval.

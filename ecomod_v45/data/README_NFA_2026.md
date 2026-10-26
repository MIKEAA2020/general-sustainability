# NFA 2026 data and recomputation

## Primary source

`NEFBA_2026.xlsx` is the official National Ecological Footprint and Biocapacity Accounts, Edition 2026, Results and Metadata version 1.0 workbook. It was downloaded on 2026-10-24 from the York University Ecological Footprint Initiative data page. The official release notes date the public release to 2026-04-22 and recommend citing Lo et al. (2026). The workbook is distributed under CC BY-SA 4.0; see the release notes and the manuscript reference list.

- Data page: https://footprint.info.yorku.ca/data/
- Release notes: https://footprint.info.yorku.ca/files/2026/04/NEFBA_ReleaseNotes.pdf
- Workbook: https://footprint.info.yorku.ca/files/2026/04/NEFBA_Data_global_national_ecological_footprint_biocapacity.xlsx

## Scope and variables

The complete world observations are 1961-2023. The 2024-2025 rows are estimated and excluded. The primary analysis is 1961-2023; the 1961-2022 sensitivity is taken from the same Edition 2026 workbook, not from Edition 2025. The release notes state that Edition 2026 recalculated common years and revised multiple sources and methods.

- `world_data.biocap_total_gha`: total biocapacity account value, `B`.
- `world_data.efp_total_gha`: Ecological Footprint of Production, denoted `E_production`; it is not relabeled as the consumption footprint.
- `world_data.pop_1000_persons`: population in 1,000 persons from UN PopStat; per-capita values in the extracts are recomputed from totals divided by this population in persons, rather than taken from rounded workbook per-capita columns.
- Component biocapacity labels are preserved as `Cropland`, `Grazing land`, `Forest biocapacity`, `Fishing grounds`, and `Built-up land`. In particular, “Forest biocapacity” is the workbook label; it is an account value, not a measurement of forest biomass, soil condition, wetland extent, fish biomass, or the model state `A_c`. Built-up land is included as an NFA accounting class; it is not ecological capital.

All reported NFA component movements are account-composition signals. The NFA workbook does not supply a populated physical-stock inventory for the paper's heterogeneous ecological assets, and this package does not convert account changes into physical-stock changes.

## Reproduction

From the package root:

```bash
python work/nfa_2026_recompute.py
python work/nfa_2026_proxy_divisia.py
```

The first script validates the observed/estimated windows, population identity, component sums, and component contributions; it writes the clean 1961-2023 annual extract, endpoint metrics, component metrics, crop/non-crop account metrics, summary JSON, and Figures 2-3. The second script is a supplementary proxy sensitivity using independent FAOSTAT-derived cropland-area and cereal-yield inputs; its residual is explicitly an accounting proxy, not physical capital. Source definitions and limitations for those inputs are in `data/empirical/README.md`.

# F13_A01 — One integrated empirical publication

**Ecological assets behind improving accounts: national forest evidence and biomass-change identifiability**  
Amin Abaee · ORCID https://orcid.org/0000-0002-0019-1842  
30 October 2026

## Publication decision

This is **one integrated main manuscript and Supplementary Information**, not a separate submission for the F12 extension. F11 identification results, supported F12 national analyses and new F13 evidence are integrated throughout the abstract, questions, methods, results, discussion and conclusions. Earlier versioned deposits remain unchanged; a deposit is a preservation unit, not necessarily a separate publication.

### Main deliverables

- `integrated_F13_A01_main.pdf` and `.tex` — integrated main manuscript.
- `integrated_F13_A01_SI.pdf` and `.tex` — integrated methods, source audits and limitations.
- `national_results_F13_A01.xlsx` — 30 readable sheets: the 19 original F12 sheets plus new interpretation, French, Canadian, Congolese and source tables.
- `COMPLETION_AND_REMAINING_WORK_F13_A01.md` — executed work and explicit unfinished targets.
- `REVISION_AND_DELETION_ACCOUNT_F13_A01.md` — substantive and editorial changes, retained results and non-deletions.

## What was actually added

1. **DR Congo:** acquired official Collection 1 country, biome and province CSV statistics, legend, ATBD and version-pinned area/statistics code. Executed the national 2000–2025 series and 2015–2023 changes. Source forest classes 3/4/5 decline **3,303,015.650 ha (2.014673%)**. Subunit footprints do not close to the country total and are not forced into a national partition. These are mapped extent results, not calibrated AGB or causal conversion.
2. **France:** recovered the historical 2013–2017 France row, **2,716 ±45 million m³**, plus its method document. Combined it with three current official inventory-cycle workbooks, retaining all three contrasts against 2021–2025. The longest reported contrast is **+200 million m³**. A full-unit-rounded, dependence-free sampling band has at least 90% coverage, **[104,296] million m³**. Additional marginal-normal assumptions give separate approximate 95% bands. Differential method/cubage bias is not independently bounded, and exact retrospective harmonization is not certified. This is production-forest stem volume across pooled windows, not exact-endpoint AGB.
3. **Canada:** prioritized direct NFI AGB/change tables over GHG flows. The reported annualized total change is **+17.639 Mt/year**, with labelled interval **[−21.279,56.557] Mt/year**. Its confidence level is not independently certified here. The change RSE and interval do not reconcile under the ordinary definition; all three HTML representations carry the same version 3.1 label, so a simple labelled-version mismatch does not resolve the issue. Repeated and projected observations, artificial-change filtering, earlier periods and 262.190 million ha of omitted northern geography are explicit. No small error bar or resolved primary trend is invented.
4. **Brazil reference route:** newly acquired the vector archive currently linked at an October 2026 URL. Its DBF header has 85,152 records and 126 fields ending in 2022, not 2023/2024. A recent URL is not evidence of a newer reference epoch or collection.
5. **Integration:** national account trajectories, three mapped cases, 634 conditional-flow certificate results, Finnish inventory inference and new source results now sit within a single scientific argument alongside the preserved local allocation, joint-set, aggregation and density-contrast analyses.

**Original calibrated 2015–2023 national forest-AGB admissions remain 0/8.** This does not erase the executed secondary evidence and is not a claim of permanent source unavailability. Conversion associations, causal effects and independent reporting-rule accuracy are not estimated.

## Reproduction and build

Python 3.13 was used; package versions are pinned in `requirements_F13_A01.txt`. LaTeX requires `latexmk`, a TeX Live installation with the document packages, and Latin Modern fonts.

The published `F11_A01`, `F12_A01` and `F13_A01` folders can be kept as siblings. The workspace's longer original folder names are also supported. Minimal typesetting inputs are vendored in `paper_support`; no whole earlier deposit is copied into F13. The earlier numerical packages remain separate, immutable dependencies.

From the F13 directory:

```bash
python -m pip install -r requirements_F13_A01.txt
# Reacquire only the pinned analysis sources; raw cache is excluded from publication.
python src/acquire_F13.py FRA_memento_2018.pdf FRA_method_2013_2017.pdf \
  FRA_2018_2022_national.zip FRA_2019_2023_national.zip FRA_2021_2025_national.zip \
  CAN_NFI_ca_t17_forage20_biom_en.csv CAN_NFI_ca_t17_forage20_biom_sep_en.csv \
  CAN_NFI_ca_t17_forage20_biom_intv_en.csv CAN_NFI_ca_t17_forage20_biom_change_en.csv \
  CAN_NFI_ca_t17_forage20_biom_change_sep_en.csv CAN_NFI_ca_t17_forage20_biom_change_intv_en.csv \
  CAN_NFI_change_html.html CAN_NFI_change_CI_html.html CAN_NFI_change_RSE_html.html \
  COD_C1_wide_csv.zip COD_C1_ATBD.pdf COD_C1_legend.pdf \
  COD_C1_statistics_getAreas.js COD_C1_statistics_buildTables.R \
  BRA_current_public_vector_2026_10.zip
python src/analyze_sources_F13.py
python src/reference_audit_F13.py
python src/reproduce_F13.py
python src/build_workbook_F13.py
python src/build_documents_F13.py
python src/qa_deliverables_F13.py
# Inspect every generated layout sheet before confirming visual review.
python src/qa_deliverables_F13.py --confirm-visual-review
python src/verify_package_F13.py
```

`reproduce_F13.py` rebuilds the 12 new data artifacts and current-reference schema audit in excluded temporary cache folders under normal and optimized Python with hash seeds 17 and 73. All **13** must match the deposited bytes; **30 tests per mode** must pass. Existing F12 source-pinned reproduction of 50 outputs and 634 independently checked witnesses is preserved, not falsely described as a new F13 optimization run. F11's earlier test/certificate evidence is also retained.

Rebuilding artifacts deliberately changes the frozen package if non-deterministic document or workbook metadata differ. Verify the untouched deposit first; use a separate working copy for an amended build and never overwrite a published version. Do not rerun a completed publisher. The additive publication receipt records package identity and remote-byte verification.

## Source attribution, licences and non-redistribution

Source URLs, exact byte sizes and SHA-256 identities are in `metadata/source_registry_F13.json`. Provider raw ZIPs, workbooks, DBF bodies, PDFs and rasters remain in excluded cache and are **not redistributed**. Canadian factual source notes and Congolese/French numerical extractions are attributed to their providers in the manuscript, SI and registry.

- National Ecological Footprint and Biocapacity Accounts derived tables/figures retain **CC BY-SA 4.0**.
- MapBiomas Brazil Collection 11, Indonesia Collection 4.1/3 and DR Congo Collection 1 retain source attribution and their stated terms. Congo's ATBD p.19 explicitly documents CC-BY access. Class groups and support differences are identified; no cross-provider harmonized forest truth is asserted.
- IGN historical factual numerical extractions: **© IGN 2018**; current national results: IGN. No provider PDF body is deposited.
- Canada's NFI and Natural Resources Canada are acknowledged; reported inventory definitions, projections and omissions are retained.
- Finnish Luke data and original inventory publications/supplements are cited in the manuscript and inherited source metadata.
- Earlier boundary-derived objects and original figures retain their separately documented licences and OSM attribution. No blanket licence overrides those terms.

Arena.ai Agent Mode was used to assist with computational methods and literature review.

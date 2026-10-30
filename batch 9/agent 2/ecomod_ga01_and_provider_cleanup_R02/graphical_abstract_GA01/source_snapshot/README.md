# GA01 source snapshot

These files are byte-exact copies of the frozen C19 inputs used by the GA01 builder:

- `code/reproduce_two_land_C18_A01.py`
- `data/empirical_endpoints_C18_A01.csv`
- `data/empirical_components_C18_A01.csv`
- `data/quality_law_comparison_C18_A01.csv`

Their SHA-256 hashes are recorded in `../graphical_abstract_claims_C19_GA01.json`; the workspace verifier also compares them directly with the frozen C19 files.

The NFA-derived CSVs are adaptations/reformats of Lo et al. (2026), *National Ecological Footprint and Biocapacity Accounts, Edition 2026 (1961–2025): Results and metadata, version 1.0*, produced for Footprint Data Foundation by researchers at York University and the University of Iceland. The source workbook specifies **CC BY-SA 4.0**: https://creativecommons.org/licenses/by-sa/4.0/. Source: https://fodafo.org/data/ and https://footprint.info.yorku.ca/files/2026/04/NEFBA_Data_global_national_ecological_footprint_biocapacity.xlsx. No provider endorsement is implied.

The full inherited C19 attribution/license notice is preserved as `DATA_LICENSE_C19_A01.md`. Model code and simulation outputs are not represented as provider-authored data.

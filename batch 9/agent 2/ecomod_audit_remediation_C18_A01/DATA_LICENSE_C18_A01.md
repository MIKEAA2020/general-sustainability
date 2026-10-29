# Data attribution and license notice

## NFA workbook and extracted world data

`reference/NEFBA_2026.xlsx` is an unchanged copy of the public workbook:

Lo, K., Basnet, N., Miller, E., Srikanthalingam, B., Foley, B., Van Berkum, J. L., Long, A. H., Toneva, P., Ermina, M. and Klinkenberg, C. (2026). *National Ecological Footprint and Biocapacity Accounts, Edition 2026 (1961–2025): Results and metadata, version 1.0.* Produced for Footprint Data Foundation by researchers at York University and the University of Iceland. https://fodafo.org/data/

Downloaded from:
https://footprint.info.yorku.ca/files/2026/04/NEFBA_Data_global_national_ecological_footprint_biocapacity.xlsx

Its `readme` sheet specifies **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**:
https://creativecommons.org/licenses/by-sa/4.0/

`world_data_extracted.csv` reformats the workbook's world sheet as CSV without changing its numerical data. That extraction is provided under the same CC BY-SA 4.0 license. The NFA-derived numerical transformations in `verification_results.json`, `verification_stdout.txt`, `si_verification_results.json` and `si_verification_stdout.txt` retain that attribution and license. No provider endorsement is implied.

## OWID/FAOSTAT inputs

`reference/cropland-area.csv` and `reference/cereal-yield.csv` are unchanged downloads from Our World in Data's grapher, using FAOSTAT data. Appropriate attribution is Our World in Data / FAOSTAT. Third-party data retain their original applicable provider terms; consult:

- https://ourworldindata.org/grapher/cropland-area
- https://ourworldindata.org/grapher/cereal-yield
- https://ourworldindata.org/faqs#how-is-your-work-copyrighted

These inputs are not represented as original audit-created measurements.

## Manuscript reference sources

The reference `.tex` files are copies from the manuscript author's repository, with authorship and source provenance retained in `README.md`. They are included for version-matched audit context and are not represented as revised manuscripts or newly authored work.

## C18 derived outputs

The NFA-derived annual series, endpoint and component calculations, proxy decompositions, and NFA-derived empirical figures in `data/` and `figures/` are adaptations/reformats of Lo et al. (2026), NFA Edition 2026, version 1.0. They retain attribution and CC BY-SA 4.0. Changes consist of annual selection and joins, population-unit conversion, recomputed measures, decomposition, and new plotting. No provider endorsement is implied. OWID/FAOSTAT inputs retain the original provider terms; combining the sources does not relicense third-party inputs. Code and model simulations are not represented as provider-authored data. Original manuscript/reference authorship and any existing repository terms are preserved.

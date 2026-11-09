# Data attribution and license notice — C19 A01

## NFA workbook and extracted world data

`repository_sources/ecomod_audit/reference/NEFBA_2026.xlsx` is an unchanged copy of the public workbook:

Lo, K., Basnet, N., Miller, E., Srikanthalingam, B., Foley, B., Van Berkum, J. L., Long, A. H., Toneva, P., Ermina, M. and Klinkenberg, C. (2026). *National Ecological Footprint and Biocapacity Accounts, Edition 2026 (1961–2025): Results and metadata, version 1.0.* Produced for Footprint Data Foundation by researchers at York University and the University of Iceland. https://fodafo.org/data/

Downloaded from:
https://footprint.info.yorku.ca/files/2026/04/NEFBA_Data_global_national_ecological_footprint_biocapacity.xlsx

Its `readme` sheet specifies **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**:
https://creativecommons.org/licenses/by-sa/4.0/

In the complete C18 archive, `world_data_extracted.csv` reformats the workbook's world sheet without changing its numerical data, and the historical verification outputs retain the same attribution and license. Those historical audit files are not duplicated in lean C19; the full C18 package remains preserved. No provider endorsement is implied.

## OWID/FAOSTAT inputs

`repository_sources/ecomod_audit/reference/cropland-area.csv` and `repository_sources/ecomod_audit/reference/cereal-yield.csv` are unchanged downloads from Our World in Data's grapher, using FAOSTAT data. Appropriate attribution is Our World in Data / FAOSTAT. Third-party data retain their original applicable provider terms; consult:

- https://ourworldindata.org/grapher/cropland-area
- https://ourworldindata.org/grapher/cereal-yield
- https://ourworldindata.org/faqs#how-is-your-work-copyrighted

These inputs are not represented as original audit-created measurements.

## Manuscript reference sources

`inherited_C18/` contains the frozen C18 main and SI sources used only for version-matched transformation and diffing. Selected `inherited_C17/` code, table fragments, and the matched-wave figure are byte-preserved dependencies. Authorship and source provenance are retained; these files are not represented as newly authored C19 numerical work.

## C18-derived outputs inherited by C19

The NFA-derived annual series, endpoint and component calculations, proxy decompositions, and NFA-derived empirical figures in `data/` and `figures/` are C18 outputs inherited unchanged by C19. They are adaptations/reformats of Lo et al. (2026), NFA Edition 2026, version 1.0, and retain attribution and CC BY-SA 4.0. Changes from the source workbook consist of annual selection and joins, population-unit conversion, recomputed measures, decomposition, and plotting. No provider endorsement is implied.

OWID/FAOSTAT inputs retain the original provider terms; combining the sources does not relicense third-party inputs. Code and model simulations are not represented as provider-authored data. Original manuscript/reference authorship and any existing repository terms are preserved. C19 changes editorial organization and companion-reference metadata only; it does not alter the underlying provider data or their license status.

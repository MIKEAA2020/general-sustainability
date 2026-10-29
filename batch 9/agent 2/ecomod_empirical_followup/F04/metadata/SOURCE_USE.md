# Data sources and licences

## National Ecological Footprint and Biocapacity Accounts

Lo, K., Basnet, N., Miller, E., Srikanthalingam, B., Foley, B., Van Berkum, J. L., Long, A. H., Toneva, P., Ermina, M., and Klinkenberg, C. (2026). *National Ecological Footprint and Biocapacity Accounts, Edition 2026 (1961–2025): Results and metadata, version 1.0.* Footprint Data Foundation; York University and University of Iceland. https://footprint.info.yorku.ca/data/

The workbook specifies Creative Commons Attribution–ShareAlike 4.0 International: https://creativecommons.org/licenses/by-sa/4.0/ . Account-availability tables, corresponding account summaries and the derived coverage figure are distributed under the same licence. Processing comprises selection of 2015–2023, publication/completeness criteria, finite-value and component-consistency tests, and identification of the specified country subset. These outputs are adaptations, not provider-endorsed measurements of ecological change. The raw workbook is not redistributed.

## ESA CCI Biomass

Santoro, M., and Cartus, O. (2026). *ESA Biomass Climate Change Initiative: Global datasets of forest above-ground biomass for 2005–2012 and 2015–2024, v7.0.* NERC EDS CEDA. https://doi.org/10.5285/6429d1aafe1e43b9b414e4a5a7f8b903

The ESA Climate Change Initiative, Biomass CCI project and individual data providers are acknowledged. Data terms are specified at https://artefacts.ceda.ac.uk/licences/specific_licences/esacci_biomass_terms_and_conditions_v2.pdf . Producer intellectual-property rights and the source disclaimer apply.

Raw biomass files, the Product User Guide and the provider processing script are not redistributed. The guide has a separate restriction on reproduction. Source metadata, factual product definitions and exact hashes are supplied for identification and reproducibility. Product interpretation follows the guide's density denominator, observation domain and uncertainty definitions. The provider processing script was inspected for its mathematical and classification operations but was not executed.

## F04 additional support sources

Full published geoBoundaries country TopoJSON objects, represented years, commits, original hashes and upstream licences are retained; detailed attribution and the ODbL terms for OSM-derived support databases appear in `BOUNDARY_LICENCES.md`. These candidate polygons and their computational repairs are not authoritative legal or forest boundaries.

Copernicus Climate Change Service, *Land cover classification gridded maps from 1992 to present derived from satellite observations*, DOI 10.24381/cds.006f2c9a: public catalogue, form and constraints inspected on 29 October 2026. Their exact JSON snapshots identify the inspected endpoint availability; no land-cover raster or forest mask was obtained from that source.

F04 reads sixteen bounded native CCI Biomass 2015/2023 endpoint windows solely for fill/zero/valid support counts. Query payload hashes, bytes and the pre-request geometry-only plan identify the observations. The raw arrays are not redistributed, no global native-resolution raster was downloaded, and no country-level stock, change, conversion or performance estimate is supplied. The source metadata records the narrower inherited coarse-file inspection separately.

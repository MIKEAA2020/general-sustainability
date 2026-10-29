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


## F05 MapBiomas local cover and additional document review

Projeto MapBiomas – Coleção 11 da Série Anual de Mapas de Cobertura e Uso da Terra do Brasil, accessed 29 October 2026 through https://brasil.mapbiomas.org/downloads/. The FAQ at https://brasil.mapbiomas.org/faq/?tema=dados states that the data are public/free and usable with source attribution. No specific Creative Commons version was verified; this record does not invent one or impose a blanket replacement licence on upstream material.

Derived cover fractions/area tables and maps use the official Collection 11 class CSV, a declared grouping and conservative WGS84 intersections on the fixed local footprint. The bundled legend is attributed to MapBiomas; own processing does not imply provider endorsement. The original country rasters, raw range blocks and source method PDFs remain external and are not redistributed. Range receipts and immutable object identities document the partial source content actually used; no full-object hash from a partial download is claimed.

The source registry identifies downloaded documents and an aborted CCI ATBD attempt. Targeted review includes Collection 11 definitions, general temporal/validation methods and Cerrado training lineage, and CCI PUG PDF pages 21/59. Neither full-document reading nor comprehensive validation is claimed. See `brazil/source_review_F05.json` for page/topic scope. Historic F04/coarse-source records keep their narrower original scope; they must not be taken to mean F05 did not read cover arrays or inspect local endpoints. MapBiomas public reference downloads were labelled Collection 9, not independently verified Collection 11 validation. Separate publishers do not imply independent errors.


## F06 reference artifacts and corrected account figure

The MapBiomas reference download page https://brasil.mapbiomas.org/downloads/pontos-de-validacao/ was accessed 29 October 2026. The two inspected CSV/vector archives retain their exact URL, ETag, size, archive/member hashes and source field inventories in `reference/`. Raw archives and point-level source records remain external; own derived schema/completeness/consistency summaries are distributed with attribution. The same public/free-use-with-attribution FAQ applies; no specific upstream CC version is asserted. The XLSX alternative was not decoded; the two examined artifacts do not exhaust possible reference information.

The corrected account coverage figure is an adaptation of the same NEFBA 2026 account audit, under CC BY-SA 4.0. Only orientation, wrapping and layout change; original per-region counts remain exact. The inherited `account_coverage.pdf` is historical and is not used by the F06 article, which uses the uniquely named `account_coverage_F06.pdf`.


## F07 local allocation summaries and bounded workbook metadata

CCI Biomass v7.0 is credited under the existing CEDA terms. Two old Brazilian native payloads are retrieved again and verified against their exact F04 SHA identities; only own aggregate conditional allocation/auxiliary-mass summaries are redistributed, not the source density arrays. Pinned MapBiomas Collection 11 subsets are redecoded and verified against old subset/range hashes; derived integer overlap counts and own aggregate envelopes are supplied with MapBiomas attribution. These are transformed scientific summaries, not provider-endorsed forest estimates. Classification and density estimates are conditioned on, not validated.

The public Excel reference alternative is inspected through ETag-pinned HTTP206 ranges: ZIP directory, workbook and shared strings only. Full workbook size exceeds the 25MB transfer cap; worksheet size exceeds the full-member decompression guard. It is not opened or decoded. No full-object SHA from this partial access is claimed. Exact range and fully read metadata-member hashes identify the actual scope in `reference/xlsx_metadata_F07.json`. No raw workbook, byte blocks or source PDFs are redistributed; public/free source attribution conditions are unchanged.


## F08 complete XLSX representation and explicit author edits

The complete MapBiomas XLSX is downloaded under a documented workbook-specific limit exception, full-file SHA verified and one worksheet streamed in read-only mode without macro/formula execution. The source workbook and raw CSV remain external and are not redistributed. Own schema/completeness, source-equivalence summaries and member/source hashes are supplied with MapBiomas attribution. Full reading supersedes the current metadata-only status, not the historical F07 record. No extra validation/reference independence is inferred from duplicate representations.

The ORCID is copied from the unchanged ECOMOD C17 author metadata at the user's direction. The seven index terms and PDF keyword metadata are editorial additions. The AI declaration is replaced with the author's exact requested sentence and Arena.ai hyperlink; it is not represented as unchanged from F07. No old publication is edited. Current and unresolved source links are itemized in `INPUT_LINKS_F08.md`; HTTP HEAD success is distinguished from full retrieval/reading.

# Direct input links and access status — F08

Access checks: 29 October 2026. This list distinguishes an unreachable URL from a source stopped by an operational size limit, a source read only in part, and an intentionally bounded raster. It covers the known input gaps in this follow-up, not every possible external source. Raw upstream files are not redistributed in the package.

## 1. Excel retry: successfully fetched and completely streamed

**[Download the MapBiomas reference XLSX](https://brasil.mapbiomas.org/wp-content/uploads/sites/4/2024/08/mapbiomas_85k_col2_1_points_w_edge_and_edited_v1-2.xlsx-2.xlsx)**

- Full retrieval succeeded: **33,714,740 bytes**.
- SHA-256: `f4bec9d2eb624aff25efb0620476cebbb0e07eaefb699d03b40ef3efcf69ac62`.
- All **85,152 records** in the one worksheet were streamed; **135 fields**, annual class fields 1985–2023; no formula cells.
- All 117 common annual CLASS/COUNT/BORDA payloads match the CSV per identifier after documented serialization normalization. Both endpoint class tokens, coordinates and training-role tokens also match.
- The workbook repeats the **4,053 nonblank 2023 labels**, including 11 labelled `NÃO OBSERVADO`; all seven local 2023 labels are blank. It is not additional independent reference evidence.

The earlier stop was caused by a 25MB download / 250MB uncompressed-member guard, **not a broken download link**. F08 uses a documented XLSX-only 40MB / 400MB exception, leaving raster/native limits unchanged. The worksheet's uncompressed size is 371,343,772 bytes. Full retrieval/audit now supersedes the current metadata-only status; the old F07 record remains historically accurate.

Alternative formats and source page:

- [Reference download page](https://brasil.mapbiomas.org/downloads/pontos-de-validacao/).
- [CSV ZIP](https://brasil.mapbiomas.org/wp-content/uploads/sites/4/2024/08/mapbiomas_85k_col2_1_points_w_edge_and_edited_v1.csv_-1.zip) — retrieved/audited; SHA verified again for this comparison.
- [Vector ZIP](https://brasil.mapbiomas.org/wp-content/uploads/sites/3/2026/10/mapbiomas_85k_points_validation.zip) — fully audited in F06; 2023 class field absent and coordinate attributes reversed relative to geometry. Not independent evidence merely because the file format differs.

## 2. CCI Biomass ATBD v7: reachable, still unread

**[CCI Biomass Algorithm Theoretical Basis Document v7](https://climate.esa.int/documents/3351/Algorithm_Theoretical_Basis_Document_ATBD_V7.0.pdf)**

Current resolved download: [direct media PDF](https://climate.esa.int/media/documents/Algorithm_Theoretical_Basis_Document_ATBD_V7.0.pdf).

- F08 HEAD check: **HTTP 200**, declared **67,553,500 bytes** (67.6 MB).
- Earlier full-download attempt stopped at the 25MB guard. The PDF was not retained or read; this is **not evidence of an inaccessible document**.
- The Excel-specific exception does not silently authorize a larger limit for this PDF.
- No full-file SHA or source-reading claim is made from the HEAD response.

The [CCI Biomass key-documents page](https://climate.esa.int/en/projects/biomass/key-documents/) is the official starting point for other validation/intercomparison and uncertainty documents that have not been comprehensively reviewed in this study. No unverified individual download URL is invented here.

The [Product User Guide v7 PDF](https://climate.esa.int/documents/3352/Product_User_Guide_PUG_V7.0.pdf) was successfully retrieved and hash verified; targeted passages, including PDF pp 21 and 59, were reviewed. That is not an exhaustive ATBD/validation review.

## 3. Obsolete MapBiomas URLs: genuine 404s, with working replacement

These two paths were checked again in F08 and return **HTTP 404**:

- [Old terms path](https://brasil.mapbiomas.org/termos-de-uso/).
- [Old FAQ path](https://brasil.mapbiomas.org/perguntas-frequentes/).

Use the **[working official data FAQ](https://brasil.mapbiomas.org/faq/?tema=dados)** instead; F08 HEAD returns **HTTP 200**. Its public/free-use-with-attribution statements were read in the earlier source review. No particular upstream CC-BY version is asserted. A failed obsolete path does not mean the data or attribution information are unavailable.

## 4. Product endpoint gap, not a fetch failure

[Copernicus land-cover catalogue DOI](https://doi.org/10.24381/cds.006f2c9a): the catalogue/form snapshots inspected in F04 list epochs through 2022, not the required 2023 endpoint. This is the availability scope of the inspected product/version, not a broken URL or a claim that every possible 2023 land-cover source is unavailable. No 2023 download link is fabricated and no 2022 substitution is made.

## 5. Large rasters: accessible in bounded subsets, not downloaded whole

These are **not failed inputs**. They remain intentionally bounded:

- [MapBiomas Collection 11 Brazil 2015 TIFF, pinned generation](https://storage.googleapis.com/mapbiomas-public/initiatives/brasil/collection11/lulc/coverage/brazil_coverage/brazil_coverage-col11_2015.tif?generation=1787144389260083) — full object 720,792,833 bytes; only verified byte ranges decoded.
- [MapBiomas Collection 11 Brazil 2023 TIFF, pinned generation](https://storage.googleapis.com/mapbiomas-public/initiatives/brasil/collection11/lulc/coverage/brazil_coverage/brazil_coverage-col11_2023.tif?generation=1787146734212508) — full object 748,872,128 bytes; only verified byte ranges decoded.
- [CCI Biomass v7 data DOI](https://doi.org/10.5285/6429d1aafe1e43b9b414e4a5a7f8b903) — bounded native queries succeeded and their exact response hashes were verified; global native rasters were not downloaded.

Source bytes, generations, ETags, subset/range hashes and actual reading scope are recorded in the package metadata. Size deferral is not relabelled as a network failure. Successful retrieval or matching public representations is not independent scientific validation.

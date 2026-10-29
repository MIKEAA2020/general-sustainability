# F07 fixed-window conditional allocation envelopes and remaining XLSX check

Date 2026-10-29. This local specification is fixed before F07 reads native biomass payloads for mass summaries, redecodes cover pixels for topological certificates, or accesses XLSX ZIP members. Not external registration or untouched held-out evaluation. F04 native valid/zero distributions, F05 cover arrays/endpoints, F06 reference findings, third-party trends and product documentation were previously inspected. XLSX HEAD metadata are already known: 33,714,740 bytes, exceeding the standing 25 MB whole-file transfer cap. Prior raster arrays were necessarily read for earlier support calculations; no pristine outcome-naive claim is made.

## Unchanged scope and targets

Use exactly the 65,536 cells in the F04/F05/F06 Brazil rectangle, rows 105890–106145 and columns 146433–146688, 2015 and 2023. No moving/enlarging, country change, interval change, probability-sample claim, or national extrapolation. Report both existing mapped groups: formations [3,5,6,49] and formations-plus-savanna [3,5,6,49,4,7]. Plantation remains separate. These define different targets, not alternative confidence intervals. They are operational map-defined domains, not validated forest-land-use masks.

Native CCI density is expressed per full cell. Calculate auxiliary full-cell masses q_it = area_i * observed_density_it, with WGS84 cell areas. Jointly valid AGB/SD range and observed-zero treatment must match F04, with exact payload SHA verification. Missing/invalid cells must not be converted to zeros or removed without an explicit scope amendment. No native/global file download: two old bounded ASCII responses only, at most 25,000,000 bytes each.

## Allocation model and exact topology

Conditional on treating the published cover labels, native AGB estimates, grid and epochs as exact and exhaustive, allow any nonnegative biomass distribution inside a cell, with no finite subcell density cap, no common forest/nonforest mean, and no temporal allocation constraint. This is a minimal algebraic allocation model, not a physically complete ecological model or a measurement-error model. Extremal allocations need not be ecologically plausible.

For a cell wholly inside a mapped group, all full-cell mass belongs to that group; for a cell with no positive-area group intersection, none does; for a mixed cell the group mass can range from zero to the full-cell mass. Derive pure/absent/mixed certificates from INTEGER counts of fine pixels having positive-area intersections with each native cell, not from an ecological purity threshold or rounded near-zero/near-one fractions. Use source-grid overlap topology and the same pinned cover windows; verify their decoded SHA and array alignment against F05. Every fine tile/range must match the old source receipts. No class uncertainty is claimed to vanish because a cell is map-pure.

For each group/endpoint, report lower L_t = sum(map-pure q_it) and upper U_t = sum(map-present q_it). These aggregate all cells: using pure cells for the lower endpoint is not a persistent-pure-only sample. Report the complete interval [L_t,U_t] and the compatible endpoint difference [L_2023-U_2015,U_2023-L_2015]. Show whether zero is contained without selecting a group or sign. Do not use nominal AGB-SD as a covariance model, compute a confidence interval, claim calibrated change resolution, or identify actual forest stock. Report auxiliary whole-window mass only with its full-pixel/domain label; it does not replace the primary forest stock. No forest extent–density point decomposition or account–asset divergence is computed.

## XLSX remaining alternative

Do not download the full 33.7 MB workbook or increase the 25 MB cap. Attempt strict ETag/Content-Range HTTP206 access to ZIP directory, workbook, shared-string and initial sheet/header metadata, with a tighter 2,000,000 distinct-byte cap for this inspection. Enforce ZIP member decompression limits (250 MB/member, 500 MB total), stream initial worksheet rows and avoid whole-sheet decoding. Do not claim overall row completeness, compatible 2023 labels, file equivalence or independent validation from a schema/prefix inspection. If ranges are ignored or metadata exceed the cap, stop and record that limitation. The workbook remains an unaudited full reference population; no local reference/map accuracy is calculated.

## Reporting and uncertainty

Publish numerical envelopes with assumptions and units; keep map/biomass measurement errors, classification/epoch mismatch and reference absence explicit. Allocation bounds are neither 95% intervals nor guaranteed bounds on true forest biomass. All national physical admissions remain on hold, with no permanent exclusions. Prior documents/frozen rules and author AI declaration remain unchanged; F07 updates active scientific results and external records separately, never rewriting old published packages.

# F05 bounded Brazil land-cover support specification

Date: 2026-10-29. This supplements, not replaces, the retained empirical protocol. It is not an external registration or a claim of outcome-naive design.

## Target and sequence

Use exactly the F04 Brazil native biomass window (rows 105890–106145, columns 146433–146688). Do not move or enlarge it after inspecting land cover. The two endpoints remain 2015 and 2023; no national population, country selection or comparison interval changes. This window is a deterministic local support demonstration, not a national probability sample.

Collection 11 metadata, its official code legend, the three-page class descriptions, targeted processing/validation sections of the general ATBD and targeted Cerrado methods have been inspected before decoding the two land-cover pixel windows. TIFF headers were inspected first; no raster class array was decoded before this specification and its class configuration were frozen. The known F04 native biomass valid/zero distributions and published third-party trend headlines were already accessible. Subsequent results must not be portrayed as an untouched held-out evaluation.

## Fixed classification definitions

Use the current official Collection 11 code CSV, not a legacy collection's labels. Preserve every source class in a per-class summary. Use these disjoint support groups:

- Mapped forest formations: codes **3, 5, 6, 49** (Forest Formation, Mangrove, Floodable Forest, Wooded Sandbank Vegetation).
- Savanna formations, kept separate: **4, 7** (Savanna Formation, Flooded Savanna beta).
- Forest plantation: **9**, kept separate.
- Open water: **33**, kept separate.
- Other listed mapped classes: all remaining codes in the official CSV.
- Unobserved/unclassified: **0 and 27**, distinguished from observed nonforest and zero biomass. Code 27 is a legacy unobserved convention, not a listed Collection 11 cover class. Its occurrence must be reported, not interpreted as forest/nonforest.
- Any other code is unexpected and causes a closed failure pending source review.

The formations group is a transparent operational cover definition, not a claim to have identified all FAO forest land use, all ecological capital or the provider's entire higher-level forest category. Save a separate sensitivity fraction adding savanna codes, and a separately labelled fraction including plantations. No threshold will be selected to obtain an account–asset sign or a preferred biomass result. The reference class definitions and biome-specific crosswalks, including wooded savanna and temporarily unstocked land, still require substantive harmonization before a national forest-land-use interpretation.

## Retrieval and grid alignment

Pin the 2015 and 2023 objects by the Google object generations and ETags already discovered in F04. Retrieve only HTTP byte ranges needed for TIFF metadata and the bounded land-cover window; refuse a full-body 200 response, wrong Content-Range, changed ETag, missing cache hashes or more than 25,000,000 distinct bytes per endpoint. Do not download the 0.72/0.75 GB country images. Raw byte blocks remain in the external cache; source ranges and their digests identify them.

Read the native geographic pixel scale, tiepoint, CRS, pixel-area convention and any no-data metadata from the TIFF rather than assuming a 30 m equal-area grid. Require compatible WGS84 north-up endpoint grids. Include every fine pixel intersecting the fixed biomass rectangle. Clip overlaps analytically; do not label pixels by nearest-neighbour assignment or treat nominal spacing as constant area.

For each biomass cell and cover group, sum WGS84 intersection areas of the mapped finer pixels and divide by that biomass cell's full WGS84 area. Longitude overlap and the ellipsoidal latitude-area primitive give separable weights. Fractions must be nonnegative and sum to one across the disjoint groups; the mapped fine-pixel group area must agree with the sum of coarse-cell fractions times cell areas. Missing/unknown support retains its own fraction and is not silently renormalized away.

Save endpoint fractions, source/class area summaries and common mapped-support descriptors. Pure-cell, union and intersection masks are descriptive only. They must not replace all changing forest strata with a persistent-forest-only sample, which would exclude conversion by construction.

## Interpretation and limits

Local mapped-cover endpoint areas will be inspected and disclosed; national or validated forest-change outcomes, biomass stocks/changes, account–asset signs and transition associations are not estimated in this pass. Do not call mapped endpoint area differences independently validated ecological change.

CCI's native AGB is a full-pixel density and is not forest-masked. Multiplying it by a finer forest fraction does not identify the forest-only biomass within a mixed pixel. A finer matched stock observation, an explicit validated allocation model, or defensible bounds would be required. A homogeneous mapped-forest pixel is not ground-truth forest.

MapBiomas temporal filtering/gap filling can use adjacent years and alters timing; nominal endpoint labels are not exact synchronous observations. Provider overall map accuracy is not transition accuracy, a local confidence probability or a 95% biomass-change guarantee. Public reference downloads labelled Collection 9 must not automatically be treated as independent Collection 11 validation, especially where training/reference samples overlap. Any shared auxiliary information with the biomass product must be traced; different publishers do not establish independent errors. Dependence, where present, requires joint error assessment rather than an unsupported independence assumption.

All eight national physical admissions remain on hold. This pass freezes a bounded mapped-cover support demonstration, not a national analytical forest sample.

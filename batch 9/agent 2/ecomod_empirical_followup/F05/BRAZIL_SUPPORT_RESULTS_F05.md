# F05 — bounded Brazil mapped-cover support results

## Scope and observations

MapBiomas Brazil Collection 11, endpoints 2015/2023, is aligned to the unchanged F04 CCI native biomass window: zero-based inclusive rows **105890–106145**, columns **146433–146688**. There are 65,536 native cells and a WGS84 footprint of **61,830.34356250836 ha**. This geometry-selected rectangle is not a national probability sample, forest-targeted location or national coverage estimate. Candidate countries, account rules and both study intervals are unchanged. All eight national physical admissions remain on hold.

The group configuration, official legend and bounded protocol were frozen before land-cover array decoding; TIFF headers, F04 support counts and third-party trend information were already known. Local cover arrays, local endpoint areas and spatial patterns have now been inspected. Those outcomes are not pristine held-out data. The local freeze is not an externally registered preregistration or independently timestamped registration.

## Exact endpoint quantities

| Disjoint group | 2015 ha | 2023 ha |
|---|---:|---:|
| Forest formations: 3, 5, 6, 49 | 4319.251708208100 | 4510.427741642644 |
| Savanna: 4, 7 | 7850.461451801662 | 6924.898458943958 |
| Plantation: 9 | 10.663425590593 | 16.905321765590 |
| Open water: 33 | 244.516181385062 | 320.456445784337 |
| Other listed mapped classes | 49405.450795522940 | 50057.655594371830 |
| Unobserved: declared 0, 27 convention | 0 | 0 |

Formations plus savanna, a non-disjoint additional quantity, is **12,169.713160009762 → 11,435.326200586602 ha**. Formations-only percentages are **6.9856505064% → 7.2948450255%**; formations-plus-savanna percentages are **19.6824284952% → 18.4946832602%**. Both are reported; opposite endpoint directions concern different target groupings, not alternative confidence bounds on one target. Neither establishes validated ecological change, national forest decline/gain or account–asset divergence. The complement is not absence of ecological assets.

Exact per-class clipped areas and window pixel counts are in `data/brazil/source_class_areas.csv`; disjoint group summaries are in `endpoint_support_areas.csv`. The NPZ contains both endpoints' group fractions, separately labelled formations-plus-savanna and formations-plus-plantation fractions, target coordinates and cell areas: twenty arrays in total.

## Mixed support and selection

- Complete published-label support at both endpoints: 65,536 target cells.
- Nonzero formations at either endpoint: 13,301 cells.
- Nonzero formations at both endpoints: 10,385 cells.
- Mapped-pure formations at both endpoints: 625 cells.
- Mixed formations cells: 10,865 (2015), 11,154 (2023).

The 1e-9 zero/one tolerance is numerical, not an ecological/detection threshold. Persistent/pure-only selection was **not** used. Such selection would omit mixed and changing strata, including the conversions sought by the study. Published-label completeness is not proof of cloud-free direct annual observation: Collection 11 has temporal filters and adjacent-year gap filling.

## Area and retrieval verification

Each finer source subset is 846 × 845, with all partial fine-cell overlaps retained. Both endpoints have the same WGS84 pixel-area grid. Exact angular/ellipsoidal overlap, rather than a nominal equal-area 30 m or 100 m assumption, is used.

- Distinct source bytes accessed, including TIFF metadata: **4,521,984 / 4,587,520**.
- Whole images: **720,792,833 / 748,872,128** bytes; not downloaded whole.
- Maximum group-fraction partition error: 3.3306690738754696e-16.
- Maximum overlap-weight partition error: 2.220446049250313e-16.
- Maximum direct-fine versus coarse-fraction area closure error: 2.635351847857237e-8 ha.

These are arithmetic checks, not classification validation or uncertainty estimates. Generation/ETag-pinned HTTP 206 range access, cached block hashes and a 25 MB distinct-byte cap per endpoint are enforced. Full-object content hashes were not computed from partial downloads; range hashes, decoded-subset hashes and immutable object identities describe what was actually read. Cached reproduction with network disabled gave exact equality of all twenty arrays and byte-identical CSV/JSON scientific summaries/provenance.

## Why forest-only biomass remains unidentified

CCI's native density refers to the full pixel and is not forest-masked. For a mixed cell, observing total biomass and forest fraction leaves two component densities unknown. A fraction-times-total calculation imposes a within-cell biomass allocation model; it is not justified by finer forest area alone. F05 computes **no** biomass stock or change. Native zeros are not treated as nonforest. Whole-territory woody biomass is a different estimand from forest-only biomass; stock and extent operands must match before using an extent–density decomposition. The primary study target has not been silently replaced with a whole-land stock.

## Source, timing and validation limits

The current Collection 11 CSV, not a remembered older legend, defines codes 6 (Floodable Forest) and 49 (Wooded Sandbank Vegetation). The formations group is operational cover, not universal forest land use or all woody natural capital. Savannas, plantations and temporarily unstocked forest need explicit substantive treatment before national harmonization.

The general ATBD reports interpreted reference observations through 2024 in its validation section while other collection scope descriptions extend through 2025. Inspected public reference downloads are explicitly Collection 9. Global overall classification accuracy is not local class/transition accuracy, stock-change confidence or a calibrated 95% rule. Training reuse, reference roles, probability weights and compatible Collection 11 labels remain to be audited.

Cerrado methods identify GEDI-derived height in training-mask refinement; CCI's PUG describes LiDAR-informed allometric development. This is potential shared auxiliary lineage, not demonstrated identical local footprints or measured error covariance. Different publishers do not establish error independence. The CCI ATBD request exceeded the 25 MB guard, was aborted, and was not read. Targeted PUG pages 21/59 were read instead; no exhaustive product-validation review is claimed.

MapBiomas Project, Collection 11, accessed 29 October 2026: https://brasil.mapbiomas.org/downloads/. The official FAQ https://brasil.mapbiomas.org/faq/?tema=dados permits public/free data with source attribution; no specific upstream CC-BY version was verified. Raw source rasters/PDFs are not redistributed. Per-source hashes, reviewed passages and restrictions are recorded in `metadata/brazil/` and `metadata/SOURCE_USE.md`.

## Remaining scientific tasks

Resolve national territory/land-use correspondence; extend bounded support acquisition appropriately rather than extrapolating this location; audit independent reference availability and input overlap; resolve the forest-only density/allocation target; quantify class/transition, spatial and temporal uncertainty; obtain full analytical coverage and record admissions/exclusions. No national forest estimate, biomass estimate, conversion association, divergence prevalence, performance or quality calibration is supplied. F05 is a concrete local support result within the unfinished intended empirical study, not completion of that study.

# F07 — conditional allocation envelopes on the unchanged Brazil window

## What is newly computed

F07 uses the same 65,536 native CCI cells, rows 105890–106145 and columns 146433–146688, endpoints 2015/2023, footprint **61,830.34356250836 ha**. The two exact F04 biomass payloads and both F05 cover subsets/range hashes are verified again. Earlier zero/valid distributions and cover outcomes were known; this is not untouched held-out evaluation.

Unlike earlier support-only calculations, F07 now computes auxiliary full-cell masses and conditional map-domain biomass-allocation sets. Current scope statements distinguish these actual local mass summaries from unestimated national or validated forest-stock changes. The primary forest target has not been silently replaced with whole-territory biomass.

## Model and scientific interpretation

Treat the published density estimates, cover labels, grid and epochs as exact for this exercise. For a full-cell mass q, a map-absent group receives zero and a map-pure group receives q. A mixed group's share may be anywhere in [0,q], under nonnegativity without finite component-density caps or temporal allocation restrictions. Every such allocation is attainable in that minimal algebraic model. This is not a complete ecological model: some extreme component densities may be implausible, and additional justified ecological constraints could narrow the set.

Sum pure-cell masses for the lower endpoint L and all map-present cell masses for the upper endpoint U. With no temporal restrictions, the difference set is [L2023 − U2015, U2023 − L2015], not the difference of two lower or two upper endpoints. These are **conditional allocation sets**, not 95% intervals, posterior intervals, validated forest stocks or guaranteed bounds on true biomass. Measurement/classification error, covariance, reference uncertainty and epoch mismatch are not calibrated here.

## Actual results, Mg of above-ground woody biomass

| Operational mapped domain | 2015 [L,U] | 2023 [L,U] | Difference [lower,upper] |
|---|---:|---:|---:|
| Formations: 3,5,6,49 | [44,230.3263, 279,193.2047] | [55,221.5525, 326,232.3438] | [−223,971.6521, +282,002.0175] |
| Formations + savanna: add 4,7 | [229,754.7757, 434,473.2029] | [256,363.4059, 489,288.5391] | [−178,109.7970, +259,533.7634] |

Both difference sets contain zero. Negative, zero and positive differences remain compatible with the minimal allocation model even before measurement uncertainty is introduced. The group definitions differ; they are not competing confidence intervals for a common forest target. Forest plantations remain separate. These operational classes do not certify all forest land use or ecological assets.

Auxiliary full-window mass sums are **463,922.52584046 Mg** and **529,164.8923703252 Mg**. These refer to all native cells, not forest-only stock; their positive difference cannot be labelled a forest-specific gain or used as a substitute primary asset result. No forest-fraction-times-whole-cell-density point estimator is used, and no forest extent–density point decomposition or account–asset divergence is computed.

## Exact topological certificates, not a purity threshold

| Group | 2015 pure / mixed / absent | 2023 pure / mixed / absent |
|---|---:|---:|
| Formations | 791 / 10,865 / 53,880 | 876 / 11,154 / 53,506 |
| Formations + savanna | 6,056 / 16,450 / 43,030 | 5,616 / 15,936 / 43,984 |

Every row totals 65,536. Integer counts of fine pixels with strictly positive geometric overlaps distinguish absent, pure and mixed cells. Near-zero or near-one fraction thresholds are not used to anchor mass bounds. All target cells and changing/mixed support remain included; the persistent-pure intersection is not the sample. The maximum fraction alignment discrepancy against F05 is 3.3306690738754696e−16. This is arithmetic consistency, not ecological classification accuracy.

Native AGB and SD remain valid everywhere in this window, with observed zero-density counts **44,546 / 44,767**, exactly as in F04. Zeros remain observed valid values, not nonforest labels. No missing values are zero-filled or silently dropped.

## Source scope and transfer limits

Two native ASCII responses total **840,183 bytes**. Cover metadata/tiles require **4,521,984 / 4,587,520** distinct source bytes, matching F05 source receipts. Full country cover images and global native rasters are not downloaded. Source files remain external; aggregate mass sets, six derived topology-count arrays, checksums and methods are distributed.

CCI Biomass v7.0, Santoro and Cartus (2026), DOI 10.5285/6429d1aafe1e43b9b414e4a5a7f8b903, is acknowledged under its existing source terms. MapBiomas Project, Collection 11, accessed 29 October 2026 through https://brasil.mapbiomas.org/downloads/, supplies the mapped classes. Processing: declared grouping, WGS84 area overlap, integer topology and stated allocation model. Public/free use with attribution follows the official FAQ; no upstream CC version is invented. Raw rasters, density arrays, source PDFs and byte caches are not redistributed.

## Remaining Excel alternative: bounded metadata only

The linked XLSX is **33,714,740 bytes**, beyond the unchanged 25 MB whole-file cap. Its worksheet declares **371,343,772 uncompressed bytes**, beyond the 250 MB full-member decompression guard. Neither cap was increased.

Strict ETag/Content-Range-pinned HTTP206 requests accessed **160,308 distinct source bytes**, below a separate 2 MB metadata cap. Only ZIP directory, workbook and shared-string metadata were decoded. The worksheet was not opened or decoded. A shared-string token's presence or absence cannot certify a populated worksheet column, completeness or reference-year coverage. No full-file content hash from this partial access is claimed; range and fully read metadata-member hashes identify what was actually inspected.

The complete Excel reference population therefore remains unaudited. No file equivalence, extra local paired labels or independent validation is claimed. F06's actual CSV/vector findings remain unchanged and do not exhaust all possible reference information. A complete XLSX audit would require a separately approved/recorded limit decision or a suitably bounded alternative representation, not a silent cap increase.

## Reproduction and remaining work

```sh
python src/allocation_envelopes.py --cache /your/external/F07-source-cache
python src/xlsx_reference_metadata.py --cache /your/external/XLSX-range-cache
# Forbid HTTP after the source caches have been filled:
python src/allocation_envelopes.py --cache /your/external/F07-source-cache --offline
python src/xlsx_reference_metadata.py --cache /your/external/XLSX-range-cache --offline
python -m unittest discover -s tests -v
bash src/build.sh
```

`protocol/ALLOCATION_ENVELOPE_F07.md`, configuration and input identities precede the new mass summaries/XLSX range inspection. F07 outcomes are now inspected and disclosed. This local freeze is not external registration. Cached scientific CSV/JSON and topology arrays are checked against a network-disabled reproduction; tests concern computation and scope, not ecological accuracy.

All eight national physical admissions remain **on hold**, with no permanent exclusions. Needed next: compatible paired reference information with source-specific classes and training/inclusion provenance; justified forest-only observation/allocation constraints; national territorial/land-use support; full valid/missing/converted coverage; covariance-aware measurement uncertainty and change validation. No national forest/biomass estimate, calibrated local forest change, conversion association, divergence prevalence or reporting-rule performance is supplied.

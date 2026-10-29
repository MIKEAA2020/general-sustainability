# Dependency-ordered empirical follow-up — R03

**Date:** 29 October 2026. **Instruction:** pursue all genuinely merited items in topological order, prioritizing feasibility. **Result:** all three branches were investigated; two produced new bounded empirical/reference findings, while production aggregation-code provenance remains unresolved. These results support a new F10 manuscript, not a revision of F08/F09.

## 1. Dependency graph and stopping rules

1. **Source/implementation identity → interpret uncertainty correctly.** Reverify the distributed change script, inspect the official v7 directory and follow actual code links rather than implementing an inferred correction to the printed equations.
2. **Reference catalogue/version → dates/support → eligibility → possible comparison.** Check current accessibility and archive structure, then fixed-footprint/reference quality. Do not calculate map–reference performance when an earlier prerequisite fails.
3. **Native variable definitions and source identity → bounded SD diagnostics.** Reuse the unchanged geometry and hash-matched original observations. Describe stored uncertainty without treating it as calibrated error or inferring error correlation from map correlation.

Branches 2 and 3 can proceed descriptively without resolving production aggregation code. Calibrated change inference cannot. All country admissions remain on hold.

## 2. Executable-method tracing: what was established

### 2.1 Distributed change script

The official [v7 directory](https://dap.ceda.ac.uk/neodc/esacci/biomass/data/agb/maps/v7.0/) lists `create_change_maps.py`, not a production aggregation script. The [distributed script](https://dap.ceda.ac.uk/neodc/esacci/biomass/data/agb/maps/v7.0/create_change_maps.py?download=1) was retrieved and matches the previously recorded full SHA-256 exactly:

`ab579be84610210bc5a8a9eb75c6f3e2529bca91ca5f27795dbcfc71bbe02401` — 8,390 bytes.

Static AST/line inspection confirms:

- **line 113:** change SD is the square root of the sum of squared endpoint SDs, without cross-year covariance;
- **line 117:** the endpoint interval multiplier is one;
- **line 141:** the annual increment constraint is 10 Mg/ha/year;
- **line 170:** the generated GeoTIFF quality-flag band's NoData value is set to **0**, while the same script assigns quality class 0 when both endpoint AGB estimates are zero.

That last convention matters for software that automatically masks a raster's NoData value: a target-derived both-zero category can be hidden as missing. It is **not** proof that the released NetCDF products have the same NoData convention. The inherited coarse NetCDF metadata instead records fill value −32768. Neither class 0 nor NoData establishes true ecological absence. This static audit does not execute the provider script or validate its classifications. The script reads input rasters as whole arrays, another reason not to run it on unbounded global files.

### 2.2 Article-linked code is not production aggregation code

The [2024 Scientific Data article](https://doi.org/10.1038/s41597-024-03930-9) repeats the printed increasing lag-correlation expression and links a [Biomass Harmonization code folder](https://github.com/CEOSBiomassHarmonization/NASA_CMS/tree/main/NASA_CMS_2023/Hunka_2024_NSD) and [Zenodo record](https://zenodo.org/records/13346188). The actual linked folder was inspected at commit:

`514c4f0ed747652f312f2b570e79d2d4e2b7e252`.

All 14 files in that folder were retrieved with Git-blob identity checks. Its README and executable content concern forest classification and layer alignment. No implementation of the 0.0445 spatial kernel or CCI production uncertainty aggregation was identified there. The linked Zenodo file list likewise concerns the classification workflow. This is a scoped negative finding, **not a claim that no aggregation code exists anywhere**. The article's use of an earlier CCI release also does not verify the v7 pipeline.

The AGBref preprint links [Plot2Map](https://github.com/arnanaraza/Plot2Map). Selected documentation and validation-tool functions were inspected at commit:

`496290680d00eaf4a0fdcf313e4d91770660d447`.

`SpatCor.R` lines 113–118 take a mean over an N × N array of terms before the square root, giving N⁻² normalization of that array. This is relevant executable validation-tool evidence, but it does **not** identify the production implementation behind E3UB's displayed equations. Its model, units and missing-value operations are not adopted as a local calibrated model. The printed normalization/correlation discrepancies therefore remain unresolved at production-code level.

Specific provider questions are prepared in `PROVIDER_QUESTIONS_R03.md`. They have **not** been sent.

## 3. Reference feasibility: a real new local candidate, not an eligible pair

### 3.1 Follow the version chain, not the preprint's access claim

The [AGBref preprint](https://doi.org/10.21203/rs.3.rs-8211898/v1), posted 9 January 2026, describes harmonized reference stocks and quality filters. It is a **preprint**, not treated here as an accepted Scientific Data article. Targeted PDF reading covered preprocessing, quality criteria, uncertainty and data/code availability, particularly PDF pp. 7–8 and 15–16. The descriptor discusses growth-rate adjustment of references within ten years of target epochs; its future repeated-measurement priority does not establish that every multi-epoch aggregate is a repeated field census.

The originally cited [Zenodo record 15495069](https://zenodo.org/records/15495069) currently has restricted access and its file endpoint returned 403. Following its actual latest-version link revealed [open record 20793072](https://doi.org/10.5281/zenodo.20793072), modified September 2026, under CC BY 4.0. It contains `agb-ref-v2.zip`, advertised size **50,273,714 bytes**. The whole archive was not downloaded.

### 3.2 Bounded archive inspection

Under a written source-specific protocol, the complete ZIP directory and four selected CSV members were inspected:

- `AGBref_2010_500m.csv`;
- `AGBref_2015_500m.csv`;
- `AGBref_2020_500m.csv`;
- the undated `AGBref__.csv`, inspected specifically to avoid assuming that an unnamed member could not contain a newer epoch.

Each selected CSV has **200,152 rows**. The directory lists named epochs 2005, 2010, 2015 and 2020; no named 2023 member is present. The unnamed member has no Year field and cannot be assigned to 2023. Other spatial-resolution data values were not decoded.

The inspection represented **22,551,986 distinct source bytes**, below the unchanged **25,000,000-byte** cumulative source guard. Complete selected-member CRC32 checks and SHA-256 identities were recorded. **The whole ZIP's advertised MD5 was not verified.** The server provided no strong ETag and omitted Last-Modified on 206 responses. The explicitly recorded partial-identity policy used the immutable numeric-version URL, exact Content-Range/total size, conditional requests, range hashes, complete-member CRC, and catalogue checksum plus HEAD size/date rechecks before/after. These are not described as full-file cryptographic identity verification. The initial stricter header probe read no body when its required response validator was absent.

### 3.3 Fixed-footprint result

The fixed native rectangle is unchanged: rows 105890–106145, columns 146433–146688. Its bounds are approximately **49.8373°W–49.6098°W, 14.3520°S–14.1244°S**.

Each selected CSV contains **one centroid inside** that rectangle, at **49.6825°W, 14.2175°S**. These are released aggregate-cell coordinates, not newly recovered original plot coordinates. Twelve centroids occur within a separately labelled 0.25° padded screening rectangle; the target was not moved to include them. A centroid query is not a polygon-overlap/representativeness validation.

For the labelled 2010/2015/2020 local aggregate:

- `N = 1`;
- `AGB_T_HA = 0`;
- `QUALITY_MIN_PLOTS = 0`;
- `QUALITY_LARGE_SIZE = 0`;
- `QUALITY_LOCALLY_REP = 0`;
- `QUALITY_STRICT_FILTER = 0`;
- timeliness is 0 for 2010 and 1 for 2015/2020;
- SD is approximately **22.55, 22.55 and 23.02 Mg/ha**, respectively.

The preprint's 500 m minimum criterion is **more than one plot**, so this aggregate fails that support criterion irrespective of the meaning of its zero stock estimate. The exported original census date, source-provider code and original plot identity are absent; `Year` is a target-epoch label. Local aggregate IDs also **differ across the three epoch files**, despite identical centroids. Neither joining those IDs nor joining centroids establishes a repeated observation of the same trees/plots. The unnamed row does not supply a missing date or a fourth independent observation.

The actual selected columns also differ from some catalogue/descriptor field inventories: e.g. the selected CSVs omit `AVG_YEAR`, `CODE` and `AGB_T_HA_ORIG`. No fields are invented or silently reconstructed. The result improves on a generic statement that no reference information exists locally: **an accessible local candidate exists, but does not satisfy the primary paired-change requirements**. Even the secondary 2010–2020 fine-support comparison fails the observed minimum/local-quality conditions. Coarser-resolution candidates were not assessed or declared unsuitable on that basis.

A limited, attributed four-row derived subset is supplied in `data/local_reference_candidate_R03.csv`. No map–reference discrepancy, confusion rate, paired biomass difference or calibration is calculated from these rows. Their zero estimates are not recoded as missing or interpreted as true absence.

### 3.4 Other reference leads screened before costly downloads

| Lead | Verified observation dates/context | Feasibility decision for the fixed primary target |
|---|---|---|
| [SLB/ORNL DAAC 1644](https://doi.org/10.3334/ORNLDAAC/1644) | Guide PDF p. 2: June 2008–August 2018; most sites single acquisition, some repeated | No 2023 endpoint; no large point clouds downloaded |
| [Irati tree census 22133098](https://doi.org/10.5281/zenodo.22133098) | Open metadata/README: 2023 and 2026, southern Brazilian urban remnant | No 2015 endpoint and different regional support; no need to download the workbook |
| [BIONTE inventories](https://doi.org/10.15486/ngt/1898910) | [OSTI metadata](https://www.osti.gov/dataexplorer/biblio/dataset/1898910): observations 1990–2019, central Amazon | Publication in 2023 is not a 2023 census; no matching endpoint/support established |

This is a targeted feasibility screen, not an exhaustive claim that suitable reference data do not exist worldwide.

## 4. Native endpoint SD diagnostics on the unchanged window

The original F04 requests already contained **both AGB and `agb_sd`**. The same two original payloads were recovered and matched in full to the previously published SHA-256/byte identities before decoding. There was no new rectangle, no nationwide download and no outcome-based reselection.

Both endpoint files report integer-valued AGB/SD in Mg/ha, fill −32768 and valid range 0–10000. All **65,536 cells** have valid nonnegative values in both layers at each endpoint. The native variable list contains no separate forest mask, zero-origin label or covariance field. The AGB `ancillary_variables` attribute names `agb_se`, although the listed uncertainty variable is `agb_sd`; this metadata mismatch is recorded, not repaired.

| Stored-data diagnostic | 2015 | 2023 |
|---|---:|---:|
| AGB = 0 | 44,546 | 44,767 |
| SD = 0 | 45,578 | 45,713 |
| AGB > 0 and SD = 0 | **1,032** | **946** |
| AGB = 0 and SD > 0 | 0 | 0 |
| Positive AGB at SD = 0: observed range (Mg/ha) | 1–4 | 1–4 |
| Median SD among positive-AGB cells (Mg/ha) | 6 | 7 |
| Positive-AGB SD interquartile range (Mg/ha) | 3–12 | 3–14 |

There are **44,021 cells with stored AGB = 0 at both endpoints**. That is a stored-value state, not independently observed persistent nonforest. The other zero/nonzero states are 525 zero→positive, 746 positive→zero and 20,244 positive→positive. These counts are not land-cover transitions or validated ecological gains/losses.

The stored-zero SD cases show why integer precision, masking/retrieval conventions and ecological absence must be separated. Rounding, truncation, clipping, model assumptions and masking are possible explanations, **not established causes here**. No native quantization rule or zero-origin provenance is verified. A zero SD therefore does not establish zero true error, exact biomass or a confidence interval with zero width. No error-correlation estimate is obtained from correlation of the maps or their SD layers. These observations do not solve mixed-cell forest allocation.

## 5. Scientific consequences and next dependency

- **Integrate supported facts into F10:** actual stored-SD patterns and the newly located but ineligible local aggregate reference. Preserve every earlier numerical result and author control.
- **Do not apply an inferred provider kernel:** production normalization/correlation implementation remains unverified. No additional covariance coefficient, error floor or bias correction is invented.
- **Do not promote candidate presence into validation:** require compatible actual census dates, original observation identity/reuse, adequate representation and the intended forest/whole-cell support.
- **No automatic national admission:** all eight holds remain; no country biomass trend, calibrated local change interval or divergence prevalence is estimated.
- The next substantive dependency is provider clarification/production-code provenance and genuinely eligible repeated reference observations. Prepared questions identify exactly what evidence would close those gaps. No outbound communication was sent.

Raw PDFs, full source code, full reference CSVs, native arrays and range blocks remain excluded cache. The publication package contains our analysis, limited derived data, source metadata, guarded reproduction code, tests and preservation checks. Technical/source checks are not ecological validation.

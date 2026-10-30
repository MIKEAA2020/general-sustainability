# Canada NFI depository search and SBFI fitness assessment

**Verification date:** 30 October 2026  
**Status:** Additive evidence clarification; no prior package, static result or generator result is replaced.

## Bottom line

The defensible conclusion is narrower than “the exact fields are not publicly deposited anywhere.”

1. **Exact `var_biom` and `sep_biom` fields are publicly archived in our original GitHub audit.** Three [current-generator WRT snapshots](https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/deeper_source_audit_2026-10-30/data/canada_wrt) returned HTTP 200 from their public raw URLs and were byte-identical to the frozen local files. They contain 58 national point, 58 national change and 550 ecozone change rows, with both fields present. They are **current-generator snapshots, not Version 3.1 static-run tables**.
2. **No independent, provider-issued, version-matched static deposit was located in the bounded searches.** Exact-phrase Zenodo and Figshare searches returned zero metadata hits for each field. GitHub’s combined `var_biom` + `sep_biom` code search returned 16 indexed files, all in our audit repository; three are the current-generator snapshots and the remainder are scripts, diagnostics or documentation. This does not prove universal absence.
3. The named [`designing_national_forest_inventories`](https://github.com/robertwbuchkowski/designing_national_forest_inventories) repository is confirmed as a **code-only soil-carbon design analysis**, not a biomass data deposit. At commit `5ec0687a9813f384b8ad76c3a10f0982a52f617c`, its tree has 15 entries/14 blobs, including ten R scripts and no data files. The README says the necessary data must be requested from the NFI. Across its README and R scripts, `var_biom`, `sep_biom` and even `biom` have zero occurrences; its variance routines concern soil-carbon change. Its [Zenodo archive](https://zenodo.org/records/17976777) likewise contains ten R scripts and no data deposit.
4. The identified SBFI product is **[Zenodo record 19357316](https://zenodo.org/records/19357316)**, DOI `10.5281/zenodo.19357316`, published 1 April 2026 under CC-BY-4.0. It contains one **11,800,441,690-byte** file, `SBFI_AGB_2020.zip`. The archive was **not downloaded wholesale**: byte-range inspection listed 2,378 entries using 815,962 bytes, followed by selective metadata and one-tile schema retrieval.
5. Two layers were inspected directly: `CA_2020_tile_179_metrics` (**2,101 stands**) and the smaller reproduction target `CA_2020_tile_705_metrics` (**7 stands**). Both have the same **209 field names**, including 85 AGB-related fields and ten `_SD` fields such as `STRUCTURE_AGB_SD`, but neither contains `var_biom`, `sep_biom`, RSE, confidence-interval or uncertainty-estimate fields. Sixteen species 1–4 component-percentage fields nevertheless differ in numeric storage type between tiles (`float64/OFTReal` versus `int32/OFTInteger`); this must be harmonized before cross-tile pooling. Both complete schemas and the archive inventory are preserved.
6. SBFI `_SD` values must not be relabelled as estimator uncertainty. The [2024 SBFI methods paper](https://doi.org/10.1093/forestry/cpad065) defines them as descriptive statistics calculated from pixels **within each stand/polygon**. They are not NFI sample-design variances, standard errors, relative standard errors or successive-period covariances.
7. The [2026 component data note](https://doi.org/10.1080/07038992.2026.2713280) states that aggregated SBFI metrics suit broad descriptive spatial patterns but are **not intended to support formal statistical inference**, and urges caution where formal uncertainty quantification is required. This directly confirms the fitness boundary.

## What SBFI can—and cannot—do while awaiting static evidence

| Use | Assessment |
|---|---|
| Biomass-component accounting by species, stemwood, bark, branches, foliage and non-treed pools | **Appropriate descriptive use.** The 2020 product constrains treed component proportions to sum to one. |
| Cross-tile component pooling | **Run schema QA first.** Sixteen percentage fields have different storage types in the two inspected tiles; harmonize them before analysis. |
| Within-stand spatial heterogeneity or exploratory sensitivity analysis | **Appropriate if labelled correctly.** `_SD` fields describe pixel dispersion within polygons, not sampling uncertainty. |
| Input to a separately specified model-based uncertainty analysis | **Potentially useful**, but requires independent residual, bias and spatial-correlation evidence; the archive does not supply the NFI design variance. |
| Substitute for `var_biom` or `sep_biom` | **No.** Different fields, estimands, statistical design and temporal scope. |
| Reconcile static Tables 17C.0 or 18C.0 | **No.** SBFI is a 2020 spatially exhaustive stock/component product, not the NFI baseline-to-first-remeasurement static run. |
| Recover successive-period design covariance | **No.** No such covariance is exposed in the inspected schema. |
| Aggregate to a formal national confidence interval | **Not from aggregation alone.** The data note explicitly warns against formal inference in this use. |

The **NFI Data Request Form** therefore remains the appropriate route for the genuinely missing provider evidence: Version 3.1 static-run `var_biom` or equivalent components, fixed-panel implementation, successive-period covariance and release reconciliation. It is not needed merely to access the already-public current-generator fields.

## Search limits

Zenodo and Figshare searches index record metadata, not every file’s internal schema. GitHub code search indexes code/content and may tokenize underscores. Zero hits are therefore recorded as **“not located in this bounded search,”** never as proof that no file exists anywhere. Direct archive/schema inspection was used for the specific SBFI deposit rather than relying on its metadata title.

## Evidence map

- `evidence/depository_search_assessment.json` — query results, positive counterexamples and indexing limits.
- `evidence/published_current_generator_snapshots.json` — three public snapshot URLs, hashes, row counts and field checks.
- `evidence/github_repository_audit.json` — pinned repository tree, code/data classification, term counts and requested input CSVs.
- `evidence/sbfi_zenodo_assessment.json` — archive, schema and documented-estimand assessment.
- `evidence/sbfi_zip_inventory.json` — all 2,378 remote ZIP entries and range-retrieval accounting.
- `evidence/sbfi_schema.json` and `evidence/sbfi_schema_tile705.json` — both complete 209-field schemas, preserving the observed storage-type differences.
- `evidence/source_files.csv` — 27 registered source responses/artifacts with integrity metadata.
- `scripts/reproduce_depository_checks.py` — bounded repository/search checks and range-based SBFI inspection.
- `scripts/validate_package.py` and `evidence/package_qa.json` — offline consistency checks.
- `evidence/package_manifest.csv` and `publication_receipt.json` — additive-publication integrity record.

## Reproduction order

```bash
# 1. Audit the named GitHub repository and run metadata searches.
python scripts/reproduce_depository_checks.py github --output ./recheck/github
python scripts/reproduce_depository_checks.py search --output ./recheck/search

# GitHub code search is optional and requires GITHUB_PAT in the environment.
python scripts/reproduce_depository_checks.py search --output ./recheck/search --include-github-code

# 2. List the remote SBFI ZIP without downloading 11.8 GB.
python scripts/reproduce_depository_checks.py inventory --output ./recheck/sbfi

# 3. Selectively retrieve geodatabase metadata and the smallest tile table.
# This schema step additionally requires pyogrio/GDAL.
python scripts/reproduce_depository_checks.py schema --output ./recheck/sbfi
```

Always write new rechecks to a new directory; do not overwrite the frozen evidence.

## Related additive correction

During this follow-up, live testing exposed a reproduction-only defect in the earlier Canada route package’s generator command. A corrected, fully live-tested [v1.1 package](https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/canada_reporting_routes_2026-10-30_v1_1) was published separately. Its route findings and numerical evidence are unchanged; the original v1.0 package remains preserved.

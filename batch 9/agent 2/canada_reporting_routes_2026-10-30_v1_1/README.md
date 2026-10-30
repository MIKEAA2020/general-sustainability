# Canada NFI reporting routes: static HTML/CSV and anonymous generator verification — v1.1

**Verification date:** 30 October 2026  
**Status:** Additive reproduction correction; all route findings and numerical results are unchanged. The original v1.0 package remains published and immutable.

## v1.1 correction

The v1.0 `generator` reproduction command did not correctly reconstruct the audited request: it used a direct WRT parameter set and assumed GeoJSON `features`. The actual service response uses the GDAS→WRT request chain and `title`/`name`/`data` arrays. This was a reproduction-code defect, not a defect in the previously recorded evidence, which had been obtained with the correct original-audit script.

Version 1.1 restores the exact GDAS URL, template, explicit attribute list and `filterClause`; parses the observed NFI array structure (with a GeoJSON fallback); and rejects empty or unrecognized responses. A fresh live test returned **58, 58 and 550 rows**, exposed both fields in every row, and produced responses byte-identical to the frozen public snapshots. Use this v1.1 script for reproduction.

## Bottom line

The useful correction is **link rotation plus separate reporting routes**, not disappearance of the data and not a blanket login restriction on variance fields.

1. The legacy `/en/reportgenerator` route returns 404, while the current interactive **[Customized report generator](https://nfi.nfis.org/en/customized_report)** returns HTTP 200.
2. The supplied **[Table 17C.0 HTML](https://nfi.nfis.org/resources/general/summaries/t1/en/CA/html/ca_t17_forage20_biom_change_en.html)** and **[direct CSV](https://nfi.nfis.org/resources/general/summaries/t1/en/CA/csv/ca_t17_forage20_biom_change_en.csv)** both return HTTP 200. The reported CSV misconfiguration was **not reproducible** during this verification.
3. Across the complete biomass scope—Canada and ecozones, Tables 17 and 18, stock and change, and point/RSE/interval—**24/24 CSVs and 24/24 HTML tables returned HTTP 200**. All 24 CSVs were byte-identical to the frozen audit inputs.
4. Change tables are labelled **Version 3.1, November 2025**; stock tables are labelled **Version 3.1, October 2025**. The HTML total of **17.64 Mt** is the two-decimal presentation of the CSV’s **17.639 Mt**, not a different estimate.
5. A cell-level comparison found **18,330/18,330 numeric cells consistent within HTML rounding and zero mismatches**. The HTML therefore adds release/source labels and presentation, not new numerical estimates. Static tables expose point estimates, RSE and interval half-widths—not raw `var_biom`.
6. Three fresh **anonymous** customized-generator queries returned HTTP 200 and exposed both `sep_biom` and `var_biom`: 58 national point rows, 58 national change rows and 550 ecozone change rows. Their data and schemas were identical to the frozen generator snapshots. No collaborator credential is needed for these tested Canada/ecozone scopes.
7. The current measurement list offers only `changes` (baseline to first remeasurement) and `point` (first remeasurement, 2007–2017); no static-release selector was found. The **[NFI Data Request Form](https://nfi.nfis.org/en/datarequest)** and **nfisupport@nfis.org** remain appropriate for version-matched static-run `var_biom` or other unreleased variance components, fixed-panel implementation details and release reconciliation—not for fields already public through the generator.

## What changes—and what does not

| Question | Verified answer |
|---|---|
| Is the old generator URL still the right route? | No. Treat its 404 as link rotation; use `/en/customized_report`. |
| Are the standard-report CSV links currently broken? | No HTTP failure was reproduced: 24/24 biomass CSVs and their HTML counterparts returned 200. |
| Does the new HTML change the audited static numbers? | No. All 18,330 comparable cells agree within HTML display rounding; CSV bytes are unchanged. |
| Do anonymous generator users receive `sep_biom` and `var_biom`? | Yes, in all three tested public queries. |
| Can the public generator be assumed to reproduce the static release? | No. Its measurement list has no static-release selector, and its numerical product remains distinct. |
| Is a provider request still justified? | Yes, narrowly: for static-run variance components or implementation/release evidence not exposed by the public routes. |

The static Version 3.1 national change total remains **17.639 Mt** at full CSV precision. The separately queried current generator forest-change sum remains **19.066 Mt**. These are not interchangeable. This supplement does not select between their uncertainties, combine their fields, infer an export defect, or claim that a displayed RSE establishes a 95% interval.

The generator page separately describes NFI-unit and jurisdiction reports as collaborator-only. That scope restriction must not be generalized to the successfully tested anonymous Canada and ecozone queries.

## Evidence map

- `evidence/route_assessment.json` — concise route-by-route conclusions and the version boundary.
- `evidence/static_biomass_retrieval.json` — all 24 asset pairs, HTTP statuses, byte counts, hashes, versions and frozen-byte comparisons.
- `evidence/html_csv_rounding_comparison.json` — per-table cell counts and mismatch results, including rules for dashes, `<0.01`, thousands separators and the RSE-cap asterisk.
- `evidence/anonymous_generator_recheck.json` — three query datasets, row counts, field exposure, frozen equality and response hashes from the initial route verification.
- `evidence/reproduction_v1_1_generator_test.json` — independent live regression test of the corrected GDAS→WRT request builder and array parser, including frozen data/schema equality.
- `evidence/source_files.csv` — 61 retrieved responses registered by URL, status, size and SHA-256, including the legacy 404 and three v1.1 regression responses.
- `scripts/reproduce_route_checks.py` — static retrieval, HTML/CSV comparison, anonymous generator queries and measurement-list retrieval.
- `scripts/validate_package.py` and `evidence/package_qa.json` — offline consistency and completeness checks.
- `evidence/package_manifest.csv` and `publication_receipt.json` — additive-publication integrity record after the commit is created.

## Reproduction order

Run from a directory with the supplement, with `requests` and `beautifulsoup4` installed:

```bash
# 1. Retrieve the 24 static CSV/HTML pairs.
python scripts/reproduce_route_checks.py static --output ./recheck/static

# 2. Compare their numeric cells without altering the source snapshots.
python scripts/reproduce_route_checks.py compare --input ./recheck/static

# 3. Re-run the three public generator queries without credentials.
python scripts/reproduce_route_checks.py generator --output ./recheck/generator

# 4. Retrieve the generator's current measurement list.
python scripts/reproduce_route_checks.py measurements --output ./recheck/generator
```

Optional `--frozen-static` and `--frozen-generator` arguments compare newly retrieved files with local frozen copies; they never write to those copies. Later source updates must be saved as new snapshots rather than overwriting this verification.

## Relationship to the published audits

This is a small independent supplement to the original deeper-source audit and its five-route follow-up. Their package and receipt identifiers remain unchanged. No national hold is released, no provider PDF is redistributed, and no static/current-generator values are pooled.

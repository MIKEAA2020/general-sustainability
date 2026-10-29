# F06 — corrected Figure 1 and actual reference-artifact audit

## Figure 1 correction

The regional labels in F05 Figure 1 overlap; that defect is acknowledged, not treated as a successful earlier legibility check. F06 regenerates the figure as horizontal stacked bars, with the long Latin America and the Caribbean label wrapped onto two lines. Europe and North America occupy separate rows. All six regional counts and the totals **183 available / 53 unavailable** are unchanged. Bounding-box checks reject intersecting region labels, and the corrected figure is visually checked inside the rebuilt manuscript, not only as a standalone image.

The article uses `results/account_coverage_F06.pdf`; PNG and count/layout checks are also supplied. `src/data_suitability.py` now calls the same plotting function as the standalone plot script, so reproducing the account audit does not restore the old layout. The original published F05 package remains unchanged.

## Actual input artifacts, not page descriptions alone

The official MapBiomas reference page labels both examined downloads Collection 9 and describes interpretation through 2024. F06 downloads and hashes the linked CSV ZIP (3,283,559 bytes) and vector ZIP (6,695,150 bytes), under the 25 MB/file cap. Uncompressed CSV and DBF are about 98 MB and 209 MB and are processed within predeclared decompression limits. Raw archives/point records remain external; no provider raster/PDF/archive is redistributed.

| Property | CSV archive | Vector archive |
|---|---:|---:|
| Records / unique TARGETID | 85,152 / 85,152 | 85,152 / 85,152 |
| Annual CLASS fields | 1985–2023 | 1985–2022 |
| 2015 nonblank entries | 85,152 | 85,152 |
| 2023 nonblank entries | 4,053 | No field |
| Reference locations inside fixed Brazil window | 7 | 7 |
| Local recorded paired 2015/2023 entries | **0** | **0** |

The CSV has **81,099 blank 2023 entries**. The 4,053 nonblank entries include 11 explicitly labelled `NÃO OBSERVADO`, so nonblank is not equivalent to usable reference truth. Annual CSV labels are Portuguese text, contrary to a literal numeric-code reading of the webpage's column description. The vector uses numeric representations. No unverified class-name/code/Collection 11 crosswalk, class confusion matrix or transition accuracy is calculated.

The seven local CSV 2023 entries are all blank. The vector lacks that year. This rules out these artifacts as a local paired-endpoint validation sample; it does **not** rule out all possible reference sources or invalidate Collection 11's documented internal assessment. The XLSX alternative has not been decoded or certified equivalent.

## Coordinate inconsistency verified across every row

All 85,152 point identifiers are shared across the two artifacts. CSV LON/LAT coordinates agree with the vector's WGS84 POINT geometries, with maximum difference about 1.78e-15 degrees. In the vector DBF, however, the attribute named `LON` equals geometry latitude and the attribute named `LAT` equals geometry longitude at **all 85,152 records** (within 1e-8 degrees). F06 uses the declared WGS84 point geometry, not those reversed attributes. The maximum reversed-attribute-to-geometry discrepancy is about 1.78e-15 degrees; the direct erroneous interpretation can differ by more than 71 degrees.

This establishes an internal attribute/geometry inconsistency, not independent positional accuracy. The source bytes are preserved externally, not edited. Counting local points from the misleading attribute names would be wrong.

## Roles, weights and provenance still require reconciliation

- CSV `AMOSTRAS=Treinamento` and `AMOSTRA_AM=1` each mark **9,999** records. The other **75,153** have blank training text and indicator zero—not a positive certification of independent validation.
- The general Collection 11 ATBD describes excluding approximately 10,000 Amazon training points. Its relationship to these exact 9,999 flags and the applicable assessment universe is not certified by this download.
- The vector lacks these training-role fields.
- Both archives contain numeric probability/weight fields after explicitly parsing CSV decimal commas. The vector has **19 zero-probability and zero-weight records**; CSV values are positive throughout. Field presence and positivity alone do not establish correct inclusion probabilities, frame matching or valid design weights.
- Common 2015 interpreter-count and border fields differ at **2,161** and **1,011** identifiers, respectively. These are differences between reference representations, not map-accuracy estimates or independent validation replications.

No source is selected for favourable agreement, no points are pooled into an assumed independent reference population, and no unsupported weight repairs or class crosswalks are imposed.

## Reproduction and scope

`protocol/REFERENCE_AUDIT_F06.md` and its hash were frozen before either reference archive download/decoding. HEAD metadata and previous local outcomes were already known. This is a local specification, not an externally registered/untouched held-out design. The initial numeric-only parser was corrected before finalization to distinguish textual labels from missing fields; this operational correction is documented here, not narrated in the article. No class-versus-map comparisons were computed.

```sh
python src/plot_account_coverage.py
python src/reference_audit.py --cache /your/external/reference-cache
# Once archives are cached, a fully offline reproduction:
python src/reference_audit.py --cache /your/external/reference-cache --offline
python -m unittest discover -s tests -v
bash src/build.sh
```

Archive/member hashes, full schemas and aggregate label/role/completeness profiles are in `metadata/reference/` and `data/reference/reference_audit_F06.json`. Cross-artifact comparisons concern coordinates and selected metadata payload fields only. No weighted national area, reference-versus-map accuracy, transition uncertainty, biomass stock/change, account–asset divergence or performance estimate is supplied. All eight national physical admissions remain on hold with no permanent exclusions.

Source: MapBiomas Project, Collection 9-labelled public reference downloads, accessed 29 October 2026, https://brasil.mapbiomas.org/downloads/pontos-de-validacao/. Public/free use with source attribution follows https://brasil.mapbiomas.org/faq/?tema=dados; no specific upstream Creative Commons version is asserted.

## Next scientific requirements

Obtain verified compatible paired endpoint reference labels and their interpretation/training provenance; reconcile the class crosswalk and probability frame; resolve the forest-only biomass observation/allocation target; complete national territory/support and valid/missing/converted coverage; establish covariance-aware change uncertainty. Do not extrapolate the fixed local window or equate a reference gap with ecological loss. The current findings advance the input-compatibility assessment within the intended empirical study; they do not complete its national physical sample.

# Follow-up F08 — Ecological assets behind improving accounts

**A boundary-matched test of composition masking — developing empirical study**

- [Main manuscript — F08](followup_F08_main.pdf), [LaTeX](followup_F08_main.tex)
- [Supplementary Information — F08](followup_F08_SI.pdf), [LaTeX](followup_F08_SI.tex)
- [Brazil support results and limits](BRAZIL_SUPPORT_RESULTS_F05.md)
- [Current admission/hold table](data/support/physical_admission_F08.csv)
- [Inherited F04 territorial/native-support report](PHYSICAL_SAMPLE_F04.md)

F08 implements the author-requested linked ORCID, seven discoverability/novelty keywords and exact AI declaration, and completes the Excel retry. See [full Excel audit and direct input links](INPUT_LINKS_F08.md) and [the explicit revision record](metadata/revision_record_F08.md). It retains the F07 [conditional local allocation results](ALLOCATION_RESULTS_F07.md). It computes auxiliary full-cell masses and minimal-model allocation/difference sets, not validated or national forest stocks.

Retained F06 work corrects the overlapping region labels in Figure 1 and adds an actual two-artifact MapBiomas reference audit. [Reference results](REFERENCE_AUDIT_RESULTS_F06.md) and [corrected figure](results/account_coverage_F06.png) document the findings.

Retained F05 evidence adds a computed 2015/2023 MapBiomas Collection 11 land-cover comparison on the **unchanged F04 Brazil 256² native biomass window**. Every fine pixel intersecting the rectangle is included using WGS84 area-overlap weights. The footprint is 61,830.3436 ha and is a deterministic local example, not a national probability sample. No global native raster or full country cover image was downloaded.

## Observed local endpoints, not national change

| Mapped quantity | 2015 (ha) | 2023 (ha) |
|---|---:|---:|
| Formations: codes 3, 5, 6, 49 | 4,319.2517 | 4,510.4277 |
| Savannas: codes 4, 7 | 7,850.4615 | 6,924.8985 |
| Formations plus savannas | 12,169.7132 | 11,435.3262 |
| Plantation: code 9, separate | 10.6634 | 16.9053 |

These groupings identify different mapped-cover targets, not confidence intervals or alternatives from which to select a preferred sign. They are not validated forest-land-use change. Complete published-label coverage is not complete direct annual observation: temporal filtering and adjacent-year gap filling affect interpretation. The complement of mapped formations includes other ecological assets.

**Important observation-operator limit:** native CCI AGB is a full-pixel density, not a forest-only density. Even an exact finer forest fraction does not locate the pixel's biomass within forest versus other land. Multiplying the two imposes an allocation model; F05 does not do so. Forest-only stock and whole-territory woody-biomass stock must remain distinct estimands with compatible area denominators.

All eight national physical admissions remain **on hold**, with no permanent exclusions. National forest/biomass change, independent conversion associations, divergence prevalence, uncertainty calibration and reporting-rule performance remain unestimated. The intended empirical study is not complete or ready for submission; it has not been replaced with a different design-only publication.

## Conditional F07 mass-allocation results

Condition on published point maps, grids and epochs being exact, nonnegative within-cell biomass, and no finite component-density or temporal allocation constraint. Formations-only endpoint sets are [44,230.33, 279,193.20] Mg and [55,221.55, 326,232.34] Mg; the difference set is **[−223,971.65, +282,002.02] Mg**. Formations-plus-savanna gives **[−178,109.80, +259,533.76] Mg** for the difference. Both contain zero. They describe different mapped domains, not competing confidence intervals.

Integer positive-overlap counts—not near-purity thresholds—anchor pure/absent/mixed cases. All 65,536 cells remain included. Auxiliary full-cell sums (463,922.53 / 529,164.89 Mg) are not forest-only estimates or substitute primary targets. The model may admit ecologically implausible extremes; measurement/classification error and temporal mismatch are not calibrated by these allocation sets.

The 33,714,740-byte XLSX was successfully downloaded and all 85,152 records/135 fields were streamed under the pre-decoding workbook-only 40MB/400MB exception. At every shared ID, all 117 common annual payloads match the CSV after documented serialization normalization. Endpoint tokens, training-role tokens and coordinates also agree. It repeats the 4,053 nonblank 2023 entries and zero local 2023 labels: no new independent or paired local validation. Earlier F07 metadata-only records retain their historical scope.

## Retained F06 findings

Both public archives contain 85,152 records and seven locations inside the fixed footprint. The CSV has 4,053 nonblank 2023 labels, but none at these seven locations; the vector stops at 2022. Vector LON/LAT attributes are reversed relative to its WGS84 point geometry at every record. CSV class names are textual, and source role/weight fields differ. These two artifacts cannot supply local paired 2015/2023 validation; this does not exclude all possible reference information. No class confusion, transition accuracy or weighted national area is estimated.

Figure 1 now uses horizontal bars, a wrapped long region label and disjoint label boxes, preserving all regional counts and 183/53 totals. Both the standalone plot script and the account-audit pipeline use the corrected layout. The figure is inspected at manuscript size. F05 remains immutable, including its acknowledged figure defect.

## Reproduce the bounded computations

```sh
python -m pip install -r requirements.txt
# External raw-byte cache, outside the distributed package:
python src/brazil_support.py --cache /your/external/mapbiomas-range-cache
python src/plot_brazil_support.py
python src/plot_account_coverage.py
python src/allocation_envelopes.py --cache /your/external/F07-source-cache
python src/xlsx_reference_audit.py --cache /your/external/F08-reference-cache
# Complete source reparse with no downloads after XLSX and CSV ZIP are cached:
python src/xlsx_reference_audit.py --cache /your/external/F08-reference-cache --offline
# Historical metadata-only F07 inspection remains available:
python src/xlsx_reference_metadata.py --cache /your/external/XLSX-range-cache
python src/reference_audit.py --cache /your/external/reference-cache
# To forbid downloads once the two archives are cached:
python src/reference_audit.py --cache /your/external/reference-cache --offline
python -m unittest discover -s tests -v
bash src/build.sh
```

The pinned country images are accessed only through bounded HTTP 206 ranges. Wrong status, Content-Range, ETag, unexpected cover codes, altered frozen rules, cache corruption/missing hash and the 25,000,000 distinct-byte cap fail closed. The cap includes cached blocks accessed, not just newly transferred bytes. Each reproduction uses approximately 4.52/4.59 MB of source blocks, including TIFF metadata. A source provider change requires a separate documented source update; do not silently unpin it.

`metadata/brazil/support_freeze_F05.json` verifies the exact class configuration, official legend and bounded protocol fixed **before decoding the cover pixels**. Headers, native valid/zero counts and third-party published trends had already been inspected. Local cover arrays, areas and endpoint patterns have now also been inspected. No external registration, pristine outcome-naive study or untouched held-out evaluation is claimed. The frozen files must not be silently edited.

In F05 the twenty saved arrays, area/class CSVs and scientific provenance were reproduced from cache with all HTTP requests disabled: decoded arrays were exactly equal and CSV/JSON/provenance byte-identical. Unit tests are computational checks, not scientific validation. The current F08 verification and document review are recorded in `metadata/computational_verification.json` and `metadata/document_qa.json`; archived F05–F07 records describe their original checks, not new F08 test runs.

## Inherited computations

The inherited account audit, country geometry and native-access scripts remain available:

```sh
python src/data_suitability.py --cache /your/external/original-input-cache --download
python src/physical_support.py
python src/territorial_crosswalk.py --workbook /your/external/original-input-cache/NEFBA_2026.xlsx
python src/native_coverage_probes.py --cache /your/external/native-probe-cache
```

The account tables/counts, substantive estimand kernel, country/window choices, research questions, allocation outputs and corrected F06 Figure 1 remain unchanged. The AI declaration is explicitly replaced at the author’s request with “Arena.ai Agent Mode was used to assist with computational methods and literature review.”, linking Arena.ai to the supplied http://Arena.ai URL. This authorized change is not represented as unchanged historical wording. The ECOMOD C17 declaration is not modified. The F04, F05 and F06 protocols are archived verbatim. Historical F04-named reports and source records retained here describe their original scope, not the current F07 outcome status. Inherited F05 support/provenance statements saying no biomass mass analysis was done describe that historical pass, not the new F07 conditional mass summaries. F07, F06, F05, F04, F03, C17 and all earlier published directories remain immutable.

## Source scope and licences

MapBiomas attribution: **Projeto MapBiomas – Coleção 11 da Série Anual de Mapas de Cobertura e Uso da Terra do Brasil**, accessed 29 October 2026, https://brasil.mapbiomas.org/downloads/. Processing: declared class grouping and WGS84 area intersection. The official FAQ permits public/free data use with source attribution; no particular upstream Creative Commons licence version was verified or invented. Raw raster blocks and source PDFs are not redistributed. The official code CSV, factual source identities, own summaries and processing are supplied.

`metadata/brazil/document_registry.json` and `metadata/brazil/source_review_F05.json` distinguish documents downloaded, targeted passages reviewed and an aborted/unread CCI ATBD request. The public reference download inspected is labelled Collection 9, not independently verified Collection 11 validation. Cerrado's GEDI-derived training information and CCI's LiDAR/allometry lineage preclude an unsupported publisher-based error-independence assumption; actual joint error covariance has not been quantified.

Account adaptations retain CC BY-SA 4.0; OSM-derived boundary support databases retain ODbL 1.0. Boundary objects and other upstream inputs retain their source-specific terms. See `metadata/SOURCE_USE.md` and `metadata/BOUNDARY_LICENCES.md`. No blanket licence replaces those terms.

The F06 archive/member registry, schema/coverage profiles and frozen pre-download specification are in `metadata/reference/`, `data/reference/` and `protocol/REFERENCE_AUDIT_F06.md`. Raw reference archives remain external; exact hashes and ETags reject source drift. F08 adds the complete XLSX worksheet audit and exact source/member hashes, superseding the current undecoded status without revising the historical F07 record. Reference-role labels and numeric fields do not certify independence or valid design weights.

The new frozen F07 specification, source input identities, conditional computations and reproduction records are in `protocol/ALLOCATION_ENVELOPE_F07.md` and `metadata/allocation/`; generated mass sets and six integer topology arrays are in `data/allocation/`. No source biomass arrays are redistributed. Reproduction uses exact cached hashes or bounded downloads; provider drift fails closed rather than silently substituting versions.

`REMAINING_EMPIRICAL_WORK.md` sets out unresolved analytical work. Revision histories and implementation records remain outside the articles. Compilation requires latexmk, xurl, recommended fonts, CM-Super and the declared LaTeX packages. `artifact_manifest.json` lists every distributed file other than itself; generated caches are excluded. PDF byte hashes may differ after recompilation.

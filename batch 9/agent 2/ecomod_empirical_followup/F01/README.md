# Empirical follow-up — F01, Stage 1 implementation

**29 October 2026. This is the first implemented stage, not a completed empirical paper.**

Start with the [six-page working manuscript](manuscript/followup_F01_stage1.pdf) and [progress report](results/STAGE1_REPORT.md). The [working protocol](protocol/PROTOCOL_F01.md) and [configuration](configs/stage1_design.json) state the design, gates and prior-information disclosure.

## Five-stage execution

1. **Specification and preflight — implemented in F01.** Consolidated the prior reviews; retrieved and hash-froze actual inputs; audited all national account identifiers; inspected small biomass files and provider methods; wrote and tested computational kernels; produced the initial manuscript.
2. **Boundary-matched physical pilot — next.** Reconcile country/territory and independent forest masks; retrieve bounded native/coarser data under a justified area denominator; validate change, source lineage, missingness and transition support. Eight candidates are not eight completed physical analyses.
3. **Calibration and extraction — pending.** Whole-pipeline noisy-null/misspecification calibration with tuning/evaluation separation; matched-support comparisons and coverage; independently justified validation rather than target-derived quality flags.
4. **Empirical estimates — pending.** Stock/extent/density and spatially offsetting local net changes, all outcome directions and abstentions; conversion associations only with independent transition validation.
5. **Completed main/SI and reproducibility release — pending.** Write from the actual estimates, validate and archive a new revision without overwriting F01.

## What was actually run

- Downloaded the current public NEFBA 2026 workbook: 4,403,325 bytes, SHA-256 in the source registry.
- Parsed **13,652 national records, 51 columns and 236 country/territory identifiers**. An account-only 2015–2023 screen passes **183** identifiers and fails **53**. All eight predeclared candidate countries pass that limited screen. No physical eligibility or trend prevalence follows from this count.
- Downloaded and opened two small CCI Biomass v7 NetCDF files, approximately 1.45 MB and 0.17 MB. Read only metadata/coordinates/time, not biomass/change values or signs. No global native-resolution download.
- Inspected selected v7 Product User Guide passages, data-use terms and the provider change-generation script. The provider script was **not executed**.
- Implemented and passed **13 unit tests**, including 500 random exact mixed extent/density decompositions, WGS84 area/partition checks and cancellation edge cases.
- Compiled a **six-page Stage 1 manuscript** with zero unresolved references/citations and zero overfull boxes. Results are preflight results, not ecological trends.

## Important actual findings

The nominal 50 km aggregate uses a 0.5° coordinate grid, not equal-area cells. Its density denominator is total grid-cell area, not forest area. The v7 guide documents spatial covariance in aggregate uncertainty and cautions about map-difference biases. The downloaded change example has a dangling time-bounds reference and lacks in-file flag meanings; external source documentation is required. Provider change flags are derived from the same endpoint maps and rule/filter operations and cannot be treated as independent validation truth or a calibrated 95% test. The public change example does not establish change quality for the primary 2015–2023 study interval.

These findings change the implementation; they are not generic checklist entries. See the method audit and source-use notes in `metadata/`.

## Reproduce

```sh
python -m pip install -r requirements.txt
python src/preflight.py --cache /your/external/raw-cache --download
python -m unittest discover -s tests -v
bash src/build.sh
```

Without `--download`, the preflight uses the three previously downloaded raw files in the specified cache. It checks their hashes against the frozen `metadata/source_registry.json` and fails if inputs change; do not silently update the registry to bypass this check. A changed source requires an amendment/new revision. The first run used `/home/user/.cache/followup_stage1`; that machine-local cache is not needed if you retrieve the registered inputs yourself.

The configuration predates these new country-pair outcome calculations, which have not been performed. Existing world-level analyses and source discovery are disclosed. **No claim of external preregistration or pristine prospective design is made.**

## Files and source terms

- `data/derived/account_eligibility.csv`: one row per national identifier; reasons for account-screen failure and explicit pending physical-alignment status.
- `data/derived/pilot_candidate_audit.csv`: the eight logistical candidates, not an eligible physical sample.
- `metadata/source_registry.json`: exact hashes, sizes and download URLs for the three empirical input files.
- `metadata/cci_schema_audit.json`: actual headers, shapes, coordinates and missing metadata references; no biomass values.
- `metadata/source_method_audit.json`: targeted document/script inspection, hashes and consequences for the analysis.
- `metadata/SOURCE_USE.md`: attribution, source-use requirements and independent-validation restrictions.
- `results/preflight_summary.json`, `results/test_and_build_checks.json`: machine-readable completed checks and scope.
- `src/estimands.py`, `src/preflight.py`, `tests/`: executable implementation, not only prose.
- `manuscript/`: working TeX/PDF; `results/account_coverage.pdf` and the numerical macro file are generated inputs.

The workbook's NEFBA-derived metadata and availability tables are shared under **CC BY-SA 4.0**, with source attribution and changes described in `metadata/SOURCE_USE.md`. CCI originators and the ESA CCI/Biomass CCI programme must be acknowledged under the source terms. Raw inputs, restricted guide text, provider code, credentials and private caches are not redistributed. Source headers and original provider metadata descriptions are retained for scientific provenance, not represented as this project's authored findings.

All earlier planning/review packages and C13 remain unchanged. This is published as a separate immutable F01 directory under `batch 9/agent 2/ecomod_empirical_followup/F01`; later work should use new revision directories.

# Bounded implementation, reference and native-SD feasibility evidence — R03

**29 October 2026.** Companion evidence package for the additive **F10** empirical follow-up. F08/F09 and all earlier repository content are protected. Start with `RESEARCH_RESULTS_R03.md`; `PROVIDER_QUESTIONS_R03.md` contains questions prepared for author review, **not sent**.

## Outcomes

- **Implementation:** 21 pinned source files reverified without executing third-party code. The distributed change script's RSS and zero/NoData conventions are identified. Plot2Map has N⁻² term averaging in its validation tool; this does not establish v7 production aggregation lineage or resolve the printed production-equation discrepancies.
- **Reference:** current open AGBref release found by following its actual version chain. Complete CRC-checked decoding of four selected CSV members used **22,551,986 distinct archive bytes** under a **25,000,000-byte** source guard. A local aggregate centroid exists, but N=1, support-quality flags, absent original census dates/source identity and lack of a 2023-labelled product prevent a paired primary comparison. No whole-ZIP MD5 verification is claimed.
- **Native SD:** original SHA-matched payloads on the unchanged 256×256 Brazilian window identify **1,032/946** positive-AGB cells with stored SD zero in 2015/2023. This is not zero true error, ecological absence or calibrated change uncertainty.
- **Inference:** no uncertainty floor, error correlation, bias correction, reference-performance estimate, forest stock change or national estimate is invented. All eight admission holds remain.

## Contents and attribution

`data/`: own SD summaries and a four-row derived aggregate-reference subset. The latter is attributed to **Araza, A., Bielig, C., and Flores, R. A. A. (2026), AGBref – Global Reference Dataset for Above-Ground Biomass (AGB), Zenodo record 20793072**, DOI [10.5281/zenodo.20793072](https://doi.org/10.5281/zenodo.20793072), CC BY 4.0. Source record/member fields are retained. It is not a newly observed field sample.

`metadata/`: public source identities/catalogues, limited factual records, code/source checks, original and reproduced archive inspection, native diagnostics and technical verification. Source identities distinguish complete small-file hashes from partial ZIP/member consistency. Source PDFs, full reference CSVs, native arrays and third-party code are **not redistributed**.

`protocol/`: archive guards/selection and explicit partial-identity policy; descriptive SD scope. The initial exploratory SD inspection preceded its scope record; **no prospective preregistration claim** is made.

`src/`: reusable bounded readers/analysis/checking code plus explicitly named one-time preparation and historical assembly/initial-inspection records. The latter retain working-cache assumptions and are **not** the reproduction entry points. `prepare_F10_R03.py` refuses an existing F10 and must not be rerun to recreate a published version.

## Reproduce

Python 3.11+; `python -m pip install -r requirements_R03.txt`.

Offline tests (no source-body acquisition):

```sh
python -m unittest discover -s tests -v
python -O -m unittest discover -s tests -v
```

From the R03 directory, using an excluded cache path:

```sh
python src/verify_code_sources_R03.py --cache .cache/reproduction --output .cache/code_check_R03.json
python src/native_uncertainty_R03.py --cache .cache/reproduction
python src/inspect_reference_archive_R03.py .cache/reproduction --output .cache/reference_check_R03.json
```

The native command rewrites derived SD outputs from the frozen original payload identities; no new geometry is selected. The archive reader uses the persistent pinned catalogue/HEAD records and rechecks them before/after; it stops if the source changes. It does not use full-archive downloads as fallback. A different hosting convention may therefore stop reproduction rather than silently weakening identity checks. The original archive audit remains unchanged when `--output` is used.

Archive reproduction was executed against the existing verified block cache: all four member summaries match exactly and **zero additional archive body bytes** were acquired; live catalogue/HEAD checks were repeated. This is not an independent second download. Metadata/HTML requests are outside the archive-specific source-byte budget. Native outputs were executed against full hash-matched original payloads. Tests are technical/arithmetic/evidence-gate checks, **not ecological validation**.

## Open dependencies

Provider production normalization/kernel provenance, zero-origin conventions, compatible repeated field observations with original dates/identities/support, joint temporal/spatial error and systematic-bias evidence, and national territorial/forest-support admission are still needed. Prepared questions identify the evidence required. No broad download or unlicensed source redistribution is justified by the current findings.

# Ecological assets behind improving accounts

**A boundary-matched test of composition masking — developing empirical manuscript**

- [Main manuscript](followup_main.pdf), [LaTeX](followup_main.tex)
- [Supplementary Information](followup_supplement.pdf), [LaTeX](followup_supplement.tex)

This remains the intended forest–cropland empirical study. It is not treated as a completed physical test or silently converted to a separate design-only publication. The current manuscript contains account-availability results, product definitions, research questions and estimands; physical matching, calibration, estimation, conversion associations and reporting comparisons remain ahead. No forest-stock trend or account–asset divergence result is supplied.

## Remaining work and protocol

- `REMAINING_EMPIRICAL_WORK.md`: concrete remaining tasks and required outputs.
- `protocol/STUDY_PROTOCOL.md`: retained design, inference requirements, prior-information disclosure and future-deviation handling.
- `protocol/archive/PROTOCOL_F01.md`: exact original protocol snapshot.
- `metadata/F01_design_input_provenance.json`: original input-provenance record.
- `configs/study_design.json`: machine-readable design, including the restored prior-information disclosure.

These operational records are separate from the journal-facing main/SI. The original account windows, source hashes, candidate countries and numerical eligibility rules are retained. Account availability is not physical eligibility; the physical sample is not yet established.

## Reproduce available calculations

```sh
python -m pip install -r requirements.txt
python src/data_suitability.py --cache /your/external/data-cache --download
python -m unittest discover -s tests -v
bash src/build.sh
```

The registry fixes three source files by exact hashes and byte sizes. Changed source bytes fail closed rather than being silently substituted. Raw workbook/biomass files, the Product User Guide and provider code are not redistributed. The processing reads biomass coordinates and metadata, not biomass pixel values.

`src/estimands.py` is unchanged and implements WGS84 rectangle area, symmetric extent–density decomposition and local-net-change cancellation. Source attributions and licence terms are in `metadata/SOURCE_USE.md`; NEFBA-derived tables/figures are distributed under CC BY-SA 4.0. ESA CCI and its data providers are acknowledged.

Compilation requires latexmk, xurl, recommended fonts, CM-Super and the declared LaTeX packages. File hashes appear in `artifact_manifest.json`, excluding the manifest itself. Build/test checks are scoped computational checks, not empirical validation or author approval for journal submission.

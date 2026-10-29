# Ecological assets and biocapacity accounts: study design and data suitability

## Manuscripts

- [Main article](followup_main.pdf) and [LaTeX source](followup_main.tex)
- [Supplementary Information](followup_supplement.pdf) and [LaTeX source](followup_supplement.tex)

The article presents a forest-led empirical design and an assessment of account availability and biomass observation definitions. It does not estimate physical forest-stock trends, account–asset divergence, land-conversion associations or diagnostic classification performance.

## Data and computation

```sh
python -m pip install -r requirements.txt
python src/data_suitability.py --cache /your/external/data-cache --download
python -m unittest discover -s tests -v
bash src/build.sh
```

The source register supplies exact URLs, byte sizes and hashes for three empirical input files. Without `--download`, existing files are read from the designated cache. Source hashes must match the register; a different file version is not an interchangeable input. Raw files are not redistributed.

`data/derived/` contains account availability for all 236 country/territory identifiers and the eight selected countries. `metadata/` contains the source registry, account definitions, biomass metadata, source-method definitions and licence information. `results/` contains generated availability counts, the coverage figure and the numerical macro file used by both manuscripts. `src/estimands.py` implements WGS84 rectangle area, symmetric extent–density decomposition and local-net-change cancellation; `tests/` supplies the verification cases.

NEFBA-derived tables and figures are distributed under CC BY-SA 4.0, with attribution in `metadata/SOURCE_USE.md`. ESA CCI and its data providers are acknowledged under the source terms. The Product User Guide, raw biomass files and provider processing code are not redistributed.

Compilation requires latexmk, recommended LaTeX fonts, CM-Super, xurl and the packages declared in the manuscript sources. `artifact_manifest.json` records the distributed files' SHA-256 hashes and sizes, excluding itself. PDF hashes can change on recompilation because of timestamps and software/font versions.

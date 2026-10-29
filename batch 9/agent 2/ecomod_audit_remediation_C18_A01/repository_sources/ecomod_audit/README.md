# ECOMOD continued 10: independent audit

Start with [the main-paper audit](AUDIT_ECOMOD_C10.md) and [the standalone SI audit](AUDIT_ECOMOD_C10_SI.md). This package reviews the submitted `ecomod_continued_10.txt` and separately uploaded `ecomod_continued_10_SI.txt`. Both uploads are byte-identical to their pinned `.tex` reference copies under `reference/`.

## Main findings

The NFA headline statistics, land-category contributions, and proxy LMDI split reproduce from the public inputs. The main issues concern the quality clamp versus the written DDE, stability analysis, incomplete Jacobian, non-unique switched equilibria, delay-saturation degeneracy, and inconsistent recovery outputs.

The submitted manuscript and figures were not edited. The retrieved source files are reference copies, not audit revisions. No fresh PDF build or execution of the author's own code was performed.

## Reproduce

Tested with Python 3.13 and the versions in `requirements.txt`:

```sh
python -m pip install -r requirements.txt
python verify_ecomod.py
python verify_ecomod_si.py
```

The script uses files relative to its own directory. If the original upload exists in the Arena workspace it also compares that source; otherwise it uses the pinned reference source. It writes `verification_results.json` and `world_data_extracted.csv` and prints the results. To refresh the recorded stdout:

```sh
python verify_ecomod.py > verification_stdout.txt
```

The separate SI checker writes `si_verification_results.json` and prints its results. Refresh its log with `python verify_ecomod_si.py > si_verification_stdout.txt`. It adds reserve/gate counterexamples, debt-bound and boundary-reduction checks, a finite-difference Jacobian check, one-stock characteristic roots, all proxy-anchor rows, and label/citation-key checks. It does not rerun the author's comparator basin experiment or regeneration-data fits.

The numerical integrator is an independent Euler reconstruction of the disclosed clipped model. Sub-percent differences from some author-reported outputs are not represented as exact reproduction. A numerical trajectory is not a continuum stability proof.

## Reference provenance

### Main and SI

Repository: MIKEAA2020/general-sustainability, pinned commit `6f626ee48b2a3a59282b5df5adda76c8d5993fdc`.

Directory:
https://github.com/MIKEAA2020/general-sustainability/tree/6f626ee48b2a3a59282b5df5adda76c8d5993fdc/agent%202%20productivity%20illusion/output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026

The main reference `.tex` is byte-identical to its uploaded `.txt`. The companion SI was retrieved from that same directory and is byte-identical to the later separate SI upload (SHA-256 `7e815ab3c5e384448c871d05cc71a735798c4ac265e66f8a068260cc10fb3aab`).

### NFA workbook

Lo, K., Basnet, N., Miller, E., Srikanthalingam, B., Foley, B., Van Berkum, J. L., Long, A. H., Toneva, P., Ermina, M. and Klinkenberg, C. (2026). *National Ecological Footprint and Biocapacity Accounts, Edition 2026 (1961–2025): Results and metadata, version 1.0.* Produced for Footprint Data Foundation by researchers at York University and the University of Iceland.

Source: https://footprint.info.yorku.ca/files/2026/04/NEFBA_Data_global_national_ecological_footprint_biocapacity.xlsx

The workbook is unchanged. `world_data_extracted.csv` is a CSV-format extraction of its complete world sheet, including the estimated 2024–2025 rows; the report's primary statistics exclude those rows. Workbook and extracted data are CC BY-SA 4.0; see `DATA_LICENSE.md`.

### Auxiliary proxy inputs

Our World in Data, using FAOSTAT data. Downloaded during this audit from:

- https://ourworldindata.org/grapher/cropland-area.csv?tab=table&country=~OWID_WRL
- https://ourworldindata.org/grapher/cereal-yield.csv?tab=table&country=~OWID_WRL

The endpoints returned full multi-country CSVs despite the country query; the audit script explicitly selects `Entity == World`. The downloaded CSVs are unchanged. Their original provider terms and attribution apply; see the OWID grapher pages and source metadata. They are not relabelled as audit-authored data.

## Integrity and limits

`artifact_manifest.json` records SHA-256 hashes of package files (excluding the manifest itself). Authentication credentials are not included. The audit is not evidence of endorsement by the manuscript author, data providers, or cited journal.

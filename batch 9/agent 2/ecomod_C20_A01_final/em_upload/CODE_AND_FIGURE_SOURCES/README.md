# Code and figure sources — ECOMOD C20 A01

**Manuscript:** A rising biocapacity total can mask ecological-capital land drawdown: a two-land model
**Version:** ECOMOD C20 A01, 31 October 2026

These are the executable sources that generate the submitted figures and the numerical results quoted in the manuscript. They replace the superseded `composition_attribution.py` and `real_series_aggregation_face.py` from the earlier submission, which belonged to a previous figure generation and no longer reproduce the current figures.

## Script → output map

| Script | Produces |
|---|---|
| `reproduce_two_land_C18_A01.py` | Figure 1 (`fig1_model_dynamics`), the baseline run, contribution budgets and timestep-refinement tables |
| `reproduce_empirical_C18_A01.py` | Figures 2 (`fig2_nfa_aggregation_face`) and 3 (`fig3_composition_attribution`), the NFA endpoints, components, Divisia sensitivity and cropland proxy |
| `reproduce_comparator_C18_A01.py` | SI Figures S1–S4 (`si_onestock_*`), the one-stock comparator suite |

Figure S5 (`fig_tb_wave_debt`) is produced by the controlled technology-wave experiment, whose scan and time-series outputs are deposited with the reproduction package described in the Data availability statement.

## Environment

```sh
python -m pip install -r requirements.txt
python reproduce_two_land_C18_A01.py
python reproduce_empirical_C18_A01.py
python reproduce_comparator_C18_A01.py
```

Pinned versions: `numpy==2.3.5`, `scipy==1.17.1`, `numba==0.66.0`, `matplotlib==3.10.9`, `openpyxl==3.1.5`, `requests==2.33.0`.

`reproduce_empirical_C18_A01.py` reads the frozen NFA Edition 2026 and OWID snapshots that accompany the reproduction package; it does not fetch live data. The other two scripts are self-contained.

## Reproducibility status

The C19 verification pass reproduced **26/26 numerical data files byte-identically**, **3/3 PNG figures byte-identically**, and **7/7 PDF figures matched in geometry and extracted content**. PDF container hashes can change across builds because embedded timestamps differ; the numerical outputs and figure geometry are the identity criteria.

These scripts are supplied for transparency and review. They are not required to compile the manuscript or the Supplementary Information, whose bibliographies are embedded and whose figures are already supplied as PDFs.

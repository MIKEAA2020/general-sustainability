# Reproduction Guide & Code Map

Companion to the manuscript *Emergent Carrying Capacity and the Composition Illusion: Two-Land Conversion and
the Identifiability of Collapse*. This guide tells a reader how to rebuild every numeric result and figure.

Workflow: **reproduce the two-land model** → **run the equilibrium / spectrum / basin analyses** →
**run the empirical calibrations (SI §S5.3)** → **render the figures** → **verify the claims**.

---

## 1. Environment & dependencies

| Item | Requirement |
|---|---|
| Python | ≥ 3.11 |
| `model_sims/` runtime | `numpy`, `scipy` (integration, spectral roots), `pandas` (empirical data), `matplotlib` (`Agg`) |
| Results serialisation | `json`, `csv` (stdlib) |
| Optional heavy backends | `sentence-transformers`, `transformers`, `hypothesis` (gap-scan tooling only, not the model) |

Install the project (optional, for the audit tooling) with `pip install -e .` (see `pyproject.toml`). The model
itself is plain NumPy/SciPy/pandas and needs no package install.

**No stochastic seed is required** — the model is deterministic and the calibration fits are closed-form
least-squares / `scipy.optimize` fits on fixed inputs.

---

## 2. File / folder structure

```
agent 2 productivity illusion/
├── model_sims/                      # the model and analyses
│   ├── twoland_fixed.py             # two-land model (quality state q; two-book biocapacity)
│   ├── twoland.py, models.py        # model helpers, fixed-point / no-conversion face
│   ├── verify_tab_conv_basin.py     # re-derives Δb_conv / λ_+ and the basin demand thresholds (SI S5.2)
│   ├── char_eq.py                   # linearisation coefficients + characteristic-equation roots
│   ├── numeric_claims.py            # auto verifiers for reported numerical claims
│   ├── r1_basin.py, r1_figure.py, r2_figure.py, r1_r2_sensitivity.py
│   ├── topdown.py, _run_topdown.py  # top-down analysis + runner
│   ├── _run_sensitivity.py          # parameter-sensitivity sweep
│   ├── recovery_metric_and_tau_p_scan.py  # SI S5.4 R_c(T) gate-sign + S5.5 τ_p-extended scan
│   ├── rebuild_S1_feedback_diagram.py     # the S1 feedback diagram (two closed loops)
│   ├── real_series_aggregation_face.py    # Figure 1 / S15 (aggregate NFA, aggregation face)
│   ├── calibrate_tau_g_recovery_curves.py # forest regeneration-timescale fit (SI S5.3a → S1b)
│   ├── calibrate_tau_g_fisheries.py       # fishery regeneration-timescale fit (SI S5.3a → S1c)
│   └── calibrate_bf_af_provisioning_leg.py# provisioning-book b_f/A_f calibration (SI S5.3b → S1d)
├── scans/                           # rendered model figures + calibration series CSV/JSON
├── data/
│   ├── empirical/                   # FAOSTAT/OWID, 2ndFOR, RAM B/BMSY, WDI crop index
│   ├── nfa/                         # NFA aggregate + land-type biocapacity/footprint files
│   ├── topdown_results.json
│   └── r1_r2_sensitivity_results.json
├── graphical_abstract/              # build_graphical_abstract.py -> .pdf/.png/.tiff
└── supplementary/                   # SI, captions, FIGURES, data-availability, abstract
```

---

## 3. Reproduce every numeric result & figure

### (a) Model, equilibrium, spectrum and basin

```bash
# 1) Regenerate the verified top-down record + the top-down figures
python -m model_sims._run_topdown

# 2) Recompute the basin and spectrum, render figures, and verify numeric claims
python -m model_sims.r1_figure
python -m model_sims.r2_figure
python -m model_sims.numeric_claims      # verifies e.g. Δb_conv, λ_+, basin thresholds

# 3) Parameter sensitivity
python -m model_sims._run_sensitivity

# 4) Regenerate the S1 feedback diagram (two closed loops)
python -m model_sims.rebuild_S1_feedback_diagram
```

### (b) Real-series aggregation face (Figure 1 / S15)

```bash
python -m model_sims.real_series_aggregation_face
```

Requires `data/nfa/GFN_world_biocapacity_footprint_population_1961_2022.csv`. Produces
`reports/real_series_aggregation_face.png` and prints the exact `d ln(B/P)`, `d ln P`, `d ln B` split and
`R_B` cross-over year.

### (c) Empirical calibrations (SI §S5.3)

```bash
# Forest regeneration timescale (SI S5.3a) — reads data/empirical/'Aboveground biomass 2ndFOR database.csv'
python -m model_sims.calibrate_tau_g_recovery_curves
#   -> scans/tau_g_calibration_summary.json, tau_g_calibration_all_fits.csv,
#      tau_g_calibration_raw_curves.csv, S1b_tau_g_calibration.png

# Fishery regeneration timescale (SI S5.3a) — reads data/empirical/ram_bmsy.csv
python -m model_sims.calibrate_tau_g_fisheries
#   -> scans/tau_g_calibration_fisheries.csv/.json, S1c_fishery_recovery.png

# Provisioning-book b_f / A_f + aggregate attribution (SI S5.3b) —
#   reads data/empirical/cropland_area_owid.csv, cereal_yield_owid.csv,
#   and data/nfa/NFA_world_landtype_biocapacity_footprint_1961_2023.csv
python -m model_sims.calibrate_bf_af_provisioning_leg
#   -> scans/bf_af_calibration_series.csv, S1d_bf_af_calibration.png
```

### (d) Recovery metric and τ_p scan (SI §S5.4–S5.5), and graphical abstract

```bash
python -m model_sims.recovery_metric_and_tau_p_scan
python graphical_abstract/build_graphical_abstract.py
```

**Current manuscript parameters** are set in the model modules and given in the SI §S4.1 table. The two-land
model uses effective (representative) parameters — see the SI §S4.1 and the manuscript §Model formulation /
§Assumptions; these differ from the earlier single-stock comparator convention and should be read from the SI
table rather than assumed.

---

## 4. Output registry

Which script produces which figure / number. All paths relative to the project root.

| Figure / output | Produced by | Source figure in package |
|---|---|---|
| `scans/feedback_diagram.png` | `rebuild_S1_feedback_diagram.py` (manuscript §7) | `FIGURES/S1_feedback_diagram.png` |
| `scans/S1b_tau_g_calibration.png` | `calibrate_tau_g_recovery_curves.py` | `FIGURES/S1b_tau_g_calibration.png` |
| `scans/S1c_fishery_recovery.png` | `calibrate_tau_g_fisheries.py` | `FIGURES/S1c_fishery_recovery.png` |
| `scans/S1_multi_ecosystem_tau_g.png` | (combined `t50` comparison; see SI §S5.3a) | `FIGURES/S1_multi_ecosystem_tau_g.png` |
| `scans/S1d_bf_af_calibration.png` | `calibrate_bf_af_provisioning_leg.py` | `FIGURES/S1d_bf_af_calibration.png` |
| `scans/topdown_macro_ratios.png` | `_run_topdown.py` | `FIGURES/S2_macro_ratios_RB_vs_RA.png` |
| `scans/topdown_ratio_separation.png` | `_run_topdown.py` | `FIGURES/S3_flow_share_separation.png` |
| `scans/topdown_delay_boundary.png` | `_run_topdown.py` | `FIGURES/S4_delay_boundary_cliff.png` |
| `IMPLEMENTED_demo.png` | (overshoot demo, manuscript §10) | `FIGURES/S5_demo_overshoot_run.png` |
| `IMPLEMENTED_demo_masking.png` | (masking window, manuscript §10) | `FIGURES/S6_masking_window.png` |
| `scans/r1_recovery_vs_collapse.png` | `r1_figure.py` | `FIGURES/S7_recovery_vs_collapse.png` |
| `scans/eco_recovery_insight.png` | `r1_figure.py` | `FIGURES/S8_recovery_insight.png` |
| `scans/r2_char_spectrum.png` | `r2_figure.py` | `FIGURES/S9_char_spectrum.png` |
| `scans/r2_a11_vs_delay.png` | `r2_figure.py` | `FIGURES/S10_a11_vs_delay.png` |
| `scans/sustainable_yield_regimes.png` | (regime-table figure, manuscript §4.1) | `FIGURES/S11_sustainable_yield_regimes.png` |
| `scans/r1_basin_baseline.png` | `r1_figure.py` | `FIGURES/S12_basin_baseline.png` |
| `scans/r1_basin_delay_response.png` | `r1_figure.py` | `FIGURES/S13_basin_delay_response.png` |
| `graphical_abstract/graphical_abstract.pdf/.png/.tiff` | `build_graphical_abstract.py` | `FIGURES/S14_graphical_abstract.png` |
| `reports/real_series_aggregation_face.png` | `real_series_aggregation_face.py` | FIGURE 1 / `FIGURES/S15_aggregation_face.png` |
| `scans/bf_af_calibration_series.csv`, `tau_g_calibration_*.csv/.json` | the calibration scripts | — |
| `data/topdown_results.json` | `_run_topdown.py` | — |
| `data/r1_r2_sensitivity_results.json` | `r1_r2_sensitivity.py` | — |

---

## 5. Verification protocol

Every reported number carries its protocol (see manuscript §Numerics):

- **Solver:** method-of-steps with RK4, the exact `[·]₊` switch (never a smooth ramp, which leaks conversion
  when `E < σ_f b_f A_f + σ_c Υ_c A_c`), clamping `A_c ≥ A_c^min`, `A_f ≥ 0`, `K ≥ K_min`, and explicit event
  detection at land boundaries.
- **Convergence:** state `dt`, history functions, and a `Δt`-convergence table for the reported runs.
- **Termination convention:** the endpoint is reported with its convention (e.g. frozen vs crashed vs
  un-clamped endings where these differ).
- **Calibration fidelity:** for the SI §S5.3 fits, the number of fits retained, the median `R²`, and any fit
  defect (right-censoring, or a parameter pinned at a bound) are disclosed rather than presented as an estimate.

Run the automated numeric verification with `python -m model_sims.numeric_claims` and the calibration scripts
above; the verification tolerances are stated in each module.

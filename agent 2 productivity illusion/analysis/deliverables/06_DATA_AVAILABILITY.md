# Data and Code Availability Statement

**Manuscript:** How Aggregation Can Conceal Composition: Aggregate Biocapacity and the Identifiability of Modelled Ecological-Capital Drawdown

---

## Data

This study combines a deterministic two-land model with an empirical calibration of its key parameters.
The primary empirical inputs are published datasets, each cited and reproduced here for transparency:

- **National Footprint and Biocapacity Accounts (NFA), world, 1961–2022** — aggregate biocapacity,
  footprint and population series (`data/nfa/GFN_world_biocapacity_footprint_population_1961_2022.csv`),
  plus the NFA land-type file (`data/nfa/NFA_world_landtype_biocapacity_footprint_1961_2023.csv`), from which
  the **world cropland biocapacity** (`Record = BiocapTotGHA`, `Cropland` column) is read. This is the
  base-year anchor for the absolute provisioning-book yield `b_f(1961)` and the aggregate-attribution result.
  The paper's headline aggregate figure is computed from the aggregate NFA series; the land-type file is
  the newer vintage and is used for the cropland-book calibration (both are reported; see the SI §S5.3b
  vintage note).
- **FAOSTAT / Our World in Data (world, 1961–2022)** — cropland area (`cropland_area_owid.csv`),
  cereal yield (`cereal_yield_owid.csv`) and cereal production (`cereal_production_owid.csv`); these give the
  provisioning area `A_f` and the physical (cereal-sentinel) yield numerator.
- **FAOSTAT Gross Crop Production Index** (domain `QI`, item `2041`, element `432`), retrieved as the World Bank
  indicator `AG.PRD.CROP.XD` (`data/empirical/faostat_crop_production_index_wdi.csv/.json`) — inspected as the
  preferred aggregate numerator but **not used** as a growth measure because the available series has
  base-period splice discontinuities (see the SI observation-operator note).
- **2ndFOR secondary-forest biomass database** (Poorter et al. 2016; `data/empirical/Aboveground biomass
  2ndFOR database.csv`) — plot-level age–above-ground-biomass pairs, used for the forest regeneration-timescale
  fit (SI §S5.3a).
- **RAM Legacy Stock–Recruitment** B/BMSY series (`data/empirical/ram_bmsy.csv`) — deplete-then-rebuild
  trajectories, used for the fishery regeneration-timescale fit (SI §S5.3a).

The third-party datasets are distributed in this package for reproducibility; the original sources are cited in
the manuscript References. The NFA data are © Global Footprint Network / York University / FoDaFo (2025 Edition),
used here for scholarly analysis.

## Code and reproducibility

The model and all calibration/analysis code is in the `model_sims/` package:

- `twoland_fixed.py`, `twoland.py`, `models.py` — the two-land model, its fixed-point and no-conversion face
- `verify_tab_conv_basin.py` — automated verification of the composition-diagnostic and basin tables
  (SI §S5.2)
- `char_eq.py`, `numeric_claims.py` — linearisation / characteristic roots, and verifiers for the reported
  numerical claims
- `calibrate_tau_g_recovery_curves.py` — forest regeneration-timescale fit from the 2ndFOR raw curves;
  writes `scans/tau_g_calibration_summary.json`, `scans/tau_g_calibration_all_fits.csv`,
  `scans/tau_g_calibration_raw_curves.csv` and `scans/S1b_tau_g_calibration.png`
- `calibrate_tau_g_fisheries.py` — fishery regeneration-timescale fit from RAM B/BMSY; writes
  `scans/tau_g_calibration_fisheries.csv/.json` and `scans/S1c_fishery_recovery.png`
- `calibrate_bf_af_provisioning_leg.py` — provisioning-book `b_f`/`A_f` calibration against FAOSTAT/OWID + the
  measured NFA cropland biocapacity, and the aggregate-attribution (cropland vs non-cropland book); writes
  `scans/bf_af_calibration_series.csv` and `scans/S1d_bf_af_calibration.png`
- `real_series_aggregation_face.py` — the aggregation-face figure (Figure 1) from the aggregate NFA series
- `topdown.py`, `_run_topdown.py`, `_run_sensitivity.py`, `r1_basin.py`, `r1_figure.py`, `r2_figure.py`,
  `recovery_metric_and_tau_p_scan.py` — the model analyses, sensitivity suite, and the recovery-metric / `τ_p`
  scan (SI §S5.4–S5.5)

Full step-by-step reproduction instructions, the solver/discretisation conventions, and the input files for every
reported number are in **`REPRODUCTION_GUIDE.md`** in this package.

## Archival / deposition

The journal policy permits external code deposition. For a formal archival record we recommend depositing this
package (the `model_sims/` code, `data/`, the calibration scripts and generated series, and this supplementary
package) in a persistent repository before acceptance, e.g.:

- **Zenodo** (recommended) — DOI-minted archive of the code release; export the git records as a release archive.
- **GitHub** — the working repository is public; a tagged release is the canonical, citable code artefact.

The deterministic model requires no random seed. The reproducibility statement in the manuscript (§Numerics) and
`REPRODUCTION_GUIDE.md` specifies the solver, `dt`, history functions, and termination convention for every
reported number. Where a fit is right-censored or pinned at a parameter bound (e.g. the six forest `τ_r` fits at
the 120-yr bound, the 13 right-censored fishery trajectories), this is disclosed rather than reported as an
estimate.

## Third-party content

Third-party datasets (NFA, FAOSTAT/OWID, 2ndFOR, RAM) are identified and cited above and redistributed in this
package solely for reproduction. The regeneration-timescale calibration is a numerical fit to the cited raw
curves and does not re-distribute any additional third-party data.

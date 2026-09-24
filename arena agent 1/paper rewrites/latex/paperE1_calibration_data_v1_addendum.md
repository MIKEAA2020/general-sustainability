# Paper E1 — Calibration Data Record v1, Addendum (release-asset findings)

**Base:** `paperE1_calibration_data_v1.md` (pushed `5b1f8b8`). **Scope:** inspection of the repository's two GitHub releases (owner request) and cross-verification of their data holdings against the record and against the primary sources. **All cross-checks pass; decision points 1(c) and 2 of the base record are resolved.**

## 1. The two releases (inventoried 2026-09-24)

| Release | Assets | Contents |
|---|---|---|
| `edwards-framework-e1` (2026-09-12) | `workspace-edwards-ecomod.sustainability.zip` (58.9 MB); `workspace-edwards.framework.2nd.zip` (77.3 MB) | Full workspace snapshots. The first contains `gs_clone/wave_e_cod/` (the Northern cod applied campaign: locked-provenance data + results) and `gs_clone/wave_e_edwards/` (Edwards Aquifer groundwater system, Texas: J17 well raw series, EAA discharge 1934–2023, USGS Comal Springs and recharge 1934–2024, Niño 3.4 indices). The second adds `arena_agent_1/` with further applied panels: Peru anchoveta + ENSO (SAU reconstructions, SAI), Iceland cod (ICES 27.5a) and haddock series, RAM target-stock tables, adh fisheries cohorts, E1–E4 rerun campaigns, `audits_E1_E3/`, `framework/`, specifications, and five ECOMOD-26-1191 review documents (`ECOMOD-26-1191_review.md`, `_findings_register.md`, `_proposed_upgrades.md`, `_root_cause_analysis.md`, `IMPLEMENTED_revision_ECOMOD.md`). |
| `compendium-v1.0` (2026-08-26) | `workspace-01a00d79-….zip` (142 MB) | A separate dynamical-systems programme (Julia depot, Hopf/Floquet/fold verification scripts) with 7 data files (`g3p_basin_gwsa.csv` = basin groundwater storage anomaly; `ram_target_stocks.csv`; `peru_anchoveta_catch_sau.csv`; fold tables). Tangential to the applied flagship. |

**Hygiene note.** The `edwards-framework-e1` asset contains a `.github_pat` file. If that token is live, it should be revoked/rotated; release assets are downloadable by anyone who can reach the repository.

## 2. Canonicalized dataset: `paperE1_calibration_data_v1_wave_e_cod/`

The nine files of `gs_clone/wave_e_cod/data/` are copied verbatim into the repository tree beside the base record, together with their locked provenance file:

| File | Content | Cross-verification performed this round |
|---|---|---|
| `ncam_2016_table_a2.csv` | The paper's input series (DFO 2016 Table A2; SSB, M, F, abundance, recruits), 1983–2015 | **33/33 years, zero mismatches** against the independent PDF extraction made today for the base record; LRP recomputed from the file = 884.58 kt (identical) |
| `xtencam_table17_ssb.csv` | **xteNCAM SSB 1954–2024 with 95 % CI columns and SSB/Blim ratios** (Regular et al. 2025, Table 17, Res. Doc. 2025/048 pp. 67–70) | Checkpoints 2005 = 26, 2017 = 451, 2024 = 342 all pass; implied Blim = 275.8 ≈ 276 kt; 71 rows |
| `dfo_2025_table1_landings.csv` | Official landings 1954–2023 (Regular et al. 2025 Table 1) | 2015 = 4,436 t, matches DFO (2016) reported landings |
| `dfo_2025_table1_landings_partial.csv` | 2J3KL totals 1954–1993 (earlier parser pass) | 1983–1993 identical to Schijns et al. (2021); 1956 differs (236 vs 263 kt), outside forecast windows |
| `catch_schijns_2021.csv` | Catch reconstruction 1508–2019 family (Schijns et al. 2021 ICES JMS 78:2675, Table 1) | documented: 2015 value matches DFO (2016) exactly |
| `rv_fall_abundance_schijns_table3.csv` | Fall RV abundance index (Schijns Table 3, citing DFO 2021b) — NCAM input, used only as noisy start state | provenance locked in SOURCES.md |
| `capelin_acoustic_observed.csv` | Capelin acoustic biomass, observed years only (Zenodo 17515115, NAFC/Steele et al. 2025; + 2023 = 331.3 kt Murphy et al. 2025); missing years listed, no interpolation | **the hidden-regime covariate for the applied paper** |
| `SOURCES.md` | Locked provenance: sources, units, pooling rules ("do not pool NCAM 2016 with xteNCAM"), F/M stored as diagnostics only | read in full; consistent with the base record |

**Note on thresholds (resolves base-record decision 2).** The 276 kt auxiliary threshold used by the applied paper is the **xteNCAM Blim** (= 40 % Bmsy under the new model), distinct from the 884.6 kt 2010/2016 NCAM LRP and from the 315 kt figure reported in press coverage of the October 2023 framework revision; the file set uses Blim = 276 kt consistently, and the 2025 revision of the LRP remains to be pinned to the 2025/2026 SAR documents (base-record decision 5).

## 3. Effect on the base record's decision points

1. **Series definition (decision 1).** Option (c) no longer requires digitizing Res. Doc. 2025/048 — `xtencam_table17_ssb.csv` already provides the new-model series 1954–2024 with confidence bands. Recommended design unchanged: RAM v4.66 1983–2021 as primary extension, xteNCAM 1954–2024 as the current-science sensitivity panel.
2. **Thresholds (decision 2).** Run all three: 884.6 (NCAM LRP), 276 (xteNCAM Blim, already the paper's auxiliary threshold), and the pinned post-revision LRP when the SAR lands.
3. **Blind-window case study (decision 3):** unchanged, and `capelin_acoustic_observed.csv` adds the real hidden-regime covariate (capelin collapse) with declared missing years — the observation-gap structure is part of the data.
4. **Second and third systems.** The Edwards Aquifer panel (wave_e_edwards) and the anchoveta–ENSO and Iceland-cod panels (arena_agent_1 in the second asset) are candidate replications for the same monitoring/viability machinery; they remain release-resident and are not canonicalized here.
5. **ECOMOD-26-1191 review documents** (five .md files, second edwards asset) concern the applied paper's journal review and its implemented revision; they are referenced here and left release-resident pending the owner's instruction on where the review record should live.

## 4. Verification log (this addendum)

| Check | Result |
|---|---|
| Table A2 digitized vs independent PDF extraction (33 yr × 3 series) | 0 mismatches |
| LRP recomputation from digitized file | 884.58 kt — identical |
| xteNCAM checkpoints (26 / 451 / 342) | 3/3 pass |
| xteNCAM implied Blim | 275.8 ≈ 276 kt |
| Landings 2015 cross-check | 4,436 t — match |
| Release inventory (3 assets) | complete; see §1 |

# Supplement (v2) to "Does a one-pool water-balance model improve forecasts of
Edwards Aquifer head? A scored test at J-17"

Companion to carrier of record `paperE3_edwards_forecast_ladder_v24_humanized` (stamp `se24-c1375ed`; values below unchanged from the frozen layers they cite). Section S1 carries the independent replication of the uncertainty layer of
Section 5.3.1; Section S2 carries the truncated-detail climate fixed-window
record of Section 5.4. All values are archived with the analysis code and
re-compute from the registered per-origin forecast files.

## S1 Independent replication of the uncertainty layer

An independent replication of this layer is registered with the repository: the archived script `campaign_e3_dm_uncertainty.py`, a second Diebold–Mariano + moving-block-bootstrap implementation — HAC lag h − 1 with unweighted truncation and population-variance scaling, block length h, 20,000 replications, seed 0, deterministic (byte-identical on re-execution) — reading the same registered per-origin forecast file. Its verified output (archived alongside it) reproduces every load-bearing reading: the M1 retention margin DM z = −0.86 with block CI [−1.22, +0.56] ft (bootstrap p = 0.38); the M2m edge over persistence (p = 0.001); the h = 5 climatology win (p = 0.035). It also registers two rows this table does not carry — the h = 1 climatology loss (+2.94 ft against persistence, p = 0.046) and the M2 h = 5 loss (+12.4 ft, p < 0.001) — both consistent with the readings above. The two implementations use different seeds, block lengths, HAC weighting, and variance conventions, and agree on every conclusion: the 0.39-ft AR(1) retention margin is statistically indistinguishable from zero, the M2m edge is the only one-year margin that separates from noise, and the five-year climatology win survives.

## S2 Climate-informed modules on the remaining fixed windows

The remaining fixed windows complete the same record: drawdown 1951–56, M2_Renso 24.30, M2_Rprecip 28.67, M2_combo 24.70, precipitation oracle 18.16 ft; pre-permit wet 1991–95, M2_Rprecip 22.03, M2_Renso 23.03, M2_Rar 23.94, M2_combo 25.71, oracle 10.98 ft; critical-period era 2015–23, M2_Rprecip 14.52, M2_Rar 14.67, M2_Renso 16.01, M2_combo 16.57, oracle 9.75 ft — on this one window the two climate-informed modules M2_Rprecip and M2_Rar edge past M1 by about one foot (14.52 and 14.67 versus 15.62 ft). On the recharge target itself the fixed-window scores are an order of magnitude coarser on every window (climate modules 199–937; precipitation oracle 80.7–487, against the 556 × 10³ acre-ft climatology scale of the rolling record), so the marginal head advantage is a window-specific result, not a recharge forecast, and it does not enter the abstract.

---

## S3 Reproducibility package

All values in the carrier and in S1–S2 recompute from the registered scripts below, archived at https://github.com/MIKEAA2020/general-sustainability; checksums (md5, first 8 hex) pin the release state. Execution is deterministic throughout — a fresh environment regenerated every archived result file byte for byte. Two independent DM/bootstrap implementations (10,000 and 20,000 replications, different seeds, block lengths, HAC weighting, and variance conventions) agree on every load-bearing conclusion; both are registered, and the nClimDiv precipitation workbook is the sole raw file not redistributed (provenance URL archived in the sources index; scoring from the registered analysis panel does not require it).

| Script (repo path) | Role in the paper | md5 | |
|---|---|---|---|
| `wave_e_edwards/src/build_panel.py` | Builds the registered twenty-column analysis panel (dataset of record) | `2cfd1649` | results analysis panel |
| `wave_e_edwards/src/build_climate.py` | Builds the climate (Niño 3.4, precipitation) panel columns | `356af249` | climate panel |
| `wave_e_edwards/src/run_ladder.py` | J-17 model ladder scoring, persistence and oracle diagnostics | `e01f29cd` | results rolling_forecasts.csv, window tables |
| `wave_e_edwards/src/e3_audit_uncertainty.py` | Main post-freeze uncertainty layer: DM + Newey–West HAC + moving-block bootstrap, 10,000 replications, seeded, deterministic | `074ff015` | wave_e_edwards/results/e3_audit_uncertainty.json |
| `batch 7 (audits of agent arena 1 paper rewrites)/campaign_e3_dm_uncertainty.py` | Independent replication of the same layer: NB = 20,000, seed 0, byte-identical re-execution | `30963493` | results/e3_dm_uncertainty.csv |
| `arena_agent_1/other documents/rerun_campaigns/campaign_e3_pumpage_scenarios.py` | Pumpage counterfactual layer of Section 5.6 | `c3fe4fe3` | scenario table outputs |
| `wave_e_edwards/src/make_figures.py` | Figures 1–5 of the main text | `57c17e29` | figs/fig1_series…fig5_fibre |

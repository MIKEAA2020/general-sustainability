# Paper 5: recovery and verification of the August-8 computation originals

Provenance: release asset `workspace-01a00d79-f20f-70dc-938a-8c93ce245a8c.zip`
(142 MB, release `compendium-v1.0`, "2nd workspace", published 2026-09-04),
a workspace snapshot whose loose root files include the paper-5 computation
originals dated 2026-08-08. None of these files existed in the tracked tree
(the tracked `stage_scan_recovered/droop_test.py` is a 2026-09-01 reconstructed
shim, explicitly documented as such; the original was "not among the recovered
files"). Verification runs below were executed 2026-09-11 (numpy 2.3.5,
scipy 1.17.1, Python 3.13.14) against the zip originals.

## 1. Inventory (all paths relative to this deposit directory)

| File | Bytes | sha256 (first 12) | Role |
|---|---|---|---|
| `ram_target_stocks.csv` | 80649 | `3100cfa46ff6` | Screen input panel: 58 forage-fish stocks, tidy stockid/tsyear/F/TC/SSB |
| `ram_crosssection.py` | 5099 | `626ff54a936d` | Spectral screen: SSB CV + Lomb-Scargle band powers A-D vs per-stock AR(1) null (200 sims, seed 7), linear detrend, n>=20 filter |
| `ram_crosssection.log` | 4583 | `aaa7570fa87e` | Original 2026-08-08 run record: 42 stocks pass filter, 1 marginal B-band flag (PANCHNCHSP) |
| `sampled_governance.py` | 5199 | `19e4a325b2a4` | Sample-and-hold review-interval simulator (eta in {0.914, 3.0}) |
| `sampled_governance_results.md` | 5456 | `e0571234bcd4` | Run record: sprat window T_r 6-12 yr P~8; anchovy T_r 2-5 yr P~4; cod stable everywhere; annual stable; dt-convergence triples |
| `cod_sprat_discriminator.py` | 3652 | `a302850c94d3` | Three-way (institutional/cohort/stable) test, Iceland cod + Baltic sprat |
| `cod_sprat_discrimination.md` | 7505 | `5e21444289d9` | Run record: cod institutional rejected both eta; sprat null (tau below window); sprat CV 0.400/n=50/low-frequency variance |
| `cod_sprat_disc.log` | 6433 | `8809216f58f0` | Original run log (48 grid verdicts) |
| `noise_robustness.py` | 6764 | `63da9542619c` | Lognormal assessment-error robustness of sampled windows + AR(1)-noise probe |
| `noise_robustness.log` | 1984 | `f9820375014b` | Original run record (T=2000, 3 seeds; RuntimeWarnings reproduced) |
| `droop_test.py` | 17977 | `28197b3bc43a` | ORIGINAL Droop-coupling test S1-S5 (supersedes the Sept-1 shim); also defines base-core constants imported by the stage scripts |
| `droop_test_results.md` | 6692 | `7817f98b2470` | Run record: pipeline reproduces tau_-=3.6662/tau_+=150.3585; Droop negative (upper edge <=0.0233); eigenvalues; nonlinear confirmation |
| `droop_test_run.log` | 6360 | `6bc0befdb039` | Original run log |
| `power_demo.py` | 5951 | `3e6f8dfb7c34` | Power machinery: operating-model effort series + multiplicative lognormal noise + LS band detect vs AR(1) null (120 sims, seed 7) |
| `effort_signal_power_report.md` | 6897 | `65a5f80baffc` | Run record with the Table-3 power values: sprat 1.00/0.24/0.58, anchovy 0.02-0.14, cod FP 0.00-0.06; E-period correction (12/60 yr) |
| `peru_anchoveta_catch_sau.csv` | 1156 | `0c41ef8bd722` | Peru SAU anchoveta catch 1950-2019 (70 rows; August extraction, differs from the tracked September `anchoveta_enso/peru_sau_annual.csv`, which runs to 2024 with revised values) |
| `stage_r_window.py` | 6122 | `70a4a7080575` | Dependency closure (byte-identical to tracked recovery) |
| `stage_decomp2.py` | 8666 | `fef38fdfeb0b8` | Dependency closure (byte-identical to tracked recovery) |
| `verify_bh.py` | — | `53c62031fdfd` | NEW (2026-09-11): BH-FDR verification of the zero count on the recovered machinery |
| `rederive_power.py` etc. | — | see log | NEW (2026-09-11): power-table re-derivation attempts (window hypotheses), see section 3 |

## 2. Verification results

| Check | Outcome |
|---|---|
| `ram_crosssection.py` re-run vs `ram_crosssection.log` | BYTE-IDENTICAL (42 stocks; SPRAT22-32 n=50 CV=0.40; 1 flag: PANCHNCHSP B=0.425 vs 95% 0.407) |
| BH-FDR (alpha=0.05, 84-test target-band family) via `verify_bh.py` | 0 rejections; smallest p=0.0448 (PANCHNCHSP B). The manuscript's "BH-adjusted zero count" is VERIFIED from the recovered machinery plus the stated procedure |
| `cod_sprat_discriminator.py` re-run vs `cod_sprat_disc.log` | IDENTICAL; cod TEST1 table 18/18 cells exact (e.g. r=0.25 g=6 window (11.7,26.4) STABLE) |
| `droop_test.py` re-run vs `droop_test_run.log` | IDENTICAL (S1 tau_-=3.6662, tau_+=150.3585; S2 windows (0.00798,0.02227)/(0.00678,0.06116); S5 P=268.4/270.2, amp 7.220/7.576) |
| `noise_robustness.py` re-run vs `noise_robustness.log` | IDENTICAL (modulo warning-header paths) |
| `sampled_governance.py` spot cells | EXACT: sprat T_r=7 oscillatory P=7.96 amp=2.22; cod T_r=5 stable |
| `power_demo.py` committed driver | RUNS but yields ~0 power everywhere: T=120 is too short for the slow effort oscillation (report: full amplitude only after ~10^3 yr), and its bands/trials differ from the report's table |

Reproduction: `python3 ram_crosssection.py` (~30 s), `python3 cod_sprat_discriminator.py`
(~4 min), `python3 droop_test.py` (~3.5 min), `python3 noise_robustness.py` (~80 s);
all outputs reproduce the committed logs. Requires numpy + scipy only.

## 3. Power-table status (partially recovered)

The section-3.6 values are sourced exactly by `effort_signal_power_report.md`
section 2 (sprat (30,120): 1.00 at H=100/sigma=0.1; 0.24 at H=100/sigma=0.3;
0.58 at H=200/sigma=0.3; anchovy (8,20): 0.02-0.14; cod false-positive 0.00-0.06).
The method (`power_demo.detect`, 120 sims, seed 7) is committed, but the
long-horizon driver is not: the report cites `power_demo.power`, a function
absent from the committed file, and the committed `__main__` uses different
bands, trials (60 vs 50), and horizons. Re-derivation with documented
parameters reproduces the sprat H=100 cells (1.00; 0.24-0.26 at early windows)
and the anchovy sigma=0.3 cells (0.06-0.10, in range) but not sprat H=200
sigma=0.3 (0.86-1.00 vs 0.58) or anchovy sigma=0.1 (0.20-0.76 vs <=0.14);
window placement and the noise process (report: white lognormal; manuscript
section 2.5: "AR(1)-type noise") are underdetermined. Recommended v30 path:
commit a proper driver with documented windows and print the recomputed table.

## 4. Manuscript-alignment gaps found (for the v30 build)

1. Selection wording: section 2.4 attributes the 42 to an eligibility
   criterion; the operative filter is n>=20 valid SSB points on a 58-stock
   panel (the annual-review designation excludes zero stocks; it is applied
   by general knowledge per the script docstring). The input panel size (58)
   is unstated in the manuscript.
2. Band mismatch: section 2.4 states biomass 4-8 yr / effort 12-60 yr; the
   script implements A 2.5-5 / B 5-9 / C 9-14 / D 14-30 on SSB only.
3. Effort side unexecuted: the CSV carries F and TC columns but the script
   reads SSB only; no 12-60 yr effort screen exists. F-series screening at
   the stated band is feasible new work.
4. Robustness legs unexecuted: no detrending/endpoint sensitivity runs exist;
   either run them (cheap) or narrow the "robust" definition.
5. Case search: only the Peru SAU input series is recovered; the screening
   table and query log (section 2.6) remain author-side.
6. Eligibility table: per-stock primary verification of the annual-review
   designation does not exist (docstring is explicit); the designation stands
   as lightly-sourced.
7. eta=0.914 is a baseline constant in every script; its calibration basis
   remains undocumented (still author-blocked).

## 5. Effect on the author-blocked ledger

Recovered and verified: the 42-stock screen, spectral routines, AR(1) null
with seed, BH-adjusted zero count, sprat CV 0.40, cod/sprat discriminator,
sampled-governance window computations with dt-convergence, noise-robustness
experiments, Droop-coupling negative result, power method plus run-record
table, one case-search input series. Remaining author-side: items 3-7 above
(power driver re-runnable by the editor; case table/log and eligibility
verification strictly author-side). The section-3.5/3.6 fork need not reframe:
rebuild on these materials.

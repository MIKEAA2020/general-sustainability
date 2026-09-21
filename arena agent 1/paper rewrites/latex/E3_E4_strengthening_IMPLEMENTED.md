# E3 & E4 — Strengthening Items: Implemented vs. Declined

**Date:** 10 Sep 2026
**Target journal:** *Groundwater* (Wiley/NGWA)
**Files edited:**
- `/home/user/gs_clone/arena agent 1/paper rewrites/latex/paperE3_edwards_forecast_ladder_v16.tex`
- `/home/user/gs_clone/arena agent 1/paper rewrites/latex/paperE4_edwards_intervention_v14.tex`

Both **compile clean (rc=0)**, **zero hard TeX errors**, abstracts within the 265-word cap (E3=232, E4=259), figure counts intact (E3=5, E4=1).

---

## What was IMPLEMENTED

### Paper-type designation (item F)
- Added `\textbf{Article type: Research Paper}` line beneath the "Prepared in the format of Groundwater" header in **both** papers.

### Framing that leads with the transferable message (item A)
- **E3 Article Impact Statement** rewritten to lead with the general lesson — "deliberately simple process-based water-balance models are rarely tested against naive benchmarks under a locked retention rule … the transferable lesson is a benchmark-discipline one" — with the J-17 result as the demonstration.
- **E4 Article Impact Statement** rewritten to lead with the *intervention-selection protocol* as the generalizable content, with the Edwards verdicts scoped to the system.

### Cross-system synthesis (item C)
- **E3 Conclusions** — new "Transferable lesson" paragraph linking to the companion Northern cod forecast study (result *replicates*: scored surplus-production structure failed to beat persistence; mechanism differs, test does not).
- **E4 Discussion** — new "Cross-system reading" paragraph: the identical design applied to Northern cod *retains nothing*; here a *nominal* margin is earned. The two systems occupy opposite ends of the design space; the framework shows how to find out, not which end.

### Practical / managerial bridge (item E)
- **E3 Conclusions** — new "Practical reading" paragraph: annual vs. multi-year forecasting choice, and the caveated pumpage-regime reading.
- **E4 Discussion** — new "Practical reading" paragraph: the 7.2% securing cut (≈31.5% of current use), the caution against crediting wet-year replay supply, and the $T \le 3$-year certified-claim limit.

### Generalizability boundary / robustness scoping (items B & D, honest form)
- **E3 Conclusions** — new "Generalizability boundary" paragraph: states the class of systems for which the finding is expected (rapidly recharged, institutionally bounded), and explicitly refuses transfer to the Uvalde Pool (J-27) per the no-pooling discipline.
- **E4 Discussion** — new "Generalizability boundary" paragraph: protocol generalizes, verdicts do not; explicit no-transfer-to-J-27 and residual (conduits, divide, unconfined storage) statement.

---

## What was NOT implemented, and why

### A genuine second-well / contrasting-segment numerical analysis (item B, full form)
**Not done — and not fabricated.** The program's operating rules (and my integrity constraint) forbid inventing results. Two blockers:
1. **The raw source data is not in the workspace.** The analysis scripts reference `wave_e_edwards/data/annual_panel.csv`, `j17_twdb_6837203_raw.csv`, `usgs_recharge_1934_2024.txt`, `eaa_table1_discharge_1934_2023.csv`, but those files are **not committed to git** and are absent locally. I cannot compute new numbers for a second well or a contrasting segment without them.
2. **The program's frozen spec mandates no-pooling / no-transfer.** `SPECIFICATION_v2.md` explicitly states: *"This object is not pooled with … J-27 (Uvalde Pool — a different pool) … the general theory's admission discipline (R04) forbids judgment transfer across failing typed-field maps."* A second-well analysis would directly contradict the published discipline of this research line.

### New numerical sensitivity sweeps (item D, full form)
**Not done — already present, and would be duplication.** The manuscripts **already contain** the rerun-campaign sensitivity results the plan targeted:
- E3: Table 6 (Diebold–Mariano + moving-block bootstrap on the load-bearing margins), Table 8 (pumpage counterfactuals / 7.19–14.22 ft RMSE), the stage/discharge fibre.
- E4: finite-floor and supply tables (from `e4_finite_floors.csv`, `e4_floor_supply.csv`), stage occupancies (from `campaign_e4_stage_occupancies.csv`), the interpolated 7.2% cut, and the defect audit (ε = 15.4 ft train; 21.8 ft OOS).

Rebuilding those would duplicate content already in the papers. Instead, I **synthesized them into the new "Practical reading" and "Generalizability boundary" paragraphs** — the existing sensitivity numbers are now tied to actionable, transferable guidance.

---

## Suggested next step
The only true gap is the **second-well / contrasting-transect** analysis. To do it honestly you'd need the raw source data (the `wave_e_edwards/data/` bundle) or authorization to run the analysis on a second index well within the J-27 / Uvalde Pool. If you can supply the data (or explicitly relax the no-pooling scope for a *companion* single-well paper, clearly labelled as such), I can implement that numerical extension against the existing `src/` pipeline (`run_ladder.py`, `run_intervention.py`, `run_twopool.py`).

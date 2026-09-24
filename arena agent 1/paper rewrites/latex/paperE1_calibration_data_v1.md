# Paper E1 — Calibration Data Record (Northern cod, NAFO 2J3KL)

**Purpose.** Published-data calibration inputs for the applied flagship (the Northern cod forecast-ladder paper, `paperE1_cod_forecast_ladder`, and the programme's applied-calibration item P5). This record discharges the calibration limitation L4 of the applications note and the owner-side item R12 of the residual ledger, insofar as public data can: every number below carries a source and was verified on 2026-09-24. No model result of the programme is changed by this record; it supplies the data and the decision points for the next edition of the applied paper.

**Companion files.**
- `paperE1_calibration_data_v1_ram_timeseries.csv` — machine-readable extract of the RAM Legacy Stock Assessment Database v4.66, stock `COD2J3KL`: 172 rows, years 1850–2021, columns TBbest/TCbest/SSB/TN/R/TC/TL/F/TAC/Cadvised/CPUE/EFFORT and ratios (DOI of source database: 10.5281/zenodo.14043038).
- `paperE1_calibration_data_v1_ram_reference_points.csv` — the stock's reference-point row (24 columns, incl. TBmsybest, MSYbest, ERmsybest, SSBmsy, SSBlim).

---

## 1. The paper's current input series — verified against the primary source

The paper is driven by the **NCAM M-shift SSB series of DFO (2016), Table A2**, years 1983–2015, with LRP = 884.6 kt. The primary source (DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026, `https://waves-vagues.dfo-mpo.gc.ca/Library/365622.pdf`) has been fetched in full and the series extracted. Spawning stock biomass (kt), average natural mortality M and fishing mortality F (ages 5–14):

| Year | SSB | M | F | | Year | SSB | M | F |
|---|---|---|---|---|---|---|---|---|
| 1983 | 841.08 | 0.391 | 0.192 | | 2000 | 34.42 | 0.717 | 0.137 |
| 1984 | 863.23 | 0.377 | 0.176 | | 2001 | 29.50 | 0.905 | 0.166 |
| 1985 | 902.94 | 0.349 | 0.219 | | 2002 | 23.87 | 0.789 | 0.150 |
| 1986 | 836.00 | 0.277 | 0.208 | | 2003 | 22.07 | 0.810 | 0.063 |
| 1987 | 940.75 | 0.494 | 0.194 | | 2004 | 20.07 | 0.362 | 0.037 |
| 1988 | 886.40 | 0.335 | 0.215 | | 2005 | 25.18 | 0.288 | 0.034 |
| 1989 | 921.66 | 0.289 | 0.228 | | 2006 | 40.83 | 0.330 | 0.041 |
| 1990 | 861.92 | 0.403 | 0.187 | | 2007 | 81.10 | 0.472 | 0.029 |
| 1991 | 734.51 | 1.002 | 0.223 | | 2008 | 106.65 | 0.570 | 0.028 |
| 1992 | 381.95 | 2.214 | 0.201 | | 2009 | 104.56 | 0.599 | 0.029 |
| 1993 | 101.05 | 2.575 | 0.150 | | 2010 | 96.91 | 0.696 | 0.025 |
| 1994 | 30.55 | 2.331 | 0.086 | | 2011 | 90.56 | 0.366 | 0.029 |
| 1995 | 9.68 | 0.288 | 0.042 | | 2012 | 112.12 | 0.216 | 0.023 |
| 1996 | 16.05 | 0.341 | 0.083 | | 2013 | 169.17 | 0.207 | 0.018 |
| 1997 | 20.57 | 0.372 | 0.047 | | 2014 | 250.12 | 0.298 | 0.014 |
| 1998 | 28.25 | 0.360 | 0.124 | | 2015 | 298.65 | 0.278 | 0.014 |
| 1999 | 34.59 | 0.392 | 0.211 | | | | | |

**Cross-checks performed (all pass).**
- LRP: mean of SSB 1983–1989 = (841.08+863.23+902.94+836.00+940.75+886.40+921.66)/7 = **884.58 kt** — matches the paper's 884.6 kt (the SAR states the LRP is the average 1980s SSB, established 2010).
- Status: 298.65/884.6 = **33.8 %** of the LRP in 2015 — matches both the paper's figure caption and the SAR's "34 % (95 % CI, 28–40 %)".
- SAR summary values: 2015 SSB = 300,000 t (95 % CI, 246,000–362,000 t); F(2015) = 0.014; M(2015) = 0.28, down from 0.70 in 2010 — all consistent with Table A2.

The same SAR provides the landings/TAC history 1958–2015 (peak total catch above 800 kt in 1968; moratorium in 1992; stewardship fishery from 2006; 2015 model-estimated removals 6,900 t), and the 2016–2018 management design: a **three-year cycle with an interim survey indicator** (a full assessment is triggered if the projected autumn RV survey biomass departs from the projection; e.g. for constant 2016 catch the projection was +22 % with 75 % CI 0.9 %–49 %), with the indicator value available by early January.

## 2. Machine-readable extension: RAM Legacy Stock Assessment Database v4.66

Source: Zenodo record 10.5281/zenodo.14043038 ("Extended RAM Legacy Stock Assessment Database version 4.66", posted 2024-11-06; assessment-only variant 10.5281/zenodo.14043031). Stock row: `COD2J3KL`, "Atlantic cod Southern Labrador–Eastern Newfoundland", region Canada East Coast, assurer DFO. Extracted with the companion CSV:

- **Catch reconstruction 1850–2021** (TC/TL columns; values from 1850, e.g. 0.36 and 0.34 in the ratio columns for 1850–51 — the longest calibrated removals series available to the programme).
- **SSB 1983–2021 (39 points) as re-read by the assessment of record (2021, same NCAM family)** — the per-year extension the paper lacks (kt):

| Year | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 |
|---|---|---|---|---|---|---|---|---|
| SSB | 238 | 277 | 340 | 433 | 394 | 419 | 440 | 411 |

- **Reference points stored for the stock** (surplus-production fit of the extended database): TBmsy = 1,699,319 t; MSY = 367,813 t; ERmsy = 0.2164; SSBmsy = 1,033,200 t; SSBlim = 932,432 t.
- **Revision phenomenon (analytically relevant).** The same calendar years differ across assessment vintages: 1983 SSB is 841.08 kt in Table A2 (2016 assessment) and 735 kt in the 2021-vintage series; 2015 SSB is 298.65 kt (2016) and 277 kt (2021). The stock state is fixed; the reading moves with the assessment vintage — precisely the observation-map dependence the calculus isolates.

## 3. The 2023 framework revision — a changed observation map, not a changed stock

The October 2023 DFO framework review replaced the assessment model (xteNCAM, integrating data from 1954 rather than 1983, plus tagging, capelin abundance and an inshore sentinel index) and **redefined the limit reference point from 884.6 kt to 315 kt** (CBC News, 2023-10-25, `https://www.cbc.ca/news/canada/newfoundland-labrador/2j3kl-new-stock-assessment-model-1.7007858`: the stock "has been out of the critical zone since 2016"; 71 % probability of being in the cautious zone, against the 2021 assessment's 99 % probability of being in the critical zone). The research document of record is **CSAS Res. Doc. 2025/048** (Regular, Skanes, Kumar, Rideout, Novaczek, Hatefi, Gregory, Koen-Alonso, Dwyer, "Assessment of the Northern Cod (Gadus morhua) Stock in NAFO Divisions 2J3KL in 2024", September 2025, `https://open-science.canada.ca/server/api/core/bitstreams/b39d82e0-0184-42fb-af90-1a19d4276401/content`); the science advisory report is **SAR 2024/049** (DFO 2024a).

Status anchors under the new framework (each with source):
- **2024 assessment** (peer review 2024-03-18/21, data to end-2023): SSB = **1.2 × LRP** (95 % CI 0.7–2.1), 22 % probability of being in the critical zone, cautious zone; no SSB growth since 2016; with zero removals the probability of declining into the critical zone by 2027 is 42 %; capelin near 10 % of pre-collapse levels (Res. Doc. 2025/048 abstract). Press summary: ≈ 350 kt (CI 250–500) (SaltWire, 2025-04-08).
- **2025 assessment** (technical briefing 2025-04-03): SSB ≈ **524 kt** (CI 300–650); the LRP was revised after being deemed overestimated in the 2024 assessment (exact revised value to be pinned to the 2025 SAR when cited); recruitment at pre-1990s levels, fishing mortality low (FFAW, 2025-04-03, `https://ffaw.ca/dfo_cod_growth/`; SaltWire, 2025-04-08, `https://www.saltwire.com/newfoundland-labrador/2025-nl-northern-cod-assessment`).
- **2026 assessment** (peer review 2026-03-24/27, released 2026-04-01): SSB ≈ **540 kt** (CI 420–700); **70 % probability of being above the upper stock reference — healthy zone** of the precautionary approach framework; increase of ≈ 20 % over the previous year (SaltWire, 2026-04-02, `https://www.saltwire.com/newfoundland-labrador/northern-cod-recovery-april-2026`; FFAW, 2026-04-01, `https://ffaw.ca/northern-cod-healthy-zone/`; MSC, 2026-04-20). The stock is described by industry science staff as the largest cod spawning biomass globally; roughly half of the survey biomass since 2019 has been observed in division 2J.

## 4. Removals and management series (post-2015)

| Season | Removals framework | Value | Source |
|---|---|---|---|
| 2022, 2023 | Stewardship MAH (rolled over in 2023 for lack of survey data) | 12,999 t | SeafoodSource, 2023-06-30 |
| 2024 | Commercial fishery reopened (first in 32 years); Canadian TAC | 18,000 t (inshore ≈ 84 %, offshore 6 %; NAFO others 5 % of overall) | Government of Canada news release, 2024-06-26 |
| 2025 | TAC increase | 38,000 t (inshore 30,400 t; offshore 9.72 %); capelin TAC held at 14,533 t | Navigator Magazine, 2025-07-11; National Fisherman, 2025-10-08 |
| 2026 | Decision pending at the time of the 2026 assessment | — | SaltWire, 2026-04-02 |

Fishery removals are ≈ 5 % of total removals in 2025–26; natural mortality remains the dominant driver (DFO scientist P. Regular, SaltWire 2026-04-02).

## 5. Observation-structure facts (instances for the calculus)

These published facts are direct real-world instances of the paper-2 mechanisms and can be used as worked material in the applied flagship:

1. **Blind window with a management consequence (timing).** Partial coverage by the fall RV survey in 2021 and 2022 meant "the leading indicator of stock size could not be calculated"; no typical assessment update was possible in 2022 or 2023, and the stewardship maximum was rolled over at 12,999 t (Res. Doc. 2025/048; SeafoodSource 2023-06-30). The survey vessel CCGS Alfred Needler was condemned in February 2023. A literal observation gap of two assessment cycles with a frozen harvest rule.
2. **Definition-dependence of the verdict (fibre/index).** The October 2023 revision moved the same stock from "critical since 1991" to "out of the critical zone since 2016" by redefining the reference point (884.6 → 315 kt) and the model, without any change in the stock. The verdict is a property of the observation map.
3. **Hidden-regime dynamics.** The M-shift series itself: natural mortality 0.28–0.49 through the 1980s, spiking to 2.21/2.58/2.33 in 1992–94 (the "catastrophic mortality event", flagged in the 2016 SAR as controversial), 0.70 in 2010, 0.28 in 2015; capelin collapse as the ecosystem driver. A regime variable observed only through its effect on the index.
4. **Witness disagreement.** A published VPA re-analysis (Fisheries Research 220, 2019, "The state of Canada's iconic Northern cod: A second opinion", `https://www.sciencedirect.com/science/article/abs/pii/S0165783619301614`) concludes the NCAM biomass is overestimated by ≈ 35 % and attributes the 1990s decline substantially to fishing rather than natural mortality. Two maintained witnesses, divergent readings — the certification-limits phenomenon in the wild.
5. **Review-timing rule.** The 2016 design (three-year cycle; full assessment triggered when the interim January indicator leaves the projected survey band, e.g. +22 % with 75 % CI 0.9 %–49 %) is a management operationalization of "the review must land before the worst-case exit time" — the boundary-viable timing identity of the monitoring companion.

## 6. Carbon-side dataset (second application candidate, P5)

Published, versioned data for a carbon-permanence instance of the same mechanisms:
- California compliance-program buffer pool: **24.6 MtCO2e** as of October 2020; CARB retired **1.12 MtCO2** for two verified wildfire reversals; post-2022 verified wildfire losses exceed **5 MtCO2** (project-reported total 3.95 MtCO2 for ACR255/CAR1102 vs satellite-based estimates 7–28 % higher; CarbonPlan buffer analysis update, 2022-12-01, `https://carbonplan.org/blog/buffer-analysis-update`).
- Systematic over-crediting estimate **30.0 MtCO2e** (90 % CI 20.5–38.6) from digitized project records, dataset DOI 10.5281/zenodo.4630684 (Haya et al., Frontiers in Forests and Global Change, 2023; preprint 2021).
- Protocol terms: ACR minimum project term 40 years; buffer contribution 23.5 ± 2 % (ibid., Table 4).
Mapping: wildfire reversal = hidden regime; buffer pool = certainly-safe set; verification lag (multi-year post-fire surveys) = T_obs; regional common-practice baselines = fibre coarseness.

## 7. Search and retrieval log (all accessed 2026-09-24)

| # | Query / action | Yield |
|---|---|---|
| 1 | DFO Northern cod 2J3KL stock assessment 2023 2024 CSAS SSB | Res. Doc. 2025/048 (full text), SAR 2024/049 reference, QP note DFO-2024-QP-00003, FFAW/SaltWire 2025–2026 status articles |
| 2 | NCAM M-shift SSB DFO 2016 Table A2 LRP 884.6 | 2016 SAR PDF (waves-vagues 365622.pdf), fetched in full; Table A2 extracted and verified |
| 3 | RAM Legacy database Northern cod | Zenodo v4.66 record; database downloaded and parsed (stock COD2J3KL) |
| 4 | CSAS 2026 assessment healthy zone | SaltWire/FFAW 2026 articles; MSC announcement 2026-04-20; SAR 2026 status (in press) |
| 5 | Northern cod TAC 2024 2025 | canada.ca reopening release (18 kt); Navigator/National Fisherman (38 kt) |
| 6 | Carbon buffer pool reversal dataset | CarbonPlan update; Haya et al. 2023 + Zenodo 4630684 |
| 7 | fetch waves-vagues 365622.pdf (7 chunks) | full 2016 SAR text incl. Tables 1–2, A1–A2 |
| 8 | RAM v4.66 download + parse | companion CSVs (timeseries 172 rows; reference points 1 row) |

## 8. Decision points for the applied edition (owner confirmation required)

1. **Series definition for re-scoring.** (a) 2016 Table A2, 1983–2015, unchanged (frozen historical test); (b) RAM v4.66 old-model series, 1983–2021 (homogeneous extension; recommended primary); (c) xteNCAM series 1954–2023 (current science; requires digitizing Res. Doc. 2025/048). A (b)-primary/(c)-sensitivity design scores the ladder on the full modern history.
2. **Threshold scenarios.** LRP = 884.6 kt (1983–89 mean, verified), LRP = 315 kt (current), and the paper's existing 276 kt auxiliary threshold; the 884.6 → 315 revision is itself the definition-dependence experiment.
3. **Blind-window instance.** The 2022–23 assessment suspension (two missed cycles; quota rollover) as the real T_obs case study.
4. **Reference points for the viability model.** MSY = 368 kt, TBmsy = 1.70 Mt, ERmsy = 0.216 (RAM v4.66) as the production-model anchors; the viability floors remain the paper's LRP-based set.
5. **2026 SAR pin.** When CSAS posts the 2026 science advisory report, pin the revised LRP/USR values and the per-year new-model series, and cite the SAR in place of the press summaries.

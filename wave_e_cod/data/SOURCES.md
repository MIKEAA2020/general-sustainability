# Data provenance (locked)

## Observation series (SSB, F, M)

**Source:** DFO. 2016. Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016.  
DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026, Table A2.  
M-shift formulation of NCAM.

**File:** `ncam_2016_table_a2.csv`

These are *joint assessment outputs*, not independent field measurements.  
F and M are **not** used as exogenous drivers of an SSB forecast (that would reconstruct the same model).  
They are stored only as diagnostics.

SSB is treated as a noisy observation \(\hat z_t\) of a latent stock.  
Subset 1991–2015 matches the values independently verified in A014.

**Do not pool** with xteNCAM (DFO 2024/2025). Different model, different LRP, different start year.

## Catch

**Pass 1 (regime, approximate).** 240 / 120 / 5 kt from DFO (2016) prose.

**Pass 2 (year-by-year).** `catch_schijns_2021.csv`  
Schijns, Froese, Hutchings & Pauly (2021), *ICES J. Mar. Sci.* 78:2675–2683, Table 1.  
Reconstruction of Hutchings & Myers (1995) updated with NAFO STATLANT / DFO to 2019.  
Units: tonnes, converted to kt.  
2015 value 4,436 t matches DFO (2016) reported landings exactly.

Reported landings remain lower than total removals (recreational, discard). xteNCAM uses catch *bounds*, not this point series.

## Fall RV abundance index

`rv_fall_abundance_schijns_table3.csv`  
Schijns et al. (2021) Table 3, citing DFO (2021b) Table 2.  
This index is an *input* to NCAM, not an independent stock. Used only as a noisy start state (q̂ × I), never as an F/M driver.

## Official landings (DFO 2025 Table 1)

`dfo_2025_table1_landings_partial.csv` — 2J3KL overall totals, 1954–1993 only  
(parser reached Table 1 through 1993; later years not extracted).

1983–1993 totals are **identical** to Schijns et al. (2021).  
1956 differs (DFO 236,210 t vs Schijns 263,210 t). That year is outside the forecast window.

## xteNCAM (DFO 2024/25)

`xtencam_table17_ssb.csv` — Regular et al. 2025 Table 17, pages 67–70 of  
`https://www.dfo-mpo.gc.ca/csas-sccs/Publications/ResDocs-DocRech/2025/2025_048-eng.pdf`  
Checkpoints: 2005=26, 2017=451, 2024=342.  
`dfo_2025_table1_landings.csv` — Table 1, 1954–2023.  
**Not pooled** with NCAM 2016. LRP = 276 kt.

## Capelin \(W\)

`capelin_acoustic_observed.csv` — observed years only from  
Zenodo 17515115 (`cap_acoustic.csv`, NAFC / Steele et al. 2025)  
plus 2023 = 331.3 kt (Murphy et al. 2025).  
No interpolation. Missing years: 1983–84, 1993–95, 1997–98, 2006, 2016, 2020–22.

## Institutional events

- Moratorium announced 2 July 1992 (DFO; A014 verified).
- Commercial reopening announced 26 June 2024, TAC 18,000 t (not used in 1983–2015 hindcast).

## LRP used here

**[N]** 2010/2016 PA LRP = mean 1980s SSB.  
Computed from Table A2 years 1983–1989 (complete 1980s years in the table) = 884.58 kt.  
SAR states 2015 SSB was 34% of LRP; 298.65 / 884.58 = 0.338. Consistent.

The 2023/24 LRP (40% BMSY under xteNCAM) is a **different specification** and is not used.

## xteNCAM 2026 vintage (DFO 2026 SAR — "Stock Assessment to 2026")

**Source:** DFO. 2026. NAFO Divisions 2J3KL Northern Cod (Gadus morhua) Stock Assessment to 2026.
Fisheries Science Advisory Report; regional peer review March 24–27, 2026. Posted
open-science.canada.ca, handle 123456789/4756, accessioned 2026-08-11;
bitstream `NAFODivisions-2J3KL-NorthernCodStockAssessment-2026-4133775x.pdf`
(MD5 1cdc8ac181a82e9148429ff9d3f444df), fetched 2026-09-16.

**File:** `dfo_2026_sar_published_points.csv` — transcribed verbatim from the typeset
Table 1 (SSB, SSB/LRP, recruits, M, F for 2022–2026) and the Science-Advice bullets.
Figure-digitized rows in the fetched text were NOT transcribed (not typeset data).

**Provenance notes:**
- **Model revision:** tagging data excluded from 2020 onward (retrospective-instability
  fix) — the tail of the series is revised relative to the archived 2025 vintage
  (ResDoc 2025/048): 2024 SSB 338 kt here versus 342 kt archived. **Do not pool.**
- The archived `xtencam_table17_ssb.csv` (2025 vintage, through 2024) stays
  authoritative for the reported frozen verdicts; the 2026 vintage points are for
  new-origin scoring only.
- Origin targets: SSB_2025 = 449 kt (363–554) for origin 2024 h=1; SSB_2026 =
  542 kt (423–696) for origin 2025 h=1. Published 2026-08-11 — earlier than the
  sheet's anticipated "vintage following the 2026 assessment".
- Remaining input for catch-supplied module scoring: annual reported landings /
  removals for 2024–2025 (SAR tabulates neither; authorized removals 2025 =
  42,867 t is official). Pending its own provenance entry before use as a driver.

## DFO 2026 vintage -- catch driver (owner-gated ingestion 2026-09-16)

Source: Regular, P.M., Skanes, K., Kumar, R., Rideout, R.M., Novaczek, E., Trueman, S.,
Gregory, R.S., Koen-Alonso, M., and Dwyer, K.S. 2026. Assessment of the Northern Cod
(Gadus morhua) Stock in NAFO Divisions 2J3KL in 2025. DFO Can. Sci. Advis. Sec. Res.
Doc. 2026/026. v + 101 p. (2026-vintage full assessment; the March 24-27, 2026 RPR
document behind SAR handle 123456789/4756.)
- Handle: 123456789/4385 (open-science.canada.ca); item uuid 93252a9d-562c-4f7d-85f4-2a932affe7d9
- PDF bitstream uuid a265b88b-9dcb-47d4-aec5-5d0a859d6bb7; MD5 d25ede381c5ebf2ad4c725801658919c; 14,218,318 bytes
- Transcribed to: dfo_2026_resdoc026_reported_landings_2020_2024.csv (typeset Table 1
  + REPORTED LANDINGS prose only; chart-digitized rows rejected)
- Status of catch-driver series (calendar year, per the ResDoc: management year is
  Apr 1-Mar 31 but catch statistics are reported in calendar year):
  * Landings series officially updated through 2024 (Table 1: "2016-24 were added").
    2020-2023 rows rounding-consistent with the archived 2025-vintage file
    (dfo_2025_table1_landings.csv) -> NO tail revision of the catch series; do-not-pool
    honored anyway (this new file is separate; archived file untouched).
  * 2024 = 15,661 t (provisional, prose) = 15.7 kt (Table 1). NOW OFFICIAL catch driver
    for origin-2024 catch-supplied modules.
  * 2025 calendar-year landings are NOT in the science series yet (ResDoc data end 2024;
    assessment used landings through 2025 without tabulating). NOT archived.

User-supplied leads (2026-09-16) and their official disposition:
- "32,700 t landings in 2025": traces to DFO communications backgrounder "Northern Cod:
  Socio-Economic Performance" (canada.ca, 2026-06-12), echoed by newfoundnews.ca.
  Official-communications grade, NOT a CSAS science table -> SECONDARY RECORD ONLY,
  never data (rule unchanged). Await the next CSAS vintage for schedule-type tabulation.
- "21,317 t for the 2024-25 management season": identified in ResDoc 2026/026 Table 1
  MAH/TAC column (calendar 2024 = 21.3 kt) as the AUTHORIZED allocation, i.e., a quota,
  NOT landings. Recorded in the new CSV as MAH_TAC_authorized; must not be used as the
  catch driver (frozen spec used reported landings).
- "4X5Y cod 466 mt": different stock (4X5Y Atlantic cod), out of scope for 2J3KL; excluded.

Also located in ResDoc 2026/026: Table 17 (pp. 46-47), full xteNCAM SSB series with 95%
CIs through 2025 (2026 vintage, tagging-excluded) -- owner-gated candidate for a future
2026-vintage carrier for new-origin work; NOT transcribed yet (vintage rules).

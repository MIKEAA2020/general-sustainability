# Sources — Wave E Edwards San Antonio Pool

No figure was digitized. No GRACE product is used as \(z\).

## Primary \(z\): J-17 daily high water elevation

- File: `j17_twdb_6837203_raw.csv`
- URL: https://waterdatafortexas.org/groundwater/well/6837203.csv
- Well: TWDB state well 6837203; EAA AY-68-37-203; cooperator ID J17
- Entity: Edwards Aquifer Authority, served by Texas Water Development Board
- Columns used: `datetime`, `daily_high_water_elevation(ft above msl)`, `status`
- Period in file: 1932-11-12 to 2026-08-23
- Status `D` = historical daily; `R` = recent/provisional (2023-03 onward in this pull)
- Land-surface elevation used by TWDB: 731 ft. AMSL is the EAA management unit.
- Literature note (not re-derived): pre-continuous J-17 values include the
  Beverly Lodges well composite (see edwardsaquifer.net/j17.html). Official
  composite used as published.
- Pulled: 2026-08-24.

## Driver \(R\): estimated annual recharge, 1934–2024

- File: `usgs_recharge_1934_2024.txt`
- Umphres, G. D., and Choi, N. J., 2025, Estimated Annual Recharge to the
  Edwards Aquifer in the San Antonio Area, by Stream Basin or Ungaged Area,
  1934–2024: USGS data release, https://doi.org/10.5066/P1BI62NY
- ScienceBase item: `67dc2a99d34eae450ac1c397`
- Method: Puente (1978) stream-loss / ungaged-area transfer; post-2004 rainfall
  from calibrated NEXRAD (EAA). Independent of J-17.
- Units: thousands of acre-feet per calendar year.
- `Total` is the M2 driver. `R_east` = Basin_5+6+7+9 is stored, not used for
  selection.
- Basin names: `usgs_recharge_basin_inputs.txt` from the same item.

## Driver \(P\): estimated annual well discharge, 1934–2023

- Extracted from EAA, 2024/25, *2023 Groundwater Discharge and Usage*, Table 1
  (USGS letter report to EAA, 5 April 2024).
- PDF: `eaa_2023_groundwater_discharge_and_usage.pdf`
- URL: https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf
- File: `eaa_table1_discharge_1934_2023.csv`
- Column used as driver: `wells_kaf` only.
- `springs_kaf` is stored and **not** used as a driver (endogenous).
- Checkpoints vs published prose: 1934 wells 101.9; 1956 springs 69.8;
  1989 wells 542.4; 1992 total 1,130.0 / springs 802.8; 2019 wells 358.6;
  2023 wells 320.5 / springs 151.2.

## Fibre \(Y\) (post-selection only): Comal Springs

- File: `usgs_08168710_comal_dv.rdb`
- USGS 08168710 Comal Springs at New Braunfels, TX
- Daily mean discharge, parameter 00060, statistic 00003
- URL: https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=08168710&startDT=1927-01-01&endDT=2026-08-25&parameterCd=00060&statCd=00003
- Pulled: 2026-08-24.
- Not used to fit or retain any module.

## Institutional thresholds (not fitted)

- EAA Critical Period Management, San Antonio Pool, Stage I: 10-day average
  J-17 < 660 ft AMSL, or Comal < 225 cfs, or San Marcos < 96 cfs; 20% reduction.
- Stages II–IV: 650 / 640 / 630 ft and 200 / 150 / 100 cfs (Comal).
- Source: https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/
  and the stage table at https://www.edwardsaquifer.net/restrictions.html
- Stage I trigger was 650 ft until the 2007 rule change. 660 is not applied
  as if it existed in 1956.
- Comal ceases near 618 ft AMSL (edwardsaquifer.net/j17.html). Physical, not
  the Stage I line.

## Pass 2 climate predictors (causal at origin \(t\); not \(z\))

- Niño 3.4 monthly SST, HadISST, 1870–2025: `psl_nino34_long.data`
  https://psl.noaa.gov/data/timeseries/month/data/nino34.long.data
  Predictor: Sep–Nov mean anomaly vs 1991–2020 monthly climatology.
- Texas nClimDiv precipitation, NCEI `climdiv-pcpndv-v1.0.0-20260806`
  https://www.ncei.noaa.gov/pub/data/cirs/climdiv/climdiv-pcpndv-v1.0.0-20260806
  **Not committed** (4.5 MB, regenerable). Derived annual columns live in `annual_panel.csv`.
  CD 06 Edwards Plateau and CD 07 South Central; annual sum, inches.
  Predictor: mean of the two divisions, year \(t\).
- CPC ONI (`cpc_oni.ascii.txt`) stored as a 1950+ checkpoint, not the Pass 2 driver.

Same-year \(\mathrm{corr}(R,\bar P)=0.78\). Lagged \(\bar P_t\) and \(\mathrm{SON}_t\) are the causal objects.

## Explicitly unused

- GRACE / G3P / any gravimetric storage reconstruction.
- MODFLOW, GWSIM, or any inverted head field.
- J-27 Uvalde index well (different pool).
- San Marcos Springs (08170000) — not this fibre.
- Any phosphorus catchment series.

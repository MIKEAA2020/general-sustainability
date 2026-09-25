# Multi-Stock Panel Discrimination Study (v1 record) — opus U17 first pass

**Date:** 2026-09-26. **Artifacts:** `applied_panel_discrimination_v1.py` (18/18 exact checks) reading the locked panel extract `paperE1_calibration_data_v2_ram_panel_v1.csv` (498 stock-years; 10 Atlantic cod stocks). **Data provenance:** RAM Legacy Stock Assessment Database v4.66 (2024-11-06), Zenodo DOI 10.5281/zenodo.14043031, file `RAMLDB v4.66.zip` md5 `ed6d7cd3f7da1fdcbc60015c3d65014b`, sheet `timeseries_values_views` (SSB, TC). **Provenance cross-check:** RAM v4.66's COD2J3KL 2016–2021 equals the viability paper's locked database extract exactly (340, 433, 394, 419, 440, 411 kt) — the paper's extract is this release.

## Design

Panel (opus's requested structure): controls CODNEAR (NE Arctic), CODICE (Icelandic), COD3Ps (3Ps — its 1993–97 closure and full recovery noted); collapse stocks with their episode years: COD2J3KL (1992 moratorium), CODGB (1994), COD4TVn (1993), COD4VsW (early 1970s), CODIS (1990s), CODKAT (2000s), CODFAPL (early 1990s). Labels are fixed by design; arithmetic label rules were tested and rejected because the record-max of 2J3KL is vintage-suppressed (839 kt at the 2021 vintage vs 941 kt at the input vintage), which flips recovery-bar labels on vintage choice. Certificates: C1 worst step < 1 (vacuous control); C2 some 5-year window with end ≤ ¾·start (level statistic); C3 some step with harvest-free bracket upper bound max{ρ+r, ρ/(1−r)} < 1 (the paper's certificate, catch ratio r = C(t+1)/S(t)); C4 two consecutive C3 steps.

## Results (alarm years)

| Stock | Label | C2 | C3 | C4 |
|---|---|---|---|---|
| COD2J3KL | 1993 | 1992 | **1992** | 1993 |
| COD3Ps | — | 1993 | — | — |
| CODNEAR | — | 1951 | — | — |
| CODICE | — | 1961 | — | — |
| CODFAPL | 1991 | 1979 | 1978 | — |
| CODGB | 1994 | 1984 | — | — |
| CODIS | 1995 | 1977 | 1978 | 2006 |
| CODKAT | 2008 | 2002 | — | — |
| COD4TVn | 1993 | 1959 | **1993** | **2003** |
| COD4VsW | 1974 | 1975 | **1974** | 1997 |

**Finding.** C2 (level statistic) fires on 10/10 stocks — non-selective, replicating the paper's threshold-straddling critique at panel scale. C3 (bracket certificate) fires on 5/10: **zero false alarms on the three controls**, at-or-before the labeled episode on 2J3KL (one-year lead), 4TVn (exact), and 4VsW (exact); early (13–17 years) on FAPL and IS, whose mid-70s drawdown episodes preceded their labeled 1990s collapses; and **misses** on GB and KAT, whose declines were catch-heavy (brackets straddle — the certificate is conservative by construction). C4 adds the 2J3KL collapse year and 4TVn's 2003 second episode.

**Reading.** The harvest-free contraction certificate is selective in exactly the paper's sense: it fires only where the certified rows can attribute the decline to the non-fishing account, never on the controls, and its misses are the catch-heavy declines it should (by construction) not certify. The 2J3KL one-year lead and 4TVn exact firing are the battery's genuine early-warning demonstrations.

## Limits

Single-vintage SSB (RAM's per-stock latest assessments); TC is RAM's total-catch compilation (its 2J3KL 1994 row, 2,720 t, differs from the locked reconstruction's 1,314 t — a third source, not used in the paper's certificates); no ROC/AUC over a larger panel (roadmap: full U17 protocol with the panel extract as the seed); labels fixed by literature verdicts, stated above. Third-vintage note: RAM reads 2J3KL 1990–1993 as 765, 747, 354, 83 kt — between the input and reassessment vintages, same breach sign pattern.

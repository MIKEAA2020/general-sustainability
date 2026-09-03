# Anchoveta–ENSO analysis v2 — battery on the owner-supplied Sea Around Us series (2026-09-03)

**Supersedes the v1 memo's data section.** The v1 battery ran on RAM Legacy
assessment series because the paper's own 1950–2019 series was not fetchable.
The owner then supplied the actual series — Peru (`shortened.txt`: Sea Around
Us entity 604, taxon 87, Q_tlw, 1950–2024) and Chile (`SAU Taxa 600004
v50-1.csv`: Engraulis ringens, all sectors and reporting statuses,
1950–2019) — and the full battery was re-run on them. The v1 memo remains as
the RAM-series record; **the numbers below are the ones that count**, because
they are computed on the series the paper's figure is built from.

## Data

- Peru: SAU annual tonnes, 1950–2024 (battery window 1950–2019, n = 70;
  extension 1950–2024 used for one spectral check).
- Chile: SAU annual tonnes, 1950–2019, n = 70 (sum over industrial/artisanal
  and reported/unreported).
- Indices: NOAA PSL ERSSTv5 NINO1/NINO3/NINO3.4/NINO4, PSL SOI, annual means.

## Results (all on 1950–2019 unless stated)

1. **Periodicity.** Peru log-catch top Lomb–Scargle peaks: 7.96 yr (power
   0.029) and **3.70 yr (0.027)** — the paper's 3.7-yr peak reproduces as a
   co-dominant peak in a flat, multi-peaked spectrum ("present" is exact;
   "robust" is generous). On 1960–2019 the 3.63-yr peak (0.049) sits just
   below 6.17 yr (0.052). Chile: 3.68 yr present among several peaks.
2. **Association (SOI).** Peru–SOI: r = +0.513 (lag 0, p < 0.0001),
   +0.419 (lag 1, p = 0.0003), +0.396 (lag 2, p = 0.0008). Chile–SOI:
   +0.417 (lag 4), +0.396 (lag 0), +0.390 (lag 2, p = 0.001). The paper's
   |r| ≈ 0.31 sits inside this bracket. Sign is the mechanistic one
   (positive SOI = La Niña → high catch). NINO1/3/3.4/4 carry nothing beyond
   SOI.
3. **Multiplicity.** Ten of the ninety tested index–lag cells (2 stocks × 5
   indices × 9 lags) survive Benjamini–Hochberg at 0.05 — **all ten are SOI
   cells** at lags 0…+4 across both stocks. The SOI association is
   multiplicity-robust.
4. **Direction.** Bivariate Granger: Peru ENSO→catch p = 0.00009 (lag 2;
   lags 1/3: 0.011/0.003), reverse p ≥ 0.21. Chile ENSO→catch p = 0.00016
   (lag 2), reverse p ≥ 0.19. One-sided in both stocks.
5. **CCM.** Directionally inconclusive even at n = 70 (cross-map skills
   ≤ 0.24, no convergence trend). No nonlinear-causality claim is made;
   the linear-directional Granger result is the evidence.
6. **Era-dependence (headline).** Split-half (cut 1985) on SOI lag +1:
   Peru 1950–1984 r = +0.424 (p = 0.013) vs 1985–2019 r = +0.129 (n.s.);
   lag +2 reverses sign post-1985 (−0.344, p = 0.050). Chile: +0.384
   (p = 0.025) vs +0.136 (n.s.), lag +2 −0.365 (p = 0.037). The coupling is
   confined to 1950–1984.
7. **Sensitivity (artefact checks).** Early-period strength is not
   crash-year-driven (Peru excluding 1972/73, 1983/84, 1998: r = +0.462,
   p = 0.010) and not reconstruction-driven (Chile reported-only lag +1:
   r = +0.387, p = 0.024 early; +0.156 n.s. late).

## Reading

The paper's own sentence is confirmed and upgraded on its own data: the
3.7-yr periodicity and the ≈ 0.31 association reproduce (SOI-resolved), the
association is multiplicity-robust for SOI, and its direction is one-sided
(ENSO→catch) in both stocks. Two honesty limits remain: CCM gives no
nonlinear-causality claim, and — the new finding — the coupling is
**era-bounded** (1950–1984), absent after 1985, with the attenuation robust
to both artefact checks. The post-1985 attenuation is registered as the
focal strengthening test (§3.6) rather than claimed as a regime effect.

## Disposition of the six suggestions (updated)

1. Mechanistic pathway model — registered (unchanged).
2. Causal methods — Granger executed, one-sided in both stocks; CCM executed
   on the full series and recorded inconclusive; IV declined (unchanged).
3. Pre-registered out-of-sample validation — the index–lag specification
   (SOI, lags 0–2, both stocks) is now fixed by the executed battery;
   the era split is the registered focal test.
4. Multiple testing — executed; the SOI association survives BH-FDR
   (10/90 cells, all SOI).
5. Replication — executed on the owner's Chilean series: full replication
   (same index, same sign, same lag structure, same era split), stronger
   than the RAM-series version.
6. Paleo/experimental — cited as mechanistic-scale support (unchanged).

## Files

`analysis/anchoveta_enso/`: `battery_v2.py`, `battery_v2_results.json`,
`supplementary_results.json`, `peru_sau_annual.csv`, `chile_sau_annual.csv`
(plus the v1 RAM-series artifacts). Paper changes: **P5 v13** (§3.7 sentence
rewritten on the SAU battery; §3.6 registered tests updated) and
**paper5_supplementary_v4.md** (S4 record rewritten).

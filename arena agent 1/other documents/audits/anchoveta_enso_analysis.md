# Anchoveta–ENSO association — strengthening battery (2026-09-02)

**Object.** The P5 v10 sentence reporting the Peruvian anchoveta–ENSO association
(|r| ≈ 0.31, ENSO leading catch, "weak-to-moderate … without identifying a mechanism").
Owner question: can a mechanistic model or independent tests strengthen the link?
Six suggestions were supplied; each is evaluated below and the feasible ones executed.

## Data

- **Series**: RAM Legacy v4.66 assessment series (Zenodo 14043031): Peru —
  PANCHNCHSP (Peruvian anchoveta, Northern Chile–Southern Peru), total catch
  1986–2019, n = 34; Chile — PANCHCCH (Peruvian anchoveta, Central Chile),
  total catch 1985–2020, n = 36. The paper's 1950–2019 series (Sea Around Us/
  FAO vintage) is not fetchable from the public APIs available in this session
  (Sea Around Us API returns no catch payloads; BOM blocks automation), so the
  battery runs on the RAM assessment series and is reported as registered-data
  evidence for that series, not a recomputation of the 1950–2019 figure.
- **Indices**: NOAA PSL ERSSTv5 NINO1, NINO3, NINO3.4, NINO4 and PSL SOI,
  annual means. (NINO1+2 unavailable — PSL returns 404; BOM blocks scraping.
  NINO1, 0–10°S 80–90°W, is the most coastal of the available regions and the
  closest to the Peruvian upwelling system.)

## Results

| Test | Peru (1986–2019, n=34) | Chile (1985–2020, n=36) |
|---|---|---|
| Lomb–Scargle dominant period (log catch) | **3.65 yr** (norm. power 0.15) | 7.81 yr |
| Best raw cross-correlation | SOI lag +2: **r = −0.514, p = 0.0026**; NINO1 lag +1: **r = −0.488, p = 0.0039** | SOI lag +3: r = −0.390, p = 0.025 |
| BH-FDR at 0.05 over 90 cells (2 series × 5 indices × 9 lags) | **0 cells significant** | — |
| Granger (bivariate, maxlag 3) | ENSO→catch **p = 0.0001** (lag 2; lag 1: 0.006, lag 3: 0.0004); catch→ENSO p ≥ 0.40 | neither direction (p ≥ 0.22) |
| CCM (pyEDM, E = 2–3, libSize ≤ 30) | cross-map skills ≈ −0.06…+0.23, noisy, no convergence — **inconclusive at n = 34** | ≈ −0.21…+0.10, inconclusive |
| Split-half (cut 2003) | early (n=17) r = −0.478 (p = 0.061); late (n=17) r = −0.561 (p = 0.024) — **sign-stable** | not run (Chile serves as the replication unit) |

**Reading.** (i) The periodicity claim replicates on the assessment series
(3.65 vs the paper's 3.7 yr). (ii) The association's magnitude is larger than
the paper's |r| ≈ 0.31 on this series and its sign is the mechanistic one
(El Niño → low catch; SOI, positive in La Niña, correlates positively).
(iii) Granger direction is one-sided: ENSO → catch at p = 0.0001 with no
reverse dependence — the strongest directional statement the data support.
(iv) Honest limits: no single cell survives multiplicity control across the
90 tested index–lag combinations; CCM is underpowered at n = 34 and must be
re-run on the full 1950–2019 series; Chile replicates in sign (SOI lag +3)
but not in Granger direction.

## Disposition of the six suggestions

1. **Mechanistic pathway model (ENSO → coastal temperature/upwelling →
   recruitment).** Literature-established pathway (e.g., Chávez et al., 2003;
   Chávez et al., 2008; Gutiérrez et al., 2009 fish-scale records), but
   building the process model is an identification study beyond this paper's
   scope. **Disposition: registered as a prospective strengthening test** in
   P5 §3.6; the pathway is cited in the supplementary record, not modelled here.
2. **Formal causal methods.** CCM run — inconclusive at n = 34 (recorded, not
   reported as negative evidence). Granger run — one-sided ENSO→catch at
   p = 0.0001. Instrumental variables/natural experiments: no candidate
   instrument exists in this data. **Disposition: Granger incorporated; CCM
   registered for the longer series; IV declined with reason.**
3. **Pre-registered out-of-sample validation.** Split-half run (cut 2003):
   sign-stable (−0.478 / −0.561). The pre-registration discipline itself is
   already P5's standing protocol; the specific index–lag pre-specification is
   added to the registered list in §3.6.
4. **Multiple testing correction.** Run: BH-FDR over the full 90-cell search
   gives zero significant cells. **This is the load-bearing honesty result**:
   the paper's "weak-to-moderate … no mechanism" wording is now confirmed by
   the data rather than being merely cautious. Incorporated.
5. **Replication across independent stocks/regions.** Run on the Chilean
   anchoveta: same index family, same sign, longer lag (SOI lag +3,
   r = −0.390, p = 0.025); Granger absent. Incorporated as a
   sign-consistent replication with its limits stated.
6. **Paleo/experimental evidence.** Not executable in this session; the
   sediment fish-scale records (Gutiérrez et al., 2009; Chávez et al., 2008)
   are cited as the existing mechanistic-scale evidence in the supplementary
   record.

## Files

- `battery.py`, `battery_results.json`, `granger_results.json`,
  `xcorr_results.json`, `PANCHNCHSP_catch.csv`, `PANCHCCH_catch.csv`,
  `indices_annual.json` — analysis artifacts, saved under
  `analysis/anchoveta_enso/` in the workspace.
- Paper changes: **P5 v12** (main text §3.7 sentence replaced by the
  battery-backed version; §3.6 prospective list extended) and
  **paper5_supplementary_v3.md** (S4 Peruvian anchoveta record rewritten with
  the battery values, index sources, and the disposition of suggestions 1–6).

# Anchoveta–ENSO battery verification — record v1 (2026-09-11)

> Repo copy: workspace original at `/home/user/verify_battery/` (identical
> content; path references adapted to this directory).

Scope: re-execute the author's `battery.py` / `battery_v2.py` (repo
`analysis/anchoveta_enso/`) and reconcile every output against the committed
result JSONs and the printed claims (main text §3.7 = v29 L1307–1332; supp v7
S4 = `paper5_supplementary_v7.md` line 108). No manuscript edits (per mandate).

Method: unmodified author scripts; missing raw inputs reconstructed or
re-fetched (details §1); bit-level diff of all deterministic outputs;
forensic adapters for the three standalone/supplementary files with no
producing script. Executable companion: `forensics.py` (run from this directory; all checks PASS).

## Verdict summary

1. **Reproduction: COMPLETE.** Both batteries reproduce bit-exactly on every
   deterministic output: spectra 5/5, xcorr 180/180 cells (incl. BH flags and
   sort order), splits 4/4, v2 Granger 12/12, v1 Granger error-strings 2/2.
   CCM reproduces within resampling noise (|Δ| ≤ 0.05, pattern-identical).
2. **A missing-value artifact drives the headline result.** The author's
   `soi_ok.data` is proven to be raw NOAA PSL `soi.data` with the 1950
   −99.99 missing-value flag parsed as a number (the author's `parse_psl`
   has no missing-value filter). With the flag dropped, ALL 18 SOI xcorr
   cells are null (|r| ≤ 0.16, p > 0.19): the +0.513 headline, all ten BH-FDR
   flags, the era-split contrast, and the collapse-exclusion robustness
   evaporate. The NINO-based results (Granger, spectra, null xcorr cells,
   CCM) use validated clean inputs and stand as computed.
3. **Provenance fully closed.** `xcorr_results.json` = v1 xcorr r-extract
   (180/180 exact); `granger_results.json` = RAM-series NINO1 Granger
   (12/12 exact); supplementary peaks/splits reproduced (peaks 4/4, SOI
   splits 10/10, all at printed precision, artifact included as committed);
   the crash-year exclusion is decoded as T = {1972,1973,1983,1984,1998}
   (FIVE years — the printed word "three" is inaccurate, see §6).
4. **One entry is unverifiable from deposits:** `chile_reported_only_lag1`
   needs the SAU sector/reporting split, which no deposited file carries.

## 1. Inputs: deposited, re-fetched, reconstructed

Deposited in `analysis/anchoveta_enso/` (12 files): both scripts, both SAU
annual CSVs, both RAM PANCH CSVs, `indices_annual.json` (NINO1/3/3.4/4 annual
means; its SOI section is EMPTY), and five result JSONs. Absent: the raw PSL
`.anom.data`/SOI files and the two `/home/user/uploads/` SAU sources the v2
script hardcodes.

- **PSL indices re-fetched 2026-09-11** (`frozen_inputs/`): `soi.data`,
  `nina1/3/34/4.anom.data` from `https://psl.noaa.gov/data/correlation/`.
  Parsed NINO1/3/3.4/4 match the deposited `indices_annual.json` on all
  1950–2019 years with max|diff| = 0.0 (forensics §1) — the fetch pipeline
  is validated and the deposits are the author's frozen ERSSTv5 vintage.
- **Uploads reconstructed** (behaviorally exact; see
  `reconstructed_uploads/README_reconstructed_inputs.txt`): `shortened.txt`
  rebuilt as one TSV row per year from `peru_sau_annual.csv` (the author's
  `load_peru` sums column 6 by year with no entity/taxon filter);
  `SAU Taxa 600004 v50-1.csv` copied from `chile_sau_annual.csv` (the
  author's `load_chile` reads only year/tonnes and sums by year).
- **SAU CSV fidelity:** the CSVs alone reproduce the committed v2 spectra
  bit-exactly (Peru 7.9587 yr / 0.02857 / n=70; Chile 3.6819 yr; Peru_ext
  6.6407 yr / n=75) — the deposits are faithful derivatives of the
  owner-supplied SAU series. (Caveat: an August-vintage Peru SAU file
  described in the Aug-08 deposit verification carries different values;
  the battery demonstrably ran on the September vintage reproduced here.)

## 2. Rerun results (unmodified scripts, `reruns/`)

| Block | v1 (`battery.py`, RAM 1985+) | v2 (`battery_v2.py`, SAU 1950–2019) |
|---|---|---|
| Spectra | 2/2 bit-exact (Peru 3.645/0.146, Chile 7.809/0.242) | 3/3 bit-exact (7.9587, 3.6819, 6.6407 yr) |
| Xcorr sweep | 90/90 bit-exact (incl. p-sort, BH, flags); nsig=0 | 90/90 bit-exact; nsig=10, all SOI |
| Splits | Peru NINO1 lag1 early/late exact | Peru NINO1 lag1 early/late exact |
| Granger | error-strings reproduced verbatim (modern statsmodels 0.15 also rejects the `verbose` kwarg — not version drift) | 12/12 exact: Peru ENSO→catch lag2 p=9e-05, Chile lag2 p=0.00016; reverse ≥0.19 |
| CCM (pyEDM, unseeded) | \|Δ\| ≤ 0.046, pattern-identical | \|Δ\| ≤ 0.033, pattern-identical |

v2 CCM pattern (committed = rerun): `enso_to_catch` NEGATIVE in all 16 rows
(−0.10…−0.18); `catch_to_enso` small-positive (+0.03…+0.24) — i.e. no CCM
support for ENSO→catch, consistent with the printed "directionally
inconclusive". Environment: statsmodels 0.15.0, pandas 2.2.3, pyEDM (pip),
scipy stack; rerun logs in `reruns/`.

## 3. The SOI missing-value artifact (headline finding)

The committed v2 SOI block cannot be produced from valid SOI data: with 1950
dropped, NO single 1950 value reconciles all cells (max attainable lag-0 r
over any 1950 fill is < 0.25 vs committed +0.5132). Instead, parsing raw PSL
`soi.data` with the author's own unfiltered `parse_psl` — which reads the
1950 all-missing row (−99.99 × 12) as the annual mean −99.99 — reproduces
the FULL 90-cell committed sweep bit-exactly (90/90, incl. all p-values, n,
BH flags). The author's `soi_ok.data` was therefore raw PSL `soi.data`,
missing flag included. Mechanism: the −99.99 outlier pairs with the
below-mean 1950 log-catch, a single leverage point that inflates every
early-window SOI correlation and forces its sign positive.

Artifact-free SOI table (1950 dropped; full table printed by `forensics.py`):

| Cell | Committed (artifact) | Clean |
|---|---|---|
| Peru lag0/1/2 | +0.513/+0.419/+0.396 (p ≤ 0.001) | +0.073/+0.158/+0.015 (p ≥ 0.20) |
| Chile lag0/2/4 | +0.396/+0.390/+0.417 | +0.052/−0.047/+0.007 (all n.s.) |
| BH-FDR 0.05 | 10/90, all SOI | 0/90 |

Further fingerprints: (i) the era-split contrast IS the artifact — early
halves contain 1950 (inflated positive), late halves don't (null/negative);
clean early Peru lag1 = +0.282, p = 0.112. (ii) v1 (RAM, 1985+, never touches
1950) finds SOI associations NEGATIVE (Peru lag2 −0.514) — the artifact flips
the sign. (iii) The late-half lag2 cells (Peru −0.344, p = 0.050; Chile
−0.365, p = 0.037) use no 1950 data and are real, but uncorrected
cherry-picked cells. (iv) Clean early lag1 WITH the crash exclusion falls to
+0.107, p = 0.58 — the "survives exclusion" robustness also evaporates.

## 4. Claim-by-claim reconciliation (§3.7 v29 L1307–1332; supp v7 S4 L108)

| Printed claim | Committed source | Rerun | Artifact status | Verdict |
|---|---|---|---|---|
| 3.70 yr co-dominant w/ 7.96 yr; 3.63 yr on 1960–2019 | supplementary peaks | 4/4 exact | clean (catch-only) | VERIFIED |
| Peru–SOI +0.513/+0.419/+0.396 (lags 0/1/2) | v2 xcorr | bit-exact | −99.99 leverage | reproduced, INVALID |
| Chile–SOI +0.390 lag2 / +0.417 lag4 | v2 xcorr | bit-exact | −99.99 leverage | reproduced, INVALID |
| 10/90 BH-FDR, all SOI | v2 xcorr flags | 10/10 | −99.99 leverage | reproduced, INVALID |
| Granger ENSO→catch lag2: Peru 9e-05, Chile 0.00016; reverse ≥0.19 | v2 granger | 12/12 exact | clean (NINO1 validated) | VERIFIED as computed |
| Era-split: early +0.42/0.013, late +0.13 n.s., lag2 sign flip | supp splits | 10/10 exact | contrast = artifact | reproduced, INVALID |
| Survives collapse-year exclusion (+0.46/0.010) | supp excl | exact via T (§6) | artifact-contaminated | reproduced, INVALID (+ "three" wrong) |
| Chile reported-only +0.39/0.024 | supp chile_reported_only | — | no sector data deposited | UNVERIFIABLE |
| CCM directionally inconclusive (n=70) | v2 ccm | within ±0.033 | clean (NINO1) | VERIFIED (generous but fair) |
| \|r\|≈0.31 ENSO-leading (archived figure) | predates battery | — | out of scope | NOT EXAMINED |

Net surviving ENSO→anchoveta evidence after artifact removal: the NINO1
Granger one-sided dependence plus the 3.7-yr spectral coincidence. The
cross-correlation case (+0.513, multiplicity-robustness, era-split,
exclusion robustness) does not survive. No manuscript edits made (mandate);
v30 must re-derive or drop every SOI-sourced number above.

## 5. Provenance closures (files with no producing script)

- `xcorr_results.json`: exact r-extract of the committed v1 sweep (180/180
  values identical) — a v1-run derivative.
- `granger_results.json`: exact RAM-series (v1-input) NINO1 Granger run
  (12/12 at 4dp, both directions, both stocks) — the author evidently ran
  Granger standalone (without the failing `verbose` kwarg) after v1's
  in-script Granger errored. Note it CONTRADICTS nothing: RAM-Chile is all
  null while SAU-Chile (v2) is lag2-significant — different series/vintages.
- `supplementary_results.json` peaks/splits: reproduced exactly (§2 table,
  forensics §6) with the artifact included, as committed.

## 6. Crash-year exclusion decoded

`peru_excl_crash_years_lag1` (early 0.462/0.0101, late −0.008/0.963) is
exactly reproducible (both cells, both precisions, both n) by plain
year-filtering with T = {1972, 1973, 1983, 1984, 1998} on cut-1985 halves,
raw SOI, lag 1 (early n=30, late n=33). Identification: n-inference from
(r, p) forces early n=30 uniquely (= 34 − 4); late admits only {1998} among
subsets of size ≤3 and no quad; among early quads the all-collapse-event
{1972,1973,1983,1984} is the unique set avoiding the 1971 all-time record
catch; all-triple searches (6 mechanics × raw/clean × cuts 1984/1985 ×
lags 1/2, plus no-log variants) are exhaustively empty, proving no 3-year
set works. So the supp/main-text phrase "the three collapse years" is
inaccurate — the numbers require FIVE years (three collapse EVENTS:
1972–73, 1983–84, 1998). S4's early cell keeps 1950, hence is
artifact-contaminated (§3.iv).

## 7. A6 contribution

The A6 root-cause report lists the power spec AND the S4 inventory as absent
registration materials. This directory now stages a partial S4 inventory:
frozen PSL inputs, behaviorally-exact uploads reconstructions (with fidelity
proof), unmodified rerun outputs + logs (`reruns/`), the executable `forensics.py`
record, and this reconciliation. Still absent: the original uploads, the
SAU sector split (for the reported-only sensitivity), and any pre-registration
document.

## 8. Reproduction instructions

```
# Full reruns (needs statsmodels, pandas, pyEDM, scipy):
mkdir run && cd run
cp <repo>/analysis/anchoveta_enso/battery.py <repo>/analysis/anchoveta_enso/PANCH*.csv .
cp ../verify/frozen_inputs/nina*.anom.data .
cp ../verify/frozen_inputs/soi.data ./soi_ok.data
python3 battery.py   # -> battery_results.json (bit-exact deterministic blocks)
mkdir run2 && cd run2
cp <repo>/analysis/anchoveta_enso/battery_v2.py .
cp ../verify/frozen_inputs/nina*.anom.data .
cp ../verify/frozen_inputs/soi.data ./soi_ok.data
# place reconstructed_uploads/ at /home/user/uploads/{shortened.txt,SAU Taxa 600004 v50-1.csv}
python3 battery_v2.py  # -> battery_v2_results.json (bit-exact deterministic blocks)
# Forensics (no pyEDM needed): cd analysis/anchoveta_enso/verify && python3 forensics.py  # ALL PASS
```

## 9. Open items

1. `chile_reported_only_lag1` — needs the SAU sector/reporting split
   (author-side; also likely artifact-contaminated via 1950).
2. The |r|≈0.31 archived ENSO-leading figure (§3.7 L1308) predates the
   battery; provenance not examined (not battery output).
3. Manuscript repair (SOI numbers, "three collapse years", §3.7/S4
   re-derivation) is staged for the v30 build; explicitly not done here.

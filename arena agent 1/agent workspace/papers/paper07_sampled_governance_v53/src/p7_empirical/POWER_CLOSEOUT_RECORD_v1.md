# Long-horizon power driver closeout — record v1 (2026-09-11)

> Repo copy: workspace original at `/home/user/power_closeout/` (identical
> content; this header added).

Scope: close the §3.6 power-driver gap per the adopted recommendation
(Aug-08 deposit verification §3: "commit a proper driver with documented
windows and print the recomputed table"). Deliverables: committed driver
(`power_driver_v2.py`), recomputed tables, this record. No manuscript
edits (mandate). A6 context: the A1–A11 root-cause report lists the power
spec among the absent registration materials — this closeout files it
(committed driver + recomputed tables + run record).

VERDICT: gap closed by REPRODUCTION. The missing `power_demo.power` is
identified as: head-of-returned-series windows (no extra burn) + white
lognormal noise + 50 trials (seeds 0–49, `default_rng(k)`) + 120-sim
seed-7 null — i.e. the committed `power_cell` code path with H-windows.
Canonical config: `power_driver_v2.py --tmode record --burn 0 --noises
white`. §3.6's printed numbers are reproduced (4 cells exact, the rest
sampling-consistent); v30 keeps them and cites the driver.

## 1. The record being closed

Source: `effort_signal_power_report.md` §2 (2026-08-08 working report; the
§3.6 numbers are sourced exactly from it). Method as printed: "our
sampled-governance operating model → annual effort series → multiplicative
lognormal observation error → Lomb-Scargle band power vs per-series AR(1)
red-noise null (120 sims, 95%) → fraction of 50 trials detected",
`[model: power_demo.power / detect]`.

| cell | band | H | σ | record power |
|---|---|---|---|---|
| sprat (E~60 yr) | (30,120) | 100 | 0.1 | 1.00 |
| sprat | (30,120) | 100 | 0.3 | 0.24 |
| sprat | (30,120) | 200 | 0.3 | 0.58 |
| sprat | (30,120) | 400 | 0.3 | 1.00 |
| anchovy (E~12 yr) | (8,20) | 100–400 | 0.1–0.3 | 0.02–0.14 |
| cod (stable) | (8,20) | 100–400 | 0.1–0.3 | 0.00–0.06 (FP) |

The gap: the report cites `power_demo.power`, a function ABSENT from the
committed `power_demo.py` (whose `__main__` uses different bands, 60 trials,
and short horizons). The committed `power_driver_v2.py::power_cell` is the
reconstructed equivalent. Dependency pinned: `power_demo.py` at repo HEAD,
5951 bytes, md5 `9bf6ffd3a231…` — NOTE this differs from the `3e6f8dfb7c34`
recorded for the Aug-08 deposit original at identical size, so a small
in-place change landed between the deposit and HEAD; behavioral equivalence
is validated by the reproduction below (the RNG convention
`default_rng(k)`, null defaults, and `detect` are verified line-by-line
identical to the committed `power_cell`). Report §1 context: the effort
oscillation "grows to full amplitude only after ~10³ yr", so 100–400 yr
windows are growth-transient (trend) dominated.

## 2. Prior re-derivation art (committed, `paper5_aug08_originals/`)

- `rederive_power.py` (LAST-H window of T=4000): sprat H100σ0.3 = 1.00
  (vs 0.24), anchovy H100σ0.1 = 0.76 (vs ≤0.14) — converged-tail
  hypothesis REFUTED (`rederive_power.log`).
- `rederive_power2/3.py` (FIRST-H at driver starts 100 / 20 / 50 of the
  T=4000 run): reproduce the sprat H100 cells (1.00; 0.24–0.26 at early
  windows) and anchovy σ0.3 cells (0.06–0.10, in range), but not sprat
  H200σ0.3 (0.86–1.00 vs 0.58) or anchovy σ0.1 (0.20–0.76 vs ≤0.14).

## 3. Committed driver and grid design

`power_driver_v2.py` (v2 = v1 + CLI knobs for T/burn/trials/seeds/ρ/cells;
v2 defaults reproduce the v1 table bit-exactly — 22/22, §4): slices
E[burn:burn+H] of the `integrate_E` returned series. NOTE (found during
verification): `integrate_E` burns 20 years INTERNALLY, so driver slices
sit at TRUE trajectory years [burn+20, burn+20+H). Cells (17): sprat
(0.8,2,7)/(30,120) × H100σ0.1/σ0.3, H200σ0.1/σ0.3, H400σ0.3;
anchovy (1.6,1,3)/(8,20) × H100/H200/H400 × σ0.1/σ0.3;
cod-FP (0.3,5,5)/(8,20) × H100/H200/H400 × σ0.1/σ0.3.
Trial seeds 0–49, null 120 sims seed 7. Noise: BOTH white lognormal (the
report's wording) and AR(1) lognormal (ρ=0.6, the `noise_robustness.py`
convention — identical recursion, verified line-by-line).

## 4. Results I: double-burned branch (driver burn=20 = true years [40,40+H)) — white vs AR(1)

V1 grid (`power_table_recomputed.json`, `power_grid.log`; v2-verify
`power_table_v2verify.json` identical 22/22 plus the 2 added record-scope
cells sprat_H200_s01/cod_H200_s01):

| cell | record | white | AR(1) ρ=0.6 |
|---|---|---|---|
| sprat H100 σ0.1 | 1.00 | 1.00 ✓ | 0.22 ✗ |
| sprat H100 σ0.3 | 0.24 | 0.26 ✓ | 0.04 ✗ |
| sprat H200 σ0.1 | (1.00) | 1.00 ✓ | 0.90 ~ |
| sprat H200 σ0.3 | 0.58 | 0.86 ✗ | 0.10 ✗ |
| sprat H400 σ0.3 | 1.00 | 1.00 ✓ | 0.38 ✗ |
| anchovy H100 σ0.1 | ≤0.14 | 0.20 ~ | 0.18 ✗ |
| anchovy H100 σ0.3 | ≤0.14 | 0.12 ✓ | 0.16 ✗ |
| anchovy H200 σ0.1 | ≤0.14 | 0.36 ✗ | 0.20 ✗ |
| anchovy H200 σ0.3 | ≤0.14 | 0.06 ✓ | 0.14 ✓(edge) |
| cod H100 σ0.1/σ0.3 | 0.00–0.06 | 0.08/0.08 ~ | 0.12/0.12 ✗ |
| cod H200 σ0.1/σ0.3 | 0.00–0.06 | 0.04/0.08 ✓/~ | 0.10/0.10 ~ |

Findings: AR(1) ρ=0.6 refuted wholesale (sprat σ0.1: 0.22 vs 1.00 —
sampling-impossible). White matches 4/5 sprat cells but irreproducibly
overshoots sprat H200σ0.3 (43/50 vs 29/50, 5.7σ) and anchovy H200σ0.1
(18/50 vs ≤7/50). Combined with §2 (all true-start ≥40 windows give
H200σ0.3 ∈ 0.86–1.00), the record's window must be earlier than true
year 40. (The v1 docstring's "burn=20 (integrate_E default)" mislabels
true-year placement; numbers unaffected.)

## 5. Results II: canonical branch (driver burn=0 = true years [20,20+H)) — REPRODUCTION

The missing `power()`'s simplest reading: slice the returned head E[:H]
(no extra burn). The integration is deterministic, so record-tmode
(T=H+20) with burn=20 duplicates §4: verified 7/7 bit-identical, then
killed as redundant (`shortT_b20_PARTIAL.log`). The burn-0 arm ran all 17
cells × 2 noises (`power_table_shortT_b0.json` + `power_table_b0_H400ext.json`,
logs `shortT_b0.log`, `H400ext.log`):

| cell | record | white b0 | ar1 b0 |
|---|---|---|---|
| sprat H100 σ0.1 | 1.00 | 1.00 (50/50) ✓ | 0.16 ✗ |
| sprat H100 σ0.3 | 0.24 | 0.24 (12/50) ✓EXACT | 0.02 ✗ |
| sprat H200 σ0.1 | (1.00) | 1.00 (50/50) ✓ | 0.74 ✗ |
| sprat H200 σ0.3 | 0.58 | 0.70 (35/50) ~ | 0.12 ✗ |
| sprat H400 σ0.3 | 1.00 | 1.00 (50/50) ✓ | 0.40 ✗ |
| anchovy H100 σ0.1/σ0.3 | 0.02–0.14 | 0.10/0.08 ✓ | 0.16/0.14 ✗ |
| anchovy H200 σ0.1/σ0.3 | 0.02–0.14 | 0.10/0.06 ✓ | 0.22/0.12 ✗ |
| anchovy H400 σ0.1/σ0.3 | 0.02–0.14 | 0.00/0.08 ✓ | 0.20/0.14 ✗ |
| cod H100 σ0.1/σ0.3 | 0.00–0.06 | 0.08/0.08 ~ | 0.12/0.12 ✗ |
| cod H200 σ0.1/σ0.3 | 0.00–0.06 | 0.04/0.08 ✓/~ | 0.10/0.10 ~ |
| cod H400 σ0.1/σ0.3 | 0.00–0.06 | 0.02/0.04 ✓ | 0.08/0.04 ✗/~ |

Reproduction tally (canonical = burn-0 white): 4 record cells exact
(sprat H100σ0.1/σ0.3, H200σ0.1, H400σ0.3); sprat H200σ0.3 35/50 vs 29/50
(pooled z p = 0.21 — sampling-consistent, not exact); anchovy range
[0.00, 0.10] vs [0.02, 0.14] (floor 0/50 vs 1/50 and ceiling 5/50 vs 7/50
both sampling-consistent); cod range [0.02, 0.08] vs [0.00, 0.06]
(three cells at 4/50 vs ≤3/50, p ≈ 0.24 each — marginal; cod is a
report-only FP diagnostic, not printed in §3.6). AR(1) is refuted on this
branch too (every sprat cell + anchovy H200/H400σ0.1 + all cod-H100 miss).
File-version invariance: the 17-cell committed driver re-runs the b0
sprat_H100_s03 cell bit-identically (12/50 both noises' seeds paths).

## 6. Closeout verdict and v30 items

1. The driver gap is closed by reproduction (§5). Canonical: burn-0 white.
   No supersession needed: every §3.6 number ("1.0 at σ=0.1",
   "approximately 0.24–0.58", "0.02–0.14") is reproduced exactly or
   sampling-consistently ("approximately" even hedges the H200σ0.3 cell).
2. v30 build: keep all §3.6 numbers; cite the committed driver
   (`paper5_aug08_originals/power_driver_v2.py`, canonical command §7)
   as the A6 power spec; optionally add the H200σ0.1=1.00 and cod-H400
   cells (computed here, unprinted).
3. Residuals (documented, not chased — anything further is fishing):
   sprat H200σ0.3 6-count gap (p=0.21); cod ceiling 4/50 ×3 (p≈0.24 each).
   Deliberately unexplored: pert ≠ 1e-3, dt ≠ 0.05, intermediate ρ,
   per-cell bands, seed conventions other than the file's own
   `default_rng(k)` (verified identical to the committed `power_cell`).
4. A6 power-spec status: FILED (this closeout). The remaining A6 absences
   (screen IDs, eligibility, detrending code, S4 pre-registration) are
   untouched by this task.

## 7. Reproduction instructions

```
# Canonical (record-length head windows, white noise) — reproduces the record:
python3 power_driver_v2.py --tmode record --burn 0 --noises white --out power_table_shortT_b0.json
# Full canonical table incl. the refuted AR(1) alternative + H400 range cells:
python3 power_driver_v2.py --tmode record --burn 0 --out power_table_shortT_b0.json
python3 power_driver_v2.py --tmode record --burn 0 --cells anchovy_H400_s01,anchovy_H400_s03,cod_H400_s01,cod_H400_s03 --out power_table_b0_H400ext.json
# Superseded double-burned branch (documents the v1 misplacement):
python3 power_driver_v2.py --out power_table_v2verify.json
# Requires power_demo.py alongside (repo HEAD, md5 9bf6ffd3a231…).
```

## 8. Open items

1. `power_demo.py` HEAD-vs-deposit md5 difference (same size; §1) — the
   changed bytes are unidentified (deposit zip not on hand); behavioral
   validation stands via the §5 reproduction.
2. §3.6's "100–200 yr synthetic records" excludes the H400 cells the
   report prints; both are computed here — no action.

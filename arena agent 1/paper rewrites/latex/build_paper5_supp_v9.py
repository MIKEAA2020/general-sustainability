#!/usr/bin/env python3
"""Build paper5 supplementary v9 from v8: A5 decomposition tables + A11 battery.

Two asserted substitutions (S8 register updates) plus an end-append of S9
(S9.1 screen-sensitivity battery verdict table; S9.2 stage-scan
decomposition tables). NOT touched: S1-S7.
"""
import os

SRC = "/home/user/paper5_v30/paper5_supplementary_v8.md"
DST = "/home/user/paper5_v31/paper5_supplementary_v9.md"
PIN = "24c980cd"

S9 = """## S9. Screen-sensitivity battery and stage-scan decomposition records

### S9.1 Screen-sensitivity battery (§3.5)

The 42-stock screen's BH-adjusted zero count (84 target-band cells, 0
rejections) is tested against eleven null/pretreatment variants, each changing
one element of the published machinery (linear detrend, Lomb–Scargle nf=1500
grid, 200 replicates, seed 7, empirical p=(k+1)/201, BH-FDR at 0.05): the AR(1)
baseline; an ARMA(1,1) null (per-stock CSS-MLE: φ median 0.729, θ median 0.285);
a trend-stationary null without detrending (data-fitted trend plus AR(1)
residuals on both sides); circular block bootstrap at block lengths 5, 10, 15
(median per-stock φ̂=0.784, so the blocks span one to three times the median
decorrelation scale); Hodrick–Prescott-cycle (λ=100) and first-difference
pretreatments with same-treatment nulls; and piecewise-AR(1) regime surrogates
with median- and tercile-split breaks. Pass criterion throughout is verdict
stability of the BH-adjusted zero count.

| variant | null / pretreatment | min-p cell | BH rej |
|---|---|---|---|
| base | AR(1), linear detrend | PANCHNCHSP B, p=0.0448 | 0 |
| arma | ARMA(1,1), linear detrend | PANCHNCHSP B, p=0.0697 | 0 |
| ts | trend-stationary, no detrend | ANCHIXa B, p=0.0299 | 0 |
| bb5 | block bootstrap L=5 | PANCHNCHSP B, p=0.0547 | 0 |
| bb10 | block bootstrap L=10 | PANCHNCHSP B, p=0.1692 | 0 |
| bb15 | block bootstrap L=15 | ANCHMEDGSA7 A, p=0.2239 | 0 |
| hp | HP-cycle AR(1) | PANCHNCHSP B, p=0.0100 | 0 |
| fd | first-difference AR(1) | SPRAT22-32 A, p=0.0149 | 0 |
| reg_med | regime, median break | PANCHNCHSP B, p=0.0547 | 0 |
| reg_low | regime, tercile-1 break | PANCHNCHSP B, p=0.0498 | 0 |
| reg_up | regime, tercile-2 break | ANCHIXa B, p=0.0746 | 0 |

The zero count holds in all eleven variants (smallest nominal p 0.0100, HP
variant). Resolution bound, stated honestly: at 200 replicates the smallest
attainable empirical p is 1/201≈0.0050 while the rank-1 BH bound is
0.05/84≈0.0006, so a rejection at this resolution requires at least nine
minimal-p cells; the battery compares nulls at the fixed published resolution
rather than raising it. Code and log (`screen_battery_v31.py`,
`screen_battery_v31.log`) are deposited with this revision; the base variant
bit-replicates `verify_bh_v30.log`. **Status: nominal tier (seed-fixed,
logged); the bit-replication of the published zero count inherits that
count's re-execution-verified tier.**

### S9.2 Stage-scan decomposition tables (§3.3)

Transcribed from the recovered-campaign machine outputs
(`rerun_campaigns/stage_scan_recovered/rerun_outputs_2026_09_01/tau0_out.txt`
§A and `stage_decomp_results.md` §2, both @ PIN), with the
τ₀-stable classification by nonlinear ground truth. Two transcription notes.
First, each cell has two "raw window" numbers from separate scans
(`stage_r_window.py` vs `stage_tau0_decomposition.py`) differing beyond
rounding (e.g. g=5, η=0.914: rwin [0.00754,0.36675] vs τ₀-scan
[0.0076,0.3705]); the table below uses the τ₀-scan's, and the rwin scan is
cited for the g=0 validation and the extended g∈{15,50} cells by pointer.
Second, crossing counts are crossings, not grid points (the rwin log's
"grid points at r≥0.2" is a different statistic). Caveats transcribed with
the data: mapped at finite resolution; not collocation-classified; the g=7,10
bands deviate from the rg≈1.5–1.6 regularity.

τ₀ decomposition grid (raw r-window; institutional-only r-window with τ=0
stable; fish-r crossings raw/institutional):

| η | g (yr) | raw window | institutional-only | crossings |
|---|---|---|---|---|
| 0.914 | 0.5 | [0.0079,0.0225] | empty | 0/0 |
| 0.914 | 1 | [0.0079,1.5719] | [1.5719,1.5719] | 1/1 |
| 0.914 | 2 | [0.0079,0.8105] | [0.7865,0.7865] | 2/1 |
| 0.914 | 5 | [0.0076,0.3705] | [0.2660,0.3285] | 12/8 |
| 0.914 | 10 | [0.0072,0.7865] | [0.0873,0.7865] | 6/1 |
| 0.914 | 20 | [0.0068,0.7185] | empty | 9/0 |
| 3.0 | 0.5 | [0.0068,0.0646] | [0.0627,0.0646] | 0/0 |
| 3.0 | 1 | [0.0068,1.5719] | [0.0686,1.5719] | 1/1 |
| 3.0 | 2 | [0.0068,0.8608] | [0.0798,0.8105] | 7/5 |
| 3.0 | 5 | [0.0066,1.5719] | [1.5719,1.5719] | 29/1 |
| 3.0 | 10 | [0.0064,1.4361] | [0.3093,1.4361] | 23/9 |
| 3.0 | 20 | [0.0062,1.0628] | [0.3285,0.4574] | 32/12 |

Middle-band table (r-band at η=0.914 and η=3.0; τ-window at band centre;
nonlinear-verified period):

| g (yr) | r-band η=0.914 | r-band η=3.0 | τ-window (yr) | period |
|---|---|---|---|---|
| 1 | 1.565–1.585 | 1.54–1.61 | (1.6,3.5) | ~4 yr |
| 2 | 0.77–0.81 | 0.71–0.86 | (2.6,7.8) | ~8 yr |
| 3 | 0.50–0.55 | 0.40–0.55 | — | — |
| 5 | 0.28–0.33 | none | (9.9,20.3) | ~17 yr |

**Status: transcribed archive records; provisional like the §3.3 windows
whose detail they supply.**
""".replace("PIN", PIN)

SUBS = [
("S8-battery-tier",
"""and the power values, independently re-executed by a driver reimplementation reproducing the reported values within fixed-seed Monte Carlo noise.""",
"""and the power values, independently re-executed by a driver reimplementation reproducing the reported values within fixed-seed Monte Carlo noise; and the screen-sensitivity battery (§S9.1), eleven null/pretreatment variants holding the BH-adjusted zero count, reported at nominal tier with seed-fixed code and log."""),

("S8-battery-discharge",
"""Discharged with the deposited material: the RAM stock identifiers and eligibility table; the processed series and spectral routines; and the power-simulation code and seeds.""",
"""Discharged with the deposited material: the RAM stock identifiers and eligibility table; the processed series and spectral routines; the power-simulation code and seeds; and the sensitivity-battery code and log."""),
]

def main():
    src = open(SRC).read()
    for name, old, new in SUBS:
        n = src.count(old)
        assert n == 1, f"{name}: {n} matches (expected 1)"
        src = src.replace(old, new)
        print(f"ok {name}")
    assert src.rstrip().endswith("transferred here."), "unexpected S8 ending"
    src = src.rstrip() + "\n\n---\n\n" + S9
    assert "S9.1" in src and "S9.2" in src and "32/12" in src
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w").write(src)
    print("wrote", DST, len(src))

if __name__ == "__main__":
    main()

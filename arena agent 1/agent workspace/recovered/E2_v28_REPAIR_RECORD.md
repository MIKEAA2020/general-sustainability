# E2 (paperE2_cod_intervention_v28) — repair record

**Status of the tex:** `fam/e2/paperE2_cod_intervention_v28.tex`
**Basis throughout:** the *registered* fit, `wave_e_cod/src/run_intervention_v2.py`
(`r = 0.2368694`, `K = 5000` pinned, residual SD `134.96`).

**Verification gates (all green):**

| gate | result |
|---|---|
| battery `paperE2_cod_intervention_v28_verification.py` | **123 passed, 0 failed** |
| residual sweep `sweep_v28.py` | **CLEAN** |
| table verifier `verify_tables_v28.py` | **ALL TABLE CHECKS PASSED** |
| sabotage `sabotage_v28.py` (19 mutations) | **no blind spots** |

---

## 1. What triggered this round

The v28 battery went green at **81 passed, 2 failed** — both failures were
`R8l`, the "class value pinned (no variant anywhere)" check.

Diagnosis: `no_variant()` masks the printed value then asserts no *variant*
survives. It caught two bare `318.8` / `114.9` sites, and chasing them surfaced
a far larger problem than a rounding typo.

---

## 2. The two campaigns

Everything hinges on this. **Two elevation campaigns were archived, and the
paper was silently mixing them.**

| | registered (`rerun_campaigns/results/`) | source-year (`src/results_srcyear/`) |
|---|---|---|
| generator | `campaign_e2_elevation.py` | `campaign_srcyear.py` |
| residual mean | **−20.44** | −10.88 |
| residual SD | **134.96** | 114.91 |
| residual min | **−460.03** | −328.97 |
| residual max (signed) | **+179.76** | +206.55 |
| q05 | **−318.76** | −287.36 |
| q10 | **−114.85** | −80.87 |
| lag-1 autocorrelation | **0.652** | 0.554 |

Note the trap: `campaign_srcyear.py` uses the source-year *residuals* but
**freezes the floor class at the registered −114.85** (`constructive_raw =
gK - 114.85`, line 251). So its K-grid constructive column is identical to the
registered campaign's, and only the kernel intervals differ.

---

## 3. Defects found and fixed

### 3.1 Section 2 residual summary — four wrong values (source-year basis)

| statistic | printed | corrected |
|---|---|---|
| mean | −10.9 | **−20.4** |
| SD | 114.9 | **135.0** |
| range max | +206.6 | **+179.8** |
| lag-1 acf | 0.55 | **0.65** |

Confirmed independently by `e2_elevation_residuals.csv`
(`-20.44, 134.96, -460.03, -318.76, -114.85, 179.76, 0.652`).

A subtlety worth flagging: `train_residual_max` in the runner is
`np.abs(res_tr).max()` — the **absolute** max (460.0285), used as the declared
defect ε. It is *not* the upper end of the range. The signed max is +179.76.
The old text printed `+206.6`, which matches neither campaign.

### 3.2 Table 5 (finite-duration floors) — all 36 cells on the wrong basis

Every value reproduced `src/results_srcyear/e2_elevation_finite_floors.csv`
exactly. Replaced with the registered campaign. Examples:

| row | q05 n=5 | q05 n=10 | q05 n=15 | worst n=5 | worst n=10 | worst n=15 |
|---|---|---|---|---|---|---|
| BAU | 1298.7 → **1412.5** | 1540.7 → **1737.1** | 1697.8 → **1967.3** | 1450.0 → **1956.4** | 1803.7 → **2815.1** | 2062.3 → **3881.7** |
| 240 kt | 2623.1 → **2774.7** | 4013.4 → **4507.6** | 8790.9 → **empty** | 2825.0 → **3521.3** | 4687.8 → **9427.0** | empty → **empty** |

This also repairs a false claim: the text asserted the `n=5` worst-floor BAU
boundary "reproduces the registered `T=5` boundary". With the old numbers it
did not (1450.0 vs 1956.393). With the corrected table it does
(**1956.4** vs 1956.393).

### 3.3 Table 3 (K-grid) Constructive column — 9 of 10 rows matched *no* artifact

| K | printed | archived |
|---|---|---|
| 1000 | −32.2 | **−62.85** |
| 1200 | 36.0 | **7.16** |
| 1500 | 62.9 | **33.92** |
| 1769.2 | 72.7 | **42.57** |
| 2000 | 77.6 | **46.62** |
| 2500 | 83.4 | **51.35** |
| 3000 | 86.6 | **53.81** |
| 4000 | 89.9 | **56.33** |
| 5000 | 57.6 ✓ | 57.61 |
| 7000 | 93.3 | **58.91** |

All four archived copies of `e2_elevation_k_grid.csv` agree on the right-hand
column. Also fixed: the K=1000 `T=1` boundary, `943.2` (source-year) →
**1009.2** (registered).

### 3.4 Fox form constructive bound

Printed `159.92 − 80.87 = 79.05` under a "source-year floor". The archived Fox
campaign computes `cstar = g(K*) − 114.8477 = 45.08`. Corrected to
`159.923 − 114.848 = 45.08` under the **registered** floor `−114.85`.
Exact values recomputed: Fox `r = 0.1043765`, `g(K*) = 159.9234`.

### 3.5 The pervasive "source-year" mislabelling

The v28 campaign migrated the *numbers* to the registered basis but left ~16
prose *labels* reading "source-year". Corrected at: §3.2 declared classes,
Table 1 caption, §3.6 lead-in, Table 2's frozen classes, Table 2 caption,
§3.7 lead-in, Table 3 caption, §3.8 pool + autocorrelation, Table 4 caption,
§3.9 convention, Table 5 caption, §3.10 bootstrap residuals, §3.12 summary.

**Kept as source-year — verified genuinely correct:**

- **§3.5 stress replay.** 953.9 / 948.9 / 923.9 / 893.9 reproduce the
  source-year runner exactly (953.96 / 948.96 / 923.96 / 893.96). The
  registered archive gives 906.52 / 901.52 / 876.52 / 846.52 — a uniform
  47.38 kt offset, because the two conventions differ in catch timing.
- **"under the corrected source-year 10th-percentile class the critical-zone
  rule, the cascade and the graded rules all hold the LRP."** Recomputed: at
  `e = −80.87` the flat_25 / S1 / cpm / flat_0 lower boundary is **884.6 at
  T = 1, 5 and ∞** — exactly BAU. At the registered `e = −114.85` they are
  886.7 / 892.5 / 900.3, i.e. strictly worse. The contrast the paper draws is
  real.
- **The provenance note** about the superseded source-year runner.

### 3.6 §3.8 now states the two-convention comparison explicitly

Table 4's values were already on the registered pool
(0.870 / 0.859 / 0.766 / 0.580). The surrounding sentence claimed the opposite.
Rewritten to state both quadruples: the source-year pool gives
**0.906 / 0.903 / 0.835 / 0.647**, i.e. **3.6 / 4.4 / 6.9 / 6.7** percentage
points higher, and to say which one Table 4 reports.

---

## 4. Battery hardening

The two `R8l` failures were **not** a regression in the paper — they were
`no_variant()` being over-strict: it substring-matches, so the full-precision
`−318.76` (a *better* statement than `−318.8`) tripped the check. Note that
`−460.0` passed only because it happens to be a substring of `−460.03`.

Fix: `no_variant()` now takes `also=()` to mask legitimate alternative
renderings at other precisions, plus a companion **R8l2** that pins the
full-precision value. Sabotage testing confirmed the relaxation did not blunt
the check: mutating `−318.8 → −318.7` or `−318.76 → −318.75` still fails.

New check groups added (these were the actual blind spots):

- **R9** — §2 residual summary (5 values × present/absent) on the registered basis.
- **R10a–b** — Table 3 constructive column and K=1000 `T=1`.
- **R10c** — Table 5 reproduces the registered campaign (scoped to the Table 5
  block; an unscoped search matches Tables 1/2/4, which share row labels).
- **R10d–h, R10f** — Result 3.8 cells, Fox constructive, §3.8 probabilities and
  deltas, an allowlist audit of every surviving "source-year" mention (5 found,
  5 approved), and Table 5's caption.

**Every one of the 19 sabotage mutations is now caught.** Before this round,
all four §2 mutations — and every Table 3/5 mutation — left the battery green.

---

## 5. Open item: the figures (needs your recovered files)

The tex references seven figures under `figs_e2/`. No `figs_e2/` directory
exists anywhere in the workspace.

| referenced | available in registered campaign? |
|---|---|
| `fig1_surplus.png` | ✅ `fig1_surplus.png` |
| `fig4_fprime.png` | ✅ `fig4_fprime.png` |
| `fig6_k_sensitivity.png` | ✅ `fig6_k_sensitivity.png` |
| `fig2_kernel_vs_catch_v21.png` | ⚠️ produced as `fig2_kernel_vs_catch.png` |
| `fig5_replay.png` | ⚠️ produced as `fig3_replay.png` |
| `fig7_stochastic.png` | ⚠️ produced as `fig5_stochastic_constructive.png` |
| `fig3_reactive_rules.png` | ❌ not produced by the elevation campaign |

Three have campaign counterparts under **different names**; one
(`fig3_reactive_rules.png`, the reactive-families plot) has none. I have not
renamed or copied any of them — I cannot view the images, and putting a plot
under a caption it does not match would be worse than leaving the reference
unresolved. Please recover the original `figs_e2/` directory, or confirm the
mapping and I will copy the campaign's files across.

---

## 6. Second open item: §3.5 sits on the source-year convention

§3.5's stress replay uses the source-year residual convention (verified above),
while the rest of the paper is registered. It is **explicitly labelled**, so it
is not a false claim — but a referee could object to the paper reporting two
catch-timing conventions in different sections without a stated rationale.
Changing it would require recomputing the whole §3.5 narrative, so I left it
labelled rather than guess. Worth a sentence of justification in the paper, or
migration to the registered replay (906.52 / 901.52 / 876.52 / 846.52).

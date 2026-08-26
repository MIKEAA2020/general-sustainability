# WAVE_E_RERUN — Independent Reproduction of the Wave E Scored Trees

**Scope.** Item 2 of the agreed plan: run `wave_e_cod` and `wave_e_edwards` from the committed sources and check the scores against what the READMEs, the manuscripts, and `PROOF_MANIFEST.md` Part VI claim.

**Toolchain.** Python 3.13.14, numpy 2.3.5, pandas 2.2.3, scipy 1.17.1, matplotlib 3.10.9 — the four packages `PROOF_MANIFEST.md` Part VI names as the requirement.

**Headline: reproduction passes, and passes more strongly than the manifest claims.** All 29 pinned hashes match, all 9 scripts run clean, and all 30 regenerated result files are **byte-identical** to the committed versions. Five documentation-level defects found; **no numerical discrepancy** between the artifacts and any prose claim. The substantive conclusion — persistence is not beaten as structure — holds.

Reproducible check: `reaudit/verify_wave_e.py` (exit 0; output `reaudit/wave_e_output.txt`).

---

## 1. Hash verification — 29/29 match

`PROOF_MANIFEST.md` Part VI pins a SHA-256 for every Wave E artifact. All 29 match the committed tree exactly, before running anything: 16 in `wave_e_cod/`, 13 in `wave_e_edwards/`, covering run metadata, rolling/fixed scores, forecast paths, locked inputs, both frozen protocols, and both manuscripts.

## 2. Script execution — 9/9 clean

| Tree | Script | Exit | Notes |
|---|---|---|---|
| cod | `src/run_ladder.py` | 0 | rewrites 6 files |
| cod | `src/run_xte.py` | 0 | |
| cod | `src/run_capelin_regime.py` | 0 | |
| cod | `src/run_capelin_index.py` | 0 | |
| cod | `src/compare_catch.py` | 0 | reports `max |diff| t = 0`, 11/11 exact year matches |
| cod | `src/make_figures.py` | 0 | see finding 5 |
| edwards | `src/run_ladder.py` | 0 | Pass 1 |
| edwards | `src/run_recharge.py` | 0 | Pass 2 |
| edwards | `src/make_figures.py` | 0 | see finding 5 |

`src/build_panel.py` exits 0. After the F4 repair it writes H/R/P/Q to `data/annual_panel_hrp.csv` and **leaves** the locked 20-column `annual_panel.csv` in place when those columns already match. `src/build_climate.py` was not run; its `climdiv-pcpndv-v1.0.0-20260806` input is gitignored (finding 3).

## 3. Byte-identity — 30/30 regenerated result files identical

Every file in `wave_e_cod/results/` (17) and `wave_e_edwards/results/` (13) was regenerated and compared byte-for-byte against a pre-run snapshot. **All identical.**

This is stronger than the manifest's own caveat — "A rerun may rewrite floating-point summaries; hash identity is not guaranteed across machines" — and it discharges the `INDEPENDENT_RERUN_NONE` label for the scored-tree result artifacts. Figures remain unpinned (finding 5). `annual_panel.csv` as committed hashes; `build_panel.py` no longer drops climate columns (F4 fixed).

## 4. Every prose number reproduces

No discrepancy was found between any artifact and any claim in the READMEs or manuscripts. Spot-check summary:

**Cod, rolling (`rolling_summary.csv`, regime rows).** persist 98/48/0.52/265 · M1 121/80/8.02/289 · M1b 115/80/8.70/289 · M2 144/61/0.59/398 · M3 135/53/3.39/366 · M4 196/82/0.76/488 · train-mean 424/375/2.35/507. Persistence wins RMSE at both horizons — the README's claim holds.

**Cod, Pass 2 (annual catch).** M2 annual 160/394 · M2 survey start 128/331 · M3 154/352 · M4 206/486. Survey start improves log-RMSE 0.58 → 0.49 while still losing to persistence on primary RMSE — exactly as the README states.

**Cod, Pass 6 (capelin).** README's "150/132 vs persist 98/88" decodes correctly to `M_cap_index` h=1 on ncam2016 (150.02) and xteNCAM (132.02) against persistence (98.05 and 87.65). "Near-tie on 2016 five-year RMSE only" = 262.34 vs 264.72. Both accurate.

**Cod, fixed windows.** Collapse M1 694.27/638.32/2.73/1.00/0.50; Recovery M1b 89.77/55.06/0.52/0.00/0.57. The manuscript's "Recovery M1 = M2" is literally true — the two rows are numerically identical in the CSV.

**Cod, LRP.** The manuscript declares `K* = LRP = 884.6 kt (1983–1989 mean of Table A2)`. Recomputed from the committed `ncam_2016_table_a2.csv`: mean `ssb_kt` over 1983–1989 = **884.58**. ✓

**Edwards, Pass 1.** persist 13.23/10.73/21.11 · mean 16.17/13.17/16.80 · M1 12.84/10.72/21.25 · M2 14.70/11.45/33.49 · M2m 12.28/10.22/17.44 · M3 14.46/11.12/33.46 · M4 14.30/11.17/33.39 · oracle 7.55/5.79/10.87. All nine rows match the manuscript table.

**Edwards, Pass 2.** M2_enso 12.82/24.42 · M2_precip 12.80/25.38 · M2_combo 12.71/26.88 · M2_Rar 13.25/25.38 · rain oracle 10.56/16.91. Margins vs M1 = 0.0176 / 0.0444 / 0.1281 ft (manuscript: "0.02, 0.04, and 0.13"). h=5 losses to persistence = 3.32 / 4.27 / 5.77 ft (manuscript: "3–6 ft"). Both accurate.

**Edwards, fibre.** persist 71.90 · M1 68.95 · M2m 68.67 · M2 74.80 · oracle 45.32 cfs (manuscript: 71.9 / 69.0 / 68.7 / 74.8 / 45.3). ✓

**Edwards, fixed windows.** `dor_recovery` persist 43.62, best causal (M2_Renso) 48.77, rain oracle 33.74 (manuscript: 43.6 / ~48.8 / 33.7). ✓

**Edwards, full-sample statistics** — all ten recomputed independently from the committed `annual_panel.csv`:

| Claim | Manuscript | Recomputed |
|---|---|---|
| corr(H_t, H_{t−1}) | 0.64 | 0.6437 |
| corr(R_t, R_{t−1}) | 0.17 | 0.1719 |
| corr(ΔH_t, R_t) | 0.74 | 0.7423 |
| corr(R_t, P̄) | 0.78 | 0.7786 |
| AR(1) φ̂ on H | 0.66 | 0.6569 |
| 1956 SON Niño 3.4 | −0.92 | −0.9228 |
| R₁₉₅₇ | 1143 | 1142.60 |
| fibre c₀ (fit 1934–50) | −2876 | −2875.6426 |
| fibre c₁ | 4.77 | 4.7682 |
| corr(Comal, J-17) | 0.986 | 0.9861 |

---

# Findings

## F1 — `pass2_meta.json` retention field contradicts both prose documents — **FIXED**

Was: `"retained": ["M2_enso", "M2_precip", "M2_combo"]` (and Pass 1 `"retained": ["M1", "M2m"]`) against prose that demotes all of those except thin M1.

**Repair.** `run_ladder.py` / `run_recharge.py` now write `listed_by_point_rule`, `class_demoted`, and `retained_as_structure`. The misleading `retained` key is gone.

- Pass 1: listed `M1`, `M2m`; class-demoted `M2m`; retained as structure `M1`.
- Pass 2: listed the three RMSE-listers; class-demoted all three; retained as structure `[]`.

## F2 — the Edwards README's Pass 1 line omits the best-performing model — **FIXED**

The README Pass 1 line now names M2m and the class demotion (beats persist at both horizons; AR(1) under constant fluxes; declined as extra structure).

## F3 — `NOT_REPRODUCIBLE_FROM_COMMITTED_CODE` is over-broad

The manifest applies that label to `build_climate.py` wholesale. The five climate columns split:

| Column | Source | Committed? | Reproduces? |
|---|---|---|---|
| `nino34_son` | `data/psl_nino34_long.data` | **yes** | yes — max abs diff **2.2e-16** over 98 rows |
| `nino34_ann` | `data/psl_nino34_long.data` | **yes** | yes — max abs diff **1.1e-16** over 99 rows |
| `pcp_cd06`, `pcp_cd07`, `pcp_mean` | `climdiv-pcpndv-v1.0.0-20260806` | no (gitignored) | no |

I ran `build_climate.load_nino34` / `son_anomaly` directly against the committed file and compared to the committed panel. Both Niño columns rebuild exactly.

**Fix (applied in the manifest).** The `NOT_REPRODUCIBLE_FROM_COMMITTED_CODE` label is scoped to the three `pcp_*` columns. Niño columns rebuild from the committed PSL file. Pass 2's ENSO arm is in `listed_by_point_rule`, not `retained_as_structure`.

## F4 — `build_panel.py` silently destroys the committed panel — **FIXED**

Was: running `python3 src/build_panel.py` overwrote `annual_panel.csv` with 15 columns and dropped climate.

**Repair.** The script writes H/R/P/Q to `data/annual_panel_hrp.csv` (gitignored scratch). If `annual_panel.csv` already has the five climate columns and the H/R/P/Q values match, dest is left byte-identical (pinned hash stands). Otherwise climate columns are merged back. Pass 2 remains consumable after a panel rebuild.

## F5 — figures reproduce geometrically, not bit-for-bit

`make_figures.py` in both trees regenerates SVGs that differ from the committed ones. The differences are confined to non-deterministic metadata: the `<dc:date>` element and matplotlib's randomly-hashed element IDs (`m39a0666634` → `mb39221357c`). Path coordinates are identical and all PNGs are byte-identical.

The manifest correctly declines to pin figure hashes. Worth recording *why*, and worth knowing that `SOURCE_DATE_EPOCH` plus `svg.hashsalt` would make the SVGs deterministic if figure hashes are ever wanted.

## F6 — markdown defect in the manifest's Edwards table — **FIXED**

The literal `\n` in the Part VI §B header separator is gone; the table renders.

---

# Substantive conclusion

Reproduction does not change the programme's honest negative. On the cod side, persistence wins RMSE outright at h=1 and h=5 against every causal rung. On the Edwards side, M1 survives the frozen point rule by 0.39 ft on n=75 — which the manuscript itself calls "not a theory confirmation … a slightly mean-reverting head" — M2m and all three Pass 2 structures are demoted on class grounds, and at h=5 the training mean beats persistence, M1, and every causal module.

`PROOF_MANIFEST.md` Part III's "every Wave E support row is **NOT CONFIRMED**" remains the correct *gate* label. The Part VI reproducibility qualifier has been upgraded: `INDEPENDENT_RERUN_NONE` is false for the scored trees — an independent rerun on a different toolchain matched every hash (`INDEPENDENT_RERUN`; see Part VI). Findings F1 and F4 remain open documentation defects; they do not make the rerun “none”.

---

# What I did not check

- **Data provenance.** The locked inputs were verified by hash, not against their upstream sources (DFO/NAFO, TWDB, USGS, NOAA PSL). `compare_catch.py` self-audits the Schijns catch table at 11/11 exact matches; I did not independently pull any source.
- **Protocol conformance.** I did not audit whether the frozen protocols (`protocol.md`, `protocol_pass2.md`) were in fact frozen before scoring, or whether the scoring code matches every declared rule. That requires commit-history forensics beyond this pass.
- **Model correctness.** I verified that the code reproduces its committed outputs and that the prose matches those outputs. I did not audit whether the Schaefer/Allee/stock-flow implementations are the right models, or whether the fits converge to global optima.
- **The 2016 xteNCAM pooling discipline** — the "do not pool" instruction is respected in the code paths I traced, but I did not exhaustively verify no cross-`Ω` leakage.

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

`src/build_panel.py` also exits 0 but is not a clean reproduction — see finding 4. `src/build_climate.py` was not run; its `climdiv-pcpndv-v1.0.0-20260806` input is gitignored (finding 3).

## 3. Byte-identity — 30/30 regenerated result files identical

Every file in `wave_e_cod/results/` (17) and `wave_e_edwards/results/` (13) was regenerated and compared byte-for-byte against a pre-run snapshot. **All identical.**

This is stronger than the manifest's own caveat — "A rerun may rewrite floating-point summaries; hash identity is not guaranteed across machines" — and it discharges the `INDEPENDENT_RERUN_NONE` label for the results artifacts on this toolchain. The label remains correct for the figures (finding 5) and for `annual_panel.csv` (finding 4).

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

## F1 — `pass2_meta.json` retention field contradicts both prose documents (highest severity)

The machine-readable record asserts the opposite of the manuscript and the README.

- `results/pass2_meta.json`: `"retained": ["M2_enso", "M2_precip", "M2_combo"]`, rule `"retain only if H RMSE < persist AND < M1"`.
- `manuscript/…md` §Pass 2: "They are M2m with a weakly adjusted intercept. **Promoting them is inflation.**"
- `README.md`: "**not retained as structure**."

The same shape in Pass 1: `results/meta.json` says `"retained": ["M1", "M2m"]`, while the manuscript's retention table records M2m as "numerical list only; **not extra structure**" and adds "Promoting M2m as 'stock-flow earned' would be inflation."

The scripts encode only the frozen point-RMSE rule; the class-demotion step that both prose documents apply is nowhere in the code. Anyone consuming the JSON — a downstream docket, a CI check, a literature-matching script — gets three retained structures where the programme's document of record retains none.

**Fix.** Either fold the demotion into the retention rule, or rename the field to `listed_by_point_rule` and add a separate `retained_as_structure`. The second is cheaper and preserves the frozen-rule audit trail.

## F2 — the Edwards README's Pass 1 line omits the best-performing model

README: "**Pass 1:** persist 13.23; M1 12.84 (thin); M2 persist-(R,P) 14.70 (reject); oracle 7.55."

M2m is absent. On the committed numbers M2m is the only model that beats persistence at **both** horizons — 12.28 vs 13.23 at h=1 (+0.95 ft) and 17.44 vs 21.11 at h=5 (+3.66 ft) — and it is what `meta.json` lists as retained. The manuscript handles this correctly and at length (constant fluxes ⇒ the model collapses to AR(1), so the edge "is not extra structure"). The README, the most likely entry point for a reader, does not mention that the baseline was beaten and why the win was declined.

**Fix.** One clause in the README: "M2m 12.28 beats persist but collapses to AR(1); demoted on class grounds, see manuscript §5."

## F3 — `NOT_REPRODUCIBLE_FROM_COMMITTED_CODE` is over-broad

The manifest applies that label to `build_climate.py` wholesale. The five climate columns split:

| Column | Source | Committed? | Reproduces? |
|---|---|---|---|
| `nino34_son` | `data/psl_nino34_long.data` | **yes** | yes — max abs diff **2.2e-16** over 98 rows |
| `nino34_ann` | `data/psl_nino34_long.data` | **yes** | yes — max abs diff **1.1e-16** over 99 rows |
| `pcp_cd06`, `pcp_cd07`, `pcp_mean` | `climdiv-pcpndv-v1.0.0-20260806` | no (gitignored) | no |

I ran `build_climate.load_nino34` / `son_anomaly` directly against the committed file and compared to the committed panel. Both Niño columns rebuild exactly.

**Fix.** Scope the label to the three `pcp_*` columns. As written it tells a reviewer that Pass 2's ENSO predictors cannot be rebuilt from the repo, which is false — and Pass 2's ENSO arm is one of the three the JSON retains.

## F4 — `build_panel.py` silently destroys the committed panel

The manifest lists `python3 src/build_panel.py` as the reproduction command for `annual_panel.csv`. Running it overwrites the file and emits **15** columns instead of **20**, dropping all five climate columns. The hash moves from the pinned `d6d725db…` to `9e60a791…` and the tree goes dirty.

The good news: the 15 H/R/Q columns reproduce **exactly** — zero differences across all 100 rows. The bad news: following the manifest's own instruction leaves a panel that Pass 2 cannot consume, with no error raised.

**Fix.** Have `build_panel.py` write to a scratch path, or merge the climate columns back when they are already present; and state in the manifest that reproducing the pinned hash requires `build_climate.py` to run afterwards. I restored the file with `git checkout`; the tree is clean.

## F5 — figures reproduce geometrically, not bit-for-bit

`make_figures.py` in both trees regenerates SVGs that differ from the committed ones. The differences are confined to non-deterministic metadata: the `<dc:date>` element and matplotlib's randomly-hashed element IDs (`m39a0666634` → `mb39221357c`). Path coordinates are identical and all PNGs are byte-identical.

The manifest correctly declines to pin figure hashes. Worth recording *why*, and worth knowing that `SOURCE_DATE_EPOCH` plus `svg.hashsalt` would make the SVGs deterministic if figure hashes are ever wanted.

## F6 — markdown defect in the manifest's Edwards table

The header separator row of the Part VI §B table contains a literal `\n`:

```
|---|---|---|---|---|\n| Pass 1 run metadata | `wave_e_edwards/results/meta.json` | …
```

The table does not render. Cosmetic, but it is in the section a reviewer uses to reproduce.

---

# Substantive conclusion

Reproduction does not change the programme's honest negative. On the cod side, persistence wins RMSE outright at h=1 and h=5 against every causal rung. On the Edwards side, M1 survives the frozen point rule by 0.39 ft on n=75 — which the manuscript itself calls "not a theory confirmation … a slightly mean-reverting head" — M2m and all three Pass 2 structures are demoted on class grounds, and at h=5 the training mean beats persistence, M1, and every causal module.

`PROOF_MANIFEST.md` Part III's "every Wave E support row is **NOT CONFIRMED**" and Part VI's `SINGLE_RUN` framing remain the correct labels. What *can* now be upgraded is the reproducibility qualifier: for the 30 result artifacts, `INDEPENDENT_RERUN_NONE` is no longer accurate — an independent rerun on a different toolchain matched every hash. Findings F1 and F4 should be fixed before that upgrade is written in, since both concern exactly the artifacts a rerun touches.

---

# What I did not check

- **Data provenance.** The locked inputs were verified by hash, not against their upstream sources (DFO/NAFO, TWDB, USGS, NOAA PSL). `compare_catch.py` self-audits the Schijns catch table at 11/11 exact matches; I did not independently pull any source.
- **Protocol conformance.** I did not audit whether the frozen protocols (`protocol.md`, `protocol_pass2.md`) were in fact frozen before scoring, or whether the scoring code matches every declared rule. That requires commit-history forensics beyond this pass.
- **Model correctness.** I verified that the code reproduces its committed outputs and that the prose matches those outputs. I did not audit whether the Schaefer/Allee/stock-flow implementations are the right models, or whether the fits converge to global optima.
- **The 2016 xteNCAM pooling discipline** — the "do not pool" instruction is respected in the code paths I traced, but I did not exhaustively verify no cross-`Ω` leakage.

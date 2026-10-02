# Frozen specification sheet — Northern cod (NAFO 2J3KL), Ω_2016 and Ω_xte

**Sheet status: FROZEN (documentation extract; no theorem or gate status is created or changed by this sheet).**

*Second edition (2026-08-29): this edition corrects the one manuscript-echo this sheet carried over from the first forecast-paper edition — the one-year ladder range in the frozen-verdict line is stated per catch treatment: 115–196 kt under the coarse catch regime, 115–206 kt across both catch treatments (batch-5 adjudication W09; the paper's second edition carries the same catch-pass split). The first edition remains the issued frozen record of 2026-08-27 and is byte-identical in the repository; no specification element, protocol lock, catch treatment, uncertainty class, governance-family member, retention rule, or verdict structure changes in this edition.*

**Issued 2026-08-27** as the per-paper specification sheet requested for the publication wave. This sheet extracts, in one place, the specification that the scored artifacts implement. The authoritative sources remain, in order: `manuscript/wave_E_cod_forecast_ladder.md` §1–2 (the declaration), `results/meta.json` + `results/xte_meta.json` (the machine locks), `protocol_intervention.md` (the intervention leg, frozen before its scores), and `batch 4/WAVE_E_SPEC_MATCH.md` (the artifact-level match record, 36 machine checks via `reaudit/verify_wave_e_spec_match.py`). Every claim below traces to those sources; nothing here supersedes them.

**No pooling, no transfer.** The two specifications Ω_2016 and Ω_xte are separate objects and are not mixed: the two SSB columns differ in four typed fields (dynamics map, safe-set map, catch treatment, horizon), no row of one enters any fit, score, or verdict of the other, and R04 forbids judgment transfer between them (both the safe-set map and the dynamics map fail). Nothing in this tree is pooled with the Edwards J-17 object (`wave_e_edwards/`) or with any phosphorus catchment.

---

## 1. Primary specification Ω_2016 — scored prediction leg

| Element | Frozen value |
|---|---|
| **System \(S\)** | Northern cod, NAFO divisions 2J3KL, as represented by the NCAM \(M\)-shift assessment |
| **Predictand / data series \(y_t\)** | NCAM \(M\)-shift spawning-stock biomass (SSB), DFO SAR 2016/026 **Table A2**, calendar years **1983–2015**, in kt |
| **Safe set \(K^*\)** | \(S_t \ge \mathrm{LRP} = 884.6\) kt (the 1983–1989 mean of Table A2; the 2010/2016 precautionary-approach LRP — **not** the 2023 40% \(B_{\mathrm{MSY}}\) LRP) |
| **Domain \(B\)** | Stock area of DFO (2016) Figure 1; calendar years 1983–2015 |
| **Catch treatment** | Primary pass: coarse regime 240 kt (\(t\le1991\)) / 120 kt (1992) / 5 kt (\(\ge1993\)); replaced by year-by-year Schijns et al. (2021) landings in §5.2. NCAM \(F\) and \(M\) are joint assessment outputs and are **never** exogenous drivers |
| **Horizon \(T\)** | Hindcast 1983–2015: two fixed windows (collapse train 1983–1990 / test 1991–1995; recovery train 1995–2007 / test 2008–2015) + rolling origin |
| **Scoring rule (primary)** | Rolling RMSE (kt) at \(h=1\) and \(h=5\) |
| **Scoring rule (secondary)** | log-RMSE; Brier |
| **Model ladder** | naive_persist; naive_train_mean; M1 (autonomous Schaefer, \(r,K,C\) constant); M1b (Allee); M2 (stock-flow, prescribed \(C_t\)); M3 (M2 + AR(1) residual); M4 (delay — forecast starts from \(S_{t-1}\)); pass-2 extension M2_survey_start (recorded, not retained on primary) |
| **Retention rule** | A module is kept only if it improves the preregistered primary score vs persistence (and vs the next-simpler causal model); oracle/fibre cannot promote |
| **Estimation** | One-step least squares on the training window only; bounds \(r\in(0.001,2]\), \(K\) above the training maximum |

**Frozen verdict (scored, independently rerun):** no structural model beats last-value persistence (h=1: persist 98.0 kt vs ladder 115–196 kt under the coarse catch regime — 115–206 kt across both catch treatments; h=5: 265 kt vs 289–488 kt); the collapse window is missed by every model (694–819 kt). Negative certificate, not a forecast gain. Part VI status `INDEPENDENT_RERUN` (`batch 4/WAVE_E_RERUN.md`: 29/29 pinned hashes, 30/30 result files byte-identical).

**Freeze-discipline caveat (recorded, not repaired):** the cod specification is manuscript-declared (manuscript §2 + `meta.json` locks), not a dated pre-score protocol file as on Edwards; the passes evolved (1→6) with extensions declared in the manuscript rather than pre-registered. The per-observation rolling artifact stores the annual (Schijns) catch treatment; the regime treatment is recorded at summary level.

## 2. Second specification Ω_xte — unpooled

| Element | Frozen value |
|---|---|
| **System \(S\)** | Northern cod 2J3KL as represented by the xteNCAM assessment (Regular et al. 2025) |
| **Predictand / \(y_t\)** | xteNCAM SSB, calendar years **1954–2024**, kt (Regular et al. 2025, Table 17, pp. 67–70 of the DFO 2025/048 research document; committed as `data/xtencam_table17_ssb.csv`) |
| **Safe set \(K^*\)** | LRP = 276 kt (40% \(B_{\mathrm{MSY}}\), 95% interval 180–423 kt) |
| **Horizon \(T\)** | Rolling origin on 1954–2024 |
| **Scoring rule** | As Ω_2016 (primary rolling RMSE at \(h=1,5\)) |
| **Ladder** | The same ladder class instantiated on the xte series (persist 88 kt vs autonomous M1 120 kt at \(h=1\)) |
| **Pooling** | **None.** Distinct observed values on all 25 shared origins; the two SSB columns are never mixed |

**Frozen verdict:** persistence wins here too; capelin-informed productivity (1991 regime break or the tabulated acoustic index without interpolation) is not retained on the primary score.

## 3. Intervention leg — the governed surplus object (companion paper)

Frozen in `protocol_intervention.md` (**2026-08-26, before any kernel, boundary, replay, or retention score was computed**):

| Element | Frozen value |
|---|---|
| **Object** | The ladder's own M2 class (discrete surplus with catch, Allee off), fit 1983–2007 on Schijns annual catch; OOS audit 2008–2015, no refit |
| **Safe set** | \(K^* =\) LRP = 884.6 kt (single threshold; Ω_2016 declares no second threshold — no cod analogue of the Edwards phys/inst pair) |
| **Uncertainty classes** | Persistent additive productivity floors UC-min / UC-q05 / UC-q10 of the fit-window residual distribution |
| **Governance family** | BAU moratorium-level 5 kt; flat caps (\(\rho\cdot240\) kt); S1 = DFO-2009 critical-zone rule at a 60 kt cap; a declared cascade |
| **Retention rule** | The Edwards intervention rule verbatim (robust viability kernels + replayed supply vs BAU) |
| **Erosion conversion** | Cor2 in the **expansive** form (\(F'(K^*) = 1.153 > 1\); the contraction form is inapplicable) — the programme's first expansive object |

**Frozen verdicts (rerun-verified):** productivity negative certificate (under UC-min/q05 no catch policy — zero included — holds the LRP); no policy retained; maximal robust flat catch 57.6 kt at UC-q10; certified kernels empty beyond \(T=5\) yr. Kernel-level admission `admission/R04_Cor2_cod_kernel.md` (APPROXIMATION). Rerun 2026-08-26 byte-identical (`reaudit/intervention_rerun_cod/`).

## 4. Standing disclosures

- \(K\) is expected to pin at its optimization bound on this series; upper edges inherit it. The residual conflates productivity shocks and Schaefer-class model error — disclosed, not repaired. One pool, no age structure, no migration (A014-L list).
- This sheet does not cite and does not rest on any theorem demoted or repaired in `batch 4/PROOF_REAUDIT.md`; the intervention leg invokes R04.Thm1 / R04.Cor2 / R03.Cor5 (PROVEN at their stated scopes, per `PROOF_MANIFEST.md` Part I) and marks its admission row APPROXIMATION.
- Wave E Part III paper-support rows remain **NOT CONFIRMED** in `PROOF_MANIFEST.md` (they concern paper claims, not these trees); nothing in this sheet changes that.

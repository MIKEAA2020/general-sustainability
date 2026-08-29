# Frozen specification sheet — Edwards Aquifer, San Antonio Pool, Ω_SA

**Sheet status: FROZEN (documentation extract; no theorem or gate status is created or changed by this sheet).**

*Second edition (2026-08-29): this edition corrects the one manuscript-echo this sheet carried over from the first intervention-paper edition — the BAU nominal-kernel horizon under the perpetual-1956 floor is \(T\approx 13\) yr (the continuous crossover is 12.7 under the paper's own convention; the \(T=12\) boundary is 692.6 ft and the \(T=13\) kernel is empty), not "~14 yr" (batch-5 adjudication W03; the paper's second edition carries the same correction). The first edition remains the issued frozen record of 2026-08-27 and is byte-identical in the repository; no specification element, protocol lock, uncertainty class, governance-family member, retention rule, or verdict structure changes in this edition.*

**Issued 2026-08-27** as the per-paper specification sheet requested for the publication wave. This sheet extracts, in one place, the specification that the scored artifacts implement. The authoritative sources remain, in order: `protocol.md` (**locked 2026-08-25, before scores were generated** — the dated pre-score protocol), `protocol_pass2.md` (Pass 2's own pre-score protocol), `protocol_intervention.md` (**locked 2026-08-26, before the intervention scores were generated**), and `batch 4/WAVE_E_SPEC_MATCH.md` (the artifact-level match record, 36 machine checks via `reaudit/verify_wave_e_spec_match.py`). Every claim below traces to those sources; nothing here supersedes them.

**No pooling, no transfer.** This object is not pooled with Northern cod (`wave_e_cod/`), with J-27 (Uvalde Pool — a different pool), or with any phosphorus catchment. Two Ω, two papers; the general theory's admission discipline (R04) forbids judgment transfer across failing typed-field maps.

---

## 1. Primary specification Ω_SA — scored prediction leg (Pass 1)

| Element | Frozen value |
|---|---|
| **System \(S\)** | Edwards Aquifer, San Antonio Pool, as indexed by well J-17 (TWDB 6837203 / EAA AY-68-37-203, Bexar County) |
| **Predictand / data series \(y_t = z_t\)** | Calendar-year mean of daily-high J-17 elevation, **ft AMSL** (the management unit; measured well, not an assessment inversion) |
| **Domain \(B\)** | San Antonio Pool management region; calendar years **1934–2023** |
| **Series construction** | All available daily highs each year; years with < 240 daily values dropped; missing days **not** interpolated; 1935 (\(n=258\)) and 1939 (\(n=242\)) retained as incomplete-coverage means; the published pre-logging composite (Beverly Lodges extension) used as official, not re-spliced [E] |
| **Safe sets** | \(K^*_{\mathrm{phys}} \approx 618\) ft (Comal Springs cessation proximity; declared, not certified); \(K^*_{\mathrm{inst}} = 660\) ft (EAA Stage I 10-day rule, post-2007) |
| **Fibre \(Y\) (excluded from retention)** | USGS 08168710 Comal Springs annual mean discharge — a post-selection robustness check only |
| **Horizon \(T\)** | Hindcast 1934–2023: four fixed windows + rolling origin (min 15 training years; \(h=1,5\); complete panel only) |
| **Fixed windows** | DOR drawdown train 1934–1950 / test 1951–1956; DOR recovery train 1934–1956 / test 1957–1961; pre-permit wet train 1980–1990 / test 1991–1995; CPM era train 1997–2014 / test 2015–2023 |
| **Scoring rule (primary)** | RMSE of annual-mean J-17, ft AMSL |
| **Scoring rule (secondary)** | MAE; Brier for \(\mathbf 1\{\hat H < 660\}\) (annual-mean proxy — **not** the 10-day rule; interpreted only for origins ≥ 2007); sign-hit of \(\Delta H\) on fixed windows |
| **Model ladder (causal)** | naive_persist; naive_mean; M1 (output/autonomous \(H_{t+1}=a+\varphi H_t\)); M2 (stock-flow, one-pool water balance, last \((R_t,P_t)\) persisted); M2m (stock-flow, training-mean fluxes); M3 (M2 + AR(1) residual); M4 (delay, starts from \(H_{t-1}\)); M2_oracle (**diagnostic only** — realized future \(R,P\); cannot retain) |
| **Retention rule** | A causal module is retained only if it reduces primary RMSE vs the next-simpler causal model **and** vs naive_persist; oracle/fibre cannot promote |

**Frozen verdict (scored, independently rerun):** persist 13.23; M1 12.84; M2 14.70 (reject); M2m 12.28 & 17.44 — beats persistence at both horizons but **declined on class grounds** (collapses to AR(1) under constant fluxes; "not extra structure"); oracle 7.55 (diagnostic — the information-layer rent). Part VI status `INDEPENDENT_RERUN` (`batch 4/WAVE_E_RERUN.md`).

## 2. Pass 2 — causal recharge (own pre-score protocol)

`protocol_pass2.md`: causal \(R\) modules (SON Niño 3.4 / lagged climate-division rain / AR) scored against M1 and persistence under the frozen Pass-1 rules. **Verdict:** listed by point rule (0.02–0.13 ft vs M1), worse than persistence at \(h=5\), `retained_as_structure` empty — the F1 field-split record (`results/pass2_meta.json`). The rain oracle (10.56) is excluded.

## 3. Intervention leg — the governed one-pool object (companion paper)

Frozen in `protocol_intervention.md` (**locked 2026-08-26, before the intervention scores were generated**) — the first §15 intervention-selection leg exercised on a real system in this programme:

| Element | Frozen value |
|---|---|
| **Object** | The scored ladder's M2 class (one pool, affine \(\Delta H_t = \alpha+\beta R_t+\gamma P_t+\delta H_{t-1}\)), OLS on 1934–1990; 1991–2023 defect audit only, no refit |
| **Data** | `data/annual_panel.csv` only (the locked 20-column panel); no new data |
| **Safe sets** | \(K^*_{\mathrm{phys}}\) 618 ft; \(K^*_{\mathrm{inst}}\) 660 ft (post-2007) |
| **Model domain** | \(H \in [610, 710]\) ft (the ladder's clip bounds; upward exits above 710 are out-of-domain for the model, not constraint violations) |
| **Uncertainty classes** | Persistent recharge floors: perpetual-1956 / q05 / q10 of training recharge |
| **Governance family** | BAU; flat caps; Stage-I reactive; CPM cascade |
| **Retention rule** | Robust viability kernels + replayed supply vs BAU, under the declared uncertainty classes; no forecast module promoted or demoted by this leg; no two-pool claim |
| **Erosion conversion** | Cor2/Cor5 invoked for the first time on a real system (`admission/R04_Cor2_edwards_kernel.md`, APPROXIMATION) |

**Frozen verdicts (rerun-verified):** S1 and cpm retained at the drought-floor/physical reading (+3.3% to +50.6% water at matched protection — the programme's first positive selection result); BAU not robustly viable beyond \(T\approx 13\) yr under the perpetual-1956 floor (the continuous crossover is 12.7; the \(T=12\) boundary is 692.6 ft); negative certificate at the institutional threshold; certified kernels defect-bound to \(T \le 3\) yr (train ε = 15.4 ft, OOS 21.8). Rerun 2026-08-26 byte-identical (`reaudit/intervention_rerun/`).

## 4. Standing disclosures

- **Climate reproducibility:** the three `pcp_*` precipitation columns of `annual_panel.csv` are `NOT_REPRODUCIBLE_FROM_COMMITTED_CODE` (the nClimDiv raw file `climdiv-pcpndv-v1.0.0-20260806` is not committed; URL in `data/SOURCES.md`); the two Niño columns rebuild exactly from the committed PSL file. Scoring Pass 1/2 from the committed panel does not need the nClimDiv file (`PROOF_MANIFEST.md` Part VI, F-item record).
- The admitted object is the **one-pool affine approximation** — not a two-pool kernel, not exact (the A005 two-pool exact specialization remains open).
- This sheet does not cite and does not rest on any theorem demoted or repaired in `batch 4/PROOF_REAUDIT.md`; the intervention leg invokes R04.Cor2 / R03.Cor5 (PROVEN at their stated scopes, per `PROOF_MANIFEST.md` Part I) and marks its admission row APPROXIMATION.
- Wave E Part III paper-support rows remain **NOT CONFIRMED** in `PROOF_MANIFEST.md` (they concern paper claims, not these trees); nothing in this sheet changes that.

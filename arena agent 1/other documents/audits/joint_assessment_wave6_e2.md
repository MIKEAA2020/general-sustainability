# Joint assessment, wave 6 — the two Grok sub-audits of E2 cod intervention v4

**Status: VERIFICATION COMPLETE; implementation DONE — `paperE2_cod_intervention_v5.md` (research-article elevation, 6,383 words, Conclusions section added, Tables 3–5 and Figures 1–6 added; v4 untouched).**
Both sub-audits were evaluated jointly against `paperE2_cod_intervention_v4.md` and the committed
`wave_e_cod` machinery. Every quantitative claim was recomputed (`campaign_e2_elevation.py`, this
folder); every structural claim was checked line-by-line against the paper.

**Classification key.** GENUINE = valid, implement now · GENUINE-micro = valid, one-clause edit ·
STALE = already present in v4 · CORRECTED = the audit's claim is partially or fully wrong and the
computation decides · DEFERRED = registered for a later pass (with reason).

---

## 1. Arithmetic verdict (both sub-audits): CONFIRMED

Both audits re-derived and confirmed all explicit quantities: g_max = rK/4 = 296.125; g(K*) = 172.48;
57.62 = 172.47 − 114.85; F′(K*) = 1.153 (1.153075); the expansive series r₁=460, r₂=990.4, r₃=1602,
r₅=3120, r₈=6384; T=1 edges 1141.0/1136.6/1016.5/886.7; T=∞ edges 900.3/1363.0/2338.3; the 1990–92
replay arithmetic (single residual ≈ −124.4 under C=0/5/30 gives 906.5/901.5/876.5); the Allee refit
(r=2.0 pinned, K=1671.7, s₀=642.3, g_max=356.2, F′ 1.782). My campaign independently reproduces all of
it, plus a stronger check the audits could not run: the analytic T-step recursion reproduces **all 72
committed nominal kernel boundaries at T=1,3,5** (every policy × every floor) to <1 kt. **No arithmetic
or certificate error exists in v4.**

## 2. Dispositions

| # | Audit item | Class | Resolution (v5) |
|---|---|---|---|
| 1 | "Productivity certificate largely tautological" (floors > g_max ⇒ emptiness at zero catch) | GENUINE (framing) — v4 already flags "qualified by that mechanism" and states the critical-floor axis ē = g_max in §3.1, but leads the abstract and §3.2 with it | Abstract reweighted q10-first; §3.2 retitled "The vacuous classes"; the harsh classes become a one-paragraph robustness qualification; the final sentence scoped to the map + classes. The groundwater analogy gets its form-only scope |
| 2 | "Bound-pinned K contaminates two headline results" | **CORRECTED by computation** — the audit asserts a data-supported K below 2K* ≈ 1769 "would restore contraction and change the certification geometry". The full in-box K-grid refit (r re-estimated per K, floors frozen, K ∈ [951, 5000] box) shows the claim is **half true**: for K < 1769.2 the refit does contract (F′(K*) = 0.61–0.93), but exactly there the informative certificates collapse — the constructive bound falls to 0–34 kt, the kernel gains upper caps, at K=1000 the BAU q10 kernel is empty at T=∞ (the moratorium itself can no longer hold the LRP), and the fit cost rises (SSE 306,532 at K=5000 → 521,053 at K=1000, +70%). For every K ≥ 2K* the map is expansive (F′ ≥ 1.0000 at K=1769.2, rising to 1.1531 at K=5000) with the constructive bound 42.6–58.9 kt and the worst-class vacuity intact. **The expansion obstruction is therefore not a bound artifact: it is the parameterization the data select, and contraction is restored only in the regime where the reference point ceases to be robustly holdable at all** | New §3.7 K-sensitivity with the table and the corrected conclusion |
| 3 | "Retention rule structurally stacked" | GENUINE (framing) — the geometric mechanism is already stated in v4's Discussion, but not in Results, and the abstract over-reads | The geometry sentence is added to §3.2 (Results) as the declared design choice; abstract scoped ("by the rule's protective clause, any harvest at the boundary is less protective than the moratorium — the declared geometry, not an empirical verdict") |
| 4 | "Model class too crude for the biological claim" | STALE for v4's internal scoping (the Discussion carries the model-type limitations); the elevation adds the standalone methods recap so the reader sees the object before the claims | New §2.1 operating-model recap |
| 5 | "Certified layer is a severe map-dependent penalty" | GENUINE (framing) — reweighted with the K-grid + bootstrap evidence (F′ 90% bootstrap interval [1.001, 1.177]: the expansion persists under residual resampling) | §3.4 extended: the certified emptiness is reframed as a methods warning about the conversion on expanding maps, supported by the new layers |
| 6 | "Allee refit is not a mild sensitivity" | GENUINE-micro — v4 already reports the better SSE and the single reversal | §3.6 retitled "Model-form comparison"; the depensatory form stated as the data-preferred co-equal specification |
| 7 | "Perfect observation, no lag" | GENUINE-micro for the framing (already a caveat in v4's Discussion) | **RESOLVED (wave 6):** the audit's lag-1 item has two senses. (a) Residual autocorrelation — implemented: lag-1 ACF = 0.652 reported in §2.1, and §3.8's block-4 resampling respects it. (b) Delayed control — the project-wide timing convention exists and declares the base model's timing as same-year perfect observation: the companion forecast study's M4 module IS the one-year assessment delay ("forecast starts from S_{t−1}"), and E2 v5's Discussion states "real governance operates under assessment lags (the one-year delay module of the companion)… delay-aware kernels would be smaller or empty". A lag-1 governance kernel is therefore a declared companion extension, not a paper defect; no kernel is added |
| 8 | "Disturbance = residual = defect; circular" | STALE — v4 already states "the disturbance classes and the defect declaration are the same measured quantity in two roles" | Kept; the new stochastic layers explicitly separate the 1992 draw (one-off) from the persistent classes |
| 9 | "S1's 10 kt uninformative" | STALE — v4 already scopes the supply replay ("a fact about the collapsed-era estimation window, not about the rule's post-recovery supply properties") | Kept |
| 10 | "Replay from 1990 already outside" | STALE — v4 already says "uncontrolled shock accounting rather than a kernel-membership test" | Kept; Figure 3 draws it |
| 11 | "Companion dependence" | GENUINE | §2.1 standalone recap + the figure set; companion results appear once, in scoped sentences |
| 12 | "Style: dense certificate jargon" | GENUINE-micro | Ordinary-fisheries-language glosses added at first use of the technical terms; SI-style precision retained in the tables |
| 13 | No Conclusion section | GENUINE (user-requested) | New §5 Conclusions |
| 14 | "Figures: the single biggest upgrade" | GENUINE | Six figures computed and inserted (Figures 1–6) |
| 15 | "K-sensitivity / profile likelihood" | GENUINE — implemented as the K-grid (item 2) | New §3.7 |
| 16 | "Stochastic viability (i.i.d., blocks, finite floors, 1992 as one-off)" | GENUINE | New §3.8 (i.i.d., block-4, i.i.d.-without-1992) + §3.9 finite-duration floors |
| 17 | "Uncertainty: 57.6 cannot stand as a point" | GENUINE | New §3.10: parametric residual bootstrap (B=2000): constructive bound median 35.6 kt, 90% interval [0, 84.8]; stochastic analogue P(57.6)=0.77–0.88; P≥0.8 crossings 48.4 (i.i.d.) / 38.9 (blocks) / 95.1 kt (no-1992) |
| 18 | "Replay that is a test" (1980s-peak starts; forward check) | PARTIAL — the stochastic layer adds 1980s-peak starts (S₀ = 1000–2500 kt); the 2008–2015 forward check already exists (OOS audit 47.1 kt in Methods) | §3.8 table covers the peak starts; the OOS audit sentence stays |
| 19 | "Policy family grounded in DFO" (actual post-1992 catch history, F-lim rule) | DEFERRED — needs DFO-document sourcing of the historical inshore TAC path before it can be scored | Registered |
| 20 | "True viability kernel / DP maximal catch, regret metric" | DEFERRED — a different computation class (existential kernels over controls), registered as the next methods extension | Registered |
| 21 | "Co-viability second constraint" | DEFERRED | Registered |
| 22 | "Fox/Pella–Tomlinson third form" | EXECUTED (wave 7) — E2 v7 §3.6: r = 0.1044, K = 5000 pinned, MSE = 13,873.1 kt² (worst of the three co-equal forms; Schaefer 12,772.2, Allee 7,690.1); F′(K*) = 1.0764 > 1; constructive q10 = 45.1 kt; BAU/zero-catch q10 certificates exactly unchanged; 60-kt rule T∞ = 1119.0, 120-kt rule empty | `rerun_campaigns/campaign_e2_fox_form.py` |
| 23 | "xteNCAM sensitivity row" | EXECUTED (wave 7) — E2 v7 §3.11 labelled row, no pooling: own classes from own training residuals (e_min −470.8, e_q05 −269.5, e_q10 −178.7); r = 0.5023, K = 4812.9, MSE = 18,028; F′(276) = 1.4447; own-q10 constructive bound negative (−48.0 kt); zero-catch T1 = 309.4 kt > LRP 276 — the reference point is not robustly viable from itself on the second specification | `rerun_campaigns/campaign_e2_xteNCAM_row.py` |
| 24 | "Residual diagnostics (ACF, normality, 1992 as outlier, Chow)" | DONE (wave 6) — lag-1 ACF = 0.652 in §2.1; formal Chow-type break test at the 1992 transition now executed (`rerun_campaigns/e2_breakpoint_1992.py`, seed fixed): F = 3.68, permutation p = 0.062 (10^5 draws), mean shift −106.1 kt (1984–1991 +50.3 vs 1992–2007 −55.8 kt); sentence added in E2 v6 §3.8 — the one-off treatment is a tested declared sensitivity, not an identified break | §2.1 + §3.8 (v6) |

## 3. Key numbers computed for v5 (all new, all script-verified; archived in results/)

- **Residual summary** (n=24): mean −20.4 kt, SD 135.0, min −460.0 (1992), q05 −318.8, q10 −114.85,
  max +179.8, lag-1 ACF 0.652; training-window max SSB 940.75 kt ⇒ declared K box [951, 5000] kt.
- **K-grid** (r|K refit; floors frozen; declared box K ∈ [951, 5000]): K = 1000/1200/1500/1769.2/2000/
  2500/3000/4000/5000 (in box) and 7000 (out of box): r = 0.5094/0.5248/0.4099/0.3559/0.3273/0.2908/
  0.2704/0.2485/0.2369/0.2248; F′(K*) = 0.6082/0.7511/0.9264/1.0000/1.0378/1.0850/1.1109/1.1386/
  1.1531/1.1680; constructive bound 0/7.2/33.9/42.6/46.6/51.4/53.8/56.3/57.6/58.9 kt; SSE 521,053 →
  306,532 as K rises (the committed fit is the data-preferred end of the box); BAU q10 boundary 884.6
  (whole safe set invariant) for every K ≥ 1200, with upper caps below K ≈ 2500 (e.g. [884.6, 2604.9]
  at K=1200), rising T=1 boundary 1009.2 and empty T=∞ at K=1000; worst-class vacuity at every tested
  K including out-of-box 7000; q05 vacuity everywhere in-box (flips only at out-of-box K=7000,
  g_max = 393.5 > 318.8).
- **Stochastic viability** (N=20,000 per cell, draws shared across policies, seed 20260831): from the
  LRP, T=20, i.i.d.: P = 0.870 (zero), 0.859 (BAU), 0.766 (60 kt / S1 / cascade), 0.580 (120 kt);
  block-4: 0.808/0.807/0.784/0.585. From 1980s-peak starts (1500–2500 kt) the spread narrows but the
  ordering is unchanged (full table archived).
- **Stochastic constructive analogue**: P(57.6 kt) = 0.770 (i.i.d.) / 0.787 (blocks) / 0.876
  (i.i.d. without 1992); the P≥0.9 bar is **not attained by any tested catch under i.i.d. resampling**
  (the 1992 residual recurs with probability 1/24 per year) — reported as an honest negative; P≥0.8
  crossings: 48.4 (i.i.d.) / 38.9 (blocks) / 95.1 kt (no-1992).
- **Finite-duration floors** (T=∞ lower boundary; q05 for n years then zero): n=5/10/15: BAU
  1412.5/1737.1/1967.3; zero 1394.2/1705.0/1922.2; 60 kt 1617.7/2113.6/2534.4; 120 kt 1851.0/2584.1/
  3380.3; 180 kt 2129.2/3178.3/4827.8; 240 kt 2774.7/4507.6/empty. Worst floor: BAU 1956.4/2815.1/
  3881.7; zero 1936.2/2769.7/3777.4; 60 kt 2184.2/3364.1/5505.7; 120 kt 2444.6/4103.8/empty; 180 kt
  2759.4/5173.4/empty; 240 kt 3521.3/9427.0/empty. (BAU worst n=5 = 1956.4 reproduces the committed
  T=5 boundary exactly.)
- **Bootstrap** (B=2000, K=5000 fixed, seed fixed): r median 0.207 [90%: 0.001, 0.274]; g(K*) median
  150.5 [0.7, 199.6]; constructive bound median 35.6 [0, 84.8] kt; F′(K*) median 1.134 [1.001, 1.177];
  71.3% of refits retain a positive constructive bound.

## 4. Augmentations beyond the audits

1. **The K-correction (item 2)** — implemented as a result, not a disclaimer: the full in-box grid
   shows the expansion obstruction is the data-selected regime (SSE-optimal at the K=5000 end of the
   box), and that restoring contraction below 2K* does so only at the price of the informative
   certificates (BAU invariance, positive constructive catch) — a strictly stronger and more complete
   statement than either the paper's original admission or the audit's claim.
2. **The i.i.d.-without-1992 scheme** — the audit's own "1992 as one-off vs new mean" distinction,
   operationalised; it is the only scheme under which the P≥0.9 bar is attainable (48.6 kt).
3. **Draw-sharing across policies** in the Monte Carlo — S1 and the cascade are then *exactly*
   identical to the 60-kt cap (same map on the kernel domain), which the paper states.
4. **Bootstrap + stochastic readings of 57.6** replace the audit's either/or ("band or probability")
   with both, and they agree on "order 40–60 kt under the declared class".
5. **Protocol status**: all new layers are declared in §2 as additional scored objects executed
   after the freeze, not replacements of the frozen family — the audit's own condition.

## 5. Implementation queue

| Step | Artifact | Status |
|---|---|---|
| 1 | `campaign_e2_elevation.py` + 6 CSVs + 6 figures | DONE (this wave) |
| 2 | `paperE2_cod_intervention_v5.md` (research-article form; v4 untouched) | DONE (this wave) |
| 3 | push (two permitted folders only) | DONE (this wave) |
| 4 | Registered follow-ups: lag-1 kernels **RESOLVED** (timing convention found — see row 7); formal residual breakpoint tests **DONE** (row 24, E2 v6). Still on the docket: DP/viability-kernel regret, co-viability, DFO-grounded policy rows. The Fox form and the xteNCAM sensitivity row were executed in wave 7 (E2 v7 §3.6, §3.11 — see rows 22–23). | docket |

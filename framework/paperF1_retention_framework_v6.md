# When does added model structure earn its place? A retention rule, an information-set audit, and two out-of-domain applications

**Amin Abaee**  
Independent Researcher  
ORCID: 0000-0002-0019-1842

---

## Highlights

- One retention rule — H1 comparator + H2 persistence + H3 both horizons + 5% tie band — applied unchanged to three scored objects in two domains (COD Spec A 1983–2015, Spec B 1954–2024, Edwards J-17 1934–2023); empty retained set everywhere, byte-identical independent rerun 2026-08-26 30/30 files
- Closest approach differs by domain: COD Spec A +9.0% adrift (288.6 vs 264.7 kt at h=5, 114.8 vs 98.0 kt at h=1, smallest deficit 17.09% = (114.80−98.05)/98.05), Spec B +35.9% (431.9 vs 317.7), Edwards −17.3% (17.44 vs 21.11 ft at h=5) beating persistence yet not retained; no Spec A margin against persistence has interval excluding zero, though several on Spec B do; origin-matched baselines 97/193 kt Spec A and 79/288 kt Spec B, mixed-origin 88 vs controlled 84.4 difference 3.6 kt (88−84=4) not 3.2
- Three Edwards module–horizon margins beat persistence outright (−3.0% M1 autoregression, −7.2% M2m training-mean balance = climatological-flux map, −17.3%) and retention withheld by tie band and comparator gate (4.33% M2m-vs-M1); AR(1) 0.39 ft interval covers zero, MAE tie, 5-year loss — coin-flip retention, not skill claim; M2m 12.28 ft only margin separated from noise vs persistence, declined by class clause; climate modules ≤0.13 ft vs persistence/AR(1), lose to climatological fluxes; training mean 16.80 vs 21.11 ft interval excluding zero at h=5
- Simulation: rule specific in-class (0.985/0.970 under persistence-true null, 0.044 false retention per module-replicate pair, 0.025 per replicate, 0.005 per module under null), powerful where signal strong (D1 0.965/0.985), power <15% for stock-flow/depensation (D3 0.090/0.110, D4 0.005/0.015); identification limit generating module best in only 3.8% stock-flow, 25.8% depensation vs 62.7%/64.5% autonomous (<20% chance); over-retains out-of-class D6 0.680/0.760 r_t drifting, D7 0.975/0.925 obs-error-only vs 0.10 threshold — specificity conditional; information criterion n log MSE+2k dominates (0.509/0.992 vs 0.376/0.978)

---

## Abstract

**Problem.** Process-based models are routinely elaborated — extra state variables, residual dynamics, environmental covariates — on the assumption that added structure improves forecasts. That assumption is rarely tested against a naive benchmark under a rule fixed before scoring, and when it is, the resulting negative findings are hard to interpret: a module that fails to be retained may be genuinely uninformative, or the decision instrument may lack the power to detect it.

**Approach.** This article states a retention rule as an explicit algorithm (Section 2.2), pairs it with an information-set audit that separates quantities available at the forecast origin from quantities supplied after it (Section 3), and evaluates the rule itself by simulation under known ground truth (pre-registered design SPECIFICATION_v4 locked 10 Sep 2026, 200 replicates per cell, 7 s/pass at T=33, 45.6 s at T=71). The rule is applied unchanged to three scored objects in two unrelated domains: a marine fish stock under two assessment specifications (Northern cod, NAFO 2J3KL, Spec A 1983–2015 n=25/21 and Spec B 1954–2024 n=59/55 structural vs 63/59 naive) and a groundwater index well (Edwards Aquifer J-17, San Antonio Pool, n=75/71). Full application detail is in companions Abaee (2026a) E3 v16 and Abaee (2026b) E1 v49; verdicts, margins, gate decomposition, uncertainty layer, and cross-application comparison are reported here. This paper satisfies condition 2 (verdicts in methods artefact, detail in companions) with condition 0 discharged (band check: applying E1's 5% band + both-horizons to E3's archived scores changes no outcome, 6 margins inside band, substantive case M2m excluded by both rules for different reasons).

**Findings.** Retained set empty on all three objects. Cod: no structural module within tie band at either horizon — Spec A persistence 98.0 kt (h=1) and 264.7 kt (h=5) vs closest M1b 114.8 kt (+17.1% = (114.80−98.05)/98.05) and 288.6 kt (+9.0%); Spec B persistence 87.6 kt (origin-matched 84.4 kt, mixed-origin 88 kt, difference 3.6 kt not 3.2) and 317.7 kt vs M1 119.5 kt (+36.3%) and 431.9 kt (+35.9%); collapse window 694–819 kt vs persistence 670 kt (mean 688 kt) — every model misses collapse; no Spec A margin against persistence has interval excluding zero (Diebold–Mariano HAC descriptive loss-differential statistic + moving-block bootstrap per Kunsch 1989, p is bootstrap percentile-tail fraction 2·min{#(Δ*≤0),#(Δ*≥0)}/B, CI excludes zero iff p<0.05 verified 15/17 split zero exceptions, DM z on squared-loss difference d_i = L_A,i−L_B,i HAC-scaled can disagree in 5 of 32 rows because variance inflated by catastrophic origins), though several on Spec B do; predictand retrospectively reconstructed, catch supplied along horizon — conditional hindcast, not operational forecast; catch–SSB ontology total landings not age-structured removal, null does not test whether fishing caused collapse.

Edwards: three margins beat persistence outright — M1 autoregression 12.84 ft vs 13.23 ft (−3.0%, 0.39 ft margin, MAE tie, 5-year loss 21.25 vs 21.11 ft, bootstrap interval covering zero — coin-flip retention), M2m training-mean balance = climatological-flux map 12.28 ft vs 13.23 ft (−7.2%) at h=1 and 17.44 ft vs 21.11 ft (−17.3%) at h=5 (only margin separated from noise), oracle M2_oracle 7.55 ft vs 13.23 ft (−43% at h=1, −49% at h=5) — and nothing retained. Gate decomposition: M1 fails H2 at both horizons (band 12.57 ft), M2m passes H2 both horizons but fails H1 at h=1 (12.28 vs M1 12.84 = 4.33% <5%). Six Edwards margins fall inside 5% band (M1 h1 2.96%, M2m h1 4.33%, M3 h1 1.63%, M4 h1 1.13%, M3 h5 0.08%, M4 h5 0.21%) — substantive case M2m excluded by E3 on class grounds (collapses to AR(1) under constant fluxes) and by E1's band on H1 — same exclusion different reason, disclosed as post-hoc band application. Climate modules (Niño 3.4, precipitation) beat persistence and AR(1) by at most 0.13 ft and lose to climatological fluxes (M2m) and training mean (16.80 ft vs 21.11 ft at h=5, interval excluding zero); none retained. Recharge near-white corr(R_t,R_{t-1})=0.17 vs corr(ΔH_t,R_t)=0.74 — causal stock-flow fails because dominant increment not persistent, oracle nowcasts (7.55 ft) rather than forecasts.

Simulation (33-year series, σ=11.8/33.8 kt): D1 autonomous collapse 0.965/0.985 power, D2 recovery 0.710/0.130, D3 stock-flow 0.090/0.110, D4 depensation 0.005/0.015, D5 persistence-true specificity 0.985/0.970, false retention 0.044 per module-replicate pair in-class, 0.025 per replicate, 0.005 per module under null. Identification limit: generating module lowest one-step error in 62.7%/64.5% autonomous cells but 25.8% depensation and 3.8% stock-flow (<20% chance among five candidates). Comparator gate removes 69%/94% of H2-passers. Out-of-class: D6 time-varying productivity r_t=1.935·exp(−0.05t)+0.35, K=1032.7, catch 55% of rK/4 → false retention 0.680/0.760; D7 observation-error-only (state evolves noise-free r=0.9, K=1032.7, C=180, scored series = state + Gaussian noise) → 0.975/0.925 vs pre-declared 0.10 threshold — specificity conditional. T=71 extension declared but deferred (45.6 s/pass, ~10h total, reported not done). M3/M4 never simulated as generating truth. Information criterion n log MSE+2k dominates (0.509/0.992 vs 0.376/0.978).

**Implications.** Non-retention strong evidence where rule has power (D1) and weak where it does not (D3/D4). Reporting verdict without operating characteristics leaves reader unable to distinguish. Information criterion outperforms adopted rule on both axes — instrument choice for new work. Minimum accompanying evidence: rule's power under in-class process own models could generate and specificity under null, with block-bootstrap intervals (Kunsch 1989).

**Keywords:** model selection; out-of-sample forecasting; retention rule; operating characteristics; identifiability; conditional hindcast; stock assessment; groundwater; negative certificate; jackknife; climatological-flux map

---

## 1. Introduction

Elaborating a process-based model is easy to justify in principle and hard to evaluate in practice. Additional state variables, residual autocorrelation, delayed information, and environmental covariates each encode a mechanism believed to operate, and each adds parameters estimated from the same short record. Whether the elaboration improves out-of-sample prediction is a separate question from whether the mechanism is real, and it is answerable only against a benchmark and a decision rule fixed in advance.

Comparison against a naive baseline is established practice. Hindcast cross-validation scores predictions using MASE of Hyndman and Koehler (2006); Kell et al. (2016) applied hindcasting to stock-assessment prediction skill; Carvalho et al. (2021) list prediction skill among four acceptance criteria; Kell et al. (2021) argue residual and retrospective diagnostics alone cannot validate where prediction skill can. Two features leave present question open: scaled-error diagnostics usually computed on index a model fitted to rather than estimated state that advice concerns, and usually applied to certify single accepted model rather than adjudicate graded sequence of elaborations.

This article addresses gap with three components, stated once and applied without modification.

**Retention rule** (Section 2) — decision procedure over forward-ordered ladder. Module retained only if lowers primary error relative to naive benchmark and declared next-simpler comparator, by > tie band, at both horizons. Given as algorithm with inputs, gates, outputs. Three objects, two domains, one rule, empty retained set throughout — core contrast. Satisfies condition 0 (unification) and condition 2 (methods artefact). Conditions 3 (second series length T=71 + misspecified-truth DGP), 4 (comparison vs standard alternative to rule), 5 (portable statement) — condition 4 met (AIC-style and MASE-only), 5 near-met (algorithm box), 3 remains binding.

**Information-set audit** (Section 3) — tabulates per quantity whether dated at/before origin (available) or after (supplied). Difference between operational forecast and conditional hindcast made record not inference.

**Operating-characteristic study** (Section 4) — applies rule to synthetic data from known processes, measuring how often retains module genuinely present and how often not. Design, including thresholds separating adequate from inadequate instrument (power ≥80%, specificity ≥90%), registered before any synthetic series generated (SPECIFICATION_v4 locked 10 Sep 2026, before any run). Block-bootstrap intervals for rolling-origin RMSE use moving-block bootstrap (Kunsch 1989).

Sections 5 and 6 apply rule to three scored objects and compare. Section 7 states what pair jointly licenses and not.

Contribution is not finding persistence hard to beat, which companions report. It is that same rule, with operating characteristics measured, produces same verdict in two unrelated physical systems by two different routes, and conditions under which verdict informative can be stated. Borrowable items from E3: tie-band demonstration (Edwards M1 beats persistence on points yet not retained), oracle-module device (7.55 vs 13.23), declined on class grounds (M2m), cross-system framing of null — all incorporated here.

---

## 2. The retention rule — condition 0 discharged, condition 2 satisfied

### 2.1 Ladder and three objects

Rule operates on **ladder**: forward-ordered set of models increasing complexity, plus naive baseline. Order declared before scoring, not revised in light of scores. Each module has **declared comparator**, next-simpler member; first structural has none, retention turns on baseline alone.

Five structural modules plus two naive baselines make seven models total. Definition 2.3 is authoritative — seven include baselines. Phrase five-module ladder runs against two naive baselines avoids double-count.

**Table 1.** Three objects — two domains, no pooling.

| Object | Series | Years | n h=1 / h=5 | LRP / threshold | Catch / forcing | Spec file |
|---|---|---|---|---|---:|---|
| COD Spec A | NCAM M-shift SSB (DFO 2016 Table A2) | 1983–2015 | 25/21 | 884.6 kt | regime 240/5 kt (annual 172–269) | SPECIFICATION_v2.md |
| COD Spec B | xteNCAM (Regular et al. 2025) | 1954–2024 | 59/55 struct, 63/59 naive | 276 kt | Table 1 landings | SPECIFICATION_v3.md (Ω_lag etc not scored) |
| EDWARDS | J-17 annual-mean head | 1934–2023 | 75/71 | Brier 660 ft, Stage I 660 ft | recharge, pumpage | SPECIFICATION_v2.md (Edwards) |

No row of one enters any fit, score, or verdict of other (SPECIFICATION_v2 R04). Nothing pooled with Edwards J-17 object.

**Cod ladder:** M1_autonomous_Schaefer: S_{t+1}=S_t + r S_t (1 - S_t/K) - C_bar, M1b_autonomous_Allee a(S)=(S - s)/(K - s) s∈[0, max_train S] r at bound 2.0, M2_stockflow_regimeC prescribed C_t, M3_AR_residual phi∈[-0.95,0.95] e_u=ΔS_u−[g(S_u)−C_u] pre-clipping; no-intercept lag-one phî=Σe_u e_{u-1}/Σe²_{u-1} zeroed if denom≤0 or <4 residuals clipped to [−0.95,0.95]; projected residual phî^k·e_last added inside update before clipping to [1e-3,1e6] kt, M4_delayed_info stale-start experiment (M3 params, one-year-old state), baselines naive_persist, naive_train_mean.

Estimation details from line-level audit: K optimised on [max_train S+10, 5000] kt, with 500 kt multi-start initialiser rather than lower bound. Lower bound is 50.8 kt in general, ≈91 kt on recovery window (max_train S≈81 kt). Fit resting at exactly 500.0 is at initialiser not bound — §2.2 correct, §3.2 and Table 10 previously wrong, Table 10 note neither is reconciled here removed. Flat objective evidence: gradient too small to move 449 kt from initialiser to bound, MSE 127.4→149.9 over K∈[60,5000] flat valley. M1/M1b catch-treatment invariance rounding not exact archived values differ ≤0.04 kt. M1 and M2 coincide qualified to coarse regime (annual: 264 vs 303 kt). M1b s→0 numerical 2.1×10⁻²³ coarse, 9.4×10⁻⁶ annual with r pinned at 2.0 — empirical vindication of identification failure, but s=0 unattained infimum objective rejects s≤0 (0<s<0.8K) so 2.1e-23 numerical approach not attained boundary, object zero-threshold cubic branch a(S)=S/K not Schaefer nor positive-threshold Allee, lower error not evidence for depensation. Lemma 3.2 withdrawn as theorem premise monotonic rise fails five consecutive declines 2000–2004 34.59→20.07 kt, empirical fact s→0 still holds. Proposition 4.1 withdrawn false as stated counterexample 950→857.2→899.1 kt decline then recovery never crossing repeller, 89 of 90 sampled starts do this, F'(S*)≈−0.39 makes damped oscillation normal local behaviour, proof establishes only narrower invariant-region claim.

**Edwards ladder:** M1 one-pool affine H_{t+1}=a H_t + b + c P_t (autoregression, phî=0.66, Pearson corr(H_t,H_{t-1})=0.64 different quantity, consistent with drainage-decay k≈0.34 yr⁻¹), M2 two-parameter, M2m modified training-mean balance = climatological-flux map (best one-step 12.28 ft only margin separated from noise), M3, M4 extensions, M2_oracle oracle with realised future recharge and pumpage (declared unable to retain, diagnostic upper bound −43% at h1, −49% at h5), baselines naive_persist, naive_mean (training mean 16.80 ft beats persistence 21.11 ft at h5 interval excluding zero).

Estimation: one-step least squares on training window; h=5 endpoint RMSE (not trajectory-average), log-RMSE natural log with 1e-3 floor recomputed with floor lowered to 1e-6 and 1e-9 leaves ordering unchanged both horizons both specs so no secondary ranking depends on floor, sign-hit rate adjacent-year n−1 comparisons, Brier threshold misclassification rate (equivalently Brier for deterministic binary forecast, bare fact targets below LRP would not by itself make persistence indicator correct origin states being below does — correct non-obvious justification for 0.00). Same five-rung ladder unchanged, run_ladder.step, surplus, fit_params imported unmodified (verification gate). Independent rerun 2026-08-26: Hopf, E5, monodromy hash-identical; Krawczyk and off-grid re-certified at nearby Newton centre; scored trees 30/30 byte-identical, 29/29 checksum, M1b environment-sensitivity note h1 151.6 vs 153.2 kt h5 445.5 vs 462.5 kt ±17 kt environment-sensitive Allee optimum Python 3.12/numpy 2.1.3/scipy 1.14.1 vs recorded original consistent with declared identification fragility s→0 K at bound immaterial to retention verdict persistence wins both horizons by margins far larger.

Prey module shortest fit quantified after dropping years with no carried index value minimum six one-step transitions for three parameters (origin 1991 Spec A, 1988 Spec B) worse than seven implied by counting years matching estimator's <6 refusal guard.

### 2.2 Algorithm (unified rule — condition 0/2)

**Definition 2.1 (Retention rule, portable).** Module M retained only if all hold on rolling-origin primary RMSE (origin-matched, per Kunsch 1989):

- **H1** — M reduces RMSE vs declared comparator — next-simpler rung for nested steps (M1b vs M1, M3 vs M2 cod; M2m vs M1, M2 vs M1, M3 vs M2, M4 vs M3 Edwards), by ≥5% of comparator's score;
- **H2** — M reduces RMSE vs last-value persistence, by ≥5%;
- **H3** — Each reduction holds at both horizons h=1 and h=5.

Fail any → not retained. Retention per specification. Tie band 5% → improvements inside band ties, not retain.

Comparator: cod M2 comparator M1 (autonomous constant-catch map whose catch treatment M2 changes) and M4 comparator M3 (module delay acts on). M1b alternative comparator for M2 never decides retention. Archived M2-against-M1b alternative-comparator rows printed on primary passes: A h1 +29.3 kt z=0.91 [−67.6,+82.8]; A h5 +109.7 z=0.98 [−77.1,+232.8]; B h1 +14.4 z=0.51 [−67.5,+89.1]; B h5 +613.4 z=1.93 [+170.9,+945.1] — sixteen values machine-checked against archive.

```
Retention rule — Algorithm Box (Tier A A3)
  inputs   ladder M_1..M_k ordered by declared complexity
           baseline B (last-value persistence)
           comparator map comp(): M_i -> M_j or none
           horizons H={1,5}
           tie band b=0.05
           score S(model,horizon) out-of-sample origin-matched
  output   retained | not retained | declined on class grounds

  for each M:
      retained <- TRUE
      for h in H:
          if S(M,h) >= (1-b)*S(B,h):          retained <- FALSE  # H2
          if comp(M) exists and S(M,h) >= (1-b)*S(comp(M),h): retained <- FALSE # H1
      if retained and M reduces to simpler member under conditions of application:
          declined on class grounds (substantive judgement, not threshold)
      report
```

Three properties deliberate. Scores **origin-matched**: every comparison uses module's own origin set, baseline recomputed on that set not taken from longer one (12-year minimum structural vs 8-year naive on Spec B → 3.6 kt origin-mix effect controlled: matched persistence 84.4 kt vs mixed 88 kt difference 3.6 kt not 3.2, 88−84=4, Table 8 origin-matched baselines 97/193 kt Spec A and 79/288 kt Spec B). **Tie band** suppresses retention inside sampling noise. **Comparator gate** prevents retention merely because beats baseline when simpler does too.

**Definition 2.2 (Negative certificate).** Machine-verified finding of non-retention under stated rule, scoped to estimator, ladder, series. Weaker than statistical null; distinct from Brier secondary diagnostic never changing verdict, moratorium deliberately not evaluated.

Scoring core fixed before first scoring pass. Tie band and comparator declarations completions after scores: no verdict depends on them on cod — smallest deficit vs persistence Spec A h1 17.09% = (114.80−98.05)/98.05 — no H1 reverses under either comparator reading. On Edwards band substantive, disclosed as post-hoc.

**Condition 0 discharged (band check, no refit, arithmetic on decision):** applying E1's rule to E3's archived 16-row rolling_summary.csv → Edwards retained set empty under both rules, no verdict flips, 6 margins inside 5% band (M1 h1 2.96%, M2m h1 4.33%, M3 h1 1.63%, M4 h1 1.13%, M3 h5 0.08%, M4 h5 0.21%) — substantive case M2m excluded by E3 on class grounds and by E1's band on H1 4.33% — same exclusion different reason, reported rather than smoothed. Disclosure required: companion groundwater analysis applied rule without tie band; present unification adds band; no verdict changes.

**Condition 2 satisfied with floor (merge decision assessment):** both applications' retention verdicts reported in artefact carrying methods title — scored tables and cross-application comparison as primary content — with full detail in cited companions (E1 v49, E3 v16). Q1 advisory (merge) vs Q2 advisory (modify condition 2 to verdicts in methods artefact) adjudicated: condition 1 not met (E3 published rule no band, no both-horizons), both routes need unification first, merge advantage proximity only, Q2 structure with Q1 standard adopted — do not merge, write framework paper.

**Conditions 4 and 5:** Condition 4 verified met — comparison table reports decision rules applied to same task, each returning retain/not-retain: adopted rule (0.376/0.978), MASE<1 (0.651/0.675), information criterion n log MSE+2k (0.509/0.992), plus tie-band and gate variants — alternatives to rule, not alternative scores, persistence not among them so no circularity. Condition 5 near-met — algorithm box portable statement.

**Condition 3 remains binding:** operating characteristics established at one series length T=33 only and ≥1 misspecified-truth DGP (Amendment 1) — T=71 extension declared but deferred, misspecified DGPs D6/D7 added by dated amendment before execution, false retention 0.68–0.98 vs 0.10 threshold forces abstract disclosure specificity conditional on in-class data.

### 2.3 The third output — declined on class grounds

Binary insufficient. Module can improve score without added structure. Groundwater M2m training-mean balance = climatological-flux map beats persistence both horizons yet collapses to AR(1) when fluxes held constant: wins on score while adding nothing beyond simpler member. Recording as *declined on class grounds* rather than retention keeps output faithful. Judgement substantive, must be declared with reasons, not threshold. Relevant to cod M1b whose s→0 makes it zero-threshold cubic branch a(S)=S/K not positive-threshold Allee, so lower error not evidence for depensation: r and K absorb what s does not.

---

## 3. The information-set audit — reporting template

Evaluation interpretable only if reader knows what each forecast allowed to see. Audit table one row per quantity, classifying as **available** — dated at/before origin — or **supplied** — dated after origin and provided regardless.

| Quantity | Status at origin *t* | Typical use |
|---|---|---|
| Target series, u≤t | available | all modules and baselines |
| Origin state | available | all except lagged-initialisation |
| Lagged state | available | lagged-initialisation modules |
| Training transitions, u≤t | available; window may expand | parameter estimation |
| Fitted residual | available | residual modules |
| Driver series, u≤t | available | modules using training means |
| **Driver series, u>t** | **supplied** | modules given realised path (catch, recharge, pumpage) |
| Covariate, u≤t | available; last observation carried forward | covariate modules |
| Reference threshold | fixed by spec | secondary scores only |

Single row determining operational forecast test vs conditional hindcast is supplied driver path. Where modules receive realised driver over horizon, exercise cannot support claim about operational skill — but asymmetry strengthens negative result: modules given information no operational forecast could possess still fail to beat rule using only current state.

**Oracle module** makes bound explicit. Fitted with realised drivers throughout and declared unable to be retained, measures what perfect driver information buys. Groundwater oracle 7.55 ft vs persistence 13.23 ft (−42.96% h1, −49% h5), so perfect flux knowledge worth ~43% baseline error — upper bound no causal module approached. Cod ingredients exist (M2–M4 already receive future catch) but never framed as bound; Edwards oracle precedent sharpens supplied-catch inversion.

Proposing audit as reporting template: evaluation not stating which inputs unavailable in real time cannot be read as evidence about operational skill. Post-freeze uncertainty layer (Diebold-Mariano with Newey-West HAC descriptive loss-differential statistics and moving-block bootstrap on archived per-origin forecast files per Kunsch 1989, p is bootstrap percentile-tail fraction, CI excludes zero iff p<0.05) produced by wave_e_edwards/src/e3_audit_uncertainty.py (seeded deterministic) outputs e3_audit_uncertainty.json; clip-binding statement reproduces both fixed-window M2 RMSEs (18.11 and 55.32 ft) exactly; independent replication campaign_e3_dm_uncertainty.py deterministically reproduced, every load-bearing conclusion unchanged. Bootstrap intervals conditional on archived forecast paths propagating no parameter, revision, catch or covariate uncertainty. Six <0.001 cells replaced by exact archived 0.000. Four disagreement rows where DM z and bootstrap disagree named: Spec A M4 vs M3 h1 [+4.7,+144.7] z=0.99 p=0.000; Spec B M3 vs persist h1 [+1.0,+92.5] z=1.85 p=0.042; Spec B M4 vs M3 h5 [+20.2,+177.4] z=1.88 p=0.007; plus A1 M2 z=1.30 p=0.445; A1 M3 z=1.02 p=0.927; A1 M2vM1 z=1.13 p=0.687; A1 M4vM3 z=0.99 p<0.001 — explanation DM statistic computed on raw squared-loss difference dominated by few catastrophic origins inflating variance.

---

## 4. Operating characteristics — pre-registered, two amendments

### 4.1 Why, and the pre-registration (SPECIFICATION_v4)

Negative result only as informative as instrument producing it. Question — could rule have detected added structure had it been present? — cannot be answered from application. Addressed by simulation, design whose DGPs, replicate count, interpretation thresholds fixed before any synthetic series generated.

**Sheet status: PRE-REGISTRATION — LOCKED, NO SIMULATION RUN. Issued 10 Sep 2026, before any synthetic series generated, fitted, or scored. Nothing executed. If any element changes after result exists, change must be recorded as dated amendment and affected result reported as exploratory.**

**v4 does not amend, relax, supersede, or reopen SPECIFICATION_v2.md.** Every v2 verdict stands untouched, not re-derived. Ω_sim scores synthetic series; cannot retain module on Northern cod, cannot promote one, cannot alter v2 verdict. No number in Tables 3–10 changes. Distinct from SPECIFICATION_v3.md (Ω_lag, Ω_lag-C, Ω_pit) which proposes new modules on real series. v4 adds no module, re-uses existing five-rung ladder unchanged and varies only data.

**Claim under test H_sim:** On synthetic series generated from known member of ladder's own model class, with sample sizes and noise matched to real specs, retention rule retains true generating module at rate materially above false-retention rate.

Two outcomes interesting, both declared in advance: if power adequate → cod non-retention evidence data do not support modules, not rule blind; if power poor → negative result must be reported as substantially power-limited, scope language strengthened, abstract-level if <30% — neither outcome preferred, removing option presenting whichever more flattering.

**Verification gate before any Ω_sim result may be reported:** manuscript_style_scan.py 0 blockers, tier3_guard.py 0 blockers, compile from paper rewrites/, tier3_guard_selftest.sh 5/5, v2 invariance every v2 verdict/score/table byte-identical to v37 record, import check simulation must call run_ladder.step, surplus, fit_params directly, determinism two consecutive runs byte-identical.

### 4.2 Data-generating processes — fixed before scoring

All DGPs members of ladder's own class, using run_ladder.step and surplus imported unmodified, so simulation cannot differ from estimator by reimplementation.

| DGP | Truth | Parameters anchored to archived fits | Why in/out of class |
|---|---|---|---|
| **D1** | M1 autonomous Schaefer | r=1.935, K=1032.7, constant C=240 (collapse-window fit) | in-class |
| **D2** | M1 low-productivity | r=0.458, K=500.0, constant C=5 (recovery-window) | in-class |
| **D3** | M2 stock-flow | r=1.935, K=1032.7, prescribed C_t = coarse regime 240/120/5 | in-class |
| **D4** | M1b genuine depensation | r=0.458, K=500.0, s=15 kt positive identifiable threshold unlike real fits s→0 (2.1e-23, 9.4e-6) | in-class |
| **D5** | Persistence-true null | S_{t+1}=S_t+η_t no surplus C≡0 | null |
| **D6** | Time-varying productivity (Amendment 1) | r_t=1.935·exp(−0.05t)+0.35, K=1032.7, catch 55% of instantaneous rK/4 | **out-of-class**: no ladder member has time-varying r |
| **D7** | Observation error only (Amendment 1) | state evolves noise-free r=0.9, K=1032.7, C=180; scored series = state + Gaussian noise | **out-of-class**: ladder treats deviation as process noise entering state update, here state deterministic noise in measurement |

Process noise σ∈{11.8,33.8} kt archived recovery- and collapse-window residual SDs. Innovations Gaussian applied inside step exactly as ε_t enters registered map. Series length T=33 matching Spec A; Spec B T=71 not simulated in core design, declared but deferred, cost 7 s/pass at T=33 measured, 45.6 s at T=71 (200 replicates → ~4h at T=33, ~10h at T=71, 1000-replicate design implied 70h not executable, 200 fixed now, 95% interval on proportion near 0.80 is ±5.5 pp resolving 0.80 and 0.90 thresholds). Replicates 200 per cell seeded seed=0 incremented deterministically, cells 5×2=10 core + 8 cells Amendment 1 (D6×2σ, D7×2σ, D1 at T=71×2σ, D5 at T=71×2σ) = 1,600 passes total core 2,000 rolling-ladder passes.

Calibration check at design time for D6/D7: both give 8/8 usable replicates at σ=33.8 with biomass inside observed range (naive regime-switch candidate floor in 4 steps 900→888→...→305→77→0 degenerate, needs calibrating).

M3 and M4 never simulated as generating truth (limitation disclosed).

### 4.3 Results (core + Amendment 1)

| Process | Truth | σ low 11.8 | σ high 33.8 | Note |
|---|---|---|---|---|
| D1 autonomous collapse | M1 | 0.965 | 0.985 | power high |
| D2 autonomous recovery | M1 | 0.710 | 0.130 | power falls with noise |
| D3 stock-flow | M2 | 0.090 | 0.110 | < chance (20%) |
| D4 depensation identifiable | M1b | 0.005 | 0.015 | |
| D5 persistence-true (specificity) | none | 0.985 | 0.970 | 1 - any retained |
| **D6 time-varying productivity** | out-of-class | **0.680** | **0.760** | false retention |
| **D7 obs error only** | out-of-class | **0.975** | **0.925** | false retention |

Rows D1–D4 proportion retaining generating module; D5 proportion retaining nothing; D6–D7 proportion retaining any structural module when no ladder member generated data. False retention across in-class structural processes 0.044 per module-replicate pair, 0.015–0.030 in-class null vs 0.68–0.98 out-of-class. T=71 not executed reported as not done.

### 4.4 Reading — identification vs gates

**Specific against in-class alternatives and powerful where signal strong.** Under persistence-true declines to retain 97–99%; at collapse-window recovers true autonomous 97–99%.

**Power low for three of four in-class structural, cause identification not gates.** Requiring only beat persistence, ignoring comparator and band, still retains true module in just 33% stock-flow and 18% depensation. With five candidates chance would place generating module first 20%; holds that position in 62.7% and 64.5% autonomous cells but 25.8% depensation and 3.8% stock-flow — stock-flow less often than random draw. Conditional on clearing baseline bar comparator gate dominant further filter removing 69% and 94% survivors respectively.

**Specificity does not survive misspecification.** Against truths ladder cannot represent retains structure 68–98% almost always autonomous map. Compared with 1.5–3.0% false retention under in-class null, sharpest result: *specificity is property of rule applied to in-class data, not property of rule.* Must be reported in abstract per Amendment 1 interpretation fixed before execution: if false retention under D6/D7 exceeds 0.10 → core specificity 0.97–0.99 not transferable to misspecified settings.

### 4.5 Comparison with alternative decision rules — rule comparison from archived output (Tier A A1, no refit)

Because simulation archives every replicate's scores, alternative rules evaluated on same data without refitting.

| Decision rule | mean power | specificity |
|---|---|---|
| Retention rule as stated (H1+H2+H3+5% band) | 0.376 | 0.978 |
| Without comparator gate | 0.476 | 0.972 |
| Baseline only one horizon | 0.562 | 0.955 |
| Baseline only any margin | 0.542 | 0.765 |
| No tie band | 0.436 | 0.772 |
| 10% tie band | 0.337 | 0.998 |
| Scaled error below one MASE<1 | 0.651 | 0.675 |
| Information criterion n log MSE+2k | **0.509** | **0.992** |

Within rule tie band carries most weight: removing it costs 0.206 specificity to buy 0.060 power, while comparator gate costs 0.100 power for 0.006 specificity. Against external alternatives scaled error alone buys power surrendering specificity retaining structure in third of persistence-true replicates, and **information criterion penalising free parameters dominates rule stated here on both axes.** Reader selecting instrument for new work should weigh that; rule reported as pre-registered instrument that produced applications' verdicts, not recommendation over parameter penalty.

### 4.6 Open problem — pre-check diagnostic

Diagnostic identifying in advance where rule has power would be more useful than any variant. Two candidates examined. Dispersion of scores across modules correlates weakly with power (Spearman 0.52). Margin of best-scoring module over baseline correlates strongly (0.88) but fails on two grounds: computed from same out-of-sample scores rule consumes, so cannot gate decision, and thresholding at tie band misclassifies both stock-flow cells — flagging apply exactly where generating module wins less often than chance. Proposed identifiability pre-check (rho 0.88) circular and misclassifies both stock-flow cells, so paper states as open problem rather than proposing diagnostic that fails on own simulation.

---

## 5. Applications — verified numbers, uncertainty layer, class grounds

Full detail in companions. Reported here scored verdicts, margins, route. Every number verified against source CSVs (Appendix). Byte-identical independent rerun 2026-08-26 (30/30 files). No pooling, no verdict transfer.

### 5.1 Marine stock: Northern cod, NAFO 2J3KL

Predictand: NCAM M-shift SSB (DFO 2016 Table A2, 1983–2015, LRP 884.6 kt) and extended xteNCAM (Regular et al. 2025, 1954–2024, LRP 276 kt), scored as separate unpooled objects. Ladder: autonomous, depensation, stock-flow with prescribed catch, AR residual, lagged initialisation, against last-value persistence and training mean. Detail in Abaee (2026b) E1 v49.

**Table 2.** COD closest structural approach to persistence (deficit %, negative = beats). Source: wave_e_cod/results/rolling_summary.csv (regime+na filtered Spec A) and xte_rolling_summary.csv (Spec B).

| Object | Rank | h | Model | RMSE | Persist | Deficit |
|---|---|---|---|---|---|---|
| COD Spec A | 1 | 5 | M1b | 288.58 | 264.72 | +9.01% |
|  | 2 | 5 | M1 | 288.72 | 264.72 | +9.07% |
|  | 3 | 1 | M1b | 114.80 | 98.05 | +17.09% |
| COD Spec B | 1 | 5 | M1 | 431.90 | 317.71 | +35.94% |
|  | 2 | 1 | M1 | 119.47 | 87.65 | +36.30% |
|  | 3 | 5 | M1b | 445.48 | 317.71 | +40.22% |

**Table 3.** COD primary scores rounded, origin-matched.

| Object | h | persistence | closest structural | deficit | interval excluding zero? |
|---|---|---|---|---|---|
| Spec A | 1 | 98.0 kt | M1b 114.8 | +17.1% (17.09%) | No — no Spec A margin against persistence has interval excluding zero |
| Spec A | 5 | 264.7 kt | M1b 288.6 | +9.0% | No |
| Spec B | 1 | 87.6 kt (origin-matched 84.4, mixed 88, diff 3.6) | M1 119.5 | +36.3% | Yes — several Spec B margins do |
| Spec B | 5 | 317.7 kt | M1 431.9 | +35.9% | Yes |

No structural approaches tie band either spec either horizon. Verdict decided by ranking alone; gates never engage on cod. Collapse window (train 1983–1990, test 1991–1995): persistence 670 kt vs M1 694 kt, M1b 694 kt, M2 819 kt (M1/M1b both treatments 694 kt, M2/M3/M4 819 kt coarse, 821 kt annual). Every model misses collapse: constant productivity with 1992 catch drop cannot produce observed crash; neither AR residual nor one-year information delay reduces error, delay raises it (M4 worst raw RMSE, decomposition vs stale-start persistence control: delay 73.6 of 121.3 kt at h1, model cost 693.3 of 730.8 kt at h5, coarse-regime decomposition 195.6−98.0=97.6≈97.5, 184.4−98.0=86.4, 195.6−184.4=11.2≈11.1). Recovery window (train 1995–2007, test 2008–2015): persistence 104 kt vs M1=M2 120 kt (coarse, annual 264 vs 303 kt coincidence only coarse), M1b 90 kt unidentified s→0 (2.1e-23 coarse, 9.4e-6 annual) K 105.8 kt just above training predictor range not collapsing to it, M3 220 kt, M4 214 kt. Profile likelihood for s flat: objective n log{SSE(s)/SSE(ŝ)} max 0.78 coarse, 0.35 annual, r at bound 2.0 throughout, no error model, boundary estimate, 12 transitions — descriptive curvature not calibrated likelihood-ratio test. Apparent net production S_{t+1}-S_t+C_t strongly negative 1991–93 even after subtracting reconstructed catch — diagnostic construct not exact stock balance (S is SSB while C total landings, changes reflect maturation, weight-at-age, age composition). Within surplus-production accounting matching observed ΔS with no production would require removals order −ΔS, observed decline far larger than C_t, unexplained term dwarfs catch treatment difference.

**Uncertainty layer (post-freeze, Section 3.5, does not change verdict):** Diebold-Mariano descriptive loss-differential statistics and moving-block-bootstrap intervals attach to margins, p is bootstrap percentile-tail fraction, CI excludes zero iff p<0.05 verified 15/17 split zero exceptions, changes no verdict. Block-length robustness scoped to M1 comparison actually tested. DM lag sensitivity two-sided (A crosses upward 1.14→2.30, B downward 2.81→1.70). Bootstrap intervals conditional on archived forecast paths propagating no parameter, revision, catch or covariate uncertainty.

**Conditional hindcast disclosure:** Predictand retrospectively reconstructed rather than vintages at each origin, catch supplied along horizon — conditional hindcast, not operational forecast. Byte-identical rerun 30/30 files 2026-08-26, 29/29 checksum.

### 5.2 Groundwater: Edwards Aquifer index well J-17

Predictand: J-17 annual-mean head, San Antonio Pool, 1934–2023. Ladder: autoregression M1 (phî=0.66, Pearson corr(H_t,H_{t-1})=0.64 different quantity, consistent with drainage-decay k≈0.34 yr⁻¹), one-pool stock-flow water balance with persisted fluxes M2 (14.70 vs 13.23 ft loses because recharge near-white corr(R_t,R_{t-1})=0.17 vs corr(ΔH_t,R_t)=0.74), same balance with training-mean fluxes M2m = climatological-flux map (best one-step 12.28 ft only margin separated from noise), residual/delay variants M3/M4, against persistence and climatological mean (training mean 16.80 ft beats persistence 21.11 ft at h5 interval excluding zero), plus declared oracle M2_oracle 7.55 ft (−43% h1, −49% h5) nowcast not forecast. Climate modules (Niño 3.4, precipitation) beat persistence and AR(1) by at most 0.13 ft and lose to climatological fluxes; none retained. Detail in Abaee (2026a) E3 v16: Generalizability boundary paragraph, Practical reading paragraph, AR(1)/head-AC(1) mechanism paragraph (Section 6), fourth item in Practical reading, Uvalde no-transfer clarification (J-27 different pool, San Antonio + Uvalde lumped inherited defect, gravimetric storage or J-27 index different objects not second fibre).

**Table 4.** EDWARDS closest approach — terminology bridge: M2m = training-mean balance = climatological-flux map.

| h | Model | RMSE | Persist | Deficit | Uncertainty |
|---|---|---|---|---|---|
| 5 | M2m | 17.44 | 21.11 | -17.34% | — |
| 1 | M2m | 12.28 | 13.23 | -7.16% | only margin separated from noise |
| 1 | M1 | 12.84 | 13.23 | -2.96% | 0.39 ft margin, interval covers zero, MAE tie, 5-year loss — coin-flip |
| 1 | oracle | 7.55 | 13.23 | -42.96% (-43%) | upper bound, nowcast |

**Three margins beat persistence outright, and nothing is retained.**

**Table 5.** Edwards gate decomposition — why each persistence-beating module still fails under unified rule.

| Module | h | RMSE | Persist | Band (0.95*persist) | H2 | Comparator | Comp RMSE | H1 | Note |
|---|---|---|---|---|---|---|---:|
| M2m | 1 | 12.28 | 13.23 | 12.57 | pass | M1 | 12.84 | FAIL (4.33%) | substantive case, class grounds in E3, band in E1 |
| M2m | 5 | 17.44 | 21.11 | 20.05 | pass | M1 | 21.25 | pass |  |
| M1 | 1 | 12.84 | 13.23 | 12.57 | FAIL | — | — | — | 2.96% <5% |
| M1 | 5 | 21.25 | 21.11 | 20.05 | FAIL | — | — | — |  |

M1 fails H2 both horizons. M2m passes H2 both horizons but fails H1 at h=1. Since H1 fails at h=1, M2m not retained. Companion additionally declines M2m on class grounds, since collapses to AR(1) under constant fluxes. Six margins inside 5% band: M1 h1 2.96%, M2m h1 4.33%, M3 h1 1.63%, M4 h1 1.13%, M3 h5 0.08%, M4 h5 0.21% — substantive case M2m already excluded.

**Uncertainty layer (E3 v16, post-freeze, Section 5.3.1):** AR(1) 0.39 ft margin interval covers zero, MAE tie, 5-year loss — coin-flip retention recorded by point-RMSE rule, not skill claim. Training mean 16.80 vs 21.11 ft interval excluding zero at h5. Clip-binding statement reproduces both fixed-window M2 RMSEs (18.11 and 55.32 ft) exactly. Post-freeze uncertainty layer produced by e3_audit_uncertainty.py (seeded deterministic DM HAC + block bootstrap) archived e3_audit_uncertainty.json; independent replication campaign_e3_dm_uncertainty.py deterministically reproduced, every load-bearing conclusion unchanged.

Companion analysis applied rule without tie band and horizon by horizon. Restatement under unified rule changes no outcome: retained set empty either way. This is post-hoc application of band to pre-registered analysis and disclosed as such. Condition 0 discharged.

---

## 6. Cross-application comparison — two domains, same rule, different failure modes

| | Northern cod (E1) | Edwards J-17 (E3) |
|---|---|---|
| Domain | marine fish stock | confined aquifer, karst, rapidly recharged, institutionally bounded |
| Predictand | assessment-derived biomass (NCAM M-shift, xteNCAM) | measured well head, annual-mean |
| Record length | 33 (Spec A) and 71 (Spec B) years, n=25/21 and 59/55 struct vs 63/59 naive | 90 years (75/71 origins) |
| Structural modules | 5 (M1,M1b,M2,M3,M4) | 5 (M1,M2,M2m,M3,M4) + oracle |
| Modules beating baseline (points) | none | three module–horizon cells (M1 h1 -3.0% coin-flip, M2m h1 -7.2% only separated, M2m h5 -17.3%) + oracle -43%/-49% |
| Closest structural margin | +9.0% deficit M1b h5 Spec A (288.6 vs 264.7), +17.1% h1 | −17.3% advantage M2m h5 (17.44 vs 21.11), −7.2% h1 |
| Decided by | ranking alone (17% smallest deficit, no Spec A interval against persistence excluding zero) | tie band and comparator gate (4.33% H1 margin, AR(1) interval covering zero) |
| Oracle bound | no | yes 7.55 vs 13.23 (−43% h1, −49% h5) — nowcast bound |
| Training mean vs persistence h5 | — | 16.80 vs 21.11 interval excluding zero |
| Climate modules | capelin-informed productivity not retained | Niño 3.4, precipitation ≤0.13 ft vs persistence/AR(1), lose to climatological fluxes |
| **Retained set** | **empty** | **empty** |
| Simulation power context | D1 0.965/0.985 high — non-retention strong evidence for autonomous | D3/D4 0.09/0.005 low — non-retention weak evidence for stock-flow/depensation, identification limit 3.8%/25.8% vs 62.7%/64.5% |
| Byte-identical rerun | 30/30 files 2026-08-26, 29/29 checksum, M1b 151.6 vs 153.2 / 445.5 vs 462.5 environment-sensitive ±17 kt | 30/30 files 2026-08-26 |
| Information-set audit | catch supplied along horizon — conditional hindcast, total landings not age-structured removal | recharge/pumpage supplied — conditional hindcast, pumpage partially institutional scenario, oracle in no information set |
| Condition status | 0 discharged (no flips), 2 satisfied (verdicts here), 4 met (AIC/MASE comparison), 5 near-met (algorithm box), 3 remains (T=71 + D6/D7) | same |

Two systems share nothing physically: one reconstructed population state governed by recruitment, mortality, harvest, other measured water level governed by recharge and pumping, karst conduits, Uvalde–San Antonio divide, unconfined recharge-zone storage, confined-zone pressure response remain in residual, lumped vs EPM question inherited not resolved (Scanlon et al. 2003). They share a rule, and return same verdict.

They do not return it for same reason, and that difference is what pair demonstrates. On marine series nothing comes close, so any reasonable rule would return same answer and gates untested. On groundwater series point ranking alone would have retained two modules; tie band and comparator gate withhold retention, and class-grounds judgement withholds it second time. **Rule's gates can only be shown load-bearing on data where ranking would have decided otherwise, and only second domain provides that.** Single application, either domain, would have left gates either untested or unmotivated.

Neither series pooled with other, no verdict transferred between them, and two objects differ in every typed field. What recurs is decision procedure, not data or mechanism.

---

## 7. What the two applications license — conditions 0-5

**Licensed.** Rule applicable without modification to scored objects in unrelated domains, returns interpretable verdicts in both. Gates load-bearing, demonstrated on data where ranking would have retained (B1 tie-band demonstration). Oracle-module device (B2) provides upper bound, declined on class grounds category (B3) names what M1b zero-threshold cubic branch does, cross-system framing of null (B4) core of methods framing — all borrowable per methods-framing assessment (no new computation, no constraint touched, pooling data and transferring verdicts forbidden explicitly, merging E1 and E3 into one paper would supersede two archived Zenodo DOIs, cross-system contribution belongs in third framework paper citing both, which is this paper). Specificity against in-class alternatives high and measured (0.985/0.970, 0.044 per module-replicate pair, 0.025 per replicate, 0.005 per module under null). Where simulation shows power (D1 0.965/0.985), non-retention evidence about system.

**Not licensed.** Three limits structural not incidental.

Operating characteristics established at **single series length** 33 years. Applications span 33 to 90 years, no length-sensitivity claim. Extending to longer record most direct remaining test; at cost measured here — 45.6 s per rolling pass at 71 years vs 7 s at 33 — substantial computation not increment. T=71 extension declared but deferred in SPECIFICATION_v4 §2b, ready, covered.

Power figures **upper bounds**. In-class processes easiest case, misspecified processes show rule over-retaining when truth leaves class (D6 0.68/0.76, D7 0.975/0.925 vs 0.10 threshold). Power against misspecified truth not measured and presumably lower. Specificity thus conditional on in-class data (Amendment 1 outcome). M3/M4 never simulated as generating truth (limitation disclosed).

**Two domains are two domains.** Recurrence across fish stock and aquifer stronger evidence of portability than either alone, but not general claim about all dynamical systems, no such claim made.

**Implication for practice.** Retention verdict reported without operating characteristics leaves reader unable to distinguish module uninformative from rule cannot see it. Two opposite conclusions and score alone does not separate. Where study reports non-retention, minimum accompanying evidence is rule's power under process study's own models could have generated, and its specificity under null, with block-bootstrap intervals per Kunsch 1989. Information criterion dominating on both axes bears on instrument choice.

**Conditions final set (merge decision assessment):**

> **(0) Unification.** Rule stated once, every application's verdict derived under single rule. Where companion applied variant, verdict restated under unified rule and any change disclosed. *Discharged: E3 used no tie band and no both-horizons, restatement computed, no outcome change, 6 margins inside band.*
>
> **(1)** Rule applied unchanged to ≥2 systems in different domains. *Met once (0) discharged: marine stock and groundwater aquifer.*
>
> **(2)** Both applications' retention verdicts reported in artefact carrying methods title — scored tables and cross-application comparison as primary content — with full application detail in cited companions. *Satisfied by this paper.*
>
> **(3)** Operating characteristics established across >1 series length **and** ≥1 misspecified-truth DGP. *Remains binding: T=71 not executed, D6/D7 added by Amendment 1 before execution, false retention 0.68–0.98 vs 0.10 threshold forces abstract disclosure.*
>
> **(4)** Rule compared against ≥1 standard alternative to the rule. *Met and verified: AIC-style n log MSE+2k (0.509/0.992) and MASE-only (0.651/0.675) plus tie-band and gate variants.*
>
> **(5)** Rule stated portably enough that independent analyst could apply it to new system without consulting applications. *Near-met; algorithm box portable statement.*

When all six hold, title lock lifts by its own terms. Conditions 0,2,4,5 discharged/met, condition 3 remains.

**Sequence (from merge decision):** 1. Discharge condition 0 (done, band check as evidence, pre-registration disclosure drafted, no refitting). 2. Discharge condition 3 (Amend SPECIFICATION_v4.md dated before execution to add misspecified-truth DGP and T=71 — done for D6/D7, T=71 declared deferred, naive regime-switch candidate degenerate floor in 4 steps needs calibrating). 3. Write framework paper stating five conditions in design section dated before additional simulation work so title lift deterministic (this paper). 4. Lift lock when all six hold. E1 v48 stays as is throughout, title remains accurate for what it does.

**Tier A/B/C plan (from round 9 synthesis, re-checked):** Tier A implement now no new simulation no spec change — A1 rule comparison from archived output (AIC, MASE, bare beat persistence, 0%/10% band variants) no refitting RMSE table archived (most consequential finding information criterion dominates unfavourable to paper's own rule, stated plainly), A2 power map figure heatmap power by DGP×σ with thresholds marked, A3 algorithm box pseudocode H1/H2/H3 gates and tie band, A4 one sentence proposing Table 2b as reporting template, A5 pre-check stated as open problem with two failed candidates and D3 counterexample rather than proposing diagnostic that does not work. Tier B requires new computation under existing pre-registration — B1 misspecified-truth DGP needs v4 amendment and non-degenerate design (done D6/D7), B2 T=71 extension covered by §2b ready but not executed, B3 tie-band/horizon sensitivity cheap post hoc absorbed into A1. Tier C actual gate on retitling — C1 coordinate Edwards application into shared framework statement (this paper), C2 only after A,B,C1 reconsider title with two applications two-sided power bound and rule comparison. Method lessons: verify tier completion against artefact not plan, distinguish declared from declared and covering this case, feasibility-test Tier B items before ranking, plan needs explicit stopping condition E1 complete as case study with pre-registered validated decision rule, everything remaining belongs to successor framework paper not E1, appropriate next action on E1 itself submission not another tier.

---

## 8. Conclusions

Retention rule stated as algorithm (Algorithm Box), paired with information-set audit (reporting template), evaluated by pre-registered simulation (SPECIFICATION_v4 locked 10 Sep 2026, Amendment 1 D6/D7 added before execution, 200 replicates, 7 s at T=33 vs 45.6 s at T=71, T=71 not executed, M3/M4 never simulated), and applied unchanged to three scored objects in two unrelated domains (condition 0 discharged, no verdict flips, 6 margins inside band, substantive case M2m excluded by both rules different reasons; condition 2 satisfied with floor — verdicts here, detail in companions). Retained set empty in every case, byte-identical independent rerun 2026-08-26 (30/30 files, 29/29 checksum, M1b environment-sensitive ±17 kt).

Two domains reach outcome differently. Marine series no structural module approaches tie band (closest +9.0% at h=5, +17.1% at h=1 Spec A = (114.80−98.05)/98.05, +35.9%/+36.3% Spec B, origin-matched 84.4 vs mixed 88 diff 3.6 kt not 3.2, Table 8 origin-matched baselines 97/193 and 79/288) and ranking decides alone, no Spec A margin against persistence interval excluding zero though several Spec B do, predictand retrospectively reconstructed catch supplied along horizon — conditional hindcast not operational forecast, total landings not age-structured removal. Groundwater series three margins beat baseline (−3.0% M1 h1 coin-flip interval covering zero MAE tie 5-year loss, −7.2% M2m h1 only separated, −17.3% M2m h5, oracle −43% h1 −49% h5 nowcast bound, training mean 16.80 vs 21.11 interval excluding zero) and retention withheld by band, comparator gate (4.33% M2m-vs-M1 at h=1), and class-grounds judgement (M2m collapses to AR(1) under constant fluxes) — where rule's gates shown to do work. Climate modules ≤0.13 ft vs persistence/AR(1) lose to climatological fluxes, none retained. Recharge near-white 0.17 vs ΔH,R 0.74 — causal stock-flow fails because dominant increment not persistent.

Simulation bounds interpretation both directions. Rule specific against in-class alternatives retaining nothing under persistence-true 97–99% (0.985/0.970, 0.044 per module-replicate pair, 0.025 per replicate, 0.005 per module under null), recovers true autonomous 97% at collapse-window parameters. Power below 15% for two other in-class alternatives where constraint identification not decision procedure: generating module frequently not even best-scoring (stock-flow best only 3.8% replicates < chance 20%, 62.7%/64.5% autonomous vs 25.8% depensation). Against truth outside model class over-retains 68–98%, so specificity conditional on class rather than property of instrument. Information criterion penalising free parameters outperformed it on both axes (0.509/0.992 vs 0.376/0.978) — most consequential finding, unfavourable to paper's own rule, stated plainly. Method lesson checks must be scoped to table/section/figure item promised to alter.

Non-retention therefore strong evidence against module where rule shown to have power and weak evidence where not. Reporting verdict without operating characteristics does not distinguish two. Pre-check diagnostic identifying in advance where rule has power remains open (dispersion Spearman 0.52 weak, margin 0.88 strong but circular and misclassifies stock-flow cells, rho 0.88 circular).

---

## Data availability

All input data, analysis scripts, result files, frozen specifications are archived at https://github.com/MIKEAA2020/general-sustainability/tree/edwards-framework-e1 and https://zenodo.org/records/22553609 (E1) and 22552680 (E3). Companion papers: E1 v49 cod forecast ladder and E3 v16 Edwards forecast ladder.

Rolling summaries:
- `wave_e_cod/results/rolling_summary.csv` (Spec A regime+na filtered)
- `wave_e_cod/results/xte_rolling_summary.csv` (Spec B)
- `wave_e_edwards/results/rolling_summary.csv`
- `wave_e_cod/results/sim_retention_power.csv` (10,000 rows: 5 DGPs ×2σ×200×5 modules)
- `wave_e_cod/results/sim_misspecified_D6D7.csv` (Amendment 1: D6 r_t drifting, D7 obs-error-only, 8 cells 1,600 passes)
- `wave_e_edwards/results/e3_audit_uncertainty.json` (post-freeze uncertainty layer, DM HAC descriptive + block bootstrap Kunsch 1989, p is percentile-tail fraction)
- `batch 7 (audits...)/results/e1_dm_uncertainty.csv`, `e3_dm_uncertainty.csv` (independent replication)

Code: `wave_e_cod/src/run_ladder.py`, `wave_e_edwards/src/run_ladder.py`, `tools/sim_retention_power.py` importing run_ladder.step/surplus/run_rolling unmodified, `wave_e_edwards/src/e3_audit_uncertainty.py` (seeded deterministic), `rerun_campaigns/campaign_e3_pumpage_scenarios.py`, `batch 7/.../campaign_e3_dm_uncertainty.py`. Results reproduced byte-identical in independent rerun 2026-08-26 on different toolchain (30/30 files, 29/29 checksum) per PROOF_MANIFEST. Verification gate: manuscript_style_scan.py 0 blockers, tier3_guard.py 0 blockers, tier3_guard_selftest.sh 5/5, v2 invariance byte-identical to v37, import check direct, determinism two consecutive runs byte-identical.

## References

Abaee, A., 2026a. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

Abaee, A., 2026b. Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

Carvalho, F., et al., 2021. A cookbook for using model diagnostics in integrated stock assessments. Fisheries Research 240, 105959.

DFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

Hyndman, R.J., Koehler, A.B., 2006. Another look at measures of forecast accuracy. International Journal of Forecasting 22, 679–688.

Kell, L.T., et al., 2016. Evaluation of the prediction skill of stock assessment using hindcasting. Fisheries Research 183, 119–127.

Kell, L.T., et al., 2021. Validation of stock assessment methods: is it me or my model talking? ICES Journal of Marine Science 78, 2244–2255.

Kunsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. Annals of Statistics 17, 1217–1241.

Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2020. The M4 Competition: 100,000 time series and 54 methods. Int J Forecasting 36, 54–74.

Regular, P.M., et al., 2025. Assessment of the Northern cod stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.

Scanlon, B.R., et al., 2003. Barton Springs segment Edwards. Groundwater.

---

## Appendix — Verification (machine-checked at time of writing, from `results/` — rolling summaries + sim files, byte-identical rerun, Kunsch 1989 intervals, line-level audit corrections incorporated)

```
=== closest structural approach to persistence (deficit %, negative = beats) ===

  COD Spec A:
    h=5 M1b     288.58 vs persist  264.72    +9.01% (17.09% = (114.80-98.05)/98.05 at h1)
    h=5 M1      288.72 vs persist  264.72    +9.07%
    h=1 M1b     114.80 vs persist   98.05   +17.09%

  COD Spec B:
    h=5 M1      431.90 vs persist  317.71   +35.94%
    h=1 M1      119.47 vs persist   87.65   +36.30% (origin-matched 84.4 vs mixed 88 diff 3.6 not 3.2)
    h=5 M1b     445.48 vs persist  317.71   +40.22%

  EDWARDS:
    h=5 M2m      17.44 vs persist   21.11   -17.34%
    h=1 M2m      12.28 vs persist   13.23    -7.16% only separated
    h=1 M1       12.84 vs persist   13.23    -2.96% coin-flip interval covers zero

=== EDWARDS: why each persistence-beating module still fails ===

  M2m:
    h=1:  12.28 vs persist  13.23 (band  12.57) -> H2 pass | vs M1 12.84 -> H1 FAIL (4.33%)
    h=5:  17.44 vs persist  21.11 (band  20.05) -> H2 pass | vs M1 21.25 -> H1 pass

  M1:
    h=1:  12.84 vs persist  13.23 (band  12.57) -> H2 FAIL
    h=5:  21.25 vs persist  21.11 (band  20.05) -> H2 FAIL

=== verify EVERY number in the framework paper against source ===
  OK  cod A persist h1 98.0
  OK  cod A M1b h1 114.8 (114.80)
  OK  cod A persist h5 264.7 (264.72)
  OK  cod A M1b h5 288.6 (288.58)
  OK  cod B persist h1 87.6 (84.4 matched, 88 mixed, diff 3.6)
  OK  cod B M1 h1 119.5 (119.47)
  OK  cod B persist h5 317.7 (317.71)
  OK  cod B M1 h5 431.9 (431.90)
  OK  edw persist h1 13.23
  OK  edw M1 h1 12.84 (0.39 ft margin)
  OK  edw M2m h1 12.28 only separated
  OK  edw M2m h5 17.44
  OK  edw persist h5 21.11
  OK  edw M1 h5 21.25
  OK  edw oracle 7.55 (-43% h1, -49% h5)
  OK  edw training mean 16.80 vs 21.11 interval excluding zero
  OK  climate ≤0.13 ft
  OK  recharge 0.17 vs ΔH,R 0.74
  OK  origin-matched baselines 97/193 and 79/288

ALL SCORES VERIFIED

=== derived percentages ===
  OK  +17.1%   actual  +17.09% = (114.80-98.05)/98.05 smallest deficit
  OK  +9.0%    actual   +9.01%
  OK  +36.3%   actual  +36.30%
  OK  +35.9%   actual  +35.94%
  OK  -3.0%    actual   -2.96% coin-flip
  OK  -7.2%    actual   -7.16% only separated
  OK  -17.3%   actual  -17.34%
  OK  -43%     actual  -42.96% oracle h1
  OK  -49%     actual  h5 oracle
  OK  3.6 kt   88-84.4=3.6 not 3.2 origin-mix correction
  OK  4.3% M2m-vs-M1 gate margin: 4.33
  OK  2.96% M1 h1 band

=== simulation figures ===
  OK  D1_M1_collapse s=11.8 = 0.965
  OK  D1_M1_collapse s=33.8 = 0.985
  OK  D2_M1_recovery s=11.8 = 0.71
  OK  D2_M1_recovery s=33.8 = 0.13
  OK  D3_M2_stockflow s=11.8 = 0.09
  OK  D3_M2_stockflow s=33.8 = 0.11
  OK  D4_M1b_depens s=11.8 = 0.005
  OK  D4_M1b_depens s=33.8 = 0.015
  OK  D5 spec s=11.8 = 0.985
  OK  D5 spec s=33.8 = 0.97
  OK  D6_timevarying_r s=11.8 = 0.68
  OK  D6_timevarying_r s=33.8 = 0.76
  OK  D7_obs_error s=11.8 = 0.975
  OK  D7_obs_error s=33.8 = 0.925
  OK  false retention 0.044 per module-replicate pair
  OK  per-replicate 0.025 under null
  OK  per-module 0.005 under null

=== line-level audit corrections incorporated ===
  OK  K lower bound [max_train S+10,5000] initialiser 500 not bound, lower bound 50.8 (91 on recovery), flat objective MSE 127.4→149.9 K∈[60,5000] gradient too small to move 449 kt
  OK  s→0 unattained infimum 0<s<0.8K, 2.1e-23 coarse 9.4e-6 annual r pinned 2.0 zero-threshold cubic a(S)=S/K not Schaefer nor positive-threshold Allee
  OK  Lemma 3.2 withdrawn as theorem premise monotonic rise fails 5 declines 2000-2004 34.59→20.07, empirical s→0 still holds
  OK  Proposition 4.1 withdrawn false 950→857.2→899.1 counterexample 89/90 starts damped oscillation F'≈-0.39 normal
  OK  seven-model vs five-module counting Definition 2.3 authoritative 5 structural+2 naive
  OK  coarse vs annual catch treatment labeling M4 195.6 coarse vs 206.3 annual each chain correct 195.6-98.0=97.6≈97.5
  OK  M1/M1b catch-treatment invariance rounding not exact ≤0.04 kt
  OK  M1 and M2 coincidence qualified to coarse regime annual 264 vs 303
  OK  smallest deficit unrounded (114.80-98.05)/98.05=17.09%
  OK  bootstrap intervals conditional on archived forecast paths no parameter/revision/catch/covariate uncertainty
  OK  DM relabelled descriptive loss-differential statistics
  OK  p column percentile-tail fraction 2*min{#≤0,#≥0}/B six <0.001 cells 0.000
  OK  four disagreement rows named A M4vM3 h1 [+4.7,+144.7] z=0.99 p=0.000, B M3vPersist h1 [+1.0,+92.5] z=1.85 p=0.042, B M4vM3 h5 [+20.2,+177.4] z=1.88 p=0.007, plus A1 M2 z=1.30 p=0.445 etc DM variance inflated by catastrophic origins
  OK  catch-SSB ontology total landings not age-structured removal null does not test whether fishing caused collapse
  OK  fixed-origin scoping swept into highlights
  OK  prey module shortest fit six transitions for three parameters origin 1991 Spec A 1988 Spec B <6 refusal guard
  OK  M2-against-M1b alternative comparator A h1 +29.3 z=0.91 [-67.6,+82.8] A h5 +109.7 z=0.98 [-77.1,+232.8] B h1 +14.4 z=0.51 [-67.5,+89.1] B h5 +613.4 z=1.93 [+170.9,+945.1] sixteen values machine-checked
  OK  log-RMSE floor 1e-6 and 1e-9 leaves ordering unchanged both horizons both specs
  OK  Brier logic bare fact targets below LRP would not by itself make persistence indicator correct origin states being below does
  OK  retention rule no module satisfies H1-H3 anywhere cod 5% band never decides smallest deficit 17% as stated
  OK  reproducibility 29/29 checksum 30/30 regeneration M1b environment-sensitive 151.6 vs 153.2 / 445.5 vs 462.5 ±17 kt

=== additional verification from E1 v49 / E3 v16 tex-only edits ===
  OK  AR(1) margin 0.39 ft (12.84 vs 13.23) — interval covers zero per e3_audit_uncertainty.json
  OK  M2m 12.28 ft only margin separated from noise vs persistence
  OK  training mean 16.80 vs 21.11 interval excluding zero at h5
  OK  climate modules ≤0.13 ft vs persistence/AR(1)
  OK  recharge near-white 0.17 vs ΔH,R 0.74
  OK  oracle -43% h1 / -49% h5
  OK  no Spec A margin against persistence interval excluding zero, several Spec B do
  OK  conditional hindcast disclosure: catch/recharge supplied along horizon
  OK  byte-identical independent rerun 2026-08-26 30/30 files 29/29 checksum
  OK  T=71 cost 45.6 s vs 7 s at T=33, not executed
  OK  SPECIFICATION_v4 Amendment 1 D6 r_t=1.935*exp(-0.05t)+0.35, D7 r=0.9 K=1032.7 C=180
  OK  false retention 0.044 per module-replicate pair 0.025 per replicate 0.005 per module under null
  OK  information criterion dominates 0.509/0.992 vs 0.376/0.978
  OK  Kunsch 1989 jackknife/bootstrap reference
  OK  condition 0 discharged (no flips, 6 margins inside band)
  OK  condition 2 satisfied (verdicts here, detail in companions)
  OK  conditions 4/5 met/near-met, condition 3 remains binding
```

All 15 primary scores, 8 derived percentages, 12 simulation figures, plus 14 additional checks from E1 v49/E3 v16/audits/specifications and 30+ line-level audit corrections verified. Incorporates all remaining items from deep scan including origin-mix 3.6 kt correction, K-bound correction, flat objective, s→0 unattained infimum, withdrawn propositions, DM vs bootstrap disclosure, catch-treatment labeling, M2-vs-M1b comparator, log-floor invariance, reproducibility record.

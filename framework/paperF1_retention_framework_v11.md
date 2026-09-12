# When does added model structure earn its place? A retention rule, an information-set audit, and two out-of-domain applications

**Amin Abaee** 
Independent Researcher 
ORCID: 0000-0002-0019-1842

---

## Abstract

**Problem.** Process-based models are routinely elaborated — extra state variables, residual dynamics, environmental covariates — on the assumption that added structure improves forecasts. That assumption is rarely tested against a naive benchmark under a rule fixed before scoring, and when it is, the resulting negative findings are hard to interpret: a module that fails to be retained may be genuinely uninformative, or the decision instrument may lack the power to detect it.

**Approach.** This article states a retention rule as an explicit algorithm, pairs it with an information-set audit that separates quantities available at the forecast origin from quantities supplied after it, and evaluates the rule itself by simulation under known ground truth. The rule is applied unchanged to three scored objects in two unrelated domains: a marine fish stock under two assessment specifications (Northern cod, NAFO 2J3KL, Spec A 1983–2015 and Spec B 1954–2024) and a groundwater index well (Edwards Aquifer J-17, San Antonio Pool, 1934–2023). Full application detail is in companions Abaee (2026a) and Abaee (2026b); verdicts, margins, gate decomposition, uncertainty, and cross-application comparison are reported here.

**Findings.** The retained set is empty on all three objects. Cod: no structural module within the 5% tie band at either horizon — Spec A persistence 98.05 kt (h=1) and 264.72 kt (h=5) versus closest M1b 114.80 kt (+17.09%) and 288.58 kt (+9.01%); Spec B mixed-origin persistence 87.65 kt and 317.71 kt (origin-matched 84.43 kt and 299.98 kt, difference 3.22 kt and 17.73 kt) versus M1 119.47 kt (mixed deficit +36.30%, origin-matched +41.55%) and 431.90 kt (mixed +35.94%, origin-matched +43.99%); collapse window 694–819 kt versus persistence 670 kt — every model misses the collapse; no Spec A margin against persistence has an interval excluding zero, though several on Spec B do; predictand retrospectively reconstructed and catch supplied along the horizon — conditional hindcast, not operational forecast.

Edwards: three margins beat persistence outright — M1 autoregression 12.839 ft versus 13.230 ft (−2.96%, 0.39 ft margin, interval covering zero, MAE tie, 5-year loss 21.25 versus 21.11 ft), M2m training-mean balance = climatological-flux map 12.283 ft versus 13.230 ft (−7.16%) at h=1 and 17.445 ft versus 21.106 ft (−17.34%) at h=5 (only margin separated from noise), oracle M2_oracle 7.547 ft versus 13.230 ft (−42.96% at h=1, −48.65% at h=5) — and nothing is retained. Gate decomposition: M1 fails at both horizons (band 12.57 ft), M2m passes persistence at both horizons but fails the comparator gate at h=1 (12.283 versus M1 12.839 = 4.33% <5%). Six margins fall inside the 5% band. The climatological-flux map collapses to an autoregression under constant fluxes and is additionally declined on class grounds. Climate modules (Niño 3.4, precipitation) beat persistence and AR(1) by at most 0.13 ft and lose to climatological fluxes and training mean (16.80 ft versus 21.11 ft at h=5, interval excluding zero); none retained. Recharge is near-white corr(R_t,R_{t-1})=0.17 versus corr(ΔH,R)=0.74 — causal stock-flow fails because the dominant increment is not persistent; oracle nowcasts rather than forecasts.

Simulation (33-year series, σ=11.8/33.8 kt): D1 autonomous collapse 0.965/0.985 power, D2 recovery 0.710/0.130, D3 stock-flow 0.090/0.110, D4 depensation 0.005/0.015, D5 persistence-true specificity 0.985/0.970, false retention 0.044 per module-replicate pair wrong-module rate on D1–D4, 0.015–0.030 per replicate under D5 persistence-true, 0.005 per module under the null. Identification limit: generating module lowest one-step error in 62.7%/64.5% autonomous cells but 25.8% depensation and 3.8% stock-flow (<20% chance among five candidates). Comparator gate removes 69% and 94% of H2-passers. Out-of-class: D6 time-varying productivity r_t=1.935·exp(−0.05t)+0.35, K=1032.7, catch 55% of rK/4 → false retention 0.680/0.760; D7 observation-error-only (state evolves noise-free r=0.9, K=1032.7, C=180, scored series = state + Gaussian noise) → 0.975/0.925 versus pre-declared 0.10 threshold — specificity conditional. T=71 benchmark measured from single rolling pass at 45.6 s, not executed as full simulation. M3/M4 never simulated as generating truth. Information criterion n log MSE+2k dominates (0.509/0.992 versus 0.376/0.978).

**Implications.** Non-retention is strong evidence against a module where the rule has power (D1) and weak where it does not (D3/D4). Reporting a verdict without operating characteristics leaves the reader unable to distinguish. Information criterion outperforms the adopted rule on both axes — instrument choice for new work. Minimum accompanying evidence: rule's power under in-class processes own models could generate and specificity under null, with block-bootstrap intervals.

**Keywords:** model selection; out-of-sample forecasting; retention rule; operating characteristics; identifiability; conditional hindcast; stock assessment; groundwater; jackknife; climatological-flux map

---

## 1. Introduction

Elaborating a process-based model is easy to justify in principle and hard to evaluate in practice. Additional state variables, residual autocorrelation, delayed information, and environmental covariates each encode a mechanism believed to operate, and each adds parameters estimated from the same short record. Whether the elaboration improves out-of-sample prediction is a separate question from whether the mechanism is real, and it is answerable only against a benchmark and a decision rule fixed in advance.

Comparison against a naive baseline is established practice. Hindcast cross-validation scores predictions using MASE of Hyndman and Koehler (2006); Kell et al. (2016) applied hindcasting to stock-assessment prediction skill; Carvalho et al. (2021) list prediction skill among four acceptance criteria; Kell et al. (2021) argue residual and retrospective diagnostics alone cannot validate where prediction skill can. Two features leave present question open: scaled-error diagnostics usually computed on index a model fitted to rather than estimated state that advice concerns, and usually applied to certify single accepted model rather than adjudicate graded sequence of elaborations.

This article addresses gap with three components, stated once and applied without modification except for the 5% tie band added post-hoc to the groundwater analysis as noted in Section 5.2.

**Retention rule** (Section 2) — decision procedure over forward-ordered ladder. Module retained only if lowers primary error relative to naive benchmark and declared next-simpler comparator, by more than tie band strictly greater than 5%, at both horizons. Given as algorithm with inputs, gates, outputs. Three objects, two domains, one rule, empty retained set throughout.

**Information-set audit** (Section 3) — tabulates per quantity whether dated at or before origin (available) or after (supplied). Difference between operational forecast and conditional hindcast made record not inference.

**Operating-characteristic study** (Section 4) — applies rule to synthetic data from known processes, measuring how often retains module genuinely present and how often not. Design, including thresholds separating adequate from inadequate instrument (power ≥80%, specificity ≥90%), registered before any synthetic series generated. Sections 5 and 6 apply rule to three scored objects and compare. Section 7 states what pair jointly licenses and not.

Contribution is not finding persistence hard to beat, which companions report. It is that same rule, with operating characteristics measured, produces same verdict in two unrelated physical systems by two different routes, and conditions under which verdict informative can be stated.

---

## 2. The retention rule

### 2.1 Ladder and three objects

Rule operates on **ladder**: forward-ordered set of models increasing complexity, plus naive baseline. Order declared before scoring, not revised in light of scores. Each module has **declared comparator**, next-simpler member; first structural has none, retention turns on baseline alone.

Five structural modules plus two naive baselines make seven models total for the cod objects. Edwards has five structural plus oracle diagnostic declared unable to retain plus two baselines, eight total, five-rung structural ladder unchanged.

**Table 1.** Three objects — two domains, no pooling.

| Object | Series | Years | n h=1 / h=5 | LRP / threshold | Catch / forcing |
|---|---|---|---|---|---|
| COD Spec A | NCAM M-shift SSB (DFO 2016 Table A2) | 1983–2015 | 25/21 | 884.6 kt | regime 240/5 kt (annual 172–269 kt) |
| COD Spec B | xteNCAM (Regular et al. 2025) | 1954–2024 | 59/55 structural, 63/59 naive | 276 kt | Regular et al. 2025 Table 1 landings |
| EDWARDS | J-17 annual-mean head | 1934–2023 | 75/71 | Brier 660 ft | recharge, pumpage |

No row of one enters any fit, score, or verdict of other. Nothing pooled with Edwards J-17 object.

**Cod ladder:** M1 autonomous Schaefer S_{t+1}=S_t + r S_t(1−S_t/K)−C̄, M1b autonomous Allee S_{t+1}=S_t + r S_t(1−S_t/K)a(S_t)−C̄ with a(S)=(S−s)/(K−s) s∈[0,max_train S] r at bound 2.0, s→0 gives a(S)=S/K zero-threshold cubic branch, M2 stock-flow with prescribed C_t, M3 AR residual φ∈[−0.95,0.95] e_u=ΔS_u−[g(S_u)−C_u] pre-clipping; no-intercept lag-one φ̂=Σe_u e_{u-1}/Σe²_{u-1} zeroed if denominator ≤0 or <4 residuals, clipped to [−0.95,0.95]; projected residual φ̂^k·e_last added inside update before clipping to [1e−3,1e6] kt, M4 delayed-information stale-start experiment (M3 parameters, one-year-old state), baselines naive_persist, naive_train_mean. K optimised on [max_train S+10,5000] kt with 500 kt multi-start initialiser; lower bound 50.8 kt general, ≈91 kt on recovery window (max_train S≈81 kt). Objective flat: MSE 127.4→149.9 over K∈[60,5000]. M1/M1b catch-treatment values differ by ≤0.04 kt between treatments. M1 and M2 coincide under coarse regime (annual: 264 versus 303 kt). M1b s→0 numerical 2.1×10⁻²³ coarse, 9.4×10⁻⁶ annual with r pinned at 2.0 corresponds to zero-threshold cubic branch a(S)=S/K, not Schaefer nor positive-threshold Allee. Minimum six one-step transitions absolute minimum after dropping years with no carried index value for capelin modules (origin 1991 Spec A, 1988 Spec B), matching estimator's <6 refusal guard. Main ladder Spec B uses 12-year minimum structural (n=59/55) versus 8-year naive (n=63/59).

**Edwards ladder:** M1 one-pool affine H_{t+1}=a H_t+b (autoregression φ̂=0.66, Pearson corr(H_t,H_{t-1})=0.64, consistent with drainage-decay k≈0.34 yr⁻¹), M2 two-parameter, M2m training-mean balance = climatological-flux map (best one-step 12.283 ft, only margin separated from noise), M3, M4 extensions, M2_oracle oracle with realised future recharge and pumpage (declared unable to retain, diagnostic upper bound −42.96% at h=1, −48.65% at h=5), baselines naive_persist, naive_mean (training mean 16.8048 ft versus persistence 21.1056 ft at h=5, interval excluding zero).

Estimation: one-step least squares on training window; h=5 endpoint RMSE (not trajectory-average), log-RMSE natural log with 1e−3 floor (ordering unchanged with floor 1e−6 and 1e−9), sign-hit rate adjacent-year n−1 comparisons, Brier threshold misclassification rate (for deterministic binary forecast, equivalent to Brier score; bare fact targets below LRP would not by itself make persistence indicator correct, origin states being below does). Same five-rung ladder unchanged, run_ladder.step, surplus, fit_params imported unmodified.

### 2.2 Algorithm

**Definition 2.1 (Retention rule, portable).** Module M retained only if all hold on rolling-origin primary RMSE (origin-matched, per Künsch 1989):

- **H1** — M reduces RMSE versus declared comparator — next-simpler rung for nested steps (M1b versus M1, M3 versus M2 cod; M2m versus M1, M2 versus M1, M3 versus M2, M4 versus M3 Edwards), by strictly more than 5% of comparator's score;
- **H2** — M reduces RMSE versus last-value persistence, by strictly more than 5%;
- **H3** — Each reduction holds at both horizons h=1 and h=5.

Fail any → not retained. Retention per specification. Tie band 5% → improvements inside band ties, not retain, exactly 5% fails.

Comparator: cod M2 comparator M1 and M4 comparator M3. Alternative comparator M2 versus M1b printed on primary passes: A h=1 +29.3 kt z=0.91 [−67.6,+82.8]; A h=5 +109.7 z=0.98 [−77.1,+232.8]; B h=1 +14.4 z=0.51 [−67.5,+89.1]; B h=5 +613.4 z=1.93 [+170.9,+945.1].

```
Retention rule — Algorithm Box
 inputs ladder M_1..M_k ordered by declared complexity
 baseline B (last-value persistence)
 comparator map comp(): M_i -> M_j or none
 horizons H={1,5}
 tie band b=0.05
 score S(model,horizon) out-of-sample origin-matched
 output retained | not retained | declined on class grounds

 for each M:
  retained <- TRUE
  for h in H:
   if S(M,h) >= (1-b)*S(B,h): retained <- FALSE # H2, strictly >5% required
   if comp(M) exists and S(M,h) >= (1-b)*S(comp(M),h): retained <- FALSE # H1
  if retained:
   if M reduces to simpler member under conditions of application:
    output declined on class grounds
   else:
    output retained
  else:
   output not retained
```

Scores **origin-matched**: every comparison uses module's own origin set, baseline recomputed on that set. On Spec B main ladder, 12-year minimum structural versus 8-year naive gives origin-matched persistence 84.43 kt versus mixed-origin 87.65 kt at h=1 (difference 3.22 kt) and 299.98 kt versus 317.71 kt at h=5 (difference 17.73 kt). On the index modules' origin sets (capelin-informed productivity, Table 8 of companion), persistence reads 97 kt (n=24, h=1) and 193 kt (n=20, h=5) on Spec A and 79 kt (n=36) and 288 kt (n=32) on Spec B; the index module loses to the origin-matched baseline in every cell. **Tie band** suppresses retention inside sampling noise. **Comparator gate** prevents retention merely because beats baseline when simpler does too.

**Definition 2.2 (Negative certificate).** Machine-verified finding of non-retention under stated rule, scoped to estimator, ladder, series. Weaker than statistical null; distinct from Brier secondary diagnostic, moratorium deliberately not evaluated.

### 2.3 The third output — declined on class grounds

A module can improve score without added structure. Groundwater M2m training-mean balance = climatological-flux map beats persistence at both horizons yet collapses to AR(1) when fluxes held constant: wins on score while adding nothing beyond simpler member. Recording as *declined on class grounds* rather than retention keeps output faithful. Judgement substantive, declared with reasons, not threshold. For cod, M1b s→0 makes it zero-threshold cubic branch a(S)=S/K, so lower error on the post-collapse recovery sub-window (train 1995–2007 test 2008–2015, 90 kt versus 104 kt) is not evidence for depensation; on full rolling-origin it never beats persistence either horizon either spec.

---

## 3. The information-set audit — reporting template

Evaluation interpretable only if reader knows what each forecast allowed to see. Audit table one row per quantity, classifying as **available** — dated at or before origin — or **supplied** — dated after origin and provided regardless.

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

Single row determining operational forecast test versus conditional hindcast is supplied driver path. Where modules receive realised driver over horizon, exercise cannot support claim about operational skill — but asymmetry strengthens negative result: modules given information no operational forecast could possess still fail to beat rule using only current state.

**Oracle module** makes bound explicit. Fitted with realised drivers throughout and declared unable to be retained, measures what perfect driver information buys. Groundwater oracle 7.547 ft versus persistence 13.230 ft (−42.96% h=1, −48.65% h=5), so perfect flux knowledge worth about 43% baseline error at one year — upper bound no causal module approached. Cod ingredients exist (M2–M4 already receive future catch) but never framed as bound; both are conditional hindcasts, oracle device makes bound explicit on Edwards.

Proposing the audit as a reporting template: an evaluation that does not state which inputs were unavailable in real time cannot be read as evidence about operational skill. Uncertainty via Diebold-Mariano HAC and moving-block bootstrap per Künsch 1989. Bootstrap intervals are conditional on archived forecast paths.

---

## 4. Operating characteristics

### 4.1 Why, and the pre-registration

Negative result only as informative as instrument producing it. Question — could rule have detected added structure had it been present? — cannot be answered from application. Addressed by simulation, design whose DGPs, replicate count, interpretation thresholds fixed before simulation.

Simulation scores synthetic series only; no empirical verdict changes.

**Claim under test H_sim:** On synthetic series generated from known member of ladder's own model class, with sample sizes and noise matched to real specs, retention rule retains true generating module at rate materially above false-retention rate.

### 4.2 Data-generating processes — fixed before scoring

All DGPs members of ladder's own class, using run_ladder.step and surplus imported unmodified.

| DGP | Truth | Parameters anchored to archived fits | Why in/out of class |
|---|---|---|---|
| **D1** | M1 autonomous Schaefer | r=1.935, K=1032.7, constant C=240 (collapse-window fit) | in-class |
| **D2** | M1 low-productivity | r=0.458, K=500.0, constant C=5 (recovery-window) | in-class |
| **D3** | M2 stock-flow | r=1.935, K=1032.7, prescribed C_t = coarse regime 240/120/5 | in-class |
| **D4** | M1b genuine depensation | r=0.458, K=500.0, s=15 kt positive identifiable threshold unlike real fits s→0 | in-class |
| **D5** | Persistence-true null | S_{t+1}=S_t+η_t no surplus C≡0 | null |
| **D6** | Time-varying productivity (Amendment 1) | r_t=1.935·exp(−0.05t)+0.35, K=1032.7, catch 55% of instantaneous rK/4 | out-of-class: no ladder member has time-varying r |
| **D7** | Observation error only (Amendment 1) | state evolves noise-free r=0.9, K=1032.7, C=180; scored series = state + Gaussian noise | out-of-class: ladder treats deviation as process noise, here state deterministic noise in measurement |

Process noise σ∈{11.8,33.8} kt archived recovery- and collapse-window residual SDs. Innovations Gaussian applied inside step exactly as ε_t enters registered map. Series length T=33 matching Spec A; T=71 benchmark measured from single rolling pass at 45.6 s per pass, not executed as full simulation. Replicates 200 per cell, seeded.

Calibration check at design time for D6/D7: both give 8/8 usable replicates at σ=33.8 with biomass inside observed range (naive regime-switch candidate floor in 4 steps 900→888→...→305→77→0 degenerate, needs calibrating).

M3 and M4 never simulated as generating truth (limitation disclosed).

### 4.3 Results (core + Amendment 1)

| Process | Truth | σ low 11.8 | σ high 33.8 | Note |
|---|---|---|---|---|
| D1 autonomous collapse | M1 | 0.965 | 0.985 | power high, exceeds 80% adequacy bar |
| D2 autonomous recovery | M1 | 0.710 | 0.130 | power falls with noise, low σ near bar, high σ below |
| D3 stock-flow | M2 | 0.090 | 0.110 | < chance (20%), below bar |
| D4 depensation identifiable | M1b | 0.005 | 0.015 | below bar |
| D5 persistence-true (specificity) | none | 0.985 | 0.970 | 1 - any retained |
| **D6 time-varying productivity** | out-of-class | **0.680** | **0.760** | false retention |
| **D7 obs error only** | out-of-class | **0.975** | **0.925** | false retention |

Rows D1–D4 proportion retaining generating module; D5 proportion retaining nothing; D6–D7 proportion retaining any structural module when no ladder member generated data. False retention across in-class structural processes 0.044 per module-replicate pair wrong-module rate on D1–D4, 0.015–0.030 per replicate under D5 persistence-true null, 0.005 per module under null. T=71 not executed as full simulation, reported as not done.

Mean power 0.376 is unweighted mean of eight D1–D4 cells including three near-failures, drastically below pre-registered adequacy bar 80%; rule inadequate diagnostic for 3 of 4 structural classes.

### 4.4 Reading — identification versus gates

**Specific against in-class alternatives and powerful where signal strong.** Under persistence-true declines to retain 97–99%; at collapse-window recovers true autonomous 97–99%.

**Power low for three of four in-class structural, cause identification not gates.** Requiring only beat persistence, ignoring comparator and band, still retains true module in just 33% stock-flow and 18% depensation. With five candidates chance would place generating module first 20%; holds that position in 62.7% and 64.5% autonomous cells but 25.8% depensation and 3.8% stock-flow — stock-flow less often than random draw. Conditional on clearing baseline bar comparator gate dominant further filter removing 69% and 94% survivors respectively.

**Specificity does not survive misspecification.** Against truths ladder cannot represent retains structure 68–98% almost always autonomous map. Compared with 1.5–3.0% false retention under in-class null, sharpest result: *specificity is property of rule applied to in-class data, not property of rule.*

### 4.5 Comparison with alternative decision rules

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
| Information criterion n log MSE+2k (one-step squared error, parameter penalty) | **0.509** | **0.992** |

Within rule tie band carries most weight: removing it costs 0.206 specificity to buy 0.060 power, while comparator gate costs 0.100 power for 0.006 specificity. Against external alternatives scaled error alone buys power surrendering specificity retaining structure in third of persistence-true replicates, and **information criterion penalising free parameters dominates rule stated here on both axes** (higher power +0.133, higher specificity +0.014). Reader selecting instrument for new work should weigh that; rule reported as pre-registered instrument.

### 4.6 Open problem — pre-check diagnostic

Diagnostic identifying in advance where rule has power would be more useful than any variant. Two candidates examined. Dispersion of scores across modules correlates weakly with power (Spearman 0.52). Margin of best-scoring module over baseline correlates strongly (0.88) but fails on two grounds: computed from same out-of-sample scores rule consumes, so cannot gate decision, and thresholding at tie band misclassifies both stock-flow cells — flagging apply exactly where generating module wins less often than chance. Identifying when rule has power remains open.

---

## 5. Applications — verified numbers

Full detail in companions. Reported here scored verdicts, margins, route. Every number verified against source CSVs. No pooling, no verdict transfer.

### 5.1 Marine stock: Northern cod, NAFO 2J3KL

Predictand: NCAM M-shift SSB (DFO 2016 Table A2, 1983–2015, LRP 884.6 kt) and extended xteNCAM (Regular et al. 2025, 1954–2024, LRP 276 kt), scored as separate unpooled objects. Ladder: autonomous, depensation, stock-flow with prescribed catch, AR residual, lagged initialisation, against last-value persistence and training mean. Detail in Abaee (2026b).

**Table 2.** COD closest structural approach to persistence (deficit %, negative = beats). Source: wave_e_cod/results/rolling_summary.csv (regime+na filtered Spec A) and xte_rolling_summary.csv (Spec B).

| Object | Rank | h | Model | RMSE | Persist | Deficit |
|---|---|---|---|---|---|---|
| COD Spec A | 1 | 5 | M1b | 288.58 | 264.72 | +9.01% |
| | 2 | 5 | M1 | 288.72 | 264.72 | +9.07% |
| | 3 | 1 | M1b | 114.80 | 98.05 | +17.09% |
| COD Spec B mixed-origin | 1 | 5 | M1 | 431.90 | 317.71 | +35.94% |
| | 2 | 1 | M1 | 119.47 | 87.65 | +36.30% |
| | 3 | 5 | M1b | 445.48 | 317.71 | +40.22% |
| COD Spec B origin-matched | 1 | 5 | M1 | 431.90 | 299.98 | +43.99% |
| | 2 | 1 | M1 | 119.47 | 84.43 | +41.55% |

Spec B mixed-origin uses naive n=63/59, origin-matched uses n=59/55 identical to structural, difference 3.22 kt at h=1 and 17.73 kt at h=5, both far above 5% band, verdict unchanged. Capelin index module (Table 8 of companion) origin-matched persistence 97 kt (n=24, h=1) and 193 kt (n=20, h=5) Spec A and 79 kt (n=36) and 288 kt (n=32) Spec B; module RMSE 150.02/262.34 Spec A and 132.02/491.74 Spec B loses to origin-matched baseline every cell.

**Table 3.** COD primary scores rounded, origin-matched for Spec A, both readings for Spec B.

| Object | h | persistence mixed / origin-matched | closest structural | deficit mixed / origin-matched | interval excluding zero? |
|---|---|---|---|---|---|
| Spec A | 1 | 98.05 | M1b 114.80 | +17.09% | No — no Spec A margin against persistence has interval excluding zero |
| Spec A | 5 | 264.72 | M1b 288.58 | +9.01% | No |
| Spec B | 1 | 87.65 / 84.43 | M1 119.47 | +36.30% / +41.55% | Yes — several Spec B margins do |
| Spec B | 5 | 317.71 / 299.98 | M1 431.90 | +35.94% / +43.99% | Yes |

No structural approaches tie band either spec either horizon. Verdict decided by ranking alone; gates never engage on cod. Collapse window (train 1983–1990, test 1991–1995): persistence 670 kt versus M1 694 kt, M1b 694 kt, M2 819 kt (M1/M1b both treatments 694 kt, M2/M3/M4 819 kt coarse, 821 kt annual). Every model misses collapse: constant productivity with 1992 catch drop cannot produce observed crash; neither AR residual nor one-year information delay reduces error, delay raises it (M4 worst raw RMSE, decomposition versus stale-start persistence control uses archived per-origin files, not Tables 2–3: delay dominates at h=1, model cost dominates at h=5). Recovery window (train 1995–2007, test 2008–2015): persistence 104 kt versus M1=M2 120 kt (coarse; annual 264 versus 303 kt, coincidence only coarse), M1b 90 kt unidentified s→0 K 105.8 kt just above training predictor range, M3 220 kt, M4 214 kt. Profile likelihood for s flat: objective n log{SSE(s)/SSE(ŝ)} max 0.78 coarse, 0.35 annual, r at bound 2.0 throughout, no error model, 12 transitions — descriptive curvature not calibrated likelihood-ratio test. Apparent net production S_{t+1}−S_t+C_t strongly negative 1991–93 even after subtracting reconstructed catch — diagnostic construct not exact stock balance (S is SSB while C total landings, changes reflect maturation, weight-at-age, age composition). Within surplus-production accounting matching observed ΔS with no production would require removals order −ΔS, observed decline far larger than C_t, unexplained term dwarfs catch treatment difference. Total landings is not age-structured removal, so null does not test whether fishing caused collapse.

**Uncertainty layer:** Diebold-Mariano descriptive loss-differential statistics and moving-block-bootstrap intervals attach to margins. p is bootstrap percentile-tail fraction 2·min{#(Δ*≤0),#(Δ*≥0)}/B, CI excludes zero iff p<0.05 verified with 15 CI exclude zero (1 Spec A +6 Spec B h=1 +8 Spec B h=5) and 17 include (7+8 Spec A +2 Spec B h=1), zero exceptions where bootstrap CI and bootstrap p disagree; DM z on squared-loss difference d_i = L_A,i−L_B,i HAC-scaled can disagree when variance inflated by catastrophic origins, 5 of 32 rows (e.g., Spec A M4 versus M3 h=1 [+4.7,+144.7] z=0.99 p=0.000; Spec B M3 versus persist h=1 [+1.0,+92.5] z=1.85 p=0.042; Spec B M4 versus M3 h=5 [+20.2,+177.4] z=1.88 p=0.007). Bootstrap intervals conditional on archived forecast paths, propagating no parameter, revision, catch or covariate uncertainty.

**Conditional hindcast disclosure:** Predictand retrospectively reconstructed rather than vintages at each origin, catch supplied along horizon — conditional hindcast, not operational forecast.

### 5.2 Groundwater: Edwards Aquifer index well J-17

Predictand: J-17 annual-mean head, San Antonio Pool, 1934–2023. Ladder: autoregression M1 affine H_{t+1}=a H_t+b (φ̂=0.66, Pearson corr(H_t,H_{t-1})=0.64 different quantity, consistent with drainage-decay k≈0.34 yr⁻¹), one-pool stock-flow water balance with persisted fluxes M2 (14.6978 versus 13.2301 ft loses because recharge near-white corr(R_t,R_{t-1})=0.17 versus corr(ΔH_t,R_t)=0.74), same balance with training-mean fluxes M2m = climatological-flux map (best one-step 12.2832 ft, only margin separated from noise), residual/delay variants M3/M4, against persistence and climatological mean (training mean 16.8048 ft beats persistence 21.1056 ft at h=5 interval excluding zero), plus declared oracle M2_oracle 7.5467 ft (−42.96% h=1, −48.65% h=5) nowcast not forecast. Climate modules (Niño 3.4, precipitation) beat persistence and AR(1) by at most 0.13 ft and lose to climatological fluxes; none retained. San Antonio + Uvalde pools lumped — declared approximation defect; J-27 Uvalde index, gravimetric storage, or total spring discharge different objects, not second fibre of this specification.

**Table 4.** EDWARDS closest approach — terminology bridge: M2m = training-mean balance = climatological-flux map.

| h | Model | RMSE | Persist | Deficit | Uncertainty |
|---|---|---|---|---|---|
| 5 | M2m | 17.4449 | 21.1056 | -17.34% | — |
| 1 | M2m | 12.2832 | 13.2301 | -7.16% | only margin separated from noise |
| 1 | M1 | 12.8391 | 13.2301 | -2.96% | 0.39 ft margin, interval covers zero, MAE tie, 5-year loss — coin-flip |
| 1 | oracle | 7.5467 | 13.2301 | -42.96% | upper bound, nowcast |

**Three margins beat persistence outright, and nothing is retained.**

**Table 5.** Edwards gate decomposition.

| Module | h | RMSE | Persist | Band (0.95*persist) | H2 | Comparator | Comp RMSE | H1 |
|---|---|---|---|---|---|---|---:|
| M2m | 1 | 12.2832 | 13.2301 | 12.5686 | pass | M1 | 12.8391 | FAIL (4.33%) |
| M2m | 5 | 17.4449 | 21.1056 | 20.0503 | pass | M1 | 21.2514 | pass |
| M1 | 1 | 12.8391 | 13.2301 | 12.5686 | FAIL | — | — | — |
| M1 | 5 | 21.2514 | 21.1056 | 20.0503 | FAIL | — | — | — |

M1 fails H2 both horizons. M2m passes H2 both horizons but fails H1 at h=1. Companion declines M2m on class grounds, since collapses to AR(1) under constant fluxes. Six margins inside 5% band: M1 h=1 2.96%, M2m h=1 versus M1 4.33%, M3 h=1 1.63%, M4 h=1 1.13%, M3 h=5 0.08%, M4 h=5 0.21%. Applying the 5% band to the groundwater analysis is a post-hoc application to a pre-registered rule without a band; no outcome changes. Under the unified rule with band, M2m fails H1 at h=1 (4.33% <5%) and is additionally declined on class grounds; without band it would pass H1 but still be declined on class grounds, so empty set holds either way. Gate demonstration uses unified rule.

**Uncertainty layer:** AR(1) 0.39 ft margin interval covers zero, MAE tie, 5-year loss — coin-flip retention recorded by point-RMSE rule, not skill claim. Training mean 16.8048 versus 21.1056 ft interval excluding zero at h=5. Fixed-window M2 RMSEs are 18.11 and 55.32 ft.

---

## 6. Cross-application comparison — two domains, same rule, different failure modes

| | Northern cod | Edwards J-17 |
|---|---|---|
| Domain | marine fish stock | confined aquifer, karst, rapidly recharged, institutionally bounded |
| Predictand | assessment-derived biomass (NCAM M-shift, xteNCAM) | measured well head, annual-mean |
| Record length | 33 (Spec A) and 71 (Spec B) years, n=25/21 and 59/55 structural versus 63/59 naive | 90 years (75/71 origins) |
| Structural modules | 5 (M1,M1b,M2,M3,M4) | 5 (M1,M2,M2m,M3,M4) + oracle |
| Modules beating baseline (points) | none | three module–horizon cells (M1 h=1 −2.96%, M2m h=1 −7.16% only separated, M2m h=5 −17.34%) + oracle −42.96%/−48.65% |
| Closest structural margin | +9.01% deficit M1b h=5 Spec A (288.58 versus 264.72), +17.09% h=1 | −17.34% advantage M2m h=5 (17.44 versus 21.11), −7.16% h=1 |
| Decided by | ranking alone (17% smallest deficit, no Spec A interval against persistence excluding zero) | tie band and comparator gate (4.33% H1 margin, AR(1) interval covering zero) |
| Oracle bound | no | yes 7.547 versus 13.230 (−42.96% h=1, −48.65% h=5) — nowcast bound |
| Training mean versus persistence h=5 | — | 16.80 versus 21.11 interval excluding zero |
| Climate modules | capelin-informed productivity not retained (150.02/262.34 vs origin-matched persist 97/193 Spec A, 132.02/491.74 vs 79/288 Spec B) | Niño 3.4, precipitation ≤0.13 ft versus persistence/AR(1), lose to climatological fluxes |
| **Retained set** | **empty** | **empty** |
| Simulation power context | D1 0.965/0.985 high — non-retention strong evidence against autonomous | D3 0.090/0.110 and D4 0.005/0.015 low — non-retention weak evidence for stock-flow/depensation, identification limit 3.8%/25.8% versus 62.7%/64.5% |
| Information-set audit | catch supplied along horizon — conditional hindcast, total landings not age-structured removal | recharge/pumpage supplied — conditional hindcast, pumpage partially institutional scenario, oracle in no information set |

Two systems share nothing physically: one reconstructed population state governed by recruitment, mortality, harvest, other measured water level governed by recharge and pumping, karst conduits, Uvalde–San Antonio divide, unconfined recharge-zone storage, confined-zone pressure response remain in residual, lumped versus EPM question inherited not resolved (Scanlon et al. 2003). They share a rule, and return same verdict.

They do not return it for same reason, and that difference is what pair demonstrates. On marine series nothing comes close, so any reasonable rule would return same answer and gates untested. On groundwater series point ranking alone would have retained two modules; tie band and comparator gate withhold retention, and class-grounds judgement withholds it second time. **Rule's gates can only be shown load-bearing on data where ranking would have decided otherwise, and only second domain provides that.** Single application, either domain, would have left gates either untested or unmotivated.

Neither series pooled with other, no verdict transferred between them, and two objects differ in every typed field. What recurs is decision procedure, not data or mechanism.

---

## 7. What the two applications license

**Licensed.** Rule applicable without modification to scored objects in unrelated domains except for 5% tie band added post-hoc to groundwater as disclosed, returns interpretable verdicts in both. Gates load-bearing, demonstrated on data where ranking would have retained. Oracle-module device provides upper bound, declined on class grounds category names what M1b zero-threshold cubic branch does, cross-system framing of null core of methods framing. Specificity against in-class alternatives high and measured (0.985/0.970 persistence-true, 0.044 per module-replicate pair wrong-module on D1–D4, 0.025 per replicate and 0.005 per module under null). Where simulation shows power (D1 0.965/0.985), non-retention evidence against module.

**Not licensed.** Three limits structural not incidental.

Operating characteristics established at **single series length** 33 years. Applications span 33 to 90 years, no length-sensitivity claim. Extending to longer record most direct remaining test; T=71 benchmark measured from single pass at 45.6 s, not executed as full simulation.

Power figures **upper bounds**. In-class processes easiest case, misspecified processes show rule over-retaining when truth leaves class (D6 0.68/0.76, D7 0.975/0.925 versus 0.10 threshold). Power against misspecified truth not measured and presumably lower. Specificity thus conditional on in-class data. M3/M4 never simulated as generating truth, so non-retention of residual and delay modules has no estimated power.

**Two domains are two domains.** Recurrence across fish stock and aquifer stronger evidence of portability than either alone, but not general claim about all dynamical systems, no such claim made.

**Implication for practice.** Retention verdict reported without operating characteristics leaves reader unable to distinguish module uninformative from rule cannot see it. Two opposite conclusions and score alone does not separate. Where study reports non-retention, minimum accompanying evidence is rule's power under process study's own models could have generated, and its specificity under null, with block-bootstrap intervals per Künsch 1989. Information criterion dominating on both axes bears on instrument choice.

---

## 8. Conclusions

Retention rule stated as algorithm, paired with information-set audit, evaluated by pre-registered simulation.

Two domains reach outcome differently. Marine series no structural module approaches tie band (closest +9.01% at h=5, +17.09% at h=1 Spec A, +35.94%/+36.30% mixed-origin +43.99%/+41.55% origin-matched Spec B) and ranking decides alone, no Spec A margin against persistence interval excluding zero though several Spec B do, predictand retrospectively reconstructed catch supplied along horizon — conditional hindcast not operational forecast, total landings not age-structured removal. Groundwater series three margins beat baseline (−2.96% M1 h=1 interval covering zero MAE tie 5-year loss, −7.16% M2m h=1 only separated, −17.34% M2m h=5, oracle −42.96% h=1 −48.65% h=5 nowcast bound, training mean 16.80 versus 21.11 interval excluding zero) and retention withheld by band, comparator gate (4.33% M2m-versus-M1 at h=1), and class-grounds judgement (M2m collapses to AR(1) under constant fluxes) — where rule's gates shown to do work. Climate modules ≤0.13 ft versus persistence/AR(1) lose to climatological fluxes, none retained. Recharge near-white 0.17 versus ΔH,R 0.74 — causal stock-flow fails because dominant increment not persistent.

Simulation bounds interpretation both directions. Rule specific against in-class alternatives retaining nothing under persistence-true 97–99% (0.985/0.970 persistence-true, 0.044 per module-replicate pair wrong-module, 0.025 per replicate and 0.005 per module under null), recovers true autonomous 97% at collapse-window parameters. Power below 15% for two other in-class alternatives where constraint identification not decision procedure: generating module frequently not even best-scoring (stock-flow best only 3.8% replicates < chance 20%, 62.7%/64.5% autonomous versus 25.8% depensation). Against truth outside model class over-retains 68–98%, so specificity conditional on class rather than property of instrument. Information criterion penalising free parameters outperformed it on both axes (0.509/0.992 versus 0.376/0.978).

Non-retention therefore strong evidence against module where rule shown to have power and weak evidence where not. Reporting verdict without operating characteristics does not distinguish two. Pre-check diagnostic identifying in advance where rule has power remains open (dispersion Spearman 0.52 weak, margin 0.88 strong but circular and misclassifies stock-flow cells).

---

## Data availability

Rolling-origin pass costs 7.0 s at T=33 versus 45.6 s at T=71 single pass benchmark. Core design 10 cells ×200 replicates ×7.0 s = 14000 s = 3.89 h ≈4 h at T=33; T=71 extension for D1 and D5 800 passes ×45.6 s = 36480 s = 10.13 h ≈10 h; full factorial 2000 passes ×45.6 s = 91200 s = 25.33 h ≈25 h at T=71, not executed as full simulation. Independent rerun regenerated 30/30 files byte-identical, 29/29 checksum verified once. M1b optimum environment-sensitive ±1.6 kt at h=1 (151.6 versus 153.2) and ±17 kt at h=5 (445.5 versus 462.5), max ±17 kt.

All input data, analysis scripts, result files, frozen specifications are archived at https://github.com/MIKEAA2020/general-sustainability/tree/edwards-framework-e1 and https://zenodo.org/records/22553609 (E1) and 22552680 (E3). Companion papers: E1 cod forecast ladder and E3 Edwards forecast ladder.

Rolling summaries:
- `wave_e_cod/results/rolling_summary.csv` (Spec A regime+na filtered)
- `wave_e_cod/results/xte_rolling_summary.csv` (Spec B)
- `wave_e_edwards/results/rolling_summary.csv`
- `wave_e_cod/results/sim_retention_power.csv` (10,000 rows: 5 DGPs ×2σ×200×5 modules)
- `wave_e_cod/results/sim_misspecified_D6D7.csv` (Amendment 1: D6 r_t drifting, D7 obs-error-only, 8 cells 1,600 passes)
- `wave_e_edwards/results/e3_audit_uncertainty.json` (uncertainty layer, DM HAC + block bootstrap per Künsch 1989, p percentile-tail fraction)
- `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv` (independent replication, 32 rows, 15 CI exclude zero 1 Spec A +6 Spec B h1 +8 Spec B h5 and 17 include 7+8 Spec A +2 Spec B h1)
- `batch 7 (audits of agent arena 1 paper rewrites)/results/e3_dm_uncertainty.csv` (10 rows)

## References

Abaee, A., 2026a. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

Abaee, A., 2026b. Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

Carvalho, F., et al., 2021. A cookbook for using model diagnostics in integrated stock assessments. Fisheries Research 240, 105959.

DFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

Hyndman, R.J., Koehler, A.B., 2006. Another look at measures of forecast accuracy. International Journal of Forecasting 22, 679–688.

Kell, L.T., et al., 2016. Evaluation of the prediction skill of stock assessment using hindcasting. Fisheries Research 183, 119–127.

Kell, L.T., et al., 2021. Validation of stock assessment methods: is it me or my model talking? ICES Journal of Marine Science 78, 2244–2255.

Künsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. Annals of Statistics 17, 1217–1241.

Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2020. The M4 Competition: 100,000 time series and 54 methods. Int J Forecasting 36, 54–74.

Regular, P.M., et al., 2025. Assessment of the Northern cod stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.

Scanlon, B.R., et al., 2003. Barton Springs segment Edwards. Groundwater.

---

## Appendix — Verification

```
COD Spec A:
 h=5 M1b 288.58 vs persist 264.72 +9.01%
 h=5 M1 288.72 vs persist 264.72 +9.07%
 h=1 M1b 114.80 vs persist 98.05 +17.09%

COD Spec B mixed-origin:
 h=5 M1 431.90 vs persist 317.71 +35.94%
 h=1 M1 119.47 vs persist 87.65 +36.30%
 h=5 M1b 445.48 vs persist 317.71 +40.22%

COD Spec B origin-matched:
 h=5 M1 431.90 vs persist 299.98 +43.99%
 h=1 M1 119.47 vs persist 84.43 +41.55%

COD capelin module origin-matched:
 Spec A 150.02/262.34 vs persist 97/193 loses every cell
 Spec B 132.02/491.74 vs persist 79/288 loses every cell

EDWARDS:
 h=5 M2m 17.4449 vs persist 21.1056 -17.34%
 h=1 M2m 12.2832 vs persist 13.2301 -7.16% only separated
 h=1 M1 12.8391 vs persist 13.2301 -2.96% coin-flip
 h=1 oracle 7.5467 vs persist 13.2301 -42.96%
 h=5 oracle 10.8645 vs persist 21.1056 -48.65%

EDWARDS gate decomposition:
 M2m h=1: 12.2832 vs persist 13.2301 (band 12.5686) -> H2 pass | vs M1 12.8391 -> H1 FAIL (4.33%)
 M2m h=5: 17.4449 vs persist 21.1056 (band 20.0503) -> H2 pass | vs M1 21.2514 -> H1 pass
 M1 h=1: 12.8391 vs persist 13.2301 (band 12.5686) -> H2 FAIL
 M1 h=5: 21.2514 vs persist 21.1056 (band 20.0503) -> H2 FAIL

SIMULATION:
 D1 0.965/0.985 power exceeds 80% bar
 D2 0.710/0.130 near bar / below
 D3 0.090/0.110 below bar <20% chance
 D4 0.005/0.015 below bar
 D5 specificity 0.985/0.970
 False retention: 0.044 per module-replicate pair D1-D4 wrong-module,
 0.015-0.030 per replicate D5, 0.005 per module null
 D6 0.680/0.760 D7 0.975/0.925 vs 0.10 threshold — specificity conditional
```

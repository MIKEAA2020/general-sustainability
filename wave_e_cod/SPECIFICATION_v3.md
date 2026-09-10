# Specification sheet v3 — Northern cod (NAFO 2J3KL), demographic-timing ablations Ω_lag

**Sheet status: PRE-REGISTRATION — LOCKED, NO SCORES COMPUTED.**

**Issued 10 Sep 2026, before any model in this sheet has been fitted, scored, or
inspected.** This is the condition that gives the sheet its value; if any element below is
changed after a score exists, the change must be recorded as a dated amendment and the
affected result reported as exploratory.

---

## 0. Relationship to `SPECIFICATION_v2.md`

**v3 does not amend, relax, supersede, or reopen v2.** It is a new frozen object scored
separately. Every v2 verdict — no module retained on Ω_2016 or Ω_xte, persistence
unbeaten on the pooled primary score, collapse window missed by every model — stands
untouched and is not re-derived, re-scored, or contradicted here.

This matters because v2's authority rests on the bar having been fixed before the scoring.
Three rounds of audit have since argued the ecology is thin. Widening v2 to admit modules
those audits suggested would convert a pre-registered negative result into a post-hoc
search. The correct response is a **new** pre-registration, which is this sheet.

**Reporting rule (binding).** Every model in this sheet is reported as an **ablation
outside the five-rung ladder**, in the manner of the capelin pass recorded in
`E1_SUPPLEMENTARY.md` SI-1. No result here can retain a v2 module, promote one, or alter a
v2 retention verdict. If an Ω_lag model outperforms persistence, that is a finding about
Ω_lag and is reported as such.

**What v3 deliberately does not change:** the predictand, the two specifications and the
no-pooling rule (R04), the retention rule and its 5% tie band, the estimator, the rolling
origin construction, the primary score, and the standing disclosure that the v2 object is
one pool with no age structure and no migration.

---

## 1. Motivation, stated before the results

`SPECIFICATION_v2.md` §4 discloses: *"One pool, no age structure, no migration (A014-L
list)."* The round-3 audits (gpt §3, grok §4, qwen 3.2/3.6) independently argued that this
disclosure is not a footnote but the substantive limitation: every module in the v2 ladder
transmits information at lag 0–1, while the biological pathways proposed for this stock
operate at multi-year delays.

The published maturity schedule makes that quantitative. Cadigan (2016), the NCAM methods
paper, gives beginning-of-year proportions mature by stock age:

| stock age | 2 | 3 | 4 | 5 | 6 | 7 | 8+ |
|---|---|---|---|---|---|---|---|
| proportion mature | 0.00 | 0.00 | 0.05 | 0.35 | 0.79 | 0.97 | 1.00 |
| weight (kg) | 0.10 | 0.28 | 0.60 | 1.03 | 1.57 | 2.29 | 3.16+ |

Age at 50% maturity falls between ages 5 and 6. A cohort recruiting at age 2 therefore
enters the spawning stock about **four to five years later**. This is an externally
published schedule, not a quantity fitted here.

**The hypothesis under test is therefore a timing hypothesis, not a "more structure"
hypothesis:** if the v2 ladder fails partly because its modules are mis-timed rather than
because added structure is useless, then information entering at the delay the maturity
ogive specifies should behave differently from the same information entering at lag 0.

---

## 2. Declared lags — fixed before scoring

**This is the element most exposed to post-hoc selection and is therefore pinned hardest.**

| pathway | declared lag | source of the declaration |
|---|---|---|
| recruitment → SSB | **ℓ = 4 and ℓ = 5 years** | Cadigan (2016) maturity ogive, A50 between ages 5 and 6 |
| condition / growth → SSB | **ℓ = 0 and ℓ = 1 years** | contemporaneous pathway; the v2 capelin modules already occupy it and serve as the null |

**Primary declared lag: ℓ = 5** (single value, chosen because A50 sits between 5 and 6 and
5 is the shorter, more conservative delay). ℓ = 4 is the single declared sensitivity.

**Lags 2, 3, 6 and 7 are excluded by this sheet.** They may be computed and archived for
completeness but are **not eligible to support any claim**, because a scan over six lags
on twenty origins will locate an apparent effect by chance. Any statement resting on a
non-declared lag must be labelled exploratory.

**A prior evaluator's descriptive correlation is on record and is not evidence here.**
`E1_AUDIT_ROUND3_JOINT_EVALUATION.md` §6.2 reports post-collapse detrended correlations
peaking at lags 4–5 (+0.74, +0.75 on n = 16, 15). That calculation used the full series,
is in-sample, is not a forecast, and was performed before this sheet. It motivated the
declaration; it does not corroborate the result. The scored test must stand alone.

---

## 3. Object Ω_lag-R — recruitment-timing ablation

| Element | Frozen value |
|---|---|
| **Predictand** | Unchanged from Ω_2016: NCAM M-shift SSB, DFO 2016 Table A2, 1983–2015, kt |
| **Covariate** | `age2_millions` from `data/ncam_2016_table_a2.csv` — NCAM's estimated number at age 2, the recruitment series of the assessment's Figure 8 |
| **Model** | `ΔŜ_t = α + β S_t + γ R_{t−ℓ}`, one-step, ℓ = 5 primary and ℓ = 4 sensitivity |
| **Comparators** | (i) the same model with γ ≡ 0 (level-only), (ii) last-value persistence on matched origins |
| **Estimation** | One-step least squares, training window only, no bounds beyond finiteness; refit at every origin |
| **Information rule** | `R_{t−ℓ}` must be dated at or before the forecast origin. With ℓ ≥ 4 this is automatic, and no future-dated value may enter |
| **Origins** | The ladder's own rolling origins; the covariate lag reduces the usable set, and the realised n is reported, not chosen |
| **Score** | Rolling RMSE at h = 1 and h = 5, origin-matched against persistence |
| **Status** | **Ablation. Outside the ladder. Cannot retain or promote any v2 module.** |

**Declared interpretation, written before the result.** Three outcomes, each already
assigned a meaning so that none can be reinterpreted favourably afterwards:

- **γ improves forecasts at the declared lag:** the v2 non-retention is partly a timing
  failure, and the missing structure concerns *when* information enters rather than *how
  much* structure is added.
- **γ does not improve forecasts:** the demographic covariate available at the assessment
  level does not repair the ladder, which strengthens v2's conclusion rather than
  weakening it.
- **γ improves in-sample but not out-of-sample:** the covariate is descriptive of the
  reconstruction, not predictive — the outcome qwen 3.2 explicitly anticipated.

**Known limitation, disclosed in advance:** `age2_millions` is an assessment *output*, not
an independent observation. Forecasting a reconstructed SSB using a reconstructed
recruitment series from the same assessment shares estimation error between predictor and
predictand. This is a weaker design than an independent survey covariate and the result
must carry that caveat wherever it is reported.

---

## 4. Object Ω_lag-C — capelin transmission-timing ablation

| Element | Frozen value |
|---|---|
| **Covariate** | Observed acoustic capelin index, `data/capelin_acoustic_observed.csv`, observed years only, **no interpolation** (unchanged from the v2 capelin pass) |
| **Model** | Surplus scaled by `(I_{t−ℓ}/I_ref)^b`, with `I_ref` the training-window median, exactly the v2 functional form with the lag inserted |
| **Declared lags** | ℓ = 5 primary (recruitment pathway), ℓ = 4 sensitivity; ℓ = 0 retained as the pre-existing null |
| **Origins** | 30 observed capelin years, 25 overlapping the NCAM window; at ℓ = 5 approximately 20 usable origins. **The realised n is reported and is small** |
| **Score** | As Ω_lag-R |
| **Status** | **Ablation. Outside the ladder.** |

**Declared limitation of the functional form.** As established in E1 v27 §3.4, the
multiplicative factor is strictly positive, so the module can shrink production but cannot
make it negative regardless of the sign of `b`. Inserting a lag does **not** repair this.
Ω_lag-C therefore tests *timing within the multiplicative pathway* and cannot test
food-limitation severe enough to drive a net loss. That would require the additive
loss form `−μ S_t d(I_{t−ℓ})` proposed by gpt §4, which **this sheet does not authorise**;
it is a different functional class and would need its own pre-registration.

---

## 4b. Object Ω_pit — high-threshold (predator-pit) ablation

Added on review of grok D(1). **Rationale corrected after round-4 audit item F2.** The
*scored* estimator bounds `𝔰 ∈ (0, max(S0))`, where `S0` is the **predictor** states, so
the recovery-window bound is **40.83 kt** (`run_ladder.py` line 85); the *profile
diagnostic* uses `[0, min_train S] = [0, 9.68]` kt. Both therefore exclude a
predator-pit threshold. An earlier draft of this sheet gave the bound as 81.10 kt — the
maximum over all states including the terminal response — and concluded that a high
threshold was not excluded; that is withdrawn (round-5 item G1).

What Ω_pit tests is therefore exactly what the scored ladder could not: a threshold above
`max(S0)`. The depensation factor `a(S) = (S − 𝔰)/(K − 𝔰)` turns negative for 𝔰 above the
observed range — at 𝔰 = 50 kt all 12 recovery-window predictor states have `a(S) < 0` —
so such a model predicts negative production across the window, which the scored
objective both excludes by its range bound and penalises. Ω_pit lifts the range bound and
accepts the negative-surplus prediction as the model's depensatory content, then scores it
out-of-sample. Its result is informative either way: a pit that forecasts better than
persistence would show the v2 verdict was a statement about the feasible set, and one that
does not would show widening the range does not rescue depensation.

| Element | Frozen value |
|---|---|
| **Model** | M1b's functional form with `𝔰` allowed on `(min_train S, max_train S]` and beyond, and negative `a(S)` accepted as the model's depensatory prediction rather than penalised |
| **Declared thresholds** | 𝔰 ∈ {25, 50, 75, 100} kt, fixed before scoring; the profile over this grid is the reported object |
| **Estimation** | `r` and `K` re-optimised at each fixed 𝔰, training window only, refit at every origin |
| **Score** | Rolling-origin RMSE at h = 1 and h = 5, origin-matched against persistence — **out-of-sample, never a fit to the test window** |
| **Status** | **Ablation. Outside the ladder. Cannot retain or promote any v2 module.** |

**Recorded in advance so it cannot be mistaken for a result.** A capacity check fitting the
2008–2015 rebuild *directly from the 2007 state* gives 18.7 kt at 𝔰 = 50 kt against 103.8
kt for persistence. That is a fit to the test window, it depends on `r` pinning at its
upper bound of 2.0, and it degrades to 104.8 and 124.4 kt at K = 1000 and 5000. It
demonstrates only that the class can represent the rebuild. **It is not skill, it must
never be quoted as skill, and Ω_pit exists precisely to replace it with an honest
out-of-sample score.**

**Declared interpretations.** If a high threshold forecasts better than persistence
out-of-sample, the v2 M1b verdict was a statement about the feasible set rather than about
depensation, and that is the finding. If it does not, then depensation is not rescued by
widening the threshold range, which strengthens v2. If it fits in-sample and fails
out-of-sample, the pit is descriptive of the reconstruction only.

---

## 5. What is explicitly out of scope

| Excluded | Reason |
|---|---|
| Full cohort projection `Ŝ_{t+1} = Σ_a N_{a,t}e^{−Z}w_{a+1}m_{a+1} + R̂w₀m₀` | Requires numbers-at-age by year; the assessment publishes figures, not the N matrix. Not obtainable from repository data |
| Four-way ΔSSB decomposition (survival / growth / maturity / recruitment) | Same missing N matrix |
| Recruitment depensation `R_t = f(S_t)` with threshold | Requires a stock–recruit model this programme does not build |
| Seal / predation module | Requires a harp seal index not in the repository; severe collinearity with capelin |
| Time-varying or random-walk productivity | Not identified on these windows (collapse window fixes only the product `rS(1−S/K)`; recovery window flat in `K` over 60–5000 kt). A free state per year on 33 observations would fit the reconstruction and forecast nothing. Predeclared breaks are the identifiable version and belong to the regime companion |
| Additive food-deficit loss term | Different functional class (see §4) |
| Any change to the v2 ladder, estimator, retention rule, tie band, or scoring rule | v2 is frozen |

---

## 6. Verification gate

Before any Ω_lag result may be reported:

1. `manuscript_style_scan.py` — 0 blockers.
2. `tier3_guard.py BASE.tex NEW.tex --si E1_SUPPLEMENTARY.md` — 0 blockers.
3. Compile from `paper rewrites/`.
4. `tier3_guard_selftest.sh` — 5/5.
5. **v2 verdict invariance check:** every v2 retention verdict, score and table value is
   byte-identical to the v26/v27 record. Any change is a blocker, not a finding.
6. **Lag-declaration check:** every reported claim rests on ℓ ∈ {0, 1, 4, 5}. A claim
   resting on any other lag is exploratory and must be labelled so.

---

## 7. Standing disclosures

- The covariate is an assessment output; predictor and predictand share estimation error
  (§3).
- The realised origin counts are small (≈20 at ℓ = 5 for Ω_lag-C). Sample sizes suffice to
  order models; they do not suffice to certify a small skill difference. The v2 language
  on this point applies unchanged.
- These objects are not pooled with Ω_xte, with the Edwards object, or with each other
  beyond the shared reporting table. R04 continues to forbid judgment transfer.
- This sheet creates no theorem and changes no admission or gate status.
- Nothing here is an operational forecast test; the conditional-hindcast caveat of the
  main paper applies unchanged.

---

## 8. Authorisation status

**This sheet is written and locked. No model in it has been run.**

It is presented for a decision on whether the Ω_lag programme should proceed. Running it
is optional: E1 v27 already states the timing argument as a specification limitation, with
the published maturity ogive as its warrant, and needs no new score to do so. The value of
executing v3 is that it converts a stated limitation into a tested one.

# E1 — Deferred and declined audit items: disposition and forward programme

**Companion to:** `E1_AUDIT_ROUND3_JOINT_EVALUATION.md`
**Scope:** every round-3 item not implemented in the manuscript, with a ruling on whether
it is (a) implementable now, (b) a declared additional pass, (c) a different paper, or
(d) permanently declined.
**Date:** 10 Sep 2026

---

## 1. Why this document exists

The round-3 evaluation ruled on sixteen items and implemented seven. The remaining nine
were marked deferred or declined, and a decline recorded only as a table cell is a decline
that will be re-litigated by the next auditor. Two of the nine turned out, on inspection,
to be **stronger than their original ruling** — one of them materially qualifies a claim
the manuscript currently makes without qualification.

Each item below states what it is, whether it can be run on data in hand, what it would
change, and where it belongs.

---

## 2. E9 — Regime-split RMSE: **upgraded to Tier 2, implement in E1**

*Auditors: grok F, qwen 3.4.* Originally deferred as "attractive, out of frozen spec".
**That ruling was wrong, and the item is the most valuable thing in the deferred set.**

### 2.1 It needs no new specification

Regime-splitting **re-partitions origins that have already been scored**. It refits
nothing, adds no module, changes no retention rule, and uses only the archived per-origin
file `results/xte_rolling_forecasts.csv`. The frozen specification fixes the ladder, the
estimator and the scoring rule; it does not forbid reporting the same scores grouped by
period. This is reporting, not re-specification.

### 2.2 What it shows (computed, h = 1, Specification B, no refit)

| band | n | persist | M1 | M1b | M2 | M3 | M4 | lowest |
|---|---|---|---|---|---|---|---|---|
| pre-1991 | 26 | **94.7** | 142.4 | 186.4 | 184.2 | 166.3 | 260.6 | persist |
| 1991–1995 | 5 | 167.0 | 126.8 | **66.6** | 299.8 | 154.8 | 321.6 | M1b |
| 1996–2012 | 17 | 20.7 | 75.0 | 75.0 | 26.3 | **19.7** | 24.0 | M3 |
| 2013–2024 | 11 | **61.0** | 112.3 | 174.5 | 160.5 | 96.4 | 136.3 | persist |

**Persistence does not win in every regime.** Pooled over all origins it does, which is
what the manuscript reports; split by regime, structural modules read lower in the
collapse band and in the rebuilding band. This is precisely grok's point that Table 4
mixes "useless at turning points" with "acceptable inside a regime".

### 2.3 Robustness — checked, and the two exceptions behave differently

- **Collapse band (1991–1995), M1 and M1b below persistence.** n = 5, so I ran
  leave-one-out: dropping any single origin leaves M1 below persistence in **all five**
  cases (78.8/118.6/141.3/141.6/141.5 against 139.6/127.4/184.5/186.6/186.7). The ordering
  is stable. It is still five points and must be reported as such.
- **Rebuilding band (1996–2012), M3 below persistence.** The gap is **+0.93 kt** on a
  20.67 kt baseline. The 5% tie band is 1.03 kt, so **the gap is inside the tie band**, and
  a 20,000-replicate moving-block bootstrap gives 95% CI **[−14.20, +14.88] kt**, which
  includes zero. **This is a tie, not a win.**

### 2.4 Consequence for the manuscript

The retention verdict is **unchanged** — the rule scores pooled rolling RMSE at both
horizons, and the one sub-band where a module reads lower is inside the tie band that the
rule itself declares non-deciding. But the *interpretation* needs a sentence it does not
currently have: the pooled result aggregates regimes in which persistence wins by a wide
margin with a collapse band in which it does not, so "no module beats persistence" is a
statement about the pooled score and not about every period.

Withholding that would be reporting the favourable aggregation only.

**Disposition: implement in E1 as a supplementary table + one Discussion sentence.
No spec change.**

---

## 3. E10 — Apparent-production figure: **implement in E1**

*Auditors: grok A, qwen 3.3.* Plot `P_t = S_{t+1} − S_t + C_t` against `S_t` with the
fitted collapse- and recovery-window Schaefer curves overlaid.

Uses only quantities already in the paper (§3.2 already discusses apparent net
production). It is a plot of existing data, not a new analysis, and it makes visible in
one panel what §3.2 currently argues in prose: the 1991–93 points sit below any fitted
dome, and the recovery-window curves are indistinguishable over the observed range but
diverge wildly on extrapolation.

Must be captioned as a diagnostic construct, not a mass balance — the SSB-versus-landings
caveat already in the paper applies unchanged.

**Disposition: implement in E1 as one figure. No spec change.**

---

## 4. E11/E12 partial — recruitment lag and capelin lag scan: **declared additional pass**

Established in `E1_AUDIT_ROUND3_JOINT_EVALUATION.md` §6: the NCAM maturity ogive
(Cadigan 2016) puts A50 between ages 5 and 6, the repository already holds NCAM's age-2
recruitment series, and the post-collapse detrended signal peaks at **lags 4–5**, where
the ogive predicts. The capelin lag scan has 20 usable origins.

These **add rungs**, so they need `SPECIFICATION_v3.md`. See §8 for whether that is
warranted.

**Disposition: additional pass, gated on a written v3. Prose statement of the
lag-mismatch argument goes into E1 now, without any new score.**

---

## 5. Items that are a different paper — documented, not abandoned

### 5.1 E15 — Management strategy evaluation *(qwen 3.13)*

Correct and important: catch is endogenous, management responds to assessment state, so a
hindcast conditional on realised catch cannot evaluate management value. But this is a
closed-loop simulation study — operating model, observation model, harvest control rule,
feedback — and it answers a different question from "does added structure forecast better
than persistence". It is also substantially the design of the **companion intervention
paper (E2)**, which already carries the governed-surplus object, the uncertainty classes
and the harvest-control family under `protocol_intervention.md`.

**Disposition: out of scope for E1; overlaps E2's existing design. Recorded as the
natural extension of the E2 line, not of E1.**

### 5.2 E11 full — N-matrix ΔSSB decomposition *(gpt §3, qwen 3.3, grok G)*

Requires numbers-at-age by year, which the assessment publishes as figures rather than as
a matrix. Obtaining it means a data request to DFO or digitising assessment output. That
is a data-acquisition project with its own provenance and admission requirements.

**Disposition: separate project. Prerequisite is the N matrix; without it the
decomposition cannot be attempted and should not be promised.**

### 5.3 E12 remainder — recruitment depensation and seal predation — **PARTLY REVISED**

**Recruitment depensation** `R_t = f(S_t)` with a threshold: the ingredients exist — the
repository holds NCAM's age-2 recruitment series and SSB — so a depensatory
stock–recruit fit is buildable. It is nonetheless a **different object**: it forecasts
recruits, not SSB, so it cannot be scored against this paper's predictand or its retention
rule without a cohort projection to carry recruits into spawning biomass, and that
projection needs the N matrix (§5.2). **Delegated unaltered to the ecosystem/recruitment
successor, with the N-matrix requirement named as its prerequisite.**

**Seal predation.** My stated reason — "needs a harp seal index that is not in the
repository" — is half right and was, again, asserted rather than checked. A search shows
DFO publishes a **modelled annual abundance series** for Northwest Atlantic harp seals
(2024 assessment: 4.4 million, 95% CrI 3.65–5.35; peak 7.5 million in 1998; the
Wiley/ESA population model gives annual estimates 1951–2019 with intervals). The series is
obtainable and covers the study period. It is *not in this repository*, which is a
data-acquisition statement, not an impossibility.

The substantive objection survives and is the one that should have been given first:
harp seal abundance rose monotonically through the 1970s–1990s and fell after 1998, so on
33 annual observations it is close to a smooth trend, and it is **collinear with both the
capelin collapse and the productivity decline the paper already documents**. Fitted as an
additive mortality term it would absorb the same variance as the implied-productivity
signal in v28 §3.2 without identifying a mechanism. That is a reason grounded in the data,
not in the specification.

**Disposition: delegated unaltered to an ecosystem-driver paper, where a predator index
can be fitted jointly with prey and temperature and the collinearity addressed by design
rather than ignored. Data acquisition is a named prerequisite, not a barrier.**

### 5.4 E6 redesign — ecological threshold metrics *(qwen 3.10)* — **RULING REVISED**

The **diagnosis** is accepted and implemented (Brier is degenerate on Specification A:
0 of 26 origins lie at or above the 884.6 kt LRP — verified).

My original ground for declining the **redesign** was that it "requires predictive
distributions the deterministic forecast convention does not produce." **A web search of
the assessment literature shows that ruling was wrong**, and wrong in the same way as the
E11/E12 decline: I inferred unavailability instead of checking.

DFO's Northern cod assessments publish **95% confidence intervals on SSB in every
reporting year** — the 2024 assessment gives SSB = 342 kt (95% CI 246–475 kt), and the
2016 assessment gives 300 kt (95% CI 246–362 kt). More to the point, those bounds are
**already committed in this repository**: `data/xtencam_table17_ssb.csv` carries
`ssb_lo` and `ssb_hi` for all **71** years, with a median relative CI width of 0.44. I had
been reading that file for months and using only the point column.

So an uncertainty band on the *predictand* exists. That does not by itself make the
ladder's forecasts probabilistic — the forecast convention is still deterministic — but it
makes a genuine probabilistic diagnostic available immediately: score the deterministic
forecasts against the assessment's own uncertainty at the target year. Computed on the
archived per-origin file, h = 1, Specification B, n = 59, taking
σ = (hi − lo)/(2 × 1.96) at each target year:

| forecast | truth within ±1.96σ of the forecast | nominal |
|---|---|---|
| persistence | **33/59 = 56%** | 95% |
| M1 | **21/59 = 36%** | 95% |

Both badly under-cover, and persistence under-covers substantially less than M1. This says
something neither RMSE nor the degenerate Brier says: the ladder's errors are large
**relative to the assessment's own stated uncertainty**, so the forecast failure is not
hidden inside assessment noise. It is also the ecologically meaningful version of what
qwen asked for, and it needs no new model and no scoring-rule change.

**Revised disposition.**
- **Implementable now, and not a scoring-rule change:** coverage of the deterministic
  forecasts against the published assessment CI, reported as a diagnostic alongside RMSE.
  This does not replace the retention score and cannot alter a verdict.
- **Requires a new object (soften the rule via v3, not the proposal):** the full redesign
  qwen specifies — P(S_{t+h} < S_t), rebuilding risk, CRPS, asymmetric loss — needs
  *forecast* distributions, not just predictand uncertainty. That means residual-bootstrap
  or state-space predictive intervals, which is a genuine change to the forecast
  convention and therefore belongs in a pre-registered object. The proposal is not
  weakened; the rule is what gives way.

**Correction to my own record:** "requires predictive distributions" was a real
constraint for the *full* redesign and a false one for the coverage diagnostic. Stating
them as one thing let a feasible item ride out on an infeasible item's justification.

---

## 6. Items that remain declined on the merits

**Standard applied.** "It is outside the frozen specification" is a statement about
bookkeeping, not about science, and it is not on its own a reason to decline anything. A
frozen specification exists to stop a preregistered negative result being rewritten after
the fact; it does not exist to protect the paper from valid criticism.

Each item is therefore judged first on whether **the proposal is valid**. A valid proposal
is never weakened, trimmed, or reinterpreted to fit the specification — the proposal
stands as its author made it. What is adjustable is the *rule*, not the science. So a
valid proposal has exactly two admissible dispositions:

1. **Soften the frozen-specification rule** so the proposal can be implemented as stated,
   in a new pre-registered object that leaves v2's verdicts intact; or
2. **Delegate the proposal, unaltered, to another paper** with a named destination.

Silence is not a disposition, and neither is diluting the proposal until it fits.

| Item | Ruling |
|---|---|
| **E13** — refit M1b with 𝔰 above max training S *(grok D(1))* | **Valid, and my original decline was too quick — see §6.6.** Delegated to `SPECIFICATION_v3.md` as object Ω_pit, not silenced. |
| **E14** — time-varying / random-walk productivity *(qwen 3.5)* | **Valid proposal, delegated — see §6.7.** The reason is not "frozen spec" but that the item is already the subject of a companion object, and that a random-walk `r_t` is unidentifiable on these windows for a reason the paper can state. |
| **E16** — drop Prop 4.1 etc. from introduction *(grok §6)* | Already done in v24; grok is reading pre-v24 text. Companion citations stay by standing policy. This is the one genuine non-item. |

---

## 6.6 E13 revisited — the predator-pit refit is a real test, and it is now specified

grok's D(1) asks for M1b refitted with the Allee threshold allowed *above* the training
range, so that a predator pit can be represented. I declined it by pointing at the
estimator's feasibility restriction. That was bookkeeping, not a scientific answer, and
checking the mathematics shows the proposal has content.

The depensation factor is `a(S) = (S − 𝔰)/(K − 𝔰)`. On the recovery window the observed
SSB spans 9.68–81.10 kt, so:

| 𝔰 (kt) | observed recovery states with `a(S) < 0` |
|---|---|
| 9.68 (the current bound) | 0 of 13 |
| 50 | 12 of 13 |
| 100 | 13 of 13 |

**The current bound does not merely restrict the threshold — it selects the one region
where the model cannot express depensation at all.** Every 𝔰 that would represent a
predator pit implies negative surplus across the observed range, which the estimator
forbids by construction. So "M1b was not retained" carries no information about high
thresholds: the hypothesis was excluded by the feasible set, not tested and rejected.

A capacity check confirms the model class *can* represent the trajectory. Fitting the
2008–2015 rebuild directly from the 2007 state gives a test-window RMSE of 18.7 kt at
𝔰 = 50 kt against 103.8 kt for persistence. **This is a fit to the test window, not a
forecast, and it must not be reported as skill** — and the 18.7 kt figure depends on `r`
sitting at its upper bound of 2.0, with K = 1000 and 5000 giving 104.8 and 124.4 kt. The
honest reading is narrow: a threshold above the data is representationally capable of the
rebuild, and the current specification cannot see it.

**Disposition: delegate to `SPECIFICATION_v3.md` as a third object, Ω_pit** — M1b with
𝔰 allowed above `max_train S`, negative `a(S)` accepted as the depensatory prediction,
scored out-of-sample on rolling origins like everything else. It is *not* a softening of
v2: v2's M1b verdict stands, and gains the sharper interpretation above. The paper keeps
grok's D(2) sentence, which v27 already carries.

## 6.7 E14 revisited — why time-varying productivity is delegated, on the merits

qwen 3.5 is right that the ecological history is non-stationary and that constant-`r`
models are brittle. v28 now *demonstrates* this rather than asserting it: the implied
productivity series runs +1.82 before 1991, negative through 1991–94, then +0.37 and
+0.25. So the diagnosis is accepted and in the paper.

The reason not to add a random-walk `r_t` module to E1 is not that the specification
forbids it. It is that **on these windows it would not be identified, for the same reason
already documented in the paper**: the collapse window fixes only the product `rS(1−S/K)`,
and the recovery window is flat in `K` over 60–5000 kt. A latent `r_t` following a random
walk adds one free state per year to a series with 33 annual observations and an
unidentified `K`; it would fit the reconstruction and forecast nothing, which is precisely
qwen's own "explains reconstruction changes but does not improve forecasts" outcome.

Predeclared regime breaks (qwen's option 1) are the identifiable version, and those are
**already the companion capelin/regime object** — a 1991 break in `r` was scored and not
retained. Adding a second, differently-broken version to E1 would duplicate it.

**Disposition: diagnosis implemented in E1 v28; the module delegated to the regime
companion, where the identification problem can be addressed with a stated break rather
than a free state.**

---

## 7. Summary of dispositions

| Item | Ruling | Where |
|---|---|---|
| E9 regime-split RMSE | **upgraded → implement** | E1 v27, SI table + 1 sentence |
| E10 production figure | **implement** | E1 v27, 1 figure |
| E11/E12 lag argument (prose) | **implement** | E1 v27, specification limitation |
| E11/E12 lag scan (scored) | additional pass | `SPECIFICATION_v3.md` |
| E6 diagnosis | implemented | E1 v27 |
| E6 coverage diagnostic | **implementable now (was declined)** | E1, alongside RMSE |
| E6 full probabilistic redesign | soften rule via new object | `SPECIFICATION_v3.md` |
| E15 MSE | different paper | E2 line |
| E11 full decomposition | different project | needs N matrix |
| E12 recruitment depensation | delegated unaltered | recruitment successor (needs N matrix) |
| E12 seal predation | delegated unaltered (data exists, collinearity is the issue) | ecosystem-driver paper |
| E13 predator-pit refit | **delegated (was declined)** | `SPECIFICATION_v3.md` object Ω_pit |
| E14 time-varying productivity | diagnosis implemented; module delegated | E1 v28 §3.2; regime companion |
| E16 | already done in v24 | — |

---

## 8. Does the frozen specification merit softening?

**No — and it does not need to be softened for any item above.**

### 8.1 The question is narrower than it first appears

Only one class of work requires touching the spec: adding a scored rung (the recruitment
covariate at lag 4–5, the capelin lag scan, time-varying productivity). Everything else in
§7 — the regime split, the production figure, the Brier diagnosis, the lag-mismatch prose
— is **reporting or interpretation of already-scored artifacts** and needs no change at
all. I initially deferred E9 as "out of frozen spec"; that was a misreading of what the
spec constrains. It fixes the ladder, the estimator and the scoring rule. It does not fix
how results are grouped for presentation.

### 8.2 Softening would destroy the paper's main asset

E1's central claim is a **negative** result: no module is retained. A negative result is
credible exactly in proportion to the reader's confidence that the bar was fixed before
the scoring and not adjusted afterwards. The specification sheet is what supplies that
confidence, and it is externally verifiable — 29/29 pinned hashes, 30/30 result files
byte-identical on independent rerun.

Relaxing the spec *after* three rounds of auditors have said the ecology is thin, in order
to admit modules chosen because the audits suggested them, would convert a preregistered
negative result into a post-hoc search. The manuscript already discloses that the passes
evolved 1→6 with extensions declared in the manuscript rather than pre-registered; that
disclosure is a recorded weakness. Adding more post-hoc rungs would deepen exactly the
weakness the sheet already admits.

### 8.3 The spec already anticipated this objection

`SPECIFICATION_v2.md` §4 standing disclosures reads:

> "One pool, no age structure, no migration (A014-L list)."

**The absence of age structure is a declared limitation of the frozen object, not an
oversight the auditors discovered.** The correct response to "you should have age
structure" is therefore not to quietly add it, but to point at the disclosure and say the
scored object is a one-pool biomass ladder by construction. That is a stronger position
than a relaxation.

### 8.4 The right mechanism already exists, and there is precedent

The standing rule is that new work needs a justified `SPECIFICATION_v3.md`. That is the
mechanism, and it does not require *softening* v2 — v3 is a **new frozen object**, scored
separately, with its own pre-registration. v2's verdicts stand untouched.

There is also a precedent for how to add a model without contaminating the ladder: the
capelin pass was added after scoring began and is reported as **its own ablation outside
the five-rung ladder**, not as a retained rung (`E1_SUPPLEMENTARY.md` SI-1). The
recruitment and lag-scan work should follow that pattern exactly — reported as ablations,
explicitly outside the scored ladder, unable to alter a retention verdict.

### 8.5 Recommendation

1. **Do not soften `SPECIFICATION_v2.md`.** No item requires it; the disclosure in §4
   already covers the auditors' main criticism; and softening would damage the negative
   result that is the paper's contribution.
2. **Implement E9, E10, E6-diagnosis and the lag-mismatch prose in E1 v27** — none of
   these touch the spec.
3. **If the recruitment and capelin-lag work is wanted, write `SPECIFICATION_v3.md` as a
   new pre-registered object** before running anything, following the capelin-ablation
   precedent: scored separately, reported outside the ladder, incapable of changing a v2
   verdict. The lag of 4–5 years must be **declared from the published maturity ogive
   before scoring**, not selected by best fit — otherwise the lag scan is a search over
   six lags on twenty origins and will find something by chance.

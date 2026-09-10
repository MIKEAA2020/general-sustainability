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

### 5.3 E12 remainder — recruitment depensation and seal predation

Recruitment depensation `R_t = f(S_t)` with a threshold needs a stock–recruit model this
paper does not build. The seal module needs a harp seal abundance index that is not in the
repository and would be severely collinear with capelin. Both are plausible ecology and
neither is testable here.

**Disposition: declined for E1; recorded as candidate content for an ecosystem-driver
paper that would need new data.**

### 5.4 E6 redesign — ecological threshold metrics *(qwen 3.10)*

The **diagnosis** is accepted and implemented (Brier is degenerate on Specification A:
0 of 26 origins lie at or above the 884.6 kt LRP — verified). The **redesign** —
P(S_{t+h} < S_t), rebuilding risk, CRPS, asymmetric loss — replaces the scoring rule,
which is a frozen element. It also requires predictive distributions the deterministic
forecast convention does not produce.

**Disposition: diagnosis in E1; redesign belongs to a probabilistic-scoring study.**

---

## 6. Items that remain declined on the merits

| Item | Reason |
|---|---|
| **E13** — refit M1b with 𝔰 above max training S *(grok D(1))* | The estimator's feasibility restriction `0 < 𝔰 < 0.8K` and the non-negativity of `a(S)` are frozen estimation elements. grok's own alternative D(2) — state that M1b cannot represent a threshold above the collapsed range — is honest, costs one sentence, and is implemented. |
| **E14** — time-varying / random-walk productivity *(qwen 3.5)* | A new model class, not a rung. Also the direct subject of the companion capelin/regime work. Would need v3 and would not change the tested question. |
| **E16** — drop Prop 4.1 etc. from introduction *(grok §6)* | Already done in v24; grok is reading pre-v24 text. Companion citations stay by standing policy. |

---

## 7. Summary of dispositions

| Item | Ruling | Where |
|---|---|---|
| E9 regime-split RMSE | **upgraded → implement** | E1 v27, SI table + 1 sentence |
| E10 production figure | **implement** | E1 v27, 1 figure |
| E11/E12 lag argument (prose) | **implement** | E1 v27, specification limitation |
| E11/E12 lag scan (scored) | additional pass | `SPECIFICATION_v3.md` |
| E6 diagnosis | implemented | E1 v27 |
| E6 redesign | different study | probabilistic scoring |
| E15 MSE | different paper | E2 line |
| E11 full decomposition | different project | needs N matrix |
| E12 seal / recruitment depensation | declined | needs new data |
| E13, E14, E16 | declined / already done | — |

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

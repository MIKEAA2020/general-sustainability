# E1 — Joint evaluation of two audits (round 4)

**Source:** `uploads/e1 audit 3.txt` (1,381 lines; gpt L9, grok L1087)
**Manuscript under review:** v29 (`E1_v29.tex`)
**Evaluator:** agent, 10 Sep 2026

---

## 0. What is different about this round

Rounds 1–3 audited work I inherited or wrote early. **This round audits the ecological
material I added in v27–v29 in response to round 3.** Both auditors concentrate on the new
paragraphs, and they are largely right: three of my four new diagnostics contain a real
defect, and one of them is a defect I introduced while *fixing* an earlier decline.

That is the honest headline. The verification below is not a defence of the current text.

**Verified independently before ruling: every numerical claim was recomputed from
`gs_clone/wave_e_cod/` source data and, where relevant, by replicating
`run_ladder.fit_params` exactly.** `/tmp` had been cleared, so all checks were rerun from
the persisted clone.

---

## 1. Verdict summary

| # | Item | Auditor | Verdict |
|---|---|---|---|
| **F1** | Ridge refit does not reproduce the paper's own fit (r 1.76 vs 1.935) | grok 1.2 | **ACCEPT — my error, Tier 1** |
| **F2** | Allee bounds contradictory: max in §2.2, min in §3.2 | gpt 1.2, grok 1.3 | **ACCEPT — Tier 1; also invalidates my E13 reasoning** |
| **F3** | Coverage diagnostic is not coverage; σ assumes symmetric normal | gpt 1.1, grok 2.2 | **ACCEPT — Tier 1, my error** |
| **F4** | "one-fifth at any K" contradicted by my own K=5000 column | gpt 1.3B | **ACCEPT — my error** |
| **F5** | "undefined for K below stock size" is mathematically wrong | gpt 1.3A | **ACCEPT** |
| **F6** | 2008–2015 band needs S₂₀₁₆; period convention unstated | gpt 1.3C | **ACCEPT** |
| **F7** | Headline too broad given the regime split | gpt 1.4, grok 2.1 | **ACCEPT — Tier 1** |
| **F8** | M3 beats persistence on my own coverage diagnostic, unremarked | grok 2.2 | **ACCEPT — sharp catch** |
| **F9** | Intro structural bar refuted by §4's catch-dependence | grok 1.1 | **ACCEPT** |
| **F10** | Table 7/8 still use unmatched Spec B baseline | grok 1.5 | **ACCEPT** |
| **F11** | "five consecutive years, 1999–2004" is six years | grok 1.6 | **ACCEPT** |
| **F12** | Table 3 prints 0.00 for persistence sign-hit; text says NA | grok 1.4 | **ACCEPT** |
| **F13** | MASE described inaccurately | gpt 2.2 | **ACCEPT** |
| **F14** | "measured quantity" → assessment-derived | gpt 2.4 | **ACCEPT** |
| **F15** | Event-type attribution beyond what catch treatment identifies | grok 2.3 | **ACCEPT** |
| **F16** | Delay paragraph reinstates the causal claim it disclaims | grok 2.4 | **ACCEPT** |
| **F17** | Rose (2026) still used as mechanism proof | grok 2.5 | **PARTIAL** |
| **F18** | Literature-gap claim too categorical | gpt 2.3 | **PARTIAL** |
| **F19** | Model descriptions inconsistent (M1 "output-only" etc.) | gpt 2.8 | **ACCEPT in part** |
| **F20** | Delete the "scored test measures the penalty" sentence | gpt 2.6 | **ACCEPT** |
| **F21** | "retention rule coded before" → "scoring core" | gpt 2.7 | **ACCEPT** |

**Tier 1 (correctness): F1, F2, F3, F7. Accept: 17. Partial: 2.**

---

## 2. The four errors I introduced

### F1 — the identification ridge does not use the paper's estimator *(grok 1.2)*

grok says that if `r=1.935, K=1032.7` is the least-squares fit, re-optimising `r` at that
`K` cannot give `1.76`. **Correct, and the discrepancy is mine.**

I replicated `run_ladder.fit_params` exactly — objective `mean((pred − dS)²)` on
*increments*, `L-BFGS-B` from `x0=[0.3, max(1.5·maxS, 500)]`, bounds `r∈(1e-3,2]`,
`K∈[max(S0)+10, 5000]`:

```
r = 1.9350   K = 1032.72   MSE = 978.49     (paper prints 1.935 / 1032.7)
```

Exact reproduction. My v28/v29 ridge scan minimised a *different* objective (RMSE on
levels, flat C=240) and reported `r=1.76`, `RMSE 60.7→74.9`. Redone with the paper's own
objective:

| K (kt) | r* | MSE | RMSE (kt) | MSY = rK/4 |
|---|---|---|---|---|
| 1032.7 | **1.935** | 978.5 | **31.3** | 499.6 |
| 1500 | 0.674 | 3164.9 | 56.3 | 252.6 |
| 2000 | 0.492 | 3824.8 | 61.8 | 246.1 |
| 3000 | 0.388 | 4245.9 | 65.2 | 290.7 |
| 5000 | 0.331 | 4485.2 | 67.0 | 414.0 |

The corrected result **weakens my claim**: training RMSE rises 31.3 → 67.0, more than
doubling, where I reported a rise of 60.7 → 74.9. So the pre-collapse window is *better*
identified in `K` than I wrote, and the ridge language must be softened, not merely
renumbered. The MSY spread (246–500 kt) survives and is still worth reporting.

**This is the second time in this project that a hand-rolled refit has disagreed with the
registered estimator. The rule should be: never re-fit by hand when the estimator is in
the repository — import it.**

### F2 — the Allee bound is stated two ways, and my E13 argument used the wrong one

*(gpt 1.2, grok 1.3)* Both are right, and this one has consequences beyond the text.

Source: `run_ladder.py` line 85 — the **scored** estimator bounds `𝔰 ∈ (0.0, max(S0))`,
i.e. **[0, 81.10] kt** on the recovery window. `profile_allee_identifiability.py` uses
`[0, min_train S] = [0, 9.68] kt`, and its docstring says why. §3.2 of the manuscript
calls the *minimum* "the bound imposed in the code", which is true of the **profile
diagnostic** and false of the **scored fit**.

**Consequence for my own prior work.** In `E1_DEFERRED_ITEMS_RESEARCH_PROGRAMME.md` §6.6 I
overturned the E13 decline on the ground that "the current bound excludes every threshold
that could represent a predator pit". That reasoning used the profile range. The scored
estimator already permits 𝔰 up to 81.1 kt — above most recovery-window states — so the
exclusion I described **does not hold for the fit that produced the verdict**. At 𝔰 = 50
kt, `a(S) < 0` on 12 of 13 states, and that configuration *is* inside the scored feasible
set; what actually suppresses it is the in-objective restriction `0 < 𝔰 < 0.8K` combined
with the penalty on negative surplus, not the range bound.

Ω_pit in `SPECIFICATION_v3.md` remains a reasonable object, but **its stated
justification must be rewritten** — the interesting question is why the scored fit,
which could have placed a high threshold, did not.

### F3 — the coverage diagnostic is not coverage *(gpt 1.1, grok 2.2)*

Accepted in full. Two specific defects, both checkable:

**(a) Wrong distributional transform.** I used `σ = (hi−lo)/(2×1.96)`, which assumes a
symmetric normal interval on the raw scale. Testing the published bounds:

| scale | intervals with >10% asymmetry |
|---|---|
| raw biomass | **67 of 71** (median relative asymmetry +0.238) |
| log biomass | 10 of 71 (median −0.000) |

The assessment's intervals are **lognormal**, not normal. My σ is the wrong transform.

**(b) Wrong object.** The published interval is uncertainty about *true* biomass given the
assessment's data and model. I re-centred its width on a hindcast and called the result
coverage. As gpt puts it, that re-centred interval has no established 95% coverage; and
the inference I drew — "the modules are not being separated by noise in the
reconstruction" — does not follow, because large individual errors say nothing about
whether *differences between* model errors are robust.

**The repair is gpt's:** keep it as a descriptive scale ratio
`D = |Ŝ − S| / [(hi − lo)/2]`, name it an error-to-interval-width diagnostic, and drop
both the word "coverage" and the robustness inference.

### F4/F5/F6 — three defects in the implied-productivity paragraph

- **F4 (my error).** I wrote that productivity "settles near a fifth of its pre-collapse
  value ... at any K". Recomputed: at K=1032.7 the 1995–2007 mean is 0.20 of pre-collapse,
  but **at K=5000 it is 1.12** — slightly *higher*, not a fifth. gpt read my own table
  correctly and I did not. The sign reversal is robust; the magnitude contrast is not.
- **F5.** "Undefined for K below the pre-collapse stock size" is wrong: the expression is
  undefined only at `S=0` and `S=K`. For `S>K` it is defined with a negative denominator;
  what fails is the *interpretation* as a positive productivity.
- **F6.** With `P_t = S_{t+1} − S_t + C_t` and the series ending in 2015, the last usable
  transition starts in **2014**. My "2008–2015" band contains **7** transitions, not 8.
  The period convention (transition-start years) must be stated and the counts given.

---

## 3. The item that changes the paper's framing

### F7 — the headline is broader than the evidence *(gpt 1.4, grok 2.1)*

Both auditors independently make the same point, and it is the most consequential item in
the round. v27 added the regime split, which shows persistence is *not* lowest-error in
the collapse band, and v29 still opens with "no module forecasts spawning-stock biomass
more accurately than last-value persistence."

gpt's replacement is precise and I adopt it: **"No tested structural implementation has
lower pooled rolling-origin RMSE than persistence at the two evaluated horizons."**

gpt's second half matters equally: *"collapse is missed by every model"* must be scoped to
the **fixed pre-collapse-origin** trajectory. A fixed forecast asks whether the decline
could be projected from pre-collapse information; rolling forecasts assimilate the decline
as it unfolds. Those are different questions and the paper currently blurs them.

### F8 — the diagnostic I added contradicts the ranking I used it to support *(grok 2.2)*

The sharpest catch of the round. On my own coverage numbers at h=1, **M3 reads 59% against
persistence's 56%**. I printed that and then wrote that the diagnostic underwrites the
RMSE ordering. grok's dichotomy is correct: if the diagnostic is meaningful it complicates
"persistence is best"; if it is not meaningful for retention it cannot underwrite the
ranking. Under the F3 repair it becomes descriptive only, and the M3 row must be
acknowledged rather than passed over.

---

## 4. Where I do not fully agree

**F17 — Rose (2026) as mechanism proof *(grok 2.5)*.** Three of the four flagged
equivalences should go, and I accept those. But grok's claim that "the LRP is not why the
columns cannot be pooled" is already the paper's position: `SPECIFICATION_v2.md` states
the no-pooling rule in terms of four differing typed fields with R04 forbidding transfer,
and the LRP is listed as one field, not the reason. The text should be checked for a
loose sentence, not rewritten to a position it already holds.

**F18 — the literature gap *(gpt 2.3)*.** Softening "almost always" and "what is missing"
is right. But gpt's proposed replacement drops the contribution claim entirely. The
defensible middle is to state the gap as *specific to the cited diagnostic papers* rather
than as a survey finding — the MASE/HCxval literature scores index-space predictions, and
this paper scores the assessment's SSB state. That is a real distinction, and gpt's own
2.3 concedes it is a *different* validation task; it should be stated as different, not
as stronger.

**F19 — model descriptions *(gpt 2.8)*.** "M1 is not output-only" and "survey
initialisation is §3.2 not §3.4" are correct and I will fix them. "M1b is not nested
within M1" is already the paper's position — v25 records M1b as a separate branch, not a
limiting case, and the non-nesting is why the comparator map exists. That one is already
right.

---

## 5. Disposition

**Tier 1, must fix before any further submission (v30):** F1 corrected ridge with the
registered estimator; F2 bound statement split into scored-fit vs profile; F3 coverage
recast as a descriptive ratio with the log-scale point noted; F7 headline rescoped, with
the fixed-origin/rolling distinction made explicit.

**Tier 2, same revision:** F4, F5, F6, F8, F9, F10, F11, F12, F13, F14, F15, F16, F20,
F21, and the accepted parts of F19.

**Consequential beyond the manuscript:** F2 requires rewriting the justification of Ω_pit
in `SPECIFICATION_v3.md` and correcting §6.6 of the programme document. That is an error
in my own audit reasoning, not in the manuscript, and it must be recorded as such rather
than quietly amended.

**Process rule added:** never re-fit a model by hand when the registered estimator exists
in the repository — import `fit_params` and call it. Both F1 and the E13 misreading trace
to reconstructing an estimator instead of using it.

---

## 6. Second pass — sections my first table did not triage

**My round-4 table above covered 21 items. The two audits contain roughly 100 numbered
sections.** That is the same failure mode recorded in round 2, where gpt's "final sentence
equating *M* and the residual" was never transcribed and survived three versions. The
sweep below closes it: every remaining section is now ruled on, and the ones that change
the manuscript are marked.

### 6.1 Newly accepted — verified against source

| # | Item | Auditor | Verification |
|---|---|---|---|
| **F22** | **M4 takes h+1 updates, not h** | gpt 3.6, grok 3.2 | **Confirmed in code.** `start_idx = i_tr[-1] − delay`, then `lead0 = i_te[0] − start_idx`. With `delay=1`, reaching `t+h` costs **h+1** updates. The paper never says this. It must be described as a perturbed initialisation at calendar time *t*, with the first catch and the residual alignment stated. |
| **F23** | **`r ≈ 2` implausibility claim conflates rate conventions** | gpt 5.8 | **Confirmed by arithmetic.** In a discrete annual map the low-biomass multiplier is `1+r = 2.935`/yr, i.e. a continuous-equivalent `ln(1+r) = 1.08`/yr — not `1.935`. I compared a discrete-map coefficient against continuous-time intrinsic rates. The estimate is still high, but the sentence as written in v28 is not a valid comparison and must be restated with an explicit convention. |
| **F24** | **MSY figures are formal curve maxima, not sustainable yields** | gpt 5.7 | Accepted. The paper already states that SSB minus catch is not a closed budget; calling `rK/4` a "biological implication" restores a management reading that caveat removes. Relabel as *implied maxima of the fitted curves*. |
| **F25** | **"No information about K" is too strong** | gpt 5.6 | Accepted. `∂g/∂K = rS²/K²` is small at low `S/K`, not zero. Replace with "weakly constrain". |
| **F26** | **Clipping in the equation ≠ clipping in the code** | gpt 3.4 | Accepted. The definition uses `[·]₊`; the implementation clips to `[10⁻³, 10⁶]`. Verified in `step()`. State both, and that fitting uses unclipped increments. |
| **F27** | **M3/M4 are also deterministic plug-in paths** | gpt 3.5 | Accepted, wording fix: all forecasts are deterministic; M3/M4 additionally propagate a fitted residual state. |
| **F28** | **Sign-hit convention self-contradiction** | gpt 4.1, grok 1.4 | Accepted and merged with F12. One convention, applied to the training-mean forecast too. |
| **F29** | **Brier explanation needs target states at first mention** | gpt 4.2 | Accepted. Origins below the LRP are not sufficient; targets must be too. Stated once, correctly. |
| **F30** | **Turning points are not required to beat persistence** | gpt 10.4 | Accepted — and this corrects text *I* added in v29 (F-E4). Sustained trends or drift suffice. |
| **F31** | **Age at maturity ≠ generation time** | gpt 10.5 | Accepted, also my v29 text. The five-year/"full generation" gloss goes. |
| **F32** | **Training-mean catch indexing** | gpt 3.7 | Accepted as a disclosure: a 1995–2007 state window has transitions starting 1995–2006, so a 1995–2007 catch mean includes one catch not attached to a training transition. State the convention. |

### 6.2 Accepted as wording, no new analysis

gpt 2.9, 3.1, 3.2, 3.3, 3.8, 3.9, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.10, 6.1–6.6, 7.1,
7.2, 7.3, 8.1, 8.2, 8.3, 8.5, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.6, 10.7, 10.8, 11;
grok 3.1, 3.3, 3.4, 3.5, 3.6, 4, 6, 7. These are precision repairs — scope qualifiers,
unstated conventions, leftover scaffolding, and table/caption mismatches. They are folded
into the v30 pass and itemised in the version record rather than here.

### 6.3 Declined or partial, with reasons

| # | Item | Ruling |
|---|---|---|
| **F33** | gpt 8.4 — primary-treatment uncertainty missing | **Valid but delegated.** The DM/bootstrap layer runs on the archived per-origin file, and the coarse-regime pass's per-origin rows were never archived (SI-1). Producing them is a rerun, not a revision. Named as a prerequisite in the version record. |
| **F34** | grok 3.5 — primary-pass forecasts not archived | Same object as F33. **Delegated, not silenced.** |
| **F35** | gpt 5.9 — recovery profile may show optimiser error, not flatness | **Partial.** F1 already establishes the optimiser converges to a local point from a fixed start. The honest statement is that flatness and optimiser path are not separated by the present diagnostic — which is weaker than the paper's current claim and weaker than gpt's implication that the flatness is spurious. |
| **F36** | gpt 12 / grok 8 — programme advice for further ecological work | **Not manuscript items.** Folded into `E1_DEFERRED_ITEMS_RESEARCH_PROGRAMME.md`. |

### 6.4 What this second pass changes about the round-4 verdict

Three of the newly triaged items — **F22 (M4 step count), F23 (rate convention), F30/F31
(persistence gloss)** — are defects in text *I* wrote, two of them in the ecological
material added in v28–v29. Combined with F1–F4, the pattern is consistent: **the material
added in response to round 3 was written faster than it was checked.** The v30 pass is
therefore a correction pass, not an expansion pass, and no new ecological content should
be added until these are cleared.

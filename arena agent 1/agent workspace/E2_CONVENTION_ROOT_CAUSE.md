# Root-cause analysis: registered v2 runner vs source-year convention

**Question put:** which version should be authoritative?
**Answer: the source-year convention.** And this is not my inference — the
project's own code already says so, in as many words, in a fix that was written
and then never propagated.

---

## 1. The difference is one character

The two runners are byte-identical except for a single index and an output path.

```python
# run_intervention_v2.py   (registered)
pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j + 1]

# run_intervention_srcyear.py
pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j]
```

That is it. 628 lines each; `diff` reports two hunks.

- **source-year**: the transition `j → j+1` removes the catch of the **source**
  year `j`.
- **destination-year**: it removes the catch of the **destination** year `j+1`.

---

## 2. The estimator is hard-wired to the source-year convention

Every fit in the project — Schaefer, Allee, Fox, the ladder — goes through
`run_ladder.fit_params`:

```python
dS    = np.diff(S)     # S[j+1] - S[j]
C_use = C[:-1]         # C[j]        <-- source-year catch
S0    = S[:-1]
pred  = surplus(S0, r, K) - C_use
resid = dS - pred
```

So the objective being minimised is

    S[j+1] = S[j] + g(S[j]) − C[j]

Both runners call it identically: `fit_params(ssb[m_tr], c_ann[m_tr])`.

**Therefore the committed (r, K) = (0.2368694, 5000) are the minimisers of the
source-year loss — and v2 then measures the disturbance under the
destination-year loss.**

That is the defect: parameters from one model, disturbance classes from another.

---

## 3. The smoking gun: the project already fixed this, twice

### Fix 1 — `run_intervention_srcyear.py`

v2 with the one line changed back to `c_ann[j]`. But its docstring is a verbatim
copy of v2's, and so still asserts:

> "Two changes relative to run_intervention.py … **Every other policy converges
> within the old cap, so all other entries are bit-identical to the committed
> results.**"

It is not bit-identical — it changes every residual. The docstring is false.

### Fix 2 — the explicit override in `campaign_srcyear.py`

```python
# ---- SINGLE-CONVENTION OVERRIDE: make the fit object's residual-derived fields
# ---- agree with the source-year residuals just computed (the map's own convention).
fit["train_residual_sd"] = float(res_tr.std(ddof=1))
...
assert abs(fit["train_residual_sd"] - 114.91) < 2.0
assert abs(e_min + 329.0) < 1.0
assert abs(e_q05 + 287.4) < 1.0
assert abs(e_q10 +  80.9) < 0.5
```

**"the map's own convention."** Whoever wrote this identified precisely the
inconsistency in §2 and corrected it — in the campaign layer. The comment
immediately above it is stale (it says "catch at t+1" while the code uses
`c_ann[j]`), which is probably why the fix was never recognised as what it is.

**Neither fix was ever propagated to the deposited artifact or the manuscript.**

---

## 4. The deposited artifact is the hybrid

Fitting both conventions self-consistently, and evaluating the hybrid, on the
same window (1983–2007, 24 transitions):

| variant | r | K | SD | worst | q05 | q10 | lag-1 acf |
|---|---|---|---|---|---|---|---|
| **A** source-year, coherent | 0.2369 | 5000 | **114.91** | −328.97 | −287.36 | −80.87 | **0.554** |
| **H** hybrid (committed v2) | 0.2369 | 5000 | 134.96 | −460.03 | −318.76 | −114.85 | 0.652 |
| **B** destination, coherent | 0.2084 | 5000 | 135.41 | −442.19 | −307.18 | −99.79 | 0.660 |

`intervention_results_v2.json` carries **−460.03 / −318.76 / −114.85** and SD
134.9610 — a match to **H**, confirmed programmatically. The committed numbers
are not a self-consistent estimate under *either* convention. They exist only
as the hybrid.

### Fit quality

| | in-sample MSE | out-of-sample MSE (2008–2015, n=8) |
|---|---|---|
| A source-year | **12,772** | **696.7** |
| B destination | 17,713 | 749.5 |

A is 28% better in sample and 7.6% better out of sample, with lower residual
autocorrelation (0.554 vs 0.660).

*Caveat stated honestly:* I first tried a model-free lag-identification
regression (ΔS on both catch terms). It is **uninformative** — `corr(C_j,
C_{j+1}) = 0.962`, and `g(S_j)` is collinear with both, so no coefficient
converges near −1 (the fitted `g` coefficient came out at −5.2). The fit
comparison is the real evidence; the regression is not.

---

## 5. Verdict

**Authoritative: A, the source-year convention.**

1. **Coherence** — the only convention under which the committed (r, K) are the
   minimisers of the loss that defines the residuals.
2. **Empirical** — better in-sample and out-of-sample fit, lower residual
   autocorrelation.
3. **Standard practice** — in annual assessment models, SSB_y is the spawning
   biomass of year y and C_y is removed during year y.
4. **Authorial intent** — the project's own override calls it "the map's own
   convention."

**And the decisive point, which does not require settling the a-priori timing
question at all:** the hybrid is indefensible on any view. If you want
destination-year, you must *refit* — you get r = 0.2084, g_max = 260.5, classes
−442.19 / −307.18 / −99.79. You may not keep r = 0.2369 and pair it with
destination-year residuals. That is not a convention; it is an error.

---

## 6. Consequences — and where I got it wrong

g_max = rK/4 = 296.087 is unchanged (same r, K).

| | A (authoritative) | H (current paper) |
|---|---|---|
| classes (worst/q05/q10) | −328.97 / −287.36 / −80.87 | −460.03 / −318.76 / −114.85 |
| §2 SD / mean / max / acf | 114.91 / −10.88 / +206.55 / 0.554 | 134.96 / −20.44 / +179.76 / 0.652 |
| **vacuous classes** | **1 of 3** (worst only) | 2 of 3 |
| q05 BAU kernel at T=∞ | **2219.6 kt** | empty |
| q05 zero-catch T=∞ | 2070.9 kt | empty |
| constructive bound g(K*)−\|e_q10\| | 172.46 − 80.87 = **91.6** | 172.46 − 114.85 = 57.61 |

### The no-dominance verdict survives — in its original form

At A-q05, T = ∞ (lower boundaries, kt):

| policy | T=1 | T=5 | T=∞ |
|---|---|---|---|
| BAU (5 kt) | 989.0 | 1298.7 | **2219.6** |
| zero catch | 984.7 | 1280.8 | **2070.9** |
| flat 25 / S1 / cpm | 1037.2 | 1499.6 | **empty** |
| flat 50 | 1090.1 | 1727.7 | **empty** |
| flat 75 | 1143.1 | 1965.9 | **empty** |
| flat 100 | 1196.4 | 2215.3 | **empty** |

Every positive-catch rule is empty at T=∞ while BAU's is nonempty — which is
exactly the mechanism v23–v27 stated, and it is **true** under A.

v27 was internally contradictory: it printed hybrid class labels (−114.9)
alongside the source-year kernel (2219.6). The v28 correction campaign resolved
that contradiction by purging 2219.6 and standardising on H.

### Where my own recent work was wrong

I have to be direct about this, because I did it:

- I purged **`2219.6` from 12 sites** across four patch passes, having
  classified it as a stale Fox-campaign artifact. It is not. It is the correct
  source-year q05 kernel boundary. **That purge was wrong.**
- My §2 "corrections" replaced the correct A-basis values (mean −10.88, SD
  114.91, max +206.55) with hybrid values. **Wrong direction.**
- My Tables 3/4/5 corrections standardised those tables on the hybrid elevation
  campaign. **Wrong basis.**
- The battery I built pins the paper to H. Those checks are now actively
  enforcing the error.

The 123-check battery is green because it faithfully verifies the wrong thing.

---

## 7. Fair statement of the alternative

Under **B** (coherent destination-year, refitted), the paper's qualitative
vacuity conclusion survives: 2 of 3 classes vacuous, q05 empty. So the "two of
three" claim is robust to B vs H and fails only under A.

What distinguishes A is not convenience but evidence: it is the convention the
estimator actually uses, and it fits the data better both in and out of sample.
If a referee asked "why source-year?", the answer is: because that is the
convention under which your published (r, K) were estimated, and because
adopting any other convention requires refitting and changes r by 12%.

---

## 8. Required remediation

1. **Promote** `run_intervention_srcyear.py` to `run_intervention_v3.py`; give
   it an honest docstring stating the convention and why, and delete the false
   "bit-identical" claim.
2. **Fix the stale comment** in `campaign_srcyear.py` line 174 ("catch at t+1"
   → "catch at t"), so the override is legible as the fix it is.
3. **Regenerate** the committed artifact: UC = −328.97 / −287.36 / −80.87.
4. **Re-run the elevation campaigns under A.** The existing
   `campaign_srcyear.py` output is *not* usable as-is: it resamples the
   source-year pool but still freezes the class floors at the registered
   −114.85 (lines 251, 396, 453). Under A the floor must be −80.87.
5. **Rewrite** §2, Table 1's q05 column, the vacuity prose (2→1 classes), the
   constructive bound (91.6), and Tables 3/4/5.
6. **Restore** 2219.6 and 2070.9 with a provenance note.
7. **Invert** the battery: it must pin A, and must *fail* on H values.

Items 3–4 require re-running the campaigns (pandas/numpy/scipy/matplotlib),
which I have not yet done and which will change every table in §3.6–3.11.

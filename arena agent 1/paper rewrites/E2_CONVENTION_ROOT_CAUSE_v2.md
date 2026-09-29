# Registered v2 runner vs source-year convention — definitive analysis

*Supersedes `E2_CONVENTION_ROOT_CAUSE.md`. Adds the blend test, the
out-of-sample test, and the third piece of project code that settles it.*

---

## 0. Figures (task 1) — resolved

`make_figs_v16.py` exists at `fam/e2/src/` and regenerates **all seven**
figures the tex references. I ran it. All seven now exist and every
`\includegraphics` reference resolves under the tex's `\graphicspath{{../}}`:

| tex reference | status |
|---|---|
| `figs_e2/fig1_surplus.png` | ✅ |
| `figs_e2/fig2_kernel_vs_catch_v21.png` | ⚠️ stale `_v21` suffix — **tex fixed** to `fig2_kernel_vs_catch.png` |
| `figs_e2/fig3_reactive_rules.png` | ✅ |
| `figs_e2/fig4_fprime.png` | ✅ |
| `figs_e2/fig5_replay.png` | ✅ |
| `figs_e2/fig6_k_sensitivity.png` | ✅ |
| `figs_e2/fig7_stochastic.png` | ✅ |

Figures placed at `fam/figs_e2/` (that is where `\graphicspath{{../}}` from
`fam/e2/` resolves). Generator output also at `fam/e2/src/figs_e2/`.

**But this created a new inconsistency — see §5.** `make_figs_v16.py` is
written *under the source-year convention*, so the regenerated figures now
disagree with the tex's captions, which are on the hybrid basis.

---

## 1. The difference is one character

```python
run_intervention_v2.py       pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j + 1]
run_intervention_srcyear.py  pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j]
```

628 lines each; `diff` reports two hunks. That is the entire difference.

---

## 2. The estimator is hard-wired to source-year

Every fit in the project goes through `run_ladder.fit_params`:

```python
dS    = np.diff(S)     # S[j+1] - S[j]
C_use = C[:-1]         # C[j]      <-- source-year catch
pred  = surplus(S[:-1], r, K) - C_use
```

Both runners call it identically. So the committed (r, K) = (0.2368694, 5000)
minimise the **source-year** loss — and v2 then measures the disturbance under
the **destination-year** loss. Parameters from one model, disturbance from
another.

---

## 3. Three pieces of project code already say source-year

**(a)** `campaign_srcyear.py`:
```python
# ---- SINGLE-CONVENTION OVERRIDE: make the fit object's residual-derived fields
# ---- agree with the source-year residuals just computed (the map's own convention).
assert abs(fit["train_residual_sd"] - 114.91) < 2.0
```
**"the map's own convention."**

**(b)** `run_intervention_srcyear.py` — v2 with the one line corrected. Its
docstring is a verbatim copy of v2's and still claims *"all other entries are
bit-identical to the committed results"*, which is false. That false docstring
is probably why the fix was never propagated.

**(c)** `make_figs_v16.py` — new to me this round:
```python
"""Source-year publication figures ...
Regenerates figs_e2/fig1..fig7 under the source-year convention:
  floors q10 -80.87, q05 -287.36, worst -328.97; constructive 91.59.
Fixes stale hardcoded destination-year labels ..."""
import run_intervention_srcyear as ri
```

The project found and fixed this three times and never propagated it to the
deposited artifact or the manuscript.

---

## 4. Evidence — including the test that refutes the best steelman

The strongest argument *against* source-year is that `ssb_kt` is **spawning**
stock biomass. Northern cod spawn ~March–May, so SSB_y is a **mid-year**
quantity, while C_y is a calendar-year total. The interval from SSB_y to
SSB_{y+1} spans roughly the back half of C_y and the front half of C_{y+1} —
so arguably **neither** pure convention is right and the truth is a blend.

I tested that directly. Fit

    S_{j+1} = S_j + g(S_j) − [ w·C_j + (1−w)·C_{j+1} ]

with w free. w = 1 is source-year, w = 0 is destination-year, w ≈ 0.5 would be
the mid-year compromise.

| w | r | in-sample MSE | OOS MSE (2008–15) | SD | acf |
|---|---|---|---|---|---|
| 0.00 (destination) | 0.2084 | 17,713 | 749.5 | 135.41 | 0.660 |
| 0.25 | 0.2155 | 16,315 | 733.5 | 129.94 | 0.643 |
| 0.50 (half/half) | 0.2226 | 15,026 | 719.3 | 124.67 | 0.620 |
| 0.75 | 0.2298 | 13,845 | 707.0 | 119.65 | 0.591 |
| **1.00 (source-year)** | **0.2369** | **12,772** | **696.7** | **114.91** | **0.554** |

**The MSE is monotone in w over the entire continuum, and the optimum is the
boundary w = 1.0 — in-sample, out-of-sample, and in residual autocorrelation.**
The blend hypothesis is refuted, not merely disfavoured. There is no interior
optimum, so the "mid-year" objection has no empirical support.

*Honest caveat:* my earlier attempt at model-free lag identification (regressing
ΔS on both catch terms) is **uninformative** — `corr(C_j, C_{j+1}) = 0.962` and
`g(S_j)` is collinear with both, so no coefficient converges near −1. The
continuum fit above is the real evidence.

---

## 5. The decisive argument, which needs no view on timing at all

Either the source-year convention is right, or it is wrong.

- **If it is right** — the committed (r, K) are valid, and only the residual
  block is wrong.
- **If it is wrong** — then the loss that produced (r, K) was misspecified, so
  (r, K) are **biased and must be refit**. Refitting gives r = 0.2084,
  g_max = 260.5, classes −442.19 / −307.18 / −99.79.

**There is no third option in which the current artifact stands.** The hybrid —
source-year parameters paired with destination-year residuals — is not a
convention. It is an error, and it is indefensible on any view.

---

## 6. What the committed artifact actually is

| variant | r | SD | worst | q05 | q10 | lag-1 | #vacuous |
|---|---|---|---|---|---|---|---|
| **A** source-year (coherent) | 0.2369 | 114.91 | −328.97 | −287.36 | −80.87 | 0.554 | **1 of 3** |
| **H** hybrid (committed v2) | 0.2369 | 134.96 | −460.03 | −318.76 | −114.85 | 0.652 | 2 of 3 |
| **B** destination (coherent) | 0.2084 | 135.41 | −442.19 | −307.18 | −99.79 | 0.660 | 2 of 3 |

`intervention_results_v2.json` matches **H** exactly (verified).

---

## 7. How much of this is one observation

| | 1992 residual | share of total SSE | SD excl. 1992 |
|---|---|---|---|
| source-year | −328.97 | 35.3% | 94.89 |
| hybrid | −460.03 | **49.3%** | 99.38 |

The timing mismatch makes the single 1992 collapse **131 kt worse** and raises
its share of residual variance from 35% to 49%. The hybrid's harsher classes are
substantially the artefact of one observation. Note also that even excluding
1992 the hybrid has the larger SD (99.4 vs 94.9), so the gap is not purely
1992-driven.

---

## 8. Verdict, and what it costs the paper

**Source-year is authoritative.** Five independent lines converge: coherence
with the estimator, in-sample fit, out-of-sample fit, residual autocorrelation,
and the project's own three fixes.

Consequences:

| | A (authoritative) | H (current tex) |
|---|---|---|
| classes worst/q05/q10 | −328.97 / −287.36 / −80.87 | −460.03 / −318.76 / −114.85 |
| §2 SD / mean / signed max / acf | 114.91 / −10.88 / +206.55 / 0.554 | 134.96 / −20.44 / +179.76 / 0.652 |
| vacuous classes | **1 of 3** (worst only) | 2 of 3 |
| q05 BAU kernel T=∞ | **2219.6 kt** | empty |
| q05 zero-catch T=∞ | 2070.9 kt | empty |
| constructive bound | 172.46 − 80.87 = **91.59** | 57.61 |

The no-dominance verdict **survives, in its original form**: at A-q05/T=∞,
BAU = 2219.6, zero-catch = 2070.9, and every positive-catch rule is **empty** —
exactly what v23–v27 claimed. v27 was self-contradictory (hybrid labels beside a
source-year kernel); the v28 campaign resolved it by deleting the correct number.

---

## 9. Error ledger (mine)

- Purged `2219.6` from **12 sites** across four patch passes as a "stale Fox
  artefact". It is the correct source-year q05 boundary. **Wrong.**
- §2 "corrections" replaced correct A-basis values with hybrid ones.
  **Wrong direction.**
- Tables 3/4/5 standardised on the hybrid elevation campaign. **Wrong basis.**
- The 123-check battery passes because it faithfully verifies the wrong thing;
  it now actively enforces the error.
- Regenerating the figures under source-year means **figure and caption now
  contradict each other** (fig1's drawn floors are −80.9/−287.4/−329.0 with the
  generator's own comment "only the perpetual-worst floor lies beyond gmax";
  the caption says −460.0/−318.8 and "both … are vacuous"). Introduced this
  round; it must be resolved by migrating the text, not by reverting the
  figures.

## 10. Honest limitation

No document in the repo states whether NCAM's `ssb_kt` is pre- or post-fishery;
`SOURCES.md` describes SSB only as "a noisy observation of a latent stock". The
conclusion therefore rests on **statistical evidence and internal coherence**,
not on a provenance statement. It is strong — five converging lines, monotone in
both samples — but a referee could ask for the DFO convention. Worth stating
explicitly in the paper rather than leaving implicit.

---

## 11. Remediation required

1. Promote `run_intervention_srcyear.py` → `run_intervention_v3.py`; honest
   docstring; delete the false "bit-identical" claim.
2. Fix the stale comment at `campaign_srcyear.py:174` ("catch at t+1" →
   "catch at t").
3. Regenerate the committed artifact: UC = −328.97 / −287.36 / −80.87.
4. **Re-run the elevation campaigns under A.** Existing `campaign_srcyear.py`
   output is not usable as-is: it resamples the source-year pool but still
   freezes floors at the registered −114.85 (lines 251, 396, 453). Under A the
   floor must be −80.87.
5. Rewrite §2, Table 1's q05 column, the vacuity prose (2 → 1 class), the
   constructive bound (91.59), Tables 3/4/5, and all figure captions.
6. Restore 2219.6 / 2070.9 with provenance.
7. Invert the battery: pin A, fail on H.

Steps 1–2 are small. Step 3 is mechanical. **Step 4 regenerates every number in
§3.6–3.11** and is the bulk of the work.

# E2 v24 — a Schaefer/Fox constant leak in Result 3.3

**Status: found, not repaired.** The numbers below are reproducible; the repair
reverses a *results* claim ("the 60-kt rules are protective"), so it is
submitted for authorization rather than applied unilaterally.

**Artifacts (pushed `d800c0a`)**
- `arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v24.tex`
- `arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v24_verification.py`
- E2 v24 = v23 + Funding + Code availability + authorship-responsibility clause.

---

## 1. The claim

E2 v23/§3.3 (Result 3.3, "Constructive boundary") states, in the paper's own
worked line (line 495):

> The value is \(g(K^*) - |e_{q10}| = 172.46 - 80.87 = 91.59\) kt yr⁻¹.

and calls **91.6 kt** "the maximal robust constant catch" — the largest flat
catch whose worst-case low equilibrium still sits at the 2016 LRP (884.6 kt).

91.6 appears **13 times** (abstract line 53, Fig. 2 caption line 405, §3.3
lines 488/491, summary tables lines 802/1080, sensitivity line 821,
stochastic viability line 903, discussion lines 1220/1245, conventions
line 1277).

## 2. The defect

`172.46` is the **Schaefer** surplus at the reference point:
\(g(K^*) = rK^*(1-K^*/K) = 0.2369 \times 884.6 \times (1 - 884.6/5000) = 172.46\),
using the fit the abstract declares (r = 0.2369, K = 5000 kt at its bound).

`80.87` is **not** that fit's 10th-percentile residual. It is the erosion
constant of a *different functional form on a different year convention* —
the Fox form, source-year — frozen in
`wave_e_cod/src/campaign_e2_fox_form_srcyear.py`:

```
FROZEN (e_min = -328.97, e_q05 = -287.36, e_q10 = -80.87 kt, source-year); the Fox fit
```

The Schaefer/source-year fit's own floors, from the committed
`wave_e_cod/results/intervention_results_v2.json`, are

| class | Schaefer (correct here) | Fox (leaked in) |
|---|---|---|
| UC_min | −460.03 | −328.97 |
| UC_q05 | −318.76 | −287.36 |
| UC_q10 | **−114.85** | **−80.87** |

Carried through the paper's own formula:

```
Schaefer:  172.46 − 114.85 =  57.61  kt   ✓ matches the committed optimiser (57.62)
paper:     172.46 −  80.87 =  91.59  kt   ✗ mixes a Fox floor into a Schaefer result
```

The paper is internally aware that 80.87 belongs to the Fox run — the Fox
passage (line 700) uses it consistently with the Fox form's own
\(g(K^*) = 159.92\): `159.92 − 80.87 = 79.05`. It is only the **Schaefer**
Result 3.3 that borrows it.

## 3. Three independent confirmations

1. **The committed optimiser.** `maximal_robust_flat_catch.UC_q10.max_flat_catch_kt`
   = **57.62**, with `positive: true`. 91.6 does not occur anywhere in
   `wave_e_cod/results/intervention_results_v2.json`.
2. **The fixed-point identity.** At \(c = c^*\) the lower fixed point of the
   worst-case closed loop must equal \(K^* = 884.6\):

   | catch c | lower fixed point |
   |---|---|
   | 0 kt | 544.06 |
   | **57.62 kt** | **884.60** ✓ |
   | 60 kt | 900.25 |
   | **91.6 kt** | **1124.46** ✗ |

   At 91.6 kt the worst-case boundary sits **240 kt above the LRP**.
3. **The committed kernel table.** `flat_25` (60 kt) has a \(T=\infty\)
   boundary of **900.25** — already above 884.6, so the LRP is *outside* the
   safe set at only 60 kt. No catch ≥ 60 kt can be robust, which rules out
   91.6 directly. The predicted boundary \(\max(K^*, \text{low fp}(c))\)
   reproduces the committed table exactly for flat_0 (884.60), flat_25
   (900.27), flat_50 (1363.06) and flat_75 (2338.43).

## 4. What the leak propagates into

| site | printed (Fox floors) | Schaefer-correct |
|---|---|---|
| Result 3.3 value | 91.59 → **91.6** | **57.6** |
| Worked line | `172.46 − 80.87 = 91.59` | `172.46 − 114.85 = 57.61` |
| q05 quantity (line 498) | `172.46 − 287.36 = −114.9` | `172.46 − 318.76 = −146.3` |
| perpetual-worst (line 499) | `172.46 − 328.97 = −156.5` | `172.46 − 460.03 = −287.6` |
| φ threshold (line 525) | `1 − 80.87/296.09 = 0.727` | `1 − 114.85/296.09 = 0.612` |
| Fig. 2 caption | "leaves the LRP at … 91.6 kt" | 57.6 kt |
| sensitivity (line 821) | "up to 91.6 kt at K = 5000" | recompute on the K-grid |
| survival probability (903) | "at the constructive bound (91.6 kt) … 0.74" | recompute at 57.6 kt |

Note the last two: they are *downstream measurements taken at the bound*, so
they need re-running against the corrected bound, not just a find-and-replace.

## 5. The narrative inverts the correction

Two passages state the direction of the fix:

- line 908: "The corrective shift of the constructive bound from **57.6** to
  **91.6** kt therefore moves the worst-case reading of the boundary to an
  order of 70–90 kt…"
- line 1277: "the corrected source-year convention **raises** the constructive
  bound (57.6 to 91.6 kt), **makes the 60-kt rules protective**, lengthens the
  certified horizon (to \(T=7\))…"

If 57.6 is correct, both statements reverse: the bound was **lowered**, and
the 60-kt rules are **not** protective (60 kt → boundary 900.25 > 884.6).
This is a results-level reversal, which is why it is not applied here.

## 6. A second, smaller finding

E2's Data availability claims:

> a verification re-execution in a fresh environment reproduced both files
> **byte for byte**.

Re-running `wave_e_cod/src/run_intervention_v2.py` in this sandbox reproduces
the file's **structure and every rounded value**, but **249 of its leaves
differ in the 9th–10th significant figure** (e.g. r: committed
0.2368694030002864 vs local 0.236869402778272; residual sd 134.96095150592583
vs 134.9609515068038). The cause is BLAS/LAPACK non-determinism, not a
modelling error — but "byte for byte" is not achievable without pinning the
linear-algebra backend, and the sentence should be weakened (e.g. "reproduced
every reported value to nine significant figures").

## 7. The battery

`paperE2_cod_intervention_v24_verification.py` — **23 pass / 6 fail, exit 1**.
All six failures are the leak above (R6a, R6b, R6d, R6f, R6g, R6h); the
23 passes confirm the fit, the LRP from primary data (mean SSB 1983–1989 =
884.58), g(K*), MSY, the erosion constants, the boundary table and the
φ threshold, and they independently *disconfirm* 91.6 (R3c, R4f).

This is the complementary method working as intended: a recompute-and-compare
check found a defect that any presence needle would have passed, because the
number is stated consistently in all thirteen places.

---

## Not done this turn

- **P3 v32, P4 v41, P5 v47 still have no numeric battery.** Their existing
  checkers (`papers/paperN_*/verify_retained_rows.py`) parse `manuscript.md`
  and verify concordance ID / citation sets (CC-A0XX-YYY) — they verify **no**
  numeric claim. Building semantic batteries for them requires pulling three
  further pipeline trees.
- The E2 repair above is specified, not applied.

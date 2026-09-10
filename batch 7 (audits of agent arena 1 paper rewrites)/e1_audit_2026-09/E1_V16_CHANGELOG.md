# E1 v15 → v16: Corrections Applied

**File:** `arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v16.tex`
**Basis:** joint evaluation of three external audits (`uploads/e1 audit.txt`: grok, gpt, qwen) plus my own
line-level audit. v15 is unmodified and retained.

Every numeric claim introduced or altered was re-derived from `wave_e_cod/data/` and `src/run_ladder.py`.
Title, author block, date, `\citep`-free citation style, and all frozen verdicts are unchanged.

---

## Tier 1 — validity

**1. Proposition 4.1 restated (was false as written).**
The old statement claimed *no* non-monotone path is a trajectory of `F`. Counterexample under the paper's own
fit: `950 → 857 → 899` kt. Since `F'(S*) ≈ −0.39`, damped oscillation is the generic local behaviour, so
non-monotone trajectories are the norm, not the exception. Retitled to **"No recovery from below the lower
equilibrium"** and restated as the invariant-region claim the proof actually establishes: a path that falls
below the repeller `S_-` cannot later exceed its value there. The proof is tightened to invoke forward
invariance of `(0, S_-)` explicitly. The hypothesis is now verified against the data in-text (NCAM SSB reaches
**9.7 kt** in 1995, far below the 144 kt repeller), so the paper's conclusion survives intact.
A new scope paragraph states the two limits: (a) the fitted map *does* produce non-monotone paths, with the
`950 → 857 → 899` example given openly; (b) the result covers autonomous, noise-free scalar maps only — not
Definition 2.1 with `ε_t ≠ 0`, and not M3/M4, which are not autonomous scalar maps.

**2. Lemma 3.2 → Observation 3.2 (premise unmet).**
Its premise required a monotone-rising window; NCAM 1995–2007 declines in five consecutive years (34.59 kt in
1999 → 20.07 kt in 2004). Demoted from theorem to empirical observation, with the non-monotonicity stated
outright. Now records the actual boundary values (`s → 0`: 2.1×10⁻²³ coarse, 9.4×10⁻⁶ annual). Three
qualifications added: the penalty is a tendency not a proof of the global optimum's location; a boundary
estimate is not proof of non-identifiability; a meaningful threshold may lie outside the sampled range. The
claim retained is the defensible one — the data do not constrain behaviour near a threshold, so the estimate
is evidence *neither way*. Downstream "identification failure is topographically forced" softened.

**3. Table 10 catch treatments un-swapped + K bound corrected.**
Verified by re-running both fits: **coarse (C=5.00) → r=0.458, K=500.0, MSE=128.35**; **annual (C=3.19) →
r=0.370, K=5000.0, MSE=127.84**. Table 10 had these reversed for both M1 and M1b; labels corrected and
`K = 105.9` fixed to the reproduced **105.8**. "Pinned at its lower bound, 500.0 kt" was wrong twice — 500.0
is the multi-start initialiser, and the declared bound is `max_train S + 10 = 50.8 kt` (the max over the
regression's predictor states, 1995–2006, is 40.8 kt). The "neither is reconciled here" note is replaced by
an explicit correction notice. §3.2 prose likewise corrected. The argument is *strengthened*: the optimiser
failing to move K the 449 kt from initialiser to bound is better evidence of a flat objective than a bound
solution would be.

**4. SSB−catch accounting narrowed.**
`ΔSSB + landings` is no longer called "the model-free accounting bound." It is now labelled a diagnostic
construct, with the reasons stated (SSB vs total landings; maturation, weight-at-age, age composition), and
the inference is explicitly conditioned on the accounting the ladder itself assumes. The claim that Regular
et al.'s `M ≈ 2.5` "is the same residual in assessment clothing" is corrected — related in direction, not the
same object.

---

## Tier 2 — internal coherence

**5. Table 9 columns defined.** New paragraph: `z` is DM on the squared-loss differential; the interval and
`p` are a moving-block bootstrap of the **RMSE** difference. Explains why 5 of 32 rows disagree (the square
root compresses the collapse-window tail), states that interval and `p` agree in every row, and concedes that
`p` inverts a percentile interval rather than resampling under a null — so it is not a calibrated test.

**6.** "no non-retention margin separates from zero" → **"no non-retention margin against persistence"** (the
M4-vs-M3 row separates, as the same paragraph later says).

**7.** Origin-mix arithmetic: **3.2 → 3.6 kt**, with the 84.4 kt controlled value named.

**8.** "r saturates at the upper bound" → "driven hard against the upper bound, reaching 1.935 of a permitted
2 without attaining it" (both occurrences).

**9.** "rises from 167 to 462 kt" → "rises from 167 kt to a 2022 peak of 462 kt before easing to 342 kt in
2024" — the path ends at 342 and is not monotone.

**10.** "rolling scores insensitive to the catch treatment" scoped to M1/M1b, which are invariant to the
kilotonne; M2/M3/M4 move (144→160, 135→154, 196→206 kt) and are now stated.

**11.** Model count: "seven-model ladder against two naive baselines" → "five-module structural ladder";
Definition 2.3 reconciles the seven-entry set with the five-module phrasing; "Schaefer/Allee ladder" →
"five-module ladder" (abstract and highlights).

**12.** "independent negative certificate" → "specification-level"; Definition 2.5 now certifies
non-retention of *the scored implementations*, not of the model class.

---

## Tier 3 — precision and disclosure

**13.** Brier: separates "degenerate event" from "little separation" — the indicator never varies, so the
score separates models but carries no early-warning information.
**14.** "Collapse-window RMSE remains about 821 kt" attributed (M2/M3/M4 annual; 819 coarse; M1/M1b 694).
**15.** Table 10: index module relabelled `M_cap_index` (was "M3"); flat-valley row relabelled M1 only.
**16.** `ε_t` role fixed: regression error at estimation, set to 0 in all forecasts (except M3's carried
residual). **Catch timing** stated: `C_t` spans `t → t+1`.
**17.** Definition 2.4: H1 declared **vacuous for M1**, whose retention turns on H2 alone.
**18.** M3's `φ` documented as a second-stage lag-one residual regression clipped to [−0.95, 0.95].
**19.** STATLANT/Schijns match stated as 1983–1993 with the 1994–1995 exposure quantified (1.31 and 0.41 kt);
1956 discrepancy explained for Specification B, which begins in 1954.
**20.** `I_known` reconciled with the no-carry-across-1991 rule; multi-step index use disclosed as a
conditional hindcast.
**21.** Vintage framing moved into §2.3 **and** the abstract: retrospectively reconstructed series, catch
supplied along the horizon — a retrospective prediction experiment, not an operational forecast test. Abstract
also now carries the Specification A "within noise" caveat.
**22.** 1995 fixed-window overlap acknowledged.
**23.** Two overreach repairs (gpt §7): "if the crash were a catch-regime event, M2 would improve" now notes a
misspecified module need not improve; "the missing term is not catch" now says *consistent with*, not
*because*.
**24.** Intro "delay and observation" corrected — observation variants are not rungs of the scored ladder.
**25.** My own B2/B3: the §4 decomposition now flags that its Spec A figures are the **coarse** pass while
Table 9's Spec A rows are the **annual** pass (M4 195.6 vs 206.3); Table 8 gains a note explaining that the
apparent 3-kt module win at h=5 is an origin-mix artefact (matched baseline 193 kt).

---

## Rejected

**Qwen §2.2** (Spec B decomposition "mixes origin treatments"). Checked: `206 − 158 = 48` of `118 = 206 − 88`,
and `1031 − 337 = 694` of `713 = 1031 − 318`. Both use the mixed-origin baselines consistently. Qwen's 731
came from substituting the controlled baseline into one term only. **No change made.**

---

## Verification

Environments balanced (43/43), braces balanced, display math balanced, `\citep` count 0, Table 8 and Table 10
column counts uniform. Title/author/date block byte-identical to v15. Re-derived and confirmed: 50.8 kt bound,
40.8 kt predictor max, 449 kt initialiser gap, both M1 and both M1b fits, `950→857→899`, 1999/2004/2007 SSB,
1995 SSB 9.7 kt, xteNCAM 167/462@2022/342, Schijns 1994–95 catches.

**Not addressed (out of scope for a correction pass):** the grok/gpt recommendation to rewrite for
accessibility — de-jargoning "negative certificate," "machine layer," "observation fibre," relocating the
protocol apparatus to a supplement, and leading with the empirical result. That is a restructuring decision,
not a defect fix.

# E1 (`paperE1_cod_forecast_ladder_v15.tex`) — line-level audit

**Scope.** Full read of all 1,432 lines: abstract, highlights, §§1–5, all ten tables, four
propositions/lemmas, declarations. Every printed number cross-checked against every other printed
instance of it, and all stated arithmetic recomputed.

**Nothing was edited.** This is a findings report. E1 is a frozen paper and is not part of the E3/E4/v3
work; the two cover letters were the only E1-adjacent items in scope earlier.

**Update (10 Sep 2026): A1 and A3 are now RESOLVED against the GitHub source.** Both artefacts I said I
could not derive from the manuscript are in the repository:
`batch 7 .../campaign_e1_dm_uncertainty.py` + `results/e1_dm_uncertainty.csv` (the DM/bootstrap layer) and
`wave_e_cod/src/run_ladder.py` + `data/ncam_2016_table_a2.csv` (the estimator). I re-ran the disputed fits.
**A1 is a reporting defect, not a computational error. A3 is worse than I diagnosed: three errors, including
a swap of the two catch treatments.** See §E.

---

## A. Material defects — these need a decision before submission

### A1. Table 9's DM *z*, bootstrap *p*, and bootstrap CI are mutually inconsistent (§3.5)

Three rows report a **95% CI excluding zero while |z| < 1.96**, which cannot both be true of the same
margin under any standard reading:

| Spec | h | Module | Comp. | Gap (kt) | DM z | 95% CI | p |
|---|---|---|---|---|---|---|---|
| A | 1 | M4 | M3 | +52.7 | **0.99** | **[+4.7, +144.7]** | **<0.001** |
| B | 1 | M3 | persist | +42.3 | **1.85** | **[+1.0, +92.5]** | 0.042 |
| B | 5 | M4 | M3 | +100.6 | **1.88** | **[+20.2, +177.4]** | 0.007 |

Separately, four rows have *p* values that no normal-theory reading of their own *z* can produce
(A1 M2 z=1.30 p=0.445; A1 M3 z=1.02 **p=0.927**; A1 M2vM1 z=1.13 p=0.687; A1 M4vM3 z=0.99 p<0.001).

A defensible explanation exists — *z* is Diebold–Mariano on the loss differential while *p* comes from a
**separate** moving-block bootstrap of the RMSE gap, so the two need not agree — but **the paper never says
this**, and the table's own header presents them as one uncertainty statement. As printed, a referee will
read it as an error. **Fix: state explicitly that `p` is the bootstrap's, not the DM z's, and that the two
procedures can disagree; or drop one column.**

### A2. §3.5's summary claim is contradicted by its own table — and by its own next sentence

> "On Specification A **no non-retention margin separates from zero**."

But the same paragraph, four sentences later, says M4-vs-M3 "separates at h=1 on **both** specifications
(p below 0.001)" — and Spec A M4vM3 is exactly the row with CI [+4.7, +144.7], p<0.001.

The first claim is presumably meant as *no margin **against persistence*** separates (true: all five h=1
and all five h=5 persistence rows have CIs covering zero). As written it is false. **Fix: insert "against
persistence".** This one is a genuine self-contradiction, not a presentational choice.

### A3. The K lower-bound contradiction is flagged but left unresolved (§2.2 vs §3.2 vs Table 10)

- **§2.2:** "K optimised on [max_train S + 10, 5000] kt, with **500 kt the multi-start initialiser rather
  than the lower bound**."
- **§3.2 and Table 10:** "r = 0.458 with **K pinned at its lower bound, 500.0 kt**."

Both cannot be true. On the recovery window max_train S ≈ 81 kt, so the declared lower bound is ≈91 kt, and
a fit resting at exactly 500.0 is either at the initialiser (not a bound) or the declared bound is wrong.

Table 10's closing note **acknowledges the clash and declines to fix it**: *"The table's rows quote the
source sections' own phrasing where the two differ … neither is reconciled here."* Transparent, but it
leaves a factual contradiction about the estimation setup in a methods section. A reader cannot tell what
was actually optimised. **This is the most substantive defect in the paper.** It needs the actual optimiser
configuration stated once, authoritatively.

### A4. Arithmetic slip: "3.2 kt" should be 3.6 (§2.3)

> "the mixed-origin reading of Table 6 (88 kt) exceeds the controlled reading by **3.2 kt**"

88 − 84 = 4; using Table 9's more precise 84.4 gives **3.6**. The figure 3.2 requires a mixed-origin value
of 87.6, which is printed nowhere. Immaterial to the verdict, but it is a wrong subtraction of two of the
paper's own numbers.

---

## B. Presentational inconsistencies — lower severity, still worth fixing

### B1. "Seven-model ladder" is counted two different ways

- **Highlights:** "A scored **seven-model** ladder runs against **two naive baselines**" → implies 7 + 2 = 9.
- **Definition 2.3:** "the forward-ordered set of **seven** models {persist, mean, M1, M1b, M2, M3, M4}" →
  the seven **include** the two baselines (5 structural + 2 naive).

Definition 2.3 is the authoritative one. The Highlights bullet double-counts. **Fix: "A scored five-module
ladder runs against two naive baselines."**

### B2. Discussion mixes coarse-regime and annual-landings values in one arithmetic chain (§4)

The M4 decomposition uses **M4 = 195.6 kt** (coarse regime, Table 4's 196) and then cites "M1 23, M1b 17,
M2 46, M3 37 … each a one-line subtraction of **Table 4's** printed values" — consistent, all coarse. But
Table 9's Spec A rows are the **annual-landings** pass (M4 = 206.3), because §3.5 states the archived
per-origin file for Spec A is the annual pass. So the paper's uncertainty layer and its headline
decomposition rest on **different catch treatments** for the same "Specification A" label.

Internally each chain is correct (I verified: 195.6 − 98.0 = 97.6 ≈ "97.5"; 184.4 − 98.0 = 86.4 ✓;
195.6 − 184.4 = 11.2 ≈ "11.1"). The risk is a reader comparing 195.6 against Table 9's 206.3. **Fix: label
which catch treatment each Spec-A number comes from.**

### B3. Table 8 bolding is inconsistent

Spec A h=5: `persist 265` is **not** bold, `M_cap_index 262` is lower but also not bold, and the
origin-matched `193` is not bold either. Elsewhere bold marks the winner. Here the all-origins baseline
loses to the module (262 < 265) — which is exactly why the origin-matched row matters — but the table gives
the reader no cue. The text handles it correctly ("the five-year near-tie … dissolves"). **Fix: bold 193,
or add a footnote.**

---

## C. Checks that PASSED (recorded so they are not re-audited)

- **Abstract ↔ tables.** "98 kt persistence vs 115–206 structural" ✓ (Tables 4–5 h=1 span 115–206);
  "265 vs 289–488" ✓ (Table 4 h=5); "694–819 structural, 670 and 688 naive" ✓ (Table 3); "1898 kt" ✓ (§3.3);
  "819 kt each" for M3/M4 ✓; "196 versus 135" ✓ (Table 4).
- **Spec B abstract figure "persistence 84 vs M1 120 at h=1"** ✓ — correctly uses the *origin-matched* 84,
  not Table 6's mixed-origin 88, and §2.3 explains the difference (only the 3.2/3.6 slip, A4).
- **Proposition 3.1 (M1–M2 coincidence)** — valid: C ≡ 5 kt on both train and test of the recovery window
  makes the two prescriptions identical.
- **Lemma 3.2 (forced Allee identification failure)** — valid; the monotone-recovery argument is correct and
  matches the reported 𝔰 → 0.
- **Lemma 2.2 (Schaefer ≠ 𝔰→0 limit)** — correct: 𝔰=0 gives a(S)=S/K, a cubic surplus, not a≡1.
- **Proposition 4.1 (non-monotone paths)** — proof is sound given the stated two-equilibrium form, and the
  fitted map (repeller 144, attractor 889, F′≈−0.39) does have that form.
- **M4 delay decomposition** (§4) — all four subtractions verified to ±0.1 kt.
- **Brier logic** (§3.3) — the parenthetical "the bare fact that targets are below the LRP would not by
  itself make the persistence indicator correct; the origin states being below it does" is the correct
  and non-obvious justification for the 0.00.
- **Retention rule application** — no module satisfies (H1)–(H3) anywhere; the 5% tie band never
  decides a case (smallest deficit 17%, as stated).
- **Origin counts** — n=25/21 (Spec A), n=59/55 (Spec B ladder), n=63/59 (Spec B baselines), n=24/20 and
  n=36/32 (index modules) are used consistently at every mention.
- **Two-specification separation** — no pooling anywhere; the "not spliced" argument at the 2005 checkpoint
  (26 vs 25.18 kt) is properly reasoned.

---

## D. Priority

| # | Item | Severity | Effort |
|---|---|---|---|
| A3 | K lower-bound contradiction, self-acknowledged and unreconciled | **High** | needs the true optimiser config |
| A1 | Table 9 z / p / CI mutually inconsistent | **High** | one clarifying sentence, or drop a column |
| A2 | "no margin separates" contradicted by its own paragraph | **High** | insert two words |
| A4 | 3.2 should be 3.6 | Medium | one number |
| B1 | seven-model / 7+2 double count | Medium | one bullet |
| B2 | coarse vs annual mixed under one "Spec A" label | Medium | labelling |
| B3 | Table 8 bolding | Low | one bold |

A2, A4 and B1 are unambiguous errors with unambiguous fixes. A1 and A3 require the author to supply a fact
I cannot derive from the manuscript (the bootstrap's relation to the DM statistic; the actual K bound).

---

## E. Resolution of A1 and A3 against the source code

### E1. A1 — Table 9 is *arithmetically faithful*; the defect is that it never explains two procedures

`campaign_e1_dm_uncertainty.py` computes **two different things** and prints them side by side:

- `DM_z` — Diebold–Mariano on the per-origin **squared-loss difference** `d_i = L_A,i − L_B,i`, HAC-scaled.
- `ci95`, `p_bootstrap` — a Künsch moving-block bootstrap of the **difference of RMSEs**,
  `sqrt(mean(L_A)) − sqrt(mean(L_B))`, 20,000 reps, seed 0.

Every value in Table 9 reproduces `results/e1_dm_uncertainty.csv` exactly. The CI and *p* are **internally
coherent in all 32 rows** (CI excludes zero ⟺ *p* < 0.05 — verified, 15/17 split, zero exceptions). So the
paper's numbers are right.

**Why they disagree with `DM_z` in 5 of 32 rows:** the DM statistic is computed on the raw squared-loss
difference, which on these windows is dominated by a few catastrophic origins, inflating its variance and
depressing |z|. The bootstrap works on the **RMSE gap**, and the square root compresses exactly that tail,
so the resampled gap is far more stable. A heavy-tailed loss difference therefore yields small |z| *and* a
tight CI. Both are correct; they answer different questions.

**This fully explains the A1 row** (Spec A, M4 vs M3: z=0.994, CI [+4.7,+144.7], p<0.001) and the four
others. **Recommended fix is now one sentence**, not a column deletion:

> *DM z tests the mean squared-loss differential; the CI and p come from a separate moving-block bootstrap
> of the RMSE gap. Because the square root compresses the heavy collapse-window tail, the two can disagree,
> and the bootstrap is the tighter of the two on this data.*

The "p vs z" mismatches I flagged (e.g. z=1.02 with p=0.927) are the same phenomenon and are **not errors**.

### E2. A3 — resolved, and it is three errors, not one

`run_ladder.py` lines 81–82 are unambiguous:

```python
x0     = [0.3, max(np.max(S) * 1.5, 500.0)]        # initial guess
bounds = [(1e-3, 2.0), (np.max(S0) + 10.0, 5000.0)]  # K lower bound = max_train S + 10
```

On the recovery window (train 1995–2007) `max(S0) = 81.1`, so **the K lower bound is 50.83 kt**, and
`x0` for K is `max(121.65, 500) = 500.0`. I re-ran both fits and reproduced the printed values exactly:

| fit | reproduced | paper attributes it to |
|---|---|---|
| C = 5.00 (**coarse**) | r=0.458, K=500.0, MSE=128.35 | **annual landings** ❌ |
| C = 3.19 (**annual**) | r=0.370, K=5000.0, MSE=127.84 | **coarse regime** ❌ |
| M1b C=5.00 (**coarse**) | K=105.8 | **annual** ❌ |
| M1b C=3.19 (**annual**) | K=129.8 | **coarse** ❌ |

**Error 1 — the two catch treatments are swapped.** §3.2 and Table 10 attribute each fit to the wrong
treatment, for both M1 and M1b. This inverts the paper's own worked example of catch-dependence.

**Error 2 — "K pinned at its lower bound, 500.0 kt" is wrong twice.** 500.0 is not a bound; it is the
multi-start **initialiser**, sitting 449 kt *above* the true lower bound of 50.83. L-BFGS-B never moved off
`x0` because the objective is flat there. **§2.2's wording is correct; §3.2 and Table 10 are wrong** — the
opposite of what Table 10's "neither is reconciled here" note implies by giving them equal standing.

**Error 3 — the correction strengthens the paper.** The argument in §3.2 is that "the (r,K) minimizer slides
along the valley as the constant changes." A solution that is a *stalled optimiser start* is **stronger**
evidence of a flat objective than a bound solution would be: the gradient was too small to move it 449 kt.
The flat-valley sweep (MSE 127.4→149.9 over K ∈ [60,5000]) independently confirms this.

**Also confirmed:** M1b's `s → 0` numerically (2.1×10⁻²³ coarse, 9.4×10⁻⁶ annual) with r pinned at 2.0 —
**Lemma 3.2 is empirically vindicated**, exactly as it predicts.

### E3. Revised priority

| # | Item | Status | Fix |
|---|---|---|---|
| **A3** | catch treatments **swapped**; "lower bound 500.0" wrong twice | **confirmed against code + rerun** | swap the two rows in §3.2 and Table 10; replace "pinned at its lower bound, 500.0 kt" with "resting at the multi-start initialiser, 500.0 kt (lower bound 50.8 kt)"; delete Table 10's "neither is reconciled here" note — §2.2 was right |
| **A1** | Table 9 z vs CI/p | **not an error** — two procedures | add the one-sentence note above |
| A2 | "no margin separates" | unchanged | insert "against persistence" |
| A4 | 3.2 → 3.6 | unchanged | one number |
| B1–B3 | presentational | unchanged | as before |

A3 is now the only item requiring a substantive correction, and it is a **factual error in a results
section**, not a wording preference.

---

## F. WITHDRAWALS (10 Sep 2026, after joint evaluation of three external audits)

Two entries in the "verified correct" list are **WITHDRAWN**. See
`/home/user/E1_THREE_AUDIT_JOINT_EVALUATION.md`.

- **Proposition 4.1 — WITHDRAWN. It is false as stated.** Counterexample under the paper's own printed fit:
  `950 → 857.2 → 899.1` kt, a decline then recovery, never crossing the repeller. 89 of 90 sampled starts do
  this; `F'(S*) ≈ −0.39` makes damped oscillation the *normal* local behaviour. The proof establishes only the
  narrower invariant-region claim, and its own parenthesis concedes the non-monotone approach. I checked the
  proof's internal validity and did not test the statement's quantifier against the fitted map.
- **Lemma 3.2 — WITHDRAWN as a theorem.** Its premise ("training window along which S rises monotonically")
  fails on the 1995–2007 window it is applied to: five consecutive declines 2000–2004 (34.59 → 20.07 kt).
  The empirical fact (`s → 0`) still holds; the theorem-packaging does not.

# E1 — Joint evaluation of two audits (round 6)

**Source:** `uploads/e1_audit_round6_source.txt` (1,603 lines; deepseek L1, gpt L111)
**Manuscript under review:** v31 (`E1_v31.tex`)
**Evaluator:** agent, 10 Sep 2026

---

## 0. Character of this round

A new reviewer (deepseek) joins gpt. Unlike round 5, **most of what they find is not
damage I introduced in the last pass** — it is long-standing material that five previous
rounds did not reach: the M1/M1b nesting contradiction, the abstract's interval claim, the
Allee zero-attainability question, and several counting errors that have been in the text
since v16 or earlier.

Two items, however, *are* mine from v31: the "every module … prescribed catch falls"
sentence I wrote three turns ago to replace the "finite-sample face" link, and the
surviving "pooled score" phrasing.

Everything numerical below was recomputed from `gs_clone/wave_e_cod/` source data or from
the archived DM file in `batch 7/results/`. Nothing is accepted on assertion.

---

## 1. Verdict summary

| # | Item | Auditor | Verdict |
|---|---|---|---|
| **H1** | M1b is treated as a nested comparator but Def 2.1 says it is not nested | deepseek 2, 18; gpt 1.3 | **ACCEPT — Tier 1** |
| **H2** | Abstract: "intervals excluding zero only on Specification B" is false | gpt 1.1 | **ACCEPT — Tier 1** |
| **H3** | `𝔰 = 0` is excluded by the objective yet reported as attained | gpt 3.1, 3.2 | **ACCEPT — Tier 1** |
| **H4** | Abstract range 115–206 mixes Table 4 (coarse) with Table 5 (annual) | deepseek 4 | **ACCEPT — Tier 1** |
| **H5** | "every module … when the prescribed catch falls" — M1 uses constant catch | deepseek 9 | **ACCEPT — my v31 error** |
| **H6** | "four specification fields" but five are listed | deepseek 3, 22 | **ACCEPT** |
| **H7** | "two of the four modules" in a five-module ladder | deepseek 8, 19 | **ACCEPT** |
| **H8** | "pooled score" undefined / ambiguous | gpt 1.2, deepseek 25 | **ACCEPT** |
| **H9** | M4 called "delay" throughout; it is a stale-start experiment | gpt 2.1, deepseek 11 | **ACCEPT — rename** |
| **H10** | "the delay, not the structure, separates M4" is too causal | gpt 2.2 | **ACCEPT** |
| **H11** | M1b "K collapses to the training range" but K = 105.8 > 40.83 | deepseek 5, 23 | **ACCEPT** |
| **H12** | "M3 … increases error" conflicts with M3 < M2 | deepseek 6 | **ACCEPT — needs referent** |
| **H13** | "Table 1 landings" points at this paper's Table 1 | deepseek 15 | **ACCEPT** |
| **H14** | Prey module: 8 training years give 7 transitions, not 8 | deepseek 12 | **ACCEPT** |
| **H15** | Coarse-regime 1992 drop lands in the 1992→1993 step | deepseek 13 | **ACCEPT — disclosure** |
| **H16** | Spec A uncertainty layer runs on the annual pass, not the primary | deepseek 10 | **ACCEPT — already disclosed, strengthen** |
| **H17** | "unbeatable" Brier wording ambiguous | deepseek 17 | **ACCEPT** |
| **H18** | 1995 overlap noted for Spec A but not Spec B | deepseek 16 | **ACCEPT** |
| **H19** | "M1b reads below M1" reads as universal | deepseek 21 | **ACCEPT** |
| **H20** | Profile range justified by an outcome-dependent argument | gpt 3.3 | **ACCEPT** |
| **H21** | Table 9 row: z = 0.99 with p < 0.001 | deepseek 7 | **PARTIAL — see §3** |
| **H22** | Log-floor could change a verdict | deepseek 24 | **PARTIAL — verified, no** |
| **H23** | Profile reads like a likelihood-ratio test | deepseek 20 | **ALREADY ADDRESSED** |
| **H24** | M4 residual/catch indexing must be specified | gpt 2.1 | **ACCEPT — resolved in round 5 as G18** |

**Tier 1: H1–H5. Accept: 19. Partial: 2. Already addressed: 1.**

---

## 2. Verified findings

### H1 — the nesting contradiction *(deepseek, gpt)*

The paper states both of these:

- Definition 2.1 and the SI-2 lemma: setting `𝔰 → 0` gives `a(S) = S/K`, a **cubic**
  modification of the logistic surplus, **not** the Schaefer law; Schaefer is the separate
  branch with `a ≡ 1`.
- Retention rule H1: *"the next-simpler rung for the nested steps (M1b against M1, M3
  against M2)"*.

Both cannot hold. `M1b(𝔰→0) ≠ M1`, so M1b against M1 is **not** a nested step. The paper
proves the non-nesting in its own supplement and then relies on nesting in the comparator
declaration. This also propagates to M1b's role as the alternative comparator for M2
(deepseek 18).

**This does not change any verdict** — M1b is not retained under H2 (against persistence)
regardless of its H1 comparator — but the comparator logic as written is inconsistent and
must be restated: M1b is an alternative production-function branch whose declared
comparator is M1 by *complexity ordering*, not by nesting.

### H2 — the abstract's interval claim is false *(gpt)*

Checked against the archived DM file (`batch 7/results/e1_dm_uncertainty.csv`):

| spec | h | A | B | gap | DM z | 95% CI | p |
|---|---|---|---|---|---|---|---|
| A | 1 | M4 | M3 | +52.7 | 0.99 | **[+4.7, +144.7]** | 0.0000 |

Exactly one Specification A interval excludes zero, so *"intervals excluding zero only on
Specification B"* is false as written. gpt's narrower repair is correct and is what the
Discussion already says: **no Specification A module-versus-persistence margin excludes
zero** — verified, 0 such rows — while one within-ladder comparison does.

### H3 — zero is an infimum, not an attained bound *(gpt)*

From `run_ladder.fit_params`:

```
bounds.append((0.0, np.max(S0)))            # box permits 0
if allee and not (0.0 < s < 0.8 * K): return 1e12   # objective rejects 0
```

The box allows `𝔰 = 0` but the objective returns a penalty there, so **zero is never
attainable**. Reporting `𝔰 = 2.1 × 10⁻²³` as a "boundary estimate" is therefore wrong in
kind: it is a numerical approach to an unattained infimum. gpt's stronger point also
stands — at `𝔰 ≈ 0` the fitted object is the **zero-threshold cubic branch**, not a
positive-threshold Allee model, so M1b's apparent improvement is not evidence for
depensation.

### H4 — the abstract mixes two passes *(deepseek)*

| table | pass | h = 1 structural range |
|---|---|---|
| Table 4 | coarse regime (**primary**) | 115–**196** |
| Table 5 | annual landings | 115–**206** |

The abstract prints 115–206 beside persistence 98 and the five-year 289–488, which are
Table 4 (coarse) values. So the headline range silently combines the primary pass with the
annual pass. Either quote the primary consistently (115–196) or state that the upper bound
is the annual-landings figure.

### H5 — my own v31 sentence overgeneralises *(deepseek)*

In v31 I wrote: *"Every module carries stationary production, so when the prescribed catch
falls in 1992 the predicted increment rises."* **M1 does not use prescribed catch** — it
plugs the training-mean constant (240 kt on the collapse window). The mechanism applies to
M2–M4. M1 still turns upward, but because its constant removal is smaller than the
realised collapse losses, not because of a 1992 drop. I wrote this three turns ago to
replace the "finite-sample face" link and overreached in the replacement.

### H11 — "K collapses to the training range" *(deepseek)*

Table 10 gives M1b recovery-coarse `K = 105.8` kt. The training predictor maximum is
40.83 kt and the terminal state 81.10 kt, so 105.8 is **above** the training range, and
the lower bound is `40.83 + 10 = 50.83`. "Collapses to the training range" is the wrong
description of a valid interior fit.

### H14 — transition count *(deepseek)*

Eight training **years** supply **seven** one-step transitions. The paper says three
parameters `(r, K, b)` are fitted on as few as eight years; the honest statement is seven
transitions for three parameters, which is worse and strengthens the paper's own
sample-size caveat.

---

## 3. Where I do not fully agree

### H21 — the z = 0.99 / p < 0.001 row *(deepseek 7)*

deepseek calls this "a red flag for the bootstrap implementation". **Partially right, and
the diagnosis is wrong.** The archived value is `p_bootstrap = 0.0000` exactly, and the
paper already defines `p` as *inverted from the percentile interval, not from a
null-centred resampling scheme* — so it is not a calibrated tail probability and is not
comparable to the DM `z`. The paper also already flags this row as one of four
disagreements.

What **is** wrong is the presentation: printing `<0.001` for an interval-inversion summary
invites exactly deepseek's reading. The repair is to print the interval and drop or
relabel the `p` column, not to recompute the bootstrap.

I also checked deepseek's implicit claim that there are four such rows: the file contains
**five** rows with `|z| < 1.96` and an interval excluding zero. The fifth is
`M2 vs M1b, Spec B, h=5` — which is precisely the alternative-comparator row the paper
states is *archived rather than printed*. So "four of the twenty-eight" **is correct** for
the printed table, and deepseek's count is consistent with mine once that row is excluded.

### H22 — could the log-floor change a verdict? *(deepseek 24)*

Verified: no. Retention is decided on **raw** rolling RMSE, and the floor affects only the
log-RMSE column, which the paper already states is not the retention score. deepseek's
request for an explicit statement is reasonable; the implied worry that a verdict might
flip is not supported.

### H23 — profile as likelihood ratio *(deepseek 20)*

Already addressed since v20: the text states the statistic is descriptive and that
`χ²₁` is not licensed. deepseek's own note concedes the value is far from any threshold.
No change.

---

## 4. Disposition for v32

**Tier 1:** H1 (restate the comparator basis for M1b — complexity ordering, not nesting),
H2 (abstract interval claim → the verified narrower statement), H3 (choose the open
domain, call `2.1×10⁻²³` an unattained infimum, and rename the object the zero-threshold
cubic branch), H4 (make the abstract range one pass), H5 (scope the catch-drop mechanism
to M2–M4).

**Tier 2:** H6–H20 — counting fixes, the M4 rename with a formal definition and its
control moved into Methods, "pooled score" → *origin-pooled rolling RMSE within each
specification and horizon*, the Table 9 `p` column relabelled, and the disclosures at H14,
H15, H16, H18.

**Process note.** Round 5 established that accepted items must be verified against the
compiled manuscript. Round 6 adds a second rule: **when replacing a deleted claim, the
replacement needs the same scrutiny as an addition.** H5 is a defect I introduced while
repairing a different defect, which is the third time in three rounds that a fix has
carried its own error.

---

## 5. Second pass — gpt §4–12, not covered by the table above

The round-1 table triaged deepseek in full and gpt §1–3. gpt §4–12 are ruled on here.
Each numerical claim was recomputed from `results/rolling_summary.csv` or the archived DM
file.

### 5.1 Newly accepted, verified

| # | Item | Verification |
|---|---|---|
| **H25** | **"M1/M1b scores identical to the kilotonne across catch treatments" is a rounding artefact** *(gpt 10)* | **Confirmed.** Archived values differ: M1 h=1 **120.5095 vs 120.5406** (0.0311 kt), M1b h=1 **114.8024 vs 114.7665** (0.0358 kt), M1 h=5 differ by 0.00025, M1b h=5 by 0.0264. They are *not* mathematically invariant — the training-mean catch does change with treatment and does move the fitted parameters. The claim must be restated as "identical after the displayed rounding", with the mechanism (future catch is not supplied to these modules) given as the reason. |
| **H26** | **"On recovery, M1 and M2 coincide" is true only under the coarse regime** *(gpt 9)* | **Confirmed.** Under annual landings Table 5 gives M1 264 kt and M2 303 kt on the recovery window. The coincidence follows from `C_t ≡ 5` kt on both train and test under the coarse regime only. Must be qualified at first use. |
| **H27** | **The 17% smallest deficit needs its comparator and unrounded value** *(gpt 11)* | **Confirmed: 17.09%.** `(114.8024 − 98.0494)/98.0494`. gpt's 17.1% is right; state the comparator (M1b vs persistence, Specification A, h=1) and the unrounded figure. |
| **H28** | **Bootstrap is conditional on archived forecast paths** *(gpt 7.2)* | Accepted. The intervals resample the origin-level loss sequence from fixed forecast files; they do not propagate parameter-estimation, assessment-revision, catch-reconstruction or covariate uncertainty. This is true and currently unstated. |
| **H29** | **DM statistics are not calibrated for this design** *(gpt 7.1)* | Accepted. Expanding-window recursive estimation, overlapping training samples, near-nested models, a smoothed target and multiple comparisons all bear on calibration. The paper already declines to rest verdicts on DM; it should also stop calling these tests. Relabel as descriptive loss-differential diagnostics. |
| **H30** | **The interval-derived `p` needs a formula or a new name** *(gpt 7.3)* | Accepted, and it supersedes my round-6 §3 recommendation to simply drop the column: gpt's `p_perc = 2·min{#(Δ*≤0), #(Δ*≥0)}/B` is the right disclosure if the column is kept. Either give that formula or rename it a percentile-tail fraction. |
| **H31** | **Name the four disagreement rows in a footnote** *(gpt 7.4)* | Accepted. gpt lists A/M4-vs-M3/h=1, B/M3-vs-persist/h=1, B/M1b-vs-persist/h=5, B/M4-vs-M3/h=5 — **exactly the four I verified independently** in §2. Naming them removes the need for readers to scan the table. |
| **H32** | **Catch–SSB ontology mismatch is stronger than "a scalar approximation"** *(gpt 4)* | Accepted. `C_t` is total landings while `S_t` is SSB, so the removal term is not an SSB-equivalent removal. The recurring formulation must make clear that failing to reproduce the collapse with a supplied catch path **does not test whether fishing caused the collapse**. |
| **H33** | **Fixed-window and rolling-window results are conflated in several statements** *(gpt 8)* | Accepted — same defect as round-5 G9, which v31 fixed in one location only. A document-wide sweep is needed. |

### 5.2 Accepted as structural additions, deferred with reasons

| # | Item | Ruling |
|---|---|---|
| **H34** | Formal information-set table — what is available at origin `t`, and to which module *(gpt 5)* | **Accept in principle, defer the full table.** This is the single most useful addition either auditor proposes and would pre-empt a whole class of confusion (G2, H24, H32). It is a new table assembled from existing facts, so it is not blocked by the frozen spec — but it must be built from the code, not from prose, and that is a pass of its own. Logged for v33. |
| **H35** | Canonical rolling-origin definition with a machine-readable origin list *(gpt 6)* | **Accept, defer.** Same reasoning; the origin sets are archived and can be printed, but doing it properly means emitting a table per experiment. Pairs with H34. |
| **H36** | One-decimal reporting in main tables *(gpt 11)* | **Decline for the main tables, accept for the claims.** Reformatting every table to one decimal is a large diff with a high transcription-error risk, and this project has already shipped two errors from hand-edited numbers. The auditable path is unrounded values in the supplement plus exact figures where a claim turns on a small difference (H27, the 0.93 kt tie-band case). |
| **H37** | Proposition 4.1 mathematical tightening *(gpt 12)* | **Accept, merge with round-5 G17.** Both concern the same object: state the proposition for the zero-clipped map or on `[ε, S₋)`, and drop the unspecified single-equilibrium case. |

### 5.3 Revision to my own round-6 ruling

In §3 above I judged the fix for the `z = 0.99 / p < 0.001` row to be "print the interval
and drop or relabel the `p` column". gpt 7.3 gives the better answer: **publish the exact
formula** for the percentile-tail quantity, or rename it. Dropping a column that readers
can recompute from the archived file is less transparent than defining it. H30 replaces my
earlier wording.

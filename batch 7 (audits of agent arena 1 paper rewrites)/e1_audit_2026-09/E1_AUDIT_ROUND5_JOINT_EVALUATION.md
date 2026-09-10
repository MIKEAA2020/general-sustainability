# E1 — Joint evaluation of two audits (round 5)

**Source:** `uploads/e1_audit_round5_source.txt` (1,306 lines; gpt L1, grok L1037)
**Manuscript under review:** v30 (`E1_v30.tex`)
**Evaluator:** agent, 10 Sep 2026

---

## 0. Headline

**My v30 correction of the Allee bound was itself wrong, and both auditors caught it
independently.** That is the most important finding of this round: a Tier-1 repair
introduced a new Tier-1 defect. Two further defects — the acoustic-index origin counts and
the Specification B Brier denominator — are long-standing and were missed by four previous
rounds and by me.

Every numerical claim below was recomputed from `gs_clone/wave_e_cod/` source data or by
replicating the estimator's own bound construction. Nothing is accepted on assertion.

---

## 1. Verdict summary

| # | Item | Auditor | Verdict |
|---|---|---|---|
| **G1** | Allee bound is 40.83 kt (predictor states), not 81.10 kt; 𝔰=50 is **outside** the scored range | gpt 1.2, grok 1.5 | **ACCEPT — Tier 1, my v30 error** |
| **G2** | Acoustic-index Spec B origins include 3 pre-1991 origins, contradicting the stated rule | gpt 1.1 | **ACCEPT — Tier 1** |
| **G3** | Spec B persistence Brier 0.06 is arithmetically impossible on 59 origins | gpt 1.3 | **ACCEPT — Tier 1** |
| **G4** | Introduction still asserts the bar §4 dismantles | grok 1.1 | **ACCEPT — Tier 1** |
| **G5** | "the 88 of Table 7" — no 88 remains in Table 7 after my v30 edit | grok 1.2 | **ACCEPT — my v30 error** |
| **G6** | Table 8 still bolds the mixed-origin baseline | grok 1.3 | **ACCEPT** |
| **G7** | "conventionally 0.00 for persistence" and the 0.00–0.50 range survive after Table 3 became NA | grok 1.4 | **ACCEPT — my v30 edit left orphans** |
| **G8** | Conclusions ignore the regime split the abstract now admits | grok 1.6 | **ACCEPT** |
| **G9** | Two collapse experiments answer different questions and are never distinguished | grok 1.6 | **ACCEPT — the sharpest item** |
| **G10** | Abstract protocol claim | gpt 1.4 | **ACCEPT** (already conceded round 4 as F21) |
| **G11** | Event-type attribution persists | grok 2.1 | **ACCEPT** (round-4 F15 not yet applied) |
| **G12** | Delay/timeliness paragraph | grok 2.2 | **ACCEPT** (round-4 F16 not yet applied) |
| **G13** | Rose (2026) equivalences | grok 2.3 | **PARTIAL** (as round-4 F17) |
| **G14** | Opening announces then retracts | grok 2.4 | **ACCEPT** |
| **G15** | "r, K, 𝔰 and C compensate" — C is plugged for M1b | grok 1.5 | **ACCEPT** |
| **G16** | Index training eligibility unspecified | gpt 1.1 | **ACCEPT — needs disclosure** |

---

## 2. Verified findings

### G1 — the bound I "fixed" in v30 is wrong *(gpt 1.2, grok 1.5)*

`run_ladder.fit_params` builds its bounds from `S0 = S[:-1]`, the **predictor states**. On
the recovery window:

| quantity | value |
|---|---|
| states 1995–2007 | 9.7, 16.1, 20.6, 28.2, 34.6, 34.4, 29.5, 23.9, 22.1, 20.1, 25.2, 40.8, **81.1** |
| predictor states `S0` (1995–2006) | max = **40.83 kt** |
| `𝔰` bound `(0, np.max(S0)]` | **(0, 40.83] kt** |
| `K` lower bound `np.max(S0)+10` | 50.83 kt |
| predictor transitions | **12**, not 13 |

v30 says the scored bound is `[0, 81.10]` kt. That is the maximum over **all** states
including the terminal 2007 response, which the code excludes. Three consequences:

1. The bound is **40.83 kt**, not 81.10.
2. My statement that 𝔰 = 50 kt is inside the scored feasible set is **false** — it is
   outside. grok states this exactly.
3. My "12 of the 13 recovery-window states" should be 12 predictor transitions, all of
   which lie below 50.

**This matters beyond wording.** In v30 I wrote that "a high threshold was therefore not
excluded from the scored estimation by its range bound." On the correct bound it **was**
excluded — which is closer to my *original* round-3 position, the one I withdrew last
round on the strength of the same misreading. The record now needs a third correction:
the round-4 F2 withdrawal was itself based on the wrong maximum.

The honest statement is narrow and I should not have gone beyond it: the scored bound is
`max` over predictor states (40.83 kt) and the profile range is `min` over them (9.68 kt);
both exclude a predator-pit threshold; the two must be given separate symbols.

### G2 — acoustic-index origin counts *(gpt 1.1)*

gpt reasoned from the stated rule that Specification B's `n=36 / n=32` exceed the maxima
of 33 and 29 by exactly three. Verified against `results/capelin_index_forecasts.csv`:

| tag | h | n | origin range | pre-1991 origins |
|---|---|---|---|---|
| ncam2016 | 1 | 24 | 1991–2014 | 0 |
| ncam2016 | 5 | 20 | 1991–2010 | 0 |
| xteNCAM | 1 | **36** | **1988**–2023 | **3** |
| xteNCAM | 5 | **32** | **1988**–2019 | **3** |

**Exactly the three he predicted.** The mechanism is in `run_capelin_index.py`: the
carry-forward resets memory at 1991 only when the last observation is pre-break *and* the
year is ≥ 1991. Origins 1988–1990 are before the break, so a pre-break observation is
legitimately available and `I_known` is finite. The code is self-consistent; the
manuscript's description of the eligibility rule is wrong, because it states the
post-1991 restriction as if it governed all origins.

### G3 — the Brier denominator *(gpt 1.3)*

Pure arithmetic, and decisive. For a deterministic binary forecast the score is `k/n`:

| k | k/59 | k/63 |
|---|---|---|
| 3 | 0.0508 → 0.05 | 0.0476 → 0.05 |
| 4 | 0.0678 → **0.07** | 0.0635 → **0.06** |

No `k/59` rounds to 0.06. The archived value is `0.063492` on **n = 63** — the unmatched
baseline. So the origin-matching correction applied to the primary RMSE baselines was
never applied to the secondary scores. gpt's required action is right: report counts and
denominators for every secondary comparison, not just the primary.

### G9 — two collapse experiments, never distinguished *(grok)*

The most valuable interpretive item in the round, and it is not a defect I can fix by
editing a number. The paper now contains:

| experiment | question | result |
|---|---|---|
| fixed origin, train 1983–1990, test 1991–1995 | can a pre-collapse fit anticipate the crash? | no — all models miss |
| rolling h=1 origins **within** 1991–1995 | from a state already collapsing, is next year closer to the model or to persistence? | some models win, n=5 |

These are compatible, and the abstract juxtaposes them as though they were one finding.
grok's line is exact: *"a one-step forecast issued in 1993 from an already-collapsed S_t is
not evidence that the model predicted the collapse."* v31 must separate them explicitly.

### G5 / G7 — orphans created by my own v30 edits

Both are consequences of fixing tables without sweeping the prose that referenced them:
after I replaced Table 7's Specification B baseline with the matched 84/300, the sentence
"the 88 of Table 7 is the all-origins value" refers to a number no longer there; after
Table 3's Direction column became NA, "conventionally 0.00 for persistence" and the
"0.00–0.50 on collapse" range became stale. **A table edit is not complete until every
prose reference to the changed cells is re-read.**

---

## 3. Where I do not fully agree

**G13 — Rose (2026).** As in round 4: three of the four equivalences should go, but
"the LRP is not why the columns cannot be pooled" is already the paper's position —
`SPECIFICATION_v2.md` grounds no-pooling in four differing typed fields under R04, with
the LRP one field among them. Fix the loose sentence; do not restate a position already
held.

**grok 1.1's stronger form.** grok says the collapse forecasts fail *because* stationary
production plus a catch drop raises biomass, not because of the repeller — and that
Proposition 4.1 should leave the introduction. I accept removing it from the introduction
(G4). I do not accept deleting the "finite-sample face" link outright without checking:
that phrasing already carries the constant-catch scope, and the correct repair is to state
the mechanism grok gives *alongside* it rather than to drop the proposition's relevance
entirely. Flagged for v31 as a rewrite, not a deletion.

---

## 4. Disposition for v31

**Tier 1:** G1 (bounds table with separate symbols for predictor-state and all-state
maxima; withdraw the 81.10 claim and the "not excluded" sentence), G2 (correct the
eligibility description and disclose the 1988–1990 origins), G3 (recompute secondary
scores on matched origins, report k and n), G4 (remove the equilibrium paragraph from the
introduction), G9 (separate the two collapse experiments in abstract, results and
conclusions).

**Tier 2:** G5, G6, G7, G8, G10–G12, G14, G15, G16, and the accepted part of G13 — plus
the round-4 items F15 and F16, which I listed as accepted but did not implement in v30.

**Process note.** Three of this round's items (G1, G5, G7) are defects *introduced or left
behind by my own v30 correction pass*. Round 4 established that v27–v29 were written
faster than they were checked; round 5 establishes that the correction pass had the same
problem. For v31 the rule is: after every edit that touches a number or a table cell,
grep the whole document for that value and for the surrounding claim before compiling.

---

## 5. Second pass — remaining sections, and unapplied round-4 items

As in round 4, the first table triaged the priority items only. What follows rules on the
remainder and records an audit of my own follow-through.

### 5.1 Round-4 items marked ACCEPT that were never applied to v30

Checked directly against `E1_v30.tex`:

| round-4 item | status in v30 |
|---|---|
| F15 event-type attribution ("a productivity, unallocated-mortality, or observation event") | **still present** |
| F16 "the value of a timely assessment exceeds…" | **still present** |
| F20 "measures how severely that bar penalizes…" | **still present** |
| F21 "retention rule, coded before…" → "scoring core" | **still present** |

**Four items I recorded as accepted last round were never implemented.** Both auditors
re-raise them (grok 2.1, 2.2; gpt 1.4), which is how the gap surfaced. Accepting an item
in an evaluation document is not implementing it; the v31 pass must verify each acceptance
against the manuscript rather than against the previous evaluation.

### 5.2 Newly triaged, verified against code

| # | Item | Auditor | Verification |
|---|---|---|---|
| **G17** | **Proposition 4.1 conflates zero-clipping with the positive floor** | gpt 10.1 | **Confirmed.** With `EPS = 1e-3`, `F(0) = F(EPS) = 0.001`: the floor is itself a fixed point, so "strict decline throughout `[0, S_-)`" fails on `[0, EPS]`. The proposition must be stated either for the zero-clipped map or on `[EPS, S_-)`. |
| **G18** | **M4's first residual is ambiguous in the text** | gpt 10.5 | **Resolved from code.** `forecast_path` applies `resid = phi * resid` *before* the first step, so the first update uses **φ·e_last**, where `e_last` is the residual of the transition `S_{t-1} → S_t`. Because M4 restarts at `S_{t-1}`, its first update re-forecasts the very transition its residual was fitted on. This must be stated. |
| **G19** | Aggregate sign scores do not establish timing | gpt 10.7 | Accepted, wording. |
| **G20** | Stale state does not make a map nonautonomous | gpt 10.3, grok | Accepted — M4's time dependence comes from the residual state and catch path, not the age of `S₀`. |
| **G21** | "single-equilibrium special case" unspecified | gpt 10.2 | Accepted: remove, or formulate separately. |
| **G22** | Unbounded `b` permits the opposite ecological response | gpt 8.7, grok 3.6 | Accepted as a disclosure — `b` is fitted without bounds, so the sign of the prey response is not constrained. |
| **G23** | "Monotonically related" too strong across varying comparisons | gpt 9.1 | Accepted. |
| **G24** | Interval-derived `p` lacks an operational definition | gpt 9.2 | Accepted (already partly disclosed). |
| **G25** | Zero-gap intervals are not the 5% retention margins | gpt 9.3 | Accepted — the intervals test a zero difference, not the tie band the rule uses. |

### 5.3 Accepted as wording, folded into v31

gpt 8.5, 8.6, 8.8, 8.9, 9.4, 10.8, 10.9, 10.10, 11; grok 3.1–3.6, 4, 5, 6, 7. Precision
repairs: unstated conventions, leftover scaffolding, caption/prose mismatches.

### 5.4 Delegated, not silenced

- **Primary-pass per-origin forecasts** (gpt 3.4 equivalent, grok 3.4): still a rerun, not
  a revision. Prerequisite recorded in the programme document.
- **Two-regime capelin specification** (grok 3.1): needs the pass rerun to document fully.
- **Orphan SI-2 pointer** (grok 3.3): checked — SI-2 exists in `E1_SUPPLEMENTARY.md`; the
  manuscript pointer is correct. **No action.**

### 5.5 What this round changes about the process

Round 4 found v27–v29 were written faster than checked. Round 5 finds the correction pass
had the same flaw **and** that four accepted items were never applied. The v31 gate is
therefore extended: every item marked accepted in rounds 4 and 5 must be verified by a
grep against the compiled manuscript, not against the evaluation document.

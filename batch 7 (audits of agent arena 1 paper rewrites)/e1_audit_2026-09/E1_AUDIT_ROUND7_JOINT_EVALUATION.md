# E1 — Evaluation of the editorial audit (round 7)

**Source:** `uploads/e1_audit_round7_editorial.txt` (90 lines, single reviewer)
**Manuscript under review:** v35 (`E1_v35.tex`)
**Evaluator:** agent, 10 Sep 2026

---

## 0. Character of this round

A short, purely editorial audit, and an unusually accurate one: **every checkable claim
verified against source.** No item was rejected.

Most of what it finds is **fallout from my own v35 change.** Moving the uncertainty layer
onto the primary coarse-regime pass updated Table 9, but the prose that quotes Table 9 —
the Section 3.5 "Readings" paragraph and a Section 4 sentence — still carried the old
annual-pass numbers. That is the same failure mode recorded at round 5: *a table edit is
not complete until every prose reference to the changed cells is re-read.* I applied that
rule to the caption and body in v35 but not to the downstream numeric prose.

---

## 1. Verdicts

| # | Item | Verification | Verdict |
|---|---|---|---|
| **1.1** | Stale Table 9 numbers in §3.5 Readings | **Confirmed exactly.** Recomputed from the regime run: h=1 gaps **16.8–97.5** kt (paper said 16.7–108.2), z to **1.53** (said 1.51); h=5 gaps **23.9–223.5** (said 221.7), p **0.078–0.421** (said 0.27–0.76); Spec A h=5 M4-vs-M3 p = **0.707** (said 0.90) | ACCEPT |
| **1.2** | §4 still says Table 9 Spec A rows are the annual pass | Confirmed; contradicts the v35 caption | ACCEPT |
| **1.3** | M4 terminology drift ("delay" vs "lagged initialisation") | Confirmed in retention rule, §1 ladder ordering, §4, §5 | ACCEPT |
| **1.4** | M1b "boundary" language vs the unattained-infimum finding | Confirmed in §3.1 and Table 10 | ACCEPT |
| **1.5** | "estimation range" used for the **profile** range | Confirmed: scored range is (0, 40.83], profile [0, 9.68] | ACCEPT |
| **1.6** | 264/303 cited to Table 5 | **Confirmed:** Table 5 contains neither value; they are fixed-window scores | ACCEPT |
| **1.7** | "M1 fit" should be "M1b fit" | Confirmed from context | ACCEPT |
| **1.8** | Prop 4.1 cites §3.3 for Spec A M2 evidence | Confirmed: §3.3 is Specification B; correct cite is §3.1 | ACCEPT |
| **1.9** | Table 10 cites "§1, §4" for M1 collapse | Confirmed; should be §3.1 | ACCEPT |
| **1.10** | "34% of the old LRP" ambiguous | **Confirmed:** 2015 gives 33.8%, 2024 gives 38.7% — the year must be named | ACCEPT |
| **2.2** | 1992 drop called endogenous in one place, policy elsewhere | Confirmed; the model supplies it exogenously | ACCEPT |
| **2.5** | Test-sounding language ("separating") | Accepted; softened to interval wording | ACCEPT |
| **3.x** | Five fields unnumbered; 121/115 mislabelled as fitted parameters; K=500 ambiguity; missing article; "Accordingly … therefore" | All confirmed | ACCEPT |

**Deferred, with reasons:** **2.3** (minimum index-transition count) and **2.4** (printing
the M2-vs-M1b comparator rows) both require emitting new counts or table rows from a rerun
rather than editing prose; **2.6** (whether any *secondary* ranking would change if the
floor were removed) is a new sensitivity computation. v36 states what is already
established — no retention verdict depends on the floor — and leaves the secondary-ranking
question open rather than asserting an unverified answer.

---

## 2. What changed in v36

All Priority 1–6 items implemented. Verification: a **30-point removed/present check**
against the compiled source — 16 stale strings confirmed gone, 14 replacements confirmed
present.

The guard reported 6 B1 blockers (`16.7`, `108.2`, `1.51`, `221.7`, `0.90`, `206.3`). Each
was machine-checked against the archived **annual-pass** DM file and confirmed to be a
superseded value replaced by its regime-pass counterpart — a justified override, not
content loss.

---

## 3. Process note

Two consecutive rounds have now found defects created by a correction rather than by the
original text (round 6 item H5, round 7 items 1.1 and 1.2). The rule that follows is
narrower than "grep every changed number": **when a table's values change, grep the
document for the values that were *removed*, not only for the ones added.** A stale
citation survives precisely because the new number is present somewhere else and the old
one is never searched for.

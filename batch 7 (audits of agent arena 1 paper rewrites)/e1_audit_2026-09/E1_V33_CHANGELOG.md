# E1 v33 — round-6 residual items + register scan

**Base:** v32. Closes the twelve round-6 items not covered by the v32 changelog, and
records a targeted register scan.

## Round-6 residual items

| # | Change |
|---|---|
| **H12** | "M3's φ=0.95 persists a negative residual and increases error" now names the referent: error rises **relative to persistence**; against its declared comparator M2 it still reads lower. |
| **H15** | Catch dating consequence stated: under the coarse regime the 1992 drop falls in the 1992→1993 step, so on the fixed collapse window (1991–1995) it **does not enter the first two forecast steps** — the models are already rising before it applies. |
| **H18** | The 1995 window overlap, previously noted only for Specification A, is now noted and justified for Specification B. |
| **H19** | "M1b reads below M1" scoped: true at h=1 on Specification A and on the fixed recovery window, **not** on Specification B (152 against 120 kt; archived 151.63 / 119.47). |
| **H20** | The profile's narrower range is now described as an **interpretive restriction**, not a feasibility condition or a statistical ground for excluding higher thresholds. |
| **H22** | Explicit: **no retention verdict depends on the log floor** — it affects the log column only, and the raw-RMSE column is the retention score. |
| **H24** | M4's indexing specified from code: the first update applies `C_{t-1}`, the first projected residual is `φ·e_last` where `e_last` is the residual of the `S_{t-1}→S_t` transition, so the first update re-forecasts the transition its residual was fitted on. |

**H16, H21, H23** required no change: the Specification A uncertainty-pass disclosure, the
`0.000` tail fractions, and the descriptive-curvature statement were already in v32.

**H34/H35** (formal information-set table, canonical origin list) remain deferred — each is
a table assembled from code rather than prose.

## Register scan — editorial / changelog / meta-commentary / over-hedging

Run two ways, because the register scanner and a hand grep can fail differently.

1. `manuscript_style_scan.py`: **0 blockers, 0 review items**.
2. Independent regex sweep over the body (comments and bibliography excluded) across four
   groups — editorial and self-praise, changelog and version references, meta-commentary
   and diary voice, over-hedging and metaphor apology: **0 hits in every group**.

**Positive control.** A copy of v33 with one violation of each category appended was
scanned: the detector fired on eight kinds (`version-reference`, `changelog` ×2,
`unresolvable-citation`, `diary`, `editorial`, `self-praise`, `metaphor-apology`,
`obvious-hedge`), while the unmodified file returned zero. The clean result is therefore a
real pass, not a silent skip — a check worth running, since this scanner reports
"0 files" when a file has no hits, which has previously looked like a skipped scan.

## Gates

Compile clean; register 0/0; content guard **0 blockers**, 3 warnings; self-test 5/5;
title and `\thanks` byte-identical; abstract 250/250; highlights 69/67/70/64/81, all ≤85.
Seven-point verification of the new edits against the compiled source: all pass.

# Open content items

Things a structural detector cannot see. The gate checks whether an artifact is
*well-formed*; it cannot check whether it is *true*, *complete*, or *yours to
assert*. These are tracked here so they do not drift.

Status key: **OPEN** = needs a human decision · **DONE** = resolved, with where.

---

## 1. CRediT authorship contribution statement — **OPEN**

Who did what is a fact about people, not about the manuscript. It cannot be
inferred from the `.tex` and must not be invented. A template with the full
CRediT taxonomy and blanks marked is now in place in both files; the blanks
need filling at submission.

| File | Before | Now |
|---|---|---|
| `paper09_cod_certification_v32.tex` | `[To be completed at submission.]` | template, all 14 roles listed |
| `paper08_governance_delay_v46.tex` | absent entirely | template added before the AI declaration |

Two blanks to fill in each:
- **Author name.** Neither file declares `\author`. The self-citations read
  `Abaee, A.`, but the full name appears nowhere in the manuscript, so the
  template says `[AUTHOR NAME --- full name as it should appear]`.
- **Which roles apply.** Delete the ones that do not.

Also worth deciding: the AI declaration and the CRediT statement both describe
contribution. They are kept separate on purpose — AI tools are named in the AI
declaration, never as a CRediT contributor — but if the venue expects CRediT to
carry everything, that is a venue-format call.

## 2. Author contributions, prose form — **OPEN**

Distinct from CRediT. `paper08_governance_delay_v46.tex` has no
Author-contributions paragraph of any kind. v45 had none and v50's was a
placeholder, so there was nothing to merge and nothing to repair. If the venue
wants prose as well as CRediT, this needs writing.

## 3. Supplement / declaration questions — **DONE, recorded**

These were open at the end of the paper08 and paper09 turns. All three are now
resolved and the reasoning is in `MERGE_PIPELINE_DIAGNOSIS.md`:

- **Both supplementary-material passages are required.** An earlier note
  proposed keeping passage A and dropping passage B. That was wrong, and the
  test that produced it was wrong: it compared supplement vocabulary against
  the *main text*, but supplement-only sections are absent from the body by
  design. Tested against the supplement `.md` files, A matches the delay
  supplement 11/11 and B matches the governance supplement 10/10, and both
  files state that both are required. **Both kept in v46.**
- **The `paper4_supplementary` cross-unit pointer** is a stale filename from the
  unit rename, not contamination. **Corrected in v46** to
  `supplementary_delay` / `supplementary_governance`. Still present in the
  superseded v42/v43/v44, which nobody will fix.
- **Anonymised vs identified declarations.** Preprints.org is **not**
  double-blind, so the four `"Anonymized for review."` placeholders were
  **resolved to real content rather than preserved**, and both Data
  availability statements were kept because they describe different data.
  Preprints.org is the final target; this is settled, not provisional.

## 4. Detector gap — **OPEN, deliberately**

`K.split-refs` only fires when a fragment has **no year** and opens with one of
~18 hardcoded journal names. Tails that carry a year, or that open with a title
word, are invisible to it. Three of the seven tails repaired in paper09 v32 were
invisible; so was the second tail in paper11 v64, which the gate reported clean.

`p5/scan_continuations.py` implements a second signal and runs **report-only**,
so its false-positive rate can be measured before anything is made fatal.
Triage across 59 files:

| Signal | Hits | Verdict |
|---|---|---|
| `C:place-tail` — bare publisher/city, no year | 20 | **100% precision**, all in superseded files. Safe to promote to fatal. |
| `B:no-year+no-author` | 18 | ~89%. Two false positives: `U.S. Geological Survey. National Water Information System…`, a legitimate year-less government data citation — the `AUTHORISH` regex does not handle corporate authors with initials. Needs tightening first. |
| `A:shipped-rule` | 8 | Already fatal. |
| `E:continuation-word` | 3 | **Removed.** 0-for-3, all `von Neumann, J. (1928)…` — a lowercase nobiliary particle is not evidence of a tail. |

Real defect this found that the gate missed: **paper11 v64** had a second
detached pair, `Texas Water Development Board.` (L3761) and
`Water Data for Texas, well 6837203 (J-17)…` (L3778), 17 lines apart.
Repaired.

**Recommendation:** promote `C` to fatal now; keep `B` report-only until
`AUTHORISH` handles corporate authors.

## 5. Gate counts — **DONE, but with a caveat**

The gate counted *findings* and printed them as "failure(s)", while the reports
counted *files*, so "32" and "12" looked contradictory. It now prints both,
labelled, and fails only on live heads:

```
LIVE HEADS failing  : 0 file(s), 0 finding(s)   <-- exit status
superseded, ignored : 9 file(s), 21 finding(s)
scanned             : 59 file(s)
```

**Caveat, stated because it bears on whether to trust the earlier number:** the
historical figure of 32 does not fully reconcile. Measured deltas account for
7 of the 11-finding drop (6 removed by the three repairs, 1 by the rule I
rewrite; 2 more if the count predated the v46 repair), leaving ~2 unexplained.
The most likely explanation is that "32" was recorded from a partial run
mid-turn in an earlier session. **Treat the current numbers as the baseline and
disregard 32** — it is not reproducible and should not be cited again.

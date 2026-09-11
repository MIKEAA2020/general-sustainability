# Should the other agent's E2 v23 / E4 v15 changes be imported into `latex/`?

**Answer: yes for both. Both are real gaps in the current `.tex` files, both are
verified correct, and both are additive — no frozen value changes.**

## Where the files are

Not missing, as I reported earlier — they are **markdown sources** at
`arena agent 1/paper rewrites/`, whereas the compiled manuscripts live in
`arena agent 1/paper rewrites/latex/`. The repo carries both layers, and the other
agent updated only the `.md` layer. The `.tex`/`.pdf` in `latex/` remain at E2 v22 and
E4 v14 and therefore do **not** contain the two fixes.

## Change 1 — E2: xteNCAM specification disagreement in abstract + conclusions

The `.md` diff adds, in two places, that the findings are *convention-robust but
specification-conditional*: on the unpooled xteNCAM specification (LRP 276 kt) the
expansion classification and kernel ordering survive, while the reference point's
self-viability does not — the 2024 stock (342 kt) sits between that specification's
one-year (309 kt) and five-year (368 kt) zero-catch boundaries.

**Verified in `latex/paperE2_cod_intervention_v22.tex`:**

| check | result |
|---|---|
| 309/368 boundaries present in body (§3.11) | **yes** |
| the qualifier present in the abstract | **no** |
| "specification-conditional" anywhere | **no** |

So the finding is in the body but absent from the abstract and conclusions. That is
exactly the defect pattern corrected in E1 at v45 — a result confined to one section
while the framing sections still read as if it did not exist.

**Source values verified independently:** the archived `xtencam_table17_ssb.csv` gives
2024 SSB = **342.0 kt**; `SPECIFICATION_v2.md` confirms LRP 276 kt and the 1954–2024
window. The body text already prints the 309.4 kt one-year boundary.

**Import: yes.** High value, additive, no frozen value altered.

## Change 2 — E4: define "registered twenty-column analysis panel"

The `.md` diff glosses the term as the companion forecast evaluation's fixed analysis
dataset, noting that only head, recharge and pumpage columns enter E4's analysis.

**Verified in `latex/paperE4_edwards_intervention_v14.tex`:** the phrase "registered
twenty-column analysis panel" appears **undefined** — the gloss ("fixed analysis
dataset") is absent. A reader cannot tell what the other seventeen columns are or
whether they enter the analysis.

**Import: yes.** Low cost, removes an undefined term of art.

## What does *not* need importing

Everything else in the other agent's report concerns work already present in the `latex/`
E2 v22 / E3 v16 / E4 v14 files, or other papers entirely. Checked and unaffected: E1 uses
`figs_e1` (their figure-downgrade incident was `figs_e2`); E1 retired "certificate" at
v20; E1 carries no dated-freeze claim; E1's bibliography entry still matches E3 v16's
title exactly.

## One discrepancy resolved, not a defect

E3 v16's abstract says "at five years climatology beats persistence robustly (16.80 vs
21.11 ft)" while my band check cites M2m h=5 = 17.44. These are different objects:
**16.80 is `naive_mean`** — E3's "climatology" is the training-mean baseline, not the
climatological-flux map M2m. Confirmed against `rolling_summary.csv`. Both figures stand.

## Recommended action

Import both changes as **new `.tex` versions** (E2 v23, E4 v15) built from the updated
`.md` sources, rather than editing v22/v14 in place — consistent with the standing rule
that revisions are new version files. Neither change touches E1, so E1 v49 is unaffected
either way.

**Caveat on scope:** E2 and E4 are the other agent's working set. The two fixes are
theirs; the useful contribution here is the verification that the `.md`→`.tex` layer is
out of sync, which is the sort of gap that survives precisely because each agent checks
only its own layer.

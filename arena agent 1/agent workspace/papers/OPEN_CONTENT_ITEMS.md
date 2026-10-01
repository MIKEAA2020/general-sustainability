# Open content items

Things a structural detector cannot see. The gate checks whether an artifact is
*well-formed*; it cannot check whether it is *true*, *complete*, or *yours to
assert*. Tracked here so they do not drift.

Status key: **OPEN** = needs a human decision · **DONE** = resolved, with where.

---

## 0. Read this first: "the gate says clean" ≠ "clean"  — **STANDING RULE**

**The gate's clean verdict has been wrong twice, in two consecutive turns.**

1. **It counted the wrong unit.** `--gate` did `bad += len(hits)` — counting
   *findings* — and printed the total as "N structural failure(s)", while the
   prose reports counted *files*. A figure of "32" and a count of "12 failing
   files" therefore looked contradictory when they were different units.
2. **It missed a real defect.** `K.split-refs` fires only when a fragment has
   no year *and* opens with one of ~18 hardcoded journal names. paper11 v64
   carried a second detached pair — `Texas Water Development Board.` and
   `Water Data for Texas, well 6837203 (J-17)…` — that met neither condition.
   The gate reported v64 clean. It was not.

Both times, **reading** caught what the gate did not.

**Therefore, standing rules:**

- **A clean verdict must name the checks that produced it.** "Clean" from a
  single gate is not a claim anyone should make or accept. Name the checks.
- **Run the report-only detector (`p5/scan_continuations.py`) on live heads as
  a routine**, not only after a repair. It is the check that found what the
  gate missed.
- **The corpus is not audited until the reading pass and the detector pass
  agree.** Neither alone is sufficient. Keep both running until they converge.

---

## 1. CRediT authorship contribution statement — **OPEN**

Who did what is a fact about people, not about the manuscript. It cannot be
inferred from the `.tex` and must not be invented. But a bare "to be completed"
placeholder gives the author nothing to fill in and gets skipped at submission,
so both files now carry the full CRediT taxonomy with blanks marked.

| File | Before | Now |
|---|---|---|
| `paper09_cod_certification_v32.tex` | `[To be completed at submission.]` | template, all 14 roles listed |
| `paper08_governance_delay_v46.tex` | absent entirely | template added before the AI declaration |

Two blanks to fill in each:

- **Author name** — **deliberately left blank.** Neither file declares
  `\author`. The self-citations read `Abaee, A.`, but the preferred name form
  for the paper is not asserted anywhere in the manuscript. The git identity is
  known and is still not a basis for guessing the byline.
- **Which roles apply** — delete those that do not.

## 2. Author contributions, prose form — **OPEN**

Distinct from CRediT. `paper08_governance_delay_v46.tex` has no
author-contributions paragraph of any kind. v45 had none and v50's was a
placeholder, so there was nothing to merge and nothing to repair. If the venue
wants prose as well as CRediT, this needs writing.

## 3. Supplement / declaration questions — **DONE, recorded**

Open at the end of the paper08 and paper09 turns; all three resolved. Reasoning
in `MERGE_PIPELINE_DIAGNOSIS.md`:

- **Both supplementary-material passages are required.** An earlier note
  proposed keeping passage A and dropping passage B. Wrong, and the test that
  produced it was wrong: it compared supplement vocabulary against the *main
  text*, but supplement-only sections are absent from the body by design.
  Against the supplement `.md` files, A matches the delay supplement 11/11 and
  B the governance supplement 10/10, and both files state both are required.
  **Both kept in v46.**
- **The `paper4_supplementary` cross-unit pointer** is a stale filename from the
  unit rename, not contamination. **Corrected in v46** to
  `supplementary_delay` / `supplementary_governance`. Still present in the
  superseded v42/v43/v44, which nobody will fix.
- **Anonymised vs identified declarations.** Preprints.org is **not**
  double-blind, so the four `"Anonymized for review."` placeholders were
  **resolved to real content rather than preserved**, and both Data
  availability statements were kept because they describe different data.

## 4. Duplicate detection: byte-identity replaced — **DONE**

Byte-identity was the wrong test. Two entries citing one report routinely
differ in citation style and nothing else, so a byte comparison says "they
differ" and leaves a human to notice the report number is identical. The DFO
2016 pair:

```
DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016.
DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.
DFO (2016). Stock assessment of Northern cod (NAFO 2J3KL).
\emph{Can. Sci. Advis. Sec. Sci. Advis. Rep.} 2016/026.
```

Not byte-identical. Same report, `2016/026`. Merged to one.

`same_work(a, b)` in `phase0_scan.py` now decides identity semantically:
a shared **DOI**, a shared **report number**, or the same **year plus ≥60%
title-token overlap**. `L.dup-ref-key` fires only when entries are the same
work, so the finding is actionable — "merge these" — rather than "go check
whether these conflict". Findings dropped from **32 to 18** across the corpus.

## 5. Detached-tail detector — **C promoted, B report-only, E dropped**

`K.split-refs` fires only on a fragment with no year that opens with a known
journal name. Three of the seven tails repaired in paper09 v32 were invisible
to it, as was the v64 pair. `p5/scan_continuations.py` asks the question the
shipped rule does not — *could this fragment stand alone as a reference?*

| Signal | Hits | Status |
|---|---|---|
| `C:place-tail` | 20 | **Promoted to fatal as `K.place-tail`.** 100% precision. Zero live-head hits today — it is a guard against future merges, which is the point. |
| `B:no-year+no-author` | 15 | **Report-only.** Was 18 with 2 false positives; the `CORPORATE` author guard removed them. Re-measure before promoting. |
| `A:shipped-rule` | 8 | Already fatal. |
| `E:continuation-word` | 3 | **Dropped.** 0-for-3, all `von Neumann, J. (1928)…`, flagged only for a lowercase nobiliary particle. |

False positives fixed in `B` (both legitimate year-less government data
citations): `U.S. Geological Survey. National Water Information System, site
08168710, Comal Springs at New Braunfels, Texas.` in paper11 v64 and paper11b
v2. `AUTHORISH` did not handle corporate authors with initials; it now defers
to the `CORPORATE` list in `phase0_scan.py` so the two rules agree.

**A near-miss worth recording.** The `CORPORATE` guard was first applied to
`K.place-tail` as well, and that was wrong: it suppressed five genuine tails —
`Cambridge University Press, Cambridge.`, `Eurostat, Luxembourg.`, `OECD
Publishing, Paris.`, `Princeton University Press, Princeton, NJ.`,
`Fisheries and Oceans Canada, Ottawa.` — because publisher names end in the
same words institutional authors do. `PLACE_TAIL` alone is 20/20 precise. The
guard applies **only** to the no-year/no-author signal, where the USGS false
positive actually arose. A guard added to fix one signal can silently blind
another.

## 6. Gate counts: the unexplained delta — **RECORDED, NOT RESOLVED**

Current gate output, and the only figures that should be cited:

```
LIVE HEADS failing  : 0 file(s), 0 finding(s)   <-- exit status
superseded, ignored : 9 file(s), 34 finding(s)
scanned             : 59 file(s)
```

**The historical figure of 32 does not reconcile.** Measured deltas account for
7 of the 11-finding drop: 6 removed by the three live-head repairs (counted
directly off the pre-repair copies still in `mtest/`), 1 by the rule I rewrite
(count-based → identity-based), and 2 more if the count predated the v46
repair. That leaves **roughly 2 findings unexplained**.

Most likely "32" was recorded from a partial run mid-turn in an earlier
session. It is not reproducible and **must not be cited again**. If someone
later asks why the count changed, the answer is here:

- unit mismatch (findings vs files) — the largest single cause of apparent
  contradiction;
- 6 findings removed by repairs, 1 by the rule I rewrite;
- ~2 unaccounted, presumed a stale partial-run figure.

## 7. Gate semantics — **DONE**

- Reports **files and findings separately**, labelled, instead of one number
  that silently meant findings.
- **Fails only on live heads.** Merging always writes a NEW version, so a
  superseded version is never re-merged and never repaired; nine dead files
  failing on every run is how a gate trains people to stop reading it.
  Superseded files are reported as informational.

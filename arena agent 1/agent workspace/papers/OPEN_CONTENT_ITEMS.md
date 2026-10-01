# Open content items

Things a structural detector cannot see. The gate checks whether an artifact is
*well-formed*; it cannot check whether it is *true*, *complete*, or *yours to
assert*. Tracked here so they do not drift.

Status key: **OPEN** = needs a human decision · **DONE** = resolved, with where.

---

## Eight-family last-versions preservation — **DONE WITH BOUNDARIES**

The user-named obstr, ws, comp, minimax, ebc, psuff, ARV, and E1 source
versions, PDFs, supplements, linked verifiers and E1 data were checked against
the reviewed standalone heads. Paper03's cited complete-proofs supplement was
absent and is now present in source-identical TeX/PDF, with a pointer in its
main article; older versions with superseded continuity arguments were not
restored. No other content repair was supported. E1's historical verifier
passes 49/49 only after fetching its separate RAM-timeseries dependency;
this is not an eight-family verification campaign. Figure-binary packaging
and upstream reproducibility remain deferred. See
[`FAMILY_DEPTH_PRESERVATION_REVIEW_2026-10-01.md`](FAMILY_DEPTH_PRESERVATION_REVIEW_2026-10-01.md).

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

## 1. Source-supported author identity — **DONE**

The owner explicitly approved the byline **Amin Abaee**. Paper08's
continuous-channel v45 and the unblinded sampled v46 identify this author;
the current combined v46 restores the approved byline. All three paper09
constituent studies (and the cod v29 seed) carry the **same exact** author,
affiliation, ORCID and source email block; current paper09 v32 now restores
that literal block on its combined title page. The versioned source dates
differ, so **no date was invented** for the new combined work. This corrects
the stale earlier instruction that its author name was deliberately blank.
The predecessor's CRediT role template was *not* permission to attribute
additional taxonomy roles. See
[`UNVISITED_CONTENT_REVIEW_2026-10-01.md`](UNVISITED_CONTENT_REVIEW_2026-10-01.md).

## 2. Approved prose contributions — **DONE; NO INFERRED CRediT ROLES**

The owner approved only “A.A. conceptualized the entire work, wrote, reviewed
and edited the manuscript.” This exact statement now appears in both current
paper08 v46 and paper09 v32; the latter replaces an unfilled template. No
additional CRediT taxonomy roles or unapproved personal facts were added.

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

## 8. Source-to-head content preservation — **CONFIRMED ITEMS REPAIRED; PRODUCER WORK REMAINS**

Historical audit (15 live heads, five supplements, 39 source-to-head comparisons):
[`CONTENT_PRESERVATION_AUDIT_2026-10-01.md`](CONTENT_PRESERVATION_AUDIT_2026-10-01.md).
Its evidence reflects the **pre-repair** heads; it is not a current defect list.
No manuscript edits or pushes occurred *during that audit*. The following are
subsequent, one-artifact-at-a-time repairs on 2026-10-01. Each manuscript has a
pre-repair snapshot and reviewed diff in `../content_audit/before/` and
`../content_audit/diff*.patch` where applicable, a source-anchored repair
script, actual-figure Tectonic compile, separate push and API reverse-sweep.

- [x] **Paper05 v16:** source-specific declarations, code/verification caveats,
  Chatterjee 2009, Stanley/Lovejoy detail, approved author/contribution; the
  container splitter refuses unsafe regeneration. See
  `../content_audit/commit05.txt`.
- [x] **Paper06 v67:** actual supplement pointer, source declarations and
  25-vs-24 caveat, Dasgupta–Mäler 2000 and nine publisher/page tails,
  approved author/contribution; splitter refuses unsafe regeneration.
  Commit `3f546425`.
- [x] **Paper11 v64:** Edwards-specific data/code record beside cod's,
  White 2000 in References, one title page and both source abstracts;
  `merge_11_11b.py` repaired and scratch-tested. Commit `fdadffe0`.
- [x] **Paper01 v63:** heading, v61's complete reference paragraphs plus
  nine distinct paper02 works (overlap merged by work rather than byte),
  approved source byline/contribution. Both v62 merger and v63 splitter
  now refuse unsafe regeneration. Commits `f6966ede`, `bbd9bc0f`.
- [x] **Paper07 v50:** restored literal unblinded-v46 author, companion
  citation/DOI, nine source-revision hashes, source declarations and only
  the approved contribution sentence; review-blinding was inherited from
  the deliberately blinded v47 seed, not introduced by a merge script.
  Commit `26c5b608`.
- [x] **Paper08 v46:** restored sampled-channel citations, DOI, revision
  hash and v45 author; replaced unfilled CRediT template with approved
  sentence and collapsed repeated title pages without deleting abstracts.
  `merge_08_07.py` fails closed on current unsafe remerge. Both existing
  supplement pointers and both channels' data declarations retained.
  Commit `dbec3656`.
- [x] **Paper11c v2:** cited Saint-Pierre 1994 moved verbatim from below AI
  into References; its merger checks source placement and its splitter
  refuses bibliography-less paper11c output. Commit `4f4ca017`.
- [ ] **Complete safe regeneration:** the paper05/06/11c splitters, the
  paper01 shared-reference merger, paper08 merger and paper09 merger
  intentionally **refuse** deficient output rather than fully regenerating
  the corrected terminal heads. For paper09, the refusal happens **before
  writing**, with reviewed v32 byte-identical in the negative test. This
  protection is not a completed pipeline rewrite.
- [ ] **Corpus-wide content tests:** generalize source-aware checks for missing
  whole sections, citation title/venue/page tails, references after
  declarations and inherited review masks. First measure report-only across
  the corpus and inspect false positives before promoting any broad fatal
  rule. Keep the manual reading pass; a detector alone is not the audit.
- [x] **Narrow paper07 v49 sensitivity prose correction (copied into paper08):**
  the source script, computation note, current paper07 v50 and current paper08
  v46 now label the calculated percentages as *finite ±2% shifts*, name the
  non-crossing case, and report the two spectral margins without an inflated
  ratio. Historical v49 remains unchanged as the origin witness. The
  source-executed check is `python3 content_audit/check_p7_sensitivity_addition.py`.
  Provenance and exact checks: [`CLAIM_EVIDENCE_AUDIT_2026-10-01.md`](CLAIM_EVIDENCE_AUDIT_2026-10-01.md).
- [x] **Unvisited version/seed preservation pass and paper09 front matter:**
  all 42 local intermediate→head pairs were screened report-only for shorter
  losses; four older merged Part II bodies were traced to their standalone
  destinations, and all five live supplements were compared with the correct
  source lineages. The only omitted, source-agreed live front matter found was
  paper09's byline and approved contribution, now restored without dropping
  the four source abstracts. A check *behind* the LaTeX seeds against original
  Markdown also found and corrected a conversion-mangled S16 lead-in in the
  paper10 supplement; its four-row table was untouched. Evidence and limits:
  [`UNVISITED_CONTENT_REVIEW_2026-10-01.md`](UNVISITED_CONTENT_REVIEW_2026-10-01.md).
- [ ] **Source-to-head reproducibility:** reviewed live heads remain target
  artifacts; final grouping is an owner decision. Repair the upstream producer
  and compare scratch output with the reviewed heads. No new 15-head scientific
  audit is a prerequisite. A full content/prior-art audit is a *separate optional
  project*, not an active repair block.

## 9. New-section evidence rule — **STANDING RULE AT THE ADDITION BOUNDARY**

When a section is **added**, before it is merged or copied into another paper,
check its quantitative prose against its *own computation*: every table heading,
perturbation size, finite/non-finite convention, percentage, comparison basis,
and qualifier must be supported by an identified source run. Preserve the
source run and a short review record with the new section. This is a
**content checklist** performed when the text is authored; a downstream
structural gate or Lean theorem is not a substitute. For the paper07 v49
sensitivity addition, `content_audit/check_p7_sensitivity_addition.py`
re-executes the source script and checks both current manuscript instances;
that targeted check is the regression example. Any *general* automated rule
must first be tested report-only for false positives and missed cases, not
promoted to a blanket fatal gate.

Latest named checks after these repairs: `phase0_scan.py --gate` reports **0
live failing files / 0 live findings**; `scan_continuations.py --live-only`
reports **0 live candidate fragments**. These named zeroes are *not* a
claim that every scientific or bibliographic claim has been verified. The
unreconciled historical gate-count delta remains recorded in §6 above.

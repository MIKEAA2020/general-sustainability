# The merges concatenate, they don't integrate

Finding and fix, 2026-10-01.

## The short version

paper08's reference list was repaired by hand — 5 glued lines split, 26 detached
tails reattached to their heads, 5 duplicate entries removed, the list re-sorted.
Every one of those repairs came back on a clean re-merge. **The merges are
scripted, so repairing merged output is temporary.** The repair belongs upstream.

Two defects have **different provenance** and need different fixes. Conflating
them was my error and produced a wrong instruction ("or a re-merge once the
script is fixed" implied the pointer was script-produced; it is not).

## Evidence

Sources are clean; the merge shreds them.

| | reference entries | orphan tails |
|---|---|---|
| `paper08_governance_delay_v45.tex` (source) | 36 | **0** |
| `paper07_sampled_governance_v50.tex` (source) | 37 | **0** |
| after `split_entries()` | 30 / 59 | **14 / 12** |

A clean re-merge (`merge_08_07.py`, gate bypassed) reproduced every artifact:
26 orphan tails, the glued `Ambio … Hutchinson` line, 2 Declarations blocks,
2 Supplementary material passages, the `paper4_supplementary` pointer.

## Defect 1 — SCRIPT-PRODUCED (H, I, K)

`merge_08_07.py` and `mergelib.py` both contain:

```python
parts = re.split(r'(?<=\.)\s+(?=[A-ZÄÖÅ][\w\'{}\\\"~\^\- ]{1,30}?, )', body)
...
merged.sort(key=lambda e: re.sub(r'[^a-z]', '', e.lower())[:24])
```

- The splitter breaks on `. ` + `Word, ` — exactly the shape of a book's
  publisher line. `…Interval Analysis.\nSIAM, Philadelphia.` becomes two
  "entries". It also misses real seams where the preceding token is a DOI or a
  bare page number, which glues one reference's tail to the next author's head.
- The sort key is the first 24 alphanumeric characters, so a detached tail sorts
  by **publisher** while its head sorts by **author**. That is the mechanism
  behind "heads sorted by author, tails sorted by journal".
- Separately: `for d in (decl_a, decl_b)` emits **one Declarations block per
  source**, and one Supplementary material passage per source. `merge_09_9b_10b.py`
  merges three sources, hence paper09 v32's **three** Declarations blocks.

**Fixing the source does nothing. The script must change.**

## Defect 2 — SOURCE-PRODUCED (J)

The `paper4_supplementary_v8.md` pointer is present in paper08 **v42 (L3424),
v43 (L3411), v44 (L3510) and v45 (L3568)** — all of which predate every merge.
It is a **stale filename from the unit rename**, not random contamination:
`paper4_supplementary_v8.md` is the ancestor of
`paper08_governance_delay_v46_supplementary_delay.md` (same title, same S1
"Interval Hopf Enclosures", 39,957 vs 40,136 bytes).

Verified: re-merging the corrected v45 gives **corrected pointer = 1,
stale = 0**. **Fixing the source fixes the output.**

## The gate

`phase0_scan.py` gained classes **H–L** plus `merge_gate()`, `gate_text()` and
`report_gate()`. `mergelib.py` and `merge_08_07.py` now gate the assembled
document **before writing**; if a fatal class fires the merge prints the
findings and **exits 1 without writing**.

```
H  more than one Declarations block
I  more than one supplementary-material passage
J  cross-unit paperNN_* file reference
K  split bibliography entry (detached tail / glued / journal opener)
L  duplicate bibliography key
```

`phase0_scan.py --gate` exits non-zero. Corpus-wide: **32 fatal findings**
(H: paper01, 03, 05, 08, 09v30, 09v32×3, 11v61×3 — I: paper06, 08 — J: paper08
×5 — K: paper03, 05, 06, 09v32, 11v64 — L: paper09v32).

### Calibration note

`L.dup-ref-key` is **non-fatal**. Making it fatal produced 176 failures, nearly
all false: paper11 carries four genuinely different Abaee 2026 works and
paper08 two different DFO 2024 documents. Those need `a/b/c` letters, not
deduplication. The fatal set is H, I, J, K and `L.dup-ref` (exact duplicates).

## Two corrections I owe

1. **Passage B is not contamination.** I tested its vocabulary against the main
   text, found `epistemic-layer`, `stage-scan`, `T_r` absent, and recommended
   deleting it. Wrong test — those are supplement-only sections. Against
   `…_supplementary_governance.md` it matches **10/10**. Both supplement
   passages are correct and both are required; the `.md` files say so
   ("Both files are required: the main text cites sections from each").
2. **`finalise_paper08_refs.py` duplicated 16 reference entries.** Its slice
   `lines[rule1_i:rule2_i]` lifted the Supplementary material section, but the
   second reference chunk sat between the prose and the closing rule, so the
   chunk came along. Every entry from Nešić to World Bank appeared twice. The
   gate's `ref_block()` stops at the first rule, which is why it was not caught
   at the time. Fixed in `repair_paper08_v46.py`, which verifies no entry would
   be lost before deleting.

## Status of paper08 v46

v46 is the head of that paper (`PAPERS_RESTRUCTURED.md`, #5 of seven, from
8 + 7) and is terminal — Preprints.org is the target and is **not double-blind**.
Terminal-artifact fixes applied and verified: 16 duplicated entries removed,
both supplement pointers corrected, Declarations collapsed to one integrated
block (the four `"Anonymized for review."` placeholders dropped; both Data
availability statements kept verbatim since they describe different data).

Gate on v46: **0 fatal findings.** 76 entries, 0 orphan tails. Compiles with
tectonic 0.15.0 — PDF builds, **0 undefined references**.

**Author contributions** is absent: v45 has none and v50's is a placeholder.
It needs to be written, not invented here.

---

# The upstream fix (2026-10-01)

Repairing v46 was the right call for that file and the wrong call as a policy,
because a repair is erased by the next re-merge. The three defects are now fixed
in the merge scripts, so a clean re-merge no longer produces them.

## What was wrong

**`split_entries()`** split the reference list on

    (?<=\.)\s+(?=[A-ZÄÖÅ][\w'{}\\"~^- ]{1,30}?, )

a period, whitespace, then "Word, ". That is exactly the shape of a book's
publisher line, so `Introduction to Interval Analysis.  SIAM, Philadelphia.`
became two "entries". Because the sort key was the first **24 alphanumeric
characters**, the orphan `SIAM, Philadelphia.` sorted under **S** while its head
sorted under **C** — the "heads by author, tails by journal" damage.

**`for d in (decl_a, decl_b)`** emitted one Declarations block *per source*, so a
three-source merge produced three blocks. Same for the supplement passage.

## What was done

1. `split_entries()` now splits on **blank lines**. A reference list is
   paragraph-delimited; this is both simpler and correct.
2. `ref_sort_key()` sorts by **surname, then year, then text**, replacing the
   24-character alphanumeric key.
3. `partition_refs()` pulls the supplementary-material section out of the
   reference block before splitting — in v45 it sits *between* References and
   Declarations, so it arrives inside the block. Without this its prose becomes
   one enormous fake reference, or is silently discarded.
4. `merge_supplement()` / `merge_declarations()` emit **one** section and **one**
   Declarations block, integrated from all sources.
5. The old-sentence-splitter **fallback for short lists** was removed: it was the
   buggy splitter, and `_split_glued()` now handles run-together entries.
6. `merge_08_07.py` no longer carries its own duplicate copies of
   `split_entries` / `norm` / the sort — it imports them from `mergelib`.

## Measured effect

| | before | after |
|---|---|---|
| v45 entries / orphan tails | 30 / 14 | **35 / 0** |
| v50 entries / orphan tails | 59 / 12 | **46 / 0** |
| re-merged v46: fatal gate findings | 37 | **0** |

The only remaining findings on a re-merge are ten **non-fatal**
`L.dup-ref-key` warnings: the same work cited in two name formats
(`Brown, C. J.,` vs `Brown, C.J.,`). These are correctly *not* auto-merged —
conservative de-duplication — and are listed for a human to reconcile.

## Two corrections made along the way

**Both supplement passages are required.** An earlier note proposed keeping
passage A and dropping B. That was wrong, and the test that produced it was
wrong: it compared supplement vocabulary against the *main text*, but
supplement-only sections are absent from the body by design. Tested against the
supplement `.md` files, passage A matches the delay supplement 11/11 and passage
B matches the governance supplement 10/10, and both files state that both are
required.

Detector rule **I** was therefore also wrong: it counted passages and failed on
more than one. It now compares *supplement identity* — two passages naming the
same file, or two near-identical unnamed passages, are duplicates; two passages
naming different files are complementary and pass.

## v46 must not be regenerated

A re-merge of v45 + v50 produces a clean file, but it is **not** v46: v46
contains content authored directly into it after the merge, which appears in
neither source (`Delay as a stabilising mechanism`, and the Niculescu, Pyragas
and Abdallah citations it depends on; the `sampled-governance channel` label;
`S1--S12`). Regenerating v46 would silently delete it. v46 stays as the repaired
head; the fix applies to future merges.

## Regression test

`p5/tests/test_merge_integrity.py` covers the generic `mergelib.merge()` used by
all six drivers: one Declarations block, one supplement heading, both passages
and both data statements kept, 3 unique references, no glued entries, no
headless fragments.

---

# Terminal repairs: the three live heads (2026-10-01)

With the scripts fixed, the remaining gate failures are legacy damage in files
that already exist. The test for whether a file gets a script fix or a direct
repair is "will it be re-merged?" -- merging always produces a NEW version, so a
current head will not be re-merged and must be repaired directly.

Corpus: 59 `.tex` files, 32 failing at the start of this work, 12 after the
script fix, **9 now**. Every one of the 9 is a superseded version (v62, v15,
v15, v66, v42/43/44, v30, v61). **All 15 live heads are clean.**

## paper01 v63 -- `8059d2b`

Two Declarations blocks, one per merge source. The second is cross-unit: its
Code availability names four **paper02** scripts and claims they "reproduce all
values, bounds, thresholds, figures, and tabulated entries verbatim". They
cannot -- paper01's label namespace is entirely `calc-` (39 labels), with no
`suff-` labels and no paper02 body. Dropped.

One name that looks like the same error and is not: block 1 names
`paper2_coverage_audit.py`, but so does the BODY at L1775, regenerating
paper01's own `calc-tab:coverage` and `calc-fig:coverage`, and paper02 v12 does
not mention the script at all. A stale filename from the unit rename -- the
paper08 v42/43/44 class. Kept; renaming it is a source-level change.

Verified: 0 fatal (was 1). Compiles: exit 0, PDF 478,150 B, 0 undefined refs.

## paper09 v32 -- `86f7d15`

A three-source merge (cod + ARV + Edwards) carrying three Declarations blocks
and six detached bibliography tails.

The tails were sorted INDEPENDENTLY of their heads -- "Aubin, J.-P., 1991.
Viability Theory." stayed under A while its publisher "Birkhaeuser, Boston."
sorted under B, four entries away. That is why the damage never appeared
adjacent to itself. Each tail was reattached using the source papers (v30/v31,
paper09b v2, paper10b v1) as ground truth; one orphan had no head of its own
(two sources carried Aubin, the heads de-duplicated, both tails survived) and
was deleted. A seventh, "Water Data for Texas...", was found late because it
opens with a title word rather than a publisher token, so the detector never
flagged it.

The three Declarations were integrated, not reduced: Data availability and Code
availability keep all three statements under lead-ins, because they describe
different data and different scripts; funding, competing interests and the AI
declaration are stated once because all three agreed.

Verified: 0 fatal (was 4). 51 entries, 0 tails (was 57, 6). Compiles: exit 0,
PDF 1,487,432 B, 0 undefined refs.

## paper11 v64 -- `7f89b2d`

One detached tail, "Fisheries and Oceans Canada, Ottawa.", four entries from its
DFO 2009 head. Intact in all three predecessors (v61/v62/v63). Two edits.

Verified: 0 fatal (was 1). Compiles: exit 0, PDF 1,294,630 B, 0 undefined refs.
The 7 remaining `L.dup-ref-key` warnings are non-fatal by design and left for a
human.

## Detector gap found while doing this

`K.split-refs` only fires when a fragment has **no year**. Tails that carry a
year in the detached half -- "Geological Survey Circular 1186, **Denver, CO.**"
is yearless, but "DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. **2016/026.**"
carries one -- are missed, and so are tails that open with a title word rather
than a publisher token. Three of the seven tails repaired here were invisible to
the gate and were found by reading. The rule needs a second signal: a fragment
whose text is a plausible continuation of another entry (publisher, city, or
report-number tail) should be reported whether or not it has a year.

---

# Follow-up: the gap, made measurable (2026-10-01)

The detector gap recorded above was implemented as a SECOND SIGNAL and run in
**report-only** mode across all 59 files before anything was made fatal, so its
false-positive rate could be measured rather than assumed. `p5/scan_continuations.py`.

The shipped rule asks "does this fragment open with a known journal name and
have no year?" The second signal asks the question the shipped rule does not:
**could this fragment stand alone as a reference?** A standalone reference needs
an author-like opening and a year; a fragment with neither is a tail.

| Signal | Hits | Verdict |
|---|---|---|
| `C:place-tail` | 20 | 100% precision, all in superseded files. Safe to promote to fatal. |
| `B:no-year+no-author` | 18 | ~89%. Two false positives, both `U.S. Geological Survey. National Water Information System...` -- a legitimate year-less government data citation. `AUTHORISH` does not handle corporate authors with initials. Tighten first. |
| `A:shipped-rule` | 8 | Already fatal. |
| `E:continuation-word` | 3 | **Removed.** 0-for-3: all three were `von Neumann, J. (1928)...`, flagged only for starting with a lowercase nobiliary particle. |

**It immediately found a real defect the gate had reported clean.** paper11 v64
carried a SECOND detached pair -- `Texas Water Development Board.` (L3761) and
`Water Data for Texas, well 6837203 (J-17)...` (L3778) -- seventeen lines apart.
The earlier repair had joined the DFO 2009 tail and the gate then said v64 was
clean. The same pair had already been repaired in paper09 v32, which is why it
looked done. Repaired.

## Gate corrected

The gate counted *findings* and printed them as "failure(s)", while the prose
reports counted *files*. "32" and "12" were therefore different units presented
as if comparable. It now prints both, labelled, and **fails only on live
heads** -- a superseded version is never re-merged, so nobody will ever repair
it, and failing on it is how a gate trains people to stop reading it:

    LIVE HEADS failing  : 0 file(s), 0 finding(s)   <-- exit status
    superseded, ignored : 9 file(s), 21 finding(s)
    scanned             : 59 file(s)

**Caveat on the historical figure.** 32 does not fully reconcile. Measured
deltas account for 7 of the 11-finding drop -- 6 removed by the three repairs,
1 by the rule I rewrite, and 2 more if the count predated the v46 repair --
leaving roughly 2 unexplained. Most likely it was recorded from a partial run
mid-turn. Treat the current numbers as the baseline; disregard 32.

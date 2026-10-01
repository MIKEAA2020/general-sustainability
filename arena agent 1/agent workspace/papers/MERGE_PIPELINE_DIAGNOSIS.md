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

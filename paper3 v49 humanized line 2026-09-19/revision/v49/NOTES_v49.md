# Notes on the v49 line — what was built, on what authority, and what is left open

Built 2026-09-19 against `humanize/v49_adaptation_first_brief.md`. The line of record for the article text
is `revision/v7/paper3_material_ledgers_v49.md`: 54 pages compiled, the same four documents as the v48 line.

## What v49 is

* **Base of record for the abstract and Section 1: the author's adaptation** — the `gemini:` half of
  `uploads/p3 humanized.txt`, lines 2–117 (title through the end of Section 1). The deposited article
  (`work/paper3.txt`) is the oracle: it decides what is right or wrong, not what is phrased how.
* **Repaired before adoption, not after.** Four operations, all logged in `v49_front_matter_edits.json`:
  chat residue stripped; the renamed vocabulary reverted onto the deposit's terms (5 substitutions, 12 rules enforced from `adaptation_term_revert_v1.csv`
  — `force` and `label` rows applied, `watch` rows reported only: stock-depletion ratio, physical depletion forecast);
  the four P0 invented assertions and the two-level framing deleted with their sentences; and a display the
  adaptation left inside a running sentence lifted onto its own lines (house style).
* **Two headings cut, one passage kept.** `Arithmetic Level` and `Dynamical Level (Yield Inflation)` went,
  with the adaptation's lead-in clause "The illusion operates on two levels:", because that is the framing
  the author ruled out. The deposited article's own two-senses passage was carried over verbatim
  (`v49_carry_over.json`) — see the next section but one.
* **Body, Section 2 onward: v48's body plus six sentences.** Nothing else moved, and that is asserted:
  after undoing the six insertions the LaTeX body is byte-identical to v48's.

## Why the body needed six sentences put back

Reading the 32 rows before the build (22 kept + 10 absorbed on atoms alone) showed the atom test was too
weak in the body as well as in the front matter. Six sentences that the deposited article states, and that
both v42 and v47 carried, are absent from v48 — each naming a defined object:

| named object | row | section | v42 | v47 | v48 | v49 |
|---|---|---|---|---|---|---|
| `monomaterial projection` | D0238 | 2.2 | yes | yes | **no** | yes |
| `never in the stock` | D0286 | 2.5 | yes | yes | **no** | yes |
| `differentiated only by` | D0385 | 4.3 | yes | yes | **no** | yes |
| `replenished by recharge` | D0521 | 6.5.1 | yes | yes | **no** | yes |
| `two readings of one ledger` | D0719 | 11 | yes | yes | **no** | yes |
| `not a primitive of the closed natural block` | D0631 | 2.5 | yes | yes | **no** | yes |

These are not waiver effects: all six sit outside Section 1, where the verbatim rule is enforced. The
mechanism was the `regen` bucket — v48 rewrote a draft sentence that already carried the deposit's wording;
the replacement kept the claim's atoms and lost the named object. In v49 each sentence is restored verbatim
from the line that carried it, placed after the aligned v42 predecessor line (log: `v49_front_matter_edits.json`
→ `restored`). Where exactly a restored sentence sits inside its section is a typographic judgement the
author may move; that it is present is not.

## The passage v48 had mangled

v48's abstract opened the productivity illusion with "The illusion has two senses, and they are distinct.
It is the compensatory-aggregation failure above …": the **second sense** and the `aggregation obstruction`
pointer to Section 10.1 had been dropped from it. v49 carries the deposited article's form over from v42 —
"It has two senses, and they are distinct. The first is arithmetic … This article formalises this sense as the
aggregation obstruction of Section 10.1. The second sense is dynamical and is yield inflation. …" — kept
beside the adaptation's two bullets, which now carry no labels. The result reads slightly doubled; unifying
it is an author's edit, not a build step.

## Gate state at the build

* `v49_waiver_gate_v1.py`, waived region, oracle = the deposit: **flag_count 0**, disclosure_count 14.
  Section 1 is checked against all 140 of its ledger rows, not exempted from them.
* `verify_v49_base.py`: **FAILURES: none** — 143/143 verbatim-protected body rows present;
  9 of 9 errata items closed; back matter byte-identical to v48's; body numerals unchanged (365 → 365);
  no unsupported Section 1 numeral; 17 Section 1 citations resolved; the compiled PDF carries
  187/187 flowing paragraphs; no unresolved reference; no stray list marker in the front matter
  (the E6 defect); and the delivered v48 package is still frozen at sha256 3ad72c04…564fa7.
* Four documents: article 54 pp, supplementary 19, companion A 10, companion B 8; overfull ≥6pt 0; `??` 0.
  The three companions are v48's bytes, hashed rather than recompiled, because v49 changes no companion.

## Open, for the author — not defects of the build

1. **The four status labels.** v48's abstract wrote `statistical index, not a stock ratio`,
   `arithmetic, not a forecast`, `pressure scale, not a depletion diagnostic`, `readouts of the ledger`.
   The adaptation's abstract states the same three classifications in its own words and the labels do not
   appear. No claim is lost. This is the one place where the build deliberately did nothing: restoring the
   labels would choose the deposit's exposition over the adaptation's, which is a content revision with its
   own decision. `G1b` in the gate now reports this class of difference (13 disclosed vocabulary items)
   instead of being blind to it.
2. **Two `watch` terms kept as the adaptation wrote them**: `stock-depletion ratio`, `physical depletion
   forecast`, one use each. `watch` was defined as "reported, not applied".
3. **The duplicated prose** where the carry-over landed.
4. v48's errata travel with this package (`ERRATA_v48.md`); the delivered v48 bytes were not touched.

## Two instrument failures found while building, and what they taught

1. `_rules()` in the waiver gate parsed the revert table with `len(fields) >= 8`, so it read **2 of 14**
   rules — every rule whose justification contained no comma was silently skipped, and G4/G5 had been
   enforcing one substitution. The lesson is that a check must report what it read: G4/G5 now returns "14
   revert/cut rules read, all satisfied", so a zero that means "nothing was tested" is visible.
2. My first front-matter pass rebuilt every line from the sentence splitter's output, and that splitter
   masks `$…$` as a placeholder — so the adaptation's inline mathematics became a literal `M` and its
   numbered lists lost their numbers. `diff` caught it, no gate did. It is the forbidden act in a new
   costume: rebuilding prose from a masked view of it. Lines are now byte-identical unless a sentence is
   actually deleted, and deletion is done on the raw line; the region maths count (11 spans in the markdown,
   11 in the LaTeX) is what keeps it honest.

A limitation stated rather than hidden: a vocabulary registry is still a list. `G1b` assembles its terms
from three sources (TERMS, the previous line's emphasised phrases and coinages, and the label list read out
of `build_v48_base.py`'s `KEEP`), which is why it caught what `G1` alone missed: `G1` compares base→build,
and where the base *is* the rewrite, that comparison cannot see what the previous line of record carried.
Whoever extends this line should not trust a hand-curated registry, including the one described here.

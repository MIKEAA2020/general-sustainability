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

## The reader's four points, and what each one turned out to be

The first v49 was packaged, pushed, and then read. Four things were wrong or wanted; all four are
addressed, and three of them were not the small problems they looked like.

**1. The abstract's first line.** The shipped v49 opened on the adaptation's sentence
*"Depletion metrics routinely circulate under a single colloquial label while answering fundamentally
incomplete questions."* It now opens, as instructed, on the deposited article's
*"Depletion indicators can carry similar units while built to inform distinct questions."* The
adaptation's opener was removed rather than left in place of honour second: it makes the same point,
and keeping both would have doubled it. Both strings are recorded in
`v49_front_matter_edits.json → first_line`, so the removed wording is recoverable.

**2. The introduction had no spacing, because its headings had eaten their paragraphs.** This was a
build defect, not a style choice, and it had two causes. The adaptation's file glues a paragraph to the
line under each of five headings (`### Abstract`, `### 1.1`, `### 1.2`, `#### What Is Explicitly Not
Claimed`, `### 1.3`); and the builder joined the extract's lines while discarding blank lines, so the
glue became structural. A block dispatcher that classifies a chunk by its first line — `if
b.startswith('### ')` — then took heading *and* paragraph as one heading, and emitted the lot as the
argument of `\subsection*{…}`. So `1.1`'s prose, `1.2`'s entire numbered contributions list and `1.3`'s
organiser sentence were set as heading type. The abstract heading also arrived at the wrong level
(`### Abstract` reached the LaTeX as a subsection, not the line of record's `\section*{Abstract}`).

The fix is a normalisation pass applied to the adaptation's front matter *before* it is adopted
(`house_form`), which does exactly three things and proves it: it drops the byline block, puts a blank
line wherever house style requires one, and raises `Abstract` to `##`. The proof is whole-line, after
two character-counting attempts that were wrong in opposite directions — one read `---` inside a table
rule as a dropped horizontal rule, the other deleted the *title's* `#` instead of the abstract's,
because `str.replace` finds the first match. Result: `every paragraph is now a paragraph` is a
measurement, not a hope — the compiled article carries **203 of 203** flowing markdown blocks where the
same check had reported 187, and the five swallowed blocks are the difference.

**3. The author block appeared twice, wide and duplicated.** The five byline lines came from the
adaptation, and v48's kept header (`\author{…}`, `\date{…}`) set them again. The line of record carries no
byline in its markdown — that is what the header is for — so those lines are now dropped at the source
and the block appears once, in the header, with ORCID and affiliation typeset narrow. One conflict is
disclosed rather than smoothed: the adaptation is dated *September 6, 2026*, the header of this line says
*September 17, 2026*, and v49 keeps the header's date because v49 is that lineage continuing.

**4. A line-level read of the shipped file.** `audit_v49_lines_v1.py` refuses to let a line of v49 be
unexplained: every non-empty line must be byte-identical to a v48 line, or to the adaptation's, or be
reproducible from one by a logged substitution/label cut, or be the instructed first line, the carried-over
passage, a restore, or the logged body repair. It then tests content per line — every one of the
**1,486** maths spans against v48 ∪ deposit (∪ v42 where a logged restore carried it), every numeral
against the same sources, and a list of formatting flaws — and reads the PDF: the abstract's first
typeset sentence, one appearance of each byline element, no heading-sized line carrying body text.
Current state: **provenance complete for all 1,694 lines** (1,196 v48-identical, 59 adaptation-identical,
7 by logged substitution or cut, 1 first line, 1 carried-over passage, 6 restores, 424 blank), maths 0
unsupported, numerals 0 unsupported, 0 new formatting flaws (2 inherited from v48, both a heading with no
blank line before it, legal in markdown and typeset correctly), 0 PDF findings.

### What that read caught, which every gate had passed

* **Two of the six restored sentences were badly built.** The restore text had been lifted from a
  flattened dump of the previous line, and that dump had already (a) turned `$\ell=\mathbf{1}$` into a
  bare `M`, and (b) run past paragraph boundaries. So one restore re-inserted a *duplicate* of the
  sentence v48 already carried, in the older wording, and another crossed a horizontal rule into the
  following paragraph. Both are now re-derived from v42's raw markdown by `make_restores_v2.py`, which
  refuses any insert that is not a verbatim substring of its donor line, that unbalances `$`, that
  crosses a heading or rule, or that repeats a sentence already on the target line (similarity ≥ 0.62).
  Three of the six claims are now carried as `extend-final-sentence` — the donor's own clause grows the
  sentence v48 kept — and three as whole verbatim sentences. The em-dash clause is joined with a space,
  a `:` or `;` clause is glued, so no `resource :` crevice is left behind.
* **v48 had shipped the same sentence twice** at §4.3: *"Two scope notes are part of the theorem."* plain
  and then bolded. v42 carries it once. The bolded twin is deleted, and the deletion is a logged edit —
  `v49_body_repairs.json` — with an assertion that the survivor count is exactly one. It is erratum E10
  of the v48 line.
* **Two reference entries are now cited by nobody**: `United Nations, 2014` (the SEEA Central Framework,
  which standardised the definition and recording of depletion) and `United Nations, 2025` (the System of
  National Accounts treatment). Both were cited only in the §1 passage the adaptation does not carry —
  the passage is *not* in the deposited article, so it is the previous line's own addition, and this build
  will not silently re-insert or silently delete it. `Baez 2023` and `Illakwahhi 2024` were uncited in v42
  and v48 too, and are recorded as house-style items for the author rather than defects introduced here.

### Instruments corrected while doing this

`texkit.overhang` reports zero pages when PyMuPDF is unavailable, which had turned "not measured" into
"0 overfull, 0 undefined" — the compile step now refuses to record a clean result for a document it could
not measure. The compile report was being read by the verifier while describing a superseded build, so the
report's own mtime is now part of the freshness assertion. The protected-row pin requires v48's wording
verbatim; three rows are grown by a logged clause, so the verifier now undoes exactly the insertions this
build logged, on the raw body, before normalising either side — an unexplained rewording still fails. And
the audit reads both kinds of revert rule (6 substitutions and 6 abolitions, 12 enforced) rather than
counting one kind and reporting 12, which is how a control can pass while reading half the file.

---

## Round 5 — point 2 spacing, point 3 byline, and a gate that had been reading a stale page

**The three build defects and their fixes, as before, plus the new ones:**

* A heading that swallows its paragraph: the adaptation emitted 11 lines where a `####` heading
  carried whole body sentences (`#### 3.2.1 A readout answers a narrower question than an exhaustibility
  verdict. It asks whether...`). Fixed in the builder: the heading's first sentence stays, the rest becomes
  its own paragraph, with an assert that no kept heading argument exceeds 190 characters. The renderer's
  own `\partitle{}` argument (631 characters) was then caught by a *new* check the audit raised as an error
  (`overlong_heading_arguments` in `build_v49_tex.py`), and a 190-character cap now applies to every
  heading argument, including `section*`/`subsection*` ones.
* The byline was present in both markdown and the .tex header. Removed from the markdown; the .tex header
  keeps the ORCID, and the rendered page still shows name, affiliation, email, date, editor.
* Punctuation spacing from the flattening step, fixed as before.

**The instrument failures this round found — the ones worth remembering.**

1. **The gate had been reading a stale surface.** The front-matter extracts it audits were hand-cut during
   an earlier round; after the byline removal they no longer described the shipped file, so `flag_count: 0`
   certified a document that did not exist. Fixed at both ends: `build_v49_base.py` writes
   `v49_base_front_matter.md`, `v49_front_matter.md` and `v48_front_matter.md` on every run, and the gate
   refuses to run unless `--built` matches the shipped front matter (`--allow_stale_built_surface` to
   override). The verifier re-checks it (`gate_input_is_the_shipped_file`) and asserts the gate and audit
   reports are newer than the markdown they describe.
2. **A numeral extractor that invented a number.** `\d{1,3}(?:,\s?\d{3})+` matched `6, 202` inside
   `September 6, 2026`, so the gate reported a lost numeral `6202`. A `(?!\d)` lookahead bounds the
   thousands groups.
3. **An excusal needs a page, not a promise.** Numerals removed with the byline are excused only when the
   digits come from a logged `byline_lines_removed` line *and* the rendered front pages show them —
   `--absorbed v49_pdf_front_pages.txt` (written by `build_v49_tex.py`, digits intact, because the audit's
   normalised text is letters-only). Five items (the four ORCID groups and 2026) are excused this way; an
   item the header does not show is listed as superseded, never hidden.
4. **`_anchors` was keyed wrong, and reported surviving cites as lost.** Four rounds of fix:
   (i) `&`-form cites keyed on the second author; (ii) a name split by a line wrap keyed on a fragment;
   (iii) the narrative form keyed on the *last* name (`Tilton and Lagos (2007)` → Lagos); (iv) institutions
   keyed on a bare `United`. All keys are now `lead author of the cite + year`, and a `def _anchors`
   duplicated three times in the file had to be deleted — the last definition was shadowing the good one.
   The accurate result: v48 §1 carries 21 anchors, v49 §1 carries 18, and the three that went are
   `Clark, 1990` (cited twice elsewhere, no orphan) and `United Nations, 2014` / `United Nations, 2025`.
5. **Re-adding a check after deleting its neighbours failed twice** — first on a front-matter boundary rule
   that differed from the producer's (grabbing the end-of-section-1 rule at line 321 instead of the
   front/body rule at 119), then on a variable the deletion had taken with it. A checker's rules must be
   the producer's rules, verbatim.

**Green state of the whole chain, rebuilt from scratch:** md 1,694 lines (215,028 B),
`v48_body_lines_lost_by_this_build: 0`, `front_matter_lines: 118`, `restored: 6`, `term_edits: 5`;
.tex 54 pp / sup 19 / A 10 / B 8, all `rc=0`, overfull ≥ 6 pt 0, `??` 0, 203/203 flowing markdown paragraphs
on the page; gate `flag_count: 0`; audit 2 findings, both the UN author decision; verifier `*** v49 verified ***`.

**Open for the author, unchanged:** whether to drop reference entries `United 2014` and `United 2025` or
restore v48's two §1.1 sentences that cited them (the passage they supported is not in the deposited
article, so this build cannot legitimately absorb it).

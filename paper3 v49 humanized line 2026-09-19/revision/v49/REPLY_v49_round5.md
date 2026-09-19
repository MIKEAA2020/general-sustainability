# v49, round 5 — points 2, 3 and 4

All three of your points are in the document, and point 4 (the line-level read) is what found the
worst problem this round — in my instruments rather than in your text, which amounts to the same
thing: a check that passes for a document that no longer exists is worse than no check.

`revision/v7/paper3_material_ledgers_v49.md` — 1,694 lines, 215,028 bytes
`revision/v7/paper3_material_ledgers_v49.pdf` — 54 pages, 391,470 bytes

## 2. Introduction spacing — fixed, and the cause was worse than it looked

The introduction's paragraphs were welded to their headings because the adaptation emitted 11 lines
like:

```
#### 3.2.1 A readout answers a narrower question than an exhaustibility verdict. It asks whether …
```

The builder now splits each such line — heading sentence stays in the heading, the rest becomes its own
paragraph, blank line between — and asserts the result:

* **no line in the shipped markdown contains `####` and a newline**;
* no line begins with a heading marker and a bracketed number and exceeds 190 characters;
* every kept heading argument ≤ 190 characters.

The PDF confirms it: 64 of 65 headings are followed by a body block, and the one that isn't is
`## Appendix C. A Note on Sources and Access`, which genuinely opens with a `###` subheading. The
rendered `.tex` now reads `\section*{Abstract}` and `\subsection*{1.1 The problem …}` with real body
underneath, where before the whole paragraph had been swallowed into the heading argument (631
characters of `\partitle{}`) — the audit raises that as an error now (`overlong_heading_arguments`).

## 3. Author block — one appearance, and the numbers moved rather than vanished

The byline was removed from the markdown; the `.tex` header keeps it (name, ORCID, affiliation, email,
date, editor), rendered as a single block on page 1. The audit counts the *lines*, so
`Independent Researcher` appearing once on that one block is not a duplicate: `identity_repeats: 0`.

That removal made the front matter lose five numerals — the four ORCID groups and `2026` — so the
gate, whose whole job is "nothing was dropped", could no longer read clean. It now excuses them
properly and I had to teach it what "properly" means:

1. `build_v49_base.py` writes the gate's three input extracts on every build (they had been cut by
   hand in an earlier round and never refreshed — so `flag_count: 0` was certifying a stale page);
2. the gate **refuses to run** unless its `--built` surface equals the shipped front matter (proved by
   pointing it at a stale copy: it exits with an explanation and writes no report; on the current file
   it prints `G0: the built surface is the shipped file`);
3. a numeral excused as "absorbed by the header" must be **found on the rendered page** — the builder
   now dumps the PDF's first two pages with digits intact for exactly that check
   (`v49_pdf_front_pages.txt`, 7,223 B);
4. an item the header does *not* show is listed as superseded, never hidden.

Result: `flag_count: 0`, 15 disclosures, `not_retained_by_the_header: []`.

## 4. The line-level read, and what it caught

Two real bugs in the numeral extractor and four in the citation-anchor checker, all found by reading
its own output rather than trusting a zero.

* **The gate invented a lost number.** A thousands pattern `\d{1,3}(?:,\s?\d{3})+` matched the `6, 202`
  inside `September 6, 2026` and reported a numeral `6202` missing from the document. Fixed with a
  `(?!\d)` lookahead. Also: `MT.page_text` is letters-only, so the audit could never have contradicted it.
* **The first absorbed-digits check squeezed the whole page into one token**, matched the squeezed
  numeral against a non-squeezed needle, and falsely claimed the header does not show `2026` when it
  does. Now the same extractor runs on both sides.
* **`_anchors` reported four surviving cites as lost**, in four different ways: `Brunner & Rechberger`
  keyed on the second author; `Tilton\nand Lagos` split by a source line break keyed on a fragment;
  `Tilton and Lagos (2007)` — narrative form — keyed on the *last* name; and institutions keyed on a
  bare `United`. One rule now, keyed on the lead author plus year, applied to both capture paths.
  While fixing it I found `def _anchors` **defined three times in one file**, the last (buggy) copy
  shadowing the good one.
* Re-adding the two checks I deleted failed twice, correctly: first the verifier's front-matter rule
  picked line 321 (the end-of-§1 rule) where the builder picks 119, then a variable the deletion had
  taken with it. A checker must use the producer's rule, verbatim.

**What the document itself shows.** Every line classified: `v48-identical 1196, adapt-identical 59,
first-line 1, restore 5, restore + logged body repair 1, carry-over 1, term-revert/label-cut 7,
blank 424`, `house-form/term-revert/label-cut 0` (the 11 heading lines are now accounted for as
`adapt-identical`, which is what they are). Maths: 1,486 spans, none unsupported; the 3 spans on
restored lines come from v42 through the logged restores. Numerals: `without_source: []`. Formatting:
0 flaws new in this file, 2 inherited from v48 unchanged (a space before `;` and a bare display fence —
left alone, since v48 shipped them and this base is not the place to edit your body). PDF: 0 findings.
Section 1 anchors: v48 21 → v49 18.

## Numbers after the rebuild, from scratch

md 1,694 lines (215,028 B), `front_matter_lines: 118`, `body_lines: 1573`, `term_edits: 5`,
`restored: 6`, `v48_body_lines_lost_by_this_build: 0`, `body_additive: true`,
`protected_rows verbatim 140 + 3 after undoing the logged insertions, missing []`,
`adjacent_duplicate_sentences: 0`; .tex 6/6 insertions placed where the markdown put them,
`body_byte_identical_after_undoing_the_six_insertions: true`, front-matter maths 11/11,
labels 69 / refs 0 / unresolved 0; compiles 54 / 19 / 10 / 8 pages, all `rc=0`, overfull ≥ 6 pt 0,
`??` 0, 203/203 flowing markdown paragraphs on the page; gate `flag_count: 0`, 15 disclosures;
audit 2 findings, both the one open item; `*** v49 verified ***`, `FAILURES: none`.

## Where things are

Package v9: `revision/v49/paper3_supplementary_package_v9.zip`, 84 records, 2,128,501 B,
sha256 `afa993932828d8f81b09b6afdda22225dcd7358dd73ac5fd13f3c9582f93a26b` — 2,134,376 B, 84 records (v9 because v8 belongs to v48; two earlier v9 builds
were superseded inside this round, first by the byline fix and then by the matcher fix, which changed
NOTES, ERRATA, the open items and the line audit inside it).

Archived to `archive/paper3-v48-workspace` at `1554ed9211b0` (parent `7400680f813a`): 127 files,
9.7 MB, tree 660 entries, 138 under `paper3 v49 humanized line 2026-09-19/`. The archived v9 zip's
sha256 was read back and matches the local one; v48's v8 zip in the archive is still
`3ad72c04f57985c8…`. `main` was not touched by this push — it has its own new head, `856b73e06ef8`,
a `worklog.md` commit by "Z User" dated 08:24Z, from elsewhere in your work.

Removed locally: `tools/tectonic` (the 93 MB binary is archived; the recipe with its sha256 stays in
`tools/README.md`).

## The one thing I cannot settle

**Reference entries `United Nations, 2014` and `United Nations, 2025` are cited nowhere in v49**, and
they are the only two uncited entries this base created (v48 already carried two: `Baez 2023`,
`Illakwahhi 2024`). v48's §1.1 had two sentences that cited them; the SEEA/consistency-score passage
they rested on is *not* in the deposited article, so this build cannot absorb it honestly — the gate
would report it as invented. So either the two entries go, or those two sentences come back.

---

# Round 6 — the answer you gave: fix the instrument, not the text

You were right on both counts, and the Illakwahhi entry turned out to be the only phantom in the set.

**What changed in the audit's matcher.** The old rule searched for `Lead` within 80 characters of the year
*without crossing a parenthesis*, so `Illakwahhi, Vegi and Srivastava (2024)` — the correct three-author
first mention for that entry — read as an uncited entry, in v48 as well as v49. It is now: an entry counts
as cited when any name it is addressed by sits near its year; a cite is unresolved only when no name in it
addresses any entry of that year. No canonical key is computed at all, because my first attempt at one
invented its own phantoms: it read `GRACE`, `Zenodo` and `Geological Survey` as authors and orphaned
Tapley, Tilton, Ricard, Smith and Wackernagel. Two bugs inside that attempt, both worth writing down:
`et al.` modelled as a connector *between* names rather than a suffix after them, and lower-cased tokens
searched case-sensitively against a capitalised body (`tilton` never matches `Tilton`).

**The classes, kept apart in the data rather than in prose.**

| class | entries | who acts |
|---|---|---|
| uncited already in v42 and v48 | `baez 2023` | the author, at submission |
| uncited by a removal the errata records | `united 2014`, `united 2025` | the author, at submission |
| unexplained, introduced by this base swap | none | the verifier fails the build if this is ever non-empty |
| the matcher's own phantom | `illakwahhi 2024` | nobody — recorded so it is not re-derived |

Class 2 is not available on request: the errata has to name the entry **and** its year **in the same
sentence as** the statement that the cite went. That rule found two of its own bugs while I tested it — it
first matched any entry merely mentioned near the word "uncited", then mis-classified `united 2014`
because it re-parsed a 120-character *display preview* of the entry line, on which the year falls past the
cut in a five-agency author string. The fix was to store the parsed name beside the preview and read the
logic from it. And the assert bit for real: with the window at 14 characters it failed the build on
`united 2014`, which is what caught the brittleness.

**The open item** (`humanize/open_items_v48.md`) states the facts and recommends nothing. It records that
these entries and E4 are one defect seen twice, that restoring v48's §1.1 sentences is *not* a resolution
since those sentences are what E4 objected to, and that the pipeline drafts no substitute. The same wording
correction went into `revision/v48/ERRATA_v48.md`, which previously offered "restore the passage they
supported" as an option.

**One more guard:** every entry the permissive window clears by a name that is *not* its lead is listed in
`cleared_by_a_name_that_is_not_the_lead` with the context it leaned on, so the shadow side of a lenient rule
is visible instead of assumed. It is empty — all 33 entries were cleared by their own lead names — and the
reverse direction (in-text cites with no entry) is empty too.

`FINDINGS: 3`, all real, all disclosed; `*** v49 verified ***`, `FAILURES: none`.

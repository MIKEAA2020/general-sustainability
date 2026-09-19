# Open items on the v48 line

Written by the run that built `paper3_supplementary_package_v8.zip`. Everything under "shipped" is what the
artefact does today; everything under "for the author" is a decision the pipeline was told not to make.

## What shipped, in one paragraph

The draft is the style exemplar; the prose is written from the deposited article (`v42`) and constrained by the
claim ledger. Of the 290 sentences the ruling cleared for verbatim reuse, the splice placed **208**, and the other **82**
ship from the deposit: 33 are sentence fragments the extractor cut at a display, 17 run through a display or a
table, 23 are not verbatim in the document once the ledger's own line filters are applied, 4 were refused because
the next sentence takes its antecedent from the one they would replace, 2 would have retitled a stated
proposition, 2 have no deposit sentence at all, and 1 was refused because the swap would have left a figure
unstated. The counts sum: 208 + 82 = 290, and the gate re-derives each of them from the run log. 18 of the placed sentences were re-set to the
draft's wording after the register pass had touched them, and none was left damaged. 268 sentences were
regenerated from the deposit in the draft's register. Gate: `*** ALL CHECKS PASS ***`.

## Shipped against a recorded recommendation (the author's call to reverse in one line)

The line read and the pointer read recommended regeneration for eight rows. None of them is in
`revision/v48/v48_overrules.csv`, so seven shipped as reused with the defect:

| row | what it costs the text |
| --- | --- |
| D0158 | `each` where the deposit reasons with `every` |
| D0129 | drops the principle that a review cycle closes at the rate of use, not of the calendar |
| D0108 | removes the article's only expansion of `Survey (USGS)`; `USGS` now appears twice unexpanded, and the draft's `US` replaces the deposit's `U.S.` |
| D0309, D0618, D0620 | lose the supplementary locators `S6`, `S2`, `S14`; the draft names the section where the deposit names the file |
| D0530 | loses `recorded in S5` |

The eighth, **D0089**, is *not* in the shipped text: the coherence guard refused it because the deposit's next
sentence — `They are not, and the worked instances of this section make the differences explicit` — answers the
sentence the row would have replaced. That is the outcome the recommendation wanted, reached by a guard rather than
by a ruling, so it is reported as luck rather than counted as a fix.

To make any of these a decision instead of an accident, append the id to `revision/v48/v48_overrules.csv` and run
the two commands at the bottom; the splice will then refuse the row and the deposit's wording stands.

## Register, stated as a cost

Distance to the draft's own flowing-prose profile: deposited article 36.8 units, accepted v47 line 21.8, **v48
28.6**. v48 is nearer the draft than the deposit and further than v47, because v47's extra closeness came from
carrying draft paragraphs whole that the ledger has now sent back. Four features moved *away* from the draft while
the aggregate improved: em-dashes (draft 11.0 per 1k, deposit 7.8, v48 7.5 — the style kit trims dashes to its own
cap), the dash-pair, the `, not Y` frame and parentheses. Nothing was tuned to the metric. Length: the article
prints on 54 pages against v47's 62 and the deposit's 57; flowing prose is 18,429 words against v47's 22,763.

## Bibliography, once more because it is the document's

* The shipped list is the deposited article's own: **39 entries, 8 carrying a DOI**, the `2026a/b/c` year letters
  intact; the gate asserts the whole back matter is byte-identical to the verified line, and the reference block
  entry for entry.
* The draft's list is a PDF text-layer reflow — 21 glued blocks, year letters dropped, the Martinez-Alier entry
  split — and is **not** adopted. Reported, not repaired, per the standing instruction.
* Verified against the publisher record: Martinez-Alier, Munda & O'Neill, *Ecological Economics* 26(3),
  277–286, Sept 1998, `10.1016/S0921-8009(97)00120-1` — the entry as the article states it is correct, and the
  article's list is the one place it carries no DOI while eight others do. House style, the author's call.
* The three 2026 Zenodo DOIs resolve to *The Limits of Compensatory Aggregation*, *Delay-Induced Regime Change in
  Harvested Stocks* and *Periodic Review as Sampled Governance*, which is what pins the `2026a/b/c` letters the
  draft dropped; `10.4230/EPTCS.380.5` is registered **2023**, not 2022.

## Anonymisation held by a guard, not by design

The draft carries four `Author, D., et al., in review` placeholder sentences. None is in the shipped text — zero
occurrences — because the one reuse row that would have brought one in (D0218) was refused by the figure guard. A
later run whose reuse set grows could ship it. If the blind submission needs a guarantee, the sentence should be
rewritten at source rather than rely on that guard. The author's own status wording is preserved: `under review`
appears once, `in review` nowhere.

## Figures that changed appearance and not value

Eight figures are written with a different thousands separator from the deposit because the draft sets them in text
where the deposit keeps them in maths (`240,000` for `240{,}000`): `1000000, 120, 120000, 240000, 250000, 600000,
74000, 74000000`. The gate folds both spellings so they are compared as the same figures; `stylekit_v1.values()`
does **not** fold `{,}` despite its docstring, which is why any invariant spanning the two sources has to fold by
hand. No arithmetic was re-typed to make the two agree, and no reused formula was normalised: the shipped document
contains zero `S^{\top}`, zero `\mathcal{H}` and zero `S_{\mathsf{T}}`, because the 16 notation rows are exactly the
ones the author overruled out of reuse. (The 4 `S^{\top}` in v47 stay as v47 shipped them.)

## Locator asymmetry, systemic

The deposit distinguishes 13 supplementary locators (S2, S2.1, S5, S5.4, S6, S7, S8, S9, S10, S11, S14, S16,
S17); the draft uses 2 (S5, S6). In the shipped article every distinct locator still appears (13 → 13) but
occurrences fell 29 → 28, the loss being the reused rows above. A build-time repair is refused: the draft's
pointer style is a difference of what the two documents *say*, not of typography.

## An artefact I created, stated plainly

An intermediate version of the packaging script still pointed at the previous version's output path, and one run of
it re-emitted `revision/v7/paper3_supplementary_package_v7.zip`. Its own manifest verifies (42 records, all OK) and
the four markdown and four tex files inside it are the unchanged ones; the three companion **PDFs** are fresh
typesettings of that unchanged markdown rather than the bytes the accepted line deposited, and the container hash is
now `18d41c7e90624f2a19a812ce493eb67be1df580554dacc1990e2c2670c1117bf` instead of the recorded
`9b1ddecc653fa89bdf0df93adc22078796e3eade0332d7cabcabc0d5baa9eeea`. The v47 build script and its sources are untouched, so
the archive can be re-derived at any time; if the original deposit bytes matter, recover them from wherever v47 was
deposited outside this workspace. Two consequences for how to read the checks. The v48 paths are now distinct
(`package_v7`, `..._v8.zip`), so nothing v48 runs writes to a v7 output. And because the container was rebuilt from
the working directory, a comparison against it is only as good as that directory: the companion check that matters
is therefore the one against the *sources* the line carries from, which holds byte for byte - `paper3_supplementary
_v14.md`, `companionA_certification_procedure_v5.md`, `companionB_standards_horizon_v5.md` are unchanged, and each
`v18`/`v9` markdown is identical to the source it was copied from (sha256 of the pair, checked in this run).

## Reproduce

```
python3 /home/user/revision/v48/build_v48_base.py      # text, tex, four compiles, note, log     (cwd: revision/v7)
python3 /home/user/revision/v48/verify_v48_base.py     # the gate, including that each reused sentence is verbatim
python3 /home/user/revision/v48/build_v48_package.py   # paper3_supplementary_package_v8.zip, 75 records
```

v8 package, as it now stands after the recovery re-run: 2,202,539 B, sha256
`3ad72c04f57985c8ed53b2d31c05bc889a0449c21ad946e229ead53aa0564fa7` (the earlier build was
`9ab9f073afe8107701cf8f6fdb80e8abf3049ad8d5712900ce33e9d3bc807156` at 2,202,536 B; the two manuscript files inside
differ only because tectonic was run twice, and the rebuild is what matches the workspace).

## Opened after v48 was called finished - 2026-09-19, raised by the author

Three things the author's challenge ("is v48 your gemini adaptation? it reads nothing like it") turned up, all
accepted and all deferred to a v49 that has been planned but **not started**:

* **the style target was the wrong document.** v48's `CORPUS_MD` is `humanized/v1/paper3_humanized_v1_full.md`, my
  plain-language rendering, not `uploads/p3 humanized.txt` (the adaptation, whose first line is the marker
  `gemini:`). Measured: 3.0% of v48's 930 sentences verbatim in the adaptation against 12.6% verbatim in the
  deposit; §1.1 difflib 0.084 to the adaptation, 0.437 to the deposit; 32.9 words a sentence against the
  adaptation's 21.1. `review/joint_evaluation_v1.md` §6 had already agreed a merge plan - deposit as authority, the
  adaptation for voice, `humanize/style_audit.py`'s ≤22-word programme - and it was never executed; v47 reached
  21.8 on the register distance and the splice pushed v48 back to 28.6.
* **a paragraph was lost in the exempt region.** "The first failure mode has a public flagship object. Earth
  Overshoot Day aggregates component flows into a single calendar date…" is at `work/paper3.txt:59` and
  `revision/v7/paper3_material_ledgers_v42.md:27`; "overshoot day" has **0** hits in
  `revision/v7/paper3_material_ledgers_v48.md`. `verify_v48_base.py` has no front-matter check (0 hits for `front`),
  which is why nothing flagged it. The adaptation's two-level "Arithmetic Level / Yield Inflation" framing likewise
  never entered this line (0 hits in v42 and v48).
* **a markdown artifact reached print.** Page 2 of the v48 PDF reads "The drift is concrete. - A **reserve-life
  ratio** divides…" - a stray list marker and an orphan bold from `build_v48_base.py`'s hand-written `FRONT` text
  losing its line breaks; v42's line 23 was clean prose.

The author's rulings on both: v49 takes the **adaptation as the base document**, repaired against the deposit, and the
290-sentence verbatim ruling is **waived for the front matter only** - the exact number being **63** of the 68 reuse
rows in §1, since 5 of those were never placed and so hold no protection to lift (`revision/v49/waiver_scope_v1.json`).

**Four further v48 items surfaced while building the waiver's guardrails**, all in the exempt front matter, all
disclosed here because none of them is v49-only:

* the §1 passage on the **2008 SNA revision, SEEA 2014 and "(United Nations, 2014)" is not in the deposit** -
  `2008` dep 0 / v48 1, `United Nations` dep 0 / v48 4, `SEEA` dep 0 / v48 2 - it entered through the upgrades line,
  and v48's 40-entry reference list carries **no 2008 entry** for the year the sentence asserts. Either the citation
  is added to the list or the sentence is trimmed to what the deposit supports;
* two section pointers, **§2.3 and §6.5.4**, present in v42's front matter, are **gone from v48's**;
* the hand-written rewrite moved the phosphate figures out of math mode - `$1{,}000{,}000$` and
  `$6.0\times10^5$` became prose digits - which is build-time normalisation of deposited mathematics inside the one
  region that was exempt from the rule against it;
* and `incidence` 5 → 3, `support pool` 4 → 3 in the same rewrite: not errors, but term dilution in the region no
  check was watching.

All four are what `revision/v49/v49_waiver_gate_v1.py` reports on the v42 → v48 pair - now **7 blocking flags and 2
disclosures**, `revision/v49/waiver_gate_controls.json`, after the gate grew G4/G5 and a coinage-derived vocabulary
check; the extra flag is **E2, the lost term "aggregation obstruction"** (`work/paper3.txt:70`, v47 1 hit, v48 0),
which the hand-written registry had missed. All seven are written up for the delivered line in
**`revision/v48/ERRATA_v48.md`**, which also marks E4 as inherited from v47 rather than introduced by v48, and says
that of the seven only E4 touches substance. The gate design, the pinned row lists and the reconciliation are
in `humanize/v49_adaptation_first_brief.md`. Plan, id lists, repair list and the two new gate checks: `humanize/v49_adaptation_first_brief.md`. Work
held pending the author's next prompt.


**v49 (2026-09-19).** The line the open items were written for is now closed by a build: v49 restores E1–E9
(the six body sentences found by the 32-row read are E8, the mangled two-senses passage is E9) and ships with
`revision/v49/NOTES_v49.md` and `ERRATA_v48.md` inside it. v48's own bytes were not touched — the zip is still
sha256 3ad72c04…564fa7 — because the decision was that no v8.1 patch ships unless v48 ships alone.
Open for the author in v49: the four status labels (a content call, disclosed not absorbed), the two `watch`
terms kept as the adaptation wrote them, and the small duplication where the two-senses carry-over landed.

---

## Open item — three uncited reference entries, one of them a matcher's fault (recorded 2026-09-19, v49)

**The facts.** v49's reference list carries three entries with no in-text cite anywhere in the article:
`United Nations, 2014` and `United Nations, 2025`, whose only citations in v48 were the two §1.1 sentences
on the SEEA consistency-score passage, and `Baez 2023`, uncited since v42.

**The two UN entries and erratum E4 are the same defect, seen twice** — once in the body, once in the
list. E4 recorded that the §1.1 passage asserted `2008 SNA` / `SEEA 2014` / `(United Nations, 2014)` with
nothing in the deposit behind it (`2008` dep 0, `United Nations` dep 0 / v48 4, `SEEA` dep 0 / v48 2).
v49's base does not carry that passage, so the unsupported assertion is gone from the body and the entries
it supported are left dangling. They should not be treated as two separate items.

**`Illakwahhi 2024` is not an orphan.** It is cited as `Illakwahhi, Vegi and Srivastava (2024)`, the
correct three-author first-mention form for that entry. An earlier version of the line audit required the
year immediately after the surname and would not cross a parenthesis, so it reported this entry as
uncited; that was a matcher bug, it has been fixed in the matcher, and the citation was left alone. The
audit now records such cases apart from real orphans (`phantoms_the_old_matcher_invented_and_this_one_clears`)
so nobody re-derives the same conclusion. Editing the citation to satisfy the old matcher would have been
editing correct text to appease a broken instrument.

**Status: no pipeline action, no recommendation.** Which way these three go depends on whether the SEEA
inconsistency is a claim this paper is to make, and that is not the pipeline's judgement. If it is, the
fix is a new sentence with a verified source, written by the author. If it is not, the entries are dead
weight. Restoring v48's two §1.1 sentences is *not* a resolution — those sentences are exactly what E4
objected to — and the pipeline will not draft replacements for them. Disclose specifically, settle at
submission. What the build guarantees meanwhile: the audit separates "inherited from an earlier line" from
"lost with no record", and the verifier fails the build if that third class is ever non-empty.

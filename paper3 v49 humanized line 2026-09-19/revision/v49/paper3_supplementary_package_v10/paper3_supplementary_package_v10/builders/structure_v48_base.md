# The v48 line: the draft as the exemplar, the prose written from the deposited article

Emitted by `build_v48_base.py` from the log that run wrote, so every figure here is the one that build
measured. v47 took the humanized draft as the document and supplied from this paper where the draft had been
overtaken. v48 keeps the same goal - the author’s own prose, not a style approximation of it - and
replaces the method: nothing is carried from the draft because a whole paragraph reads the same. What is
carried is decided one sentence at a time by a claim ledger the author adjudicated, and everything else is
written from the deposited article in the draft’s register.

## What the pass may touch

* the claim ledger (`v48/claim_ledger_v1.py`, 558 sentences extracted from the draft, 0 skipped, 0 with no
  verdict) pairs each sentence that asserts a fact, claim, hedge, scope or attribution with the proposition
  of the deposited article it rests on, and marks it supported, drifted, contradicted or not stated; the
  author’s ruling then decides the partition, and the pipeline does not;
* 290 sentences cleared for verbatim reuse - 260 supported at high or certain match, 30 signposting - are put into the text as the draft wrote them, and
* 268 were regenerated from the deposit in the draft’s register: 188 where the match
  was medium or low, 64 where the line-by-line read flagged a value, attribution or scope problem, and
16 the author marked for regeneration over a notation defect;
* 0 of the 290 cleared sentences were placed in the article, 290 could not be
  placed - 0 are halves of sentences the extractor cut at a display, 0 run
  through a display or table, 0 are not in the document verbatim once the ledger’s
  line filters are applied - and an unplaced row ships from the deposited article, which is the direction the
  ruling asks for; 0 inserted sentences the register pass had rewritten were set back to the
  draft’s wording after the pass, and 0 could not be found again;
* the rest of the flowing prose is styled by the rules obtained by aligning the draft against the PDF it was
  made from (`stylekit_v1.py`, the GEM_* tables), a block at a time, and only where the values are untouched
  and the linter finds nothing new in the result.

## What the reuse was checked against, and what was found

* the ledger was self-tested by planting 21 defects into the deposited text; it caught 4 of 8 value
  changes, 2 of 3 strengths, 1 of 3 causalities, 1 of 3 attributions, and 0 of 4 scope hedges, so
  `supported` means the instruments could see the claim and no disagreement was found, and the
  `scope` finding is reported as a weakness of the instrument, not a pass;
* 290 reused sentences were read line by line against the passage of the deposit each was paired with:
  10 flagged, 296 clean, and a self-test on 6 planted defects caught 6;
* 79 reused rows point at something - 96 of the passages they restate are cited by the deposit in the
  aligned block, 4 are cited on the draft’s own authority and all 4 resolve to an object that exists and
  is right, and none points at an object that does not exist;
* 16 rows carried the article’s notation where the deposit’s identity does not hold in it (`A^\top`,
  `\mathcal{H}`, `\mathsf{T}`); the author overruled them out of reuse, so `v48_reuse_split.json` reads
  290/268 instead of the 306/252 the classifier produced;
* eight rows carry a defect that the line read or the pointer read found and recommended for regeneration, and none of the eight is in the author’s overrule file. 7 of them were placed by the splice and so ship reused against that recorded recommendation: D0158 (`each` where the deposit reasons with `every`); D0129 (the principle that a review cycle closes at the rate of use, not of the calendar); D0108 (the deposit’s only definition of `Survey (USGS)`, and its `U.S.` spelling); D0309 (the locator `S6` the deposit carries); D0530 (the phrase `recorded in S5`); D0618 (the locators `S2` and `S14`); D0620 (the same two locators in the next sentence). The other 1 - D0089 - were not placed at all: the splice refused them for a reason of its own (the sentence after the one it would replace takes its antecedent from it), so the deposited wording stands in their place. That is the outcome the recommendation wanted, arrived at by a guard rather than by a ruling, and it is stated as such rather than counted as a fix.

## What it may not

* no table cell, no displayed equation, no statement heading, no numbered list item: they pass through
  byte for byte, and the splice locates sentences only inside flowing prose - it refuses a row whose
  deposit sentence runs through a display, because a splice there would move structure, not a sentence;
* no heading text, so the section numbering and the article labels the supplementary cites survive;
* not the front matter and not the back matter. The reference list, the availability statements and the
  declarations belong to the document: the article’s own list is carried untouched and the draft’s
  reflowed list is not adopted, which is why the draft’s 21-entry blob, its missing `2026a/b/c` year
  letters and its split Martinez-Alier entry are reported and not repaired. Where the draft’s version is
  intended the author marks it in `v48_overrules.csv`, and that is the only input the pass reads for a
  move. In-text self-reference is part of the document, so the citation-status wording and the
  article-names-itself map are applied after the splice, to reused text as well.
* not the three companion documents, carried byte for byte from the v43 line: the draft is a humanization
  of the main text alone, so there is no draft wording for them to adopt;
* no arithmetic is re-typed by the pipeline. Where the draft writes a figure in text and the deposit keeps it
  inside maths, the swap leaves 8 figures written with another separator style   (`240,000` for `$240{,}000$`), and the gate compares folded keys so that is counted as the same figure.
  The same refusal is why the reused prose carries `$S^{\top}$` and `$\mathcal{H}$` where the deposit writes
  `$S_{\perp}$` and `\mathsf{H}`: the draft’s symbols are its typography, not a claim. Four instances in
  v47 stand unrepaired for the same reason; v48 reports them in `v48_notation_drift_v1.py` instead of
  silently normalising the author’s sentences.
* 2 draft paragraphs were refused by the earlier block-level test and no longer apply; the
  sentence-level test above is what governs;
* and no swap survives whose own value multiset differs from the sentence it replaced. That test decides
  each edit, and the document-wide equality of values, of table rows and of displays is the assertion.

## What the shipped reference list is, and what the draft’s list would have cost

The list is the deposited article’s own: 39 entries, 8 of them carrying a DOI, and the year letters that separate this author’s 2026 papers (`2026a/b/c`) intact; the gate asserts the whole back matter is byte-identical to the verified line. The draft’s list is a PDF text-layer reflow in which these 39 works survive as 21 glued blocks with the year letters dropped, so it is reported, not adopted. Two consequences belong to the author rather than to the pipeline. The list carries no DOI for Martinez-Alier, Munda and O’Neill (*Ecological Economics* 26(3), 277–286, 1998; `10.1016/S0921-8009(97)00120-1`, read back from the publisher’s record), where eight other entries do; and the draft’s four `Author, D., et al., in review` placeholder sentences did not reach the shipped text, because the one reuse row that would have carried one (D0218) was refused by the figure guard: the anonymisation a blind submission needs is intact here by a guard rather than by design, and a run whose reuse set grows could ship it. The same guard is why `in review` appears nowhere in the shipped file and the author’s own `under review` is the single status sentence.

## Measured on both sides

| quantity | before | after |
| --- | --- | --- |
| flowing-prose words | 20,911 | 19,990 |
| sentences of flowing prose | 818 | 831 |
| mean sentence length (words) | 27.0 | 25.4 |
| p90 sentence length | 56.0 | 54.0 |
| longest sentence | 231.0 | 231.0 |
| sentences over 60 words | 60 | 55 |
| em-dashes | 143 | 140 |
| semicolons | 215 | 193 |
| ", not Y" frames | 58 | 65 |
| "we" and "our" per 1k words | 0.3 | 0.3 |
| self-reference by "the article" | 37 | 5 |

The register is judged as the distance to the draft’s own profile, per 1000 words of flowing prose,
feature by feature and in aggregate, and the gate refuses the build unless that distance fell. Where the
audit instrument’s numeric target contradicts the draft, the draft governs and the gate names the
conflict instead of satisfying the cap; on this text the line is the semicolons, and the sentence-length
maximum, which the article’s theorem statements set at 231 words against the draft’s 153 because
the draft is anonymised and carries neither abstract nor statements.

## How the LaTeX is made

The four documents are typeset from their markdown, each by the converter the deposit has always used;
the article’s LaTeX carries 1431 formulas lifted out of the markdown before
conversion and put back unchanged after it, 3 piece(s) were fitted to the measure by scaling or narrowing (display scaled to the measure at line 628, 173.1pt, display scaled to the measure at line 574, 36.3pt, display scaled to the measure at line 542, 69.5pt), and
the gate reads the compiled text back and requires every flowing paragraph of the markdown to be in it.

## Reproduce

```
python3 /home/user/revision/v48/build_v48_base.py     # text, tex, the four compiles, this note, the log
python3 /home/user/revision/v48/verify_v48_base.py    # every check, including that each reused sentence is verbatim
python3 /home/user/revision/v48/build_v48_package.py  # the package and its manifest
```

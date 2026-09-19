# v44 — the humanized line: what changed after "v43 reads nothing like gemini's"

## Why a new line rather than another pass

The v43 deliverable satisfied the instrument and was rejected on reading. Measuring that rejection
(`verify_v44_hum.py` group [0], `/tmp/al2.py`) located the cause exactly: the corpus-alignment of the
article *fell* under v43.

| md | prose sentences | verbatim in the corpus | verbatim or near |
|---|---|---|---|
| v42 (the author's line) | 703 | 119 (17 %) | 227 (32 %) |
| v43 (mechanical breath cuts) | 987 | 104 (11 %) | 217 (22 %) |
| **v44 (corpus adoption)** | 956 | **180 (19 %)** | **249** |

v43's surgery split 910 sentences into 1183 with no corpus content, and splitting a sentence is the
surest way to stop it matching a corpus sentence verbatim. So v44 was built from **v42's md**, and the
style improvement is done by *putting the corpus's own wording in* rather than by re-cutting the author's
syntax. The v43 register work is kept only for the three companion documents, which v44 carries verbatim
(`paper3_supplementary_v15` = `paper3_supplementary_v14`, `companionA…_v6` = `…_v5`, `companionB…_v6` =
`…_v5`), because `humanized/v1/*` is a humanization of the main text alone — there is no corpus wording to
adopt for a supplementary note, and the measurement showed a companion-only punctuation pass buying nothing
and costing two PDF metrics.

## `stylekit.humpass(text, corpus, kind, keep, ratio=.84, para_ratio=.74, maxw=34, log)`

1. **Paragraph adoption** (`humanized_paragraphs`, `adopt_paragraphs`): a v42 prose block is replaced by the
   corpus paragraph when similarity ≥ 0.74 **and** the guards below agree. This is what moves whole passages
   onto the corpus's cadence: *"The first failure mode has a public flagship object."* →
   *"This first failure has a well-known public object."*
2. **Sentence adoption** (`humanized_sentences`, `adopt`): with no paragraph twin, each sentence is replaced by
   its closest corpus sentence at ≥ 0.84. 67 of the article's 696 prose sentences qualify.
3. **Breath, only where the corpus is silent** — the `breathe`/`semicolons` cut, the `we are able to`→`we can`
   class of `voice` rules and the `consider/suppose` insertion run on the blocks the adoption did **not**
   touch; `maxw` 34. The `touched` index set is what protects adopted wording from being re-cut.
4. **Value and lint guards** (`adopt._numbers/_status/_maths/_refs`, `_head`): adoption is refused unless the
   numeric multiset, the status words (only/almost/less/exact/even/just/too/**not**), the bare numbers and
   operators, the `S§` references and the sentence's opening referent all agree — so "It has two senses"
   cannot become "The illusion has two senses", and "dynamic form" cannot become "a moving form". A block that
   afterwards differs in any value, or that gains a lint finding it did not have, is reverted whole.
5. **Self-reference is settled last, on every block**, with `$…$` and `$$…$$` masked out so no formula is
   touched: 30 occurrences in editable prose in v42 → 5 now (the residue sits in lines that carry a display,
   where a word swap would have to distinguish a delimiter from an apostrophe).
6. Nothing runs inside a heading, a `**Theorem N (…)**`-style label line, a table row, a list item or a `$$`
   display. Two bugs from the first v44 build were exactly this class: the block-level whitespace collapse
   swallowed a `## 7.` heading that followed a proof, and `refill` re-wrapped an `S9.4` table. Both stages
   now skip any block whose later lines, or whose first line, are structural.

## What the gate now proves that earlier gates did not

* group [0]: `align()` — the article's verbatim-corpus **count** must exceed the parent's by ≥ 40 and its
  **share** must not fall; both hold for v44 (119→180, 17 %→19 %), and v43 would have failed it.
* group [1]: the four documents reverse to their v42 parents **word for word** by undoing the logged edits
  (216 logged article edits), so every change is attributable and none is a rewrite of content.
* the lint comparison exempts a finding inside an adopted paragraph, since the corpus's own prose enumerates
  "(1). … (2). …"; and `lint` no longer reports `et al.,` as a stop stack, which is the journal's citation
  style and was firing ~40 times per document.
* group [3]: the instrument's own lines — semicolons 1.3/1k, `—…—` 9/1k, `this article`/`the article` in
  body prose, no `et al. …`, no "In this paper, we", no first-person `S§` references — all met; em-dash
  interrupters 203 → 59; `we`+`our` 3 → 35 per 1k.

## What did not change

Every verified number, statement label and title, status sentence, S-list table, display, attribution and
caveat; page counts and PDF geometry are re-measured (57 / 19 / 10 / 8 pages, 0 Overfull, 0.0 pt overhang).
`FRAMES_SPLIT` remains off: the "X, not Y" → "X. It is not Y." rule is grammatical only when the tail is a
noun phrase, and that is not decidable safely in a regex — so the frame count is reported (article 34 → 25,
supp 15 → 17 because of an `instead of` substitution that created a new frame in v43's file, which is carried)
rather than forced down by a rule that can produce a fragment. Counted on the flowing prose: the article goes
from 56 frames to 35. For the three carried documents the gate's `no style metric is worse than v42` assertion
covers the frame count on both the prose and the flow surface, and it passes; the earlier v44 attempt to give
them their own pass is what produced a 15 → 17 frame movement and a p90 rise, and that attempt was dropped in
favour of carrying the v43 files, which are byte-identical to what the v44 line ships.

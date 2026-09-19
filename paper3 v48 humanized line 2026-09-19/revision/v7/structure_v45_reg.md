# v45 — the register measured as distance to the draft, not as my own thresholds

## What was wrong with the criterion, not just the result

v43 was rejected because it read nothing like the humanized draft. v44 answered that by adopting the draft's
sentences, and measured success as *overlap*: 174 of the article's prose sentences verbatim, 247 verbatim or
near. That is the right thing to preserve and the wrong thing to aim at, because it can only ever reach the
fraction of the text where the draft and this paper say the same thing. What was never measured was whether the
rest **moves the way the draft moves**. So v45 measures the register itself.

`verify_v45_reg.py` group [0b] profiles flowing prose (maths stripped, one extractor used for both texts, since
comparing md against a PDF is how an earlier round of this work invented a nominalisation gap that was not
there) and asserts the *distance to the draft's profile*, per feature and in aggregate:

| per 1k words of flowing prose | draft | v42 | **v45** |
|---|---|---|---|
| mean words/sentence | 19.1 | 25.0 | 20.4 |
| p90 words/sentence | 37 | 50 | **37** |
| `the X of the Y` chains | 0.7 | 1.3 | 1.0 |
| em-dashes | 11.0 | 7.8 | 8.9 |
| colons | 10.2 | 12.1 | 9.9 |
| semicolons | 9.3 | 11.5 | 10.0 |
| `-tion/-ment/-ness/-ity` | 64.3 | 71.0 | 70.0 |
| sentences opening "This" | 1.3 | 0.7 | 1.2 |
| `we`/`our`/`us` | 0.4 | 0.2 | 0.9 |
| **aggregate distance** | — | 36.8 | **15.3** |

Aggregate distance is asserted to fall; the five features that define the register (mean, p90, chains,
em-dashes, colons) are asserted not to move away from the draft. Three features are reported and not forced:
`we` at 0.9 (12 sentences, every one of them the author's own or the draft's own — "We separate the two failures
with a typed stock–flow accounting layer", "what we deliver, then, is a grammar" — and stripping them to hit a
rate would be silencing the author, which is the same mistake in the opposite direction), the interrupter-pair
count, and `paren`, where the draft has more parentheses than either version of this paper.

## Where the rules come from

`uploads/paper3_material_ledgers_v32.pdf` is the pre-humanization source of `humanized/v1/paper3_humanized_v1_full.md`.
Aligning them sentence by sentence (924 pairs at ratio ≥ 0.55) and diffing the words gives the humanizer's own
edits, and those are encoded in `stylekit_v1.py`:

* `GEM_DROP` — the padding the draft does not contain. `in order to`, `for the purposes of`, `the fact that`,
  `it should be noted that`, `Note that`, `is able to`, `makes it possible for`, `gives rise to`, `utilize`,
  `subsequent to`, `thereby`, `herein`, plus the attested plain-verb swaps (`summed`→`added`,
  `remained`→`stayed`, `regenerates`→`regrows`, `maintained`→`held`, `since`→`because` with a date look-ahead
  so "since 1961" cannot become "because 1961").
* `denom()` — two shells only: `is a restatement of` → `restates`, `the certification of X takes n steps` →
  `certifying X takes n steps`. The paper's terms of art (depletion, conservation, compartment, incidence,
  statement, proposition) are nouns because they name objects in the theory; a pass that turned
  "conservation law" into a verb would be changing the content, so it is out of the tables.
* `chain()` — `the classification of the pool` → `the pool's classification`, capped at 90 per document,
  never applied to a name ("the ledger of record").
* `dashjoin()` — the draft's colon rate is below its source's and its em-dash rate above, so a trailing gloss
  or list after a colon runs on a dash instead. **Budget 35 per document**, sized from the two rates, because
  a per-paragraph cap let the pass spend 75 colons where the profile asked for about 35; `reset_budget()`
  in `humpass` is where that number is set.
* `semis_in()` — the draft joins two balanced clauses with a semicolon ("services are readouts; conservation is
  a law"), and the breath cut was spending them, so they are given back where both halves are real clauses.
* `GEM_FRAME` + `frame_rejoin()` — the `, not Y` frame is the draft's signature (77 of them). `rather than` /
  `instead of` fold into the frame, and a breath cut that left "Not a forecast." standing as a sentence is put
  back into the sentence it came from — only when the tail has no verb, so "Not every ledger admits this." stays
  a sentence.
* `GEM_AGENT` — the draft is near-impersonal (6 `we`, one `our` in 23,000 words): the ledger, the certificate,
  the account and the section do the showing. `voice()` used to answer self-reference with "we show"; it now
  keeps the author's verb and changes only the subject (`This article shows` → `The account shows`), and
  `strip`ping the author's own first person is not part of the plan.

## Two things that had to stop

`breathe` may not cut at a colon whose gloss begins lowercase, nor inside an em-dash pair, nor before a
`not …` tail: those three cuts are what destroyed the draft's own devices while the length numbers looked good.
And `asides()` — moving parentheticals onto dashes — is switched off (`do_asides=False`): the measurement that
said the humanizer unpacked parentheses came from comparing a PDF against markdown. The audit's cap of 60
em-dashes, its 120-semicolon cap and its frame target sit on the other side of the draft's own rates, so those
three lines are exempted in group [3] **by name**, with the draft's number printed next to them and the corpus
distance asserted in [0b] instead; nothing there is a tolerance.

## What did not move

61 statement labels and their headings, 70 table rows, 79 displayed equations, 74 heading lines, every numeric
value, the cross-reference set, the data-vintage years, the two NFA edition tables, S9.4's 27 article loci.
The 205 logged edits reverse to `paper3_material_ledgers_v42.md` word for word. All four documents recompile at
0 Overfull and 0.0 pt overhang, 57 / 19 / 10 / 8 pages, and the three companion documents are the v43 register
line carried byte for byte, because the draft is a humanization of the main text alone.

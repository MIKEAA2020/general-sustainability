# The v43 line: register only

v42 is the content line. v43 rewrites punctuation and voice in the same four documents and moves nothing else.
It exists because the v42 sources did not read the way the humanized draft reads: sentence lengths in the 60 to
80 word range, em-dashes in the tens, no agent in most sentences, "the article" where the authors are speaking.

## What the pass is

`stylekit_v1.py` holds the instrument, `build_v43_style.py` runs it over the four markdown sources, then rebuilds
the LaTeX and the PDFs with the geometry machinery unchanged (`texkit_v1`, `tablekit_v2`,
`build_supp_tex_v1`, `build_companions_v1`). Three kinds of edit:

* **Hand-written spans**, in `FRONT`, located by a start and end anchor that must each occur exactly once. The
  abstract, the §1.1 metrological paragraph, the §1 closers and the supplementary's lead. These carry the
  author's own sentence, including `Depletion indicators can carry similar units while built to inform distinct
  questions.`, and the connective sentences between the failure statement and the accounting layer.
* **Section leads**, in `LEADS`: one sentence at the head of each section, in the authors' voice ("We define the
  ledger here: compartments, fluxes, and the typing that keeps them apart."), because the register the humanized
  draft uses names an agent at the point where work is being done.
* **A mechanical pass** over the flowing prose: sentences cut to one breath (`breathe`, `semicolons`, `dashes`),
  impersonal self-reference turned into "we" in the article and into "the main text" in the three companions
  (`voice`), hypothetical framings kept plain (`hypotheses`), and two global budgets for em-dashes and contrast
  frames. It ends with a grammar repair (`unbreak`, `glue_fragments`, `lint_fix`) and a linter (`lint`).

## What the pass may not touch

This is the part that took the work. A block is left exactly as v42 wrote it if it

* contains a display equation, or is a statement line (`**Definition 45 (…)**`), or is a table row, a fenced
  block, a list item, or back matter from `## References` onwards;
* contains one of the phrases in `KEEP`, which are the sentences whose wording the author fixed;
* would leave with a different multiset of numeric values, or with a grammar fault the source did not already
  have. Both checks are inside `polish`, per rewritten unit *and* per finished block, so the pass reverts itself.

The contrast-frame rewrite (`"X, not Y"` into two sentences) is switched off: it is grammatical only when the
tail is a noun phrase the clause can stand without, and deciding that mechanically produced fragments such as
"It is not as a projectable reduction." The frame count is reported as measured instead of forced down.

## Measured, on the flowing prose of the sources (math excluded) and on the PDFs

| document | mean words/sentence v42 → v43 | p90 | PDF mean | em-dashes | frames |
|---|---|---|---|---|---|
| article | 31.6 → **21.5** | 64 → **41** | 28.9 → **20.6** | 190 → **63** | 58 → 48 |
| supplementary | 36.5 → **24.6** | 70 → **48** | 28.3 → **21.6** | 33 → **2** | 15 → 12 |
| companion A | 44.3 → **31.6** | 75 → **66** | 29.0 → **26.3** | 17 → **14** | 10 → 9 |
| companion B | 32.9 → **29.4** | 60 → **52** | 23.9 → **22.2** | 22 → **20** | 13 → 13 |

Targets are met outright for the article's prose mean (≤ 22) and for every punctuation and self-reference target
in all four: semicolons, "rather than", "the article", and for the companions on the PDF surface. What is not
met: the p90 ≤ 40 and mean ≤ 22 for the supplementary and the two companions (their prose is protocol steps and
formula-dense derivation, which the pass is not permitted to enter), the example-marker and
"consider/suppose" floors in A, and the "we" rate of 2.0 per 1k words in the article. On that last metric the
honest position is this: impersonal self-reference in the article's prose was converted everywhere it occurred
(25 sites of the "is proved in Section", "is defined in", "this section records", "the present work" family were
converted, and "the article" fell from 40 occurrences in 38 lines to 9, the survivors sitting in statement lines,
a table and the reference list, which the pass may not enter), and each of the eleven sections was given a lead sentence in the
authors' voice. The count of "we" and "our" in the article went from 3 to 24, which is 0.7 per 1k words against
the instrument's 2.0, and below the 40 to 60 the protocol names for a paper of this length. The remaining
distance can only be closed by writing more sentences that say what the authors did, section by section; that
is an editorial act rather than a mechanical one, so it is left for the author to direct, and the count was not
padded to reach a number -- the corpus README forbids exactly that.

## Invariance, and how to re-check it

`verify_v43_style.py` prints, for all four documents: that reversing the logged edits returns the v42 file word
for word; that the multiset of numeric values, the ordered statement labels with their headings, the table rows,
the displayed equations, the heading lines and the LaTeX cross-reference set are unchanged; that no style metric
is worse than v42 on any of the three surfaces; that the linter finds no fault the source did not already have;
and that each PDF recompiles with `rc=0`, `0` Overfull `\hbox`, `0.0 pt` overhang and the same page count, with
S9.4 still bijecting with the article's labels 21 to 47. Last run: `ALL CHECKS PASS`.

## Two things for the author, both pre-existing

1. **`paper3_supplementary_v14.md` (and v13) has a broken sentence** in the data-availability paragraph:
   "…carries `source/MANIFEST.md` with the two retrieval commands and the hashes that settle what was read.
   **edition is free** but registration-gated, so the 2022 row quoted in the main text's Remark 33 is not
   reproducible from an open download…". A subject is missing after "read." — v42 read "The FT/FAOSTAT" there and
   the words were lost in an earlier rebuild. Suggested repair: "…what was read. The 2018 edition is free but
   registration-gated…". This is content, not style, so the register pass left it, and the gate reports it as a
   finding the source already had.
2. The article's source has about a hundred lines the linter flags as "lowercase after a full stop" inside
   numbered enumerations ("1. like with like: every identification pairs compartment …"). Those are the author's
   own item style, and the linter now excludes `N.` and `a.` markers and abbreviations; what remains is the
   lowercase start *within* an item, which is a house-style choice rather than an error.

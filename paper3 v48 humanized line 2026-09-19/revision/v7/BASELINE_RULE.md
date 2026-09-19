# The baseline rule for the v47 line, and for v48

Written so that the stance is committed once, in a file the build reads, instead of being re-derived at every seam.
Every oscillation in this project - v47 restoring the superseded article's 40-entry reference list, then recutting
the draft's reflowed reference paragraph into entries, then refusing the back matter altogether - came from the
same absence: no top-level rule, so each seam negotiated its own baseline and the conservative default (keep the
deposit's sentence, because it carries the verified facts) won each time. This file is the rule. It states what is
settled, what is measured, and the one question that is still the author's.

## Settled

1. **Back matter is not prose, and no pass may hold it or lose it.** The reference list, the availability
   statements and the declarations ship as the document arrived with them, entry for entry. The graft is refused
   there, as it is refused on headings, table rows, labelled statements and the front matter. The self-reference
   map stops at the first back-matter heading: it had reached into a reference annotation and turned
   `submitted with this article` into `submitted with this paper`, which is the author's wording, not the pass's.
2. **A defect in the baseline is reported, not repaired.** No stage of this build exists to fix citations, complete
   a reference list, recover year letters, or un-glue words that a PDF text layer mangled. If a pass could be
   written that would make a defect disappear, the answer is the open-items list, not the pass.
3. **The draft's prose is the register baseline.** Not its punctuation counts, not its reference list, not the
   length of its paragraphs where the paper has more to say. Where the draft is silent, the paper's own text is
   not a failure of the method; it is the method running out of exemplar.

## Measured, so that nobody re-litigates these with a plausible-sounding rule

- **The register distance metric has a floor of about 19.5 units.** Distance is the sum of twelve absolute
  differences in profile rates over flowing prose, and the draft's own first half measured against its own second
  half gives 19.5. v47 sits at 21.8, and v47's draft-verbatim paragraphs alone sit at 20.9. So: a clause
  demanding `distance <= 5` would fail the draft against itself, and adopting a further 100% of the draft would
  move this instrument by about one unit. **Distance is evidence that the pass moved toward the draft; it is not
  evidence that the register was reached.** The honest objective is the share of body words the draft supplies
  (v47: 33% of 22,448), plus what the ledger says about facts and claims.
- **The draft invents no values.** It states 229; the deposit states 301. Of the 28 values the draft has and the
  deposit's markdown lacks, all 28 are reflow artifacts - digit runs split out of DOIs and URLs - and 0 fail to
  appear in the deposit's PDF. The worry that a humanized draft manufactures numbers does not survive checking
  here.
- **The draft loses 100 values the deposit states**, and 15 of its 40 works: `Ahuja 1993`, `Baez 2023`,
  `Gale 1957`, `Jadbabaie 2004`, `Prajna 2004`, `Prajna 2007`, `Smith 1995`, two UN/World Bank documents, and
  others. A wholesale policy is therefore a decision to shorten the paper, not a decision to polish it: shipping
  the draft's body as the whole body costs about 14,300 words of body prose on the >40-word measure, 15,253 words
  on the whole body, which is 67% of the body.
- **Only 5% of the retained paragraphs are near-duplicates of a draft paragraph** (7 of 124 paragraphs over 25
  words are at least 80% identical to one). So the retained two-thirds of the body really is the deposit's prose,
  not the draft's prose slightly varied. Anyone claiming the graft has already transferred the register has
  counted paragraphs instead of words.
- **Where wording is shared, nothing drifts.** Of the 67 body paragraphs whose text the draft and the deposit
  share outright, 0 differ in any hedge, quantifier or scope marker count. Adoption by verbatim substitution is
  the safe direction; the accuracy risk lives entirely in the parts the draft does not contain.
- **The list that shipped is clean, and was checked at the registry.** All eight DOI-bearing entries in the
  article's reference list match their DataCite/Crossref registrations on year and title, including
  `Baez, 2023` / `10.4204/EPTCS.380.5` (registered 2023, listed 2023) and the three 2026 Zenodo records whose
  titles fix the `2026a` / `2026b` / `2026c` letters the draft's reflow dropped. And the draft's list contains no
  work the article's list lacks: its apparent `O'Neill, 1998` is the reflow splitting
  `Martinez-Alier, J., Munda, G., O'Neill, J., 1998.` mid-author-list. Nothing from the draft's bibliography is
  merited and missing, so nothing was implemented.
- **Eleven works are listed and not cited** by the article's own prose (`Groot 2003`, `Shellenberger 2013`,
  `Wackernagel 2018`, `Weisz 2011`, `Patterson 2023`, and six report-shaped entries). That is an author's
  editorial question - the draft may have dropped some of them for exactly this reason - and it is on the open
  items list, not in a pass.

## Open: the one question the author answers

`v48` starts from the draft file. Which of these the draft is, decides the paper's length and its coverage, and
the pipeline will not guess it again:

| stance | what the body becomes | what it costs | what the gate then measures |
|---|---|---|---|
| completed draft | the draft's paragraphs wherever the draft speaks, the paper's own where it is silent (v47's shape) | 33% of body words are the draft's | draft-word share, value coverage, claim coverage, dangling citations reported |
| draft is the document | the draft's body, with the deposit's 100 values ported into draft sentences and every gap disclosed | about 15,253 words of body prose; 15 works; the paper shrinks toward 19,061 body words | share of body sentences that are the draft's (approaches 100% on covered ground), value coverage vs the deposit, no repair stages |
| rewrite against the exemplar | fresh prose for the whole body, generated to the draft's profile from the deposit's propositions, ledger-constrained | the verbatim share falls; register uniformity is bought with new sentences | ledger coverage of facts *and* of claims with their hedges, plus the profile comparison reported rather than demanded |

Until that answer arrives, nothing in `build_v47_gbase.py` changes: v47 stands, gate green, package verified from a
fresh unpack.

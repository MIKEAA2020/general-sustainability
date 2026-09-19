# The v47 line: the humanized draft as the surface of record

Emitted by `builders/build_v47_base.py` from the log that run wrote, so every figure here is the one that
build measured. It replaces the method of every earlier line of this revision: the humanized draft in
`humanize/` is taken as the document, and this paper supplies what the draft cannot, instead of the draft
being used to decorate a text this paper had already written.

## What the pass may touch

* a flowing prose block inside a numbered section, one at a time, when the draft has a paragraph for the
  same passage and the two carry the same values (numbers, status words, bare quantities, cross-
  references), in which case the draft’s paragraph is used as it stands;
* 164 paragraphs were taken, of which 0 are the draft’s own framing prose, inserted where this
  paper had no counterpart, and 0 carry this paper’s numbers transplanted into the draft’s sentence
  because the draft has since been overtaken;
* 33 of the paper’s paragraphs were displaced by the draft’s own paragraph for the same passage, and 128 of the draft’s paragraphs were taken where this paper had no counterpart; 164 draft paragraphs are in the text and 81 of this paper’s are left standing;
* the residue is restyled by the rules obtained by aligning the draft against the PDF it was made from
  (`stylekit_v1.py`, the GEM_* tables), a block at a time, and only where the values are untouched and the
  linter finds nothing new in the result.

## What it may not

* no table cell, no displayed equation, no statement heading, no numbered list item: they pass through
  byte for byte;
* no heading text, so the section numbering and the article labels the supplementary cites survive;
* not the front matter and not the back matter: the abstract’s sentences are fixed by instruction, and the
  references are carried;
* not the three companion documents, carried byte for byte from the v43 line: the draft is a humanization
  of the main text alone, so there is no draft wording for them to adopt;
* 8 headings of this paper (10, 2, 3, 3.7, 4, 6, 6.6, 8) carry prose of their own that the draft has no heading at the same number beside: that prose stays as this paper wrote it, and nothing is moved into it from elsewhere;
* 2 draft paragraphs were refused because the figures in them are not this paper’s;
* and no substitution survives whose own value multiset differs from the passage it replaced. That test
  decides each edit; the document-wide equality of values is the assertion.

## Measured on both sides

| quantity | before | after |
| --- | --- | --- |
| flowing-prose words | 20,911 | 24,529 |
| sentences of flowing prose | 818 | 1,038 |
| mean sentence length (words) | 27.0 | 25.2 |
| p90 sentence length | 56.0 | 53.0 |
| longest sentence | 231.0 | 231.0 |
| sentences over 60 words | 60 | 67 |
| em-dashes | 143 | 194 |
| semicolons | 215 | 227 |
| ", not Y" frames | 58 | 73 |
| "we" and "our" per 1k words | 0.3 | 0.2 |
| self-reference by "the article" | 37 | 4 |

The register is judged as the distance to the draft’s own profile, per 1000 words of flowing prose,
feature by feature and in aggregate, and the gate refuses the build unless that distance fell. Where the
audit instrument’s numeric target contradicts the draft, the draft governs and the gate names the
conflict instead of satisfying the cap; on this text the line is the semicolons.

## How the LaTeX is made

The four documents are typeset from their markdown, each by the converter the deposit has always used;
the article’s LaTeX carries 1647 formulas lifted out of the markdown before
conversion and put back unchanged after it, 3 piece(s) were fitted to the measure by scaling or narrowing (display scaled to the measure at line 728, 173.1pt, display scaled to the measure at line 664, 36.3pt, display scaled to the measure at line 634, 69.5pt), and
the gate reads the compiled text back and requires every flowing paragraph of the markdown to be in it.
Until this run the article’s .tex was the previous deposit’s, polished paragraph by paragraph beside
the markdown, which left the PDF carrying prose the style line had displaced. v45 and v46 shipped that way.

## Reproduce

```
python3 builders/build_v47_gbase.py      # text, tex, the four compiles, this note, the log
python3 builders/verify_v47_base.py      # every check, including the provenance of each paragraph
```

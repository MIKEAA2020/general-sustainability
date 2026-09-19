
## v46: the draft as the baseline document (what the method had to become)

The metric-target method (v44), the adoption-at-a-sentence-unit method (v44b) and the register-distance method
(v45) all left the document reading like the assistant's prose with corpus words in it. v46 inverts it: the
humanized draft is the document, and the paper supplies what the draft cannot. Measured on the shipped article:
97 of 250 flowing paragraphs are the draft's own text (40 of them the draft's framing prose, inserted where the
paper had no counterpart; 1 with the paper's numbers transplanted), 344 sentences verbatim in the draft against
119 in v42 and 174 in v45, register distance to the draft's profile 36.8 -> 23.1 units.

Durable findings:

* **Substitution is bounded by content, not by style.** The draft cannot supply §9, §11, the 63 statements, the
  tables or the exhibits: only section-level pairing with number transplant works, and the ceiling is the
  paragraph, not the sentence. Optimizing verbatim overlap alone capped near 20%; adoption at the paragraph with
  a *local* `values(body) == values(passage)` guard reached 39%.
* **Guard every edit at the unit of the change.** A document-wide value check reverted 62 of 65 good edits,
  because one stale digit elsewhere poisoned the whole set. The global equality is the assertion; the local one
  is the filter.
* **Any pass that mutates a whole-document buffer must run after the last structural rewrite of it**, and must
  run *on the text that ships*: v46 first computed styling into a buffer that a later stage rebuilt, which
  silently discarded it, and the gate only caught it because the profile is measured.
* **Protecting the author's wording has to cover every stage, not the first one.** The front matter, the back
  matter, table rows, headings and the section leads each had to be excluded from adoption, restyling and the
  self-reference map separately; a global regex map over the document rewrote a table cell and a lowercase
  "paper" after a full stop, and the gate named both.
* **Adopted draft text is not a style surface.** Once a block is the draft's, `register()` must not touch it:
  styling it moved it off the draft, which is the one thing the inversion is for. Same for the sentence-level
  `adopt()`: it had reached into the abstract and taken back a sentence the author fixed.
* Provenance is checkable at the sentence unit, not the block unit: a long block with three clauses edited
  scores ~0.4 similarity yet traces to source sentence by sentence.
* A defective kit rule surfaced only because the new test compared every shipped block against the sources:
  `GEM_AGENT`'s `we call -> the name given is` produced ungrammatical text (it reached the shipped v45 once).
  It is now `what we call -> what is called`, and restyle results are refused if the linter finds a fault the
  input did not have.

## v47: the draft as the document itself (the direction that finally worked)

v46 took the draft's paragraphs into the paper's document. v47 does the opposite and is the line that reads like
the humanization: the draft is the document, and the paper is grafted into it. Per numbered section, the draft's
paragraphs are emitted in the draft's own order; the paper supplies the skeleton the draft does not hold
(headings and numbering, the 61 statements, tables, displays, front and back matter), the prose of the ten
sections the draft has no heading for, and its figures where the draft has been overtaken. Result on the shipped
article: 141 of 333 flowing paragraphs (42%) are byte-identical to a paragraph of the draft, against 4 of 249
(2%) in v42; 458 of 942 prose sentences are verbatim in the draft; 52 of the paper's paragraphs were dropped as
restatements of admitted draft prose; register distance to the draft's profile 36.8 -> 21.4; 57 pages, unchanged.

What the draft could not be used for, and what that cost: 33 of its own statement-labelled paragraphs were
dropped in favour of the paper's numbering; 7 refused for a figure the paper does not state in that section; its
"how to read this version" note and its plain-words abstract are notes about the humanization, not article text.
The builder's five navigation leads were removed too - under this method a sentence written by the build for flow
would be the only text in the document that is neither the corpus's nor the author's, and the draft's 128
framing paragraphs do that job instead.

Two guard shapes made it survivable: a per-section containment test (a draft paragraph may displace a paper
paragraph only when the section goes on stating every value, hedge and reference the displaced one stated,
checked against the assembled section, with the whole section reverting if it does not), and a redundancy test
that requires *sentence-level* near-matching before a paper paragraph is dropped, so a caveat containing no
digits cannot be dropped because it happens to have nothing numeric in it. The document-level invariant changed
from "same multiset of values" to "nothing invented, nothing lost", because a merge legitimately repeats a
figure; the counts that moved are printed (89 values), and the tables, statements and equations remain
byte-identical, which is where the load-bearing numbers live.

Also: an `if os.path.exists(...)` guard around a shipped-file list hid a renamed builder for a whole package
build - the manifest diff against the previous archive found it. Diff the new archive against the old one; do not
trust a copy loop that cannot fail.

### v47, after the audit: what the two corrections were

The gate now prints ALL CHECKS PASS on a build whose article prints on 62 pages, and the LaTeX is transpiled from
`paper3_material_ledgers_v47.md` (1,647 formulas lifted out before conversion and put back unchanged), because the
`.tex` had been v42's file polished beside the markdown: v45 and v46 therefore shipped PDFs that never carried their
own graft. The tell was the page count not moving after 3,352 words were added; the proof the gate now holds is
that every flowing paragraph of the markdown is read back out of the compiled text (293 of 293).

Two wrong corrections were made and withdrawn during that fix, and both are worth keeping in the register. The
first imported the superseded article's 40-entry reference list into the document, on the theory that a citation
dangled; that makes v42 the baseline, which is not what was instructed. The second went the other way and recut the
draft's reflowed reference paragraph into entries, recovering lost year letters by DOI, which is a style line
deciding an authorship question. The rule that survives is the one already in the project: back matter is not prose
and no pass may hold it or lose it, so the graft is refused there as it is refused on headings, tables, statements
and front matter, and `verify_v47_base.py` asserts that the list shipped is the list the document arrived with,
entry for entry (40 = 40, and the self-reference map no longer turns `submitted with this article` into
`this paper`). What the baseline owes the reader is now recorded instead of repaired: the draft's list carries 25
of the 40 works, its reflow dropped the year letters separating five 2026 papers, and some words are glued -
open items for the author, not for this line.

Register, as the gate measures it on the shipped file: 164 paragraphs taken from the draft, 128 of them the draft's
framing prose, 40 carrying the draft's shape with this paper's numbers ported; 466 of 969 prose sentences verbatim
in the draft, 558 verbatim or near; 136 of the body's 293 flowing paragraphs the draft's as written against 105 of
this paper's own; distance to the draft's profile 36.8 to 21.8. Devices above the audit's cap and above the draft
are named, not trimmed: em-dashes 231 against the draft's 202, semicolons 225 against 170, ", not Y" 71 against 52.
Package: `paper3_supplementary_package_v7.zip`, 43 files, 1,439,179 bytes,
sha256 9b1ddecc653fa89bdf0df93adc22078796e3eade0332d7cabcabc0d5baa9eeea, manifest verified from a fresh unpack.

### v48, step 1: the claim ledger, before any prose

`revision/v48/claim_ledger_v1.py` pairs the draft's non-shared sentences with the deposit propositions they restate
and counts the verdicts; `claim_ledger_v1.md` holds the 62 pairs that need an adjudication, the CSV every one of
the 558. Nothing was written into the document and no build file was touched: the instruction was pairs first.

The instrument needed fixing before its numbers meant anything, and each fix removed a class of false alarm. Block
alignment by token overlap paired a reworded abstract with whichever paragraph in the file shared the word
`number`; sequential sentence alignment fixed that. Comparing a sentence's markers against one deposit sentence
called faithful plain English a dropped hedge; comparing against the aligned passage fixed that, and then
comparing *conditions* against the passage over-called them, so scope and strength are judged against the matched
sentence and its neighbours, and only on a pair good enough to compare. The value test read the prose after the
maths was stripped and so reported `$600{,}000$ kt` as a figure the deposit never states; figures are now read from
the raw text, `10^6` and `1,000,000` included. And a citation is a surname set with a year, not the last name
before the year, or `(Martinez-Alier, Munda and O'Neill, 1998)` becomes an invented `Munda 1998`.

The result: of 558 ledgered sentences, 465 restate a deposit proposition with no marker out of place, 0 contradict
the deposit on a value or on the direction of a claim, 61 differ in force, condition or attribution, 1 is a
sentence the deposit does not contain at all, and 31 are signposting rather than claims.

### v48: the reuse ruling, before the build

The author's ruling is recorded as data, not as a memory: `revision/v48/v48_reuse_split_v1.py` reads the claim
ledger and writes `v48_reuse_split.json` (every row, with the deposit passage to write from) and
`v48_reuse_split.md`. Reuse verbatim: the 275 supported sentences with a high-confidence pair plus the 31
signposting sentences that assert nothing, 306 in all. Regenerate from the deposit in the draft's register: the 188
supported rows at medium or low confidence - thin confidence is about the alignment, not about the draft, and where
the pairing is uncertain the truth source is the safer input - plus the 64 flagged rows, 252 in all. The two sets
partition the 558 ledgered sentences, checked by an assertion in the script.

The one sentence with no partner, `D0081` - `support drawdowns cannot be traded against revenue anywhere in the
ledger` - is kept and regenerated at the deposit's scope, because the deposited article's claim runs to
cross-component trades inside scalar indices and never uses the word `revenue`.

Two audit numbers changed after the figures-reading fix, and the corrected ones are the ones to quote: 463
supported (not 465), 12 scope flags and 18 strength flags (not 11 and 17). The spot-check stands as reported:
`scope` detected 0 of 4 planted defects, so those 12 are a floor; the strict census - the aligned passage no
longer answering for the sentence - moved 1 row, so the value and causality zeros are measurements and not the wide
window. And the 306 are disclosed as screened, not certified, which is written into the ruling file so a green
gate cannot be read as a claim about understanding.

## v48: the 306 read against the deposit, line by line (after the gate, before any build)

The split was a ruling from marker rules; the user refused to let that be the end of it — "check the 306 against the
deposit. read at line-level for flaws." Four instruments, all in `revision/v48/`, none of which touches a document:

- `v48_reuse_audit_v1.py` — restores the maths the ledger strips, puts each reused sentence beside the deposit's
  nearest sentence, checks pointers / surnames / strength verbs / status labels / universals / voice / units.
  Result: 10 flagged of 306, 296 nothing raised.
- `v48_audit_selftest_v1.py` — the zero spot-checked, because that number is either a clean set or a blind filter
  and the two look the same from outside: six planted defects, **6/6 caught**, untouched control clear. Getting
  here exposed four bugs in the audit itself — a `\0`-in-`re.sub` crash, a figure regex that read `240,000 kt/yr`
  as `000 kt`, a surname regex that caught `Finally`, and an **inverted unit test** that flagged figures the deposit
  had and ignored ones it did not. Fixed; the 296 is the working instrument's answer.
- `v48_notation_drift_v1.py` — the same 306 read as *maths*: 221 inline spans, 126 as the deposit writes them,
  20 grouping/QED, 19 font wrapper, 25 sub/superscript swap, **31 in no form at all**.
- `v48_reuse_findings_v1.py` — those 31 read one at a time: **16 sentences / 23 spans where the draft's symbol
  form collides with an object the deposited article has reserved** (`S^{\top}` vs `S_{\mathcal{T}}` and moiety `S`;
  `\mathsf{S,K}` for the §2.4 state vs the hybrid incidence matrix; a dropped `\mathsf{S}` in Conditional Theorem 15's
  hypothesis; `\mathcal A` for a barrier that is the article's *adequacy functional*; `\mathcal B` for a biomass
  limit that is the *attainable-balance domain*; `\mathcal H` for horizons the article calls `H_A^{…}`).
  `v48_overrules_notation_candidate.csv` moves those 16 to regenerate — dry-run: reuse 306→290, regenerate
  252→268, partition 558 of 558, all moves logged. The live `v48_overrules.csv` is still the empty template.

Substantive, in the same read: D0089's "every depletion horizon … stated against a rate **and** a barrier"
mis-describes the article's own three-quantity table (rate / ratio / first-passage-under-scenario) and sits in the
31 rows reused for "asserting nothing", 20 of which do assert document facts; D0158 has `each` → `every` in the
depletion-quantity list; D0108 as the draft wrote it drops `(USGS)` — the only definition of an abbreviation used
three times — and prints `US` where both documents print `U.S.` elsewhere. Six of the ten flags were my own noise
and are recorded as such, not silently dropped.

And the finding that changes what "carry the draft's sentences" means: 4 `S^{\top}` and 6 `\mathcal H` are **already
in the packaged v47**, next to the notation-table row that defines `S_{\mathcal{T}}`, with `\mathsf{S}` printed for
two different objects. The numbers gate could not see it — the figures inside the spans are the deposit's own — and
the ledger could not see it at all, because it deletes `$…$` before reading a sentence. Reported, not repaired: the
choice between "regenerate the 16" and "normalise the reused maths at build time" belongs to the author, and the
build note has to carry the D0218 anonymised-citation placeholder either way.

Still no document touched. v48 builds when the user says so.

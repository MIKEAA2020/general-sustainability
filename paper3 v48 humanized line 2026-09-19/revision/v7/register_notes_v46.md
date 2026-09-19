
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

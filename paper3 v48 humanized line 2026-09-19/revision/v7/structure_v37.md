# Structure register - paper3_material_ledgers_v37

Built from v36 by `build_v37_kernel.py` (10 logged edits; v36 and earlier unchanged on disk). Gate
`verify_v37_build.py` -> ALL CHECKS PASS. PDF 54 pages (v36: 53, v35: 51, v34: 48).

## What this batch is

Not a reviewer response. It is the closure of the last two items that had been parked as "the author's", after
checking whether they really were:

- **D4** was recorded as "wording the author must draft". That was wrong: the wording has existed in
  §1.5 (Antecedents) since v5, and what was outstanding was the *substance* of its standards claim. Every
  clause of it has now been verified against primary material, and the sentence was rewritten so that it makes
  a point instead of gesturing at one. The reference entry's "Adopted by ... fifty-sixth session" became
  "Endorsed by ... fifty-sixth session, March 2025", which is the language the adopting body uses.
- **MDV** was recorded as needing the author's theory. Its checkable half turned out to be an undefined object
  *in the article itself*: equation (1) writes $S_{\mathcal{T}}$, and "typing" is then used as one of the three
  admissibility predicates (Definition 42), as the thing Section 2.5's routing claim belongs to, and as the
  reason a score in Section 6.5 mixes incommensurable objects --- five uses, no definition. So the root cause
  was not a missing citation but a missing definition, and it is now supplied: **Definition 47 (Type
  structure)**, **Proposition 42 (No conservation law crosses a type class)**, **Remark 36 (What the type
  structure buys, and what it does not)**. MDV as a valuation thesis stays out, explicitly and with reasons.

## New subsection

`### 3.8 The type structure the operator's subscript abbreviates`, placed at the end of Section 3 so the
continuous label counter stays monotone (Definition 47, Proposition 42, Remark 36), with forward pointers from
the four places that were using the word:

- §2.1 "That sentence presumes a declaration, and the declaration is Definition 47";
- §2.1 "Proposition 42 states exactly in what sense it cannot" --- attached to the sentence that had been the
  article's barest assertion ("the identity does not create a scalar sustainability mass across incommensurable
  systems"), which is now a corollary of a block-diagonal decomposition;
- Definition 42's predicate list reads "typing (Definition 47)";
- §6.5's charge names "the type structure of Definition 47".

## What Proposition 42 actually says

Types joined by declared conversions form classes; admissible columns meet one class each; so $S_{\mathcal T}$
is block diagonal and $\ker S_{\mathcal T}^{\top} = \bigoplus_\gamma \ker S_\gamma^{\top}$, hence every
conservation law is carried by one class and none prices one class against another. Two consequences the batch
needed: the cross-class "sustainability mass" is not derivable from (1) but an additional declaration (so the
question is Definition 23's, and its propagation is Proposition 36's); and invariance to *reporting*
redrawing holds exactly when no conversion is declared or withdrawn --- the precise, checkable form of the
umbrella invariance that the review cycle kept asking for, and the reason a single unconditional theorem is
still not stated.

## Data-integrity addition found while verifying (Section 6.5.1)

The G3P exhibit now names its anomaly reference period (April 2002 to December 2020, per the producer's
documentation) and carries the producer's own defect notice: a faulty snow-water-equivalent entry for June 2005
propagates into groundwater storage, with a recommendation to exclude that month. The article's window
(April 2002 to September 2023) spans that month, so the exhibit states that a re-derivation must declare
whether it is retained, since both the fitted trend and the series' own minimum can move. Naming the reference
period also satisfies a rule the article states for itself (Lemma 4: an anomaly is reported together with the
construction of its baseline, never against an implicit one) --- previously it promised that and did not do it.

## Gate

- Reversal: undoing the 10 edits reproduces v36 byte-exactly in both formats (md 204,628 chars normalised, tex
  221,170), modulo whitespace and the display-underscore convention.
- Block: `v37_block_typing.md` shipped verbatim into md; into tex after the md->tex dialect conversion
  (`block_to_tex`, which also emits the `\subsubsection{...}\label{...}` heading).
- Labels: 58 -> 61, md set identical to tex set, no type+number pair repeated, no duplicate `\label` in tex;
  maxima Definition 47, Proposition 42, Theorem 24, Remark 36, Lemma 4, Corollary 19; numbering note reads
  "1-47" with the extended added-label list in both formats.
- Dialect: tex pure ASCII, `$` count 0, doubled backslashes 0 in both formats, block `$` count 80 (even).
- Superseded wording absent: the old standards clause, the old "Adopted by" reference line, and the old
  "typing of Section 2.1" citation are gone from both formats; "LSIT" still absent from both.
- 26 prose probes and 7 math probes present in both formats; 7 PDF text probes present; literal underscores in
  the rendered math still 2 (the e-mail address).
- One build-loop defect caught by the gate and fixed: an edit intended for Section 6.5 matched the *same
  wording quoted inside the new block* and rewrote a quotation. The block now paraphrases rather than quotes,
  and the gate asserts the quoted phrase appears exactly where the article says it does.

## Files this batch produces

`paper3_material_ledgers_v37.{md,tex,pdf}`, `build_v37_kernel.py`, `verify_v37_build.py`,
`v37_block_typing.md`, `revisions_v37_kernel_log.json`, `supplementary_v9_candidate.md`, and
`review/open_items_v5_d4_mdv.md`.

## What is left for the author

1. One cell in the supplementary table: the pull date (or DOI/release tag) of the archived RAM Legacy extract.
   Its content is re-derivable but its *vintage* lives in an analysis repository that is not in this tree, and
   the existing S5 record already shows that no public release reproduces the 43-stock cohort.
2. One yes/no: keep the rewritten Section 1.5 standards paragraph (it is now sourced clause by clause), or cut
   it back to a half-sentence. Either is safe; the paragraph is positioning, not a premise.
3. Confirm which RAM Legacy release the supplementary's version-sensitivity table calls "current v4.66"
   (v4.65, dated 17 June 2024, is the newest I could confirm today; v4.44's label and Zenodo record 2542919 are
   both correct as printed).
4. The standing items: `revision/v5/code/` into the deposit record; whether the article ever names MDV in the
   body (default now: no, with the correspondence table in S12 doing the work).

Nothing in this list blocks another reviewer round.

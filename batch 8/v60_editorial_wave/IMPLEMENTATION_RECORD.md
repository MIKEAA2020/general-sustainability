# v60 Editorial Wave — Implementation Record

Task 118 / batch 8 / paper 1. Source: `paper1_assessment_separation_v59.tex` (3,186 lines,
52 pp). Product: `paper1_assessment_separation_v60.tex` (3,174 lines, 52 pp).
Builder: `make_v60_p1.py` (this directory; 30 anchored, position-independent
operations; idempotence by destination-exists gate; exit 0).

## Owner directives and their disposition

1. **Affiliation.** The `\address[aff]` block now reads
   "Independent Researcher, Tehran, Iran, ORCID: ..., amin_abaee@ut.ac.ir" —
   matching the family's paper3 (JIE v3) and paper4 (v41) convention.

2. **Change-log / diary strip (findings-first restatement).**
   - Off-diagonal closure opener: "The first limit recorded above is no
     longer open. A third dedicated exact computation ... after the spectrum
     above and the common-shock computation of Section 5.9 ... has decided
     every off-diagonal cell that the rational conditions left undecided"
     → "Every off-diagonal cell that the rational conditions leave
     undecided --- and with it the complete two-dimensional σ*-landscape ---
     is decided by a dedicated exact computation in the same programme
     (same datum, same exactness standard, same delimitations)." (The
     computation-order narration is dropped; the check-list accounting
     already establishes separateness.)
   - "The fail-loud discipline ... was never triggered: zero cells remain
     undecided." → "Under the fail-loud discipline (...), zero cells remain
     undecided."
   - Continuum slice closure opener: "The second limit recorded above is no
     longer open either. A fourth dedicated exact computation ... has
     decided the continuum." → "The continuum slice-minimum --- the open
     residual recorded above --- is decided: a dedicated exact computation
     in the same programme (same datum, same exactness standard, same
     delimitations) settles the continuum."
   - "the scan evidence of the fixed-sum remark is upgraded to a proof" →
     "the fixed-sum remark's scan-level finding is thereby proved."
   - "acquires no closed form" → "admits no closed form."
   - Common-shock intro: "left ... as the one honestly-open verdict: its
     assertion demanded ..." → present-tense "leaves ... as the one
     undetermined verdict: its assertion demands ..."; "records that
     computation, and in passing sharpens" → "records that computation and
     sharpens."
   - Theorem M2: "the resource route no longer rescues every failure
     state" → "fails to rescue every failure state."
   - Limitations registry: item (x) 's stale trailing clause ("the
     continuum slice-minimum remains an open residual, the interval
     character ... machine-evidenced, not proved") removed — superseded by
     the closure; item (xi)'s "stated two limits in place ... a limit the
     off-diagonal closure has since closed, every cell now decided" →
     "states two limits ... the off-diagonal closure decides every such
     cell by finite rational proof"; the common-shock item's "states its
     limits in place" → "states its limits"; items (xiii)+(xiv) MERGED into
     one findings-first item ("The continuum slice-minimum of the fixed-sum
     tolerance structure --- where a slice's best point lies --- is closed
     (the continuum slice closure of Section 5.8): ... certified on the
     continuum, not only at the scanned points ..."), preserving every
     certified fact of item (xiv) and the ecological-content clause of item
     (xiii) in upgraded form. Registry now ends at item (xiii).
   - Contributions list item (xiii): stale locator "(the closing block of
     Section 5.8)" corrected to "(Section 5.8)"; the continuum slice
     closure — the one Section 5.8 result the list omitted — added (the
     φ-reduction, the ten-place flip total, intervals, the total-3
     boundary, the harmonic circle, the σ*-depth sandwich, the flip-total
     ladder), "machine-verified as a fifth check list" → "as fifth and
     sixth check lists."

3. **Self-praise / informal register.**
   - "Verification and honest limits." → "Verification and limits." (×2);
     "Honest limits, in the spirit of the two recorded above:" /
     "Honest limits, in the same spirit:" / "Limits, stated honestly:" →
     "Limits:" (×3); "an honest open residual" → "an open residual";
     "the one honestly-open verdict" → "the one undetermined verdict";
     "the programme's one honestly open mathematical residual" (removed
     with the merge); "the family's defining honesty" → "the family's
     defining property."
   - "punchline" → "statement" (contributions item (xi); Theorem S2 title).
   - "seen to bite on" → "seen to bear on"; "Northern-cod-style" → "after
     the Northern cod case"; "DFO-precautionary-approach-style" → "DFO
     precautionary-approach"; "in the domestic language of" → "in the
     language of"; "The datum, domesticated." → "The datum, in resource
     terms."; "the family's non-pooling policy" → "the programme's
     non-pooling policy" (×4; one unambiguous referent, consistent with
     "the same programme").
   - Provenance header comment added (one line, after the existing
     author/software comment).

4. **Deliberately NOT touched (legitimate, per the owner's directive).**
   The "No empirical ..." scope delimitations (Limitations, benchmark,
   labelled-extension intros); the photograph/tube metaphor pair and its
   uses; the LPI-identification caveats; "deliberately spare" /
   "deliberately adverse reporting architecture" (design rationales); the
   standard "first unrescuable-by-reserve failure states on this datum"
   (standard first-example mathematical usage); all companion-paper
   citations (all carry Zenodo DOIs or "Manuscript submitted for
   publication" APA status — they will be published, so referencing them
   is correct); first-person-plural conventions. No reference to any
   superseded manuscript version exists in v59/v60 (scanned: "version",
   "draft", "superseded", "v5x", "manuscript version" — zero hits).

## Content audit (owner's question: anything lost or condensed?)

- v58 → v59 verified purely additive (two hunks, zero removed lines).
- Chain audit v22 → v59: removal steps carry 93–100% distinctive-token
  survival in v60; the few non-surviving fragments are LaTeX scaffolding,
  line-fragments whose continuations survive, or verified reformulations
  (the Martinez-Alier attribution survives in the introduction; the
  v33 data-requirements checklist survives as the S9 supplement pointer).
- Original upload (`paper rewrites/paper1_assessment_separation.md`): all
  49 distinctive numeric tokens survive in v60.
- Internal duplication scan: only the intentional parallel verification
  formulas, abstract↔body echoes, and the one-sentence scope statement
  repeated in contributions and limitations (all acceptable); the one
  genuine redundancy (limitations items xiii/xiv) is merged in this wave.
- Over-hedging scan: zero "map-is-not-the-territry"-type apologies exist;
  the scope statements that remain are standard delimitations.

## Gates (all green)

- **Inverse reconstruction:** reverting all 30 operations in reverse order
  reproduces v59 byte-identically (count-aware reversion).
- **Math-span multiset:** 1,470 → 1,470 (4 superseded spans removed with
  the merged limitations item: (141/50, 353/125], 2√2, the free-standing
  σ*, and item (xiii)'s edge-clause 3; 4 added by the contributions
  extension: φ, t* = a* + b*, 3, σ*; zero alterations of any other span).
- **Marker accounting:** 34 new markers present, 37 retired markers absent.
- **Structure pins:** environments balanced and unchanged (enumerate 4,
  itemize 8, figures/tables unchanged); exactly one `\item` removed (the
  merge); all pinned headings intact.
- **Register sweep:** 11 banned residues absent (honest, punchline, no
  longer open, was never triggered, has since closed, in passing,
  addendum, domesticat, in place:, stated in place, upgraded to a).

## Compile battery (all green)

- Tectonic in place: exit 0; 52 pp (v59: 52); 0 errors; 0 undefined
  references; overfull profile identical to v59 (the single pre-existing
  2.43091pt header box); underfull 55 = v59's 55.
- Flat self-containment compile (tex + figs_p1 alone, scratch directory):
  exit 0, 52 pp.
- PDF text layer: all edited regions render (Tehran affiliation; both
  closure openers findings-first; the merged item; the contributions
  extension; every informal-term replacement). The single initial
  text-layer miss was a pdftotext de-hyphenation artifact ("nonpooling"
  from a hyphenated line break), verified present after normalization.
- VLM raster checks: page 2 (affiliation renders "Independent Researcher,
  Tehran, Iran, ORCID: ...", cleanly typeset), page 34 (the continuum
  closure opener and the Limits lead-ins render; no diary phrasing), page
  41 (a single merged item (xiii); clean typesetting).

# Structure register - paper3_material_ledgers_v38

Built from v37 by `build_v38_kernel.py` (9 logged edits; v37 and earlier untouched). Gate
`verify_v38_build.py` -> ALL CHECKS PASS. md 219,231 B / tex 235,748 B / PDF 55 pages (v37: 54, v36: 53, v35: 51, v34: 48).

## What this batch changed

1. **Funding** (`funding-declaration`). The Declarations block had Data availability, Code availability and a
   competing-interest statement and no funding line. Now `## Funding` / "None declared." in the same position and
   wording the sibling articles in the repository use (`\subsection*{Funding}` / "None declared."), ahead of the
   competing-interest statement in both formats.
2. **Section 1.5 made causally self-contained** (`sec15-causal-coherence`). The paragraph is *kept*, and the
   decision to keep it is not cosmetic: v37's Remark 36 refers back to it ("the statistical standards recalled
   in Section 1.5"), and v37's rewrite had dropped the asset-boundary sentence that reference pointed at,
   leaving a forward pointer to content that no longer existed. v38 restores the missing clause (for the
   renewable-resource categories the 2025 revision admits, the asset boundary is drawn by viability under
   prevailing technology and prices - an eligibility statement of the kind Remark 36 treats as
   reclassification) and adds the direction clause: the standards supply an instance, not a premise, and
   nothing in Sections 2 to 10 depends on the paragraph. So the causal arrow inside the article now runs one
   way and is labelled, and the paragraph's only load-bearing dependant (Remark 36) resolves.
3. **A false statement in a proof, corrected** (`fibre-polytope-fix`, `fibre-proof-fix`). The shipped proof
   asserted that extrema of a continuous function over a polytope are attained at vertices - contradicted by the
   instance printed two sentences earlier. Recomputed: max of tau = 3.912023 at y = 50.0 (interior), min = 0 at
   an end. The claim is replaced by the exact polyhedral case and its scope.
4. **Rows versus quotient, both given** (`quotient-versus-rows`) in Definition 34, including the
   class-wide type/unit agreement check that now means something because of Definition 47, and the statement
   that certificate descent is Proposition 36's and not automatic.
5. **Definition 40's verdict made three-way** (`compensation-verdict`) with its infeasibility witness, its
   not-established branch, its no-dynamic-safety limit, and the point that a positive charge prices rather than
   prohibits compensation.
6. **Interface price and capacity price re-labelled for what they are** (`price-is-certificate-relative`) in
   Remark 34: the price is certificate-relative (lambda = (2,1) vs (1,2) on the same physics), admissibility is
   not; a capacity price at a kink is a supergradient selected from the interval [0, 1], verified by LP on the
   two-cycle programme rather than quoted from the review.
7. **The fisheries extract's vintage pinned** (`ram-vintage-pinned`, `ram-vintage-data-avail`): release v4.66,
   Zenodo 14043031, vintage verified from the extract's own published-F anchors, no cohort statistic quoted from
   any other release. This replaces "the pull date is archived in the analysis repository", which no reader can
   check.

## No new labels

Every edit sits inside an existing numbered statement, so the continuous counter is unchanged at 1-47 with
maxima Definition 47 / Proposition 42 / Theorem 24 / Remark 36 / Lemma 4 / Corollary 19, and the numbering note
is untouched in both formats (the gate asserts this).

## Gate

9 reversible edits; reversal v38 -> v37 byte-exact modulo whitespace in both formats (md 211,992 normalised
chars, tex 228,782); 61 labels, md set identical to tex set, no repeats; tex pure ASCII, `$` count 0, doubled
backslashes 0; 8 math and 16 prose probes present in both formats; the Funding heading present in both and
ordered before the competing-interest statement; 5 superseded or erroneous strings asserted absent (including
the false vertex assertion and both "archived in the analysis repository" phrasings); md 219,231 B / tex 235,748 B / PDF 55 pages with 6 text
probes present and literal underscores in rendered math still 2 (the e-mail address).

## Provenance

`review/points_v5_prompt_response_closed.md` (all 16 markers of `uploads/p3 prompt response.txt` adjudicated
against v37's text, with the LP and grid verifications recorded), and the read-only sparse checkout of
`github.com/MIKEAA2020/general-sustainability` at `refs/tags/edwards-framework-e1` for the RAM Legacy record.
`revision/v7/supplementary_v9_candidate.md` has no `[author]` cells left.

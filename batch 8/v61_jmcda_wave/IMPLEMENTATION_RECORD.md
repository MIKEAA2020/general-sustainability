# v61 JMCDA Alignment Wave — Implementation Record

Task 119 / batch 8 / paper 1. Source: `paper1_assessment_separation_v60.tex`
(3,174 lines, 52 pp). Product: `paper1_assessment_separation_v61.tex`
(3,256 lines, 54 pp). Builder: `make_v61_p1.py` (this directory; 18
anchored, position-independent, prose-level operations; idempotence by
destination-exists gate; exit 0). Reference records: `batch 8/p1 journal
alignment.txt` (the owner's uploaded inventory, preserved verbatim) and
`batch 8/v61_jmcda_wave/JOURNAL_ALIGNMENT_EVALUATION.md` (this wave's
evaluation: Part A — the venue research and pre-upload inventory S1–S13;
Part B — the owner's inventory B1–B8, evaluated and reconciled).

## The venue decision

Target: *Journal of Multi-Criteria Decision Analysis* (Wiley), special issue
**"Better Decisions for a Better Tomorrow: MCDM Approaches for
Sustainability, Risk, and Complex Systems"** — open for submissions,
deadline 31 January 2027 (verified on the journal's Wiley home page and the
MCDM Society announcement; the owner's inventory independently confirms).
JORS evaluated as comparator and recorded as fallback only (its practice
orientation would require scope changes the owner's delimitations exclude;
the surviving JORS suggestions — the OR translation emphasis — are absorbed
into the JMCDA edits; the JORS-SI citation it suggests is recorded for
rerouting use only, unverified at source).

## The implemented operations (S/B-numbers refer to the evaluation record)

1. **Provenance (OP 1).** The v60 header comment's date corrected
   (2025-09-22 → 2026-09-22, matching the wave's own implementation
   record) and the v61 header line added.
2. **Venue declaration (OP 2).** `\journal{Journal of Multi-Criteria
   Decision Analysis}` (family precedent: the EMS variant declares its
   venue). Wiley free-format submission accepts the elsarticle chain.
3. **JEL apparatus retired (OP 3a/3b).** The `\providecommand{\jel}`
   definition and the `C61; C62; D81; Q01; Q56` block removed — an
   economics-venue artefact; JMCDA is an OR journal. The git chain
   preserves both for any economics rerouting.
4. **Abstract opening re-cast (OP 4, S1).** Now opens "In multi-criteria
   assessment, compensatory and noncompensatory aggregation give two
   readings of the same constraint set: the scalarized reading, which
   permits substitution through a weighted aggregate (weak sustainability),
   and the coordinate-wise reading, which imposes separately-binding floors
   (strong sustainability)." The sustainability anchor survives; the
   aggregation semantics lead. (Abstract: 266 words — within the venue's
   300-word limit.)
5. **Keywords re-ordered (OP 5, S1) then trimmed to seven (OP 14, B6).**
   Final list: "multi-criteria decision analysis; compensatory and
   noncompensatory aggregation; composite indicators; scalarization;
   robustness; sustainability assessment; transition safety" — the
   venue's seven-keyword limit (matching the original v60 count).
6. **First highlight re-cast (OP 6, S1).** "Compensatory and
   noncompensatory (weak- and strong-sustainability) criteria are compared
   as robust transition-safety problems on a common datum."
7. **The MCDA compensability canon (OP 7, S2).** Section 1.1:
   multi-attribute value theory's substitution rates (Keeney and Raiffa,
   1976); outranking's concordance/veto (Roy, 1996); the decision-aiding
   treatment of incommensurability in sustainable development (Munda,
   2005); "orthogonal to both" widened to "orthogonal to all of these:
   even if weights perfectly reflect importance and substitution rates are
   elicited faithfully, the quantifier order can still produce the gap."
8. **Adjustable-robustness reading promoted (OP 8, S4).** At the protocol
   introduction (Section 1.2): Protocol 4 commits to one plan before the
   assessment weight is known, Protocol 2 lets the plan adapt once the
   weight is observed — the here-and-now versus wait-and-see distinction
   of adjustable robust optimization (Ben-Tal et al., 2004), with the
   weight in the role of the uncertain parameter.
9. **The acceptance-semantics positioning paragraph (OP 9, S3 + S5,
   absorbing S11).** Section 5.2, after the established-theory paragraph:
   the four protocols as acceptance semantics — the sorting problematic
   of decision aiding (Roy, 1996; Vincke, 1992); the weight-adaptive rule
   stated precisely; the licensing thresholds as the verdict's exact
   weight-sensitivity intervals, the acceptance-side analogue of the
   sensitivity analyses applied to composite-indicator rankings (Nardo et
   al., 2008); the static-vs-protocol compensability delimitation against
   Cinelli, Coles, and Kirwan (2014) and Schär, Pohl, and Geldermann
   (2025).
10. **The three-constituency conclusions paragraph (OP 10, S6).**
    Multi-criteria assessment (the certification failure lies in the
    acceptance protocol — not in weight choice, not in compensability at
    fixed profiles); decision making under uncertainty (the gap measures
    the value of information about the assessment weight; menu
    convexification, not temporal sharing, removes it); transition
    management (per-floor reporting along the path is the detection
    requirement the separation makes exact). No venue named.
11. **The decision-aiding-context paragraph (OP 15, B1 — the owner's
    policy-critical item).** At the fishery benchmark's opening
    (Section 6.3), directly after the "no empirical claim" sentence: the
    decision maker (the resource authority); the decision alternatives
    (the menu's management schedules: NO-SWITCH, FAST, SLOW, and the
    reserve-financed STAGED); the criteria (the two typed floors,
    evaluated path-wise under the declared disturbance); the preference
    reading of the scalarization weights; the acceptance gap as a
    robustness failure of the decision-aiding process in the precise
    sense of Theorem 5 (at every preference weighting the index licenses
    some alternative — possibly a different one at different weightings —
    while no single alternative satisfies the criteria path-wise); the
    analyst-communicable deliverables (the licensing thresholds as the
    preference ranges over which each alternative is certified; the
    rescue threshold as the adjustment funding that converts an
    unlicensable state into a staged transition); and the operational
    decision relevance (the asymmetric allocations of the substitutability
    extension, where the same total margin draws opposite verdicts and
    opposite management responses). This satisfies the JMCDA editorial
    policy that theoretical papers be "well-motivated by explicit decision
    making contexts" — the one gap left by the Part-A adoptions.
12. **The preference-range clause (OP 16, B3).** The Section 5.2 threshold
    sentence gains "the preference ranges over which each plan is
    certified" beside the weight-sensitivity/Nardo analogue.
13. **References (OP 12, S2).** Four canonical entries added
    alphabetically — Keeney & Raiffa (1976); Munda (2005, the State of the
    Art Surveys chapter); Roy (1996); Vincke (1992). All verified
    canonical; Munda bridges MCDA and the ecological-economics
    weak-comparability thesis the paper already cites.
14. **Cover letter (OP 13, S7 + B5).**
    `COVER_LETTER_paper1_assessment_separation_JMCDA_v1.md` (latex
    folder): the SI-named submission letter — the acceptance question in
    MCDA terms, the established results, the three-theme fit
    (sustainability / risk / complex systems), the exact-arithmetic
    verification discipline, the per-floor reporting implementation
    insight, and the declarations. Follows the family's JEDC/SVVA letter
    format.

## Evaluated and rejected (recorded in the evaluation record, not implemented)

- S8 retitle (the cross-paper citation network cites the current title).
- S9 MCDA/MCDM abbreviation entries (the manuscript spells the terms out).
- S10 software-paper reorientation (the EMS lineage owns that treatment).
- S12 JORS practice/case-study reorientation (violates the scope
  delimitations).
- S13 mathematical-register softening (the verification discipline is a
  core contribution).
- B2 wholesale terminology replacement "plans"→"alternatives",
  "floors"→"criteria" (would overwrite the technical register the
  companion network shares; absorbed instead by OP 15's decision-context
  vocabulary, used exactly where it is the right register).
- B3's dedicated thresholds subsection + decision table (redundant with
  Theorem 5(6), the two translation tables, and the weight-intervals
  figure; the deliverable reading adopted instead via OP 15/16).
- B7 the JORS 2026 sustainability-SI citation (JMCDA target; unverified at
  source; recorded for any JORS rerouting).

## Gates (all green)

- **Inverse reconstruction:** reverting all 18 operations in reverse order
  reproduces v60 byte-identically.
- **Math-span multiset:** 1,470 → 1,470, zero delta — every operation is
  prose-level by design (verified by multiset equality, the strongest
  form: no span added, removed, or altered).
- **Marker accounting:** 30 new markers present, 9 retired markers absent.
- **Structure pins:** environments balanced and unchanged (enumerate,
  itemize, figure, table, longtable, abstract, keyword, highlights,
  frontmatter); `\item` count unchanged; all pinned headings intact.
- **Register sweep:** the 11 v60 banned residues absent; venue register
  clean — no journal name, abbreviation, or special-issue mention in the
  document body (the single References occurrence of the journal name is
  the Schär et al. 2025 entry — a JMCDA paper the manuscript already
  cites, verified to be exactly one).

## Compile battery (all green)

- Tectonic in place: exit 0; 54 pp (v60: 52 — the additions account for
  the two pages); 0 errors; 0 undefined references in the final pass (no
  `??` anywhere in the PDF text layer).
- Overfull/underfull profile identical to v60: the single pre-existing
  2.43091pt header box, underfull 110 = v60's 110 — zero new boxes.
- Flat self-containment compile (tex + figs_p1 alone, scratch directory):
  exit 0, 54 pp.
- PDF text layer: all markers render, including the final build's new
  items (the seven-keyword line; the decision-aiding-context paragraph
  with all six content elements; the preference-range clause in Section
  5.2). The three initial text-layer misses were artifacts, verified
  present after inspection: a de-hyphenated "multicriteria" at a line
  break, and two page numbers interleaved by pdftotext at page breaks
  (20 in Section 5.2; 41 in Section 6.3).
- VLM raster checks: page 2 (seven keywords exactly, ending "transition
  safety"; no "viability theory"/"quantifier order" in the keywords; the
  "Preprint submitted to Journal of Multi-Criteria Decision Analysis"
  footer), page 21 (the strengthened threshold sentence with the
  preference-ranges clause), pages 42–43 (the decision-aiding-context
  paragraph spanning the break; all six content elements verified: the
  decision maker and alternatives, the criteria and preference reading,
  the robustness-failure sentence, the deliverables sentence, the
  operational-relevance close). Earlier-build checks for the
  Part-A-only regions (abstract p2, intro canon p4, conclusions p46)
  remain valid — those operations are byte-identical in the final build
  and marker-verified by the builder's gates.

## Companion deliverables

- `COVER_LETTER_paper1_assessment_separation_JMCDA_v1.md` (latex folder;
  described above).
- `batch 8/p1 journal alignment.txt` — the owner's uploaded inventory,
  preserved verbatim (received mid-wave via the repository; reconciled in
  the evaluation record Part B).
- `batch 8/v61_jmcda_wave/JOURNAL_ALIGNMENT_EVALUATION.md` — this wave's
  evaluation record (venue facts, fit table, S1–S13 + B1–B8 inventories
  with adopt/reject decisions, and the implementation map).

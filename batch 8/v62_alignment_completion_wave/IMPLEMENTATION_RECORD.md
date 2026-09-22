# v62 Alignment-Completion Wave — Implementation Record

Task 120 / batch 8 / paper 1. Source: `paper1_assessment_separation_v61.tex`
(3,256 lines, 54 pp). Products: `paper1_assessment_separation_v62.tex`
(3,268 lines, 54 pp) and `paper1_supplementary_v12.md` (327 lines; v11 +
exactly one appended S10 note). Builder: `make_v62_p1.py` (this directory;
4 anchored, prose-level operations; idempotence by destination-exists
gate; exit 0).

This wave answers the owner's six-question post-v61 audit: (1) remaining
points of `batch 8/p1 journal alignment.txt` worth implementing; (2)
anything worth delegating to the supplementary; (3) full alignment of
abstract, keywords, sections, and supplementary with the latest version;
(4) whether the supplementary needs completing; (5) whether the work
merits additional genuine pedagogical/expository/ecological completions;
(6) a conceptual-clarity and seamless-flow scan.

## The audit findings

**Q1 — remaining alignment items.** One item remained implementable: the
owner's uploaded inventory (its JMCDA plan item 2) asked for the benchmark
to be presented with "conflicting objectives (ecological floor vs. income
floor)" and "multiple stakeholders (fishers, regulators, conservationists)".
Task 119's OP 15 adopted the decision-aiding context but left the
stakeholder/conflict vocabulary implicit. Adopted here as OP 4. Everything
else was verified settled: the terminology-map rows for the rescue
threshold and the acceptance gap already exist in the Section 5.3 table
(the JORS plan's item 5); the decision table for the licensing thresholds
stays rejected (redundant with Theorem 5(6), two translation tables, and
the weight-intervals figure); the JORS-side items (the JORS-2026-SI
citation, unverified at source; the ~5000-word limit; the code-deposit
emphasis) stay recorded for rerouting only.

**Q2 — delegation to the supplementary.** Evaluated and declined. The
venue has no strict word limit; the labelled extensions (Sections 5.8 and
5.9) carry the relevance chains — the named-decision / report-flip /
action-flip evidence — that serve the venue's "explicit decision making
contexts" requirement; the verification discipline is a distinguishing
contribution; the Limitations registry is load-bearing scoping; the
framework extensions are already in the supplementary (S1–S4); and the
practitioner checklist serves the applied readership. No main-text
material warrants delegation.

**Q3 — alignment.** Two gaps found and fixed:
- The List of abbreviations carried three entries (CES, MSY, PROMETHEE)
  while the body uses four further abbreviations without entries: DFO
  (Section 5.8's relevance chain and the benchmark's data anchor), LPI
  (eleven uses from the sigma-extension on; spelled out twice but never
  formally introduced), LRP (eighteen uses, first in Section 5.8 — long
  before the benchmark's expansion), and NCAM (twice at the data anchor;
  expansion confirmed against the family corpus: Northern Cod Assessment
  Model). Fixed by OP 2 (seven entries, alphabetical).
- The supplementary's S10 positioning notes (which "expand the main
  article's Section 5.2") lagged the v61 Section 5.2 by its newest
  paragraph — the acceptance-semantics positioning (sorting problematic;
  weight-sensitivity intervals; static-vs-protocol compensability). Fixed
  on both sides: OP 3 announces the reading in the Section 5.2 pointer,
  and the supplementary v12 adds the fourth S10 note.
  Everything else audited clean: the abstract (263 words, within the
  venue's 300) and keywords (7, the venue's limit) match the body; all
  section cross-references resolve (5.5/5.6/5.7/5.8/5.9, 4.9–4.11,
  Appendices A–C, S8/S9/S10 pointers); the supplementary's title line
  matches the manuscript title exactly; the check-list counts (25/24/57/
  50/44/77) are consistently stated; the companion citations carry DOIs
  or submitted-status per the standing convention.

**Q4 — supplementary completeness.** The supplementary is complete as a
companion: every S-section referenced by the main text exists (S8
enumerates the 25 checks one by one; S9 itemizes the five data
requirements; S7 covers both the grid verifier and the software
companion's 24-check suite; S1–S6 carry the declared-status extensions).
The partial-status markers (S4's conditional/unsupported items) are
deliberate, load-bearing honesty — completing them is new research
(composition-extension equations and proofs), not an editing task, and
the main text's Scope statement depends on their declared status. The
one completion warranted was the S10 alignment note (Q3), implemented.
An enumeration of the four extension check lists (57/50/44/77) in the
supplementary was evaluated and declined: the main text's inline
verification paragraphs carry the counts and scope; the deposited run
logs carry the enumerations; a supplementary copy would duplicate.

**Q5 — additional genuine completions.** Two of the three implemented
items are expository completions (the S10 note; the abbreviations
list); the third (OP 4) is the Q1 stakeholder sentence. Beyond these,
the audit found the expository density already at ceiling: the paper
carries the minimax/game reading, the here-and-now/wait-and-see
identification, the value-of-information reading, the photograph/tube
pair, the ladder's ecological reading, the moderate-concentration-
beats-balance window, the doughnut-literature link, the transition-
finance instruments, and the Northern-cod data anchor. Further
additions would be decorative — declined.

**Q6 — clarity and flow scan.** Full read of v62's 3,268 lines. All 18
v61 insertion seams sit seamlessly (abstract opening; Section 1.1 canon;
Section 1.2 protocol reading; Section 5.2 acceptance-semantics paragraph
and threshold clause; conclusions paragraph; Section 6.3 decision-aiding
context). Register sweep: the only "family's" is the CES family's
defining property (mathematical usage); the only "no longer" is the
tubes' conservatism under depensation (mathematical statement) — both
legitimate. The new v62 insertions verified in place and seam-clean.
No conceptual-clarity defects found; no flow repairs warranted.

## The implemented operations

1. **Provenance (OP 1).** The v62 header comment added (the v61 line
   stands).
2. **Abbreviations completed (OP 2).** Seven entries, alphabetical:
   CES; DFO — Fisheries and Oceans Canada; LPI — Living Planet Index;
   LRP — limit reference point; MSY; NCAM — Northern Cod Assessment
   Model; PROMETHEE.
3. **Section 5.2 pointer (OP 3).** The Supplementary-Material pointer
   gains "and the acceptance-semantics reading of the protocols as
   decision-aiding sorting rules (Roy, 1996; Vincke, 1992)" —
   announcing the new S10 note.
4. **Section 6.3 stakeholder sentence (OP 4).** After the preference
   reading of the weights: "The two criteria are conflicting objectives
   --- each of the two principal schedules protects one at the expense
   of the other --- and each is defended by a distinct constituency, so
   the weight space reads both as an assessor's calibration and as the
   preference profile of the stakeholder dispute." Scope-safe
   (descriptive decision-aiding vocabulary; consistent with the
   translation table's "stakeholder weight elicitation" reading and the
   weights-versus-importance delimitation); completes the special
   issue's "multiple stakeholders and conflicting objectives"
   vocabulary in the paragraph that satisfies the venue's editorial
   requirement.
5. **Supplementary v12.** v11 + exactly one appended S10 note,
   "Acceptance semantics and decision aiding" (sorting problematic,
   Roy/Vincke; the licensing thresholds as the verdict's weight-
   sensitivity intervals — the preference ranges over which each plan
   is certified — the acceptance-side analogue of the Nardo et al.
   sensitivity analyses; the Keeney-Raiffa/Munda elicitation
   background; the static-vs-protocol delimitation against Cinelli et
   al. and Schär et al.). Byte-verified: v12 = v11 + the one paragraph;
   style-consistent with the other S10 notes.

## Gates (all green)

- **Inverse reconstruction:** reverting all 4 operations in reverse
  order reproduces v61 byte-identically.
- **Math-span multiset:** 1,470 → 1,470, zero delta — every operation
  is prose-level.
- **Marker accounting:** 10 new markers present, 1 retired marker
  absent.
- **Structure pins:** environments balanced and unchanged; the \item
  count grows by exactly +4 (the new abbreviation entries); all pinned
  headings intact.
- **Register sweep:** the 11 banned residues absent; venue register
  clean (no journal name/abbreviation/special-issue mention in the
  body; the single References occurrence is the Schär et al. 2025
  JMCDA entry).

## Compile battery (all green)

- Tectonic in place: exit 0; 54 pp (unchanged from v61); 0 errors; 0
  undefined references (no `??` in the PDF text layer).
- Overfull/underfull profile identical to v61 (112 console warnings
  both; the only overfull is the pre-existing 2.43091pt header box) —
  zero new boxes.
- Flat self-containment compile (tex + figs_p1 alone, scratch
  directory): exit 0, 54 pp.
- PDF text layer: all new markers render — the four abbreviation
  entries; the Section 5.2 clause; the Section 6.3 stakeholder
  sentence (one apparent miss was a regex parenthesis artifact in the
  search, verified present in context).
- VLM raster checks: page 21 (the acceptance-semantics clause, exact
  quote verified, clean typesetting), page 43 (the stakeholder
  sentence, exact quote verified, the decision-aiding paragraph reads
  continuously), page 46 (the abbreviations list: heading + six
  entries). The list now breaks 6/1 across pages 46–47 (the four new
  entries pushed PROMETHEE to page 47) — a standard list continuation
  at a page boundary, acceptable for the venue's free-format
  submission (production typesetting re-flows it).
- Abstract 263 words (limit 300); keywords 7 (the venue's limit) —
  both unchanged and compliant.

## Submission package state

`paper1_assessment_separation_v62.tex/.pdf` (54 pp) +
`paper1_supplementary_v12.md` +
`COVER_LETTER_paper1_assessment_separation_JMCDA_v1.md` — the JMCDA
special-issue package ("Better Decisions for a Better Tomorrow", 
deadline 31 January 2027). Open (carried, unchanged): the owner-side
Zenodo deposit-title refresh; the ECOMOD next-round flags; the SI
submission itself (owner action via the Wiley portal).

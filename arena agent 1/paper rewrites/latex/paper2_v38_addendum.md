# v38 — Pass A: reproducibility, abstract qualification, proof-collection wording

## Changes

1. **GAP 1 (reproducibility).** Section 8's coverage audit is now tied to an
   archived, self-contained script `paper2_coverage_audit.py`, which recomputes
   the 48-cell grid audit and regenerates Table 1 and Figure 1. Verified: it
   reproduces exactly the published counts (42 nonviable = 30 one-step + 12
   timing, 0 uncovered). The "Code availability" declaration, which previously
   (and contradictorily) stated "No code was used or produced", now points to
   the script at https://zenodo.org/records/22545740; "Data availability" now
   reads "No external data were used." The audit sentence's editorial verb
   "conceded" was replaced with "identified".
2. **GAP 2 (abstract qualification).** "finitely checkable in the finite-state,
   polyhedral, and finite-horizon cases" -> "finitely checkable in the
   common-action, fibre-certification, and finite-horizon forms" (the three
   certificates actually shown to be finitely checkable); abstract stays 262
   words (<= 265).
3. **GAP 9 (proof-collection wording).** Section 1.4 now reads "...the complete
   proofs of the Section 3 certificates, the expanded sufficiency review, and
   the auxiliary constructions are collected in the Supplementary Material; the
   results of Sections 7 and 9 are proved in the main text." The supplementary's
   S1 intro sentence was aligned ("complete proofs of the Section 3
   certificates (S1)").
4. **Restored the missing Section 6.3 heading** ("6.3 Relation to the
   estimation-tube programme"), which was referenced from three places (Section
   1.2, Section 5(b), and the supplementary) but had been absorbed into Section
   6.2 during the reorder.

## QA

- Main: 15 pages, 4 images, 0 `??`, no overfull, abstract 262 words.
- Supplementary: 12 pages, 3 images, 0 `??`.
- Numbering: Theorems 1-7, Propositions 1-9, subsubsections 3.1-3.6 all present
  and sequential; new Section 6.3 heading renders and its cross-references
  resolve.

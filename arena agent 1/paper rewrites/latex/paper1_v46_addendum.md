# v46 — alignment, tone, and delegation pass (with content-loss audit)

## Alignment (title / abstract / keywords / intro / sections)

- Title, keywords unchanged and verified current (*Aggregate Indices and
  Transition Safety: …*; keyword list already venue-neutral: sustainability,
  viability theory, robust control, scalarization, multi-criteria decision
  analysis, quantifier order, transition safety).
- **Abstract** extended by one sentence (benchmark realization, exact
  rational verification, unit anchoring to a regulated biomass limit,
  terminology guide): 233 words, within the 265-word limit.
- Intro contribution list now references Proposition 10 by number.
- Section cross-references verified after the v45 renumbering (5.3
  translation guide; rescue/data subsection now 5.6).

## Tone / over-hedging pass (scan: metaphor apologies, reader-directed
meta, informal run-ins)

- "We emphasize what the instantiation is and is not …" rewritten as one
  formal scope sentence; the duplicated scope clause in the data-anchor
  paragraph removed ("Three caveats keep the claim honest" → "Three
  qualifications apply", with the repeated disclaimer merged). One scope
  statement per location; legitimate scope statements retained.
- Run-ins formalized: "What the abstraction buys a modeller." → "The case
  for the abstraction."; "What the reader should see." → "The dashboard
  reading."
- No diary/change-log/self-praise patterns found in the rendered text
  (the version header comment is source metadata only, not rendered).

## Numbering defect fixed

- The rescue-threshold proposition was unnamed ("Proposition (rescue
  threshold)"); numbered **Proposition 10** (next in the paper-wide
  sequence after Proposition 9), with the contribution-list reference
  updated.

## Delegation to supplementary (new S10)

- Section 5.2's per-literature exegesis (commensurability foundation,
  maximin/indicator formulations, compensability mapping) moved to new
  **Supplementary S10**; the main text keeps the condensed positioning with
  **all citations intact** and a pointer to S10. The Supplementary Material
  pointer now lists S10.

## Supplementary v10 (aligned to v46)

- **Title fixed**: the supplementary still carried the superseded title
  ("The Limits of Compensatory Aggregation"); now carries the current title.
- **Archive pointer fixed**: S7 still pointed to the Zenodo preprint record
  for the verification code; now points to the figshare deposit
  (10.6084/m9.figshare.33764023) and notes the benchmark script.
- Cross-references updated to the renumbered main text (5.5 → 5.6).
- S9 gains the regulated-instance note (Northern cod LRP = 884.6 kt;
  DFO, 2016) consistent with the main text's data anchor.
- New S10 (delegated positioning notes).

## Content-loss audit (v29 → v46, plus supplementary v9 → v10)

- Section/subsection titles: all present (differences are the EMA-driven
  Declarations renames and the Figures-subsection consolidation).
- Manual theorem/proposition/remark numbering: identical sets (Propositions
  3, 4, 9 + new 10; Remarks 1, 2, 6; Theorems 5, 7, 8; Theorem 6 in env
  form).
- References: all v29 entries retained; the only form change is the
  standing rule's replacement of "Abaee (2026a/b/c)" shorthand with full
  titles and DOIs (plus the later additions: figshare data citation, DFO
  2016, De Lara–Doyen 2008, Rockström et al. 2009, Raworth 2012,
  Schaefer 1954).
- Figures: 1 (v29) → 4 (v46), no losses.

## QA

- Compile exit 0; 33 pages; 4 images; 0 `??`; overfull only the
  pre-existing 2.43 pt frontmatter box; abstract 233 words.
- Supplementary v10: 0 occurrences of the old title; 0 occurrences of the
  Zenodo record; 25 changed lines total vs v9 (surgical).

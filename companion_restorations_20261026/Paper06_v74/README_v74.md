# Paper06 v74 — source-checked prose and full-cone axis clarification

**Title:** *Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules*

**Date:** 2026-10-27

**Parent:** Paper06 v73, preserved unchanged. V74 is a new source-edited derivative; it inherits the v73 Figure 2 correction.

## Scope

V74 implements the source-checked revision plan selectively. It improves the opening and the definitions of the two acceptance semantics, makes the coordinate-axis weight cases explicit, and updates current-edition references. The paper's model, parameters, mathematical results, proofs, and numerical results are unchanged; Theorem 2's prose is clarified to state the weight-ratio domain and axis cases. Table 1 and the figure assets are retained; the prior general motivating paragraph after Table 1 is replaced by one witness-based example after the formal definitions, rather than duplicated.

## Deliverables

- [`paper06_assessment_separation_v74.pdf`](paper06_assessment_separation_v74.pdf) — main article, 48 pages.
- [`paper06_assessment_separation_v74.tex`](paper06_assessment_separation_v74.tex) — assembled main source.
- [`paper06_assessment_separation_v74_supplementary.pdf`](paper06_assessment_separation_v74_supplementary.pdf) — Supplementary Information, 40 pages.
- [`paper06_assessment_separation_v74_supplementary.tex`](paper06_assessment_separation_v74_supplementary.tex) — assembled SI source.
- [`paper06_assessment_separation_v74_src/`](paper06_assessment_separation_v74_src/) — editable TeX parts, figures, and figure scripts. The v73 Figure 2 and all other figure files are byte-identical to v73.
- [`CHANGELOG_v73_to_v74.md`](CHANGELOG_v73_to_v74.md) — exact scope and build/audit results.
- [`IMPLEMENTATION_RECORD_v74.md`](IMPLEMENTATION_RECORD_v74.md) — plan-to-source disposition and verification record.
- [`EDITORIAL_ASSESSMENT_AND_REVISION_PLAN.md`](EDITORIAL_ASSESSMENT_AND_REVISION_PLAN.md) — the source-checked assessment and advisory plan, updated to record that selected recommendations were implemented in v74, not copied verbatim.
- [`CHANGELOG_v72_to_v73.md`](CHANGELOG_v72_to_v73.md) and [`CHANGELOG_v71_to_v72.md`](CHANGELOG_v71_to_v72.md) — inherited release history; both describe earlier editions.

## Main changes

- **§1.1:** Opens with the compensability question, preserves the existing literature citations, and distinguishes fixed-profile aggregation from the transition-certification question without claiming a general gap in the literature.
- **§1.2:** Defines the finite menu, declared disturbance set, typed margins, and common physical safe and destination sets. Both `E_w` and `E_typ` retain those same physical, destination, and universal-disturbance requirements; the aggregate or typed floor test applies on every tube state and successor state. The quantifier distinction and full-cone identity are then stated explicitly.
- **Motivating example:** Retains Table 1 and replaces the former generic public-authority example with a source-bounded example from the four-plan witness, after the formal definitions.
- **Witness and notation:** For `w₁>0`, the ratio `r=w₂/w₁` is now scoped explicitly; `(1,0)` and `(0,1)` are classified separately. The theorem wording preserves the exact thresholds, overlap, and “among the two principal plans” qualification. The notation row records the extended ratio at `w₁=0<w₂`.
- **Pagination and edition references:** The definition block and contribution-list boundary are typeset cleanly; the witness-point summary is concise; a float barrier keeps Figures 2–3 before the persistence result rather than splitting it. Main/SI headers, version strings, and package paths identify v74.

## Build and validation

Built from this directory with **Tectonic 0.17.0**:

```sh
tectonic paper06_assessment_separation_v74.tex
tectonic paper06_assessment_separation_v74_supplementary.tex
```

The main and SI PDFs are 48 and 40 pages. Extracted text contains no unresolved `??` markers. The SI text is identical to v73 after normalising the edition label; its 9 hyperlink annotations have the same URL targets as v73. The main PDF's 12 hyperlink annotations likewise retain the v73 URL-target multiset. The captured TeX warning signatures match the same-engine v73 baseline after normalising source filenames and line numbers; the existing layout warnings remain, with no new warning signature. The revised and flow-affected main pages (2–36) were visually checked, including the notation table, witness theorem, and figure/table pages; a float barrier keeps Figures 2–3 before Proposition 3. The inherited Figure 2 remains on page 17 with its equality labels horizontal and above the diagonal.

## Preservation and release discipline

Paper06 v73 and all earlier releases remain unchanged. This edition has no new DOI deposit. No checksum registry, ECOMOD c10 or its pins, c8/c9, `main`, or prior release was changed. V74 is published as a separate directory on the archive branch; the immutable commit is the version pin.

# Paper06 v75 — Gemini-based prose revision

- **Date:** 2026-10-27
- **Parent:** Paper06 v74, preserved unchanged. V75 is a separate derivative and inherits v73’s Figure 2 correction.

## Scope

V75 implements the revised prose plan in §§1.1–1.2. Gemini’s supplied humanized drafts are the sentence-level prose base; Grok’s strongest contributions are used as targeted precision checks, not as the voice or structural template. The claims, definitions, citations, and qualifications were checked against the v74 manuscript. The abstract, theorem statements, proofs, model, parameters, numerical results, and SI substantive text are unchanged.

The rewrite retains Gemini’s direct opening question, the progression from fixed profiles to transitions, and its plain-language explanation of the plan/weight fork. It corrects the overbroad “literature-wide blind spot” and unsupported real-world or promotional claims. In §1.2, the common physical-safety, destination, and disturbance requirements are explicit for both operators; the weighted or typed floor is checked over the full tube and successor set. The exact quantifier domains and full-cone identity are stated, Table 1 is retained, and the example is tied to the action-indexed four-plan witness.

## Deliverables

- [`paper06_assessment_separation_v75.pdf`](paper06_assessment_separation_v75.pdf) — main article, 48 pages.
- [`paper06_assessment_separation_v75.tex`](paper06_assessment_separation_v75.tex) — assembled main source.
- [`paper06_assessment_separation_v75_supplementary.pdf`](paper06_assessment_separation_v75_supplementary.pdf) — Supplementary Information, 40 pages.
- [`paper06_assessment_separation_v75_supplementary.tex`](paper06_assessment_separation_v75_supplementary.tex) — assembled SI source.
- [`paper06_assessment_separation_v75_src/`](paper06_assessment_separation_v75_src/) — editable TeX parts, figures, and figure scripts.
- [`CHANGELOG_v74_to_v75.md`](CHANGELOG_v74_to_v75.md) — exact changes and verification summary.
- [`IMPLEMENTATION_RECORD_v75.md`](IMPLEMENTATION_RECORD_v75.md) — source mapping, build and audit record.
- [`EDITORIAL_REVISION_PLAN_v75.md`](EDITORIAL_REVISION_PLAN_v75.md) — corrected plan and implementation scope.
- [`EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md`](EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md) — historical v74 claim audit and plan; its earlier stylistic hierarchy is superseded by the v75 plan.
- The inherited v71→v72, v72→v73, and v73→v74 changelogs and the v74 README/implementation record are retained as historical records.

## Build and validation

Built from this package with **Tectonic 0.17.0**. Main/SI page counts remain 48/40. There are no unresolved `??` markers, undefined references, missing-file errors, or fatal build errors. The main PDF has 12 URI links and the SI 9; their URL-target multisets match v74. After replacing the edition label `v75` with `v74`, SI extracted text matches v74 exactly. Main-text differences after that normalization are confined to the revised opening on pages 2–3. The normalized warning-signature multisets match v74 (46 main and 69 SI warnings); existing warnings remain and are not represented as absent. Pages 2–4 were visually inspected; the revised opening and quantifier explanation fit cleanly, and Table 1 and the contributions boundary remain intact.

## Preservation and release discipline

V74 and all earlier releases remain unchanged. V75 is published as a separate directory on `archive/ecomod-companion-restorations-2026-10-26`; no DOI deposit, checksum registry, `main`, ECOMOD c10 or its pins, c8/c9, or prior release was changed.

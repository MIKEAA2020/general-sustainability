# Paper06 v75 — implementation and verification record

- **Date:** 2026-10-27
- **Parent release:** Paper06 v74, immutable archive commit `6e4a1fdeb374e22fe31fe9e64587f3a450353e1d`.
- **Implementation scope:** New source-edited derivative; v74 and earlier releases are preserved unchanged.
- **Plan:** [`EDITORIAL_REVISION_PLAN_v75.md`](EDITORIAL_REVISION_PLAN_v75.md); the source-checked v74 claim audit is retained in [`EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md`](EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md).

## Gemini-base mapping and source checks

| Gemini material | V75 treatment | Source check / reason |
|---|---|---|
| Opening question: can strength in one area make up for failure in another? | Retained as the opening sentence of §1.1, with only light adaptation to the paper’s transition context. | It frames the existing compensability question without adding an empirical claim. |
| MAVT/outranking contrast and weak/strong sustainability | Retained in readable prose, with the paper’s original citation set. | Claims were checked against the v74 literature framing; no generated claims about all MCDA methods or capital stocks were added. |
| “Static snapshots” versus dynamic transitions | Retained as the transition from fixed profiles to the paper’s path-wise question. | “Much of this work” replaces Gemini’s broader “almost this entire body” claim; the manuscript’s scope remains transitions under declared disturbances. |
| Weight calibration, static Pareto limitation, acceptance semantics | Kept as three distinct questions, in direct prose. | Existing citations and scope are retained; the result is framed as a certification-rule result, not a general attack on composite indices. |
| Transition datum and exact-tube explanation | Used as the explanatory sequence, with common physical-safe and destination conditions added. | Both `E_w` and `E_typ` require physical safety, destination attainment, and every declared disturbance; aggregate or typed floors are tested on the full tube and successor set. |
| Quantifier fork and “some plan may differ” explanation | Retained and formalized with complete domains and set-membership predicates. | `W_+` is the full nonnegative cone with zero excluded, including axis weights; the full-cone identity and common-plan equivalence to typed-plan existence are stated. |
| Here-and-now / wait-and-see analogy | Retained as an analogy for quantifier order, with an explicit limit on its interpretation. | It is not presented as evidence about actual auditor or policymaker behavior. |
| “Chameleon Dashboard,” invented service scenario, 100% clean bill, disaster, and generic/never claims | Not carried over. The introduction instead uses the paper’s four-plan action-indexed witness. | The example is bounded to `(x,s₁,s₂)=(1/2,6/5,6/5)`, where `s₁+s₂=12/5≥2`; every weight licenses FAST or SLOW, while no plan in the declared menu is typed-admissible. This is not generalized to real-world menus. |

Grok’s strongest features were used as precision checks—especially the plan/weight quantifier distinction, compact definitions, source-near literature framing, and the menu-relative verdict. Grok was not used as the prose base.

## Changed source scope

- `paper06_assessment_separation_v75_src/parts/00_front.tex` — Gemini-based §§1.1–1.2 text and witness paragraph, plus v75 header/path references.
- `paper06_assessment_separation_v75.tex` — assembled main source synchronized with the modular front matter; v75 edition/file references.
- `paper06_assessment_separation_v75_src/parts/07_refs.tex`, `si_00_front_proofs.tex`, and `si_03_verification_positioning.tex` — current-edition and file-label updates only.
- `paper06_assessment_separation_v75_src/work/edit_fig_witness_triangle_labels.py` — package-root path/comment updated to v75.
- `paper06_assessment_separation_v75_supplementary.tex` — v75 edition/file references only.
- All other source parts and all seven figure assets are unchanged from v74. The assembled and modular §1.1–1.2 blocks match exactly.
- The v74 README and implementation record, and the v74 claim-audit plan, are retained as explicitly named historical records. The new v75 plan supersedes the v74 stylistic hierarchy.

No theorem statement, proof, assumption, model, parameter, citation target, or numerical result was changed.

## Build and PDF audit

- **Engine:** Tectonic 0.17.0; build output/logs were kept under `/tmp` and are not included in the package.
- **Page counts:** main 48; SI 40, matching v74.
- **Build checks:** no unresolved `??` markers, undefined-reference messages, missing-file errors, or fatal build errors.
- **Hyperlinks:** main has 12 URI annotations and SI has 9; both target multisets match v74.
- **Extracted text:** SI matches v74 exactly after normalizing `v75` to `v74`. In the main PDF, after that normalization, only pages 2–3 differ; later article text is unchanged.
- **Warnings:** after normalizing source filenames and line numbers, warning-signature multisets match v74 exactly: 46 main and 69 SI warnings. Existing underfull/overfull warnings remain; none was suppressed or described as absent.
- **Visual review:** main pages 2–4 were inspected. The revised prose and formal definitions fit without clipping or awkward interruption; Table 1 remains intact and the contributions section starts cleanly after it.
- **Figures:** all seven figure files are byte-identical to v74.

## Release boundary

The v75 directory was added separately to `archive/ecomod-companion-restorations-2026-10-26`. The push was performed through GitHub’s Git Database API, without materializing a repository working tree. The remote archive head and `main` were checked after publication. No earlier release, DOI deposit, checksum registry, ECOMOD c10 or its pins, c8/c9, or `main` was changed.

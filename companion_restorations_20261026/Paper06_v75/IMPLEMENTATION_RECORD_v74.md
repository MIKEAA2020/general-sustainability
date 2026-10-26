# Paper06 v74 — implementation and verification record

**Date:** 2026-10-27

**Parent release:** Paper06 v73, immutable commit `99ebea2728660d88047a2388ceed545788e09ca0`; preserved unchanged.

**Plan source:** [The original v73 plan](../Paper06_v73/EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md); a status-updated copy is also included in this v74 package at [`EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md`](EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md). The plan's proposed copy was used as editorial guidance, not transplanted verbatim.

## Implementation decisions

| Plan item | V74 disposition | Source check / qualification |
|---|---|---|
| Open with the question of compensability; distinguish a fixed criterion profile from a transition-certification rule. | **Implemented** in §1.1. | Existing citation keys were retained. The rewrite avoids claims that prior sustainability or decision-analysis literature missed the issue. |
| Define the shared physical, destination, and disturbance conditions before contrasting the two assessments. | **Implemented** in §1.2. | Both `E_w` and `E_typ` require physical safety and destination attainment for every declared disturbance; the aggregate or typed floor is checked at every tube state and successor. This matches the operators in `parts/01_setting.tex`. |
| Put the plan/weight quantifier orders adjacent, explain the full-cone identity, and retain the protocol table. | **Implemented.** | The full-cone coordinate weights recover each typed floor; common-plan acceptance remains exactly typed-plan existence. Table 1 is retained, unchanged in content. |
| Use a bounded motivating example only after the formal definitions; avoid duplicating the table. | **Implemented.** | The former generic public-authority paragraph after Table 1 was replaced by one witness-based example. It identifies the roles of FAST, SLOW, STAGED, and NO-SWITCH and explicitly limits the result to the declared datum/menu. |
| Preserve the finite-menu theorem's assumptions and path-maximisation/scalarisation order. | **Preserved and signposted.** | No theorem or lemma's mathematical result, assumptions, or proof changed. Theorem 2's prose is clarified for the ratio domain and coordinate-axis weights. The contribution wording remains limited to destination-feasible margin-class plans and the synchronization lemma's stated continuous-path assumptions; it does not say that every finite menu has a gap. |
| State exact witness thresholds and handle axes in the full nonnegative cone. | **Implemented.** | For `w₁>0`, `r=w₂/w₁`; the FAST/SLOW thresholds and overlap remain explicit. `(1,0)` licenses SLOW but not FAST; `(0,1)` licenses FAST but not SLOW, among the two principal plans. The notation row gives `r=+∞` when `w₁=0<w₂`. These cases match Theorem 2's aggregate inequalities and its coordinate-axis weights. |
| Keep the reserve threshold's full typed-failure domain and distinguish `Q`, rescue `R`, and gap `I`. | **Preserved.** | The contribution still gives `κ*(z)=(1−x)_+ 1[z∉V_typ]`; the gap remains `I`, not all of `Q` or all typed failures. |
| Keep the remedy and robustness qualifications. | **Preserved.** | Blending remains limited to the action-indexed class; the shared-shock gap is not described as blend-closed; full-depth alternation is distinguished from arbitrarily fine duty cycling. CES intervals remain limited to the witness-defined diagonal gap slice, and the DFO figures remain context-only. |
| Rebuild, compare, inspect, and record. | **Completed.** | Details below. No Lean/formal-verifier or independent numerical-check rerun was needed or claimed: only prose clarifications were made; no formal statement's mathematical content, proof, model, or numerical result changed. The new wording was checked against the source definitions and witness inequalities. |

## Changed source scope

The only changed files inside the editable source bundle are:

- `parts/00_front.tex` — §§1.1–1.2, witness-led example, and the coordinate-axis note in the contribution list.
- `parts/01_setting.tex` — notation-row domain for the extended weight ratio.
- `parts/03_witness.tex` — weight-ratio scope, axis cases, theorem note, a concise witness-point recap, and a float barrier before the persistence subsection.
- `parts/07_refs.tex` — current-edition references only.
- `parts/si_00_front_proofs.tex` and `parts/si_03_verification_positioning.tex` — v74 edition labels only.
- `work/edit_fig_witness_triangle_labels.py` — package-root path/comment only.

The assembled main and SI TeX files carry those changes plus v74 headers and output paths. A block comparison confirmed that the revised §§1.1–1.2 in the modular source and assembled main TeX are identical; the revised notation row and witness-axis clause also occur identically in both. A source-tree comparison found no other changed source parts. All seven figure files are byte-identical to v73, including the corrected Figure 2.

## Build and PDF audit

- **Engine:** Tectonic 0.17.0.
- **Builds:** `paper06_assessment_separation_v74.tex` and `paper06_assessment_separation_v74_supplementary.tex` both build successfully.
- **Page counts:** main 48; SI 40. Same-engine v73 comparison copies also build at 48/40 pages.
- **Text extraction:** zero `??` markers in either v74 PDF; no undefined-reference, missing-file, or fatal-error marker in the captured build logs. SI extracted text is exactly identical to v73 after normalising the edition string `v74` to `v73`.
- **Hyperlinks:** main 12 URI annotations and SI 9; each URI-target multiset matches v73 exactly.
- **Layout warnings:** the captured v74 logs contain 46 main and 69 SI warning occurrences, including warnings repeated during TeX passes. After normalising source filenames and line numbers, their warning-signature multisets match the same-engine v73 baseline exactly. The existing underfull/overfull box warnings remain; none was suppressed or represented as absent.
- **Visual review:** main pages 2–36 were inspected at rendered-page scale, with a closer check of the revised opening, Table 1/contribution boundary, notation table, witness theorem, Table 5, and Figures 2–5. The definition block starts cleanly on the next page rather than splitting a sentence; the contribution list starts at a clean boundary; the witness-point recap no longer breaks after a colon. A float barrier keeps Figures 2–3 ahead of the persistence subsection, so they no longer interrupt Proposition 3. Figure 2 remains on page 17, and its equality labels remain horizontal above the diagonals. After edition-label normalisation, extracted main-page text is identical to v73 from page 37 onward; earlier differences reflect the revised wording and resulting pagination, not source changes to later sections.

The v73 baseline used for comparison was built from a temporary copy under `/tmp/Paper06_v73_baseline/`; the workspace v73 release was not rebuilt over or altered.

## Release boundaries

V74 is a source-edited manuscript derivative, not a DOI deposit. No earlier Paper06/Paper3/Paper4 release, ECOMOD c10 or its pins, c8/c9, checksum registry, or `main` branch was changed. The v74 directory was published separately on the archive branch.

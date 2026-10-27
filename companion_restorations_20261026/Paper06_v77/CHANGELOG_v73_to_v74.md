# Changelog: Paper06 v73 → v74

## Scope and parent

- Preserved Paper06 v73 unchanged; created v74 as a separate, source-edited derivative.
- Applied selected, source-checked parts of the editorial plan. V74 is not a wholesale or verbatim adoption of the proposed §§1.1–1.2 copy; the actual wording follows the manuscript's notation and theorem domains.
- No model, disturbance class, parameter, underlying theorem result, proof, numerical result, or literature citation was added or changed. Theorem 2's statement prose was clarified for the `w₁>0` ratio domain and the two coordinate-axis cases. The v73-corrected Figure 2 and all other figure assets are byte-identical to v73.

## Manuscript changes

1. **§1.1 — framing and literature context.** Rewrote the opening around the compensability question; retained the existing citation set; distinguished fixed-profile aggregation from the paper's transition-certification question; and avoided a claim that prior literature has a general blind spot.
2. **§1.2 — common constraints and quantifier order.** Replaced the compressed definition with an explicit transition datum: finite plan menu, typed-margin vector, declared disturbance class, common physical safe set, and destination set. Both `E_w` and `E_typ` carry the same physical, destination, and universal-disturbance conditions. Their respective aggregate and typed tests apply to every tube state and successor state. The full-cone identity and the two quantifier orders are stated alongside the retained Table 1.
3. **Motivating example.** Removed the former generic public-authority paragraph after Table 1 and added one bounded example from the declared witness menu after the formal definitions. It retains the roles of FAST, SLOW, STAGED, and NO-SWITCH and does not imply that the menu is observed policy.
4. **Witness weights and notation.** Theorem 2 now says that `r=w₂/w₁` is used when `w₁>0`; reports the exclusive and overlap ranges for the two principal plans; and separately classifies `(1,0)` and `(0,1)`, explicitly limiting that comparison to the two principal plans. The theorem note and notation row repeat the domain guard and specify `r=+∞` for `w₁=0<w₂`. The contribution list now records that the axis weights are classified separately.
5. **Witness-point recap and layout.** Shortened the recap after Theorem 2 without changing its numerical content. Kept the formal-definition block together, started the contribution list at a clean boundary, and placed a float barrier before the persistence subsection so Figures 2–3 do not interrupt Proposition 3.
6. **Edition references.** Updated main/SI edition headers, supplementary-file references, current-edition citations, and the editable Figure 2 script's package-root path from v73 to v74. The SI result-map table now labels the main-text numbering as v74.

## Explicitly unchanged

- Table 1 is retained; it was not duplicated or removed.
- The finite-menu theorem and its synchronisation lemma are unchanged. The contribution wording retains the margin-class, destination, and path-maximisation/scalarisation qualifications.
- The reserve threshold remains defined over the full typed-failure set, not only the aggregate-accepted gap. The witness distinction `Q=R∪I` is preserved, with `I` as the gap and `R` as the rescue set.
- The blend result remains action-class-specific; the shared-shock qualification, full-depth alternation limitation, and different duty-cycling class remain distinct.
- CES interval claims remain limited to the witness-defined diagonal gap slice; the Leontief-only uniform-safety claim remains limited to the full gap. The DFO fishery values remain a limited scale/context anchor, not a fit, forecast, validation, or performance claim.
- The Supplementary Information's substantive text is unchanged; only v74 edition/file references are updated.

## Build and audit

- Built main and SI with Tectonic 0.17.0 from the v74 package root.
- Main PDF: **48 pages**. SI PDF: **40 pages**.
- Extracted main and SI text contain no `??` markers. The SI text matches v73 exactly after normalising `v74` to `v73`.
- Main hyperlink annotations: 12; SI: 9. Their URI target multisets match v73 exactly.
- Captured Tectonic logs: 46 main and 69 SI warning occurrences, including repeated passes. After normalising source filenames and line numbers, the warning-signature multisets match the same-engine v73 baseline exactly; no new warning signature was introduced.
- The source parts and assembled main TeX agree on the revised §1.1–1.2 block, notation row, and witness-axis clause. A source-tree comparison found only the intended changed parts and edition-path/reference updates; all figure files match v73 byte-for-byte. The staged change is confined to the new v74 directory, and `git diff --cached --check` passes.
- Visually inspected the changed and flow-affected main pages, pages 2–36. The revised prose, notation row, witness theorem, and table/figure placements are legible; the float barrier keeps Figures 2–3 before Proposition 3. Figure 2 remains on page 17 with both `s₁+s₂=2` labels horizontal and above their diagonals. After edition-label normalisation, extracted main-page text is identical from page 37 onward; earlier differences reflect the revised wording and consequent pagination, not source changes to later sections.

## Release discipline

- No DOI deposit was created or refreshed.
- No prior Paper06 edition, Paper3/Paper4 release, ECOMOD c10 or its pins, c8/c9, checksum registry, or `main` branch was changed. V74 is a new directory on the archive branch.
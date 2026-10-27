# Changelog: Paper06 v75 → v76

**Parent:** Paper06 v75 at archive commit `0208f8b1523446a32ef48cbfe50415fe7ec78947`. V75 is preserved unchanged; v76 is local-only.

## Source-verified corrections

- **Witness notation:** Replaced the literal tab after `r=` with the TeX command `\tfrac12`. The prior v75 PDF visibly printed `frac12`; the rebuilt v76 PDF displays the intended one-half value.
- **Abstract:** Clarified that the witness’s unnormalised equal-weight margin sum `12/5` exceeds the licensing threshold `2`, so the comparison is explicit in the abstract.
- **§6.4 bridge:** Added a concise sentence explaining that the four novelty claims regroup the five contributions listed in §1.3.
- **Archive locator:** Added the exact GitHub commit and a direct link to the v75 package containing its source files and PDFs: `0208f8b1523446a32ef48cbfe50415fe7ec78947`.
- **Theorem 4 and SI proof:** Restricted the finite-rung/positive-tube conclusion to the deep interior, `1 < s_1 < 2` and `1 < s_2 < 2`. Clarified that gap states with `min(s_1,s_2) <= 1` are accepted only by the linear member, rather than calling all such states boundary states. The theorem’s mathematical conditions and conclusions are unchanged.
- Updated active-edition labels and file paths to v76. The assembled main/SI sources and their edited modular parts are synchronized.

## Unchanged scope

No model, assumptions, theorem math, proof result, parameters, numerical results, citations, acknowledgments, or figure artwork were changed. All seven figure files—including Figure 2—are byte-identical to v75. No DOI deposit or Git push was made.

## Validation

- Built main and SI with Tectonic 0.17.0: **49** and **40** pages, respectively.
- Both builds completed and produced PDFs. No unresolved `??` markers, unresolved references/citations, missing-file errors, or fatal build errors were found.
- Non-fatal TeX warnings remain (underfull/overfull boxes, font/PDF-string warnings, and one SI float-size warning); they were not suppressed. Temporary build logs are not included in the package.
- The main PDF contains the direct v75 archive link. PDF text and hyperlink annotations were checked; the main PDF has 14 URI annotations (9 unique destinations) and the SI has 9 (5 unique destinations).
- Visually reviewed main pages 1, 16, 24, 32–33, 42, and 49, and SI pages 5 and 40. In particular, the corrected fraction renders properly, the bridge ends cleanly before the claims, and the theorem/SI deep-interior wording is legible.
- The seven figure assets were compared byte-for-byte with v75. Edited assembled and modular source passages were checked for exact synchronization.

V76 remains local pending the user’s separate post-QA release decision.

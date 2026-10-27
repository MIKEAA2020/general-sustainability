# Paper06 source-correction plan — v76

**Status:** Implemented locally in Paper06 v76. Paper06 v75 and all earlier releases remain unchanged.

**Parent:** Paper06 v75, archived at commit `0208f8b1523446a32ef48cbfe50415fe7ec78947`.

## Purpose and scope

V76 is a narrow, source-checked correction pass—not a prose rewrite. Apply only changes supported by the manuscript source or confirmed by the rendered v75 PDF. Preserve all mathematical results, model assumptions, data, citations, acknowledgments, and artwork.

### Approved corrections

1. **Repair the witness’s TeX token.** The assembled main source and modular witness part contain an actual tab after `r=` followed by `frac12`; the v75 PDF confirms the malformed rendering. Replace it with `\tfrac12` in both sources.
2. **Clarify the abstract’s threshold comparison.** State explicitly that the unnormalised equal-weight margin sum `12/5` exceeds the witness’s licensing threshold `2`.
3. **Bridge §1.3 and §6.4.** The manuscript lists five contributions in §1.3 and four novelty claims in §6.4. Add one concise sentence explaining that the four claims regroup the five contributions.
4. **Provide an archive locator.** Link directly to the v75 package at commit `0208f8b1523446a32ef48cbfe50415fe7ec78947`, where its source and PDFs are preserved.
5. **Correct Theorem 4/SI scope language.** The gap region’s strict interior is broader than the set on which every primitive plan has positive tube ratios. State the finite-rung conclusion on the deep-interior subset (`1 < s_1 < 2`, `1 < s_2 < 2`); clarify that `min(s_1,s_2) <= 1` describes gap states accepted only by the linear member and is not synonymous with a boundary state. Do not change the theorem’s math.

## Synchronization and QA gates

- Keep the assembled main/SI TeX and edited modular source parts synchronized.
- Confirm the tab is gone and `\tfrac12` compiles and renders correctly.
- Build both PDFs; inspect relevant text, links, and page layouts; scan for unresolved references, missing files, fatal errors, and `??` markers.
- Compare all figure assets with v75 and preserve the v75 package unchanged.
- Keep this derivative local. **Do not push or deposit it** without separate authorization after QA review.

## Implementation record

Completed changes and QA results are recorded in [`IMPLEMENTATION_RECORD_v76.md`](IMPLEMENTATION_RECORD_v76.md) and summarized in [`CHANGELOG_v75_to_v76.md`](CHANGELOG_v75_to_v76.md).

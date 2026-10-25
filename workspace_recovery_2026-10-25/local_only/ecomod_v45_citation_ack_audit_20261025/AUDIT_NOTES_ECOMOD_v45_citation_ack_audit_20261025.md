# Audit findings: companion references and readability — 2026-10-25

## Companion-paper currency and titles

I checked the current advertised branches and tags rather than treating `main` or the largest number in one filename as sufficient. The remote refs were unchanged during this check; `main` is `2efaa62083f2007dec3446c15c475af88f0925f3`.

| ECOMOD key | Current companion | Finding and disposition |
|---|---|---|
| `Abaee2026a` | Paper4 delay dynamics, **v41** | Current title remains *Governance delay and the stability of harvested stocks: mobilising and protective feedback rules, and the review interval as a design parameter*. This title is accurate and the ECOMOD entry already had it. v41 is the latest located version across the relevant branches. The old linked PDF at `c1168a…` has the same Git blob as v41 at current `main`; the refreshed entry points to the current pinned tree and labels v41. |
| `Abaee2026b` | Assessment separation, **Paper06 v71** | This is the current successor in the paper1 v62/v63 → Paper06 v64–v70 → v71 lineage. The paper1 v64 rewrite is explicitly marked superseded because it was based on a stale ancestor. The current title is *Aggregation is a claim, not a presentation: the geometry of the acceptance gap between compensatory and noncompensatory transition assessment*. ECOMOD's old v59 title/link should be replaced. The old `Lemma A` / `Theorem S2(ii)` locators do not identify the current main-text result; the relevant current locators are Sections 2 and 4, Theorem 2 (witnessed separation), and Theorem 4(iii) (the substitutability ladder's uniform result). The manuscript now limits the uniform-safety statement to the specified acceptance-gap region. |
| `Abaee2026c` | Material-ledgers, **Paper3 v50** | The full-length v50 title remains *Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons*. The title in ECOMOD was already correct, but its v32 URL was stale; it now points to the v50 PDF. The shorter title used in a journal-targeted cut refers to that different cut, so it was not substituted for the full-length v50 title. |

The reference links are pinned to the current `main` commit `2efaa62083f2007dec3446c15c475af88f0925f3`. The v41, v50, and v71 PDF and TeX blobs were checked across the relevant `main`, `e2-v3-source-year`, and recovery trees and match byte-for-byte; the archived Paper3 branch contains v49.

### Separate Paper3 v50 metadata item

The current tree contains Paper3 v50 Markdown, TeX, and PDF; the 54-page PDF title and updated companion-reference text were checked. Its parent `README.md` / `CHECKSUMS.sha256` still describe/list v49, and the v50 TeX header still says it was typeset from the v48 Markdown file. This does not change the title or the pinned v50 PDF, but the Paper3 package metadata should be refreshed before it is treated as a fully reconciled release. I have not edited the companion paper as part of this ECOMOD task.

## Readability and overcorrection audit

The comparison used the current v45 source, the archived v45 readability package, v44 acknowledgment wording, and the v42 source. The user's previously identified P0 corrections and terminology restorations remain in place; the current title choice also remains unchanged.

Two additional abstract-level overcompressions were clear enough to correct:

1. **Conversion trigger:** “available fast-land supply” narrowed the model's trigger incorrectly. The shortfall is based on the supply available to people from both land contributions (with the declared shares), not fast land alone. The abstract now says “the supply available to people falls short of demand.”
2. **Balance-point wording:** “the model has one balance point” followed by an above-threshold floor approach blurred the distinction between the unique feasible balance branch and demand above its ceiling. The abstract now says “at most one,” places the curve-floor meeting at the baseline ceiling, and separately states that area approaches the floor above it.

The full orchard/two-book explanation and the elevator analogy's no-fold caveat are retained, as are “aggregate,” “heuristic,” and “diagnostic,” the named composition diagnostic and its premium/neutrality/discount regimes, and the distinct composition and liquidation masks. The v42 Divisia material remains in the SI, while the current main text keeps the data-vintage and account-versus-physical-stock limits explicit. I found no other omitted passage that should be restored solely for readability. In particular, I did not reinstate v42's broad “no sustained boom–bust cycle” or Allee-threshold negatives: the current text scopes claims to the reduced model and reported range rather than presenting those as general results for the coupled system.

## Build verification

Tectonic 0.17.0 produced a 34-page main manuscript and a 20-page SI. All bibliography keys resolve, the updated Paper06 title and current locators appear in the PDFs, the restored acknowledgment appears on the final pages, and no `??` or obsolete v59 reference remains. The build has no errors or unresolved references; the non-fatal overfull/underfull box warnings are recorded in the build logs.
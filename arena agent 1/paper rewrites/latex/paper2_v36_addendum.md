# v36 — equation-tag ordering fix (found by final re-verification)

## The defect

The Section 3 reorder left the hardcoded equation tags out of reading order.
The tagged displays appear physically as (2) [Section 3.2], (3),(4) [Section
3.3], (1) [Section 3.5], (5) [Section 4] — so equation (1) was reached after
(2), (3), (4). In-text references were hardcoded and had to follow.

## The fix (main text only)

| old | meaning | new |
|-----|---------|-----|
| (1) | finite-time-exit drift condition (H1.1) | (4) |
| (2) | common-action safety obstruction (H3.2) | (1) |
| (3) | delayed-information drift (H4.2) | (2) |
| (4) | delayed-information timing bound (H4.3) | (3) |
| (5) | fibre criterion (Section 4, unmoved) | (5) unchanged |

All hardcoded in-text references were remapped consistently:
"By (1)"/"integrates (1)"/"readings of (1)"/"Second, (1)" -> (4);
"Condition (2)"/"condition (2)" -> (1);
"drift (3)"/"hypothesis (3)"/"drift certificate (3)" -> (2);
"timing bound (4)"/"Condition (4)"/"and (4)"/"even when (4)" -> (3).

The supplementary is a self-contained document whose own tags (1)-(5) already
appear in its internal reading order; it is unchanged.

## Final verification (v32 -> v36)

- Display-equation count: 38 in both versions; the only differences are the
  intended tag renumberings (the single flagged author-block "difference" was
  a text-extractor artifact, empty under a direct diff).
- All 22 numbered environments accounted for: 16 byte-identical; the 6 that
  differ differ only by the remapped `Section 3.x` references, the added
  Section pointers, or the equation-tag renumberings above — no mathematical
  content changed.
- Word-multiset delta v32 -> v36: 13 removed / 54 added word-instances, each
  traced to the intended connective rewrites, the §1.4 rewrite, the new §3.4
  heading, and the duplicated-phrase fix. No content loss.
- Numbering sequences all complete: Theorems 1-7, Propositions 1-9,
  Remarks 1-4, Corollary 1, Example 1; subsubsections 3.1-3.6; equation tags
  now (1)-(5) in reading order with consistent references.
- QA: main 15 pages / 4 images / 1 table / 0 `??` / no overfull / abstract
  262 words; supplementary 13 pages / 3 images / 0 `??`.

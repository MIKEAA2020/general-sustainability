# E3 v26 / SI v4 version-currency audit

**Audit date:** 2026-10-17  
**Repository:** `MIKEAA2020/general-sustainability`

## Version scan before numbering

Checked all six branch tips, both tags, both releases, the current `VERSION_CURRENCY.md`, the split/prior-art record, and the local historical Paper11/Paper11b merge note before adopting the next E3 number.

| Ref | Tip / target SHA |
|---|---|
| `archive/paper3-v48-workspace` | `0200b6dc75a51feb40728df07e855facbb791383` |
| `e2-v3-source-year` | `47bbfb284042ed70b1aba20ccd86286504d51d40` |
| `edwards-framework-e1-audit-implementation` | `9f3a3842795df6bc34db379d797c46b01c8948f1` |
| `edwards-framework-e1` | `66a0a71f976e76df403425e85690d2c9dcb4c141` |
| `lean-audit-v4` | `c2fe8fca63384cbf9243434d4213c6e74543a840` |
| `main` | `1ba3d3c8a286a055b1342b5102731b601ec3d428` |
| Tag `edwards-framework-e1` | `60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e` |
| Tag `compendium-v1.0` | `504f78e176ca25da88ba487571aa4a674299ace3` |

At this scan, E3 v25/SI v3 was the latest standalone Edwards edition on `edwards-framework-e1-audit-implementation`. Paper11 v68 main/SI was current on `main`. No E3 v26 or SI v4 was present on the checked branch/tag refs before this edition was prepared. The existing Paper11b v2 remains the recovered Edwards half of the older merged lineage; it is not a newer standalone E3 edition. The E3 v24/SI v2 versus Paper11 v67/SI S15–S22 claim crosswalk is retained unchanged.

`VERSION_CURRENCY.md` on `e2-v3-source-year` (blob `f4d5a9799949a4cfc7509710d441fa87c1164f44`) recorded E3 v25/SI v3 and the 2026-10-16 v67 crosswalk. `PAPER11_SPLIT_AND_PRIOR_ART.md` on that branch (blob `dc7db07992e948c9c64a4befe61e17e04aa9139e`) describes the old v61/v64 split/merge lineage, not the current v68 comparison. The local `census/PAPER_MERGE_11_11b.md` likewise documents the historical v64 merge rationale, not a replacement for the current E3/v68 alignment.

## Release assets

Release API metadata listed:

| Release tag | Asset | Bytes | Asset last updated |
|---|---|---:|---|
| `edwards-framework-e1` | `workspace-edwards-ecomod.sustainability.zip` | 58,868,212 | 2026-09-12 |
| `edwards-framework-e1` | `workspace-edwards.framework.2nd.zip` | 77,252,329 | 2026-09-12 |
| `compendium-v1.0` | `workspace-01a00d79-f20f-70dc-938a-8c93ce245a8c.zip` | 142,023,921 | 2026-09-04 |

A ZIP tail-range request for each asset returned HTTP 501 (“Unsupported client range”). The internal ZIP directory/payload names therefore could not be inspected without downloading the full 279 MB. That full download was not performed because it is unnecessary for version currency and would add substantial workspace use. The API-visible asset filenames and update dates are recorded above; all predate E3 v25 (2026-10-16) and this E3 v26/SI v4 (2026-10-17).

## Number and target decision

- **Main:** E3 v26 is justified by current Paper11 v68 alignment, a corrected abstract/impact-statement page flow, and incorporation of the archived rolling-origin increment attribution. It is not a bookkeeping-only version.
- **Supplement:** SI v4 is justified by the real compile defect in published SI v3 and the clarified raw-proposal versus clipped-emission record. SI v3 remains unchanged.
- **Target:** same path/branch as v25: `e3/` on `edwards-framework-e1-audit-implementation`.
- **Preservation:** E3 v25, SI v3, Paper11 v67, Paper11 v68, Paper11b v2, prior tags/releases, and the dated v24/v67 crosswalk are not overwritten, renumbered, or deleted.

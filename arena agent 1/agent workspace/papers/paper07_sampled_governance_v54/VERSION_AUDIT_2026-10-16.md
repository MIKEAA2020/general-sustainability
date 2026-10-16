# Paper07 v54 lineage audit — 2026-10-16

**Repository:** `MIKEAA2020/general-sustainability` (public). This is a fresh pre-numbering check of all remote branches, tags, and GitHub releases before assigning v54. Tree metadata were inspected through the existing blob-filtered sparse clone; no repository-wide clone was made. The unsafe `/home/user/gs2` worktree was not modified.

## All-ref inventory at the time of the v54 decision

Remote branches and tips:

| Branch | Tip (full SHA) | Paper07 / related lineage finding |
|---|---|---|
| `archive/paper3-v48-workspace` | `0200b6dc75a51feb40728df07e855facbb791383` | No Paper07/Paper08 candidate. |
| `e2-v3-source-year` | `556240fda8498d11efa8921b7aa5d469da2e9140` | Latest standalone Paper07 was v53; parallel Paper08 v48 is present. |
| `edwards-framework-e1` | `66a0a71f976e76df403425e85690d2c9dcb4c141` | Historical Paper5 sampled-governance lineage through v46; no later Paper07. |
| `edwards-framework-e1-audit-implementation` | `8cf4ab0c6515aeb9c7a3dd55fb1e67eff299283e` | Historical Paper5 lineage through v46; no later Paper07. |
| `lean-audit-v4` | `c2fe8fca63384cbf9243434d4213c6e74543a840` | Historical Paper5 lineage through v47 blinded; no later Paper07. |
| `main` | `217d110f006ec4b6b43755e53350d7043b0d1ddc` | Historical Paper5 lineage through v47 blinded; no later Paper07. |

The two tags are `compendium-v1.0` and `edwards-framework-e1`. The GitHub releases endpoint lists two prereleases with those same tag names. Neither tag nor prerelease contains a Paper07 edition or a Paper07-specific release. No Paper07 v54 or higher was present in any checked ref before this edition was assigned.

## Version-currency and split/merge checks

- `arena agent 1/agent workspace/papers/VERSION_CURRENCY.md` was read after the v53 publication; its latest Paper07 entry was v53. This audit and the new v54 addendum supersede that entry for current numbering without rewriting its historical notes.
- Paper07 v53 is preserved at `arena agent 1/agent workspace/papers/paper07_sampled_governance_v53/`, based on v52. V54 is a new directory and continuation, not an overwrite.
- Paper08 v48 remains at `paper08_governance_delay_v48.tex` with its two existing supplements, unchanged. The v46 split/merge note and v43 de-duplication/inheritance note were reviewed; neither authorizes replacing v48 or merging it into this standalone v54.
- The older `paper5_sampled_governance` names are historical lineage material and do not supersede standalone Paper07 v53.

## Recovery check for the v52 Supplementary file

The v52 PDF and TeX source explicitly refer to a separate Supplementary file. A path/content search across all six branches and both tag trees found no Paper07/v52 SI file and no copy of the promised “dimensionless identifiability chart.” The v52 source gives no separate DOI for that SI. Its closing inventory lists S1–S10, while in-body references extend through S13.3, so the old supplement's full extent cannot be established from the recoverable record. The v52→v53 crosswalk records this limitation and does not treat the 36-page main PDF as the whole v52 package.

## Publication decision

Continue the standalone lineage as **Paper07 v54**, based on v53, at `arena agent 1/agent workspace/papers/paper07_sampled_governance_v54/` on `e2-v3-source-year`. The pre-publication remote tip is `556240fda8498d11efa8921b7aa5d469da2e9140`; update only if the remote still descends from it, and push fast-forward-only. Preserve v52, v53, Paper08 v48, all other existing versions, tags, and releases. No tag or release is created by this update.

The v54 edition corrects stale SI references and clarifies the archived sensitivity record; adds bounded design implications and an AI-use disclosure; and publishes the recovered-content crosswalk. It does not claim new numerical reruns or reconstruct the unavailable v52 SI.

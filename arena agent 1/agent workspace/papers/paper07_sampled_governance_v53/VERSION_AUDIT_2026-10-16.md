# Paper07 / Paper08 lineage audit — 2026-10-16

**Repository:** `MIKEAA2020/general-sustainability` (public). The audit used the GitHub API to enumerate remote branches, tags, and releases, and tree metadata for every branch/tag. No repository-wide clone was performed. The existing `/home/user/gs2` worktree was not modified; its index still contains 6,551 staged deletions and has no configured remote, so it was not used for publication.

## Branch and version findings

Remote branches and current tips:

| Branch | Tip (short SHA) | Date | Paper07 / sampled-governance finding |
|---|---|---|---|
| `e2-v3-source-year` | `fe1eabdc9ffb` | 2026-10-15 | Latest standalone Paper07 found: v52. Also contains the latest Paper08 v48 combined manuscript. |
| `main` | `217d110f006e` | 2026-10-15 | Latest file under the older Paper5 rewrite lineage is v47 blinded; no Paper07 v52 or later. |
| `lean-audit-v4` | `c2fe8fca6338` | 2026-09-28 | Paper5 rewrite lineage through v47 blinded; no later Paper07 edition. |
| `edwards-framework-e1-audit-implementation` | `8cf4ab0c6515` | 2026-09-22 | Paper5 rewrite lineage through v46; no Paper07 v52 or later. |
| `edwards-framework-e1` | `66a0a71f976e` | 2026-09-12 | Paper5 rewrite lineage through v46; no Paper07 v52 or later. |
| `archive/paper3-v48-workspace` | `0200b6dc75a5` | 2026-09-19 | Paper03 archive/workspace branch; no Paper07/Paper08 candidate. |

The newest confirmed Paper07 source is:

- `arena agent 1/agent workspace/papers/paper07_sampled_governance_v52.tex`
- `arena agent 1/agent workspace/papers/paper07_sampled_governance_v52.pdf`

The parallel combined Paper08 edition is:

- `arena agent 1/agent workspace/papers/paper08_governance_delay_v48.tex`
- `arena agent 1/agent workspace/papers/paper08_governance_delay_v48.pdf`
- `paper08_governance_delay_v48_supplementary_delay.md`
- `paper08_governance_delay_v48_supplementary_governance.md`

The v52/v48 files are on `e2-v3-source-year`; immediately before the v53 release, no branch or tag contained Paper07 v53 or a higher Paper07 version. The older `paper5_sampled_governance` naming is a separate historical path and does not supersede the v52 Paper07 lineage.

Baseline Git blob IDs on `e2-v3-source-year` before the v53 release:

| Preserved artifact | Git blob ID |
|---|---|
| Paper07 v52 `.tex` | `5e55af0f006eb28789ac29bc70bf000dcdf88843` |
| Paper07 v52 `.pdf` | `515d9a8b58ed3c07625b4edf7df8813b260cd1cb` |
| Paper08 v48 `.tex` | `57c2d374191ecf9bc4c9089577e79163ffb016a1` |
| Paper08 v48 `.pdf` | `a2b9c09db3427139abcf7f63f6125d39f1686371` |
| Paper08 v48 delay supplement | `6aa37d587751cb86ea0cd3d7caba37ad8cfaca75` |
| Paper08 v48 governance supplement | `70f8f78b384b6059b0c89531c81ed270dbdc5c0e` |

## Tags and releases

The repository has two tags, `edwards-framework-e1` and `compendium-v1.0`, and two prereleases with those same tag names. Their trees contain no Paper07 v52/v53 release artifact; no Paper07-specific tag or release exists. The v53 addition will therefore continue the branch lineage without reusing a branch, tag, or release version.

## Version and split/merge notes checked

- `arena agent 1/agent workspace/papers/VERSION_CURRENCY.md` is dated 2026-09-29 and still says Paper07's source of record is `diffs/p5_v47.tex`. That entry is stale relative to the v52 file on `e2-v3-source-year`; the release adds a dated addendum rather than rewriting the historical audit.
- `PAPER_MERGE_08_07.md` is a historical note about the v46 two-regime merge. It does not authorize replacing the later v48 combined edition.
- `PAPER08_DEDUP_AND_INHERITANCE.md` records the v43 correction of the inherited 6.5-year claim; `PAPER08_REF_RECONSTRUCTION.md` is a historical bibliography repair record. The current v48 combined Paper08 files are retained unchanged.
- The local `src/VERSION_CURRENCY_context.md` is a dated historical copy of the 2026-09-29 audit, not an up-to-date inventory. This full-ref audit supersedes it for the Paper07/Paper08 numbering decision.

## Publication decision

Continue as **Paper07 v53**, a standalone edition based on v52, on branch `e2-v3-source-year`, at `arena agent 1/agent workspace/papers/paper07_sampled_governance_v53/`. Preserve all existing versions and Paper08 v48. Pre-push requirement: verify the remote branch tip still equals or descends from `fe1eabdc9ffb`, and make a fast-forward-only update; never alter the unsafe `/home/user/gs2` index. No Paper08 source, PDF, or supplementary file is to be modified.

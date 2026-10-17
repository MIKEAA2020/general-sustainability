# Workspace legacy clone audit — 2026-10-18

**Scope:** local legacy/test roots only: `p07_v53/`, `paper1_v64/`, `p09_layout_test/`, and `p09_source_test/`. This is the pre-deletion manifest. No deletion has occurred at the time of this audit.

**Excluded from deletion by instruction:** all of `portfolio_work/`, `uploads/`, loose root-level deliverables/review images, `.git` and tool caches, and every file not listed as a byte-verified remote copy. This audit does not authorize deletion outside the four named roots.

## Method and refs

Scanned all six branch tips and both tag tips; every recursive tree was complete. Each local regular file in scope was hashed as a Git blob and checked against reachable remote blobs. For every file designated for deletion, the matching remote blob was fetched and its bytes compared to the local file. The per-file record is `WORKSPACE_LEGACY_CLONE_AUDIT_2026-10-18.csv`.

- `branch:archive/paper3-v48-workspace` — `0200b6dc75a51feb40728df07e855facbb791383`
- `branch:e2-v3-source-year` — `600354c149aad300780d647cdb0768451ec726dc`
- `branch:edwards-framework-e1-audit-implementation` — `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5`
- `branch:edwards-framework-e1` — `66a0a71f976e76df403425e85690d2c9dcb4c141`
- `branch:lean-audit-v4` — `c2fe8fca63384cbf9243434d4213c6e74543a840`
- `branch:main` — `1ba3d3c8a286a055b1342b5102731b601ec3d428`
- `tag:edwards-framework-e1` — `60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e`
- `tag:compendium-v1.0` — `504f78e176ca25da88ba487571aa4a674299ace3`

## Disposition

| Local root | Files scanned | Byte-verified remote copies (deletion candidates) | Candidate bytes | Local-only/modified files retained | Retained bytes |
|---|---:|---:|---:|---:|---:|
| `p07_v53/` | 273 | 223 | 8,554,704 | 50 | 8,037,709 |
| `paper1_v64/` | 30 | 30 | 3,066,566 | 0 | 0 |
| `p09_layout_test/` | 146 | 138 | 3,139,034 | 8 | 164,361 |
| `p09_source_test/` | 149 | 137 | 2,787,701 | 12 | 702,919 |
| **Total** | **598** | **528** | **17,548,005** | **70** | **8,904,989** |

The 528 deletion candidates total **17,548,005 bytes (16.74 MiB)** and have exact, byte-verified copies on reachable refs. The 70 other files total **8,904,989 bytes (8.49 MiB)** and are retained because they are local-only or differ from every reachable remote blob. No Paper11, Paper11b, E3, Paper08 v51, or other portfolio files are included.

The candidate copies are re-clonable from the exact ref/path in the CSV. The published editions and remote repository objects remain unchanged. After the audit and CSV are published and byte-verified, the planned cleanup is limited to unlinking those exact local candidates, with a fresh per-file hash/blob check immediately before each deletion. No directories, unique/local-only files, or other workspace paths are scheduled for removal.

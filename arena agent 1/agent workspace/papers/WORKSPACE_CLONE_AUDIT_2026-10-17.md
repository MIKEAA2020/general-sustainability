# Targeted workspace clone audit — 2026-10-17

**Scope:** local `p11_v67/` and `p11_v68/` build folders only. No deletion has occurred.
**Remote scan:** all 6 branches and 2 tags (8 refs total); each recursive tree was complete. Local file contents were hashed as Git blobs and compared to reachable remote blobs. The CSV is the per-file record.

| Disposition | Files | Bytes | MiB |
|---|---:|---:|---:|
| Exact remote copies — planned deletion only after this audit is pushed/verified | 198 | 21529298 | 20.53 |
| Local-only/unique files — retain | 12 | 189778 | 0.18 |

The deletion candidates are byte-identical to blobs reachable on the recorded branch/tag refs, with the matching ref and repository path listed in `WORKSPACE_CLONE_AUDIT_2026-10-17.csv`. All local-only files stay in place. The audit covers only these two now-reviewed Paper11 folders; it does not authorize removal from active `portfolio_work/`, user uploads, or any other local-only directory.

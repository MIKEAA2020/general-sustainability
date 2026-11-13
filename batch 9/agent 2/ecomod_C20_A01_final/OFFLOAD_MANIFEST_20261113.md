# Offload manifest — 2026-11-13 (rev. 2, GitHub-only)

Revision note: an earlier rev. 1 of this file listed Dropbox as the archive target. That was wrong —
**GitHub is the repository**. Dropbox copies were deleted and this manifest now records only the
GitHub + Zenodo anchors. No Dropbox dependency remains.

## Deleted locally on 2026-11-13 (disclosed, all reclonable/restorable)

| Removed | Size before | Where it lives now |
|---|---|---|
| `ecomod_audit_remediation_C18_A01/` | 27 MB | GitHub `offload_archives/ecomod_audit_remediation_C18_A01.zip` (12,482,391 B) |
| `governance_elevation_P4_v43_P02/` | 11 MB | GitHub `offload_archives/governance_elevation_P4_v43_P02.zip` (8,320,036 B) |
| `ecomod_editorial_division_C19_A01/` | 9.1 MB | GitHub `offload_archives/ecomod_editorial_division_C19_A01.zip` (6,581,138 B) |
| `ecomod_zenodo_deposit/ECOMOD_C20_A01_reproduction_package.zip` | 6.0 MB | Zenodo DOI `10.5281/zenodo.24092131` **and** GitHub `offload_archives/` (6,021,179 B) |
| `_offload_staging/` (temporary zips) | 32 MB | n/a |

Workspace: **103 MB → 51 MB**. `ecomod_zenodo_deposit/HOW_TO_DEPOSIT.md` kept.

## Which package is the Zenodo zip?
`ECOMOD_C20_A01_reproduction_package.zip` is the reproduction package for the **current paper** —
ECOMOD C20 A01 (Ecological Modelling, "aggregation, identifiability, delay differential equations";
manuscript of record `10.20944/preprints202611.0852.v1`). It is not a historical artifact: it is the
deposit behind Dataset DOI `10.5281/zenodo.24092131`, md5 `8a51345b76609063d10c8a282c1b8387`,
6,021,179 B (md5 matches the published Zenodo record).

## GitHub anchors (primary repository)
`MIKEAA2020/general-sustainability` @ `main`, under `batch 9/agent 2/ecomod_C20_A01_final/`:
- 86-file submission set — commits `b26504d…`, `2a63509…` (86/86 blob SHAs verified)
- `offload_archives/` — C18, C19, P4/v43, reproduction package, EM upload set, preprint source zip
  (each pushed with the commit's `content.sha` compared to the local git blob hash; all matched)
- `OFFLOAD_MANIFEST_20261113.md` (this file)

## Zenodo anchors
- Dataset `10.5281/zenodo.24092131` — C20 reproduction package.
- Preprint v35 record 22554480 unchanged; manuscript of record `10.20944/preprints202611.0852.v1`.

## Restore any deleted root
```
curl -L -o C18.zip https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/main/\
batch%209/agent%202/ecomod_C20_A01_final/offload_archives/ecomod_audit_remediation_C18_A01.zip
unzip C18.zip -d /home/user/
```
Reproduction package, canonical source:
```
curl -L -O https://zenodo.org/records/24092131/files/ECOMOD_C20_A01_reproduction_package.zip
md5sum ECOMOD_C20_A01_reproduction_package.zip   # 8a51345b76609063d10c8a282c1b8387
```

## Still streamed (no duplicate copies)
`public_downloads/` symlinks, port 8000: `EM_upload_C20/`, `C20_package/`,
`ecomod_C20_preprints_source_20261031.zip`, `WORKSPACE_CLEANUP_AND_PUSH_20261031.md`,
`READ_ME_FIRST_portal_compile_fix.md`, this manifest.

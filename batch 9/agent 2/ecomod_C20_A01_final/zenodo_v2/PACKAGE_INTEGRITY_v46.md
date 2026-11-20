# Deposit package — completeness report (v46)

**Path to upload:**
`/home/user/ecomod_zenodo_v2/ECOMOD_v46_reproduction_package.zip`

**Size:** 6,022,335 B · **md5:** `6425f8a2bae6af83e2423fae12e0a992`

Deposit as a **new version of record 24092131** (concept DOI `10.5281/zenodo.24092130`).

## Contents — 62 files

| Directory | Files | What |
|---|---|---|
| `manuscript/` | 2 | v46 main `.tex` + `.pdf` (40 pp) |
| `supplementary/` | 2 | v46 SI `.tex` + `.pdf` (31 pp) |
| `figures/` | 8 | Figs 1–3, S1–S5, tech-wave debt, one-stock basin (vector PDF) |
| `data/` | 26 | all numerical outputs (CSV/JSON) |
| `tables/` + `inherited_C17/` | 10 | the nine `\input` fragments + budget solver |
| `code/` | 4 | three reproduction scripts + pinned requirements |
| `repository_sources/` | 4 | NFA 2026 workbook, OWID cropland/cereal, v44 drawdown CSV |
| `zenodo/` | 2 | metadata + upload helper |
| root | 4 | `README.md`, `CITATION.cff`, `LICENSE_DATA_ATTRIBUTION.md`, `SHA256SUMS.txt` |

## Verified before upload

| Check | Result |
|---|---|
| File set vs published v1.0 | **62 = 62** — nothing missing, nothing extra |
| Changed files vs v1.0 | exactly 6: README, CITATION.cff, manuscript tex+pdf, SI tex+pdf |
| `code/` and `data/` | **byte-identical to v1.0** |
| Reproduction scripts (offline, from the zip) | **3/3 exit 0** |
| `SHA256SUMS.txt` | regenerated; **61/61 entries verify** inside the archive |
| Stale title anywhere in the package | **none** |
| Manuscript/SI compile warnings | 0 errors; 40 pp / 31 pp |

## Two defects found and fixed in this pass

1. **`SHA256SUMS.txt` was stale.** Five entries failed — README and both manuscript/SI file pairs.
   Regenerated over the whole tree; all 61 now verify.
2. **`CITATION.cff` was wrong.** It carried the old title, version 1.0, and — more seriously — the
   DOI field pointed at **`10.5281/zenodo.22554480`**, which is the *v35 preprint* record, not this
   dataset. Corrected to the concept DOI `10.5281/zenodo.24092130`, version `2.0 (ECOMOD v46)`,
   date 2026-11-13.

## Metadata to paste (web route)

- **Title:** Reproduction package for: Rising biocapacity, falling ecological capital: how aggregation conceals composition
- **Version:** 2.0 (ECOMOD v46) · **Date:** 2026-11-13 · **Type:** Dataset · **Licence:** CC BY-SA 4.0
- **Related:** `10.20944/preprints202611.0852.v1` (is supplement to) · `10.5281/zenodo.22554480` (is related to) · GitHub repo (is identical to) — the `isNewVersionOf → 24092131` link is added automatically
- Description/keywords/creators: already in `zenodo_metadata_api.json` in this folder

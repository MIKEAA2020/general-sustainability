# Recovery guide — ECOMOD artifacts (2026-10-25)

**Recovery directory:** `/home/user/ecomod_v45/RECOVERED_ARTIFACTS_20261025_01/`

This is a newly named recovery directory created after confirming that the path did not already exist. During this recovery pass I wrote only inside this directory. I did not overwrite or delete any existing file, refresh a checksum, package a ZIP, or push changes.

## What is included

- **`CURRENT_POST_PAGEBREAK/`** — separately named copies of the latest QA main/SI PDFs, assembled TeX, TeX logs, `assemble.py`, and all 13 current editable source-part files.
- **`CURRENT_ROOT_DOCS/`** — copies of the current README, review status, changelog, and the known-stale root checksum text. The checksum text is copied unchanged and is not a refreshed manifest.
- **`AS_FOUND_STAGING_COPY_20261025/`** — a copy of the pre-existing staging directory exactly as found, including its named `SI_verified` PDFs, TeX, logs, parts, figures, notes, README, and existing `SHA256SUMS.txt`. That checksum file was copied unchanged, not validated or refreshed.
- **`RECONSTRUCTED_PRE_PAGEBREAK/`** — TeX reconstructed from current parts by removing only the inserted S4.2 `\par\pagebreak` from SI; the existing S4.4 pagebreak remains. The main TeX matches the current assembled main source. It also includes local figure support assets and a successful fresh Tectonic build in `build_with_local_assets_01/`. The rebuilt PDFs are explicitly reconstructions, not recovered original PDF bytes.
- **`FROM_RECOVERY_COMMIT_7ae113d5/`** — 76 historical manuscript-related files available in recovery commit `7ae113d5edeaeb9e547b7d48195a2c19387f9282`: earlier v45 main/SI PDF variants, assembled TeX, editable parts, and review docs. These are preserved under their historical variant names and paths.
- **`FROM_PUBLIC_MAIN_2efaa620/`** — the public-main v44 main and supplementary PDFs from commit `2efaa62083f2007dec3446c15c475af88f0925f3`; they are older published reference files, not v45.
- **`DIFF_REPORTS/`** — both documentation-diff snapshots (before and after the selective packaging-description reverts).
- **`RECOVERY_INDEX.md`** and **`RECOVERY_STATUS_ADDENDUM_01.md`** — supporting provenance and status notes.

## Recovery limits and PDF comparison

The exact prior/deleted `SI_verified` PDF bytes were not found in the inspected Git commits. The staging copy contains PDFs with `SI_verified` in their filenames, so I preserved them rather than treating them as lost; however, their page-by-page extracted text matches the latest QA PDFs, and their bytes differ. They therefore cannot be certified as the earlier overwritten/deleted pair.

The successful reconstructed PDFs are 35-page main and 20-page SI. Their page-by-page extracted text matches the latest QA PDFs; removing the inserted SI page-break does not change the extracted pagination in this reconstruction. The earlier citation-acknowledgement/restoration alternatives from commit `7ae` have a different split: their SI p. 6 ends “The thresholds are identical” and p. 7 starts “to three decimals.” The staging/current-QA SI p. 6 ends with the 3.14-cap result and p. 7 starts “The thresholds are identical to three decimals.” The historical alternatives are not exact substitutes for the unidentified original pair.

A first reconstruction compile attempt is retained in `RECONSTRUCTED_PRE_PAGEBREAK/build/`; it failed because the first build context lacked figures. It was not overwritten. The successful compile used the distinct `build_with_local_assets_01/` folder.

## Why the latest changes were not pushed

I’m sorry I did not make this clear sooner. The session record carried an explicit standing constraint: **no push without separate authorization**. Your question about why it was not pushed is not itself an explicit instruction to push now, and having a PAT does not remove that constraint. Also, `/home/user/ecomod_v45` is not a Git checkout; `/tmp/ecomod_repo_audit` is an inspection clone. No push of the latest changes has occurred. I will not push unless you explicitly authorize it.

The previous audit identified recovery commit `7ae113d5edeaeb9e547b7d48195a2c19387f9282` on `workspace-recovery-2026-10-24` and public `main` at `2efaa62083f2007dec3446c15c475af88f0925f3`. No PAT or other secret was copied into this recovery directory.

## Manuscript facts retained from session memory

- Citation-key mapping remains `Abaee2026a` = Paper4/governance, `Abaee2026b` = Paper06 v71/assessment, `Abaee2026c` = Paper3/ledger.
- Paper06 Theorem 4(iii) supports exact false-certification intervals only on its witness-defined diagonal-gap region. Paper3 is pinned to the public-main commit above; its v50 / README-checksum v49 / TeX-header v48 discrepancy is disclosed.
- The preferred matching main/SI title is “Aggregate biocapacity does not identify its composition.”
- Table S4’s reported value was checked against both drawdown CSVs; the sampled 0.1-cap grid showed no monotonicity violations across both CSVs and both minimum-area columns.
- Do not restore broad boom–bust or “no Allee threshold other than the floor”; retain the weak/strong Paper3 framing and distinguish Half-Earth’s spatial target from the model’s annual flow reservation.

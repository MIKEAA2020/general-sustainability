# Recovery overview — ECOMOD manuscript artifacts

**Location:** `/home/user/ecomod_v45/RECOVERED_ARTIFACTS_20261025_01/`

A fresh, previously unused directory was created for this recovery. At final verification it contained 246 files and occupied about 57 MB. The recovery pass did not overwrite or delete existing project files. No checksum was refreshed, no ZIP/package was made, and no push occurred. A temporary `pypdf` library used for read-only PDF text comparisons was installed under `/tmp/recovery_pdf_tools`; see `RECOVERY_CORRECTION_01.md`.

## Recovery contents

- `CURRENT_POST_PAGEBREAK/` — latest QA main/SI PDFs, assembled TeX, build logs, assembler, and 13 current source-part files, all copied under distinct names.
- `CURRENT_DATA_AND_SCRIPTS/` — all 16 current CSVs, current NFA JSON summary, and 17 Python scripts relevant to the manuscript/data/figures, copied with relative paths. Includes both drawdown CSVs used for Table S4 checks.
- `CURRENT_ROOT_DOCS/` — current README, review status, changelog, and the stale root checksum text, copied unchanged.
- `AS_FOUND_STAGING_COPY_20261025/` — copy of the pre-existing staging directory as found (39 files), including its named `SI_verified` PDFs, TeX, source parts, figures, logs, notes, README, and existing checksum file. Its checksum file was copied verbatim, not checked or refreshed.
- `RECONSTRUCTED_PRE_PAGEBREAK/` — main/SI TeX reconstructed from current parts by removing only the inserted S4.2 SI page-break command; the older S4.4 break remains. `build_with_local_assets_01/` contains successful reconstructed main/SI PDFs (35 and 20 pages) and logs. `build/` preserves the first failed diagnostic attempt; it is incomplete and is not the usable build.
- `FROM_RECOVERY_COMMIT_7ae113d5/` — historical v45 manuscript PDFs, assembled TeX, source parts, root review docs, and support CSV/Python/JSON files available in recovery commit `7ae113d5edeaeb9e547b7d48195a2c19387f9282`.
- `FROM_PUBLIC_MAIN_2efaa620/` — published v44 main and SI PDFs from public commit `2efaa62083f2007dec3446c15c475af88f0925f3`; these are older reference versions.
- `DIFF_REPORTS/` — pre- and post-selective-revert documentation patches.
- Notes: `RECOVERY_INDEX.md`, `RECOVERY_STATUS_ADDENDUM_01.md`, `RECOVERY_DATA_ADDENDUM_01.md`, `RECOVERY_GUIDE_02.md`, and `RECOVERY_CORRECTION_01.md`.

## What is and is not recovered

The exact old `SI_verified` PDF pair has not been conclusively recovered from the inspected Git commits. The staging directory currently contains files with `SI_verified` names; I preserved them as found, but their page-by-page extracted text matches the latest QA PDFs while their bytes differ. They cannot be certified as the earlier overwritten/deleted binaries.

The reconstructed pre-page-break TeX is reproducible from current parts: the main TeX matches the current assembled main, and the reconstructed SI TeX differs from current SI only by removing the inserted S4.2 page-break command. Fresh PDFs were built; their page-by-page extracted text matches current QA (35-page main, 20-page SI). Those PDFs are reconstructions, not byte-recovered originals.

The older citation-acknowledgement/restoration alternatives in the recovery commit have a different SI pagination around the threshold sentence: p. 6 ends “The thresholds are identical”; p. 7 begins “to three decimals.” The current staging/latest-QA SI instead has the 3.14-cap result at the end of p. 6 and starts p. 7 with “The thresholds are identical to three decimals.” The alternatives are preserved but are not exact substitutes for the unidentified original.

## Why no push happened

I’m sorry I did not make this clear earlier. The session record carried a standing explicit constraint: **no push without separate authorization**. Your question about the missed push is not itself an explicit instruction to push now; having a PAT does not override that constraint. `/home/user/ecomod_v45` is not a Git checkout, and `/tmp/ecomod_repo_audit` is an inspection clone. No latest changes were pushed. I will only push if you explicitly authorize the push and target branch. No PAT or secret was copied into the recovery directory.

## Manuscript decisions retained from session memory

- Citation keys: `Abaee2026a` = Paper4/governance; `Abaee2026b` = Paper06 v71/assessment; `Abaee2026c` = Paper3/ledger.
- Paper06 Theorem 4(iii) is scoped to its witness-defined diagonal-gap region. Paper3 is pinned to the public-main commit above, with the v50 / README-checksum v49 / TeX-header v48 ambiguity disclosed.
- Main/SI titles match the preferred result-style title, “Aggregate biocapacity does not identify its composition.” Table S4’s value was checked against the two drawdown CSVs; the sampled 0.1-cap grid had no monotonicity violations in both CSVs and both minimum-area columns.
- Do not restore broad boom–bust or “no Allee threshold other than the floor”; preserve Paper3 weak/strong framing and distinguish Half-Earth’s spatial conservation target from the model’s annual flow reservation.

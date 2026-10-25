# Recovered ECOMOD artifacts — RECOVERED_ARTIFACTS_20261025_01

This directory was created as a new, non-overwriting recovery area. Nothing here is a push or release. No checksum manifest was generated.

## Current post-page-break QA build

`CURRENT_POST_PAGEBREAK/` contains separately named copies of the latest fresh QA main/SI PDFs, assembled TeX, TeX logs, assembler, and current editable `parts/`. These correspond to the 35-page main and 20-page SI build.

## Pre-page-break reconstruction

`RECONSTRUCTED_PRE_PAGEBREAK/` contains TeX reconstructed deterministically from current parts by removing only the newly inserted S4.2 `\par\pagebreak`; the older S4.4 pagebreak remains. These are explicitly reconstructed, not the original overwritten byte copies.

## Earlier pushed snapshot

`FROM_RECOVERY_COMMIT_7ae113d5/` contains the selected ECOMOD v45 main/SI PDF variants, earlier assembled TeX, source parts, and review documents available at commit `7ae113d5edeaeb9e547b7d48195a2c19387f9282`. These are historical alternatives, not the exact deleted `SI_verified` PDFs. The commit tree has no `output_v45_citation_framing_SI_verified_20261025/` path.

`FROM_PUBLIC_MAIN_2efaa620/` contains the published v44 main/SI PDFs from public commit `2efaa62083f2007dec3446c15c475af88f0925f3`; these are not v45 files.

## What the session memory establishes

- Citation mapping: `Abaee2026a` = Paper4/governance; `Abaee2026b` = Paper06 v71/assessment; `Abaee2026c` = Paper3/ledger.
- Paper06 Theorem 4(iii) was narrowed to its witness-defined diagonal-gap region. Paper3 is pinned to commit `2efaa62083f2007dec3446c15c475af88f0925f3`; the footnote discloses PDF v50 / README-checksum v49 / TeX-header v48.
- Main and SI titles match. Main Table 2(a) `E_{ceil}=1.138 gha` was inspected; `phi_0=0.128647` was checked. SI Eq. (18), the Table S2-in-§S3 reference, and Table S6 layout were checked.
- Table S4's `0.050` was verified against both drawdown CSVs. The sampled 0.1-cap grid had zero monotonicity violations across both CSVs and both minimum-area columns; this is sampled evidence, not a proof between grid points.
- The latest build is 35 US Letter main pages and 20 A4 SI pages, with zero unresolved `??` markers. SI p. 6 ends on a complete sentence; p. 7 starts with the threshold-comparison sentence; Tables S4 and S6 were visually checked.
- The exact pre-follow-up `SI_verified` PDFs and root assembled TeX bytes were not preserved. The current main TeX matches deterministic reconstruction from unchanged main parts; reconstructed pre-break SI differs from current SI only by the inserted S4.2 page-break command.
- No push of the latest follow-up occurred. The session record shows earlier recovery-branch commit `7ae113d5edeaeb9e547b7d48195a2c19387f9282` and public main `2efaa62083f2007dec3446c15c475af88f0925f3`.

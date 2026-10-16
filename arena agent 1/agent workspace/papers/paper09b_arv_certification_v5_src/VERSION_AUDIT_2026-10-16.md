# Paper09b v5: lineage and preservation audit (2026-10-16)

## Version decision

A fresh all-ref scan found Paper09b v4 already present on the active `e2-v3-source-year` branch at `arena agent 1/agent workspace/papers/paper09b_arv_certification_v4.tex`, alongside its existing PDF. The v4 edition is preserved; this conditional-accounting revision is v5, not an overwrite or reuse of v4. The current branch is the latest Paper09b lineage among the checked remote branches. Other checked branches and tags did not contain a higher Paper09b edition. The previously inspected GitHub release inventory contained no Paper09b-specific release asset.

## What v5 changes

- Keeps assessed SSB distinct from DFO 2025 Table 1 reported **total landings** and from the Schijns catch reconstruction.
- States the exact tonnes-to-kilotonnes conversion, defines unknown nonnegative `kappa`, and evaluates both adjacent-year landings assignments for each selected transition.
- Replaces unconditional harvest-free/biological language with row-specific strict `kappa*` conditions under both accounting placements.
- Adds a source-row/rational-arithmetic checker and the small locked CSV extracts it reads. The checker does not claim to re-extract the cited reports or validate assessment uncertainty.
- Corrects the 1983--1989 reported-landings scale proof to use the minimum and maximum across all seven rows and limits the comparison to the 1994--1995 low-landings rows.

## Verification and build status

`verify_kappa_thresholds.py` passes: source-row consistency; the 1983--1989 range calculation; 70 adjacent xteNCAM band comparisons; exact conversion; all seven primary and one later-vintage threshold pairs; and both accounting identities below, at, and above each threshold. Static TeX checks pass for one document structure, balanced environments/braces, unique labels, and resolved internal references. No TeX engine is installed in the workspace, so v5 has not been compiled and no v5 PDF is claimed.

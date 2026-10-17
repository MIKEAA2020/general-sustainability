# Source-only edition build and page-count audit

**Date:** 2026-10-17  
**Repository/branch:** `MIKEAA2020/general-sustainability`, `e2-v3-source-year`  
**Pre-publication branch head:** `1488e61f5c0e92452805ac9deaba6240d78d466f`  
**Scope:** build/readiness checks for active source-only editions; verification of the reported Paper 11 60-to-49-page change. No edition numbers were assigned, and all existing source editions remain unchanged.

## Executive result

- **Paper10 v54 main and SI build cleanly and are ready for publication.** The main is 56 pages; the SI is 19 pages. Both PDFs were visually reviewed page-by-page via contact sheets. The main log has no warnings; the SI has only underfull-box warnings, with no overfull boxes, errors, or unresolved references. The MCS 2026 verifier passes.
- **Paper08 v49, Paper09b v5, and Paper10b v3 compile, but their generated PDFs are not promoted as release PDFs.** Each contains a visibly problematic overflow: Paper08's interval-certificate table overlaps its columns; Paper09b's lemma display and summary table overflow in the two-column layout; Paper10b's long EAA URL is clipped at the right margin. Their sources remain byte-identical to the current remote sources. No new version number was created to fix these issues.
- The correct latest 60-page Paper 11 baseline is **v66**, not v67. The v66 PDF in the current `papers/` path is 60 pages; v67 is already 49 pages. The v66-to-v67 changelog explicitly documents the consolidation and the transfer of technical material to a 35-page, S1–S24 supplementary PDF. No restoration is warranted solely to recover a 60-page main PDF.

## Build method and source identity

All builds used the previously verified Tectonic 0.15.0 binary (`/tmp/tectonic-bin/tectonic`; SHA-256 `f0b36e78c13dd75b821984830533f872c9a12c62957e51357bc16e65cdb71013`). Each local TeX source was byte-compared with its current `e2-v3-source-year` remote counterpart before compiling:

| Edition | Remote source blob | Local/remote bytes |
|---|---|---:|
| Paper08 v49 main | `956b050cf0d6919b862a88a03ad0becffd0013c3` | 343,547 |
| Paper09b v5 main | `e7c13c59f1228508b5f918c6c31a956aad838807` | 56,045 |
| Paper10 v54 main | `5c1cf71376da9dc647ca3876077f4d90affef235` | 243,404 |
| Paper10 v54 SI | `5116c95681288e33f676e978541969e9b3a9a0e6` | 74,492 |
| Paper10b v3 main | `fd0d0c4b75c8e2c518b891c8173e3156704ef47c` | 75,203 |

The three external figure dependencies were missing from the local candidate folders but were found on the same remote branch and fetched byte-for-byte into temporary build folders. No source file was edited and no duplicate figure asset was added to the repository:

- Paper08 v49: `figs_p4/fig2_five_regime_topology_v2.png` and five `figs_p5/` images; remote blob IDs include `d24b6fb12cc548402b17d0a0481845f20f422969`, `00b6dfbe400cb4043a1dbb67f0dda1b1c3d32bbf`, `2c0b58ec89f6fba99efa7577993de83a28b09432`, `f2f37234ffb3b5682a5d50869342773285eabd07`, `b1bc092ade3df1ec2f90a5e23bcaea4e9a4de6d4`, `2d8c1b8ed71794185f81e1dff40de536034507bc`.
- Paper09b v5: `figs_arv/fig_record.pdf`, remote blob `d7ce0274571e3a3e48e0a87b5790edf90dd5a2b6`.
- Paper10b v3: `figs_e4/fig1_attractors.png`, remote blob `d2a461419aaa83bed94f13221536f70d33315e90`.
- Paper10 v54 main/SI: no graphics or input-file dependencies were referenced in the checked sources.

The assets exist remotely, but are not co-located with the relevant source-only paper files/packages. A clean clone/build should stage those known assets at the referenced relative paths.

## Build/readiness results

| Edition | Build result | PDF check | Warnings / disposition |
|---|---|---|---|
| Paper08 v49 main | Compiled; no LaTeX error or unresolved reference/citation | 87 pages; 47,601 extracted words; no blank pages | 11 overfull-box warnings. On p.18 the interval-certified longtable visibly overlaps its columns and is not legible. Tectonic also warned about an invalid UTF-8 byte in its bundled `lineno.sty` (package file, not source). **Do not promote this PDF until layout is repaired in a properly versioned revision.** |
| Paper09b v5 main | Compiled; arithmetic verifier **PASS** (source rows, 70 xteNCAM band pairs, tonnes-to-kt conversion, thresholds, both accounting identities) | 9 pages; 7,688 extracted words; no blank pages | Two overfull boxes: 332.8 pt in the conditional-multiplier lemma display and 111.7 pt in the three-column summary table. Sampled p.3 and p.8: the lemma display is clipped/illegible and Table 3 spills into the adjacent column. **Do not promote this PDF until layout is repaired in a properly versioned revision.** |
| Paper10 v54 main | Compiled; MCS 2026 verifier exited successfully | 56 pages; 31,636 extracted words; no blank pages | No LaTeX errors, unresolved references/citations, or overfull/underfull boxes. Contact sheets of all pages inspected; no visible clipping or overlap. **Ready; PDF and build log published.** |
| Paper10 v54 SI | Compiled | 19 pages; 8,847 extracted words; no blank pages | Six underfull-box warnings only; no overfull boxes, errors, or unresolved references. Contact sheets of all pages inspected; no visible clipping or overlap. **Ready; PDF and build log published.** |
| Paper10b v3 main | Compiled; 660-ft bootstrap verifier completed 5,000 draws (`noncontractive=0`, `gamma>=0=0`); regenerated CSVs byte-match their remote copies | 18 pages; 9,668 extracted words; no blank pages | Two overfull boxes (114.5 pt at the EAA Critical Period URL; 64.0 pt in the code-availability paragraph). Sampled p.16 shows the URL cut off at the right margin. **Do not promote this PDF until layout is repaired in a properly versioned revision.** |

Paper07 v54 was not rebuilt because its main/SI PDFs and build logs are already present on the remote branch. Paper11b v2 is preserved but excluded from this active build batch: it is a historical Edwards component already superseded/represented in the Paper11 v66/v67 lineage and the current E3 line, not a current source-only edition.

## Paper11 page-count investigation

The comparison was made against repository artifacts rather than inferred from a version label:

| Artifact | Branch/path | Pages | Extracted PDF words | Blob / note |
|---|---|---:|---:|---|
| Paper11 v64, `b11/` PDF | `e2-v3-source-year` | 60 | 32,701 | `a3e439c86aed51b97ed55303f771797aac7833cb` |
| Paper11 v65 PDF | `e2-v3-source-year`, `papers/` | 60 | 33,020 | `814863e591826b06511a2c84c94de59b8fcc21e9` |
| **Paper11 v66 PDF** | **`e2-v3-source-year`, `papers/`** | **60** | **32,982** | **`57ead69986cbe9ebdfa580cba8cd36f6497e76a6`** |
| Paper11 v67 PDF | `e2-v3-source-year`, `papers/` | 49 | 18,520 | `4d6795042b4e9492314cc9ec7b8c235fffed1fbb` |
| Paper11 v67 SI | `e2-v3-source-year`, `papers/` | 35 | 11,579 | `8cedac6d7e84cfbc8770315ded697c52484d3499` |
| Paper11 v68 PDF / SI | `main`, `paper rewrites/latex/` | 49 / 36 | 18,528 / 12,072 | v68 is not the 60-page baseline |

There are also alternate v64/v66 compile copies in archival directories; the `papers/` v66 PDF is the latest pre-v67 main artifact and is 60 pages. The v67 build changelog (`paper11_forecasting_baselines_v67_CHANGELOG_v66_to_v67.md`) explicitly identifies the lineage: v66 bound together the Northern cod ladder (Part I, essentially PaperE1 v60) and the Edwards study (Part II, Paper11b v2), with duplicated introductions/methods/discussions/conclusions and a short unsupported cross-system coda. V67 became one research article with a unified design and synthesis.

The changelog maps the main-text reduction to a new S1–S24 supplementary apparatus: derivations, protocol transcripts, fixed-window tables, variant passes, counterfactuals, service-series scoring, climate fixed windows, and reproducibility records moved to SI. The SI grew from the v66 Markdown companion (1,900 words) to 11.3k body words and a compiled 35-page PDF (11,579 extracted words). The main PDF fell from 60 to 49 pages, while the combined v67 main+SI is 84 pages. The changelog's body-word accounting is 30.9k (v66) versus 14.3k main + 11.3k SI (v67): some reduction is genuine consolidation/compression, not a one-for-one transfer of every old page.

A specific old cross-system explanation—that cod failed because apparent surplus production was weakly autocorrelated—was withdrawn because the measured autocorrelations were high (0.75, 0.71, 0.91 under the reported definitions). V67 replaces it with the increment-decomposition result and a scoped synthesis. This is a correction, not content to restore. The supported E3 details are in SI S15–S22. **Finding:** no scientific result merits restoration solely to recreate a 60-page main PDF; restore only if a specific load-bearing result is shown to be absent from both v67's main text and SI, not merely because the main PDF is shorter.

## Publication record

The v54 main/SI PDFs and dated Tectonic logs are stored locally in `/home/user/portfolio_work/paper10/` and are published under the established v54 filenames on `e2-v3-source-year`. The other three candidate PDFs were retained as build diagnostics only and were not added to canonical paths because their visible layout defects make them unready. No existing editions, sources, or assets were overwritten or deleted.

# ECOMOD v45 — citation, framing, and SI verification follow-up

**Date:** 2026-10-25  
**Status:** Local working follow-up only. This is not a public or approved release; nothing was committed, pushed, or published.

## Deliverables

- `ECOMOD_v45_citation_framing_SI_verified_20261025_main.pdf` — main manuscript, 35 pages, US Letter.
- `ECOMOD_v45_citation_framing_SI_verified_20261025_SI.pdf` — supplementary information, 20 pages, A4.
- Matching assembled TeX sources are included as `..._main.tex` and `..._SI.tex`.
- `parts/`, `figures/`, the two main-text figure assets, and `assemble.py` are included for a local source rebuild. The packaged TeX files compile directly; rebuilding from editable parts is also possible.
- `logs/` contains the final Tectonic logs. `AUDIT_NOTES_ECOMOD_v45_citation_framing_SI_verified_20261025.md` records the substantive checks and their scope. `SHA256SUMS.txt` fingerprints the package files (excluding itself).

The selected result-style title is **“Aggregate biocapacity does not identify its composition: a two-land model of ecological-capital drawdown.”** The SI uses the same title.

## Citation-key mapping retained

| Key | Companion |
|---|---|
| `Abaee2026a` | Paper4 — governance / institutional feedback |
| `Abaee2026b` | Paper06 v71 — assessment / transition criteria |
| `Abaee2026c` | Paper3 — material ledger |

The main bibliography and SI retain that mapping. Paper3 is pinned to public repository commit `2efaa62083f2007dec3446c15c475af88f0925f3`; its footnote discloses the PDF v50, README/checksum v49, and TeX-header v48 mismatch rather than treating the version labels as consistent.

## Build and QA

Built with Tectonic 0.17.0 using `--reruns 2` (three TeX passes per document). The PDFs were independently rebuilt from the packaged TeX sources and assets. Final extracted text contains no unresolved `??` markers; page counts and page sizes match the deliverables.

Visual review included the main title page; the Paper3 metadata footnote; main Table 2(a), including the `E_{ceil}` heading/value; the NFA anchor; the narrowed Theorem 4(iii) discussion; Half-Earth framing; companion references; SI title, Eq. (18), Theorem 4(iii), SI pp. 6–8 (including Tables S4 and S6), and SI references. The final §S4.2 comparison now starts on SI p. 7 as a complete sentence; p. 6 also ends on a complete sentence.

The build has non-fatal TeX box warnings: one 2.608 pt overfull box during main-page output and underfull boxes in text/table lines. The inspected pages show no clipping or material readability issue. See `logs/` for the full logs.

## Rebuild

From this directory:

```bash
python assemble.py
tectonic --reruns 2 manuscript_working_main.tex
tectonic --reruns 2 manuscript_working_si.tex
```

Or compile the included assembled `ECOMOD_v45_..._main.tex` and `ECOMOD_v45_..._SI.tex` directly. A TeX installation with the required packages and the local `figures/` assets is needed. The package is a TeX-rebuild package; it does not include the underlying empirical workbooks or model-run datasets needed to recompute analyses or regenerate all figures.

## Scope and preservation

Table S4's reported `0.050` was retained after checking the deposited drawdown CSVs and the sampled-grid monotonicity; no pattern-based alteration was made. The paper's annual human-available-flow reservation is distinguished from Half-Earth's spatial conservation target. The manuscript does not claim a general coupled-model boom–bust threshold or restore the removed “no Allee threshold” statement. Earlier readability snapshots and historical packages were not overwritten; the prior restoration finalcheck files remain comparison artifacts, not the current PDFs.
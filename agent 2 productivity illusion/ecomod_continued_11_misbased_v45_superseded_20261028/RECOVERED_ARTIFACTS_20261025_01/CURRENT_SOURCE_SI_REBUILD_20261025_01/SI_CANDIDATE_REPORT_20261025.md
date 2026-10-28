# SI candidate comparison and current-source rebuild

## Files compared

- **Current staged `SI_verified` candidate:** `/home/user/ecomod_v45/output_v45_citation_framing_SI_verified_20261025/ECOMOD_v45_citation_framing_SI_verified_20261025_SI.pdf`
- **Citation-audit SI:** `/home/user/ecomod_v45/output_v45_citation_ack_audit_20261025/ECOMOD_v45_citation_ack_audit_20261025_SI.pdf`
- **Current main benchmark:** `/home/user/ecomod_v45/output_v45_citation_framing_final_QA_20261025/manuscript_working_main.pdf` and current main TeX/aux.

Both SI candidates have 20 pages. In both PDFs, `Abaee2026c` is **not cited or listed**. The current main’s mapping for that key is Paper3/the ledger companion (v50).

## Three requested checks

| Item | Current staged `SI_verified` | Citation-audit SI | Current main text |
|---|---|---|---|
| `Abaee2026a` | Paper4: governance-delay paper (v41) | Paper06: assessment paper (v71) | Paper4: governance-delay paper (v41) |
| `Abaee2026b` | Paper06: assessment paper (v71) | Paper4: governance-delay paper (v41) | Paper06: assessment paper (v71) |
| `Abaee2026c` | Not cited/listed in this SI | Not cited/listed in this SI | Paper3: ledger companion (v50; metadata ambiguity disclosed in main) |
| Balance-point citation | Eq. **(18)** | Eq. **(19)** | Eq. **(18)** is `A_c^*(E)` (`eq:Acstar`); Eq. (19) is the affine matrix `J` (`eq:J`) |
| Paper06 Theorem 4(iii) | Cites `Abaee2026b`; states an exact interval of diagonal-gap states falsely certified as safe and limits the non-safety result to the companion’s **witness-defined diagonal-gap region** | Cites `Abaee2026a`; says no positive-elasticity member is uniformly safe over a **specified acceptance-gap region**; it omits the explicit exact-interval statement and uses the reversed a/b mapping | Cites `Abaee2026b`; gives the exact interval and the **witness-defined diagonal-gap region** scope |
| Matches current main on all three? | **Yes** | **No** | Benchmark |

## Current-source rebuild

The SI was assembled from the current `parts/si_00.tex`, `parts/si_01.tex`, `parts/si_02.tex`, and `parts/si_refs.tex`; the referenced `parts/si_tab_*.tex` tables were inlined using the current assembler’s rule. A separate copy of the eight current `parts/si_*.tex` files and figure support assets is preserved beside the build. No existing source or PDF was changed.

- Assembled TeX: `REBUILT_CURRENT_SOURCE_SI.tex`
- Successful rebuilt PDF: `BUILD_02/REBUILT_CURRENT_SOURCE_SI.pdf` (20 pages)
- Build log: `BUILD_02/REBUILT_CURRENT_SOURCE_SI.log`
- The assembled TeX is byte-identical to the current staged SI TeX and the current root `manuscript_working_si.tex`.
- Extracted-text check: pypdf text from the rebuilt PDF, joined pagewise and split on whitespace (punctuation and symbols retained), is identical to the staged `SI_verified` candidate: 20 pages, 9,111 tokens, zero non-equal diff hunks, and pagewise whitespace-normalized equality.
- Against citation-audit SI: not equal; 20 pages, 9,105 tokens, 27 non-equal diff hunks. Thus the rebuild matches the staged `SI_verified` candidate in extracted content, not the citation-audit SI.
- The rebuilt PDF has no unresolved `??` markers. Tectonic completed successfully; the log contains underfull-box warnings and a transient resource-fetch retry, not a fatal build error.

## Conclusion

The current staged `SI_verified` SI and the current-source rebuild match the current main text on the three requested checks. The citation-audit SI does not. All build outputs and this report are newly named within this recovery subdirectory; no existing file was overwritten, deleted, or renamed.

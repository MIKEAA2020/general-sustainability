# ECOMOD submission figures — upload these files, under these EXACT names

The manuscript (`manuscript_ECOMOD_v38.tex`) embeds exactly two figures:

| File (upload under this exact name) | Figure | Source |
|---|---|---|
| `real_series_aggregation_face.png` | Fig. 1 — the aggregation face of the masking result (NFA, world, 1961–2022) | `reports/real_series_aggregation_face.png` (regenerable: `model_sims/real_series_aggregation_face.py`) |
| `composition_attribution.png` | Fig. 2 — measured land-type composition of the aggregate change | `reports/composition_attribution.png` (regenerable: `model_sims/composition_attribution.py`) |

## Why the exact names matter

`\includegraphics{real_series_aggregation_face.png}` and
`\includegraphics{composition_attribution.png}` resolve by filename. In the
v35 submission these PNGs were uploaded to Editorial Manager under the renamed
forms `Figure1_aggregation_face.png` / `Figure2_composition_attribution.png`,
so even a successful server-side compile would have found no figures. This
folder previously contained only the misnamed `Figure1_aggregation_face.png`
copy — that trap is removed; both PNGs here are byte-identical (md5) to the
ones the manuscript builds with.

## Editorial Manager upload recipe (v38)

1. **Manuscript item:** `manuscript_ECOMOD_v38.pdf` (the compiled 31-page
   PDF) — this is what the reviewer sees displayed. Do not rely on the portal
   compiling the `.tex`.
2. **LaTeX source items:** `manuscript_ECOMOD_v38.tex` + the two PNGs above
   (flattened, exact names). Since v38 the `.tex` is engine-adaptive, so even
   if EM's pdfLaTeX server compiles it, it builds cleanly (verified: 0 errors,
   0 overfull).
3. **Supplementary items:** the SI package
   (`03_SUPPLEMENTARY_INFORMATION_v2.md`, `04_FIGURE_CAPTIONS.md`,
   `05_REPRODUCTION_GUIDE.md`, `06_DATA_AVAILABILITY.md` from
   `analysis/deliverables/`) and, if the portal asks for the SI figures as
   items, the S-figure PNGs from `supplementary/FIGURES/` (S1–S13; S14 is the
   graphical abstract, S15 duplicates Fig. 1).

# ECOMOD submission package — the .tex is the Manuscript item

**Owner directives (v39-v41 rounds, 2026-10-04):** the portal requires the `.tex`
itself — a submitted PDF **cannot be relied on for display**. The upload must
therefore be arranged so the portal's own server-side compile of the `.tex`
succeeds and produces the displayed PDF. That is verified for
`manuscript_ECOMOD_v41.tex` under every engine a portal might pick.

## The three files that constitute the manuscript item

| File (upload under this exact name) | Role |
|---|---|
| `manuscript_ECOMOD_v41.tex` | **Manuscript** — the portal compiles this |
| `real_series_aggregation_face.png` | Fig. 1 — the aggregation face of the masking result (NFA, world, 1961–2022) |
| `composition_attribution.png` | Fig. 2 — measured land-type composition of the aggregate change |

The manuscript embeds exactly these two figures, by bare filename
(`\includegraphics{real_series_aggregation_face.png}`,
`\includegraphics{composition_attribution.png}`), and
`\graphicspath` lists `{./}` first — so the flattened single-directory layout
Editorial Manager stages resolves them. Upload all three files at the same
item level (LaTeX source item group), flattened, exact names, no subfolders.

## Why the exact names matter

In the v35 submission these PNGs were uploaded to Editorial Manager under the
renamed forms `Figure1_aggregation_face.png` / `Figure2_composition_attribution.png`,
so even a successful server-side compile would have found no figures. Both
PNGs in this folder are byte-identical (md5) to the ones the manuscript builds
with (`reports/real_series_aggregation_face.png`,
`reports/composition_attribution.png`; regenerable via
`model_sims/real_series_aggregation_face.py` /
`model_sims/composition_attribution.py`).

## Why the server-side compile will now succeed (v39 verification)

The v35 "manuscript not displayed" failure had two causes, both eliminated at
source since v38/v39:

1. **Engine mismatch** — v30–v37 were LuaTeX-only (`fontspec` is a fatal
   error under EM's pdfLaTeX). Since v38 the preamble is engine-adaptive via
   `iftex`: the pdfLaTeX branch uses `fontenc`/`inputenc`/`lmodern` only.
   *Verified:* Editorial-Manager simulation (flat directory: `.tex` + the two
   PNGs alone, `pdflatex -interaction=nonstopmode` x2): **0 errors / 0
   overfull (27 pages for v41), both figures embedded.**
2. **System-font absence** — the Lua/XeTeX branch's `DejaVu Serif` /
   `DejaVu Sans Mono` / `Latin Modern Math` are system fonts portal servers
   do not have. Since v39 each `\set*font` is guarded by
   `\IfFontExistsTF`, falling back to the distribution's bundled Latin
   Modern. *Verified by probe* (font lookups forced to fail): compiles
   green, figures embedded. So even a portal that compiles with
   Lua/XeTeX cannot fail on fonts.

There are **no** `\ref`/`\cite`/`\bibliography`/`\input` dependencies — the
file is self-contained, so even a single server pass yields a complete PDF.

## Optional companion PDF

If the portal offers a separate slot for a compiled PDF (or the owner wants a
copy for the record), upload `manuscript_ECOMOD_v41.pdf` (the 30-page
LuaLaTeX build; the tectonic chain compiles the same source green) there —
but the display must not depend on it; the `.tex` + PNGs above are what
the portal compiles.

## Supplementary items (unchanged from the v38 round)

(The v40 round restated the Declarations block per the owner: Data
availability at the Zenodo record, no funding, no competing interests, a
CRediT statement, and "AI declarations"; the v41 round removed the orphaned
supplementary-file bullet list that had sat under the References --- the
payload of the supplementary-material sentence deleted with the lengthy
data-availability statement --- none of which affects the compile or the
upload list above.)

The SI package (`03_SUPPLEMENTARY_INFORMATION_v2.md`,
`04_FIGURE_CAPTIONS.md`, `05_REPRODUCTION_GUIDE.md`,
`06_DATA_AVAILABILITY.md` from `analysis/deliverables/`) and, if the portal
asks for the SI figures as items, the S-figure PNGs from
`supplementary/FIGURES/` (S1–S13; S14 is the graphical abstract, S15
duplicates Fig. 1).

# ECOMOD continuation 2 — lineage and change record

- **New working version:** `ecomod_continued_2.pdf` / `ecomod_continued_2.tex`; SI companion `ecomod_continued_2_SI.pdf` / `ecomod_continued_2_SI.tex`.
- **Working-content parent:** the 35-page source-matched QA candidate at `/home/user/ecomod_v45/output_v45_citation_framing_final_QA_20261025/manuscript_working_main.pdf`, built from the then-current assembled TeX. The 33-page `ecomod_continued_1.pdf` remains preserved as the saved-on-PC reference; its SHA-256 is `e665f4e6673ebd5a35c91c9c5f8e90cb8bb6f061133f0b9479ba774aa05fc15a` and it is byte-identical to the release asset `manuscript_working_main.pdf`.
- **Title correction:** `How a rising biocapacity total can mask ecological-capital land drawdown: a two-land model`. This keeps the accessible “how/can” framing while replacing the ambiguous “ecological base” with the model-defined land class.
- **Metadata-note correction:** the Paper3 caveat now says accurately that at the pinned commit the v50 PDF is present, the manifest lists v49 files but omits v50, the README (dated 2026-09-19) has no explicit version label, and the v50 TeX header points to the v48 Markdown source. Citation pin remains `2efaa62083f2007dec3446c15c475af88f0925f3`.
- The SI title is synchronized with the new main title. No other manuscript prose or citations were intentionally changed in this pass.
- Existing source files, the 33-page baseline, the 35-page QA PDF, prior variants, and root checksums were left untouched. No archive/package was created.

Build from this directory with Tectonic 0.17.0:

```sh
tectonic --reruns 2 --outdir . ecomod_continued_2.tex
tectonic --reruns 2 --outdir . ecomod_continued_2_SI.tex
```

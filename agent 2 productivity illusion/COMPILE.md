# Compiling the Manuscript

**Manuscript:** `manuscript_ECOMOD_v40.tex`

**Since v38 the preamble is engine-adaptive** (via `iftex`) and the source is
pure ASCII; **since v39 the fontspec branch is guarded** (`\IfFontExistsTF`),
so every engine a journal portal might pick compiles the file:

- **LuaLaTeX / XeLaTeX** (recommended; the shipped PDFs are built this way):
  loads `fontspec` + `unicode-math`. Each font is guarded: if the DejaVu
  Serif / DejaVu Sans Mono / Latin Modern Math *system* fonts are absent
  (the portal-server case), the build silently falls back to the
  distribution's bundled Latin Modern (`latinmodern-math.otf` for math)
  instead of failing. Authoritative builds on machines that have the fonts
  are unchanged (verified: v38 and v39 shipped PDFs have identical text
  layers on all 31 pages).
- **pdfLaTeX** (journal-portal servers such as Elsevier Editorial Manager):
  loads `fontenc` T1 + `inputenc` + `lmodern` instead — the file compiles
  cleanly with plain `pdflatex` (verified: 0 errors, 0 overfull boxes).

This closes the v35 portal failure: v30–v37 were LuaTeX-only (`fontspec` is a
fatal error under pdfLaTeX), so portals that typeset the uploaded `.tex` with
pdfLaTeX produced no PDF at all ("manuscript not displayed"). v38 builds under
all three engines; v39 additionally survives a Lua/XeTeX portal that lacks the
system fonts.

## Editorial-Manager simulation (verified for v39 and v40)

The portal stages uploads **flattened into one directory** and compiles the
`.tex` server-side. Simulated exactly so (tex + the two exact-name PNGs alone,
`pdflatex -interaction=nonstopmode`, twice): **0 errors / 0 overfull /
27 pages (v40), both figures embedded**. The `\graphicspath` now lists `{./}`
first, so the flat layout resolves the PNGs explicitly (27 pp in v40 vs the 30 pp
LuaLaTeX build because lmodern is narrower; pagination difference is expected
and harmless).

---

## Recommended: `latexmk` (auto-runs the needed passes)

A `latexmkrc` is included that forces LuaLaTeX, so a plain `latexmk` just works:

```bash
latexmk manuscript_ECOMOD_v40.tex
```

or, via the Makefile:

```bash
make            # build the PDF
make view       # build then open it
make clean      # remove build artifacts
```

## By hand

```bash
lualatex manuscript_ECOMOD_v40.tex   # or: xelatex / pdflatex — all work
lualatex manuscript_ECOMOD_v40.tex
```

(There are no `\ref`/`\cite` cross-references — citations are manual — so
even a single pass yields a complete PDF.)

## Engine notes

| Command | Works? | Why |
|---|---|---|
| `lualatex manuscript_ECOMOD_v40.tex` | ✅ | fontspec + unicode-math branch (recommended) |
| `xelatex manuscript_ECOMOD_v40.tex` | ✅ | fontspec + unicode-math branch |
| `pdflatex manuscript_ECOMOD_v40.tex` | ✅ | iftex picks the lmodern branch (portal-safe) |
| `latexmk` (with the bundled `latexmkrc`) | ✅ | auto-selects LuaLaTeX |
| pdflatex in a **flat upload dir** (EM simulation) | ✅ | verified 0 err / 0 overfull / 27 pp, figures embedded |
| Lua/XeTeX with the system fonts **absent** | ✅ | `\IfFontExistsTF` guards fall back to bundled LM (probe-verified) |

(For v30–v37 the pdfLaTeX rows were ❌ — fontspec/unicode-math are
XeTeX/LuaTeX-only. v38 removed that restriction; v39 removed the
system-font dependency too.)

## Fonts (LuaLaTeX/XeLaTeX branch only)

Preferred, if installed as system fonts:

- `DejaVu Serif` — body text
- `DejaVu Sans Mono` — `\verb`/`\texttt`
- `Latin Modern Math` — math

**None of them are required**: if any is missing, the v39 guards fall back to
the distribution's bundled Latin Modern automatically (fontspec's default
faces; `latinmodern-math.otf` for math — both ship in every TeX Live). The
pdfLaTeX branch needs no system fonts at all.

## Figures

The build expects `real_series_aggregation_face.png` (Fig. 1) and
`composition_attribution.png` (Fig. 2), resolved through
`\graphicspath{{./}{reports/}{supplementary/FIGURES/}{graphical_abstract/}}`
(`./` first, so the flattened journal-upload layout works). If a PNG is
missing the build errors on the corresponding `\includegraphics`; rebuild it
with `python3 model_sims/real_series_aggregation_face.py` /
`python3 model_sims/composition_attribution.py`.

**Journal upload:** figures must be uploaded under these *exact* filenames
(flattened next to the `.tex`), see `reports/figures_for_submission/`.

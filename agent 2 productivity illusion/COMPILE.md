# Compiling the Manuscript

**Manuscript:** `manuscript_ECOMOD_v38.tex`

**Since v38 the preamble is engine-adaptive** (via `iftex`), and the source is
pure ASCII:

- **LuaLaTeX / XeLaTeX** (recommended; the shipped PDFs are built this way):
  loads `fontspec` + `unicode-math` with DejaVu Serif / DejaVu Sans Mono /
  Latin Modern Math, exactly as v30–v37 did.
- **pdfLaTeX** (journal-portal servers such as Elsevier Editorial Manager):
  loads `fontenc` T1 + `inputenc` + `lmodern` instead — the file compiles
  cleanly with plain `pdflatex` (verified: 0 errors, 0 overfull boxes).

This closes the v35 portal failure: v30–v37 were LuaTeX-only (`fontspec` is a
fatal error under pdfLaTeX), so portals that typeset the uploaded `.tex` with
pdfLaTeX produced no PDF at all ("manuscript not displayed"). v38 builds under
all three engines.

---

## Recommended: `latexmk` (auto-runs the needed passes)

A `latexmkrc` is included that forces LuaLaTeX, so a plain `latexmk` just works:

```bash
latexmk manuscript_ECOMOD_v38.tex
```

or, via the Makefile:

```bash
make            # build the PDF
make view       # build then open it
make clean      # remove build artifacts
```

## By hand (run 2–3 times so `\ref`, `\label` and the figures resolve)

```bash
lualatex manuscript_ECOMOD_v38.tex   # or: xelatex / pdflatex — all work
lualatex manuscript_ECOMOD_v38.tex
lualatex manuscript_ECOMOD_v38.tex
```

## Engine notes

| Command | Works? | Why |
|---|---|---|
| `lualatex manuscript_ECOMOD_v38.tex` | ✅ | fontspec + unicode-math branch (recommended) |
| `xelatex manuscript_ECOMOD_v38.tex` | ✅ | fontspec + unicode-math branch |
| `pdflatex manuscript_ECOMOD_v38.tex` | ✅ | iftex picks the lmodern branch (portal-safe) |
| `latexmk` (with the bundled `latexmkrc`) | ✅ | auto-selects LuaLaTeX |

(For v30–v37 the pdfLaTeX row was ❌ — fontspec/unicode-math are
XeTeX/LuaTeX-only. v38 removed that restriction.)

## Fonts needed (LuaLaTeX/XeLaTeX branch only)

- `DejaVu Serif` — body text
- `DejaVu Sans Mono` — `\verb`/`\texttt`
- `Latin Modern Math` — math

On a full Linux TeX Live these ship with the distribution. If a font is
unavailable, either install it or temporarily edit the `\setmainfont` /
`\setmathfont` lines in the preamble. The pdfLaTeX branch needs **no** system
fonts.

## Figures

The build expects `real_series_aggregation_face.png` (Fig. 1) and
`composition_attribution.png` (Fig. 2), resolved through
`\graphicspath{{reports/}{supplementary/FIGURES/}{graphical_abstract/}}` (and
the current directory). If a PNG is missing the build errors on the
corresponding `\includegraphics`; rebuild it with
`python3 model_sims/real_series_aggregation_face.py` /
`python3 model_sims/composition_attribution.py`.

**Journal upload:** figures must be uploaded under these *exact* filenames
(flattened next to the `.tex`), see `reports/figures_for_submission/`.

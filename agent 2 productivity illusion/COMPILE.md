# Compiling the Manuscript

**Manuscript:** `manuscript_ECOMOD_v34.tex`

**The one thing to get right: this document is LuaTeX-only.** Its preamble uses
`fontspec` and `unicode-math` and sets `\setmainfont{DejaVu Serif}` /
`\setmathfont{Latin Modern Math}`. These packages *refuse* to run under pdfLaTeX
(`pdflatex`) or plain `latex`. If you try, you get:

```
Fatal Package fontspec Error: The fontspec package requires either XeTeX or LuaTeX.
You must change your typesetting engine to, e.g., "xelatex" or "lualatex"
instead of "latex" or "pdflatex".
```

Use **LuaLaTeX** (preferred, what this project is set up for) or XeLaTeX.

---

## Recommended: `latexmk` (auto-runs the needed passes)

A `latexmkrc` is included that forces LuaLaTeX, so a plain `latexmk` just works:

```bash
latexmk manuscript_ECOMOD_v34.tex
```

or, via the Makefile:

```bash
make            # build the PDF
make view       # build then open it
make clean      # remove build artifacts
```

---

## By hand (run 2–3 times so `\ref`, `\label` and the figures resolve)

```bash
lualatex manuscript_ECOMOD_v34.tex
lualatex manuscript_ECOMOD_v34.tex
lualatex manuscript_ECOMOD_v34.tex
```

Run it a third time so the newly added Figure 1 (`\ref{fig:aggregation}`) and the
table cross-references (`\ref{tab:...}`) settle.

---

## Engine notes

| Command | Works? | Why |
|---|---|---|
| `lualatex manuscript_ECOMOD_v34.tex` | ✅ | fontspec + unicode-math supported |
| `xelatex manuscript_ECOMOD_v34.tex` | ✅ | fontspec + unicode-math supported |
| `latexmk` (with the bundled `latexmkrc`) | ✅ | auto-selects LuaLaTeX |
| `pdflatex manuscript_ECOMOD_v34.tex` | ❌ | fontspec/unicode-math are XeTeX/LuaTeX-only |
| `latex manuscript_ECOMOD_v34.tex` | ❌ | plain TeX — no fontspec |

---

## Fonts needed

The config expects these fonts (standard in a full TeX Live install; if missing,
LuaLaTeX will warn and fall back to a default):

- `DejaVu Serif` — body text
- `DejaVu Sans Mono` — `\verb`/`\texttt`
- `Latin Modern Math` — math

On a full Linux TeX Live these ship with the distribution (the `dejavu` and
`lm` font packages). If a font is unavailable, either install it or temporarily
edit the `\setmainfont` / `\setmathfont` lines in the preamble.

---

## Suggested workflow

1. `latexmk manuscript_ECOMOD_v34.tex`
2. Inspect `manuscript_ECOMOD_v34.pdf`.
3. Run `make clean` if you want to clear build artifacts (they are git-ignored).

The first build compiles the figure (`reports/real_series_aggregation_face.png`)
into Figure 1; if that PNG is missing the build will error on
`\includegraphics{real_series_aggregation_face.png}`. Rebuild it with
`python3 model_sims/real_series_aggregation_face.py`.

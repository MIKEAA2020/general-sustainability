# Portal compile failure — cause and fix

## What the portal's log actually shows

The portal took `Manuscript_ECOMOD_C20_A01.tex` and compiled it **on its own**, in a directory that contains only the `.tex` file. Three consequences, in the order they appear in your log:

1. `Citation ... undefined` — expected on a first pass; harmless. The bibliography is embedded, so these resolve on pass 2. They are warnings, not the failure.
2. `! LaTeX Error: File 'fig1_model_dynamics_C18_A01' not found.` — the source expects `figures/` and `inherited_C17/figures/`, populated by the code repository. The portal has neither, and the figures you uploaded are named `Figure_1.pdf` …, which the old source never asks for.
3. `! LaTeX Error: File 'inherited_C17/tables/model_bounds_rows.tex' not found.` → `Emergency stop` — the fatal one. The manuscript `\input`s nine table fragments that live beside the code, not beside the `.tex`.

So the failure is **missing sibling files**, not a corrupt PDF. The separately uploaded `Manuscript_ECOMOD_C20_A01.pdf` is fine; the portal rejected it after its own build failed.

## The fix: upload the portal-safe source

Two new files, single-file and self-contained:

| File | Use |
|---|---|
| `Manuscript_ECOMOD_C20_A01_portalsafe.tex` | replace the previous manuscript source in the portal |
| `Supplementary_Information_ECOMOD_C20_A01_portalsafe.tex` | replace the previous SI source, if the portal compiles it |

Both have:

- **All nine table fragments inlined** — no `\input`, no `inherited_C17/` dependency.
- **Guarded figure includes** — each figure tries `Figure_N.pdf` (the name you upload), then the internal name, then falls back to a captioned placeholder box instead of aborting. It can no longer hard-fail on a missing figure.
- Embedded bibliography retained; no BibTeX step.

## Verified here, in the two conditions that matter

| Condition | Main | SI |
|---|---|---|
| Compile with **no assets at all** (portal worst case) | 38 pp, 0 fatal errors, 0 undefined | 28 pp, 0 fatal errors, 0 undefined |
| Compile **with `Figure_1.pdf`…`Figure_S5.pdf` present** | **38 pp**, 0 fatal, 0 undefined | **31 pp**, 0 fatal, 0 undefined |
| Single pass only (how many portals build) | 0 fatal, 0 undefined | 0 fatal, 0 undefined |

With the figure files present the page counts match the deposited version exactly (38 and 31).

## Upload order that avoids the failure

1. Manuscript source slot → `Manuscript_ECOMOD_C20_A01_portalsafe.tex`
2. Manuscript PDF slot → `Manuscript_ECOMOD_C20_A01.pdf`
3. Supplementary slot → `Supplementary_Information_ECOMOD_C20_A01_portalsafe.tex` and/or `Supplementary_Information_ECOMOD_C20_A01.pdf`
4. Figure slots 1–3 → `Figure_1.pdf`, `Figure_2.pdf`, `Figure_3.pdf`; SI figures → `Figure_S1.pdf` … `Figure_S5.pdf`
5. Highlights, cover letter, response, graphical abstract as before.

Keep the file names `Figure_1.pdf` … `Figure_S5.pdf`: the guarded includes look for exactly those names first, so the portal's build will show the real artwork rather than placeholders.

The non-portal-safe originals remain in the package for the repository and the source ZIP; they are the files that need sibling assets and should not be given to a compiler that receives one file.

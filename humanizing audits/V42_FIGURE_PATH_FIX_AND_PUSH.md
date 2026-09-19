# V42 round record — the reported LaTeX figure error fixed (the missing `figs_p4` asset inside `latex/`)

**Task 101, 2026-09-19.** Owner directive: fix the reported compile errors on
`paper4_delay_dynamics_v40.tex` — *"Package pdftex.def Error: File
`figs_p4/fig2_five_regime_topology_v2.png' not found: using draft setting"* at
line 2050, with the matching *"LaTeX Warning: File … not found on input line
2050"* — then commit and push the previous round (Task 100) together with this
fix, and provide the repo paths.

---

## Part I — the diagnosis

### The reported error, reproduced and explained

The v40 tex (`arena agent 1/paper rewrites/latex/paper4_delay_dynamics_v40.tex`)
includes its single figure at line 2050:

```latex
\includegraphics[width=\linewidth]{figs_p4/fig2_five_regime_topology_v2.png}
```

with the preamble (line 35) declaring `\graphicspath{{../}}`. The png itself
lives at `arena agent 1/paper rewrites/figs_p4/` — **one directory above
`latex/`**. Consequently:

- **Compiling inside the repository's `latex/` folder** (how every wave-19–23
  tectonic build ran): graphicx falls back to the `../` graphicspath entry,
  `../figs_p4/fig2_five_regime_topology_v2.png` resolves, and the build
  succeeds — which is why the shipped `paper4_delay_dynamics_v40.pdf`
  (md5 `3d7f3c04…`, 45 pp) was always built clean, figure included.
- **Compiling the tex anywhere else** — an Overleaf upload of the latex-folder
  contents, a flat download of the tex, any compile context in which the
  parent `paper rewrites/figs_p4/` structure is absent — the path resolves
  nowhere and pdflatex raises exactly the reported `pdftex.def` error
  ("not found: using draft setting", interactive `H <return>` prompt), with
  the figure replaced by an empty draft box.

The `latex/` folder was self-contained for papers 1 and 2 (`figs_p1/` and
`figs_p2/` already sit inside it — the established in-folder pattern) but
**not for paper 4**: `figs_p4/` existed only at the parent level.

### The fix (purely additive — no frozen artifact touched)

`figs_p4/fig2_five_regime_topology_v2.png` is now committed **inside the
`latex/` folder**:

- `arena agent 1/paper rewrites/latex/figs_p4/fig2_five_regime_topology_v2.png`
  — a byte-identical copy of the parent-level original (sha256
  `a4bbddc6221476a9adbc0562ca5dc0a4e0ca0517572567f5420b379a4be6e058`;
  195,393 bytes; both copies verified equal).

No tex, md, or pdf file was modified: graphicx tries the direct relative path
first, so `figs_p4/…` now resolves inside `latex/` with no tex change; the
`{{../}}` graphicspath remains valid whenever the parent structure is
present. The shipped v40 md/tex/pdf and every frozen gate (references,
abstract, prior checksums) stand unchanged; the round's git delta is exactly
one new binary asset.

### Verification (this round, fail-loud)

1. **The user's exact scenario simulated** — a flat directory containing only
   `paper4_delay_dynamics_v40.tex` + `figs_p4/fig2_five_regime_topology_v2.png`
   (no parent fallback available): tectonic compiles **clean** (no
   missing-file error, no draft box), 45 pages, Figure 1 on page 27, and the
   PDF **text layer is byte-identical** to the shipped PDF's.
2. **Repo-context rebuild**: tectonic in `latex/` (now finding the png via the
   direct path instead of `../`) — clean, 45 pages.
3. **Pixel-identity chain at 100 dpi**: committed PDF page 27 == repo rebuild
   page 27 == flat build page 27 — `ImageChops.difference` bbox `None`, max
   pixel delta 0, zero nonzero pixels: the figure renders identically in all
   three contexts.
4. The shipped `paper4_delay_dynamics_v40.pdf` was restored after the
   verification rebuilds and md5-verified (`3d7f3c04…`).
5. All 11 P4 tex versions that reference this png (v30–v40) inherit the fix
   automatically (same path, same resolution mechanism).

### The remaining honest caveat

If the tex is compiled **truly standalone** — the tex file alone, with no
`figs_p4/` folder next to it — the figure still cannot be found (nothing
repo-side can fix a missing asset). The remedy in that case is to place
`figs_p4/` (now available inside `latex/` in the repository) alongside the
tex before compiling, e.g. uploading both to Overleaf.

---

## Part II — a red-herring investigation, recorded for honesty

The round began with an apparent second defect: the tex's figure environment
appeared (in grep/sed output) as `\begin{figure}tbp]` — a malformed
placement specifier that would typeset literal "tbp]" above the figure.
Investigation (minimal-document experiments rendered the stray text; the
shipped PDF contained none) closed with the discovery of a **session-tooling
display artifact**: the tool-output rendering layer eats the literal
two-character sequence `[h` (controlled test: `[htbp]` displays as `tbp]`,
`[h]` as `]`, `[hx]` as `x]`, while `[x]` survives). A byte-level `od -c`
inspection then confirmed the truth: **the v37–v40 tex files have always
contained the correct `\begin{figure}[htbp]`** — no defect ever existed, no
fix was needed, and the shipped PDFs were always clean. Recorded so the
investigation is auditable and so future rounds know that bracket-adjacent
readings of tex source in this channel must be `od`-verified before being
believed.

---

## Part III — the systemic finding (flagged, not acted on)

A full scan of every tex file in `latex/` found **45 distinct figure paths**
referenced. Fourteen resolve directly inside `latex/` (`figs_p1` recent
files, all `figs_p2`); **31 rely on the `../` graphicspath** — the entire
`figs_e1/` (7 paths, 36 tex files), `figs_e2/` (7), `figs_e3/` (5), `figs_e4/`
(1), `figs_p5/` (5 + 3 written `../figs_p5/…`), and 3 older `figs_p1` paths —
the same latent error class as the reported one, should any of those papers'
texs be compiled outside the repository structure. The remedy is mechanical
(one folder copy each, the pattern this round establishes for `figs_p4`), but
those papers belong to other waves/agents, so no action was taken unilaterally;
flagged here for the owner. (With `figs_p4` now committed, P4 is fully
self-contained: its tex references exactly one figure path.)

---

## Part IV — implementation record

- New file: `arena agent 1/paper rewrites/latex/figs_p4/fig2_five_regime_topology_v2.png`
  (sha256 as above; byte-identical to the parent-level original).
- Verification artifacts (sandbox-side, not committed): the flat-context
  build, the repo-context rebuild, the pixel-identity comparisons, and the
  controlled `[h`-eating display test.
- No manuscript, supplementary, tex, or pdf file changed; `git status` shows
  exactly the one new asset; the shipped PDF md5 re-verified after restore.
- This record; repo worklog Task 101; both commits pushed with the owner's
  PAT (Task 100's `539563f` first, then this round's — see the push record in
  the worklog).

## Honest residuals

1. The truly-standalone compile caveat (Part I) — user-side remedy documented.
2. The 31-path systemic finding (Part III) — awaiting an owner decision to
   commission the same fix for the E1–E4/P5/P1-older tex families.
3. The Zenodo deposit staleness and the Task-97 abstract-phrase decision —
   unchanged standing owner-level items.

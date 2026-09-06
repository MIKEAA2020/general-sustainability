# Wave 9 — Owner-Directed LaTeX/PDF Pass (Task 79)

Owner directive: provide LaTeX sources and compiled, error-free PDFs of all
nine papers, confined to `arena agent 1/paper rewrites`. Standing directives
carried in: revisions as new versions (nothing overwritten), no change-log or
meta-commentary in the journal articles, formal academic register, and no
change to any frozen verdict, score, kernel, boundary, spectral record, or
table value.

## Deliverables (all new files; every previous version untouched)

| object | new file | build |
|---|---|---|
| P4 v30 | paper4_delay_dynamics_v30.md | apply_batch9_p4_v30.py |
| P5 v25 | paper5_sampled_governance_v25.md | apply_batch9_p5_v25.py |
| P5 figure | figs_p5/fig1_crossing_record_v25.png | make_fig_p5_v25.py |
| LaTeX + PDF ×9 | latex/paper*.tex, latex/paper*.pdf | build_latex.py |

MD5s (byte-reproducible; every build run twice with identical output):
P4 v30 15c85c5f…, P5 v25 a75021e2…, figure v25 341ba748…; LaTeX bodies
(tex) E1 c82ad0cd…, E2 5cb881ff…, E3 2a536808…, E4 cfaf5639…,
P1 d024503d…, P2 59f565fe…, P3 ee0662e8…, P4 39555f6c…, P5 be6e316e….

## 1. The two latent defects the pass surfaced (fixed as new versions)

The conversion pass is a rendering stress test; it surfaced exactly two
latent presentation defects, both fixed non-destructively as new versions
before the build:

- **P4 §9.6 setext-heading accident (P4 v30).** The `**Status.**` paragraph
  (the scaffold-companion record statement, "These are registered, verified
  numerical records…") was followed directly by a `---` separator with no
  blank line between, so markdown parsers — including pandoc — read the pair
  as a **setext H2 heading**: the entire paragraph rendered as a section
  heading, and pandoc additionally duplicated it into the PDF bookmarks via
  `\texorpdfstring`. Fix: exactly one blank line inserted between the
  paragraph and the separator (line 529), so the paragraph stays a paragraph
  and the `---` becomes a horizontal rule as in the other papers. Verified:
  `grep -c texorpdfstring` on the built tex = 0 (the pre-fix symptom);
  the paragraph renders as `\textbf{Status.} …` body text; every table row
  and every other line asserted byte-identical in-script; line count 677→678.
- **P5 Figure 1 legend superimposed on the title (figure v25 + P5 v25).** In
  the v24 figure the four-entry legend row (anchored at
  `bbox_to_anchor=(0.5, 1.01)`) superimposed on the centred title "Crossing
  record of the logistic hold map" — the "complex unit-circle pair" and
  "real −1 multiplier" entries collided with the title words, making both
  unreadable. Fix (make_fig_p5_v25.py): the legend is re-anchored above the
  title (`(0.5, 1.17)`), so the figure reads, top to bottom: legend row,
  title, axes. **Data unchanged** — the registered crossing record of §3.3
  (protective exact stable [0.2, 200]; protective Euler stable [0.2, 2.306],
  real −1 at 2.306 yr; extractive exact unstable [0.2, 6.501], complex pair
  at 6.501 yr; extractive Euler unstable [0.2, 47.536], complex pair at
  47.536 yr, stable [47.536, 79.143], real −1 at 79.143 yr, unstable
  [79.143, 200]). VLM-verified: title fully readable with no overlap, legend
  above the title, no entry collisions, all four data rows and markers
  readable, no clipped elements. P5 v25 (apply_batch9_p5_v25.py) changes
  exactly one line (line 268): the Figure 1 image reference
  `figs_p5/fig1_crossing_record_v24.png` → `…v25.png`; the Figure 1 caption
  and all table rows asserted byte-identical in-script.

## 2. The LaTeX/PDF build (build_latex.py)

Pipeline per paper (E1 v14, E2 v21, E3 v15, E4 v13, P1 v22, P2 v12, P3 v31,
**P4 v30**, P5 v25):

1. **In-memory markdown fixes only** (the .md files on disk are NOT
   modified; exact-count assertions make these fail-loud):
   - E4: the literal-star notation `K*_phys`, `K*_inst`, the two closed
     formulas in `H*`/`K*`, and the seven remaining `K*` sites → inline math
     superscript-star notation (`$K^{\ast}$` etc.) — pandoc would otherwise
     mis-parse the literal stars as emphasis spans.
   - E2: the one table-cell `0.5K*` → `$0.5K^{\ast}$` (same class).
   - E1: the three-part state-equation display (122 pt too wide at 11 pt)
     wrapped in `\begin{gathered}` with a line break before the `a(S_t)=`
     cases part — content unchanged, one added `\\`.
2. **pandoc** markdown → LaTeX body.
3. **Post-processing:** the top `#` title → `\title{}` (pandoc's auto-label
   dropped); `\subsection{Abstract}` → a proper `abstract` environment
   terminated at the Keywords paragraph or the next heading; every pandoc
   implicit figure merged with its following bold "**Figure N.**" caption
   paragraph into a proper `\begin{figure}[htbp]` + `\includegraphics[width=
   \linewidth]` + `\caption{…}`; the "Prepared in the format of…" /
   methodology-note paragraph centred in small type; all remaining Unicode
   mapped to LaTeX macros (prose Greek, mathematical relations, sub- and
   superscript runs, accented reference names, the QED box, the script 𝔇,
   combining accents on β̂/γ̂/P̄).
4. **Fail-loud integrity checks** on every paper: the final tex is pure
   ASCII; no emphasis-span mis-parse symptom; merged figure count equals
   the markdown's figure count; **the numeric-token multiset is EXACTLY
   equal** between the (transformed) markdown and the final LaTeX body —
   frozen values cannot change in conversion (the digits absorbed by
   LaTeX auto-numbering — figure numbers and enumerate markers, both
   rendered identically by pandoc's machinery — are accounted for
   precisely); **no markdown word is lost** (only environment-infrastructure
   words and the two declared per-paper exceptions may be gained).
5. **tectonic compile**: exit code 0, no "Missing character", no TeX error
   lines; the log archived to wave9/logs/.

## 3. Results (all nine compile error-free; .tex byte-identical across two full runs)

| paper | pages | figures embedded | overfull hboxes | PDF | tex MD5 |
|---|---|---|---|---|---|
| E1 v14 | 20 | 4 | 65 (all ≤ 25 pt; pandoc minipage-table cells + dense tables) | 455 KB | c82ad0cd |
| E2 v21 | 19 | 7 | 1 | 684 KB | 5cb881ff |
| E3 v15 | 16 | 5 | 8 | 544 KB | 2a536808 |
| E4 v13 | 14 | 1 | 1 | 217 KB | cfaf5639 |
| P1 v22 | 23 | 1 | 1 | 323 KB | d024503d |
| P2 v12 | 20 | 0 | 1 | 163 KB | 59f565fe |
| P3 v31 | 40 | 0 | 2 | 283 KB | ee0662e8 |
| P4 v30 | 39 | 1 | 10 | 459 KB | 39555f6c |
| P5 v25 | 29 | 1 | 1 | 267 KB | be6e316e |

- Embedded-image audit (pdfimages): every PDF carries exactly 2 image
  objects per figure (PNG + its soft mask) — 8/14/10/2/2/0/0/2/2 across the
  nine, matching the figure counts. The figure references resolve to the
  newest wave-8/9 figures: P1 `fig1_witness_v22.png`, E2
  `fig2_kernel_vs_catch_v21.png`, P5 `fig1_crossing_record_v25.png`.
- Overfull hboxes are cosmetic warnings (the widest is 24.9 pt on E1, from
  pandoc's minipage-based table cells on the wide comparator tables; the
  rest are ≤ 10 pt); none is an error, none loses content, and the
  numeric-multiset check proves no value changed.
- The tex headers carry the regeneration instruction (edit the markdown,
  re-run the build script); compiles with tectonic and is compatible with
  pdflatex/xelatex.

## 4. Non-destructiveness

- The markdown sources on disk are untouched by the LaTeX build (the
  in-memory fixes are conversion-layer only, with exact-count assertions).
- The only new markdown versions are P4 v30 (one blank line) and P5 v25
  (one figure reference); P4's table rows and P5's table rows and Figure 1
  caption are asserted byte-identical in-script; no frozen verdict, score,
  kernel, boundary, spectral record, or table value changed anywhere.
- `git status` shows only new files; every previous version, every other
  folder (including ECOMOD), and every supplementary file untouched.

## 5. Verification summary

- make_fig_p5_v25.py, apply_batch9_p5_v25.py, apply_batch9_p4_v30.py each
  run twice → byte-identical outputs (MD5s pinned above).
- build_latex.py run twice → 9/9 papers OK both times; all nine .tex files
  byte-identical across the runs (diffed by MD5).
- VLM verification of the v25 figure: title fully readable, legend above
  the title, no collisions, all rows/markers readable (Section 1).
- P4's setext symptom re-checked on the built artifact: zero
  `\texorpdfstring` occurrences; the Status paragraph is body text.

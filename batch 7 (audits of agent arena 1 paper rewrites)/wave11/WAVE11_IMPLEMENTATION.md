# Wave 11 — Implementation Record (Task 81)

Owner directive (two parts, both confined to `arena agent 1/paper rewrites`):

1. **All 9 papers' PDF and LaTeX** carry the author front matter:
   Amin Abaee, Independent Researcher, amin_abaee@ut.ac.ir,
   ORCID 0000-0002-0019-1842, and the AI declaration "GLM (Z.ai), Qwen
   (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative
   review".
2. **Graphical-abstract fixes**: E2 middle-column lower box "the sentence
   zone rule holds... does not make sense"; E2 right-column lower box
   first and second sentence should swap; P4 right column move the review
   interval down just a tiny bit; P5 middle column move the
   prot·exact / prot·Euler / extr·exact / extr·Euler labels to the left.

## Part A — the graphical abstracts: root cause + the four fixes

### The root cause the owner's E2 feedback exposed

Diagnosing the E2 complaints pixel-precisely (matplotlib window extents;
1 data unit = 1 display px at 200 dpi) surfaced a **systemic latent defect
in the wave-10 generators**: the `vlines` box-text stacker drew each
box's line list **bottom-to-top**, so every multi-line text box in all
five graphical abstracts rendered in **reverse reading order** — the
bold headline sat at the *bottom* of its box and the detail lines above
it. (The ECOMOD house original places text with explicit coordinates,
bold headline on top; the wave-10 `vlines` port authored its lists in
reading order but stacked them inverted.) The owner's two E2 comments are
exactly the two boxes where a multi-line *sentence* is involved, so the
reversal made the text read as garbage:

- **Middle-column lower box** — rendered (top→bottom) "zone rule holds
  the LRP itself / hold the safe set; the critical- / zero catch and the
  moratorium". The owner quoted the top line: "the sentence zone rule
  holds... does not make sense". Wave-10 had *also* mangled the sentence
  itself (line-splitting dropped both the "from" in the paper's
  registered idiom "hold the LRP **from** itself" and the "cascade").
- **Right-column lower box** — rendered "than the frozen convention
  implied / the margin they must supply is smaller / the LRP is protected
  by good years": the margin sentence's two fragments in reverse order.
  The owner: "first and second sentence should swap" — i.e. the box
  should read the margin sentence first, in correct order, then the bold
  protected-by-good-years line.

VLM transcription of the crops confirmed the reversal before the fix
(e.g. E2 panel A's fact box read "can any catch policy hold the LRP? /
**the 1992 moratorium**"), and confirms correct reading order after it.

### The fixes (all in the wave-10 generators, documented in each docstring)

| Where | What |
|---|---|
| all five generators | **Root-cause fix**: `vlines` now renders its line list in reading order (first line on top, the ECOMOD house convention). One inserted block; the stack geometry is unchanged (identical slots), so no layout regression is possible — the wave-10 pixel audit passes unchanged on all five. |
| E2 panel B lower box | Restores the paper's registered abstract sentence **verbatim**: "zero catch and the moratorium / hold the safe set; the critical-zone and / cascade rules hold the LRP from itself" (bold headline on top; the wave-10 stale draft-ATTR remnants removed). |
| E2 panel C lower box | The owner-directed swap, with "they" resolved to "good years" (the paper's own Section-4 wording): "the margin good years must supply is / *smaller than the frozen convention implied* / **the LRP is protected by good years**". |
| P4 right column | The review-interval axis label "review interval T_r (yr, log)" moved down 8 px (y 238 → 230, "just a tiny bit"): its bbox top 247.1 was 3.1 px *inside* the protective strip above it (bottom edge 244); now 5.7 px of ink clearance. The middle column's "τ (yr, log)" keeps its wave-10 position — the owner scoped the instruction to the right column, and moving the middle label collides with the no-Hopf box text (audit-proven; the first attempt did exactly that and was reverted). |
| P5 middle column | The four row labels right-aligned at x = 588: they were centred at x = 560 with right ends up to x = 617.8, riding 24 px onto the strips' left end (x = 594, dark navy on green/red). Now 6 px clear of the strips, leftmost edge ≈ x 472, well inside the panel-B frame. |

### Verification

- **Byte-reproducibility**: every generator run twice; all 15 output
  files (5 papers × PDF/TIFF/PNG) byte-identical across the runs. Pinned
  MD5s: e2 pdf b168d8bbf2708423f0dd7bfb792541af · png be7768f93824fa64809d05a15a017303 ·
  tiff 6dbf998564bb782703f4e6600c2ca7b5; p1 pdf 9b61e125e07f65325df5ab1ebd4c529a ·
  png ec1f8c6067ea165613ff97b0010acea0 · tiff 0c9c1e2c911a077db99ff54e21739b34;
  p3 pdf a6d98f531d085529459dc34029ec3dca · png a2d82d24f83b20e1ca87bea2bf1f1360 ·
  tiff 76d0430a0c2398a68b4bf0078e8dd88e; p4 pdf b26eb875d2217de82eacc2708350ff92 ·
  png b71d5ee8039e62a9ce0e6e592d3c122f · tiff fce0f8779d45e4beee8bed1a9b72b574;
  p5 pdf 4299a065603c5d61e10a6edc460200b4 · png af104b13a40957e96095910a486b9e51 ·
  tiff 365b9bc443e7e6b50980d04866ad5aef. Sizes still asserted: PNG
  1328 × 531, TIFF 2656 × 1062 @ 400 dpi.
- **Layout audit**: wave10/audit_ga.py (out-of-figure / text-text /
  panel-edge) passes with 0 issues on all five generators; wave11's new
  audit_fixes.py adds the deterministic checks the wave-10 auditor lacks
  (text-vs-strip clearance, box reading order, exact label positions) —
  0 issues: P4 right-label top 239.1 (4.9 px clear of the strip at 244),
  middle label at its wave-10 position; P5 labels at x 472.4–588.0
  (6.0 px clear); E2 boxes carry the registered sentence and the swapped
  order with the wave-10 mangled wording absent.
- **VLM (all five PNGs)**: every multi-line box now reads naturally
  top-to-bottom (bold headline first); the E2 lower boxes transcribe
  exactly as specified above; no overlap or collision noted. Remaining
  VLM notes are pre-existing cosmetic items unchanged by this wave
  (P1: the FP_agg italic lines sit 4 px above the box's bottom border —
  house-compliant ≥3 px; P3: the wave-10-accepted schematic-bar
  crowding; P4: the Euler-artefact × marker sits on the strip by design;
  P5: the axis label sits 3.1 px clear under the extr·Euler strip).

## Part B — the author front matter for all nine LaTeX/PDF

`wave11/build_latex_author.py` = the wave-9 pipeline with exactly one
functional change: the title block now carries the author (byline
"Amin Abaee" with "Independent Researcher" beneath, a \thanks footnote
with amin\_abaee@ut.ac.ir, ORCID 0000-0002-0019-1842, and the AI
declaration). Every wave-9 fail-loud integrity check is inherited
(pure-ASCII body, numeric-token multiset exactly equal between markdown
and LaTeX body, no markdown word lost, figure counts match), plus two
new ones:

- **Body identity**: on the first run (wave-9 files present) each new
  tex was asserted byte-identical to the wave-9 output **after only the
  header-comment and \author substitutions** — so nothing in any paper
  body can have drifted. On the second run the rebuild was asserted
  byte-identical (idempotence). Both runs passed for all nine.
- **Author presence**: name, affiliation, email, ORCID, and the AI
  declaration asserted in every final file.

Results: 9/9 compiled error-free with tectonic (logs archived in
wave11/logs/); page counts unchanged from wave-9 (E1 20, E2 19, E3 16,
E4 14, P1 23, P2 20, P3 40, P4 39, P5 29 — the footnote did not push any
paper over a page boundary); overfull-hbox counts unchanged in character
(E1's 65 are the wave-9-documented cosmetic minipage ones; all others
≤ 10). VLM-verified page 1 of E2 and P4: byline and footnote render
exactly as specified, abstract follows, no overlap; the email renders as
amin_abaee@ut.ac.ir (confirmed on a 300-dpi crop; low-dpi VLM reads of
the underscore are transcription artifacts).

Pinned tex MD5s (byte-identical across both runs): E1 d94ba3e4a3…,
E2 689fe8d28a…, E3 89648f0e7f…, E4 2962dcc8d5…, P1 b3dfcb01d5…,
P2 7a3fd916fb…, P3 96954a9338…, P4 c6fe1ec5e2…, P5 b56525b715…

## Non-destructiveness

- **Papers, supplementaries, and figures untouched**: no .md, no
  supplementary, no figs_* file changed; no frozen verdict, score,
  kernel, boundary, spectral record, or table value restated in altered
  form anywhere (the GA texts now quote the papers' registered sentences
  *more* verbatim than wave-10 did; the LaTeX body is byte-identical to
  wave-9, machine-asserted).
- **Updated in place, with full recoverability**: the 9 latex/.tex+.pdf
  and the 15 graphical_abstracts/ files are regenerated under their
  canonical names (the owner's own ECOMOD practice for generated
  artifacts — the ECOMOD graphical abstract was regenerated in place
  v24 → v26). The wave-9/wave-10 originals remain exactly recoverable
  at commits 05b0fe7/da21eaa; the per-file diffs are surgical (tex: the
  5 header-comment lines + the one \author line; GA: the documented
  text/position changes above).
- Scope: everything confined to `arena agent 1/paper rewrites` + the
  batch-7 wave-11 records; ECOMOD and all other folders untouched.

## Deliverables

- `arena agent 1/paper rewrites/latex/` — 9 tex + 9 pdf with the author
  front matter (bodies byte-identical to wave-9).
- `arena agent 1/paper rewrites/graphical_abstracts/` — 15 files
  regenerated with the root-cause reading-order fix and the four
  owner-directed fixes.
- `wave11/` — build_latex_author.py, audit_fixes.py, logs/, this record.

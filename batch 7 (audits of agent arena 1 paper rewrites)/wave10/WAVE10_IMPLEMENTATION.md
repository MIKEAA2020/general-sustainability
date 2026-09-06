# Wave 10 — Owner-Directed Graphical Abstracts (Task 80)

Owner directive: provide graphical abstracts, as separate files, for P3 and
P4 as well as any other papers in `arena agent 1/paper rewrites` that
genuinely merit one. Journal spec: 531 × 1328 pixels (h × w) or
proportionally more, readable at 5 × 13 cm; preferred file types TIFF, EPS,
PDF, or MS Office. Standing directives carried in: confined to
`arena agent 1/paper rewrites`, revisions as new files (nothing
overwritten), no meta-commentary inside the artefacts, and no invented
values — every number in every abstract is the paper's registered value.

## Deliverables (all new files; every previous file untouched)

Five graphical abstracts, each in three formats (15 files) in
`arena agent 1/paper rewrites/graphical_abstracts/`:

| paper | narrative (3 panels) | PDF | PNG | TIFF |
|---|---|---|---|---|
| P3 v31 | one label, three numbers → the typed ledger → no weight hides a deficit | graphical_abstract_p3.pdf (c61538f2) | …p3.png 1328×531 (599251b6) | …p3.tiff 2656×1062 (b9e1f7a9) |
| P4 v30 | the delay sits in governance → two channels, opposite math → the review interval as control | graphical_abstract_p4.pdf (9f7e2e76) | …p4.png (fafa89ab) | …p4.tiff (fe7a3023) |
| P5 v25 | governance is periodic → the crossing record → stability does not transfer | graphical_abstract_p5.pdf (0c6aece1) | …p5.png (d2c3a904) | …p5.tiff (f70f761f) |
| E2 v21 | after the collapse → what catch can hold (91.6 kt) → when catch cannot help | graphical_abstract_e2.pdf (7dd2005d) | …e2.png (6efdba3b) | …e2.tiff (6458c75a) |
| P1 v22 | one number from many capitals → the witness → the separation | graphical_abstract_p1.pdf (3a6229fc) | …p1.png (15adccb9) | …p1.tiff (a4b344d3) |

Format compliance: PNG exactly 1328 × 531 px (h 531 × w 1328, 200 dpi);
TIFF 2656 × 1062 px at 400 dpi — the same aspect, proportionally more
(2×); PDF vector (preferred type; TIFF preferred type; PNG included as the
online preview, matching the ECOMOD precedent). All 15 files byte-identical
across two full runs (PDF creation/mod dates suppressed for
reproducibility).

## Merit assessment (which papers got one, and why the rest did not)

Implemented — P3 and P4 (mandated) plus P5, E2, and P1, each of which has
a self-contained three-panel pictorial story grounded in registered values:

- **P3** — the one-label/three-numbers confusion is the paper's opening
  image; the typed ledger and the noncompensation obstruction are both
  drawable without equations.
- **P4** — the two-channel stability window (Hopf pair near 3.7 and 150 yr
  vs the no-Hopf theorem) and the review-interval strip (6.5-yr
  restabilising crossing, Euler 47.5-yr artefact) are inherently graphical.
- **P5** — the crossing record is already the paper's Figure 1; the GA
  re-tells it (all four rows, the registered crossings 2.306 / 6.501 /
  47.536 / 79.143) with the sample-and-hold staircase and the
  operators-do-not-transfer verdict.
- **E2** — the 91.6-kt robust-catch dial against the LRP floor (884.6 kt)
  with the survival endpoints (0.91 at zero catch, 0.65 at 120 kt, CI
  [0, 87.1]) is the paper's policy punchline in one bar.
- **P1** — the aggregate-passes/floor-fails witness and the nested
  V_weak ⊃ V_typ sets with the impossibility region FP_agg are the
  separation theorem in pictures.

Declined, with reasons (recorded here):

- **E1, E3** (forecast ladders) — the papers' honest message is numeric
  (RMSE ladders, the negative certificate); their existing figures already
  carry the visuals, and a GA would re-render a table rather than tell a
  mechanism story.
- **E4** (Edwards intervention) — its mirror-verdict subtlety (reactives
  retained nominally) resists honest pictorial compression, and E2 already
  carries the intervention picture for the pair.
- **P2** (obstruction calculus) — pure theory with zero figures; every
  honest GA would either trivialise the theorem set or overload it
  (viability-theory notation is not interdisciplinary-readable at 5 cm
  height).

## Method (house style + fail-loud discipline)

- Generators: wave10/make_ga_{p3,p4,p5,e2,p1}.py — self-contained
  matplotlib banners in the ECOMOD house style (1328 × 531 px, 200 dpi,
  three tinted panel frames, auto-fitted text, FancyBbox boxes/arrows,
  the shared palette), each with fail-loud post-conditions: exact PNG and
  TIFF sizes asserted; PDF size asserted; MD5s printed.
- Every displayed number is the paper's registered value: P4 — Hopf window
  3.7/150 yr (interval-certified), loop gain 0.080 < 1, 6.5-yr
  Neimark–Sacker crossing, Euler 47.5-yr artefact, five-regime topology
  note; P5 — the §3.3 crossing record (2.306, 6.501, 47.536, 79.143),
  the 42-stock screen, the Northern cod case; E2 — r = 0.2369, K = 5000 kt,
  LRP 884.6 kt, 91.6 kt, 0.91/0.65 survival, CI [0, 87.1], 7-yr kernel
  horizon, 2K* = 1769.2 kt; P3 — the three-quantity separation and the
  three public-data applications (G3P / USGS / RAM); P1 — the
  every-weight witness and the FP_agg gap with nonempty relative interior.
  Bar charts and the staircase are explicitly labelled "schematic" and
  carry no numbers.
- Layout audit: wave10/audit_ga.py re-executes each generator's drawing
  body and measures every text's pixel bounding box — fail-loud on
  out-of-figure text, text-text overlap, or panel-edge crossing. All five
  pass with 0 issues. (The audit drove the design: 1 pt = 2.78 px at
  200 dpi, so stacked lines carry ≥ 3 px clearance, and every string is
  short enough that the auto-fit never bottoms out — a fit assertion
  makes over-long strings fail the build rather than overflow.)
- VLM verification of every PNG (readability, collision-freedom): P3 9/10,
  P4 9/10 (clean after the row-gap widening), P5 clean, E2 clean, P1 8/10
  (cosmetic border-crowding notes only; the pixel audit confirms ≥ 3 px
  clearances).

## Non-destructiveness

No paper, supplementary, figure, or LaTeX file was touched (git status
shows only the new graphical_abstracts/ folder and the new wave10/ record).
No frozen verdict, score, kernel, boundary, spectral record, or table value
is restated in any altered form — the abstracts quote the registered
values verbatim in pictorial layout.

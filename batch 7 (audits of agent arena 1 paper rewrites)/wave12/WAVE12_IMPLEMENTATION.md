# Wave 12 — Implementation Record (Task 82)

Owner directive (two items, confined to `arena agent 1/paper rewrites`):

1. **E2 graphical abstract, right column, last box**: "the lrp line
   should be at top."
2. **Advisory question**: "does paper 2 merit a constructive title?"

## Item 1 — E2 GA right-column last box: the LRP line moved to the top

### What changed

`wave10/make_ga_e2.py`, panel C lower box — the last box of the right
column (`box(876, 96, 422, 74)`) — had its line list reordered. The box
now renders:

```
the LRP is protected by good years          (bold, TOP)
the margin good years must supply is
smaller than the frozen convention implied  (grey italic)
```

(wave-11 order was margin-first with the bold LRP line at the bottom).
The three strings, their fitted sizes (7.0 / 6.6 / 6.6 pt), the box, and
the stack geometry are all unchanged — the vlines stacker's total height
is order-independent, so only the slot assignment changed. No other box,
panel, or generator is touched; the other four abstracts are
byte-identical to wave-11.

### Why this order

The wave-11 "swap the first and second sentences" instruction was issued
while every multi-line box still rendered **bottom-to-top** (the wave-10
vlines reversal bug) — it was a compensation for the reversed rendering,
and once the reading-order root fix landed it left the box's bold
takeaway on the *last* line. The owner's wave-12 directive restores the
headline-first ECOMOD house convention that every other box in all five
abstracts already follows (bold takeaway on top, supporting sentence
beneath). Both docstrings (`make_ga_e2.py`, `wave11/audit_fixes.py`) now
record this provenance.

### Verification

- **Byte-reproducibility**: `make_ga_e2.py` run twice; all three E2
  outputs byte-identical across the runs. MD5s (wave-11 → wave-12):
  pdf `b168d8bbf2708423f0dd7bfb792541af` → `d35012e244c08259d4de4003bcd37dbb`;
  png `be7768f93824fa64809d05a15a017303` → `1c776da5da90f73c92a2c5ef3328b995`;
  tiff `6dbf998564bb782703f4e6600c2ca7b5` → `513a0d5f83849e13bc4191fe38b7814a`.
  Sizes still asserted in-generator: PNG 1328 × 531, TIFF 2656 × 1062
  @ 400 dpi, PDF vector.
- **Layout audit**: `wave10/audit_ga.py` (out-of-figure / text-text /
  panel-edge) passes with **0 issues** on all five generators (E2 changed,
  the other four re-confirmed unchanged).
- **Targeted audit**: `wave11/audit_fixes.py` updated to assert the
  wave-12 order (bold LRP line's bbox bottom above the margin line's top;
  margin line above the "smaller" line; all three bboxes inside the box)
  — **0 issues**; its P4/P5 checks unchanged and passing.
- **VLM (rendered PNG)**: transcription of the last-box crop reads
  exactly "the LRP is protected by good years / the margin good years
  must supply is / smaller than the frozen convention implied", first
  line bold, no overlap, text inside the box; the full right-column crop
  transcribes all four boxes in reading order with no collisions and no
  text escaping any box.

## Item 2 — Advisory: does "paper 2" merit a constructive title?

Answered for both readings of "paper 2"; **no title change is merited
under either**. (No file was changed for this item.)

### Reading 1 — E2 (`paperE2_cod_intervention_v21.md`)

Current title: *"Robust viability of the 2J3KL limit reference point
under a surplus-production map: policy scoring, expansion, and when
catch cannot help."* **No — a constructive title is not merited.**

1. **The paper's own protocol forbids the constructive claim.** The
   frozen retention rule was deliberately recast as a dominance *partial
   order* rather than a selection filter because presenting the outcome
   as an adopted policy "would overstate it" (Definition 2.6's own
   rationale). A constructive title ("a robust catch policy for the
   2J3KL LRP", "a framework that holds the LRP") claims exactly what the
   protocol declines to claim: the scored verdict is that **no non-BAU
   policy dominates BAU**.
2. **The load-bearing results are negative certificates**: no
   non-BAU policy dominates BAU; every positive-catch rule's kernel is
   empty at the 5th-percentile class at T = ∞; the map is expansive at
   the LRP for every admissible K ≥ 2K* = 1769.2 kt, so certified
   kernels are empty beyond 7 yr. The constructive content (the 91.6-kt
   largest robust constant catch; the critical-zone and cascade rules
   holding the LRP from itself) is real but class-scoped (the informative
   10th-percentile class), and the paper itself documents a reading (the
   class-vacuity reading) that reverses under the depensatory refit.
   Headlining the constructive reading unconditionally would tie the
   paper's identity to its most scope-limited result.
3. **"When catch cannot help" encodes the paper's actual answer to its
   own question.** The Introduction asks: "Can any catch policy hold a
   collapsed stock's spawning biomass above its limit reference point
   when productivity is depressed? Or is the reference point instead
   protected by good years rather than by demand management?" The
   paper's answer is the second branch — the final abstract sentence and
   the GA's bold takeaway say it: the LRP is protected by good years. A
   constructive title would dodge the question the paper exists to
   answer.
4. **Series-register consistency**: the E-series is the honest
   scored-test series (E1: "Does a surplus-production ladder improve
   forecasts of Northern cod?" — answered no; E3 the same interrogative
   form at J-17). E2's declarative verdict clause is the series'
   counterpart voice.
5. **Discoverability of the constructive content is already carried** by
   the abstract's final sentence, the GA's bold line, and the keywords
   (harvest control rules, robust viability kernel, limit reference
   point) — the title's job is the verdict.

*Registered option (not implemented)*: the subtitle's middle term
"expansion" is the paper's internal jargon (the map's local expansion at
the LRP — the mechanism that empties certified kernels beyond 7 yr); if
a plainer subtitle is ever wanted, that is the candidate for
replacement — but the verdict clause should stay.

### Reading 2 — P2 (`paper2_obstruction_calculus_v12.md`)

Current title: *"An Obstruction Calculus for Viability under Incomplete
Observation."* **No change needed — it is already constructive in the
only honest sense available.** The title takes the instrument-naming
form ("An X for Y"), exactly parallel to mathematical obstruction
theory, where the *constructed object* is the instrument that certifies
nonexistence. The paper's own positioning: "The necessity side … has
lacked a comparable instrument. … We develop an obstruction calculus."
The contribution is the calculus, not a viability guarantee; the title
says precisely that.

Both readings converge: **keep the current titles.**

## Non-destructiveness

- No paper (`.md`), supplementary, figure, LaTeX, or PDF file touched.
- No frozen verdict, score, kernel, boundary, spectral record, or table
  value restated in altered form — the GA text strings are the same
  three registered lines as wave-11, re-ordered per the owner's
  directive.
- The three E2 GA files regenerate in place under their canonical names
  (the owner's ECOMOD practice for generated artifacts), with the
  wave-11 originals exactly recoverable at commit 314c939 and a surgical
  per-file diff; the other 12 GA files are untouched.
- Records: this file, the JOINT_AUDIT_EVALUATION wave-12 addendum, and
  the worklog Task 82 entry.

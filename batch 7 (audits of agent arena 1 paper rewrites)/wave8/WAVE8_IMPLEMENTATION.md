# Wave 8 — Owner-Directed Journal-Presentation Pass (Task 78)

Owner directive (verbatim points): (1) confine the work to `arena agent 1/paper
rewrites`; (2) seven discoverability/contribution keywords per paper; (3) P1
Figure 1 panel A's "intermediate weights" label repositioned (it superimposed
the dotted ρ₂ = 3 curve and the s₂ = 2 equation); the version-log paragraph
before each abstract removed; abstracts under 315 words; no questions as
italicised writing (the P2 instance); (4) each paper cites its supplementary
file in the manuscript text; (5) P5 Figure 1's full-width clipped title fixed;
(6)–(7) E2 Figure 2's BAU and 60-kt labels raised off the horizontal boundary
together with the maximal-robust-flat annotation.

Standing directives carried from the previous instruction: revisions as new
versions (nothing overwritten), no change-log/diary/meta-commentary in the
journal articles, no references to superseded manuscript versions, no naive
over-hedging (none found in scope — the in-scope hedges are legitimate scope
statements), formal academic register.

## Deliverables (all new files; every previous version untouched)

| object | new file | build |
|---|---|---|
| E1 v14 | paperE1_cod_forecast_ladder_v14.md | apply_batch7_wave8_e1.py |
| E2 v21 | paperE2_cod_intervention_v21.md | apply_batch7_wave8_e2.py |
| E3 v15 | paperE3_edwards_forecast_ladder_v15.md | apply_batch7_wave8_e3.py |
| E4 v13 | paperE4_edwards_intervention_v13.md | apply_batch7_wave8_e4.py |
| P1 v22 | paper1_assessment_separation_v22.md | apply_batch7_wave8_p1.py |
| P2 v12 | paper2_obstruction_calculus_v12.md | apply_batch7_wave8_p2.py |
| P3 v31 | paper3_material_ledgers_v31.md | apply_batch7_wave8_p3.py |
| P4 v29 | paper4_delay_dynamics_v29.md | apply_batch7_wave8_p4.py |
| P5 v24 | paper5_sampled_governance_v24.md | apply_batch7_wave8_p5.py |
| P1 supp v3 | paper1_supplementary_v3.md | apply_batch7_wave8_supps.py |
| P3 supp v8 | paper3_supplementary_v8.md | apply_batch7_wave8_supps.py |
| P4 supp v5 | paper4_supplementary_v5.md | apply_batch7_wave8_supps.py |
| P1 figure | figs_p1/fig1_witness_v22.png | make_fig_p1_v22.py |
| P5 figure | figs_p5/fig1_crossing_record_v24.png | make_fig_p5_v24.py |
| E2 figure | figs_e2/fig2_kernel_vs_catch_v21.png | make_fig_e2_v21.py |

MD5s (byte-reproducible; every build run twice with identical output):
E1 c0b11a69…, E2 2b2c0eaf…, E3 48a856d4…, E4 cc9509b4…, P1 5ffb3f95…,
P2 84cf136a…, P3 491e5dd2…, P4 fab85c5e…, P5 c2e325ba…; supp v3 53871fd2…,
v8 59490ee3…, v5 8b017081….

## 1. Version-log removal

Every paper's `*Version log (vN).*` paragraph(s) before the abstract are
removed (E3 carried four: v11–v14). The record of what changed and why lives
in the repository (the wave records and the worklog), not in the journal
article. In-body version-history narration was recast at every site found by
the remnant battery:

- E1: "completions recorded at this revision" → "recorded after the scores of
  Section 3 were computed" (the load-bearing protocol disclosure kept); the
  DM-layer echo "as the completion records" → "as the protocol disclosure
  records".
- E2: the abstract's "now hold … so the earlier geometry-based verdict does
  not survive" → a present-tense convention comparison; "*Why the filter
  vocabulary is retired.*" → "*Why the filter vocabulary is not used.*";
  "demoted to definitional notes" (three sites) → "stated as definitional
  notes" / "a definitional note rather than a numbered result"; §4's "The
  earlier claim that boundary-harvesting rules are …" → "The
  boundary-harvesting rules' … reading under the frozen convention is …".
- E3: the climate-rung comparator deviation loses "corrected in this
  version" / "Earlier versions of this paper declared…" / "This version
  corrects…" — the deviation record now states the comparator declaration,
  why declaring M2m as the gate would be circular, and that the choice
  changes no frozen verdict; "the owner-archived script" → "the archived
  script" (two sites).
- P2: the abstract's italicised question and the Introduction's italicised
  question recast declaratively; the exists-strategy quantifier-order remark
  loses its "of the earlier version was circular … replaced" clause (the
  mathematical rationale kept); the EViab withdrawal loses "at this revision
  … recorded in the version log"; the symbol table loses "the fraktur
  information symbols of earlier versions are retired".
- P3: the three "(re-lettered from …)" notation parentheticals → present
  tense ("chosen so that …" / dropped); the §3.1 numbering note loses
  "audited demotions"/"demoted Theorems" (the two-counter declaration kept);
  "neither a demotion of the number" → "(both recorded)"; "now supplied and
  re-verified" → "supplied and re-verified"; the supplementary pointer's
  "pre-v28 status words … demotion relabels" → "the supplementary's status
  words to the main text's current labels".
- P4: §7's "an earlier reading of this section … was a label error and is
  superseded by …" → the positive label-fixing statement; §9.6's "the three
  records that earlier versions of this section carried as unreproducible"
  → "the three records that entered the archive as unreproducible … whose
  generating code and result files have been recovered" (artifact
  provenance, present tense); the supplementary paragraph's "predates the
  rebuilt…" → "describes the pre-rebuild state…; the status note, S12,
  records the current state"; the S10 parenthetical's "pre-v25 labels" →
  the S12 label mapping.
- P5: "is now complete" → "is complete"; "(…reproduces the registered
  numbers before extension)" → "(…it reproduces the registered numbers on
  the range they cover)"; Appendix A's "previously carried in the main flow"
  → "out of the Methods".
- Supplementaries: P1's S8 "Appended at the wave-4 revision (main-text v20)…"
  preamble and trailing "Revision note (wave-7 build, v21)"; P3's S6 "Appended
  at the wave-5 revision, when the main text stood at v29…v28…pre-v28"
  narration (the mapping table, the two-counter declaration, and the
  status-word resolution all kept, with the one header cell "main text's
  label since v28" → "main text's current label"); P4's S11 "Appended at the
  wave-4 revision (main-text v27)…v26" preamble, "per the wave-4
  relocation", S12's "(dated at the wave-7 build)" and "pre-v25 statement
  labels". The P5 supplementary carries no process narration and is
  unchanged.

The three remaining "demotes" hits (E2 §3.11, E4 §8, P3 §1) are present-tense
scientific usage ("nothing here promotes or demotes any forecast module";
"neither demotes stocks"), not version history — kept. The data-version
strings (RAM Legacy v4.44/v4.66, G3P v1.12) are database versions, kept.

## 2. Keywords (7 per paper, discoverability + contribution emphasis)

- E1: + negative certificate (6 → 7).
- E2: + NAFO 2J3KL, + robust viability kernel (5 → 7).
- E3: + J-17 index well, + water balance (5 → 7).
- E4: + viability kernel, + groundwater governance (5 → 7).
- P1: + capital substitution (6 → 7).
- P2: + viability kernel, + output feedback (5 → 7).
- P3: unchanged (already 7, contribution-emphasising).
- P4: unchanged (already 7).
- P5: "stability" (bare, generic) replaced by sampled-data control and
  Neimark–Sacker bifurcation (6 → 7).

## 3. Abstracts under 315 words

E1 300 (untouched), E2 459→313, E3 322→312, E4 374→312, P1 299 (untouched),
P2 345→307, P3 281 (untouched), P4 256 (untouched), P5 354→310. The five
rewritten abstracts preserve every verdict, recorded value, caveat, and
scoping statement; the cuts are phrasal redundancy, duplicated framing, and
change-log-flavoured narration. Value-presence is asserted in each build
(the E2/E3/E4/P5 builds pin the frozen numbers; the table rows are asserted
byte-identical everywhere — the only table-line changes in the whole wave are
P3's two notation-table rows losing their "(re-lettered …)" cells and the P3
supplementary's one status-map header cell).

## 4. Questions as italicised writing

P2's two instances (the abstract's "— when can one certify that no
observation-based policy exists? —" and the Introduction's "when can we
*certify that no policy works* — …?") are recast declaratively. The remaining
in-text questions (E2's numbered research questions Q1–Q4, the plain-prose
motivating questions, the papers' question-form titles, and P3's
notation-table glosses) are plain-text journal conventions, not italicised
rhetorical questions — kept.

## 5. Supplementary citations in the manuscript text

P1 names `paper1_supplementary_v3.md` (§6.2 pointer, updated from v2); P3
names `paper3_supplementary_v8.md` (§11 pointer, updated from v7); P4 names
`paper4_supplementary_v5.md` (the supplementary-material paragraph, updated
from v4); P5 now names `paper5_supplementary_v5.md` (added to the
Supplementary-material statement — it previously cited "Supplementary
material … S1–S8" without the file). P2 and E1–E4 have no supplementary files
(the directive is inapplicable for them; recorded here).

## 6. Figures

- P1 Figure 1 → figs_p1/fig1_witness_v22.png: same geometry (the Q region,
  the strict legs, the ρ₁ = 3 / ρ₂ = 3 dotted threshold curves, the witness
  (6/5, 6/5) with leader, "outside FP₀"); the "intermediate weights /
  license both" annotation is repositioned into the clear interior band
  (centred at (1.55, 1.02)/(1.55, 0.90), inside the region it describes),
  the "s₂ = 2" leg label is horizontal under the top border at a clear
  spot, and every other label was nudged clear of its curve (the witness
  label previously grazed the ρ₂ curve). VLM-verified collision-free in
  both panels.
- P5 Figure 1 → figs_p5/fig1_crossing_record_v24.png: the clipped
  full-width title is replaced by a compact centred title plus a four-entry
  legend row (stable/unstable/complex unit-circle pair/real −1 multiplier)
  inside the figure width; the row labels use the paper's channel
  vocabulary (Extractive/Protective — the previous rendering's "Mobilising"
  mismatched the paper's own caption); the registered crossing record is
  unchanged (2.306, 6.501, 47.536, 79.143 yr; the exact protective channel
  stable throughout). VLM-verified.
- E2 Figure 2 → figs_e2/fig2_kernel_vs_catch_v21.png: same boundary curves
  (r = 0.2368694030002864, K = 5000, K* = 884.6, e_q10 = −80.8697790157355,
  constructive 91.59402037298193; the same T=∞ preimage recursion and T=1
  one-step scan); "BAU" and "60 kt / S1" are raised above the flat segment
  (y ≈ 930), the "91.6 kt: maximal robust flat catch" annotation sits at
  y = 985 with its leader to the constructive point, and "flat 240" (never
  visible in the previous rendering — its marker lies beyond the viable
  catch range) is placed clear above the curve's upper end. VLM-verified
  collision-free.

## 7. Non-destructiveness

No frozen verdict, score, kernel, boundary, spectral record, or table value
changed anywhere. Every build asserts the table rows byte-identical against
its source version (the two disclosed exceptions above). The E1 and P1
abstracts are untouched at 300/299 words; P3/P4 abstracts untouched. No
previous version was modified: `git status` shows only new files. Scope was
confined to `arena agent 1/paper rewrites` for all content edits (papers,
supplementaries, figures); this wave's build scripts and records are additive
entries in the batch-7 audit directory, and the repo worklog carries Task 78.

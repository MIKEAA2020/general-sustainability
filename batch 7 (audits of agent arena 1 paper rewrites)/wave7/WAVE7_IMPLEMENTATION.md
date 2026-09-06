# Wave 7 — Implementation Record (Task 77, 2026-09-08)

Owner directive (three parts): (1) verify the joint adjudication of diverging audit points for all papers;
(2) scan all papers for conceptual clarity, seamless flow, remnants and redundancy; (3) scan all papers for
consistent terminology, stylistic writing and syntax. Parts 2–3's accepted findings were implemented in nine
fail-loud, byte-reproducible builds; part 1's verification is DIVERGENCE_ADJUDICATION.md; the full findings
and dispositions are QUALITY_SCAN_FINDINGS.md.

## Builds (all non-destructive: no frozen verdict, score, kernel, boundary, spectral record, or table VALUE
changed anywhere; every pre-existing table row byte-identical except the seven disclosed label cells)

| Paper | New version | Script | MD5 | Headline edits |
|---|---|---|---|---|
| E1 | paperE1_cod_forecast_ladder_v13.md | apply_batch7_wave7_e1.py | 91f09b63… | critical-zone remnant; roadmap 3.5/3.6; SSE→MSE labels (×3, RMSE-arithmetic-verified); §4 duplicate clauses + paragraph split; reference hygiene (2024a/b, DFO-2010 drop, NAFC + Cadigan cited) |
| E2 | paperE2_cod_intervention_v20.md | apply_batch7_wave7_e2.py | 1b98afc9… | parenthesis closed; four-consequences; Table 6 captioned; roadmap re-named; 80–90→70–90 (×2); form-sensitivity class corrections (×2 — the pre-v15 remnants); Registered Schaefer; Regular entry |
| E3 | paperE3_edwards_forecast_ladder_v14.md | apply_batch7_wave7_e3.py | eb025e02… | "declined gate" label; Tables 4-and-7 pointer; RMSE owners (CSV-verified); citation dedupe; Author-B entry dropped; predictand dedupe + glosses; unit fix |
| E4 | paperE4_edwards_intervention_v12.md | apply_batch7_wave7_e4.py | 2ed109e6… | **mirror-verdict un-swap**; floors §2.2; 692.7→691.96 (panel-verified; 12.0-yr arithmetic unchanged at 11.98); gap coordination; **tables renumbered to appearance order**; BAU alias fence; 31.5%; positive-pumping; frozen-protocol record; EAA/Puente cited |
| P1 | paper1_assessment_separation_v21.md (+ supplementary v2) | apply_batch7_wave7_p1.py | 73d912eb… | witness menu; relative interior (Thm 5 + abstract, 298 words preserved); W₊ fence + display; novelty trim; tombstone; tuple→record (×4); weight family (×4); Daly cited + refiled; supp S1/S6 re-lettered + note |
| P2 | paper2_obstruction_calculus_v11.md | apply_batch7_wave7_p2.py | 1b872c9b… | Theorems 3-and-5; mechanism count; kernel compressions (×3); meta-narration drops (×3); Viab(V;U,Π_CE) displays; λ fence; robust certification; apposition/pointer fixes; spellings |
| P3 | paper3_material_ledgers_v30.md | apply_batch7_wave7_p3.py | 2b3ae4d6… | Daly entry; notation scoping (B-row, S/P, q, H^win); abbreviation discipline (ADH/SSB/F/USGS/MCS); six echo trims; paragraph split; referent fixes; curly quotes |
| P4 | paper4_delay_dynamics_v28.md (+ supplementary v4 S12) | apply_batch7_wave7_p4.py | f1a488de… | labled; Theorem 4.1 pointer; duplicate/narration trims (×4); Figure 1 cited; τ_m wording; ν scope; ζ/ς order; references refiled/harmonised; S3/S10 pointers; **S12 appended** (S3 pre-rebuild status note + label mapping) |
| P5 | paper5_sampled_governance_v23.md | apply_batch7_wave7_p5.py | 00d42840… | **operator-contrast orientation corrected** (the companion's window is delay-stabilising; the continuous-delay stability at τ = 1 yr was inverted); reconciliation re-scoped (records close at zero delay); abstract clause; notation dedupes; 200+ → 200; Figure 1 cited; B-Y cited |

Every script runs clean twice (byte-stable); the supplementary edits are idempotent-with-verification
("already present — verified, no write"). Each build's mechanical checks pin the frozen needles (body-only
counts, old-log-stripped), the table-row byte-identity (with the disclosed label exceptions), the abstract
word counts (E1 298, P1 298 preserved), and the post-edit vocabulary invariants.

## The two substantive corrections (both disclosed in the version logs)

1. **E4's mirror-verdict swap (v11 → v12).** The Introduction's companion sentence read "reactive rules
   retained there, none retained here" — exactly backwards against both papers' records (the cod companion
   retains nothing — its no-dominance outcome, correctly stated two paragraphs later in E4's own Discussion;
   the aquifer retains the reactive rules, nominally under the mildest floor class). The mechanism clause in
   the same sentence was already correct, which made the swap a pure label inversion.
2. **P5's one-plant operator contrast (v22 → v23).** §3.4 read the companion's certified Hopf window
   (3.666, 150.358) yr as a delay-destabilised window ("stable under continuous delay at τ = 1 yr < τ_-, the
   unstable window's lower edge"), inverting the companion's declared orientation (P4: the undelayed gated
   loop is already unstable — a stated Routh–Hurwitz violation — and the window is the delay-stabilised one:
   unstable for 0 < τ < τ_-, stabilising lower crossing, destabilising upper crossing). The inversion also
   manufactured the "open" zero-delay tension that §3.4's undelayed-limit paragraph then recorded: under the
   companion's actual orientation, λ > 0 is fixed, zero crossings lie strictly between 0 and τ_-, and the
   records close. Both paragraphs are corrected; no frozen record of P5 changes (ρ = 1.00035, the 6.501
   crossing, the Euler artefact readings, every table row stand as recorded).

## Non-destructiveness

No frozen verdict, score, kernel, boundary, spectral record, or table value changed anywhere in the nine
builds. The number-level changes are exactly three, all correction-of-print classes with verification:
E1's SSE→MSE *labels* (values untouched; the RMSE arithmetic proves the objective is the per-transition mean);
E4's 692.7→691.96 (the record's actual maximum annual mean — the 1992 value E4 itself prints two sentences
later and E3's Figure 1 prints; the ceiling arithmetic is unchanged at the corrected value); E2's 80–90→70–90
reading range (the conclusions' settled form). All table bodies are byte-identical except the seven disclosed
label cells.

## Records and registry

- wave7/DIVERGENCE_ADJUDICATION.md — part 1 (the 106-divergence verification).
- wave7/QUALITY_SCAN_FINDINGS.md — parts 2–3 (the per-paper findings and dispositions, implemented and
  declined-with-reason).
- JOINT_AUDIT_EVALUATION.md — headers updated to the nine new versions; the wave-7 addendum records the
  verification answer, the four missing (B)-block summaries (P5, E2, E3, E4), and the scan outcome.
- Declines stay declined with recorded reasons (QUALITY_SCAN_FINDINGS.md); the wave-5 registered-follow-up
  list is unchanged by this wave except for the two new registered items (P2's §5(d) symbol definitions;
  P5's S2 supplementary gloss drift — both noted for the next allowed pass).

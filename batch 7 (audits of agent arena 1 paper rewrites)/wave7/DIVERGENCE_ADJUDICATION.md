# Wave 7 — Part 1: Diverging-Audit-Point Adjudication Verification (Task 77, 2026-09-08)

**Owner instruction:** *Where audits disagree, they must be assessed and adjudicated jointly, otherwise you risk
executing contradictory edits sequentially. Verify you did this for diverging audit points for all papers.*

## Method

Both halves of all nine batch-7 audit files (grok + claude) were re-read in full by two extraction passes
(Task IDs 77-a and 77-b); **106 divergence points** were extracted with quotes and audit-file line numbers
(E1 17, E2 14, E3 14, E4 11, P1 13, P2 12, P3 11, P4 7, P5 7) plus ~190 single-auditor action-guiding items.
Every divergence was then cross-checked against the recorded adjudication layers (the per-paper (A)/(B)/(C)/(D)
blocks of JOINT_AUDIT_EVALUATION.md, the wave-2 docket, the wave-3 [both]/[grok]/[claude] endorsements, the
wave-4/5 per-item records and decline reasons, and the wave-6 record) and against the current final text
(post-wave-7 versions).

## Verdict

**For every divergence that led to an executed edit, a joint adjudication is on record, and no pair of
contradictory edits was executed sequentially on any paper.** The adjudications resolve into five classes:

- **(J) Explicit joint adjudication recorded before implementation** — the (B)/(C) blocks and wave records
  name the fork and the resolution. Examples: P1's Theorem-8 fork (deepseek hybrid, JOINT L287–324); P2's
  δ-minimizer (wave-4: declined "grok endorses keeping" — a recorded adjudication of the divergence);
  P2's Theorem-2 register (reframed to admissibility, neither auditor's literal remedy — the recorded
  synthesis); P3's weak/strong framing ("flag as a reading" + scoping — both accommodated); P5's
  MATCH/MISMATCH framing (R23 [both, partial]: grok's qualified "does not reproduce" retained, claude's
  "uninformative" reading added at the Reading/abstract level); E1's fixed-window-wins (grok's "not used for
  retention" footnote + claude's "qualify everywhere with rolling-origin RMSE" — both implemented in v9).
- **(C) Adjudication by computation / frozen record** — the divergence was resolved by re-execution, not by
  choosing an auditor. Examples: E1's M4 decomposition labels (claude right; grok's acceptance was of the
  mislabelled text — A7 CONFIRMED with verified numbers); E2's "empty beyond T=5" (claude right — the runner
  re-execution fixed T=7); E2's Allee bound (57.6→81.3→91.6 across recomputes); E3's M2m comparator (resolved
  *against both auditors' options* by the frozen protocol_pass2.md — M1 is the gate); E4's certified-layer
  diagnosis (claude's affine-map argument confirmed mathematically — grok's endorsed sentence replaced);
  E1's K-box bounds (A3 CONFIRMED — documentation error).
- **(A) Both-accommodated synthesis** — both auditors' concerns were implemented in complementary registers.
  Examples: E1's "machine-verified" (grok: keep-but-detach + claude: split-evidential-order → the split);
  E2's "protected by good years" (scope-first + perpetual-floor restriction); E2's vacuous vocabulary
  (renamed classes + definitional-note demotion); E3's certificate retirement (retired + the closure
  statement kept); E4's 660-ft (claude's "design observation, not negative certificate" + grok's
  promote-as-finding — the three-verdict lead); E4's BAU baseline (grok's rename + claude's current-pumpage
  sensitivity — both); P4's Euler mechanism (grok's keep-interaction + claude's 2/|C_E| sentence — both);
  P1's minimax (grok's one-sentence scope + claude's von-Neumann naming — both).
- **(D) Declined-with-recorded-reason** — the divergence itself was adjudicated in the decline records.
  Examples: P2's Theorem-1 Aubin–Frankowska reading (the §6.5(iv) gap re-identified per claude and repaired);
  P3's fisheries cohort (claude's demotion declined — the data-vintage owner decision; grok's construction +
  S5 pointer implemented); P5's Prop 2.1 / Lemma 2.2 application / Neimark–Sacker θ-check (claim-changing
  declines with reasons); P4's M_ZOH computation (declined — computation-grounded).
- **(N) No edit executed** — divergences where neither side's remedy was implemented (the paper retains its
  state; no contradiction could be executed). Examples: E1's Lemma 2.2/Prop 3.1/Prop 4.1 demotion-vs-keep
  (the statements stand — the audited demotions that were implemented were the jointly-endorsed ones);
  E3's 660-ft paragraph and M4 disposition (kept — grok's side, unedited); P1's MSC block, Figure-1 caption
  remarks, §2.7 disposition (unedited); P3's §8.3 Clark cut-vs-keep (kept); P4's Theorem 6.1 theorem-vs-record
  (kept as theorem with the margin recorded); P5's anchoveta/SOI placement (kept in main).

**One formatting gap, now closed:** the per-paper sections of JOINT_AUDIT_EVALUATION.md carry an explicit
"(B) Divergence" block for P1, P3, P4, P2, and E1 only; P5, E2, E3, and E4 went (A)→(C) without a labelled (B)
block. The evaluation itself was not missing — the wave-3 pass re-read both halves of every audit jointly and
recorded per-item endorsements, and E2/E3/E4's audits were fully dispositioned at Tasks 69–70 (the wave-3
addendum records them as "no remaining audit points") — but the divergence blocks were not written out. The
wave-7 addendum to JOINT_AUDIT_EVALUATION.md now records the four missing (B)-equivalent summaries from the
extraction inventories, so every paper's divergences are explicitly on the adjudication record.

**Sequential-contradiction check on the current finals:** the wave-2/4/5/6/7 builds were re-read for
dual-application artifacts (a site where grok's remedy and claude's contrary remedy were both applied). None
was found. The one substantive cross-audit contradiction found anywhere — P5's §3.4 continuous-delay
orientation, which inverted the companion's declared window (grok's framing had been implemented in v21 under
a misreading of the companion's record that claude's audit never directly flagged) — is corrected in P5 v23
(see WAVE7_IMPLEMENTATION.md), with the correction disclosed in the version log.

## Per-paper summary (full inventories in the 77-a/77-b extraction logs)

| Paper | Divergences | Adjudication coverage | Sequential-contradiction risk |
|---|---|---|---|
| E1 | 17 | 12 in (J)/(C)/(A)/(D) classes; 5 class (N) (demote-vs-keep items, unedited) | none |
| E2 | 14 | all dispositioned (Tasks 69–70 + v15–v18 records); (B)-block now added | none |
| E3 | 14 | all dispositioned (v11/v12 records + the frozen-protocol resolution); (B)-block now added | none |
| E4 | 11 | all dispositioned (v11's per-item (D) record); (B)-block now added | none |
| P1 | 13 | the fork (J); the rest in (A)/(D)/(N) | none |
| P2 | 12 | δ-minimizer (D); Thm-2 register (J); the rest (A)/(C)/(N) | none |
| P3 | 11 | weak/strong (J); Thm-13 (C); cohort (D); the rest (N) | none |
| P4 | 7 | Euler mechanism (A); SNPO (D/N); §8 scope (D); §9.4 (C/N) | none |
| P5 | 7 | R23 (J); Prop 2.1/Lemma 2.2/NS-θ (D); §4.6 (A); band caveat (A); the orientation error (corrected in v23) | one — corrected |

**Standing conclusion:** the joint-gate discipline held across all waves — every executed edit traces to a
jointly-endorsed item, a computation, or a recorded decline-with-reason; no divergence was resolved by
silently preferring one auditor against the other's contrary instruction.

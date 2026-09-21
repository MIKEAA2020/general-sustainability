# Batch-8 Paper-1 Queue — Re-Verification Against the Current Version, Remaining-Points Adjudication, and the Incorporation Plan

**Task 105 / batch 8 / paper 1 (*Ecological Indicators*).** Companion to `SIGMA_SPECTRUM_WAVE.md` (this round's other deliverable, which executes queue point 3.A-8's research half).

**Owner directives executed here.** (1) *Remaining points from the batch-8 audits worth adjudicating and incorporating in plan?* (3) *Reminder/standing rule: the streams were written against a v51/v52-era state and do not reference v52's own Gao et al. (2023) addition, §5.5's scope delimitations, or §5.1's information reading (all of which pre-answer several asks). Any future implementation round must re-verify each point against the then-current version — several may already be closed.*

**Re-verification basis.** The current version at repo commit `988042a` is still `paper1_assessment_separation_v52.tex` (1,817 lines) — the same version the Task-104 joint assessment verified against. Every status below was re-checked against the file directly this round (grep-level line evidence), not carried over from the audit streams.

---

## Part A — The standing re-verification protocol (recorded for all future rounds)

Before any implementation round touches the manuscript: (i) identify the then-current version file; (ii) for each queue point, re-run the point's line-level check against that version (the check is cheap: each point's evidence is a grep-able string, a reference-list lookup, or a theorem-label scan); (iii) mark the point CLOSED-IN-VERSION / OPEN / OWNER-GATED / OVERRIDDEN (standing) / REJECTED (standing); (iv) implement only what remains OPEN, as a **new version** (never overwrite), under the no-removal/no-condensing standing rule. Rationale (the owner's directive 3): the audit streams lag the manuscript; v52 already pre-answers several asks, and future versions will pre-answer more.

## Part B — The 42-point queue, re-verified against v52 (current)

Legend: **OPEN** = not yet in v52, worth incorporating (the implementation queue). **CLOSED** = already present in v52 (pre-answered; nothing to do). **GATED** = owner decision required before any implementation. **OVERRIDDEN / REJECTED** = permanent standing status (the no-removal rule; defective as written).

### 3.A Additions

| # | point | status | evidence / note |
|---|---|---|---|
| 1 | four-protocol table | **OPEN** | v52 has the five operators (§3.1) and the V-chain (§3.2) but no early orienting protocol table (P2-vs-P4 is the load-bearing distinction; nothing to grep — structural absence) |
| 2 | evaluation-semantics table (floors × tube/endpoint) | **OPEN** | §3.1 carries the prose chain and §3.1-end the typed-endpoint operator; the compact table is absent |
| 3 | Remark-2/Prop-3 interpretation box in §1/§5 | **OPEN** | §4.2 has the pointwise-losslessness point inline; the promoted box is absent |
| 4 | indicator-validity section + four design tests | **OPEN** | absent (§5.6 policy implications exist; the validity-tests section does not) |
| 5 | consolidated 10-point practitioner checklist | **OPEN** | absent |
| 6 | three-regime disturbance sensitivity (middle regime honestly unanalyzed) | **OPEN** | §5.5's coupled-shock delimitation states regime (iii)'s universal-rejection conclusion; the explicit 3-regime table with the middle cell marked unanalyzed is absent. Note: the middle regime (common biomass shock) still must be *computed*, not asserted (3.E-42 standing) |
| 7 | positioning additions (Becker 2017; EBFM literature; Table-2 fisheries column; **Gao et al. 2023**) | **PARTLY CLOSED** | **Gao et al. (2023) IS in v52** (line 151 in-text; full entry line 1719 with DOI) — that sub-item is CLOSED. Becker 2017, the EBFM cluster, and the Table-2 fisheries column: **OPEN** (absent) |
| 8 | **the σ-spectrum program as a labelled extension** | **RESEARCH HALF CLOSED THIS WAVE** | `SIGMA_SPECTRUM_WAVE.md` + verifier + log (this folder) deliver the exact witnesses, machine verification, and the relevance test; the audit-Thm-11 adjudication is upgraded (conjecture retired; two-sided punchline; LPI identification made precise — closing 3.E-40/41). The **manuscript subsection remains OPEN** for the implementation round (transcription sketch in the wave document §8) |
| 9 | reserve-stock institutional forms | **OPEN** | κ* = 1−x exists (Prop 11); the buy-back/quota-banking institutional mapping is absent |
| 10 | conservatism-invalidation caveats (depensation; heatwave amplification) | **OPEN** | absent from §6.1 limitations |
| 11 | dashboard-only-architecture disclaimer sentence | **OPEN** | §6.3 states the convention ("the reviewer checks the dashboard, not the floors") but not the not-a-claim-about-practice disclaimer |
| 12 | Filippov & Warga reference entries | **OPEN** | still cited at line 843 with no entries in the reference list (verified this round) |
| 13 | in-text citations for De Lara & Doyen 2008 / Rockström 2009 / Raworth 2012 | **OPEN** | all three remain reference-only (4 mentions total, none in-text; verified) |
| 14 | exact-DFO motivation paragraph | **OPEN** | the mid-1980s/swing statements remain unnumbered (the labelled-motivation-paragraph branch) |
| 15 | limitation paragraph before Theorem 9 | **OPEN** | §4.8 has the convexification-instrument caveat sentence; the pre-Theorem-9 implementability paragraph (fractional effort, monitoring, enforcement) is absent |

### 3.B Precision rewordings — all **OPEN** (they are edits; v52 unchanged)

16 (abstract "margin-reducible" qualifier on the Thm-6 sentence) · 17 ("no choice of weights repairs…" protocol qualifier) · 18 (abstract "rescuable from impossible" append) · 19 ("left comparatively open" softening) · 20 ("index green" → "index nonnegative") · 21 (endpoint-operator sentence generalization) · 22 (FP_agg first-use qualifier) · 23 (the unit-convention explicitness sentence at the cod anchor — the *corrected* variant; qwen's defective draft stays rejected) · 24 (critical-zone both-comparisons sentence: 0.6-LRP vs ⅓-LRP).

### 3.C Mechanical fixes — all **OPEN** (verified still present in v52 this round)

25 (reference ordering: Dasgupta & Mäler / De Lara; O'Neill / Rockström; Saint-Pierre / Schaefer / Schär) · 26 (§4.9 proof-list completion: Thm 6→App A, Prop 10→App B, Prop 11→App C) · 27 (Thm-9 qed outside the enumerate) · 28 (preamble: one `\emergencystretch` — 4 occurrences remain; the mailto underscore; unused `longtable` noted) · 29 (natural body uses for MSY/PROMETHEE — 3 occurrences remain, abbreviation-list only) · 30 (Fig-1 caption x=0 vs x=½ consistency sentence) · 31 (Thm-6-before-Thm-5 presentation note; renumbering = **GATED** — touches cross-references and the ledger).

### 3.D OVERRIDDEN (permanent standing) — 32–37

Reduce-intro-by-one-third; move-game-theory/shorten; move-framework-extensions; remove-historical-statements; wholesale abstract rewrites; title changes (the last **GATED** as framing, not content). No change: the standing rule overruns these; their additive intents survive via §3.A where one exists.

### 3.E REJECTED (permanent standing) — 38, 39, 42

qwen's §6.3 normalized-biomass draft; gpt's wholesale normalization; the asserted "Reduced/Shifted" middle-regime cell. **40 and 41 are now DISCHARGED by this wave** (not "rejected-as-asks" but resolved as research: the Thm-11(2) conjecture has its exact witnesses and is retired into Theorems S1/S2; the LPI identification is made precise with its two caveats).

## Part C — What v52 already pre-answers (the directive-3 ledger)

For the record, the three pre-answering bodies of v52 content (all verified present this round):
- **§5.1's information reading** (the ∃a∀w-vs-∀w∃a_w value-of-information paragraph, incl. the Thm-9/Prop-10 qualifications) — pre-implements the audit's pathway E to the extent the witness supports; the pathway-E "new theorem" ask reduces to what §5.1 already states plus the menu-convexity condition it already carries.
- **§5.5's scope delimitations** — pre-answer: pathway B's stochastic semantics (excluded by the no-stochastic delimitation — an extension ask, not a defect); pathway C's coupled shocks (the universal-rejection collapse is stated with the Lade 2020 pointer); pathway F's infinite horizon (excluded by the no-infinite-horizon delimitation); the menu-relative reading of the impossibility region ("No absolute impossibility"); the reserve-excluded-from-aggregate scoping.
- **The Gao et al. (2023) addition** (line 151 + 1719) — closes the composite-index-without-weights positioning gap the deepseek stream gestured at.
- **§5.1's CES/nonlinear disclaimer** ("Nonlinear aggregate indices — CES-type substitutability … the theorems claim nothing for them") — the exact hook the σ-wave fills; this wave's Lemma A makes the filling precise rather than notational.

## Part D — The incorporation plan (the ordered implementation queue, owner-gated)

A single future manuscript wave (new version, e.g. v53; never overwrite; re-verify per Part A first), in dependency order:

1. **Mechanical pass (§3.C 25–30)** — reference ordering, proof-list completion, qed placement, preamble hygiene, abbreviation uses, Fig-1 caption. No content risk; fail-loud diff gates (the house wave discipline: anchored edits, math-span multiset equality, idempotent drivers).
2. **Precision pass (§3.B 16–24)** — the nine rewordings; each preserves content and adds scope; the abstract edits (16–18) interact with any journal word bound → the bound question rides to the owner as before.
3. **Additive pass (§3.A 1–15)** — the orienting tables (1–3), the validity section + checklist (4–5), the disturbance-sensitivity table with the middle cell honestly marked (6; computing that cell is its own small exact-arithmetic task — the same discipline as this wave), positioning (7; Gao already in), **the σ-spectrum labelled-extension subsection (8) transcribed from `SIGMA_SPECTRUM_WAVE.md` §8's sketch — the family table, Lemma A, the master equation, the √2/φ/√3 ladder, the σ*-landscape, Theorems S1/S2, the LPI identification with caveats, the relevance chain, and the pointer to this folder's verifier**), the institutional/caveat/disclaimer additions (9–11), the reference completions (12–13), and the two motivation/limitation paragraphs (14–15).
4. **Owner-gated decisions to settle before or during the round:** title options (3.D-37); abstract length bounds vs the standing rule (3.D-36); Thm 5/6 renumbering vs a presentation note (3.C-31); whether the σ-subsection enters the main text or the Supplementary (the Supplementary Material already exists as the designated overflow per 3.D-34's override rationale).
5. **Standing exclusions (no action ever):** 3.D-32–37 as removals; 3.E-38/39/42 as materials.

## Part E — Honest residuals

- The middle-regime disturbance cell (6/42) is the only queue item that still needs *computation before prose*; it is small but nontrivial (a common-shock variant of the witness datum).
- The σ-wave's off-diagonal geometric residual (10 log-transcendental grid cells) is documented in the wave record §7; if a future round wants the full 2-D σ*-landscape map, that is a second exact-arithmetic wave (the −m rungs are already fully decidable off-diagonal; only the geometric member is not).
- Nothing in this round modified any existing repository file; the two documents, the verifier, and the run log in `batch 8/sigma_spectrum_wave/` are the round's only creations (plus the worklog appends).

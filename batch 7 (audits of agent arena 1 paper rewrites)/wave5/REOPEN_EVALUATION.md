# Wave-5 re-open evaluation — the registered follow-ups left behind the owner gate

**Task ID:** 75 (main orchestrator). **Date:** 2026-09-07 (this repo's clock).
**Directive:** (1) check the recorded reasons for declining — are they still
valid now that other changes have happened? (2) decide if any should be
re-opened; if a paper's statement numbering is causing confusion, a controlled
re-letter might now be worth doing.

**Method.** Every item registered or declined in the wave-2 docket
(WAVE2_IMPLEMENTATION.md §3), the wave-3 addendum, the wave-4 addendum, and the
six wave-4 per-paper records was re-verified by direct grep/read against the
current versions (E1 v11→v12, E2 v18, E3 v12, E4 v11, P1 v20, P2 v9→v10,
P3 v28→v29, P4 v27, P5 v21→v22 of this wave). Nothing was re-opened on
general plausibility; each re-open required a verified-open condition in the
current file plus a recorded reason that no longer holds.

---

## 1. The registry, re-verified — verdicts

### E1 (paperE1_cod_forecast_ladder, v11 → **v12 built this wave**)

| Registered item | Recorded reason | Re-verification | Verdict |
|---|---|---|---|
| Parameter table (claude priority 5) | "new computations… need a scored campaign" | **Reason mis-stated**: the fitted values are printed, scattered (§1, §2.2, §3.1–3.4, Prop 4.1); the P5-Table-3 pattern (as-printed + archive markers) needs no computation | **RE-OPENED → implemented** (new §3.6 + Table 10, 11 rows + §2.2 pointer; wave5/e1_record.md) |
| claude A7's constructive finding ("the value of a timely assessment exceeds the value of any structure tested") | not registered separately — buried inside A7, whose label half v10 implemented | **Verified absent**: no timeliness statement anywhere in v11; all needed numbers printed (86.4/11.1/184.4/195.6 + Table 4's values) | **RE-OPENED → implemented** (one §4 sentence; claude's "every structural model" corrected to "every delay-free module" — M4 at 196 does not beat the 184.4 stale control; the honest form is stronger) |
| Drift/damped-trend baseline | new computation | Still a computation; R3 was the only authorized one | **Stays registered** |
| Leave-one-origin-out influence (h=5) | new computation | Still a computation (the 1990-origin ~110 kt fact is grok's, not a printed record) | **Stays registered** |
| Table-6 forecast explanation (900–1900 kt); M3/M4 609/586 deterioration explanation | new analyses | Still analyses | **Stays registered** |
| M4 decomposition as a results table | folded into "needs a scored campaign" | Numbers exist in §4 prose (stated twice with correct labels since v10 + the new constructive sentence); promoting to §3 relocates frozen-record prose for presentational gain | **Stays registered** (reason corrected — not a computation, but a relocation of record prose) |
| log-RMSE demotion | (wave-4 implicit) table edit | v11 already carries the full floor disclosure (ε_log, per-origin hit counts, "the raw-RMSE column is the retention score"); dropping a recorded score column from frozen Table 4 contradicts cite-don't-drop | **Stays declined** — reason updated to the disclosure ground |

### P1 (paper1_assessment_separation, v20)

| Registered item | Recorded reason | Re-verification | Verdict |
|---|---|---|---|
| **Statement numbering** (the owner's example: "if P1's statement numbering is causing confusion, a controlled re-letter might now be worth doing") | n/a — a question, not a registered item | **Verified NOT confusing**: single shared 1–9 counter (Remark 1, Remark 2, Proposition 3, Proposition 4, Theorem 5, Remark 6, Theorem 7, Theorem 8, Proposition 9); every cross-reference updated; the four old-name tokens ("Proposition 1", "Lemma 2", "Theorem 3", "Theorem 6") occur exactly once each and all sit inside the version log's demotion record; S7's one internal "Theorem 6" token is fenced by the S8 preamble *inside* the supplementary ("the statement numbers are unchanged, so every reference resolves by number") | **No action — verified answer**: the numbering is coherent and the one cosmetic mismatch is already fenced where the reader meets it. A controlled re-letter was evaluated and **declined on verification**: renumbering (per-type counters) would break the number resolution with S7/S8 that the relabels were chosen to preserve; reverting type-words would undo adjudicated demotions. The genuine numbering confusion was found in **P3** instead (see below) |
| Frozen-statement re-letters (K/ε inside theorem statements) | statement changes on frozen statements | The §2.8 two-scope fences answer the readability; no jointly endorsed re-letter exists (grok's D_agg was declined on merit — D names the disturbance class) | **Stays declined** — reason still valid |
| Title change | no endorsed retitle | Unchanged; §7's scoping sentences carry the anti-doctrinal reading | **Stays declined** |
| S7's internal "Theorem 6" tokens | supplementary is append-only | The S8 preamble note is the in-file fence | **Stays as-is** (already fenced) |

### P2 (paper2_obstruction_calculus, v9 → **v10 built this wave**)

| Registered item | Recorded reason | Re-verification | Verdict |
|---|---|---|---|
| §1.2 "Each theorem exhibits the violating constraint, the admissible disturbance, and the quantitative bound" | v9 record: "not in the docket… awaiting the next registered wave" | Verified open at L48; false for Theorems 2 and 5 (claude §1.2) and Theorem 3's exhibit is the incompatible controls | **RE-OPENED → implemented** (scoped by mechanism; wave5/p2_record.md) |
| §6.4 "least-constrained compatible state" | "awaiting the next registered wave" | Verified open at L287; reads backwards (inf-q has least slack) | **RE-OPENED → implemented** ("most-constrained… minimum-q state, least constraint slack") |
| §6.4 "admissible exactly when… and no finer" | "awaiting the next registered wave" | Verified open at L289; overstates Theorem 3 twice | **RE-OPENED → implemented** (exposure wording: fibre-crossing; finer never hurts) |
| Singleton-belief sanity lemma (claude A8) | new mathematics (lemma + proof) | Still new mathematics; the audits' anti-inflation stance cuts against adding theorems | **Stays registered** — reason still valid |
| grok restructure items (tube-form Thm-3, Thm-2 plant replacement, Thm-5 demotion, §4.2 stub, §5(d)/Appendix-A relocation) | statement-scale churn | Wave-4 just adjudicated these theorems' repairs; re-opening would churn freshly adjudicated content | **Stays registered** |
| claude structural asks (Marchaud pass, chattering remark, §5(c) observer citation, Thm-2 domain extension) | various | §5(c)'s observer citation is a literature item that cannot be invented; the others unchanged | **Stays registered** |

### P3 (paper3_material_ledgers, v28 → **v29 built this wave**)

| Registered item | Recorded reason | Re-verification | Verdict |
|---|---|---|---|
| **Statement numbering** (the real instance of the owner's example) | not registered — surfaced by this wave's verification | **Verified confusing**: v28's demotions put five propositions (4, 6, 17, 18, 20) on the type-word of the paper's separate layering stream (Propositions 1–2 of §3.1), so the propositions read 1, 2, 4, 6, 17, 18, 20 — every label unique, the convention undeclared; and the supplementary's S4 inventory carries the pre-v28 status words with the offset recorded only in the main-text version log | **RE-OPENED → implemented by declaration** (not a re-letter): §3.1 numbering note + supplementary S6 append (the P1-S8-preamble pattern: the eight-row naming-offset table + the two-counter declaration) + the main-text pointer naming S6; wave5/p3_record.md. A re-letter was considered and declined: renumbering the layering propositions (e.g. to Claims) is an un-adjudicated status change; renumbering the demoted items breaks the supplementary's number resolution |
| 21k→12k length remainder | restructure-level cuts would remove publishable core | Unchanged | **Stays registered** |
| Per-row USGS re-pin | requires the per-country MCS 2026 reserve table | External data still absent | **Stays registered** |

### P4 (paper4_delay_dynamics, v27)

| Registered item | Recorded reason | Re-verification | Verdict |
|---|---|---|---|
| Per-campaign tables for §9 | "restructure-scale pass on frozen record prose (registered, not declined on merit)" | Still true: §9.2/§9.3 are prose records; the consolidated channel × scheme × T_r table (v27 §8) plus the growth-rate/stock-mode sentences delivered the readability substance | **Stays registered** — reason still valid |
| RH-margin quantification (6×10⁻⁵) | not a printed record (claude's recomputation) | Unchanged | **Stays declined** |
| M_p(1) eigenvalue triple as recorded values | paper records only ρ | Unchanged; the uncoupled-mode restatement stands | **Stays declined** |
| Flip-type classification of the 2.306 crossing | no recorded eigenvalue type | Unchanged | **Stays declined** |
| Start-of-period ≈3.0-yr recomputation | contradicts the registered 6.5013 record | Unchanged | **Stays declined** |

### P5 (paper5_sampled_governance, v21 → **v22 built this wave**)

| Registered item | Recorded reason | Re-verification | Verdict |
|---|---|---|---|
| "sampled governance" vs "sample-and-hold governance" (grok §6 + claude) | "title-level change outside this wave's mandate" | Verified open: two names, one architecture, no equivalence declared; the title carries both — but a **fence** avoids the title entirely | **RE-OPENED → implemented as the fence** (one §1 sentence declaring equivalence and interchangeability; title untouched; wave5/p5_record.md) |
| Abstract "thirty-plus" vs "more than thirty" (claude) | "the joint item covers only 42" | Verified open: 1 vs 3 sites | **RE-OPENED → implemented** (harmonised to the dominant form) |
| Figure 1 caption "four update pairs" (claude §3.4) | "not elevated" | Verified open | **RE-OPENED → implemented** (claude's exact wording, the four named) |
| Lemma 2.2's seal-predation application + Prop 2.1 demotion | claim-changing | Unchanged | **Stays declined** |
| θ strong-resonance check | computation | θ recorded as not-printed | **Stays declined** |
| Nonlinear "exact update" definition | would assert unrecorded content | Unchanged | **Stays declined** |
| "Three objects"/"two operators" counts | bound by the reconciliation paragraph | Verified binding | **Stays declined** |

### E2 / E3 / E4 (v18 / v12 / v11 — closed papers)

| Registered item | Recorded reason | Verdict |
|---|---|---|
| E2: full single-convention recompute (the 1992 −460.0 vs −329.0 disclosure) | new computation (refit under one convention) | **Stays registered** — reason still valid |
| E3: §5.7 placement + Table-8 numbering as literal layout | "renumbering v11's structure to imitate a lost file would churn the already-implemented paper for no content gain; the substance is fully incorporated" | **Stays declined** — reason still valid (verified: §5.3.1 carries the layer) |
| E4: Stage-I/flat-80% 613.1-ft securing computation | new computation (labelled follow-up at the sensitivity site) | **Stays registered** — reason still valid |

### Standing leftover check (from the session directive)

The **a025_model.py model-consistency audit** was confirmed already resolved in
Tasks 65–66: the model audit verdict recorded SHA-256 `c1dae18b…` identical
across all four manuscripts; no action remained. (The other "registered
leftover" — E2 §3.6's SSE→MSE labels — was fixed in wave 2, Task 71.)

---

## 2. Answers to the two questions

**Q1 — Are the recorded reasons still valid?** Mostly yes: every
computation-grounded decline (E1's baselines, E2's recompute, E4's securing
check, P5's θ) and every claim-change ground (P5's seal-predation application,
P2's new mathematics, P1's title) survives re-verification unchanged. Two
classes of reason did **not** survive:

1. **"Awaiting the next registered wave"** (P2's three §6.4/§1.2 one-liners) —
   that wave is this one; the gate the owner just opened is exactly what the
   reason was waiting for. All three re-opened and implemented.
2. **Mis-stated blanket reasons**: E1's parameter table was registered under
   "needs a scored campaign" although everything it needs is printed (the
   P5-Table-3 pattern answers it without computation); claude A7's constructive
   finding was never registered as its own item although its label-half was
   implemented in v10; P5's term unification was declined as "title-level"
   although a title-free fence exists. All three re-opened in their bounded
   form.

**Q2 — Should any be re-opened?** Yes — nine items across four papers (the
table above), all implemented this wave in four fail-loud byte-reproducible
builds:

| Paper | New version | Build | Items |
|---|---|---|---|
| E1 | paperE1_cod_forecast_ladder_v12.md | apply_batch7_wave5_e1.py | §3.6 + Table 10 (parameters as printed) + §2.2 pointer; §4 constructive timeliness sentence |
| P2 | paper2_obstruction_calculus_v10.md | apply_batch7_wave5_p2.py | §1.2 mechanism-scoped exhibit sentence; §6.4 "most-constrained" correction; §6.4 coarseness exposure wording |
| P3 | paper3_material_ledgers_v29.md + supplementary S6 | apply_batch7_wave5_p3.py | §3.1 numbering note; S6 naming-offset append (8-row table + two-counter declaration); pointer naming S6 |
| P5 | paper5_sampled_governance_v22.md | apply_batch7_wave5_p5.py | §1 architecture-name fence; abstract "more than thirty"; Figure 1 caption "update × channel combinations" |

**The owner's specific example — P1's statement numbering** — was verified
first and found **not** in need of a re-letter: P1's shared 1–9 counter is
coherent, all cross-references resolve, and the single supplementary-side
mismatch (S7's "Theorem 6") is already fenced inside the supplementary by the
S8 preamble. The verified instance of exactly that confusion is **P3** (the
two-counter Proposition hybrid 1, 2, 4, 6, 17, 18, 20 plus the unfenced
supplementary inventory), and it was fixed by declaration — a numbering note at
the §3.1 layering site and the appended S6 offset table — rather than by a
re-letter, because a re-letter would break the number resolution that the
relabel strategy was chosen to preserve.

## 3. Non-destructiveness

No frozen verdict, score, kernel, spectral record, or table value changed
anywhere: E1's Tables 1–9, P2's displays and proofs, P3's tables, and P5's
tables are byte-identical (machine-checked in every build); E1's abstract is
untouched at 300 words; P5's title is untouched; P3's supplementary edit is
append-only (43 insertions, 0 deletions, git-verified). All four builds are
byte-reproducible (MD5s in the records) and the P3 supplementary append is
idempotent-with-verification.

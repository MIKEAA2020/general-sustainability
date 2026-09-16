# Merged Improvement Plan — All Venues (baseline: F1 v18, 2026-09-13)

**Purpose.** One document merging every suggestion from every review venue that has
touched the framework paper, with every item classified, every cross-venue
contradiction adjudicated, and the remaining work laid out as phases — so that no
two venues can ever drive opposing edits again. v18 is the baseline; nothing in this
plan reopens a verdict reported in the paper.

**Venue policy (standing).** Companion papers are cited formally (Abaee 2026a/b);
earlier manuscript versions are never referenced. New versions only — v13–v18 are
frozen. Contradictions are adjudicated **before** implementation; each phase is then
one coordinated pass. The manuscript stays in journal register (three automated
scanners enforce this: `journal_style_automated_scan.py`,
`journal_formalization_scan.py`, `redundancy_scan.py`; a fourth,
`content_coverage_scan.py`, guarantees no scientific content is lost).

---

## 1. Venue inventory

| # | Venue | Source file | Disposition |
|---|---|---|---|
| V1 | Qwen audit, framework v12 | `uploads/audit of framework v12.txt` | all items adjudicated/implemented (ledger §2) |
| V2 | Claude audit, framework v12 | `uploads/audit of framework v12.txt` | all items adjudicated/implemented (ledger §2) |
| V3 | Four-audit joint evaluation (Grok ×2, Gemini ×2) | `uploads/framework audits.txt`, `JOINT_EVALUATION_FOUR_AUDITS_v2.md` | 12 contradictions adjudicated pre-v12 (`CONTRADICTORY_POINTS_ADJUDICATION.md`); all defect items closed |
| V4 | Two-audit register + adjudications AD1–AD8, N1–N6 | `REMAINING_POINTS_TWO_AUDITS_v13.md`, `JOINT_EVALUATION_TWO_AUDITS_v13.md` | the authoritative ledger; phases A–E closed every item (§2) |
| V5 | Author verification transcript (source behind §4.3 provenance, N1/N4/N5) | `uploads/last message.txt` | folded into AD1/N1/N4/N5 |
| V6 | Owner interactive decisions (Phase B) | `PHASE_B_ROOT_CAUSE_DECISION_MEMO.md` | binding: AD6 adopt fully; AD2 option (a); AD4 option (b) |
| V7 | Phase C computational campaigns | `phase_c/PHASE_C_RESULTS.md`, `PHASE_C_CHANGELOG_v15_to_v16.md` | data source for the single number set |
| V8 | Companion-paper audits (E1/E3) | `audits_E1_E3/`, `batch 7/`, `arena agent 1/…` | no F1 edits; feed the forward cross-check (O7) |
| V9 | **Qwen — framework journal fit** | `uploads/qwen framework journal fit.txt` | **received 2026-09-13 (10.5 KB), fully processed through the merge pipeline: journal targeting (IJF first, EMS second) recorded as submission strategy; 9 content items classified (below); 1 contradiction adjudicated (NEW-1); 2 owner-gated structural proposals recorded (NEW-2).** |

---

## 2. Master ledger — every suggestion, by status

### 2.1 CLOSED — implemented and verified (pointer to where)

**Contradiction adjudications (V3, pre-v12).** C1 phantom baselines 97/193 and 79/288;
C2 origin-matched vs mixed-origin 84.4/88/87.6; C3 3.2 vs 3.6 vs 4 kt; C4 Edwards
margins −17.34/−17.39, 4.33/4.36, −42.96/−42.93; C5 runtime 4 h/10 h/25 h (now measured
costs in Data availability); C6 tie-band "≥5%" vs algorithm strictly-greater; C7 band
post-hoc disclosure; C8 class-grounds gate placement; C9 seven-model ladder counting;
C10 climate 0.13 ft; C11 K bound 500/50.8/multi-start; C12 DM z vs bootstrap p vs CI
(inconsistent procedures allowed; DM labelled descriptive). All settled in
`CONTRADICTORY_POINTS_ADJUDICATION.md`, implemented in v11/v12, carried into v18.

**Register adjudications (V4).**
- **AD1** (K bound, claude upheld, data-backed): 950.8 kt (1987) / 50.8 kt (2006,
  terminal state excluded) — in §2.1, E1-v20 wording. Never reuse 91.1.
- **AD2** (D6/D7 labels): owner option (a) — frozen labels kept, prose rename to
  "mechanism misattribution", Table 2b "Row measures" column; realised predictive
  gains now numeric (D6 +3.1/+9.2, D7 +2.6/+9.4 kt at h=1, 100% beat persistence).
- **AD3** (reproducibility vs the band): rerun registered, executed, **passed** —
  Edwards audit layer reproduces exactly (six archived comparisons + the D1 M2m-h5
  cell); the "gates load-bearing" claim stands, tolerance sentence retained.
- **AD4** (band calibration vs C1): owner option (b) — future-only; now an
  operational procedure in §4.7; never re-opens reported verdicts.
- **AD5** (MCS vs DM posture): MCS/encompassing enter as context diagnostics, never
  gate inputs — delivered as §4.5 sensitivity rows; verdicts unchanged.
- **AD6** (reframe): owner decision adopt fully — title/abstract/§1/§7/§8 reframed as
  a minimum reporting standard (Phase B).
- **AD7** (persistence baseline): one sentence in §5.2 — persistence is the
  pre-registered H2/H3 anchor; training-mean superiority reported as evidence about
  the baseline choice.
- **AD8/N3** (frozen sheet "eight cells" vs archived rows): dated note; no numeric
  change. **N2** (E1-v20 K-bound wording) adopted. **N4** (DM universe): 32 rows
  stated; E1's "four of the twenty-eight" reconciles as 24 primary + 4 comparisons.
  **N5** (archive paths) fixed. **N6** (as-of-verified scope) recorded.

**Qwen items (V1).** 1.1–1.22 (22 inconsistencies, C1–C15 list); 2.1–2.3, 2.5–2.7
(numeric checks); 2.4 (0.0359); 2.8 (p_perc language, p<1/B); 3.1–3.2 (band
versioning, class grounds); 3.4 (M3/M4 scoping); 3.5 (in-class specificity scoping);
3.8 (fixed-window/15-year labelling); 3.10 (AD7); 4.1–4.28 (glosses incl. 4.10
"printed on primary passes", 4.11 "moratorium", 4.18 "bold 193" removed, 4.23 MAE
10.72/10.73, 4.24 "17.64"); Tables 2-2/3-2/4-2/4-4/5-2 (12.1971 comparator band);
§5.2 oracle h=5 row; item 9 (Makridakis in-text citation). All verified present in v18.

**Claude items (V2).** 1.1–1.5, 1.7, 1.10–1.11 (arithmetic); 1.6 (AD1); 1.8
(alt-comparator +29.3 row — verified against the archived run and documented in the
N4 universe); 1.9 (M4 worst RMSE scoped to collapse window); Appendix AIC vs
"information criterion n log MSE+2k" reconciled.

**Phase C data closures (V7).** D3/N1 — the pinned-seed campaign reproduces published
§4.3 (D1 0.955/0.960, D2 0.780/0.060, D3 0.110/0.100, D4 0.010/0.010, D5 0.995/0.950;
D6/D7 0.633–0.933; T=71 0.900/1.000, 0.000/0.000; wrong-module 0.034; null 0.0055;
mean power 0.373); v18 carries this single number set; the archived replicate table
is retained solely as the stated source of the §4.5 alternative-rule rows. Smoother
test (claude 3.1) executed — §6 mechanism quantified (margin compression 7–13×,
power 0.90/1.00 → 0.63/0.67; real, not sufficient alone). SNR curves (D1 flat
0.88–1.00 over σ∈{5,45}; D3/D4 ≈ 0 at σ=5). Third pre-check candidate (training-window
profile curvature; D3 pinned to the 1991–92 catch transition). Uncertainty gate +
hybrid + MCS (§4.5 sensitivity rows). Amendment-1 length-sensitivity check satisfied
(|Δ| 0.055/0.040 ≤ 0.15). Per-regime decomposition (no verdict flips).

**Phase D closures.** §4.7 Prospective registration (model set, next origins,
prospective band, Amendment procedure); remnant/redundancy scan 91 → 0 findings
(incl. the §6 table sync to pinned-seed numbers).

### 2.2 OPEN — remaining work (phases in §6)

| ID | Item | Origin | Phase | Nature |
|---|---|---|---|---|
| O1 | Abstract: add the §4.5 caveat that the information criterion does not enforce the multi-year persistence requirement (register 6.7, partial) | qwen 6.7 | F | **CLOSED — Phase F (v19)** |
| O2 | §5.2 "not second fibre of this specification" — informal term | register item 9 (partial) | F | **CLOSED — Phase F (v19)** |
| O3 | Climate-module table in §5.2 (margins per module per horizon; data archived) | claude 2.3 / register item 8 (remainder) | F | **CLOSED — Phase F (v19; NEW-3)** |
| O4 | M3/M4-as-truth operating-characteristic cells (optional in the original plan, never executed) | register §5 (optional) | G | computational, optional |
| O5 | Full registered designs: T=71 at 200 replicates; Amendment-1 eight cells × 200 (measured ≈25 CPU-hours) | Amendment 1 / §4.2 | G | computational, hardware-gated |
| O6 | Execute the prospective-band calibration at the first future application (Edwards 2024–2033 origins; cod Spec B 2025+ vintages) | claude 4.2 / AD4 | H | **EXECUTED 2026-09-13 (Phase K) — cod calibration on the pinned-seed archive: no band attains power≥0.80 and specificity≥0.90 (power identification-limited: 0.444→0.312 over 0–15%) → frontier reported, 5% band retained (v24 §8; o6_cod_band_calibration_20260913.json). Edwards: draft calibration sheet registered (owner-gated; no runs until approval); origin-2024 inputs archived (2024/2025 panel). Cod Spec B: origin 2025 scores at the 2027 vintage. Full 200-rep T=71 frontier remains O5.** |
| Companion cross-check when E1/E3 are finalized: every number F1 cites from them (Tables 2–5, the 32-row DM universe vs E1's 28, titles/DOIs, "Table 8 of companion" references) | V8 venues | H | **CLOSED — 2026-09-13 as-of current companions (E1 v49 / E3 v16 + cited archives): COMPANION_CROSSCHECK_20260913.md; NEW-4a (M1 point-rule reconciliation → v22) and NEW-4b (O9 M3/M4 archive fix) adjudicated; re-runs at E1/E3 finalization** |
| O8 | Elevate the information-criterion result from a §4.5 table row to its own subsection with stated implications (kept within the AD4 posture: the rule is the pre-registered instrument, the band the prospective replacement) | V9-D | F2 | **CLOSED — Phase F2 (v20; written from the archived O9 result)** |
| O9 | Co-primary IC check: re-score the archived replicates with the information criterion as a co-primary rule and report whether any verdict changes (context diagnostic, never a gate input — AD5 posture; needs the archived IC-rule definition) | V9-D (option 2) | G | **CLOSED — Phase G (2026-09-13): archived o9_ic_coprimary_20260913.json; instrument validated cell-by-cell vs identification_limit_20260913.json; cod agrees, Edwards selects M2m — the gates are load-bearing against the IC** |
| O10 | Class-grounds accessibility: state the general principle early (§1) and add a travelling gloss ("structural redundancy" — a module that reduces to a simpler member adds no information regardless of its score); keep the pre-registered output name "declined on class grounds" | V9-E | F | **CLOSED — Phase F (v19)** |
| O11 | Problem-first lead: open the abstract/§1 with the three-sentence framing (module doesn't beat the benchmark — useless module or weak test?); state the standard in one consolidated page separating standard / demonstration / simulation | V9-B, V9-C | F | **CLOSED — Phase F (v19; V9-B was a duplicate, one-page statement added)** |
| O12 | Unpack parenthetical density: move number-dense prose into the existing tables/appendix and narrate findings in plain sentences (e.g., the Spec B deficit chains, §8's summary) | V9-F | F2 | **CLOSED — Phase F2 (v20)** |
| O13 | Reproducibility-discourse paragraph: connect pre-registration, pinned seeds, archived forecasts and §4.7 to the registered-report / pre-registration literature and M-competition protocols (citations verified at edit time) | V9-G | F | **CLOSED — Phase F (v19)** |
| O14 | Consolidated limitations paragraph in §7 (series length, upper bounds, two domains, M3/M4, in-class specificity) — gather the scattered caveats into one formal statement | V9-I | F | **CLOSED — Phase F (v19)** |
| O15 | Journal targeting (submission strategy): IJF first choice, EMS second, per V9 §1; owner's decision at submission time — no manuscript edit implied | V9-J | — | strategy note |
| O16 | Deeper V9-A compression (main text 10.7k → 8–10k words by further movement to the supplement) | V9-A remainder | — | optional, owner-gated |
| O17 | V9-G remainder: name the M4/M5 competition protocols in the reproducibility paragraph + M5 reference | V9-G | F | **CLOSED — Phase O17 (v23, 2 rules)** |

### 2.3 V9 processing record (qwen framework journal fit, received)

Nine content items, classified per the §5 pipeline:

- **Duplicates (already implemented):** the AD6 reframe covers most of V9-C's
  "standard vs demonstration" separation and V9-B's problem-first lead; §4.7 covers
  the prospective-registration point V9-G builds on; §7's "Not licensed" block covers
  most of V9-I. These map to remainder items (O11, O13, O14), not new work.
- **Compatible text items:** V9-E (O10), V9-F (O12), V9-G (O13), V9-I (O14).
- **Contradiction (adjudicated NEW-1):** V9-D option 1 conflicts with the AD4 owner
  decision; option 2 adopted (O8/O9).
- **Owner-gated structural proposals (NEW-2):** V9-A (compression), V9-H (reorder),
  V9-C remainder (one-page standard statement) — pending the owner's decision.
- **Submission strategy (O15):** IJF first choice, EMS second; no manuscript edit.

**V9 final disposition (2026-09-13).** All nine content items closed. O17
(M4/M5 protocols) implemented in v23. Three V9-A sub-proposals are **declined
with recorded reasons**, not open items: (1) moving the simulation to a
supplement — contradicts the paper's own structure, where the
operating-characteristic study is the standard's third mandatory component and
Section 6 is its report; (2) compressing the cod domain to the comparison
table alone — the cod worked example is already short and is the standard's
demonstration on a second domain; (3) the residual 8–10k-word compression —
owner-gated O16, excluded by owner direction 2026-09-13. V9-D's prediction
("verdicts likely unchanged under the co-primary IC") was tested empirically:
unchanged on both cod objects, but on Edwards the IC would retain the
class-grounds-declined M2m — the divergence lands exactly where Section 4
shows the gates to be load-bearing, which strengthens the standard more deeply
than V9 anticipated.

---

## 3. Contradiction adjudication record (all venues)

| # | Conflict | Venues | Adjudication | Status |
|---|---|---|---|---|
| C1–C12 | numeric/labelling/procedure contradictions (baselines, margins, runtime, band, gates, ladder count, K bound, DM) | V3 | data-backed or pre-registration-backed resolutions in `CONTRADICTORY_POINTS_ADJUDICATION.md` | settled |
| AD1 | K bound 91.1 vs 50.8 vs 500 | V2 vs paper | claude upheld; computed 950.8/50.8 | in text |
| AD2 | rename "false retention" vs frozen pre-registered labels | V2 vs pre-registration | owner option (a): keep labels, prose rename + Row measures | in text |
| AD3 | "gates load-bearing" vs unmeasured environment sensitivity | V2 vs §6 | register the rerun; rerun passed → claim stands | closed by data |
| AD4 | "pre-register the OC, not the threshold" vs adjudicated 5% band | V2 vs C1/C7 | owner option (b): prospective replacement, future-only; §4.7 procedure | in text |
| AD5 | MCS as verdict instrument vs descriptive-DM posture | V2 vs A1 | context diagnostics only, never gate inputs | in text |
| AD6 | reframe as reporting standard vs original framing | V2/qwen 3.3 vs paper | owner decision: adopt fully, one coordinated rewrite | in text |
| AD7 | persistence vs training-mean baseline | V1/V2 | persistence = pre-registered anchor; baseline-choice evidence reported | in text |
| AD8 | "eight cells, 1,600 passes" vs archived row count | frozen sheet vs archive | dated note, no numeric change | in text |
| N1 | zip CSVs vs published §4.3 (replace vs disclose) | V5 vs archive | pinned-seed reproduction vindicates §4.3; v18 = single number set; archived table retained as §4.5 source only | closed by data |
| mean power | 0.376 (paper) vs 0.373 (fresh) | archive vs Phase C | statistically indistinguishable; v18 cites campaign with §4.5 cross-reference | closed |
| IC row | 0.376/0.978 vs 0.373/0.973 | archive vs Phase C | same resolution as mean power; abstract cites 0.373/0.973 with §4.5 pointer | closed |
| false retention | 0.044 vs 0.034 | archive vs Phase C | v18 uses 0.034 everywhere | closed |
| identification | 62.7/64.5, 25.8, 3.8 vs 61, 37/18, 1/11 | archive vs Phase C | v18 uses pinned-seed values in prose and tables | closed |
| D6/D7, T=71 | published vs fresh values / "not executed" | archive vs Phase C | v18 carries fresh values; T=71 reported as executed | closed |
| DM count | "5 of 32" vs E1 "four of the twenty-eight" | V5 vs E1 | N4: 24 primary + 4 comparisons = 28 | closed |
| NEW-1 | V9-D option 1 ("present the IC as the recommended instrument for future applications") vs AD4 (owner decision: the simulation-calibrated band is the registered prospective replacement) | V9 vs owner | AD4 binds — the prospective replacement remains the band; the IC recommendation is rejected as stated. V9-D option 2 (co-primary IC check, context diagnostic) is compatible with AD5 and adopted as O8/O9 | adjudicated |
| NEW-4a | E3 retains M1 at h=1 (pre-registered point rule, no band, h=1-only) vs F1's unified-rule M1 failure with no reconciliation | E3 v16 vs F1 §4 | companion verdict authoritative for its own rule; F1's unified-rule verdict frozen; reconciliation sentence added to §4 in v22 (rule-version difference, not data difference); "no outcome changes" sharpened | closed by data (O7, v22) |
| NEW-4b | O9 JSON derived Edwards M3/M4 = 12.483/12.624 vs companion Table 4 (14.46/14.30) | O9 archive vs E3 | companion values adopted; IC-best unchanged (M2m); paper text unaffected; archive + runner note regenerated | closed by data (O7) |
| NEW-3 | F1 §5.2 "R-ENSO variant 0.41 ft worse" / "M2_Rprecip and M2_Rar edge past M1 at h=1 (12.71 vs 12.84)" vs archived companion (E3 v16 Table 7, wave_e_edwards manuscript v2 Table 6, wave6 tablerow audit) | F1 v13+ prose vs E3 archive | archive authoritative: 0.41-worse module is M2_Rar (13.25 vs 12.84); within-0.13 trio is Renso −0.02 / Rprecip −0.04 / combo −0.13; "edge past M1" (14.52/14.67 vs 15.62) is the 2015–23 fixed window. Fixed in Phase F with new Table 5b | closed by data (Phase F, v19) |
| NEW-2 | V9-A/H/C (compress to 8–10k + supplement; reorder demonstration-before-simulation; separate standard/demonstration/simulation layers) vs the AD6 one-coordinated-rewrite rule and the no-content-loss policy | V9 vs AD6/coverage policy | not content contradictions — owner-gated structural proposals; if approved they form one coordinated structural phase (Phase J) with a supplement vehicle, guarded by the content-coverage scanner; if declined, only the text-level items (O10–O14) proceed | owner-gated |

**Phase J executed (2026-09-13, per the owner decision):** v21_restructured + Supplement S1 — worked examples before simulation, three layers separated, supplement vehicle in place; line-completeness audit 0 unaccounted; main 10,695 words + supplement 913. Remaining V9-A compression to 8–10k recorded as O16 (optional, owner-gated). NEW-2 closed.

**Owner decisions (2026-09-13):** NEW-1 — the honest, root-cause resolution is confirmed: AD4 stands; the IC recommendation is rejected; the empirical completion (O9 co-primary IC check on the archived pinned-seed replicates) is the data-driven defense of the IC finding. NEW-2 — Phase J runs **after** the text passes (F, F2); the restructured version keeps the continuous version count but carries a distinguishing filename suffix marking the restructure (e.g. `_restructured`), per owner instruction; the pre-restructure lineage stays frozen.

**Rule that made this possible:** every conflict was adjudicated once, recorded, and
implemented in a single phase pass; no venue ever edited another venue's fix.

---

## 4. Precedence rules (non-contradiction guarantee)

1. **Owner decisions bind** (AD6/AD2/AD4) — revisable only by the owner.
2. **Pre-registered elements are frozen** (rule algorithm, 5% band for reported
   verdicts, DGP labels, ladder, comparators); changes only by pre-registered
   amendment (as Amendment 1 did).
3. **Reported verdicts are immutable** — nothing re-opens them (§4.5, §4.7).
4. **Pinned-seed numbers supersede older point values** everywhere except the
   archived table's stated role as the §4.5 source.
5. **Only companion papers are referenced**, never earlier versions of this
   manuscript; journal register enforced by scanners.
6. **Adjudicate, then implement** — one pass per phase, new version per pass,
   verification + push after every phase.
7. **N6 caveat** — "all points implemented" is as-of-verified; any new venue can
   reopen an item through the same pipeline.

---

## 5. Merge pipeline for new venues (applies to V9 immediately)

For each suggestion in a new venue:
1. **Duplicates check** — already implemented? (register + scanners) → CLOSED-dup,
   cite the pointer.
2. **Frozen-element check** — conflicts with pre-registered labels/rule/verdicts or an
   owner decision? → **adjudication table** (§3), owner consulted if it touches an
   owner-gated item.
3. **Open-item check** — duplicates an O1–O7 item? → merge, keep one ID.
4. **New item** → append to ledger with a phase assignment (F text / G computational /
   H event).
5. After adjudication, implement phase-by-phase; re-run the four scanners; push.

---

## 6. Remaining work plan

- **Phase F — text consolidation pass → v19** (O1, O2, O3, O10, O11, O13, O14):
  abstract IC caveat; "fibre" fix; climate-module table; class-grounds principle +
  travelling gloss; problem-first opening + one-page standard statement;
  reproducibility paragraph; consolidated limitations. All text/table, no verdict
  contact, no new computation.
- **Phase F2 — text pass → v20** (O8, O12): the IC subsection (from existing numbers;
  written with O9's co-primary result if available) and the parenthetical-density
  unpacking.
- **Phase G — optional computation** (O4, O5, O9): M3/M4-as-truth cells; the full
  200-replicate T=71 and 8×200 Amendment-1 designs (≈25 CPU-hours measured); the
  co-primary IC check. Results refine, never reverse, the reported verdicts.
- **Phase H — event-triggered** (O6, O7): §4.7 calibration at the first future
  application; companion cross-check when E1/E3 finalize.
- **Phase J — journal-fit structural pass (owner-gated, NEW-2):** if approved, ONE
  coordinated pass applying V9-A (compress to 8–10k words, remainder to a
  supplement), V9-H (worked examples before simulation), and the V9-C remainder;
  guarded by the content-coverage scanner (nothing lost, only moved). Never
  incremental patches.
- **Perpetual guardrails:** every version passes the four scanners; register §5 and
  MANIFEST updated per phase; all artifacts pushed to
  `edwards-framework-e1-audit-implementation`; main never modified.

## 7. Status summary

Phases A–E **DONE** (v14 → v18); venues V1–V9 **all received and processed**;
contradiction count across all venues: **27 adjudicated, zero outstanding**
(25 earlier + NEW-1 + NEW-2, the latter owner-gated with a recorded recommendation);
open items: **17 recorded** (O1–O17), of which 16 closed; O4/O5 and O16 remain owner-excluded, and O6 is executed for cod with the Edwards calibration sheet owner-gated and Spec B origin 2025 pending the 2027 vintage — O1–O3, O10, O11, O13, O14 form the small text pass
(Phase F, v19); O8, O12 a second text pass; O4, O5, O9 optional computation; O6, O7
event-triggered; O15 submission strategy; Phase J structural work awaits the owner's
decision on NEW-2. Nothing in V9 re-opens any reported verdict or any frozen element.
## 7. Status summary

Phases A–E **DONE** (v14 → v18); venues V1–V8 **fully incorporated**; contradiction
count across all venues: **25 adjudicated, zero outstanding**; open items: **7**
(O1–O7), of which O1–O3 are a small optional text pass, O4–O5 optional computation,
O6–O7 event-triggered. Venue V9 (qwen framework journal fit) is **pending content** —
the pipeline above folds it in without re-opening anything.

---

## 8. Companion venues (V10) — remaining points, adjudicated (2026-09-13)

Scan of the E1/E3 companion venues for remaining improvement points. All are
companion-side or governance items — none contradicts any F1 adjudication or
frozen element, and none re-opens a reported verdict.

| ID | Point | Source | Adjudication |
|---|---|---|---|
| CV1 | Promote origin-matched persistence into E1 Tables 6–8 as the primary column; demote all-origin baselines to an audit table (T8, marked "Remaining"; values from rolling_forecasts.csv / xte_rolling_forecasts.csv, never retyped) | E1_TIER3_RESTRUCTURING_PLAN.md | owner-gated E1 edit; **aligns with F1** (F1's Tables 2/3 already carry origin-matched as primary) — no contradiction |
| CV2 | E1 Tier-3 deliberate one-pass restructure (T1 highlights block, T8, etc.) | E1_TIER3_RESTRUCTURING_PLAN.md | owner-gated; E1's own plan defers it to a single pass; F1's O7 cross-check re-runs at E1 finalization |
| CV3 | E1 v49 DM table row A h1 M4vM3 prints z=1.21, [4.4, 134.4] (coarse-regime pass, M4 195.6) while the annual-landings replication archives z=0.99, [4.7, 144.7] (M4 206.3); F1's numbers match the cited replication | COMPANION_CROSSCHECK_20260913.md (O7) | companion-side reconciliation at E1 finalization; F1 verified against its cited archive — no F1 edit |
| CV4 | TCS-1.1 migration — registered as an open Wave-0 obligation with checklist; deliberately not executed (scoping decision recorded) | TRANSFER_AUDIT_RESPONSE.md | governance item; record only — not paper content |
| CV5 | Per-paper DEFERRED open lists (e.g., U4 belief-space kernel; each paper's declared open list) | joint_assessment_wave5.md | stay on their declared lists; none is F1-relevant |

No contradiction check failures: CV1 uses the same origin-matched convention F1
already reports; CV2/CV3 are E1-internal; CV4/CV5 are governance/open-list
records. When E1/E3 are finalized, O7 re-runs and this section updates.

---

## 9. Venue V11 — humanized rewrites (Grok + Gemini), 2026-09-13

Received two full humanized rewrites of v24. Drift-audited before adoption:
Grok — 0 fabricated numeric tokens, all 20 content headers, all adjudicated
strings → **adopted as the v25 base** (frozen `v25_source_grok_rewrite.md`).
Gemini — 28 unarchived/invented numbers, fabricated companion titles and
swapped Zenodo labels, reference swaps, table renumbering → harvested
selectively, everything else rejected.

| ID | Adjudication |
|---|---|
| V11-adopt | Base = Grok rewrite; §6.4 bolded topic sentences; sentence-level humanization throughout |
| V11-adopt | Gemini abstract forward-reference: the criterion applied alone would retain the structurally redundant module the standard withholds (O9-consistent) |
| V11-adopt | Gemini §2.3 derivation: constant training-mean fluxes fold into a single intercept, leaving an affine autoregression |
| NEW-5 | **Fixed:** M4 reference "54 methods" → "61 forecasting methods" (published IJF 36(1) title, verified against the publisher record) |
| NEW-6 | **Rejected:** Gemini's fabricated companion titles and E1/E3 Zenodo label swap — O7-verified titles/DOIs stand |
| NEW-7 | **Rejected:** Gemini's unarchived numbers (M1 CI [−0.954, +0.180]; oracle 10.865; 612.5 ft) — no unarchived number enters the paper |
| NEW-8 | **Rejected:** Gemini's Carvalho/Kell reference swaps (different real papers) |
| NEW-9 | **Rejected:** Gemini's M5 title ("Background, organization, and results") — cited paper is "M5 accuracy competition: results, findings, and conclusions", IJF 38(4), 1346–1364 |
| V11-fix | Grok-base regressions caught by the scanners and fixed in v25: verbatim repetition reintroduced (§9 sentences), ≈ spacing, Diebold–Mariano hyphen |

Result: v25_restructured (8 asserted rules over the frozen base); numeric drift
v24→v25 = none (386 = 386 tokens); all scanners green; coverage clean.
Evaluation: `JOINT_EVALUATION_HUMANIZED_REWRITES_V11.md`.

---

## 10. Venue V12 — novelty/impact audits (Qwen + GPT), 2026-09-13

Joint evaluation + verification: `JOINT_EVALUATION_IMPACT_AUDITS_V12.md`. Every
claim verified against v25 and the archives; 8 contradictions adjudicated
(NEW-10…NEW-17); the implementable remainder opened as O18–O39.

### New open items

| ID | Item | Origin | Phase | Feasibility |
|---|---|---|---|---|
| O18 | Standalone two-page specification + checklist (the deliverable, not a summary) | qwen 3.1 / gpt 1,3 | L | **CLOSED — Phase L (v26)** |
| O19 | Formal class-grounds criterion — prospective only (pre-registration keeps the declared judgement for reported verdicts; NEW-13) | qwen 3.2 | owner | prospective |
| O20 | IC instruments on the existing archive: IC at h=5; multi-horizon penalised criterion; IC-ranking + rule-gates hybrid (both audits' #1 technical item) | qwen 3.3 / gpt 4 | M | **CLOSED — Phase M (S1.5)** |
| O21 | Additional out-of-class DGPs (threshold / regime switch / non-stationary mean) | qwen 3.4 / gpt 2.3 | G | **CLOSED — sheet-gated by frozen v4 §96** (σ=0 / 𝔰∈{5,30} declared but deferred; props to the Spec-B sheet, owner-gated there) |
| O22 | Register the third-domain requirements prospectively in §8 (what it must look like; not executed here) | qwen 3.5 | L | **CLOSED — Phase L (v26)** |
| O23 | Forecast-comparison and multiple-testing literature: paragraph + framework comparison table (White 2000; Hansen 2005; Hansen–Lunde–Nason 2011; Giacomini–White 2006; Clark–West 2007; equivalence testing; FDR) — citations verified at edit time | qwen 3.6 / gpt 7 | O | text, after citation verification |
| O24 | Negative-certificate scoping: N0–N3 claim-strength taxonomy, expiry/invalidation conditions, combining rules | qwen 3.7 / gpt 3 | L | **CLOSED — Phase L (v26)** |
| O25 | Decision-context paragraph per domain (who decides, what a non-retention implies operationally) | qwen 3.9 | L | **CLOSED — Phase L (v26)** |
| O26 | Minimal reproduction package (one script: archived data → rule → gate decomposition + 20 D1/D5 replicates, runs in under an hour) | qwen 3.10 / gpt 9 | N | **CLOSED — Phase N (S3)** |
| O27 | Two-axis reading guide (predictive result × structural interpretation; NEW-11) + clarifying sentence: the M2m decline is a ladder-membership verdict, its predictive margin remains reported | gpt 2 | L | **CLOSED — Phase L (v26)** |
| O28 | Reference implementation of the gates (stable interface, gate decomposition, certificate output) + YAML negative-certificate schema | gpt 3 | N | **CLOSED — Phase N (S3)** |
| O29 | §6.4/§8 epistemic-consequence sentence ("non-retention descriptive rather than evidential for the affected classes") + decision-based margin as an admissible alternative basis (NEW-10; AD4 stands) | gpt 5 | L | **CLOSED — Phase L (v26)** |
| O30 | Exact counts + binomial (Wilson) intervals for every published power/specificity/misattribution rate | gpt 2.2 | M | **CLOSED — Phase M (S1.5)** |
| O31 | More misspecification DGPs (merged with O21) | gpt 2.3 | G | computational |
| O32 | Formal identification decomposition P(retain truth) = P(rank 1) × P(baseline|rank 1) × P(gates|…) from archived components; plus regret/false-attribution metrics | gpt 2.4 | M | **CLOSED — Phase M (S1.5)** |
| O33 | Tiered adoption guidance (core / evidential / strong non-retention; NEW-14) in §9 | gpt 4.1 | L | **CLOSED — Phase L (v26)** |
| O34 | Independent third-party application + usability study (post-release) | gpt 4.2 / qwen 3.5 | H | event |
| O35 | "Proposed" in the title (abstract already says "proposes"; title tweak only) | gpt 4.3 | owner | **CLOSED — executed in v25 (humanized title) ** |
| O36 | Abstract compression (full-findings abstract is a lineage design choice) | gpt 6 | owner | **CLOSED — executed in v25 (full-findings abstract kept) ** |
| O37 | "Portable and domain-free" → moderated phrasing for the obligations | gpt 8 | L | **CLOSED — Phase L (v26)** |
| O38 | Abstract "worked unchanged" parenthetical pointing to the §4 rule-version disclosure | gpt 8 | L | **CLOSED — Phase L (v26)** |
| O39 | Three-quantity terminology sentence (model-class identification / predictive selection / mechanism attribution; "power" keeps its §6.1 definition — NEW-16) | gpt 8 | L | **CLOSED — Phase L (v26)** |

### NEW-10…NEW-17 (adjudicated)

AD4/Phase K binds over any band replacement (NEW-10); frozen output labels over
the two-axis redesign (NEW-11); frozen ladder over M3/M4 removal (NEW-12);
pre-registration over a retrofitted class-grounds criterion (NEW-13); tiers
adopted as an adoption ladder consistent with the mandatory-OC component
(NEW-14); Phase J structure stands, further compression = O16 (NEW-15); "power"
keeps its defined usage (NEW-16); DM-to-supplement = O16 remainder (NEW-17).
Contradiction count: 43 adjudicated, 0 outstanding.

### Owner review 2026-09-13 (NEW-18, NEW-19) — see OWNER_REVIEW_20260913_RELAXATION_AND_PHASING.md

- **NEW-18 (owner):** restructuring to supplementary is approved when merited.
  Unblocks the merited subset of NEW-17/O16: DM mechanics of the §4/§5
  uncertainty layers move to S1 (new S1.4); main text keeps the descriptive
  label, the "verdicts do not rest on DM statistics" sentence, and the one
  decision-relevant statement per domain (§4: 4.33% gate vs 3.8% environment
  sensitivity; §5: one-line label). O16's full 8–10k compression recorded
  not-merited (would cut decision-relevant evidence). §6.5 IC co-primary block,
  §3 Table 2b template, §7 table, §8 frontier stay. O36 (abstract compression)
  remains owner-gated with a concrete proposal in the memo.
- **NEW-19 (review record):** relaxation test of every frozen pre-registration
  and spec rule, criteria = honesty + root cause. Verdict: none merits relaxing
  (5% band: verdicts band-invariant per §1/§4/§5, calibration executed for cod,
  frontier disclosed; output vocabulary: O27 guide inside frozen labels; ladder:
  O24 scopes interpretation; class grounds: prospective criterion proposed;
  "power": O39 disambiguation; executed calibration: no surviving flaw claim).
  O29 extended: reported-verdict band-invariance statement + decision-based
  margin as admissible alternative ("practical-equivalence margin" umbrella, no
  component rename). O19 gained a concrete prospective criterion proposal
  (owner approval pending; mirrors the AD4 machinery). One pending owner
  decision on the Edwards DRAFT: E2m class-grounds convention (with-decline
  proposed). Contradiction count unchanged: 43 adjudicated, 0 outstanding.


**Phase L executed 2026-09-13 → v26_restructured** (apply_phaseL_v25_to_v26.py, 16 rules; PHASE_L_CHANGELOG_v25_to_v26.md): O18 (S2 two-page specification + checklist), O22 (§8 third-domain registration), O24 (§2.2 N0–N3 + expiry/combining), O25 (§4/§5 decision-context paragraphs), O27 (§6.4 two-axis reading guide + §4 M2m sentence), O29 (+NEW-19 band-invariance and decision-based margin), O33 (§9 adoption tiers), O37/O38/O39 wording, NEW-18 (DM mechanics → S1.4). Numeric accounting: 0 added, 13 removed = exactly the moved DM tokens (all in S1.4). Scanners green; coverage pair clean vs v0/v13. v25 frozen. Remaining: O19 (owner approval), O20/O30/O32 (M), O26/O28 (N), O23 (O).
**V12 sweep addendum 2026-09-13:** full-read sweep of both impact-audit transcripts (all 653 lines): every item maps to O18–O39, CV4, or a declined V12 point; no additional open items. NEW-20 (audit N-level semantics vs cumulative implementation — optional refinement, deferred), NEW-21 (redistributive restructuring = §3.5 precedent, declined), NEW-22 (extended instrument-comparison grid — deferred pending Phase M results). 46 adjudicated owner-decision records in total (43 + NEW-18/19), 0 outstanding contradictions.


**Phase M executed 2026-09-13 → S1.5 supplement** (PHASE_M_CHANGELOG_archive_20260913.md): O20 instrument comparison (stated rule / IC-h1 / IC-h5 / hybrid — no dominance, gate = price of specificity), O30 exact counts + Wilson intervals (collision-safe subset), O32 identification decomposition (D2 = inference-limited inside an identification-limited study). Deliverables in `paperF1_retention_framework_v26_supplement.md` §S1.5; frozen JSON `phase_c/results/phaseM_archive_computations_20260913.json`. Zero new simulation; v26 main text untouched (Data-Availability bullet only). Remaining: Phase N (O26/O28), Phase O (O23).

**Phase N+O executed 2026-09-16 → S3+S4 supplement + DRAFT decisions**: O28 (S3.1 fillable audit canvas), O26 (S3.2 record + S3.3 validator `certificate_schema_S3.py`), O23 (S4 verified literature table). Edwards DRAFT: O19 prospective class-grounds criterion (§3a) + E2m convention DECIDED with-decline (§4, root-cause); status line finalisation-gated 2026-09-16. Zero contact with frozen numbers; v26 main text untouched. Remaining: owner-review items NEW-20/NEW-22 (optional), long-term O34/O35.

**Cod Spec-B deep root cause 2026-09-16** (`COD_SPECB_ROOTCAUSE_20260916.md`): three coupled problems — A data availability RESOLVED (post-2026-assessment vintage, from 2026-09-16 web evidence); B T=71 identifiability = the binding one, DEFERRED by frozen sheet v4 (T=71 outside core design; 200-rep pilot only); trigger = dedicated pre-registered Spec-B sheet + owner approval; C execution follows B. Edwards full campaign: pre-flight audit passed after declared-asymmetry M4 fix; registered follow-through per newest-only.

**2026-09-16 (close-out, this pass):**  NEW-20/NEW-22 and O34/O35 are closed as bequeathals — none is highly merited in-version (NEW-20 folds at the NEW-21 submission pass; NEW-22 at the next registered campaign; O34/O35 are external multi-party work, not further in-repo edits).  Edwards full band-calibration campaign LAUNCHED (frozen sheet; pre-flight audit passed with declared-asymmetry M4 fix), ~3.3-4 h runtime; result follow-through = band adoption or frontier + first-origin-2024 scoring per sheet §6.  Cod Spec-B NOT launched in this pass — sheet-frozen deferral stands (see `COD_SPECB_ROOTCAUSE_20260916.md`); trigger remains a dedicated pre-registered Spec-B sheet + owner approval.

**2026-09-16 (three deferred items closed):** (1) deferred Edwards inputs = P_2024 ONLY (R_2024/H_2024/H_2025 already archived); archived as sidecar + build_panel merge hook, owner-gated on the EAA/USGS annual figure. (2) 2029 h=5 = designed waiting (frozen §6), no action. (3) Cod Spec-B dedicated sheet drafted (`SPECIFICATION_cod_T71_frontier_DRAFT_20260916.md`, §3a/§4 as-is, sweep = registered refinement) — owner-gated freeze, not executed.


**2026-09-16 owner-gate lattice audit (root cause):** 'owner gate' was shorthand for several different things. Dispositions:
(1) **P_2024 input** — publish-gated (EAA/USGS annual figure ~early-2026), archived as sidecar + build_panel hook; not an owner decision. (2) **2029 h=5 actual** — designed waiting per frozen Edwards sheet §6 (H3); not an owner decision. (3) **Cod Spec-B sheet freeze** (`SPECIFICATION_cod_T71_frontier_DRAFT_20260916.md`) — the only genuinely parked pre-registration decision: an affirmative owner word is required to lift T=71 out of frozen-v4 deferral; trigger, not drift. (4) **Companion-side edits CV1–CV5** — owner-gated BY INSTRUCTION (never edit E1/E3 without the owner); may be re-presented at E1/E3 finalization. (5) Stale carries removed in this pass: O21 (sheet-gated by frozen v4 §96, props to the Spec-B sheet — not a standalone owner choice), O35/O36 (title/abstract executed in the humanized v25 lineage — 'owner-gated' had outlived the fact). The only remaining genuinely-parked decision is #3; #4 is procedural.

**2026-09-16 (Cod Spec-B sheet improved while parked):** five root-cause integrity fixes recorded in-manifest; frozen v4 cells/rule/replicates untouched. Owner freeze gate stands.

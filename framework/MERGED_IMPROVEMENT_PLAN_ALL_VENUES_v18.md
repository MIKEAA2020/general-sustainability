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
| O6 | Execute the §4.7 prospective-band calibration at the first future application (Edwards 2024–2033 origins; cod Spec B 2025+ vintages) | claude 4.2 / AD4 | H | event-triggered, by design |
| O7 | Companion cross-check when E1/E3 are finalized: every number F1 cites from them (Tables 2–5, the 32-row DM universe vs E1's 28, titles/DOIs, "Table 8 of companion" references) | V8 venues | H | event-triggered consistency pass |
| O8 | Elevate the information-criterion result from a §4.5 table row to its own subsection with stated implications (kept within the AD4 posture: the rule is the pre-registered instrument, the band the prospective replacement) | V9-D | F2 | text, from existing numbers |
| O9 | Co-primary IC check: re-score the archived replicates with the information criterion as a co-primary rule and report whether any verdict changes (context diagnostic, never a gate input — AD5 posture; needs the archived IC-rule definition) | V9-D (option 2) | G | computation, zero new ladder cost |
| O10 | Class-grounds accessibility: state the general principle early (§1) and add a travelling gloss ("structural redundancy" — a module that reduces to a simpler member adds no information regardless of its score); keep the pre-registered output name "declined on class grounds" | V9-E | F | **CLOSED — Phase F (v19)** |
| O11 | Problem-first lead: open the abstract/§1 with the three-sentence framing (module doesn't beat the benchmark — useless module or weak test?); state the standard in one consolidated page separating standard / demonstration / simulation | V9-B, V9-C | F | **CLOSED — Phase F (v19; V9-B was a duplicate, one-page statement added)** |
| O12 | Unpack parenthetical density: move number-dense prose into the existing tables/appendix and narrate findings in plain sentences (e.g., the Spec B deficit chains, §8's summary) | V9-F | F2 | text |
| O13 | Reproducibility-discourse paragraph: connect pre-registration, pinned seeds, archived forecasts and §4.7 to the registered-report / pre-registration literature and M-competition protocols (citations verified at edit time) | V9-G | F | **CLOSED — Phase F (v19)** |
| O14 | Consolidated limitations paragraph in §7 (series length, upper bounds, two domains, M3/M4, in-class specificity) — gather the scattered caveats into one formal statement | V9-I | F | **CLOSED — Phase F (v19)** |
| O15 | Journal targeting (submission strategy): IJF first choice, EMS second, per V9 §1; owner's decision at submission time — no manuscript edit implied | V9-J | — | strategy note |

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
| NEW-3 | F1 §5.2 "R-ENSO variant 0.41 ft worse" / "M2_Rprecip and M2_Rar edge past M1 at h=1 (12.71 vs 12.84)" vs archived companion (E3 v16 Table 7, wave_e_edwards manuscript v2 Table 6, wave6 tablerow audit) | F1 v13+ prose vs E3 archive | archive authoritative: 0.41-worse module is M2_Rar (13.25 vs 12.84); within-0.13 trio is Renso −0.02 / Rprecip −0.04 / combo −0.13; "edge past M1" (14.52/14.67 vs 15.62) is the 2015–23 fixed window. Fixed in Phase F with new Table 5b | closed by data (Phase F, v19) |
| NEW-2 | V9-A/H/C (compress to 8–10k + supplement; reorder demonstration-before-simulation; separate standard/demonstration/simulation layers) vs the AD6 one-coordinated-rewrite rule and the no-content-loss policy | V9 vs AD6/coverage policy | not content contradictions — owner-gated structural proposals; if approved they form one coordinated structural phase (Phase J) with a supplement vehicle, guarded by the content-coverage scanner; if declined, only the text-level items (O10–O14) proceed | owner-gated |

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
open items: **15** (O1–O15) — O1–O3, O10, O11, O13, O14 form the small text pass
(Phase F, v19); O8, O12 a second text pass; O4, O5, O9 optional computation; O6, O7
event-triggered; O15 submission strategy; Phase J structural work awaits the owner's
decision on NEW-2. Nothing in V9 re-opens any reported verdict or any frozen element.
## 7. Status summary

Phases A–E **DONE** (v14 → v18); venues V1–V8 **fully incorporated**; contradiction
count across all venues: **25 adjudicated, zero outstanding**; open items: **7**
(O1–O7), of which O1–O3 are a small optional text pass, O4–O5 optional computation,
O6–O7 event-triggered. Venue V9 (qwen framework journal fit) is **pending content** —
the pipeline above folds it in without re-opening anything.

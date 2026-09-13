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
| V9 | **Qwen — framework journal fit** | `uploads/qwen framework journal fit.txt` | **arrived empty (0 bytes); content pending. Nothing incorporated or adjudicated from it yet — merge pipeline ready (§5).** |

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
| O1 | Abstract: add the §4.5 caveat that the information criterion does not enforce the multi-year persistence requirement (register 6.7, partial) | qwen 6.7 | F | text micro-fix |
| O2 | §5.2 "not second fibre of this specification" — informal term | register item 9 (partial) | F | text micro-fix |
| O3 | Climate-module table in §5.2 (margins per module per horizon; data archived) | claude 2.3 / register item 8 (remainder) | F | table from archived CSVs |
| O4 | M3/M4-as-truth operating-characteristic cells (optional in the original plan, never executed) | register §5 (optional) | G | computational, optional |
| O5 | Full registered designs: T=71 at 200 replicates; Amendment-1 eight cells × 200 (measured ≈25 CPU-hours) | Amendment 1 / §4.2 | G | computational, hardware-gated |
| O6 | Execute the §4.7 prospective-band calibration at the first future application (Edwards 2024–2033 origins; cod Spec B 2025+ vintages) | claude 4.2 / AD4 | H | event-triggered, by design |
| O7 | Companion cross-check when E1/E3 are finalized: every number F1 cites from them (Tables 2–5, the 32-row DM universe vs E1's 28, titles/DOIs, "Table 8 of companion" references) | V8 venues | H | event-triggered consistency pass |

### 2.3 PENDING INPUT

- **V9 (qwen framework journal fit)** — file arrived empty. Merge pipeline in §5;
  expected to map mostly onto Phase F-style items (presentation, journal conventions,
  structure); any computational or verdict-level claim will be adjudicated before
  implementation, exactly like AD1–AD8.

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

- **Phase F — text consolidation pass** (O1, O2, O3; candidate for the next version,
  v19, whenever the owner approves; all three are text/table-only, no new computation,
  no verdict contact):
  - O1: one clause in the Abstract after the IC-dominance sentence: "although the
    criterion does not encode the requirement that a module beat persistence at the
    multi-year horizon" (mirrors §4.5).
  - O2: replace "not second fibre of this specification" with "outside this
    specification".
  - O3: a climate-module table in §5.2 (module, h, RMSE vs AR(1) vs climatological
    flux; values from the archived per-origin files; the companion's Table 8
    reference stays).
- **Phase G — optional computation** (O4, O5): M3/M4-as-truth cells and the full
  200-replicate T=71 / 8×200 designs; hardware-gated (≈25 CPU-hours measured);
  results would refine, never reverse, the reported verdicts (pre-registered
  thresholds already stated).
- **Phase H — event-triggered** (O6, O7): run the §4.7 calibration at the first
  future application; run the companion cross-check when E1/E3 are finalized.
- **Perpetual guardrails:** every version passes the four scanners; register §5 and
  MANIFEST updated per phase; all artifacts pushed to
  `edwards-framework-e1-audit-implementation`; main never modified.

---

## 7. Status summary

Phases A–E **DONE** (v14 → v18); venues V1–V8 **fully incorporated**; contradiction
count across all venues: **25 adjudicated, zero outstanding**; open items: **7**
(O1–O7), of which O1–O3 are a small optional text pass, O4–O5 optional computation,
O6–O7 event-triggered. Venue V9 (qwen framework journal fit) is **pending content** —
the pipeline above folds it in without re-opening anything.

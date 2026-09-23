# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v9)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v44_Automatica_routes.tex` + supplementary).
**Scope:** consolidated follow-up programme — in-manuscript open problems, the
adjudicated nonstandard proposals, the unification and generalization
programmes, the review-of-record demand list, the evidence-gap closure sweep,
and editorial items.
**Disambiguation:** the general-theory programme's separate "Paper 2" (the
Typed Theorem Atlas, `papers/paper2_theorem_atlas/`) is a different paper;
its venue/split memo is out of scope here.

**Sources consolidated:** v44 §6.5/§7/§9 and its Open Problem registry;
`uploads/obstruction calculus nonstandard.txt` and its adjudication
`paper2_nonstandard_joint_audit.md` (+ `paper2_nonstandard_verification.py`,
51/51); `paper2_evidence_gaps.md` (10-gap audit of v37 — **fully incorporated
in v2 of this roadmap**); `paper2_v31_verification_report.md` (the gpt
review's line-by-line disposition table); `uploads/suggested generalizations.txt`;
`uploads/6 parallel mechanisms.txt`; `uploads/gpt paper 2 automatica.txt`;
`uploads/qwen p2.txt`; the batch-7 wave6 sentence-level diff scan; the
addenda trail (v32–v43).

**v9 changes:** C3 is **DRAFTED** with D2 and D3 absorbed —
`successor_five_layer_v1` ("Five Layers of Obstruction: A Successor
Architecture for Viability under Incomplete Observation"; standalone
lineage name, no paperN prefix): the five layers (dynamics, belief-action,
timing, certification, policy class) each carrying the companions'
certificate families; D2 as Section 3 (read-then-act per-cell semantics,
refinement monotonicity, the incomparable-structures instance with
opposite verdicts, erosion 28 vs 26 viable pairs); D3 as Section 4
(exit-time values, level-set identities on the audited grids, level sets
equal to the bridge's LP thresholds); one verified firing-only instance
per layer boundary; 7/7 exact check families. The mainline (A, B, C,
D1-D3) is fully drafted; remaining: D4-D13 as they mature.

**v8 changes:** D1 is **DRAFTED** — `paper2_stochastic_selector_v1`
("The Stochastic Selector: Exact Rational Belief-State Safety Values
under Partial Observation"): the belief-state value as the stochastic
selector, piecewise-linear value iteration with rational alpha-vectors,
deterministic-limit degeneration (survived-mass formula recovering the
robust verdicts), certificates as deficit lower bounds, and the
certificate–value agreement theorem on the audited 48-cell grid (kink
locus = certificate boundary; deficit exactly one half; class declaration
quantified); machine-verified, 10/10 exact check families. Also: the
viable-selector spine paper advances to **v2** (layout repair only —
Table 1 wrapped columns and two split displays; zero overfull boxes;
content and verification record unchanged).

**v7 changes:** C1–C2 are **DRAFTED** as paper 3 v1
`paper2_viable_selector_v1` ("The Viable Selector: A Unifying Framework
for Obstruction Certificates under Incomplete Observation"): the recursive
viable-selector correspondence with finite-horizon exactness and the
measurable-selection qualification (Theorem 1), the meta-theorem with
monotone soundness and the policy-class corollary (Theorem 2), the three
bridging propositions (correspondence ladder; timing as blind-window
predecessor emptiness; certification as label selection), the
specialization table, and the source's over-unification discipline kept
intact (Section: what is not unified). Machine-verified in exact arithmetic
on the companions' worked systems (7/7 check families). **D1's stochastic
theory is next** (previewed as the paper's closing outlook), then C3.

**v6 changes:** Track B is **DRAFTED end-to-end** — companion v1
`paper2_companion_recourse_bridge_v1` ("Finite Nonviability Certificates
under Delayed Information", main + supplementary with complete proofs),
carrying B1 (the bridge theorem, §§2–5, 7), B2 (erosion identity, §9),
B3 (held-control exactness remark, §5.1), B4 (solver-certified mesh study,
§6.4 — the audit's one unexecuted verification step, LP optimality by an
actual HiGHS run, is closed with exact primal/dual witnesses, 9/9 checks;
the 51-check predecessor record re-confirmed), B5 (scope delimitations,
§10). Submission-ready pending the owner's venue decision (SCL-class per
Doc 1 §14 and the audit).

**v5 changes:** A3 is **EXECUTED in v48** — the qwen-p2 editorial programme
adjudicated point by point (three accepted edits: the §1 "necessity side"
sentence rewritten in converse/negation form; the erosion passage compressed;
the §2.4 local-letters lead neutralized; nine items already satisfied with
verification pointers; four rejected with reasons, including the central-object
rename and global symbol renames per the recorded guardrails); the batch-7
wave6 v5→v10 dropped-segment register reviewed once against the current source
with **no load-bearing loss** and no restoration required. Dispositions:
`paper2_obstruction_calculus_v48_addendum.md`. **Track A is complete**; the
manuscript is submission-ready pending the owner's venue decision.

**v4 changes:** A5 and A6 are **incorporated in v46** (`682b467`) — Theorem 4
(LP instantiation of the timing certificate), Example 2 (unbounded relaxation
gap), the adjoint-duality remark (§3.3), and Propositions 9–10 (exact two-phase
decomposition; window-measurability no-go, §7), with the supplementary advanced
to v46 and a 12-check exact-arithmetic verification record. Gaps 5 and 8 of the
A4 table are **closed in v47** — the §9 worked belief-state instance (exact
safety values on the audit grid; certificate partition reproduced cell by cell;
degenerate bound attained; unrestricted-policy contrast) and the §8 two-patch
protection audit (minimal two-dimensional epistemic emptiness; certainly-safe
readings y ≥ 4; all nonviable beliefs common-action-certified), with a 12-check
verification record regenerating both new tables verbatim. Track A remainder:
the A3 editorial sweep (planned v48); the full multidimensional numerical
campaign remains deferred as stated in §8.

**v3 changes:** the two theorem candidates formerly filed under Track B ("B6" timing-instantiation LP theorem; "B7" partial converse) are re-lettered **A5/A6** — they are paper-2 manuscript content if proven (the evidence-gap audit itself proposed them as manuscript closures), gated only by the new-mathematics rule, not companion material; Track B is pinned to the continuous-to-finite companion (B1–B5) proper. **v2 changes:** Track A gains the evidence-gap closure sweep (A4) — the one
audit previously under-incorporated — with per-gap status against the current
manuscript; A1 is anchored to the v31 disposition report; Track B gains the
timing-instantiation theorem and the partial-converse candidate; guardrails
recorded; sequencing updated.

---

## Track A — The Automatica manuscript itself (pre-submission)

**A1. Review-of-record verification sweep.** Baseline:
`paper2_v31_verification_report.md` — the line-by-line disposition table
(FIXED / ALREADY SATISFIED / REJECTED) for the `gpt paper 2 automatica`
review (Theorem 6 → static-observation reduction; Remark 3 → policy-specific
claim; belief-history circularity; `𝒜_N` definition; blind-window class
re-quantification; finite-checkability phrasing; Proposition 5 scoping; and
the remainder). **Action:** re-diff every v31 disposition against the v44
source (drift check across v32–v44), record a fresh disposition table.

**A2. Open problems carried in v44:** (i) the **residual dynamic gap** — a
complete continuous-time characterization of the
insufficient-post-observation-recourse mode *without* the §3.7 oracle
relaxation; (ii) **timing-certificate checkability** for continuous
blind-window control classes (finite classes settled; Open Problem);
(iii) the **deferred numerical campaign**.

**A3. Editorial programme (EXECUTED in v48 — dispositions in the v48 addendum).** (from `qwen p2`): rename the central object;
state the unifying idea early; reduce the number of named mechanisms; demote
elementary results; replace "necessity side" language; trim the notation
section; reduce rhetorical framing; handle Appendix A; the three proposed
figures; estimation-tube connection; audit "complete proof" phrasings.
*Add (batch-7 QC):* review the wave6 v5→v10 dropped-segment register once
for any load-bearing content lost in the early condensation.

**A4. Evidence-gap closure sweep** (from `paper2_evidence_gaps.md`, audit of
v37; statuses below are to be *verified* on v44 during the sweep):

| Gap | Content | Status / action |
| --- | --- | --- |
| 1 (critical) + M1 + M3 | Declarations say "no code was used or produced" while §8 presents a "reproducible" coverage audit (30/12/42 cells); audit code unarchived; the Zenodo citation points at a *different* paper | **Verify on v44; if open: archive the delayed hidden-regime solver + coverage-figure generator (`route2_numerics.py`) at the Zenodo record, give it its own citation, cite from §8, machine-generate Table 1, rewrite the declarations** |
| 2 | Abstract's finite-checkability claim vs the timing obstruction | Phrasing fixed in v31 (verified v45); substantive close **done in v46** via A5 (Theorem 4) |
| 3 | Complementarity (barrier certificates, estimation tubes) asserted, not demonstrated | **Open.** Add "one shared example, three methods": one plant; what barrier says/cannot say; what the tube reduction returns; which obstruction fires; what design change it licenses |
| 4 | Helly sparse witness (Prop 4) hypotheses undefended at the boundary | **Open.** Short counterexample (non-convex safe-action set, empty intersection, no m+1 witness) or a precise convexity-scope remark |
| 5 | §9 probabilistic lift asserted, not demonstrated | **CLOSED in v47** (§9 worked instance: exact V_k on the audit grid; partition reproduced; degenerate bound attained; feeds D1) |
| 6 | Flagship timing certificate lacks a general computational instantiation | **CLOSED in v46** (Theorem 4: LP instantiation over polytope-declared classes; continuous classes remain a template, as recorded in §3.3) |
| 7 | Post-observation-recourse mode named, never exhibited | **Closed in v43/v44** (three-branch recourse instance §3.7; silent-certificates instance S3/A.3) — verify wording |
| 8 | Governance audience: no empirical anchor; case study one-dimensional | **CLOSED in v45 + v47**: (ii) calibration paragraph (v45); (i) two-patch protection audit (v47, Table 3); (iii) optional real-schedule illustration not taken (marked optional in the roadmap source) |
| 9 | "Complete proofs in the Supplementary" not literally true (Prop 4 main-only; §7/§9 main-only) | **Open (cheap).** Reword §1.4: proofs of the §3 certificates in the supplement; §7/§9 proved in the main |
| 10 | "Sound but not complete" never quantified | **CLOSED in v46** (Propositions 9–10: exact decomposition + window-measurability no-go) |
| M2 | §6.4 "bias is the one governance structures can omit" — uncited behavioral claim | Cite the information-design/governance literature or soften |

**A5 (INCORPORATED in v46 — Theorem 4, Example 2, and the adjoint-duality remark, §3.3).
Polyhedral timing-instantiation theorem** [Gap 2b/6]: H3.2 as a finite LP /
robust-reachability check for piecewise-constant blind-window controls over
polyhedral data (or the scoped-limitation statement with the
constant-observation, hold-until-T_obs case fully worked). Turns the
flagship certificate from template to algorithm; the technical crux is the
relaxed-vs-implementable sigma* gap that any occupancy-measure reduction
must close or bound. Incorporated in §3.3 of v46 (entered at the checkability paragraph, before
Figure 3) with the sharpness instance and the Farkas dual; machine-verified
(paper2_v46_a5a6_verification.py, 12/12).

**A6 (INCORPORATED in v46 — Propositions 9–10, §7).
Quantified converse / no-go** [Gap 10]: either a class-restricted partial
converse ("both certificates silent on [0,T] implies some implementable
policy viable on [0,T]", generalizing the joint-completeness remark beyond
the delayed hidden-regime class) or a counterexample showing no converse
without the full recursion. Known subtlety: the naive statement is **false**
— the S3/A.3 recourse instance is certificate-silent yet nonviable — so the
content is the precise characterization of when the pair is complete.
Upgrades the central concession into a boundary result. Incorporated in §7 of
v46 as the exact two-phase decomposition and the window-measurability no-go;
machine-verified (paper2_v46_a5a6_verification.py, 12/12).

**Guardrails (do not disturb — per the same audit):** the ladder structure
and its cross-referencing; supplementary constructions A.1
(coupling-creates-viability) and A.2 (emptiness-despite-factorwise-viability);
the coverage audit as the right evidence type once reproducible; the
hypothesis/equation tag consistency achieved in the reorder.

## Track B — Companion paper (B1–B5 only): recourse-aware continuous-to-finite certification — DRAFTED as v1 (see v6 changes)

Adjudicated and partially merged (v43/v44): the three-branch instance (§3.7),
the oracle-recourse proposition (§3.7), the "m+1 fails for blind control
functions" caveat (§3.4), the sparse-dual robustness lemma (§3.2). Core of
what remains (venue: SCL-class, per Doc 1 §14 and the audit — not an
Automatica claim yet):

- **B1. (DRAFTED in companion v1; the LP-solver verification step EXECUTED)**
  The continuous-to-finite bridge (adjoint safety rows; finite
  obstruction certificate Γ; moment-approximation LP with certified value
  sandwich; completeness under refinement; atomic dual representation; sparse
  witnesses). **The one unexecuted verification step: LP optimality must be
  certified by an actual solver run.**
- **B2.** The refinement-erosion identity (φ_U superadditivity; 3,240
  rational pairs verified).
- **B3.** Lemma 6.1 (averaging ⇒ held-control polyhedron).
- **B4.** The mesh/complexity study (ρ(h) = 0.06 − Th/4; factor-2 sharpness).
- **B5.** Scope delimitations (no general-purpose computational-calculus
  claim). (Former B6/B7 are now A5/A6 — manuscript content, not companion.)


## Track C — Unification programme ("6 parallel mechanisms")

- **C1. (DRAFTED in the viable-selector paper v1, Sections 4-5)** The four one-step mechanisms as specializations of the **viable
  selector under information**; the timing obstruction as its blind-window
  predecessor-emptiness form; the fibre criterion connected but not a
  policy-viability obstruction.
- **C2. (DRAFTED in the viable-selector paper v1, Sections 3-4)** The **unified meta-theorem** (admissible ∧ implementable ∧
  tube-safe ∧ recursively viable ⇒ impossibility of the class) with the
  strengthening lemmas (nested action correspondences; timing as predecessor
  emptiness; certification as label selection).
- **C3. The five-layer architecture — DRAFTED (`successor_five_layer_v1`)**
  (dynamic → belief-action → timing
  → certification → policy-class), respecting the source's over-unification
  warning; strongest claim only at the precision its §13 supports.
- **C4.** Destination: the successor paper / major-restructuring spine —
  realized by `successor_five_layer_v1`.

## Track D — Generalization catalogue (`suggested generalizations.txt`)

D1 belief-state viability kernels — **DRAFTED** (`paper2_stochastic_selector_v1`)
(seeded by v44 §9; A4-Gap 5 supplies its first worked instance) · D2 general information structures — **DONE** (successor §3) · D3 exit-time
value functions — **DONE** (successor §4) · D4 multiple floors / vector constraints · D5 complete
finite-horizon certificates · D6 certificates as dual objects across the
four obstruction types · D7 policy-class taxonomy · D8 monitoring design ·
D9 beyond constant drift (state-dependent, comparison functions,
multi-constraint exit) · D10 hidden parameters / adaptive observation ·
D11 hybrid systems · D12 approximate / buffered viability · D13
decentralized / institutional observation.

## Track E — Sequencing

| Priority | Item | Depends on |
| --- | --- | --- |
| 1 | A1 sweep ✓ (v45) + A4 sweep ✓ (v45; Gaps 5/8 closed v47) + A3 editorial sweep ✓ (v48) — **Track A complete** → Automatica submission (owner: venue decision) | nothing |
| 2 | B1–B5 companion paper (LP-solver campaign) | nothing (parallel) |
| 3 | A5/A6 theorem candidates — **DONE** (incorporated in v46: §3.3, §7) | — |
| 4 | C1–C2 meta-theorem consolidation — **DONE** (viable-selector paper v1: `paper2_viable_selector_v1`) | Track A settled |
| 5 | D1 belief-state theory — **DONE** (`paper2_stochastic_selector_v1`, Gap 5 instance first) | C3 chosen |
| 6 | C3 five-layer successor paper — **DONE** (`successor_five_layer_v1`; absorbs D2/D3; D6 cited as outlook) | 4–5 |
| 7 | D4–D13 as they mature | per-item |

*Every claim above is a pointer into the cited sources; nothing here creates
theorem status. The strengthened-verification discipline (exact rational
re-derivation before acceptance; solver runs before LP-optimality claims)
applies to all tracks.*

# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v2)

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

**v2 changes:** Track A gains the evidence-gap closure sweep (A4) — the one
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

**A3. Editorial programme** (from `qwen p2`): rename the central object;
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
| 2 | Abstract's finite-checkability claim vs the timing obstruction | Phrasing fixed in v31 (verify survives); the substantive close is option (b) — see B6 |
| 3 | Complementarity (barrier certificates, estimation tubes) asserted, not demonstrated | **Open.** Add "one shared example, three methods": one plant; what barrier says/cannot say; what the tube reduction returns; which obstruction fires; what design change it licenses |
| 4 | Helly sparse witness (Prop 4) hypotheses undefended at the boundary | **Open.** Short counterexample (non-convex safe-action set, empty intersection, no m+1 witness) or a precise convexity-scope remark |
| 5 | §9 probabilistic lift asserted, not demonstrated | **Open.** Worked instance: compute \(V_k\) for the hidden-regime POMDP, tabulate against certificate verdicts (feeds D1) |
| 6 | Flagship timing certificate lacks a general computational instantiation | **Open → B6** |
| 7 | Post-observation-recourse mode named, never exhibited | **Closed in v43/v44** (three-branch recourse instance §3.7; silent-certificates instance S3/A.3) — verify wording |
| 8 | Governance audience: no empirical anchor; case study one-dimensional | **Open.** Cheapest-to-strongest: (i) second, two-dimensional instance (coupled-patch, coarse shared indicator); (ii) calibration paragraph mapping ε, T_obs, bias b, floor onto stock-assessment-estimable quantities; (iii) optional real observation-schedule illustration |
| 9 | "Complete proofs in the Supplementary" not literally true (Prop 4 main-only; §7/§9 main-only) | **Open (cheap).** Reword §1.4: proofs of the §3 certificates in the supplement; §7/§9 proved in the main |
| 10 | "Sound but not complete" never quantified | **Open → B7** |
| M2 | §6.4 "bias is the one governance structures can omit" — uncited behavioral claim | Cite the information-design/governance literature or soften |

**Guardrails (do not disturb — per the same audit):** the ladder structure
and its cross-referencing; supplementary constructions A.1
(coupling-creates-viability) and A.2 (emptiness-despite-factorwise-viability);
the coverage audit as the right evidence type once reproducible; the
hypothesis/equation tag consistency achieved in the reorder.

## Track B — Companion paper: recourse-aware continuous-to-finite certification

Adjudicated and partially merged (v43/v44): the three-branch instance (§3.7),
the oracle-recourse proposition (§3.7), the "m+1 fails for blind control
functions" caveat (§3.4), the sparse-dual robustness lemma (§3.2). Core of
what remains (venue: SCL-class, per Doc 1 §14 and the audit — not an
Automatica claim yet):

- **B1.** The continuous-to-finite bridge (adjoint safety rows; finite
  obstruction certificate Γ; moment-approximation LP with certified value
  sandwich; completeness under refinement; atomic dual representation; sparse
  witnesses). **The one unexecuted verification step: LP optimality must be
  certified by an actual solver run.**
- **B2.** The refinement-erosion identity (φ_U superadditivity; 3,240
  rational pairs verified).
- **B3.** Lemma 6.1 (averaging ⇒ held-control polyhedron).
- **B4.** The mesh/complexity study (ρ(h) = 0.06 − Th/4; factor-2 sharpness).
- **B5.** Scope delimitations (no general-purpose computational-calculus
  claim).
- **B6** *(new, from Gap 2b/6)*: a polyhedral checkability theorem for the
  timing obstruction — H3.2 as a finite LP / robust-reachability check for
  piecewise-constant blind-window controls (or, if genuinely hard, the
  scoped-limitation statement with the constant-observation,
  hold-until-T_obs special case fully worked). Also the natural Track A
  addition if it lands before submission.
- **B7** *(new, from Gap 10)*: a quantitative partial converse — "if no
  certificate fires on [0,T], some policy is viable on [0,T]" — or a
  separation counterexample proving no such converse exists; the coverage
  audit's "jointly complete in the delayed class" is the existing gesture.
  Upgrades the paper's central concession into a boundary result.

## Track C — Unification programme ("6 parallel mechanisms")

- **C1.** The four one-step mechanisms as specializations of the **viable
  selector under information**; the timing obstruction as its blind-window
  predecessor-emptiness form; the fibre criterion connected but not a
  policy-viability obstruction.
- **C2.** The **unified meta-theorem** (admissible ∧ implementable ∧
  tube-safe ∧ recursively viable ⇒ impossibility of the class) with the
  strengthening lemmas (nested action correspondences; timing as predecessor
  emptiness; certification as label selection).
- **C3.** The **five-layer architecture** (dynamic → belief-action → timing
  → certification → policy-class), respecting the source's over-unification
  warning; strongest claim only at the precision its §13 supports.
- **C4.** Destination: the successor paper / major-restructuring spine.

## Track D — Generalization catalogue (`suggested generalizations.txt`)

D1 belief-state viability kernels (seeded by v44 §9; A4-Gap 5 supplies its
first worked instance) · D2 general information structures · D3 exit-time
value functions · D4 multiple floors / vector constraints · D5 complete
finite-horizon certificates · D6 certificates as dual objects across the
four obstruction types · D7 policy-class taxonomy · D8 monitoring design ·
D9 beyond constant drift (state-dependent, comparison functions,
multi-constraint exit) · D10 hidden parameters / adaptive observation ·
D11 hybrid systems · D12 approximate / buffered viability · D13
decentralized / institutional observation.

## Track E — Sequencing

| Priority | Item | Depends on |
| --- | --- | --- |
| 1 | A1 sweep + A4 sweep (incl. Gap 1 code archiving) + A3/A4 editorial items → Automatica submission | nothing |
| 2 | B1–B5 companion paper (LP-solver campaign) | nothing (parallel) |
| 3 | B6, B7 (if pre-submission B6 upgrades the paper) | 1 in progress |
| 4 | C1–C2 meta-theorem consolidation | Track A settled |
| 5 | D1 belief-state theory (Gap 5 instance first) | C3 chosen |
| 6 | C3 five-layer successor paper absorbing D2/D3/D6 | 4–5 |
| 7 | D4–D13 as they mature | per-item |

*Every claim above is a pointer into the cited sources; nothing here creates
theorem status. The strengthened-verification discipline (exact rational
re-derivation before acceptance; solver runs before LP-optimality claims)
applies to all tracks.*

# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v1)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v44_Automatica_routes.tex` + supplementary).
**Scope:** consolidated follow-up programme — in-manuscript open problems, the
adjudicated nonstandard proposals, the unification and generalization
programmes, the review-of-record demand list, and editorial items.
**Disambiguation:** the general-theory programme's separate "Paper 2" (the
Typed Theorem Atlas, `papers/paper2_theorem_atlas/`) is a different paper;
its venue/split memo is out of scope here.

**Sources consolidated:** v44 §6.5/§7/§9 and its Open Problem registry;
`uploads/obstruction calculus nonstandard.txt` (two proposal documents) and
its adjudication `latex/paper2_nonstandard_joint_audit.md` (+ `paper2_nonstandard_verification.py`, 51/51 checks); `uploads/suggested generalizations.txt`;
`uploads/6 parallel mechanisms.txt`; `uploads/gpt paper 2 automatica.txt`
(line-level review of record); `uploads/qwen p2.txt`; the audit/revision
trail (`paper2_evidence_gaps.md`, `paper2_v31_verification_report.md`,
addenda v32–v43, `paper2_strengthening_prompt.md`).

---

## Track A — The Automatica manuscript itself (pre-submission)

**A1. Review-of-record verification sweep.** The `gpt paper 2 automatica`
review's demand list (Theorem 6 static-observation completeness; the Remark 3
certainty-equivalence claim; continuous-time review semantics; belief
definition circularity; kernel-notation hierarchy; Theorems 1–4 quantifier
fixes; blind-window hypothesis; initial-observation convention;
obstruction-tree quantifiers; fibre/checkability statements; Proposition 5
notation; example separation; coverage-audit reproducibility; the fishery
example's computational claim; §9 probabilistic section; novelty positioning;
numbering/typography) is the checklist of record. v44's current claims
already reflect the corrected architecture — completeness is now claimed only
for the one-step and static-observation classes, with the residual dynamic
gap stated as an Open Problem, and the static case reduces exactly to
open-loop robust viability. **Action:** re-confirm each demand item against
the v44 source one by one before submission; record the disposition table.

**A2. Open problems carried in v44** (these are the paper's own declared
frontier): (i) the **residual dynamic gap** — a complete continuous-time
characterization of the insufficient-post-observation-recourse mode *without*
the oracle relaxation of the §3.7 certificate; (ii) **checkability of the
timing certificate** for continuous blind-window control classes (finite
classes are settled; the continuous case is a template — Open Problem);
(iii) the **deferred numerical campaign** (explicitly "future work").

**A3. Editorial programme for the next revision** (from `qwen p2`): rename
the central object; state the unifying idea early; reduce the number of named
mechanisms; demote elementary results (finite-time exit certificate, fibre
criterion, certainty-equivalence remark) to propositions/remarks or the
supplement; replace "necessity side" language; trim the notation section;
reduce rhetorical sustainability framing; handle Appendix A (interesting but
tangential — supplement or cut); the three proposed figures (observation
fibre crossing a safe boundary; incompatible safe controls; delayed
information); strengthen the relation to estimation tubes; audit every
"complete proof" phrasing against existence assumptions.

## Track B — Companion paper: recourse-aware continuous-to-finite certification

The nonstandard follow-up (Doc 1 of `obstruction calculus nonstandard.txt`)
was adjudicated item-by-item (exact rational re-derivation; 51/51 checks).
Accepted content already merged into v43/v44: the three-branch worked
instance with explicit LP, Farkas certificate and mesh study (§3.7,
compressed); the oracle-recourse certificate proposition (§3.7); the
"m+1 fails for blind control functions" scoping caveat (§3.4); the sparse-dual
robustness lemma (§3.2). **What remains — and forms the companion paper's
core** (venue per Doc 1 §14 and the audit: *Statistics, Optimization and
Information Computing*-class / SCL; explicitly not an Automatica claim yet):

- **B1.** The full continuous-to-finite bridge: adjoint safety rows, the
  finite obstruction certificate Γ, the moment-approximation LP with certified
  value sandwich, completeness under mesh refinement, atomic dual
  representation, sparse witnesses (Doc 1 §§2–5, 10, 12.3 — verified
  internally; **LP optimality must be certified by an actual solver run**,
  which the audit flags as the one unexecuted step).
- **B2.** The refinement-erosion identity (φ_U superadditivity; verified on
  3,240 rational pairs) — belongs to the LP certificate functional.
- **B3.** Lemma 6.1 (averaging ⇒ held-control polyhedron; sound, new).
- **B4.** The mesh/complexity study with the closed-form error law
  ρ(h) = 0.06 − Th/4 and the factor-2 sharpness margin.
- **B5.** Scope statement per Doc 1 §13–14 delimitations (no general-purpose
  computational-calculus claim).

## Track C — Unification programme ("6 parallel mechanisms")

The paper's mechanisms are one family, not six: the unifying object is the
**viable selector under information**. Programme items, in increasing order
of ambition:

- **C1.** The four one-step mechanisms (dynamic exit, admissibility/common
  action, certainty-equivalence trap, certification) as specializations of
  one selector problem; the timing obstruction as its blind-window
  predecessor-emptiness form; the fibre criterion connected but explicitly
  *not* a policy-viability obstruction (keep the boundary honest).
- **C2.** The **unified meta-theorem** (Doc §9): no policy is simultaneously
  admissible under the policy class, implementable under the information
  structure, tube-safe over the review interval, and recursively viable —
  with the strengthening lemmas (nested action correspondences; timing as
  predecessor emptiness; certification as label selection).
- **C3.** The **five-layer architecture** (Doc §10; mirrors qwen §4.3's
  hierarchy): Layer 1 full-information dynamic obstructions → Layer 2
  one-step belief-action → Layer 3 timing → Layer 4 certification →
  Layer 5 policy-class. Respect Doc §12's explicit warning about what must
  *not* be unified too aggressively; state the strongest claim only at the
  precision Doc §13 supports.
- **C4.** Destination: this programme is the natural spine for the successor
  paper (or the major revision's restructuring), and supplies qwen's
  "state the unifying idea early" demand in one stroke.

## Track D — Generalization catalogue (from `suggested generalizations.txt`)

Thirteen directions, each stated in the source with definitions; the lead
item is already seeded by v44 §9:

- **D1. Belief-state viability kernels** (the stochastic lift; v44 §9
  defines the safety value \(V_k(b)\) and its obstruction certificate —
  develop to a full theory).
- **D2.** General information structures beyond a static observation map
  (filtrations, delayed/partial schedules).
- **D3.** Exit-time value functions for the timing obstruction.
- **D4.** Multiple floors / vector constraints.
- **D5.** Complete finite-horizon certificates (beyond sufficient ones).
- **D6.** Certificates as dual objects across all four obstruction types
  (common-action, timing, fibre, barrier).
- **D7.** Systematic policy-class taxonomy.
- **D8.** From obstruction to **monitoring design** (observation scheduling).
- **D9.** Dynamic obstruction beyond constant drift: state-dependent drift,
  comparison functions, multiple-constraint exit.
- **D10.** Hidden parameters and adaptive observation.
- **D11.** Hybrid / discrete-continuous systems (careful — mode semantics).
- **D12.** Approximate and buffered viability (robustness margins).
- **D13.** Decentralized / institutional observation (links to the
  programme's institutional-feedback strand).

## Track E — Sequencing

| Priority | Item | Depends on |
| --- | --- | --- |
| 1 | A1 verification sweep + A3 editorial pass → Automatica submission | nothing |
| 2 | B1–B5 companion paper (with the LP-solver campaign) | nothing (parallel) |
| 3 | C1–C2 meta-theorem consolidation | Track A settled |
| 4 | D1 belief-state theory (extends v44 §9) | C3 architecture chosen |
| 5 | C3 five-layer successor paper incorporating D2/D3/D6 | 3–4 |
| 6 | D4–D13 as they mature | per-item |

*Every claim above is a pointer into the cited sources; nothing here creates
theorem status. The strengthened-verification discipline (exact rational
re-derivation before acceptance) applies to all tracks.*

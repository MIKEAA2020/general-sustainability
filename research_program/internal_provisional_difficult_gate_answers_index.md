# Internal Provisional Answers — Difficult Gates

## Status

Both answers are complete internal inputs for future joint adjudication. Neither is authorized for manuscript implementation.

**[Adjudication update 2026-08-26:** see `difficult_gate_answers_adjudication_2026-08-26.md`. The composition answer has been jointly adjudicated with ER044–ER047 and implemented as the controlling corrected theorem record `A001_restricted_composition_theorem_corrected.md` (that adjudication predates this note's original text and is now recorded here). The novelty answer is partially adjudicated: its verdict is confirmed at the bounded-search level by the executed E6 audit, its recommendation-3 theorem exists as the proved R01 record, and its journal decision remains gated on the full-text pass at paper-drafting time.**]**

## 1. A001 composition theorem

**File:** `internal_provisional_A001_composition_theorem_answer.md`

**Verdict:** the submitted theorem is repairable but invalid as proved. Separate local safe-control feasibility does not imply joint feasibility. The internal answer supplies:

- a minimal shared-control counterexample;
- a repaired joint robust safe-control theorem;
- independent- and shared-control corollaries;
- coupling destruction and rescue examples;
- selector, well-posedness, interface, and strong-invariance requirements;
- publication routing and remaining proof obligations.

**Implementation status:** ADJUDICATED AND IMPLEMENTED — the external responses arrived (ER044–ER047), the joint audit was executed (`external_reviews/joint_audit_A001_composition_internal_ER044_ER047.md`), and the controlling corrected theorem record is `research_program/A001_restricted_composition_theorem_corrected.md`.

## 2. Paper 1 Operator II novelty

**File:** `internal_provisional_Paper1_operatorII_novelty_answer.md`

**Verdict:** the exact-tube backward recursion is correct but structurally standard relative to viability/capture-basin, robust predecessor, reach-avoid-stay, dynamic-programming, and hybrid reachability literatures. Typed sustainability semantics may be distinctive but do not create theorem novelty by naming alone.

The answer recommends:

- no claim to invention of backward reachability;
- keeping Paper 1's independent-result gate open;
- adding a typed false-positive/impossibility theorem and worked transition example;
- systematic literature and future external audits before deciding journal status.

**Implementation status:** PARTIALLY ADJUDICATED (2026-08-26): verdict confirmed at the bounded-search level (`E6_NOVELTY_AUDIT_EXECUTION.md` row 1.1 — known-and-weaker; the exact-tube-at-finite-review-depth discipline is the delta); the typed false-positive theorem the answer asked for is proved (R01); Paper 1's journal decision remains gated on the full-text novelty pass at paper-drafting time.

## Workflow diagnosis

No scientific computation or workspace process was interrupting execution. Prior turns were stopped before completion when subsequent messages arrived, and intermediate status checkpoints made the work appear repeatedly paused. The corrected protocol is recorded in `workflow_continuity_correction.md`.
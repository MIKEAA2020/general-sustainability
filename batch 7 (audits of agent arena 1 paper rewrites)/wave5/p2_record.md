# Wave-5 P2 record — paper2_obstruction_calculus_v10.md (from v9)

**Task ID:** 75-b. **Directive:** owner gate opened — re-evaluate the registered
follow-ups; re-open what is now worth doing.

## The re-opened items (all three were "awaiting the next registered wave" in the v9 record's decline section)

| Item | Endorsement | Disposition | v10 evidence |
|---|---|---|---|
| §1.2 "Each theorem exhibits the violating constraint, the admissible disturbance, and the quantitative bound…" false for Theorems 2 and 5 (and Theorem 3's exhibit is the incompatible controls, not a disturbance/bound pair) | claude §1.2 | **IMPLEMENTED** (scoped by mechanism) | L48: "Theorems 1 and 4 each exhibit the violating constraint, an admissible disturbance, and the quantitative bound…; Theorems 2 and 3 exhibit the incompatible admissible controls — the merged observation whose incompatible safe controls certify emptiness — with no quantitative bound claimed there; and Theorem 5 is the converse-side characterization of the certification limit itself, not a failure exhibit." |
| §6.4 Timing: "the least-constrained compatible state" reads backwards (the inf-q state has least constraint slack) | claude §6.4 | **IMPLEMENTED** (corrected with gloss) | L287: "the worst-case time from the most-constrained compatible state — the minimum-$q$ state, which has the least constraint slack — to constraint violation" |
| §6.4 Coarseness: "coarse indicators are admissible exactly when they are constant on the safe-control partition … and no finer" (finer never hurts; "exactly when" overstates Theorem 3) | claude §6.4 | **IMPLEMENTED** (exposure wording) | L289: "an indicator is exposed to Theorem 3's obstruction when some observation fibre crosses the safe-control partition…; keeping every fibre within a single class is what removes that exposure; finer observation never hurts (it merges nothing the coarser one did not), though Theorem 3 claims no benefit beyond the removal, and other mechanisms may still certify nonviability on a finer partition." |

## Build and verification

- `apply_batch7_wave5_p2.py` (fail-loud: three asserted-once sub1 anchors + the
  version-log splice). Ran clean twice: **MD5 6a629cf55ec462401df85f8bfebcee7f**
  both runs (379 lines, 12,154 words). v9 untouched (git status: only v10, the
  script, and this record added).
- Diff = exactly 4 hunks: L3 (version log), L48, L287, L289 — the three docket
  items and nothing else.
- Mechanical checks: "least-constrained", "and no finer", "Each theorem
  exhibits" all body-zero; Theorem 5's own true "exists exactly when"
  characterization (abstract + statement) untouched; all five theorem headers
  byte-identical; body counts of every frozen needle unchanged ((H1.1)/(H1.2)/
  (H3.1)/(H3.3)/(H4.1)/(H4.2)/(H4.3), EViab/ERViab/IRViab, ℐ/𝒥).

## Still behind the gate (reasons re-verified, still valid)

- **claude A8's singleton-belief sanity lemma** (ERViab = RViab for singleton
  beliefs under injective O) — new mathematics (a new lemma with proof); the
  audits' own theorem-inflation stance argues against adding theorems; needs
  owner-adjudicated proof review, not an edit wave.
- **grok's restructure items** (tube-form Theorem-3 statement, Theorem-2 plant
  replacement, Theorem-5 demotion, §4.2 stub, §5(d)/Appendix-A relocation) —
  statement-scale churn on theorems whose repairs wave-4 just adjudicated.
- **claude's remaining structural asks** (Marchaud pass, chattering remark,
  §5(c) observer citation — a literature item that cannot be invented,
  Theorem-2 domain extension) — unchanged grounds.

## Non-destructiveness

No theorem statement, hypothesis, proof step, display, or number changed; the
three edits are presentation-layer wording fixes on §1.2 and §6.4 prose.

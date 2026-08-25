# TCS-1.1 — The Frozen Schema Diff

## ⚠ Controlling-schema status (mandatory — read before any formalisation or compatibility claim)

1. **TCS-1.0 is the controlling schema.** Every record, packet theorem, batch-2 result, session theorem, and artifact in this programme is a **TCS-1.0** object. The canonical reference is `research_program/general_theory_math_closure_packet/control/01_canonical_system_schema_TCS_1_0.md` (whose §10 states: TCS-1.0 is frozen; changes create TCS-1.1 and require concordance migration entries).
2. **TCS-1.1 is a frozen DIFF, not an operative schema.** What is frozen is the *content of the change* below. **Zero records conform to TCS-1.1.** The migration has **not** been executed: no concordance migration entries exist.
3. **Consequence for claims.** No theorem, record, or artifact may be cited as "TCS-1.1-compatible" or "valid under TCS-1.1". All formalisation claims are scoped to **TCS-1.0** — in particular: E1's language completeness is relative to the **TCS-1.0 §4** judgment inventory; C-a's decidability is decidability of the **TCS-1.0** judgment language; the composition gates below are an *enumeration inside the diff*, not a property of any existing record. (The master review's earlier "valid under both TCS-1.0/1.1" claim was withdrawn in the Wave-4 repairs; nothing has reintroduced it.)
4. **Migration is an open Wave-0 obligation.** Executing the migration (rewriting every record with the five new types and seven mandatory fields, adding concordance entries, re-validating the 17-field discipline against the new required fields) is a prerequisite for *any* TCS-1.1-scoped claim. It is deliberately **not** done in the current repair wave (scope decision recorded in TRANSFER_AUDIT_RESPONSE.md, Finding 3).

### Migration checklist (open obligation)

- [ ] Add the five types (T-1…T-5) to the type registry; version the registry.
- [ ] Add the seven mandatory fields (F-1…F-7) to every record; backfill the existing records.
- [ ] Insert the registry layering rule R-1 into the constraint-generation semantics.
- [ ] Re-validate every record against the enumerated composition gate G-1…G-5.
- [ ] Add concordance migration entries per TCS-1.0 §10.
- [ ] Re-run the master review's verdict table against the migrated records.
- [ ] Only then: TCS-1.1 becomes controlling for *new* records (TCS-1.0 records remain citable at their own scope).

---

## The diff (frozen content)

### New types

- **T-1: `specification_path`** (GAP-1) — the provenance path from a normative specification to the constraint cell; mandatory on every constraint-declaring record.
- **T-2: `confinement_certificate`** (GAP-2) — non-`none` **mandatory for infinite-horizon claims** (the E5 discipline generalized: no infinite-horizon claim without an exhibited positively-invariant enclosure).
- **T-3: `erosion_triple`** (GAP-3) — the `(L, r, Δ)` bookkeeping as a first-class typed object.
- **T-4: `observation_map` tagged union** (GAP-4) — exact / quantized / mode-indicator / belief, with the A3 clopen-fibre class as one tag.
- **T-5: `h_translation` enum** (GAP-5) — accumulate / cap / forgive (E4.Thm3's declared semantics).

### Mandatory per-record fields

- **F-1: `solution_concept`** — named from the frozen list (Carathéodory ODE, RFDE, hybrid event, set-valued...).
- **F-2: `chance_support`** — the declared probability structure when family 6 is invoked.
- **F-3: `implementation_branch_quantifier`** — how the implementation map's branches are quantified.
- **F-4: `recoverability_quantifier`** — the reach-avoid-maintain quantifier chain for family 7.
- **F-5: `judgment_tag`** — `RViab_T / Inf / Inv / StrongInv / …` per the frozen tag list.
- **F-6: `information_pattern`** — the canonical frozen pattern (review-time, sampled, hybrid event, belief).
- **F-7: `strategic implementation declaration`** — the B10 docket's declaration field.

### Registry layering

- **R-1:** `𝕂 = 𝕂^phys ∩ π^{-1}(𝕂^epi)` — the physical/epistemic layering of the constraint registry.

### Composition gate (enumerated in the diff)

- **G-1:** corrected restricted proximal-normal (packet).
- **G-2:** tubular assume–guarantee (R05, convexified).
- **G-3:** eroded generation-transfer (E4).
- **G-4:** nonlinear monotone-operator (A4).
- **G-5:** chance-kernel recursion (B9).
- Everything else: **UNRESOLVED** (not admitted through the gate).

### Status vocabulary (frozen)

`proved here / exact instantiation / conditional corollary / conjectural bridge / counterexample only`.

---

## Status

**FROZEN (diff only). NOT CONTROLLING. TCS-1.0 controls. Migration open.** — The freeze card records *what TCS-1.1 will be*; it confers no compatibility on any existing object (see the controlling-schema header above, which is part of this card's normative content).

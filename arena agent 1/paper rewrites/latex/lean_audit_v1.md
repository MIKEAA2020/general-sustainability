# Lean audit — `general-sustainability` formalization layer (v1)

Date: 2026-09-27. Target: `general-sustainability` → `lean/` (10 modules),
against the **latest** paper editions.

## 1. Latest editions — confirmed two ways

Derived independently from the git tree (max version per family) and
cross-checked against `supersession_map_v11.md` → "Current editions (after
round 30)". They agree exactly. **6 of the 9 versions in your list were
already superseded**:

| Slot | You listed | Latest | Module |
|---|---|---|---|
| obstr (P1, board) | v55 | v55 ✓ | `P1_Obstruction` |
| obstr supp | v51 | v51 ✓ | — |
| comp | v17 | **v18** ✗ | `Comp_Certification` |
| ws | v17 | v17 ✓ | `WS_WorkedSystems` |
| minimax | v9 | **v11** ✗ | `Minimax_Dual` |
| ebc | v8 | **v10** ✗ | `EBC_ExactBelief` |
| psuff (P3) | v10 | **v11** ✗ | `P3_ProbSufficiency` |
| ARV | v8 | **v9** ✗ | `ARV_RegimeViability` |
| E1 | v58 | **v59** ✗ | `E1_ForecastLadder` |
| P1-AS (head) | — | `paper1_assessment_separation_v62` | `P1_AssessmentSeparation` |

## 2. Build matrix — both green

The layer has **no Mathlib** (empty `lake-manifest.json`, `Prelude` imports
nothing), so builds are seconds, not minutes.

| Toolchain | Result | Time |
|---|---|---|
| `v4.34.1` (**pinned**) | **rc=0**, 13 jobs | 14 s |
| `v4.35.0-rc3` (newest) | **rc=0**, 13 jobs | 15 s |

Zero `sorry`, zero `admit`, zero `axiom`. Only linter warnings (unused
variables at `P1_AssessmentSeparation:1983/2980/2990/3028`; unused simp args
in `EBC_ExactBelief:89–91`).

**Consequence:** there is no *compile* fault to find, and the kernel
guarantees no theorem is *unsound*. So the interesting defects are of a kind
`lake build` structurally cannot detect.

## 3. Suspect theorems (ranked)

Scanned 392 theorems/lemmas across 10 modules for: unused hypotheses,
trivial proofs, ex-falso statements, dangerous constants, and dead code.
23 flagged; most were regex false positives (primed names like `h2'`,
predicates used via hypotheses). **These are the real ones:**

### S1 — `lemB_reject` — `P1_AssessmentSeparation.lean:1983` — HIGH

```lean
/-- **Lemma B**(i): θ < 1 members' admissibility forces the positivity
rider — the collapse convention is the family's defining property. -/
theorem lemB_reject {_pw} {w1 w2} {a} {z} {rung : Prop}
    (h : CollapseSafe a z ∧ rung) : CollapseSafe a z := h.1
```

It is **`And.left`**. The parameter `rung : Prop` is a phantom — the theorem
holds for *every* proposition in that slot, so it can "force" nothing. The
linter independently flags `w1`, `w2` as unreferenced. **It is never
referenced anywhere in the layer.** The docstring claims content the
declaration does not have.

### S2 — `lemB_ii_only_linear` — `P1_AssessmentSeparation.lean:3561` — HIGH

```lean
/-- Every θ < 1 member rejects the collapsed plan of Lemma B(ii) ... -/
theorem lemB_ii_only_linear ... (h : ThetaSubAdm ... ∨ ThetaMidAdm ...)
    (hcs : ¬ CollapseSafe a z) : False := by
  cases h with | inl hsub => exact hcs hsub.1 | inr hmid => exact hcs hmid.1
```

True **by definition, not by proof**: `ThetaSubAdm` and `ThetaMidAdm` are
both defined as `CollapseSafe a z ∧ <rung cond>`, so `.1` hands over
`CollapseSafe` immediately. The proof never inspects either rung condition —
delete them and the proof is unchanged. Never referenced.

### S3 — redundant-hypothesis cluster — LOW (benign, but fidelity noise)

Proofs that never use a stated hypothesis, i.e. the theorems are strictly
stronger than stated:

- `half_pow_scaled:2702` — `hm : 1 ≤ m` unused (bound also holds at `m = 0`)
- `negm_master_bound:2773` — `hm : 1 ≤ m` unused
- `pw_sq_ge:2979`, `pw_cube_ge:3026` — `hq : 0 ≤ q` unused
- `pw_sq_le:2990` — `hnn` unused

Not errors. Worth tightening only if you want statements to be minimal.

## 4. What is *not* wrong — the honest contrast

- **`lemB_ii_linear_witness` (`:3521`)** is the genuine Lemma B(ii): it
  constructs `z₀ = (1/2, 1/2, 5/2)`, proves the coordinate collapse
  `1 + (1/2 − 2) ≤ 0`, proves the θ = 1 member still certifies at the equal
  weight, and derives `¬ CollapseSafe` from an explicit tube dip. Real work.
- **`s2_two_sided_summary` (`:3574`)** — headline Theorem S2 — is properly
  assembled from `s2_i_linear_accepts`, `s2_leontief_rejects_gaps`,
  `s2_ii_negm_interval`. Not vacuous.
- 115 of 482 declarations are unreferenced, but the overwhelming majority are
  **endpoint theorems** (`finite_horizon_sound`, `certified_sandwich`,
  `ladder_telescope`, `dual_certificate_sound`, …) — expected, not a defect.
  S1/S2 are different: they are named as *steps* yet have no consumer.

## 5. Verified playground snippets

`playground_checks_v1.lean` (this workspace) — compiles clean on **both**
`v4.34.1` and `v4.35.0-rc3`; paste any section into
https://live.lean-lang.org/. It reproduces S1 and S2 in miniature and
contrasts them with an honest witness.

## 6. Revisions — proposed, **not yet applied**

Nothing has been overwritten. The layer is untouched; all work was done on a
scratch clone under `/var/tmp/lean`.

- **A (minimal, safest):** delete S1 and S2 — both are unused, so removal
  cannot break the build — and point the Lemma B section at
  `lemB_ii_linear_witness`.
- **B (faithful):** keep them, replace the over-claiming docstrings with a
  note that the collapse convention is a definitional conjunct.
- **C (strengthen):** make S2's rung conditions actually do work. This is a
  *modelling* change (the rung conditions do not currently imply
  `CollapseSafe`), not a repair — needs your call.

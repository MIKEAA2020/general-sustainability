# Lean audit v29 — the value side of `thm:support` consequence 1

**Object:** `thm:support` consequence 1 — "for the unrestricted sequential
class, `V_k(b) = 1` iff `supp(b) ∈ 𝒲_k`" — on the class `def:value` names.

**Context.** v28 read the text and concluded that consequence 1 is about
`Π_seq` ("the class of all sequential policies"), i.e. the **feedback**
recursion `Wmem`, and that this is *not* the same as the blind recursion
`Wblind` that the existing value operator `VR` implements (proved by a
deterministic-kernel counterexample). v28 closed the *set* side
(`Wmem_iff_feedback`) and left the *value* side open: `VR` is a maximum
over action **tuples**, and `List Y → A` is infinite with no finiteness
hypothesis on `Y`, so `lmax` cannot be applied to the policy class
directly.

This version closes it.

---

## 1. The obstruction, and the way around it

The naive route — define the feedback value as `lmax` over the list of all
policies — is blocked: the policy class `List Y → A` is infinite and `Y`
carries no enumeration. The root cause is not the finiteness of `Y`; it is
that maximizing over *policies* is the wrong level of description.

The paper already gives the right level. `prop:antichain` (i):

> `V_k(b) = max_{S ∈ 𝒮_k} b(S)`, where `𝒮_k` is the family of subsets of
> the support **jointly survivable by one admissible class-element**
> (sequence **or policy**).

Under deterministic kernels, a branch's survival under a fixed policy is a
**deterministic** event, so the mass a policy saves is exactly `b(S_π)`
for `S_π = {x : x survives π}`. Maximizing over policies is therefore
maximizing over jointly-survivable sets — a finite family. Substituting
"`Wmem`-viable" for "`Survivable`" turns `Sfam`/`Vfam` (the blind family
value, `P3_Freeze_Noisy`) into the feedback family value. Nothing else
changes, and the construction mirrors the existing one line for line.

So `VFb` is **not** an ad hoc stand-in: it is `prop:antichain` (i) read
for the class consequence 1 names, and `prop:antichain` (i) is the paper's
own route from sets to values.

## 2. What was built

`lean/Formalizations/P3_FeedbackValue.lean` (new module, 33rd import):

| declaration | content |
|---|---|
| `suppPred`, `suppList` | `supp(b) = {x ∈ univX : b(x) ≠ 0}`, as predicate and as list |
| `Wmem_empty`, `Wmem_downward` | structural facts about the feedback family |
| `survPol_mono`, `Wmem_succ`, `Wmem_mono` | horizon nesting `𝒮_{k+1} ⊆ 𝒮_k` |
| `lsum_mem_subsetsOf_le` | a sublist of nonnegative terms sums to no more than the whole |
| `lsum_subset_add_le` | **the split lemma over subsets** — the form the deficit bound needs |
| `SfamFB`, `VFb` | the feedback family and its value |
| **`VFb_eq_total_iff_Wmem`** | **consequence 1** |
| `VFb_min_mass_bound` | consequence 2 (min-mass deficit bound) |
| `VFb_antitone` | consequence 3 (non-increasing in `k`) |
| `VFb_lt_total_of_not_Wmem` | consequence 1 `⟹`, proved **strictly** |

Supporting arithmetic/list lemmas the layer lacked:
`le_add_of_nonneg_right'`, `lt_add_of_pos_right` (proved by cancellation),
`lmax_lt` (a finite maximum of strict inequalities is strict — one line
from `lmax_isMax`), `filter_mem_subsetsOf`, `lsum_filter_eq_of_zero`.

The three consequences, verbatim:

```
VFb_eq_total_iff_Wmem (M) (k) (b) :
    VFb M k b = totalD M b ↔ Wmem M k (suppPred M b)

VFb_min_mass_bound (M) (k) (b) (mn)
    (hmn : ∀ x ∈ univX, b.f x ≠ 0 → mn ≤ b.f x)
    (hlost : ¬ Wmem M k (suppPred M b)) :
    mn ≤ totalD M b - VFb M k b

VFb_antitone (M) (hkn : k ≤ n) (b) : VFb M n b ≤ VFb M k b
```

Under the normalization `totalD M b = 1` the first is exactly the paper's
`V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k`.

### Two remarks on the proofs

* **The forward direction is strict, and needs no uniform lower bound.**
  If `supp(b) ∉ 𝒲_k` then every set in the family misses a branch of
  *strictly positive* mass (using `Mass.nonneg` plus `b(x) ≠ 0`), so each
  `b(S)` is strictly below the total; a maximum of finitely many strict
  inequalities is strict. Earlier deficit bounds in this layer
  (`min_mass_bound`) are inequalities of the form `mn ≤ 1 − V`, which
  cannot by themselves separate `V = 1` from `V < 1`.
* **Admissibility is enforced.** `SfamFB` requires `Wmem`, and `Wmem`
  requires every action to lie in `univA` at every history. The new family
  therefore does **not** inherit the admissibility gap noted in §4.

## 3. Scope: robust vs stochastic, and why it does not bite here

`DetMDP` reads the disturbance adversarially (`survK` quantifies over all
`d ∈ univD x a`), so `VFb` is the **robust** feedback value. `def:value`'s
`V` is a probability under a policy. They differ in general —
`rem:operators` says so.

They coincide on the models `thm:support` is stated for. With
**deterministic kernels** (`|univD x a| = 1`, the paper's hypothesis, and
`DetKernel` in `P3_Feedback.lean`) the disturbance path is unique, so
"survives under every disturbance" and "survives" are the same event, and
the only randomness left is the prior `b`. `VFb` is then exactly
`max_π P_π(survival | b)`. So consequence 1 is closed on the model class
the paper states it for, with no operator gap.

Off that class (nondeterministic kernels, as in `prop:degen`'s robust
reading) `VFb` remains the robust value, and the paper's expectation value
is a different operator — as it should be.

## 4. A fidelity defect found on the way, and left unfixed

`Survivable` (`P3_Freeze_Noisy:151`) is

```
Survivable M S k := ∃ u : Nat → A, ∀ x, x ∈ S → survK M k u x
```

— **no admissibility constraint on `u`**. `prop:antichain` defines `𝒮_k`
as the subsets "jointly survivable by one **admissible** class-element",
and `DetMDP` carries the admissible action set `univA`. So `Sfam` (hence
`Vfam`, hence `prop:antichain` (i) and `prop:freeze` as formalized in v18)
ranges over a family that can be **larger** than the paper's: an
inadmissible action sequence can witness survivability whenever one
exists that helps. `Vfam` may therefore overstate the paper's value.

This is reported rather than patched, because:

* the structural theorems that use it (`Vfam_antitone`,
  `Vfam_finite_range`, `Sfam0_card_le`) are monotone in the family and
  survive unchanged; only the *identification* with the paper's `𝒮_k` is
  affected;
* fixing it means either editing `P3_Freeze_Noisy` (against the
  never-overwrite rule) or a new module re-deriving `Sfam`/`Vfam` for the
  admissible family. The containment is the trivial direction
  (`SurvivableAdm ⊆ Survivable`), and the new feedback family `SfamFB` is
  already admissible, so no result in this version depends on the defect.

Recommended next step: a `P3_Freeze_Noisy_v3` carrying
`SurvivableAdm`/`SfamAdm`/`VfamAdm`, with `VfamAdm ≤ Vfam` by
`lmax_le_lmax_of_subset`.

## 5. State of `thm:support`

| consequence | blind class (`Π_B`, `prop:degen`) | feedback class (`Π_seq`, consequence 1) |
|---|---|---|
| identity `supp(b⁺) = Post(supp b, a, y)` | `support_identity` (v25, on `SafeMDP`) | same |
| 1: `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k` | `VR_eq_total_of_jointly_surviving` (v12) + `Wblind_iff_survK` (v27), composition still un-composed | **`VFb_eq_total_iff_Wmem` (v29)** |
| 2: min-mass bound | `min_mass_bound` (v12) | **`VFb_min_mass_bound` (v29)** |
| 3: monotone in `k` | `Vfam_antitone` (v18) | **`VFb_antitone` (v29)** |

Coverage totals for P3 are unchanged: 11 complete, 0 partial, 6 instance,
1 out of reach.

## 6. Open items (none blocking)

1. **Blind composition** (v27 item 1): `Wblind_iff_survK` +
   `survT_iff_survK` + `VR_eq_total_of_jointly_surviving`. Mechanical
   (~80 lines: a membership characterisation of `tuples M k` and a
   tuple↔schedule conversion). Now low priority: it would formalize
   `prop:degen`'s class, and `prop:degen` is already closed.
2. **`Survivable` admissibility** (§4) — a new module for the blind
   family.
3. **`lean_README_v6.md`** — v5 predates v27/v28/v29 (three new modules,
   the `Wmem`/`Wblind` resolution, and the consequence-1 closure).
4. `prop:pl` rationality clause (needs `K := ℚ`); Sperner count in
   `prop:antichain` (iii).

## 7. Record

* `lake build` → **rc 0, 36 jobs, 0 warnings, 0 `sorry`**; verified from a
  **fresh clone** of `lean-audit-v4` (33 imports; `P3_Viable.lean` md5
  `ea88fe02…`, i.e. unchanged since v27).
* Axioms of the new theorems: `propext`, `Classical.choice`, `Quot.sound`
  only — the standard classical trio (`Quot.sound` enters through
  `funext`; `Classical.choice` through `lmax` and, in `Wmem_succ`,
  through `Wmem_iff_feedback`'s per-observation choice of policy). No
  custom axioms.
* Branch: `888319e` (v27) → `5cf05d9` → `ec5acc6` (v28b, corrective) →
  **`cef0007` (v29)**.

# Lean audit v21 — the pushed tree never built, and `prop:antichain` (ii) is closed

**Scope.** `general-sustainability` → `lean/`, branch `lean-audit-v4`, toolchain
`v4.34.1`, `lake build` gold standard.
**Result: rc = 0, 28 jobs, 0 warnings, 0 `sorry`.**

This turn produced two things, and the first is more important than the second.

---

## 1. A defect in my own prior reporting: the pushed tree never built

Every build result I reported from v8 through v20 was measured against
`/var/tmp/lean/gs/lean` — my **local** working tree. The repository only ever
received the individual module files as blobs. It never received the updated
`Formalizations.lean`, so **the aggregate import list in the repo was still the
original v1-era one.**

Consequence, verifiable from a clean clone:

| | pushed repo (before this turn) | my reported figures |
|---|---|---|
| jobs | **13** | 27 |
| warnings | **9** | 0 |
| modules compiled | 11 | 24 |

Specifically the repo's `Formalizations.lean`

- did **not** import `P3_ClassLattice`, `P3_Sufficiency`, `P3_Deterministic`,
  `P3_Freeze_Noisy`, `P3_Freeze_Noisy_v2`, `P3_Convexity`, `P3_Antichain`,
  `P1_TimingCertificate`, `P1_BeliefSafety`, `P1_BeliefSafety_Value`,
  `P1_BeliefSafety_Policy`, `ARV_RegimeViability_v2`, `Comp_Certification_v2`,
  `EBC_ExactBelief_v2`, `WS_WorkedSystems_v2`, `P1_AssessmentSeparation_v5` —
  i.e. **every module added from v7 onward was present but orphaned**; and
- still imported the superseded `EBC_ExactBelief` (4 warnings) and
  `P1_AssessmentSeparation` (5 warnings), which is where the 9 warnings came from.

So the modules were on the branch but were **never compiled by `lake build`**.
My "rc = 0, 0 warnings" claims were true of the tree I was editing and false of
the tree I shipped. That distinction matters and I should have checked it
earlier: a green build of an unwired module is not evidence of anything.

**Fix.** Reconstructed the full 24-module import list and pushed it as
`lean/Formalizations.lean` (commit `e555b04`). A clean clone now reproduces
`rc = 0, 27 jobs, 0 warnings` at that point, and `rc = 0, 28 jobs, 0 warnings`
with v21 added. The reconstruction is exact — it reproduces the job count I
had been reporting, which is the evidence that the module set matches.

**Standing correction to my own process:** after any push that adds a module,
push the import list too, and re-verify from a *fresh clone*, not from the
working tree.

---

## 2. v21 — `Formalizations/P3_Antichain_v2.lean` closes `prop:antichain` (ii)

`prop:antichain` (v11 of the paper) reads, in relevant part:

> (ii) the alpha-vectors are exactly the indicators of the maximal elements
>      of `S_k` in the componentwise order;

v20 supplied the order vocabulary (`subsetOf`, `MaximalIn`, `Antichain`) and
proved (iii), but left (ii) open, naming the blocker: *every `S ∈ S_k` must sit
below a maximal `T ∈ S_k`*, plus an `lsum` rearrangement to turn
"maximal by inclusion" into "the value is attained there". Both are supplied
here, so (ii) is now **complete**.

### 2.1 What the probe found

v20 guessed the needed list lemmas; that guess was wrong in both directions.

**Present:** `List.erase`, `List.length_erase_of_mem`, `List.erase_cons_head`,
`List.erase_cons_tail`, `List.Nodup.erase`, `List.Perm`, `List.Sublist`.
Note these require `[BEq α] [LawfulBEq α]`, **not** `[DecidableEq α]`; both
instances derive from `DecidableEq`, so `[DecidableEq X]` is sufficient.

**Absent:** `List.mem_erase`, `List.dedup`, `List.nodup_dedup`, `List.mem_dedup`,
`List.Subperm`, `List.perm_ext`, `List.length_le_of_sublist`, `List.count_pos`,
`List.Nodup.filter`, `List.mem_of_mem_filter`.

Consequence: the **permutation** route to "same elements ⟹ same `lsum`" is
unavailable (`Subperm` and `perm_ext` are both missing), and the **`erase`**
route requires proving `mem_erase` by hand. The module proves it as
`mem_erase_iff`, and that is the concrete price of the thin stdlib.

### 2.2 Theorems

Order-theoretic and list infrastructure:

| theorem | statement |
|---|---|
| `mem_erase_iff` | `l.Nodup → (x ∈ l.erase a ↔ x ∈ l ∧ x ≠ a)` |
| `lsum_erase_mem` | `l.Nodup → a ∈ l → lsum (l.map f) = f a + lsum ((l.erase a).map f)` |
| **`lsum_eq_of_mem_iff`** | two `Nodup` lists with the same elements have the same `lsum` |
| `mem_filter_mem` | `x ∈ l.filter p → x ∈ l` |
| `nodup_filter` | `l.Nodup → (l.filter p).Nodup` |
| `subsetsOf_subset` | every member of `subsetsOf l` is a sublist of `l` |
| `subsetsOf_nodup` | every member of `subsetsOf l` is `Nodup` if `l` is |
| **`bS_mono_of_subset`** | `S ⊆ T ⟹ b(S) ≤ b(T)` — the domination engine |
| **`lift_maximal`** | lifts a maximal element from `rest` to `A :: rest` |
| **`exists_maximal_above`** | every element of a finite family sits below a maximal one |

and the result itself:

| theorem | statement |
|---|---|
| `Pruned` | the witness family filtered to its maximal elements |
| `Pruned_ne` | the pruned family is inhabited |
| `Vfam_prune_ge` | (ii) ⊆ — a non-maximal witness never raises the maximum |
| `Vfam_prune_le` | (ii) ⊇ — every witness is dominated by a maximal one |
| **`Vfam_prune_eq`** | **`V_k(b) = max over the maximal survivable sets`** |

### 2.3 On `exists_maximal_above`

v20 floated a termination argument or a `Nat`-maximum over supersets. Neither
is needed. The proof is a plain induction on the family: for the head `A`, ask
whether anything in `rest` contains `A` — if so, recurse into `rest` and lift
the result via `lift_maximal`; if not, `A` is already maximal. The lifting step
is a two-way case split on whether `A` dominates `T`. No well-founded
recursion, no numeric measure.

The result is genuinely **non-constructive** at one point: the
"does anything in `rest` contain `A`" test is a `by_cases` on an existential
over a `Prop` with quantifiers. That is reflected honestly in the axiom
profile below. It could be made constructive, but the family is finite, so
nothing is lost — and I would rather ship the classical proof than a
constructive one I have not checked.

### 2.4 Axioms (`#print axioms`)

```
lsum_eq_of_mem_iff   [propext]
bS_mono_of_subset    [propext]
exists_maximal_above [propext, Classical.choice, Quot.sound]
Vfam_prune_eq        [propext, Classical.choice, Quot.sound]
```

No `sorry`, no `admit`, no axiomatized structure. `Classical.choice` enters
through the `by_cases` on `∃ U, U ∈ rest ∧ subsetOf A U` described above.
`Quot.sound` comes with the classical prelude in this configuration.

### 2.5 What is *still* not claimed for `prop:antichain`

- **(iii) Sperner bound.** v20 proved the maximal elements form an antichain.
  The counting bound `≤ C(n, ⌊n/2⌋)` is **not** proved and is not implied by
  the antichain statement — it is a separate combinatorial theorem.
- **(iv)** is open; see §3.
- The delayed-instance census at the end of the proposition (the three-type
  classification) is a computed artifact of the verification script, not a
  formalized claim.

---

## 3. Next: `prop:antichain` (iv)

> (iv) the deficit is `1 - V_k(b) = min b(S^c)`, the minimum over the maximal
>      survivable sets, and the min-mass bound is the special case `|S^c| = 1`.

The paper's one-line proof — "`1 - max_S b(S) = min_S b(S^c)`" — is correct but
conceals two hypotheses worth stating, and I will state them rather than
assume them:

1. **Normalization.** `1 - b(S) = b(S^c)` requires `b(S) + b(S^c) = 1`, which
   requires `lsum (univX.map b.f) = 1`. The `Mass` structure carries `nonneg`
   but **no normalization field**, and the existing `total` is defined against
   `SafeMDP`, not the P3 `DetMDP`. So this must enter as an explicit
   hypothesis. This is not a defect in the paper — every belief in the paper is
   a probability distribution — but it is an assumption the code must name.

2. **Why the min may be taken over maximal sets only.** This is *not* the same
   move as the max. `S ⊆ T` gives `b(T^c) ≤ b(S^c)`, so the minimum of `b(S^c)`
   is attained at the **largest** sets — which is why (ii) is what licenses
   restricting to the maximal family. So (iv) is a genuine corollary of (ii),
   and it is pleasant that the dependency runs that way.

Missing infrastructure, confirmed by probe: **`lmin` does not exist** in this
layer (only `lmax`), so `lmin`, `lmin_le`, `le_lmin` and the max/min duality
`1 - lmax (l.map f) = lmin (l.map (fun x => 1 - f x))` all have to be built,
along with `complOf`.

---

## 4. Status

### `prop:antichain`, per clause

| clause | content | status |
|---|---|---|
| (i) | `V_k(b) = max_{S ∈ S_k} b(S)` | complete (v1) |
| (ii) | alpha-vectors = indicators of maximal elements | **complete (v21)** |
| (iii) | maximal elements form an antichain | complete (v20); Sperner count not claimed |
| (iv) | `1 - V_k(b) = min over maximal S of b(S^c)` | **open** |

### Work order

1. ~~probe `List.erase`/`Subperm`/`Perm`, prove `lsum_eq_of_mem_iff`~~ — **done**
2. ~~prove `exists_maximal_above`, reinstate `Vfam_prune_le`/`_ge`, close (ii)~~ — **done**
3. `prop:antichain` (iv) — next
4. `prop:pl`, explicit half (witness set `Γ_k`, masked-backup identity, growth law)
5. `thm:support` — needs a disturbance-weighting modelling decision

### P3 coverage (18 results)

complete 9 · partial 2 · instance 6 · out of reach 1 (`prop:probecount`).
Formalizable backlog: empty.

---

## 5. Commits

| commit | content |
|---|---|
| `476e79a9` | v20 — `P3_Antichain` (iii) |
| `e555b04` | **wire the v7–v20 modules into the build** (`Formalizations.lean`) |
| *this turn* | v21 — `P3_Antichain_v2` (`prop:antichain` (ii)) |

Branch: <https://github.com/MIKEAA2020/general-sustainability/tree/lean-audit-v4>

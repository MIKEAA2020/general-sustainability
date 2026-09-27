# Lean audit v22 — `prop:antichain` (iv) is closed

**Result: `lake build` rc = 0, 29 jobs, 0 warnings, 0 `sorry`.**
File: `lean/Formalizations/P3_Antichain_v3.lean` (8.9 KB).

With this, **`prop:antichain` is closed in all four clauses** — modulo the
Sperner count in (iii), which is a separate theorem and is still not claimed.

---

## The statement

> (iv) the deficit is `1 - V_k(b) = min b(S^c)`, the minimum over the maximal
>      survivable sets, and the min-mass bound is the special case `|S^c| = 1`.

The paper's proof is a single line: "`1 - max_S b(S) = min_S b(S^c)`". That is
**correct**, but it hides two things the code has to make explicit. Stating
them honestly is most of the value of this audit entry.

### 1. Normalization is an assumption, not a fact

`1 - b(S) = b(S^c)` requires `b(S) + b(S^c) = 1`, i.e.
`lsum (univX.map b.f) = 1`. But:

- the `Mass` structure carries `nonneg` and **no normalization field**; and
- the existing `total` is defined against `SafeMDP`, not the P3 `DetMDP`.

So normalization enters as an explicit hypothesis `hnorm`. This is **not** a
defect in the paper — every belief there is a probability distribution — but
the code must name the assumption rather than silently inherit it. I did not
add a normalization field to `Mass`, because that would change a structure
every other module depends on, for the benefit of one clause.

### 2. The *minimum* over maximal sets is a different move from the maximum

`S ⊆ T` implies `b(T^c) ≤ b(S^c)` — complements reverse inclusion — so the
minimum of `b(S^c)` sits at the **largest** sets. Restricting the minimum to
the maximal family is therefore licensed by **`prop:antichain` (ii)**: every
`S` lies below a maximal `T`.

So **(iv) is a genuine corollary of (ii)**, and the dependency is visible in
the code: `deficit_eq_min_compl` rewrites by `Vfam_prune_eq` from
`P3_Antichain_v2` in its first step. The two clauses are not independent
one-liners; the paper's proof sketch does not say this, and it is worth
saying.

### 3. `S^c` is relative to the support

`complOf M S` is `M.univX.filter (· ∉ S)` — the complement **against
`univX`**, not against an ambient type. `X` is a `Type`, not a `Fintype`, so
there is no type-level complement to take. This matters for the min-mass
special case: `|S^c| = 1` means *one support state outside `S`*, which is
exactly what the paper means.

---

## Infrastructure notes

**`lmin` already existed — my v21 note said otherwise.** `P3_ClassLattice`
defines `lmin l := -lmax (l.map (fun x => -x))` together with `lmin_le`,
`le_lmin` and `lmin_mem` (lines 111–137). The v21 probe reported `lmin` as
absent because it ran with only `Formalizations` and `Formalizations.POMDP`
opened; these names live in `Formalizations.P3`. v3 imports them rather than
rebuilding them. **Corrected**: what was genuinely missing was only the
max/min duality, now `lmax_sub_dual`.

**`lsum_filter_split` is the right tool.** `Prelude:502` gives
`lsum ((l.filter A).map mass) + lsum ((l.filter (fun a => !A a)).map mass)
= lsum (l.map mass)` with **no `Nodup` hypothesis**. Using it avoids having to
prove `nodup_append` for `S ++ S^c` (which would have needed disjointness).
`Nodup` is only required at one step — identifying `univX.filter (· ∈ S)` with
`S` itself — and `lsum_eq_of_mem_iff` from v2 discharges that.

**A type-inference trap worth recording.** `lmax_sub_dual` was first written
as `theorem lmax_sub_dual {l : List K} (h) (f : K → K)`. Because `K` is a
section variable bound to the *field*, Lean instantiated the list's element
type to the field, and the error surfaced as `expected Mass (List X) X` —
pointing at the call site, not the declaration. The fix is a fresh type
parameter: `{β : Type} {l : List β} (h) (f : β → K)`.

---

## Theorems

| theorem | statement |
|---|---|
| `lmax_sub_dual` | `1 - lmax (l.map f) = lmin (l.map (fun x => 1 - f x))`, `l ≠ []` |
| `sub_eq_of_add_eq` | `a + c = o ⟹ o - a = c` |
| `pIn` | `S`'s indicator as a `Bool` predicate (lists filter on `Bool`, not `Prop`) |
| `complOf` | `S^c` relative to `M.univX` |
| `complOf_nodup` | complements of `Nodup` supports are `Nodup` |
| **`bS_compl`** | `b(S) + b(S^c) = 1`, under `hnorm` and `S ⊆ univX` |
| `deficit_point` | `1 - b(S) = b(S^c)` on the maximal family |
| **`deficit_eq_min_compl`** | **`1 - V_k(b) = min over maximal S of b(S^c)` — (iv)** |
| **`bS_compl_singleton`** | `b(S^c) = b(x)` when `x` is the only support state outside `S` — the min-mass case |

## Axioms (`#print axioms`)

```
lmax_sub_dual          [propext, Classical.choice, Quot.sound]
bS_compl               [propext]
deficit_eq_min_compl   [propext, Classical.choice, Quot.sound]
bS_compl_singleton     [propext]
```

`Classical.choice` enters via `lmax`/`lmin`, which are themselves
`Classical.choose`-based — not from anything new here. No `sorry`, no `admit`.

---

## `prop:antichain`, final status

| clause | status |
|---|---|
| (i) `V_k(b) = max_{S ∈ S_k} b(S)` | complete (v1) |
| (ii) alpha-vectors = indicators of maximal elements | complete (v21) |
| (iii) maximal elements form an antichain | complete (v20) |
| (iii) Sperner bound `≤ C(n, ⌊n/2⌋)` | **not claimed** — separate theorem, not implied by the antichain statement |
| (iv) `1 - V_k(b) = min over maximal S of b(S^c)` | **complete (v22)**, under explicit `hnorm` |
| (iv) min-mass case | complete, as `bS_compl_singleton` |
| delayed-instance census | computed artifact of the verification script; not a formalized claim |

## Work order

1. ~~probe `erase`/`Subperm`/`Perm`, prove `lsum_eq_of_mem_iff`~~ — done (v21)
2. ~~`exists_maximal_above`, `Vfam_prune_le`/`_ge`, close (ii)~~ — done (v21)
3. ~~`prop:antichain` (iv)~~ — **done (v22)**
4. `prop:pl`, explicit half — next: witness set `Γ_k`, masked-backup identity,
   growth law `|Γ_{k+1}| ≤ |A| · |Γ_k|^{|Y|}`
5. `thm:support` — needs a disturbance-weighting modelling decision

P3 coverage (18 results): complete 10 · partial 1 (`prop:pl`) · instance 6 ·
out of reach 1 (`prop:probecount`).

**Carried forward:** `lean_README_v4.md` is still stale on the rows for
`prop:freeze`, `prop:pl` and `prop:antichain`. It will be updated with the
next batch rather than as a standalone commit.

## Commits

| commit | content |
|---|---|
| `e555b04` | wire the v7–v20 modules into the build (`Formalizations.lean`) |
| `0dafd81` | v21 — `P3_Antichain_v2`, `prop:antichain` (ii) |
| *this turn* | v22 — `P3_Antichain_v3`, `prop:antichain` (iv) |

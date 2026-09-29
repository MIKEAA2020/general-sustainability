# Lean audit v26 — README refreshed, and a second misreading corrected

**Result: `lake build` rc = 0, 33 jobs, 0 warnings, 0 `sorry`.**

Two items this turn. The second is another correction of my own prior work,
of the same species as the v23→v24 one, and it is the more important of the
two.

---

## 1. `lean_README_v5.md` — the stale index is refreshed

`lean_README_v4.md` was stale on four rows and on the build count. v5 is a
new file (never-overwrite), pushed as `56d969d`.

| v4 said | v5 says |
|---|---|
| `prop:freeze` **partial** (drop count not proved) | **result** — `prop_freeze_drop_count` (v18) |
| `prop:pl` **partial** (convexity not closed) | **result** — v19, v23, v24 |
| `prop:antichain` **partial** (alpha-vector characterisation not proved) | **result** — v20, v21, v22 |
| `thm:support` **partial** (identity not proved) | **result** — v25 |
| build 24 jobs | 32 jobs |
| P3 module list: 5 modules | 12 modules |
| totals 7 result · 4 partial | **11 result · 0 partial** |

Three things v5 adds that v4 did not say:

- **The v21 orphaned-import defect is documented**, with the standing rule:
  a push that adds a module must also push `Formalizations.lean`, and the
  build must be re-verified from a **fresh clone**, never the working tree.
- **Each newly-closed result records what is still *not* claimed** — the
  Sperner count, `prop:pl`'s rationality clause, and the general stochastic
  masked backup. A coverage index that only lists successes is how v4 became
  misleading in the first place.
- **A correction to v5's own predecessor.** v25 reported the P3 totals as
  "12 complete · 0 partial · 6 instance · 1 out of reach", which sums to
  **19 against a table of 18 rows**. The correct figure is 11; I had counted
  `prop:deficit` (i)(ii)(iii) as three results in a table where it is one
  row. v5 says so explicitly rather than silently printing 11. A miscount in
  a coverage index is exactly the class of error the index exists to catch,
  so it gets flagged, not quietly fixed.

---

## 2. The "bridge" I proposed in v25 was a second misreading

v25 recommended as the next item: *"The `SafeMDP`/`DetMDP` bridge — would
discharge `thm:support` consequence 2."*

**Consequence 2 was already proved, and never needed a bridge.**

`min_mass_bound` (`P3_Deterministic:248`) states it, and its own header has
said so since v12:

> The min-mass bound — `prop:deficit` (ii) and **`thm:support`'s
> consequence**.

It is a statement about the **robust** operator `VR`, not about `SafeMDP`'s
stochastic `V` — and per `rem:operators` those are different operators that
do **not** coincide ("the degeneration is a theorem about the robust
operator; it is not a claim about the stochastic plant, whose expectation
and robust readings differ in general"). So the bridge I proposed would not
have been a hard theorem; it would have been **a false one**.

This is the same failure as v23: both times I read a statement about the
robust operator and reached for machinery belonging to the stochastic one.
v24 found the first; this turn found the second, while checking whether the
bridge was needed at all. Recorded as a pattern: **before proposing new
structure, re-read what the existing code already claims in its headers.**

### What `thm:support` genuinely still lacks

| consequence | status |
|---|---|
| 2. `1 - V_k(b) ≥ min_{x ∈ supp b} b(x)` | **already proved** — `min_mass_bound`. v25 was wrong. |
| 3. `V_k` non-increasing in `k` | covered by `Vfam_antitone` (`prop:freeze`, v18) |
| 1. `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k` | **the real gap** — the `𝒲_k` viable-set recursion is defined in **no** module |

So consequence 1 is the only genuinely open piece, and it is a definition
plus an equivalence, not a deep theorem.

---

## 3. What v26 actually adds: `P3_Bridge`

Root cause of a real (if quieter) problem: **P3 computed the same value
twice, in incompatible vocabularies, with nothing connecting them.**

- `P3_Freeze_Noisy` — `Survivable M S k := ∃ u : Nat → A, ∀ x ∈ S,
  survK M k u x`: **infinite schedules**, `Prop`-valued, feeding
  `Sfam`/`Vfam`. This is `prop:antichain` (i)'s `max_{S ∈ 𝒮_k} b(S)`.
- `P3_Deterministic` — `survT M t x`: **finite tuples** of length `k`,
  `Bool`-valued, feeding `VR`. This is `prop:degen`'s
  `max_{t ∈ Π_B} Σ_x b(x)·1[x survives t]`.

Two modules, two survival predicates, no lemma relating them. v26 supplies
the connection.

| theorem | statement |
|---|---|
| `survK_congr_prefix` | `survK M k u x` sees only `u 0 … u (k-1)` |
| **`survT_iff_survK`** | `survT M t x = true ↔ survK M t.length (fun i => t.getD i a0) x` |

The two definitions are structurally parallel — `survK` uses `∧` and
`∀ d, d ∈ …`, `survT` uses `&&` and `.all` — so the equivalence is an
induction on the tuple, once the schedule is read off the tuple by `getD`.
The fallback `a0` is arbitrary, and `survK_congr_prefix` is what makes that
harmless.

This is the lemma that explains *why* `prop:antichain` (i) and `prop:degen`
describe the same number. It does not yet discharge consequence 1 — that
still needs `Survivable` to be tied to `𝒲_k`, which is a definition — but it
is the load-bearing step.

### Axioms

```
survK_congr_prefix   (no axioms)
survT_iff_survK      [propext, Quot.sound]
```

`survK_congr_prefix` is **axiom-free**. No `sorry`, no `admit`.

---

## Status

P3: **11 result · 0 partial · 6 instance · 1 out of reach.** Build
**rc = 0, 33 jobs, 0 warnings, 0 `sorry`**. README is current as of v5.

Remaining, in the order I would take them:

1. **`𝒲_k`** — define the viable-set recursion and prove
   `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k`. This closes `thm:support` outright, and
   `survT_iff_survK` is now in place to support it.
2. `prop:pl` rationality — needs `K := ℚ`.
3. Sperner count in `prop:antichain` (iii) — separate combinatorial theorem.

## Commits

| commit | content |
|---|---|
| `489cc96` | v23 — `prop:pl` growth law |
| `6e82a52` | v24 — adversarial reading; `prop:pl` segment form |
| `a4217b3` | v25 — `thm:support` support identity |
| `56d969d` | `lean_README_v5` — refreshed index, P3 totals corrected to 11 |
| *this turn* | v26 — `P3_Bridge`: `survT_iff_survK`; v25's bridge proposal retracted |

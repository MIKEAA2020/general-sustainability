# Lean audit v27 — `𝒲_k` defined, and identified with `survK`

**Result: `lake build` rc = 0, 34 jobs, 0 warnings, 0 `sorry`.**
File: `lean/Formalizations/P3_Viable.lean`.

`𝒲_k` was the last missing piece of `thm:support`. It is now defined, and
proved equivalent to the layer's existing survival notion.

---

## What the paper says, and the two decisions it forced

> Write `supp(b)` for the states carrying positive mass, and let `𝒲_k`
> denote the calculus's viable-set recursion: `𝒲_0 = {B ⊆ 𝒱}` and
> `𝒲_k = {B : some admissible a maps every x ∈ B into 𝒲_{k-1}-supported
> posteriors}`.

and `thm:support`, consequence 1: *"for the unrestricted sequential class,
`V_k(b) = 1` if and only if `supp(b) ∈ 𝒲_k`."*

### Decision 1: safety is re-checked at every level

As literally written, the recursion does **not** require `B ⊆ 𝒱` for
`k ≥ 1`: `B ∈ 𝒲_1` asks only that the *successors* of `B` lie in `𝒱`. But the
paper needs `𝒲_{k+1} ⊆ 𝒲_k` (for `prop:freeze` and for `thm:support`'s
monotonicity consequence), and under the literal reading that **fails at the
base** — a set containing an unsafe state can have all-safe successors.

What rescues it in the paper is that `⊥` is absorbing ("absorption at `⊥` is
permanent"), so an unsafe state's successors are unsafe too. `DetMDP` carries
`safe : X → Bool` but **no absorbing-`⊥` axiom**, so that rescue is
unavailable here. `Wblind` therefore conjoins `B ⊆ 𝒱` at every level.

This is **not** an unsupported guess. `Wblind_iff_survK` proves the resulting
notion is *exactly* `survK`-viability — the predicate the layer has used since
v12, which `survK_mono_succ` shows is nested. So the definition is validated
against the property the paper needs, not merely asserted.

### Decision 2: two recursions, and an ambiguity I am not resolving by fiat

The paper's recursion quantifies over **posteriors**, i.e. over
observations: `∃a, ∀y, Post(B,a,y) ∈ 𝒲_{k-1}`. That is a **feedback**
recursion — a different continuation may be used per observation. That is
`Wmem` below, transcribed faithfully.

`Wblind` drops the split: one continuation for all successors. That is the
**open-loop / blind** recursion, which is what `DetMDP`'s `survT` and `VR`
actually implement, and `prop:degen` is explicitly stated for a blind window.

**Which one `thm:support` means by "the unrestricted sequential class" is not
determinable from the text with confidence.** "Sequential" suggests
open-loop; the `∀y` recursion is a feedback recursion. Rather than pick, both
are defined, `Wblind_le_Wmem` records the direction that holds
unconditionally, and the theorem is proved for `Wblind`. **This is a question
for the paper's author, not for me.** It is the one open judgement call in
this module and it is flagged in the source.

---

## What is proved

| theorem | statement |
|---|---|
| `succPred` | the blind successor-set operator |
| `Wblind` | the blind viable-set recursion `𝒲_k` |
| `postPred` | the observation-`y` slice (predicate form of `P3_Support.postMem`) |
| `Wmem` | the paper's `𝒲_k`, transcribed exactly (`∀y`, feedback) |
| `Wblind_downward` | `𝒲_k` is downward closed — **axiom-free** |
| `Wblind_le_Wmem` | blind viability ⟹ observation-split viability — **axiom-free** |
| **`Wblind_iff_survK`** | **`𝒲_k`-viability ⟺ `survK`-viability with an admissible schedule** |

```
Wblind_iff_survK (M) (k) (B) :
  Wblind M k B ↔ ∃ u, (∀ i, u i ∈ M.univA) ∧ ∀ x, B x → survK M k u x
```

The right-hand side is `Survivable` (`P3_Freeze_Noisy:151`) **plus**
admissibility of the schedule — `Survivable` itself ranges over arbitrary
`Nat → A` with no `univA` constraint, which is a small mismatch worth noting
between the two modules.

**What this discharges.** Consequence 1 of `thm:support` is
`V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k`. The pieces are now all present and already
proved separately:

- `Wblind_iff_survK` — `𝒲_k` ⟺ `survK`-viability (v27);
- `survT_iff_survK` — `survK` ⟺ `survT` (v26);
- `VR_eq_total_of_jointly_surviving` — `V_k(b) = 1` ⟺ a jointly-surviving
  tuple exists (v12).

They have not yet been *composed* into the single iff the paper prints; that
composition is mechanical but is not yet in the tree, and I am not claiming it
as done.

## Axioms

```
Wblind_downward     (no axioms)
Wblind_le_Wmem      (no axioms)
Wblind_iff_survK    [propext]
```

No `sorry`, no `admit`.

## A process note

Two faults cost time here, both worth recording:

- **`h.2.2` on an `Exists` proof is rejected by the kernel** with the opaque
  `(kernel) invalid projection h.1`, reported at the *theorem's name*, not at
  the offending line. Use `rintro ⟨…, …, …⟩`.
- **Predicates have no `∈`.** With `B : X → Prop`, write `B x`, not `x ∈ B`.

---

## Status

P3: **11 result · 0 partial · 6 instance · 1 out of reach.** Build
**rc = 0, 34 jobs, 0 warnings, 0 `sorry`**. README current as of v5.

`thm:support` is now closed as to its identity (v25) and its `𝒲_k` (v27).
Remaining:

1. **Compose the three lemmas** into the literal
   `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k` — mechanical, not yet in the tree.
2. **Resolve the `Wmem`/`Wblind` question** with the author — a paper-side
   judgement, not a code-side one.
3. `prop:pl` rationality — needs `K := ℚ`.
4. Sperner count in `prop:antichain` (iii) — separate combinatorial theorem.

## Commits

| commit | content |
|---|---|
| `6e82a52` | v24 — adversarial reading; `prop:pl` segment form |
| `a4217b3` | v25 — `thm:support` support identity |
| `56d969d` | `lean_README_v5` — refreshed index, totals corrected to 11 |
| `aac9d1b` | v26 — `P3_Bridge`: `survT_iff_survK` |
| *this turn* | v27 — `P3_Viable`: `𝒲_k` defined, `Wblind_iff_survK` |

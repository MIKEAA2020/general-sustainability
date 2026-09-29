# Lean audit v20 — `prop:antichain` (iii) closed; (ii) diagnosed

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 27 jobs**, **0 warnings**, zero `sorry`.

New module **`lean/Formalizations/P3_Antichain.lean`** (7,137 B).

| Item | Outcome |
|---|---|
| `prop:antichain` (iii) — the antichain property | **Closed** |
| `prop:antichain` (ii) — alpha-vectors = indicators of maximal sets | **Not closed.** Blocking lemma diagnosed and named |
| `prop:pl` explicit half, `thm:support` | Not started this batch |

---

## What was proved

`prop:antichain` (iii) turns out to be **one line from the definition of
maximality**, and needs neither finiteness nor Sperner's theorem:

```
def MaximalIn (l) (S) := S ∈ l ∧ ∀ T, T ∈ l → subsetOf S T → subsetOf T S

theorem maximals_incomparable (hS : MaximalIn l S) (hT : MaximalIn l T)
    (hST : subsetOf S T) : memEquiv S T := ⟨hST, hS.2 T hT.1 hST⟩

theorem maximals_antichain (l) : Antichain l (MaximalIn l)
```

Maximality says every *larger* element is in fact equivalent, so two maximal
elements comparable by `⊆` are extensionally equal. That is exactly the
antichain statement.

Also supplied: the order vocabulary (`subsetOf` with refl/trans,
`memEquiv` with refl/symm/trans — an equivalence relation), and the two
definitions that link this to `prop:pl`: `alphaOf` (the indicator of a
subset) and `dotOn` (the pairing `αᵀb` over a finite ambient list).

**Not attempted:** the counting consequence `≤ C(n, ⌊n/2⌋)`. Sperner's
theorem is a separate combinatorial result and is not implied by the
antichain property proved here.

## What was not proved, and exactly why

`prop:antichain` (ii) is the conjunction of

* (⊇) every maximal element's indicator *is* an alpha-vector — the value is
  unchanged by pruning the witness family to its maximal elements;
* (⊆) every alpha-vector *is* a maximal indicator — nothing non-maximal
  survives pruning.

Both need the same engine, which I have named and left as an explicit
hypothesis rather than assumed:

```
def MaximalAbove (l) (S) (T) := T ∈ l ∧ subsetOf S T ∧ MaximalIn l T
-- missing:  ∀ S, S ∈ l → ∃ T, MaximalAbove l S T
```

**Every `S ∈ S_k` is contained in a maximal `T ∈ S_k`.** True in a finite
family, but the proof needs one of:

1. a termination argument (length strictly increases along a chain, bounded
   by `univX.length`), or
2. a `Nat`-maximum over the sub-family of supersets of `S`,

together with the lemma that **two `Nodup` sublists of `univX` with the same
elements have the same `lsum`** — which is what converts "maximal by
inclusion" into "the value is attained there". That last lemma needs
`List.erase` / `List.Subperm` infrastructure. Probing showed this layer
carries `lsum_filter_le` and `lsum_filter_ind` but I did not confirm
`erase`/`Subperm`, and establishing them is the next unit of work.

I **attempted** the stronger statements (`dotOn_alphaOf_eq_bS`,
`dotOn_alphaOf_filter`, `Vfam_prune_le`) and they did not compile — the
`sorry`-free build required trimming them out. Rather than ship them with
`sorry` or a faked hypothesis, they are removed and the module states
plainly that they are open. `Vfam_prune_le` was already written
conditionally on `hmax`, so reinstating it is mechanical once
`exists_maximal_above` lands.

## A deliberate assumption, recorded

This module assumes **`[DecidableEq X]`**, unlike the other P3 modules.
`alphaOf` is defined by `if x ∈ S`, and `x ∈ S` on a `List` is decidable
only with `DecidableEq X`. Earlier P3 modules avoided this by representing
subsets as `List X` rather than `X → Bool`; that avoidance is unavailable
once indicators are wanted *as functions*, which is what (ii) requires. `X`
is finite throughout, so nothing is lost mathematically.

## Technical note

`List.filter` is `Bool`-valued, so `l.filter (fun S => MaximalIn l S)` does
not elaborate — the same trap as v18. `Antichain` is therefore parameterised
by a **predicate** `P : List X → Prop` rather than by a filtered list. This
is the second time this has bitten; the general rule is that `Prop`-valued
selection over lists should be carried as a predicate parameter, not by
filtering.

## P3 status

| Status | Count | Results |
|---|---|---|
| Formalized (complete) | 8 | `thm:recursion`, `thm:lattice` (i), `prop:dr` (i), `prop:pathdeficit`, `prop:deficit` (i)(ii)(iii), `prop:degen`, `prop:noisyprobe`, `prop:freeze` |
| Partial | 3 | `thm:support`, **`prop:antichain`** ((i) done, **(iii) closed**, (ii)(iv) open), `prop:pl` (convexity closed; witness set open) |
| Instance-level | 6 | `cor:closed`, `thm:parametric`, `thm:agree`, `thm:class`, `prop:learn`, `prop:additivelaw` |
| Out of reach | 1 | `prop:probecount` (mathematically verified, v10 §3) |

## Suggested next steps

1. **Probe for `List.erase` / `List.Subperm` / `List.Perm`**, then prove
   `lsum_eq_of_mem_iff` (same elements + `Nodup` ⟹ same `lsum`). That is
   the single missing lemma for (ii) and for the `prop:pl` bridge.
2. **Prove `exists_maximal_above`** (route 1 or 2 above), then reinstate
   `Vfam_prune_le` / `Vfam_prune_ge` to close (ii) (⊇), and its converse.
3. `prop:antichain` (iv) — the deficit as `min b(S^c)` over maximal
   survivable sets.
4. `prop:pl` explicit half, then `thm:support` (still a modelling decision
   about the disturbance weighting, not merely a proof).

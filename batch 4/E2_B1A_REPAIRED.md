# E2.B1(a) — Maximal Certificate Family: REPAIRED

**Target.** The `B1.Theorem (a)` section of `batch 2/02_elevation/E2_SELECTORS_AND_CERTIFICATES.md`, and the manifest row `E2.B1(a)` (line 75).

**This file is a proposal. No repository file has been modified.**

**Disposition.** The Knaster–Tarski half is correct and is retained verbatim. The final sentence — *"R02.Thm1 applies to every subfamily `(C,c)` with `C ⊆ 𝒱*` … which is consistent because consistency is inherited by subfamilies"* — is **false**, and the direction of the monotonicity argument is exactly backwards. The repair keeps the whole of what the theorem was for: `R02.Thm1` does apply, but to the family `𝒱*` itself, and the correct reason is that certificates generated from a subset **land inside `𝒱*`**, not that the subset is itself consistent.

**Verification.** `reaudit/verify_e2b1a_b9_repair.py`, Part A, 12 assertions, exit 0.

---

## 1. What is correct and stays

`𝒦(X)` (closed subsets of the compact `X`, ordered by inclusion) is a complete lattice; `Γ` monotone makes Knaster–Tarski apply; the greatest fixed point exists with

```
𝒱* = ∨ { C ∈ 𝒦(X) : C ⊆ Γ(C) }      (join of all post-fixed points).
```

All verified: backward iteration from the top converges to `𝒱*`, `Γ(𝒱*) = 𝒱*`, and `𝒱*` equals the join of the post-fixed points.

---

## 2. What is false

> "…applied to any subfamily of the maximal one, **which is consistent because consistency is inherited by subfamilies** (monotonicity of the certificate conditions)."

Consistency is the post-fixed condition `C ⊆ Γ(C)`. Monotonicity gives `C ⊆ C′ ⟹ Γ(C) ⊆ Γ(C′)`. From `C ⊆ 𝒱*` it follows that

```
Γ(C)  ⊆  Γ(𝒱*)  =  𝒱*,
```

which is the **wrong direction**: it bounds `Γ(C)` from above by `𝒱*`, whereas consistency needs `Γ(C)` to contain `C`. Subfamilies of a consistent family are in general **not** consistent.

**Counterexample (verified).** `X = {1, 2}` and

| `C` | `Γ(C)` |
|---|---|
| `∅` | `∅` |
| `{1}` | `{2}` |
| `{2}` | `{1, 2}` |
| `{1, 2}` | `{1, 2}` |

`Γ` is monotone (all 16 comparable pairs checked). Backward iteration from `X` gives `𝒱* = {1, 2}`, and `Γ(𝒱*) = 𝒱*` ✓. Now `C = {1} ⊆ 𝒱*`, but `Γ(C) = {2}`, and `{1} ⊄ {2}` — so `C` is **not** post-fixed, hence not a consistent certificate family, even though it sits inside the maximal one.

The same check confirms the general failure: there exist `C ⊆ P` with `P` post-fixed and `C` not post-fixed.

**The direction that *is* true.** Post-fixed sets are closed under **joins**, not under subsets: if `C_i ⊆ Γ(C_i)` for each `i`, then with `C = cl(⋃ C_i)`, monotonicity gives `Γ(C) ⊇ Γ(C_i) ⊇ C_i` for every `i`, so `Γ(C) ⊇ ⋃ C_i`, and closedness gives `Γ(C) ⊇ C`. Verified on all 9 pairs of post-fixed sets. This is precisely why `𝒱* = ∨{post-fixed points}` is itself post-fixed — and it is the only inheritance property available.

---

## 3. `E2.B1(a)` repaired

> ### E2.B1(a) (repaired) — Maximal certificate family
>
> Let `Γ : 𝒦(X) → 𝒦(X)` be monotone (P1) and well defined on `𝒦(X)` (P2). Then:
>
> **(i)** `Γ` has a greatest fixed point `𝒱* = ∨{C ∈ 𝒦(X) : C ⊆ Γ(C)}`, and `Γ(𝒱*) = 𝒱*`. In particular `𝒱*` is itself a consistent certificate family.
>
> **(ii)** The post-fixed ("consistent") sets are closed under **joins**. They are **not** closed under taking subsets, and `C ⊆ 𝒱*` does **not** imply `C ⊆ Γ(C)`.
>
> **(iii) Correct transfer.** For every `C ⊆ 𝒱*`,
> ```
> Γ(C) ⊆ Γ(𝒱*) = 𝒱*,      and hence      Γⁿ(C) ⊆ 𝒱*   for every n.
> ```
> So `R02.Thm1` applies **to the family `𝒱*`**, and the closed-loop certificate recursion may be *started* from any `C ⊆ 𝒱*` provided the certificate states are **tracked in `𝒱*`**, not in `C`.

*Proof.* (i) Knaster–Tarski, as in the original. (ii) The join argument of §2; the counterexample of §2 for the negative. (iii) `C ⊆ 𝒱*` and monotonicity give `Γ(C) ⊆ Γ(𝒱*) = 𝒱*`; induction gives `Γⁿ(C) ⊆ 𝒱*`. `R02.Thm1`'s hypothesis is that (REG) holds at every member of the family it is run on — and `𝒱*` satisfies that, being a fixed point. ∎

**Why (iii) is what the theorem needed.** `R02.Thm1`'s clause (REG)(ii) requires successor certificates to be **members of the family**. A smaller family makes that obligation *harder*, not easier; a larger family makes it easier but adds new points at which (REG) must hold. `𝒱*` is the maximal family closed under the recursion, so it imposes the weakest closure obligation while still containing every reachable certificate state. That is exactly why one runs the recursion in `𝒱*` — and it is a stronger statement than the original's, because it identifies the object the recursion actually lives in.

**Suggested register text** (proposal only — not applied):

> `E2.B1(a) | Maximal certificate family | Γ monotone on the complete lattice 𝒦(X) ⟹ greatest fixed point 𝒱* = ∨{post-fixed points}, with Γ(𝒱*) = 𝒱*; post-fixed sets are join-closed but NOT subset-closed; R02.Thm1 applies to 𝒱* itself and the recursion may be started from any C ⊆ 𝒱* provided it is tracked in 𝒱* | PROVEN (repaired) — the original claimed consistency is inherited by subfamilies, which is false (explicit 2-point counterexample). See batch 4/E2_B1A_REPAIRED.md`

---

## 4. Verification

`reaudit/verify_e2b1a_b9_repair.py`, Part A — 12 assertions, exit 0.

| # | Claim | Result |
|---|---|---|
| A0 | `Γ` monotone (all comparable pairs); well defined on `𝒦(X)` | ✓ |
| A2 | `𝒱* = {1,2}` by backward iteration; `Γ(𝒱*) = 𝒱*`; `𝒱*` = join of post-fixed points | post-fixed: `∅, {2}, {1,2}` |
| A1 | `C = {1} ⊆ 𝒱*` but `Γ(C) = {2} ⊉ C` — not consistent | ✓ |
| A1 | monotonicity gives `Γ(C) ⊆ 𝒱*`, the wrong direction | ✓ |
| A3 | joins of post-fixed sets are post-fixed (9 pairs); hence `𝒱*` is post-fixed | ✓ |
| A4 | there exist `C ⊆ P`, `P` post-fixed, `C` not post-fixed | 1 instance |
| A5 | `Γ(C) ⊆ 𝒱*` for every `C ⊆ 𝒱*` (4 subsets); iteration stays inside `𝒱*` | ✓ |

**One error in my own test, caught by it failing.** My first attempt at the (REG)-inheritance check treated a *set* as though it were a *family of sets* and indexed the operator by states, raising `KeyError`. Beyond the bug, the framing itself was wrong: "closure is inherited upward" is not the right statement either, since a larger family adds new members that must themselves satisfy (REG). I replaced it with (iii), which is both true and what the theorem needs.

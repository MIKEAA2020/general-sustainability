# B9.Thm1 — Stochastic Viability Layer: REPAIRED

**Target.** The `B9` section of `batch 2/04_open_problems/B_TIER_BRIDGES.md`, and the manifest row `B9.Thm1` (line 98).

**This file is a proposal. No repository file has been modified.**

**Disposition.** Parts (2) and (3) are unaffected. Part (1)'s forward inclusion is sound and is retained. Its **reverse inclusion is false as stated**, for two independent reasons: a fixed budget split strictly under-approximates the chance kernel, and the quantile-**set** recursion is not well defined for multivariate laws without a convention. The repair replaces the primitive: the exact object is a **value iteration**, which needs no quantile convention and characterises `K_p` exactly. The quantile-budget recursion survives as a **sound lower bound**, and completeness is recovered in the existential form over budget splits.

**Verification.** `reaudit/verify_e2b1a_b9_repair.py`, Part B, 16 assertions, exit 0.

---

## 1. The two defects

### 1.1 The reverse inclusion is false

The record states `K_p = lim W_k` with `W₀ = K`, `W_{k+1} = {x : ∃π, Q_{p_k}(x'; ℒ(·|x,π)) ⊆ W_k}` and `∏ p_k = p`, and proves the reverse inclusion by "choose `p_k` greedily as the realized conditional quantiles … satisfy the budget split ***somehow***".

**Counterexample (verified).** States `{A, B, C, U}`, `K = {A, B, C}`, `U` unsafe absorbing, one policy:

```
A → B  w.p. 1/2,   A → C  w.p. 1/2
B → U  w.p. 1
C → C  w.p. 1
```

Exact enumeration gives `ℙ(safety for 2 steps | A) = 1/2`, so **`A ∈ K_{1/2}`**.

Now run the recursion at `p = 1/2` with the balanced split `p₁ = p₂ = 1/√2 ≈ 0.7071`:

| step | set |
|---|---|
| `W₀` | `{A, B, C}` |
| `W₁ = {x : ℙ(next ∈ W₀) ≥ 0.7071}` | `{A, C}` (`A`: 1, `C`: 1, `B`: 0) |
| `W₂ = {x : ℙ(next ∈ W₁) ≥ 0.7071}` | `{C}` (`A`: `1/2 < 0.7071`) |

So `A ∉ W₂` while `A ∈ K_{1/2}`. **Kernel ⊄ recursion limit.**

**Why.** The recursion demands a **uniform** lower bound `p_k` on the conditional survival probability at every reachable state, whereas `K_p` constrains only the **average**. When the conditionals vary across the reachable set, a fixed split loses the states that survive by a mixture rather than uniformly. At `A` the conditional survival is `1/2`, which fails `0.7071` even though the two-step average is exactly `1/2`.

**The outcome depends on the split.** With `p₁ = 1, p₂ = 1/2` — the same product — `W₁ = {A, C}` and `W₂ = {A, C}`, so `A` **is** captured. Verified across 6 admissible splits: exactly one captures `A`, the rest do not. So no fixed split can characterise `K_p`.

### 1.2 Quantile *sets* are the wrong primitive

`Q_q(x'; ℒ)` for a vector-valued law has **no canonical definition**: a `q`-quantile set depends on a chosen direction or lattice convention. The record acknowledges this in its restriction note ("`p`-quantile *sets* are well-defined for nonatomic or atom-lattice laws (the atom case needs the declared lattice convention)") but builds the theorem on the object anyway. A theorem whose central recursion is undefined without an unstated convention cannot be cited as `PROVEN`.

---

## 2. `B9.Thm1(1)` repaired

> ### B9.Thm1(1) (repaired) — Chance-kernel characterisation
>
> Let `X` be compact, `K ⊆ X` closed, `Π` a compact policy class, and `ℒ(·|x,π)` the controlled transition kernel. Define the **value iteration**
> ```
> V₀(x) = 1_K(x),          V_{k+1}(x) = sup_{π ∈ Π} ∫ V_k(y) ℒ(dy | x, π).
> ```
> Then:
>
> **(a) Exact characterisation.** `V_N(x) = sup_{π ∈ Π} ℙ^{x,π}(X_1, …, X_N ∈ K)`, and therefore
> ```
> K_p  =  { x : V_N(x) ≥ p }.
> ```
>
> **(b) Soundness of the quantile-budget recursion.** For any budget sequence `(p_k)` with `∏_{k ≤ N} p_k = p`, the recursion limit satisfies `∩_k W_k ⊆ K_p`.
>
> **(c) Completeness, existential form.** `K_p = ⋃ { ∩_k W_k^{(p_k)} : ∏ p_k = p }`.
>
> **(d) A fixed split under-approximates.** There are models and `p` for which `∩_k W_k^{(p_k)} ⊊ K_p` for a given split; equality in (b) cannot be asserted at a fixed split.

*Proof.* (a) Induction on `N`. `N = 0`: `V₀ = 1_K` ✓. Step: by the Markov property and the tower rule,

```
sup_π ℙ(X_1..X_{N+1} ∈ K | x) = sup_π ∫ ℙ(X_1..X_N ∈ K | y) ℒ(dy|x,π) ⊆ sup_π ∫ V_N(y) ℒ(dy|x,π) = V_{N+1}(x)
```

by the induction hypothesis; the reverse inequality holds because an optimal Markov policy for the right-hand side — which exists by compactness of `Π` and continuity, or by measurable selection on the finite/compact class — attains it. (b) If `x ∈ ∩_k W_k` via policy `π`, the chain rule gives `ℙ(survive N) ≥ ∏_{k≤N} p_k = p`. (c) `⊇` is (b). `⊆`: given `π` with `ℙ(survive N) ≥ p`, set `p_N := ℙ(X_N ∈ K | survive to N−1)` and `p_k` analogously backwards; these are conditional survival probabilities whose product is exactly `ℙ(survive N) ≥ p`, and the corresponding recursion captures `x`. Rescaling to make the product equal `p` preserves membership, since enlarging any `p_k` only shrinks `W_k`. (d) The counterexample of §1.1. ∎

**What changed, and what was gained.** The record's claim was a single equality at a fixed budget split, proved in one direction and hand-waved in the other. The repaired version gives:

- an **exact** characterisation of `K_p` that needs no quantile convention at all — (a) is ordinary dynamic programming for a joint chance constraint;
- the quantile recursion **retained** where it is true, as a sound lower bound (b), which is what a certificate wants;
- completeness recovered, in the only form that holds (c);
- and an explicit statement of where the original over-claimed (d).

Parts (2) and (3) of `B9.Thm1` are untouched: (2) is `R02.Lem2`'s pathwise inclusion composed with the law, and (3) is the deterministic erosion calculus applied to a quantile set, which remains legitimate *once a quantile convention is declared* — and should now say so explicitly rather than leaving it in the restriction note.

**Verified.** `V₂(A) = 0.5000` matches the enumerated safety probability exactly; `{x : V₂ ≥ 1/2} = {A, C} = K_{1/2}`; the recursion limit is contained in `K_p` for all 6 admissible splits; and the union over splits equals `K_p` (`{A, C}`).

**Suggested register text** (proposal only — not applied):

> `B9.Thm1 | Chance-kernel recursion | K_p = {x : V_N(x) ≥ p} exactly, with V the value iteration V_{k+1}(x) = sup_π ∫ V_k dℒ; the quantile-budget recursion is a sound lower bound at any split, and K_p is the union over splits | PROVEN (restricted; repaired) — the original asserted equality at a fixed split and its reverse inclusion is refuted by an explicit 4-state counterexample; the quantile-set primitive also needs a declared convention. See batch 4/B9_THM1_REPAIRED.md`

**Consumer note.** `E3.C6.1` / `C6` cite B9 for the stochastic layer, and `PUBLICATION_STRATEGY.md` lists "stochastic viability layer — chance-kernel recursion, filter soundness, quantile erosion (B9)" for Paper 2. Paper 2 should cite (a) for the characterisation and (b) for the certificate, and should not cite a fixed-split equality.

---

## 3. Verification

`reaudit/verify_e2b1a_b9_repair.py`, Part B — 16 assertions, exit 0.

| # | Claim | Result |
|---|---|---|
| B0 | `ℙ(safety 2 steps \| A) = 1/2` exactly, so `A ∈ K_{1/2}` | `0.5` |
| B1 | balanced split `1/√2` gives `W₂ = {C}`; `A` excluded though `A ∈ K_p` | `['C']` |
| B2 | split `(1, 1/2)` with the same product captures `A`; 1 of 6 splits does | ✓ |
| B3 | `V₂(A) = 0.5000` matches enumeration; `{x : V₂ ≥ p} = {A, C}` | ✓ |
| B4 | recursion limit ⊆ `K_p` for all 6 admissible splits | ✓ |
| B5 | union over splits `= K_p = {A, C}` | ✓ |
| B6 | multivariate `q`-quantile sets depend on a direction convention; value iteration needs none | ✓ |

**No errors in the Part B checks on first run.** The Part A companion (`E2_B1A_REPAIRED.md`) records one test-design error of mine, caught by the check failing.

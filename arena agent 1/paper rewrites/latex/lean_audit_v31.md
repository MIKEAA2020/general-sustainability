# Lean verification audit — v31
## Items 4 and 5: `prop:pl` rationality, and the Sperner count in `prop:antichain` (iii)

Branch `lean-audit-v4`. Build after this work: **rc = 0, 40 jobs, 37 imported
modules, zero warnings, zero `sorry`.** Verified in the working clone that
produced it; the fresh-clone check is named as the closing step of §3.

Two new modules, neither of which edits an existing file:

| module | item | status |
|---|---|---|
| `Formalizations/P3_Rational.lean` | 4 — `prop:pl` rationality | **complete** |
| `Formalizations/P3_Binomial.lean` | 5 — Sperner count | **machinery only; the bound is NOT claimed** |

---

## 1 · Item 4 — `prop:pl` rationality — CLOSED

### 1.1 The claim, verbatim

`prop:pl` closes (paper2 v11, lines ~490–551) with:

> Over rational `T`, `g`, and priors, every `α` is an exact rational vector,
> every `V^Π_k(b)` at a rational belief is an exact rational, and the
> attaining witness is part of the computation.

and the proof says only:

> rational transition and observation data with rational `Γ^Π_k` give
> rational backups, by induction.

### 1.2 The design decision, and why

The obvious move is to instantiate at `K = ℚ`. **Doing that would make the
clause vacuous**: at `K = ℚ` every element is rational, so "every `α` is an
exact rational vector" degenerates to a statement about the type of `α` and
carries no content — it would be satisfied by a construction that is
intuitively transcendental, because no transcendental elements exist to
distinguish it.

The paper's clause has content precisely as a **closure** claim: the
construction preserves rationality, given rational data. So rationality is
introduced as an interface over an arbitrary `OrdField K`:

```
class RatSub (K : Type) [OrdField K] where
  isRat : K → Prop
  rat_zero : isRat 0
  rat_one  : isRat 1
  rat_add  : isRat a → isRat b → isRat (a + b)
  rat_neg  : isRat a → isRat (-a)
  rat_mul  : isRat a → isRat b → isRat (a * b)
  rat_inv  : isRat a → isRat a⁻¹
```

and the theorems proved are closure theorems: `rat_lsum` (finite sums),
`rat_lmax` (finite maxima — via `lmax_isMax`, so the maximum is *attained*,
not merely approached, which is what makes the witness clause go through),
`rat_ind`, then `alphaSeg_rat`, `smass_rat`, `VR_rat`, `VFb_rat`,
`VfamAdm_rat`. The "attaining witness is part of the computation" half is
discharged by `VfamAdm_rat_witness`, using `VfamAdm_finite_range`.

`instance ratSubRat : RatSub Rat` (`isRat := fun _ => True`) shows the
interface is satisfiable, i.e. that the theorems are not vacuous where they
have content (abstract `K`).

### 1.3 A second, larger consequence: the layer now has a model

`P3_Rational` proves

```
instance ratOrdField : OrdField Rat
```

Until now **every** theorem in this layer was proved over an abstract
`OrdField K` with no instance anywhere in the layer. That is consistent —
and consistent-only. Nothing ruled out the interface being uninhabited, in
which case all 40 jobs of theorems would be vacuously true. `Rat` satisfies
the interface, so the layer is now known to be inhabited and every prior
result has a non-vacuous interpretation.

Three fields needed work: `zero_ne_one` and `zero_le_one` by `decide`, and
`add_le_add`, assembled from `Rat.add_le_add_left` in four `calc` steps
(`OrdField` is not a `Preorder`, so `le_trans` has to be applied by hand and
`calc` cannot chain two `≤` steps).

### 1.4 Scope, stated plainly

Rationality is proved for the **segment form only**. `alphaSeg_rat` holds
because `α^seg` is the survival indicator `ind (survT M t)`, i.e. `0` or
`1` — rational with **no hypothesis on the data at all**, which is stronger
than the paper's clause and is the honest reading of the objects this layer
assigns to the deterministic operator.

The general masked backup would need rational `T` and `g` on `SafeMDP`'s
stochastic kernels. That is the *other* operator, and it is out of scope by
design since v24 (`rem:operators` + `prop:degen` prescribe the adversarial
reading for the deterministic layer). Formalizing rationality there would
mean first formalizing a rational-kernel `SafeMDP` interface, which is a
separate module and a separate decision.

---

## 2 · Item 5 — the Sperner count — MACHINERY LAID, RESULT NOT CLAIMED

### 2.1 The claim, verbatim

`prop:antichain` (iii) (paper2 v11, lines 355–357):

> (iii) the maximal elements form an antichain, so their number is at most
> `\binom{n}{\lfloor n/2 \rfloor}` for a support of size `n` (Sperner);

with the proof (line 384–387):

> (iii) Maximality is inclusion-maximality, so the maximal sets form an
> antichain, and their count is at most `\binom{n}{\lfloor n/2 \rfloor}` by
> Sperner's theorem (Sperner, 1928).

So (iii) has **two** halves: the antichain property (which the paper
*proves*) and the count (which the paper *cites*).

* The antichain half is already formalized: `P3_Antichain` (v20) has
  `Antichain`, `maximals_incomparable`, and `maximals_antichain`.
* The count half is the new work, and it is **not finished**.

### 2.2 What blocks it: the layer has no combinatorics at all

This is the finding of the turn, and it changes the shape of the task. The
layer is dependency-free, and (probed directly, v31) the following are
**unknown identifiers**:

```
Nat.choose   Nat.choose_succ_succ   Nat.choose_le_middle   Nat.choose_le_pow
Nat.factorial   Nat.factorial_succ   Nat.choose_eq_factorial_div_factorial
List.permutations   List.length_permutations   List.mem_permutations
LinearOrderedField   Rat.instLinearOrderedField   Rat.instField
```

`OrdField` (`Prelude.lean:51`) is the layer's own interface, not a fragment
of mathlib's algebraic hierarchy. So Sperner cannot be reduced to a library
call, and it cannot be reduced to importing one either. The binomial
foundation has to be built.

### 2.3 What was built

`P3_Binomial` defines `choose` by Pascal's recursion — so the recursion law
is `rfl` — and proves:

| theorem | content |
|---|---|
| `choose_succ_succ` | Pascal's recursion (definitional) |
| `choose_zero_right` | `C(n,0) = 1` |
| `choose_zero_succ` | `C(0,k+1) = 0` |
| `choose_eq_zero_of_lt` | `n < k → C(n,k) = 0` |
| `choose_self` | `C(n,n) = 1` |
| `choose_pos` | `k ≤ n → 0 < C(n,k)` |
| `choose_succ_self` | `C(n+1,n) = n+1` |
| `choose_six_three` | `C(6,3) = 20`, by `native_decide` — a check that the recursion computes binomials |

This is the prerequisite without which the bound cannot even be *stated*.
It is not the bound.

### 2.4 What remains, and the precise reason it is not done

Three steps.

1. **Unimodality**: `C(n,k) ≤ C(n, ⌊n/2⌋)`.
2. **LYM**: `Σ_{S∈A} 1/C(n,|S|) ≤ 1` for an antichain `A`, by maximal-chain
   counting.
3. **The bound**: `|A| ≤ C(n,⌊n/2⌋)`, from (1) + (2) + `|A|` finite.

**Step 1 was attempted and failed, informatively.** The natural induction
reduces `C(n+1,k+1) ≤ C(n+1,k+2)` to `C(n,k) ≤ C(n,k+2)` — *two* steps, not
one. The first step is the induction hypothesis; the second needs the
hypothesis at `k+1`, and at the boundary (`2(k+2) = n+1`) that hypothesis is
**false**, while the conclusion is still **true** — at the boundary the two
binomials are equal by **symmetry**. So the recursion cannot close without
binomial symmetry, and symmetry (`C(n,k) = C(n,n-k)`) is itself a separate
non-trivial induction. Unimodality was therefore **removed rather than
claimed**; a plausible-looking proof that does not elaborate is worse than
an honest gap.

**Step 2 needs more than that**: factorials, an enumerator for permutations
of a finite list, and the identity `C(n,k)·k!·(n-k)! = n!`. `List.Perm`
exists; `List.permutations` does not, so the enumerator has to be written
and its length proved. This is the larger half of the work.

**Honest estimate**: two to three further modules (`P3_Binomial2` for
symmetry + unimodality; `P3_LYM` for factorials, the permutation
enumerator, and the chain count; `P3_Sperner` for the final bound). Not
attempted here rather than half-attempted.

### 2.5 What this means for the coverage claim

`prop:antichain` is currently **partial**: (i), (ii), (iv) are formalized;
(iii) is formalized **as an antichain** but the stated **cardinality bound
is not**, and the paper's own proof cites Sperner rather than deriving it.
The coverage index must record (iii) as partial, not complete. This
correction is the point of the audit: "the maximal elements form an
antichain" is a five-line theorem that was done in v20, and it is easy to
read that row as covering (iii) when half the statement is a cited
cardinality bound.

---

## 3 · Build state and totals

`lake build` → **rc = 0, 40 jobs**, 37 imported modules. **Zero warnings**,
zero `sorry`.

P3 totals: **11 complete · 0 partial · 6 instance · 1 out of reach**, with
`prop:antichain` (iii) now correctly counted as **partial** by §2.5 — so
11 complete · **1 partial** · 6 instance · 1 out of reach.

Two fixes were needed on first build, both mechanical and both recorded for
the next turn:

* `theorem … : DecidableEq Rat := inferInstance` fails — `DecidableEq` lives
  in `Type`, not `Prop`. Stated instead as
  `rat_exact_dedup (a b : Rat) : a = b ∨ a ≠ b`, by `by_cases`.
* Helpers whose `K` appears only implicitly need `(K := K)` at **both** the
  definition and every call site, or elaboration reports
  `typeclass instance problem is stuck` at the definition and
  `Unknown identifier` at the uses.

Remaining step: confirm the fresh-clone build (clone to `/var/tmp`, not
`/tmp` — a full clone costs ~906 M against a 993 M tmpfs).

---

## 4 · Files

| file | status |
|---|---|
| `lean/Formalizations/P3_Rational.lean` | new, green |
| `lean/Formalizations/P3_Binomial.lean` | new, green, machinery only |
| `lean/Formalizations.lean` | 35 → 37 imports |
| `lean_README_v7.md` | new; supersedes v6 (40 jobs / 37 imports) |
| `lean_audit_v31.md` | this file |

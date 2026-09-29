# Lean audit v19 — `prop:pl`, convexity half

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 26 jobs**, **0 warnings**, zero `sorry`.

New module **`lean/Formalizations/P3_Convexity.lean`** (10,121 B).

Second of the four P3 partials. `prop:pl` moves from *partial* to
**partial-with-convexity-closed**; see the scope statement below, which is
the substantive part of this report.

---

## The claim, and the half that is closed

> Fix a declared class `Π`. At every horizon `k`, `V^Π_k` is piecewise
> linear and **convex**: `V^Π_k(b) = max_{α ∈ Γ^Π_k} αᵀb` for a finite
> witness set `Γ^Π_k` … constructed by the masked backup …

The proposition has two halves. The **explicit representation** (the
`Γ_k` construction and the masked-backup identity) and the **convexity**
that representation entails. This module closes the second and says nothing
about the first.

**Convexity survives the Bellman recursion without ever mentioning
alpha-vectors**, because every operation in a backup preserves it:

```
V_0     = total                          linear, hence convex
V_{k+1} = max_a  Σ_y  V_k ∘ step(a,y)
          └─ max of finitely many convex functions is convex
                └─ sum of convex functions is convex
                      └─ convex ∘ linear is convex
```

`VAdm_convex` establishes convexity of `V^Π_k` for **every** declared class
and every horizon, over the abstract `OrdField`.

## Why the explicit half is not closed

The route through `Γ_k` needs
`Γ_{k+1} = {α^{a,γ·} : a ∈ A(Π), γ· a selection}`, and expanding
`Σ_y max_{γ_y}` into `max_{selections} Σ_y` requires:

* a `selections` construction — all functions `Y → Γ_k`, as a list;
* a max/sum exchange lemma over that list;
* bookkeeping for duplicate removal "by exact equality", which needs
  `DecidableEq` on the alpha-vectors.

None of that exists in this dependency-free layer, and building it is
genuinely combinatorial rather than a routine extension. It is flagged rather
than faked, per the standing instruction.

So `prop:pl` is **not** complete. Convexity — the property the paper draws
from the representation and the part that is a statement about the value
function rather than about a particular witness construction — is now proved,
and it is proved *without* assuming the representation. That is worth having
independently: it does not depend on the `Γ_k` machinery being correct, and
it needs no rationality of `T`, `g`, or the prior.

## New declarations

| Declaration | Content |
|---|---|
| `mixF`, `mix` | the mixture belief (nonnegativity needs `0 ≤ w ≤ 1`) |
| `Convex`, `SeesF` | convexity on beliefs; "sees only the mass function" |
| `total_mix` | `total` is linear |
| `step_mix_f` | the belief update is linear, pointwise in the state |
| `convex_lsum` | a sum of convex functions is convex |
| `convex_lmax` | a max of finitely many convex functions is convex |
| `convex_step` | convexity is preserved under precomposition with `step` |
| `VAdm_seesF` | `VAdm` sees only `.f` (via `VAdm_congr`) |
| **`VAdm_convex`** | **`prop:pl`, convexity** |

*Axioms:* `VAdm_convex` and `convex_lmax` → `[propext, Classical.choice,
Quot.sound]` (choice enters through `lmax`). `step_mix_f` → `[propext]` only
(funext). No `sorry`.

## A design note worth keeping

`Mass` has **no extensionality lemma** in this layer — a fact recorded since
v8. So `step(mix w m₁ m₂)` cannot be proved equal to
`mix w (step m₁) (step m₂)` as beliefs. The workaround is `SeesF`: the two
beliefs have the *same* `.f` (proved by `funext` + `step_mix_f`), and a
function that sees only `.f` cannot distinguish them. This is the same
discipline as v8's Prop-valued `survK`, and it is why `convex_step` carries
the `SeesF` hypothesis rather than being stated for arbitrary `f`.

## Technical notes

1. **`λ` is a reserved token** — it cannot be a variable name. The weight is
   called `w`.
2. **Distribution is `left_distrib` / `right_distrib`**, not `mul_add` /
   `add_mul`. `(a+b)*c` is `right_distrib`.
3. **`OrdField.mul_le_mul_of_nonneg'`** is a structure field; the exposed
   theorem is `mul_le_mul_of_nonneg_right`.
4. **`unfold` on a structure-literal `def` is unreliable**; `change` against
   the reduced form worked, but only when the two sides are definitionally
   equal — an associativity difference (`(w·m₁)·T·g` vs `w·(m₁·T·g)`) is
   *not*, and needs an explicit `simp only [mul_assoc]` step.
5. `one_sub_nonneg` (v13) and `VAdm_congr` (v11) were reused as-is; the
   module imports `P1_BeliefSafety`, `P3_Sufficiency`, `P3_Freeze_Noisy`.

## P3 status

| Status | Count | Results |
|---|---|---|
| Formalized (complete) | 8 | `thm:recursion`, `thm:lattice` (i), `prop:dr` (i), `prop:pathdeficit`, `prop:deficit` (i)(ii)(iii), `prop:degen`, `prop:noisyprobe`, **`prop:freeze`** |
| Partial | 3 | `thm:support`, `prop:antichain`, **`prop:pl`** (convexity closed; witness set open) |
| Instance-level | 6 | `cor:closed`, `thm:parametric`, `thm:agree`, `thm:class`, `prop:learn`, `prop:additivelaw` |
| Out of reach | 1 | `prop:probecount` (mathematically verified, v10 §3) |

## Suggested next steps

1. **`prop:antichain` (ii)** — alpha-vectors are exactly the indicators of
   the maximal survivable sets. This is the natural bridge to the `Γ_k`
   construction above, since it identifies the witnesses concretely in the
   deterministic-kernel case; doing it may make `prop:pl`'s explicit half
   cheaper.
2. **`prop:pl`, explicit half** — the `selections` combinatorics.
3. **`thm:support`** — the support identity. Still the hard one: it needs a
   disturbance *weighting*, because the robust reading carries no
   disturbance distribution and so the posterior mass is not defined. That is
   a modelling decision, not merely a proof.

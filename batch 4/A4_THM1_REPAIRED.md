# A4.Thm1 — Nonlinear Assume–Guarantee: REPAIRED

**Target.** The `A4.Thm1` proof, Step 2, in `batch 2/04_open_problems/A4_NONLINEAR_SMALL_GAIN.md`, and the manifest row `A4.Thm1` (line 93).

**This file is a proposal. No repository file has been modified.**

**Disposition.** Step 1, Step 3, the statement, and all of `A4.Thm2` are correct. **Step 2's displayed inequality has the wrong sign on `α`** and puts the encroachment on the wrong side of the bound. The error is **not cosmetic**: A4's inequality admits outward velocities that leave the eroded set immediately. The repair restates Step 2 in the packet's convention; **the conclusion of A4.Thm1 is unchanged**, because Step 3 consumes only `⟨n, w⟩ ≤ 0` on the boundary, which the corrected chain delivers from `(∗)`.

**Verification.** `reaudit/verify_e2b2a_a4_repair.py`, Part B, 17 assertions, exit 0.

---

## 1. The controlling convention

`research_program/general_theory_math_closure_packet/corrected_theorems/02_operator_I_strong_invariance_and_erosion.md`, Lemma 2, states:

```
sup_{v ∈ G(p)} ⟨n(p), v⟩ ≤ −α < 0        on ∂K          (α is a MARGIN)
d_H(G(x), G(p)) ≤ L_G ‖x − p‖            in the inner tube
G̃_ε(x) ⊆ G(x) + Δ_ε B

L_G r + Δ_ε ≤ α,  0 < r < ρ,  K_{−r} ≠ ∅   ⟹   K_{−r} strongly invariant,
```

with the proof's key line

```
⟨n, w⟩  ≤  −α + L_G r + Δ_ε  ≤  0.
```

So `α` enters **negatively**: it is the inward margin the velocity field has on the *uneroded* boundary, and erosion plus error spend it.

## 2. What Step 2 says, and why it is wrong

Step 2 writes:

> "packet B1's restricted proximal-normal inequality gives … `⟨n_i, f_i(x_i, u)⟩ ≤ α_i + L_i r*_i` … the encroachment `Λ_i Σ_j δ_ij(r*_j) + Δ_i` is **covered by** `α_i + L_i r*_i`."

Two errors: `α_i` appears with a **positive** sign, and the encroachment is placed on the **right**-hand side as something to be covered, rather than on the left as something to be bounded.

**This is not a cosmetic slip.** Take `K = [0,1]`, so `K_{−r} = [r, 1−r]` and the outward normal at the right boundary of `K_{−r}` is `n = +1`. With `α = 0.4`, `L_G = 0.2`, `r = 0.05`, `Δ = 0.1`:

| bound | value | consequence |
|---|---|---|
| **packet:** `⟨n,w⟩ ≤ −α + L_G r + Δ` | `−0.2900` | `w < 0` — inward, invariance holds |
| **A4 Step 2:** `⟨n,f⟩ ≤ α + L r` | `+0.4100` | admits `w > 0` — **outward** |

Choose `w = +0.2050`, which satisfies A4's bound (`0.2050 ≤ 0.4100`) and violates the packet's (`0.2050 > −0.2900`). Starting at the right boundary `x = 1 − r = 0.95`, the trajectory leaves `K_{−r}` **immediately** (verified: exit at the first integration step). So A4's displayed inequality does **not** imply invariance, and Step 3's invocation of the strong-invariance theorem would not be licensed by it.

## 3. `A4.Thm1` Step 2 repaired

> **Step 2 (tangency on the eroded product) — repaired.** Let `x ∈ ∂K_{r*}` with active face set `I(x) = { i : dist(x_i, ∂K_{i,−r*_i}) = 0 }`. For `i ∈ I(x)`, let `n_i` be the outward normal at `x_i`, which is a proximal normal to `K_{i,−r*_i}`, and let `p_i` be the corresponding point of `∂K_i` with the same outward normal (packet Lemma 2's normal correspondence). Choose the shared control `u ∈ A(x)` (hypothesis 2 — the same `u` serves every active face). Then, chaining the packet's three estimates,
>
> ```
> ⟨n_i, f_i(x_i, u)⟩  ≤  −α_i + L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i  ≤  0,
> ```
>
> where the first inequality is `−α_i` (the margin on `∂K_i`) plus the envelope transport `L_i r*_i` plus the interface encroachment `Λ_i Σ_j δ_ij(r*_j)` and the implementation/model error `Δ_i`; and the second inequality is **exactly `(∗)` at `r*`**, established in Step 1.

*Justification.* On `∂K_i`, `sup_{v ∈ G_i(p_i)} ⟨n_i, v⟩ ≤ −α_i`. For `w ∈ G̃_i(x_i)`, write `w = v_x + e` with `‖e‖ ≤ Δ_i` and `‖v_x − v_p‖ ≤ L_i r*_i`; the interface defect contributes `Λ_i Σ_j δ_ij(r*_j)`. Hence `⟨n_i, w⟩ ≤ −α_i + L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i`, and `(∗)` makes this `≤ 0`. ∎

**Note on the sign of `α`.** `α_i` is a *margin*, not a *budget*: it is what the velocity field gains on the uneroded boundary, and erosion, interface defect and implementation error spend it. The condition `(∗)`, `L_i r + Λ_i Σ_j δ_ij(r_j) + Δ_i ≤ α_i`, is precisely "the spending does not exceed the margin".

## 4. What is unchanged

- **Step 1** is correct and is an exact rearrangement of `(∗)`: `L_i r*_i ≥ Λ_i Σ_j δ_ij(r*_j) + Δ_i − α_i ⟺ L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i ≤ α_i`. Its sign is consistent with the packet; only Step 2's is not.
- **Step 3** consumes only `⟨n, w⟩ ≤ 0` on `∂K_{r*}` together with `A` nonempty-closed-graph-compact-valued, and then invokes the packet's strong-invariance theorem and `E2.B2(a)`'s selector. The corrected Step 2 supplies exactly that. **The conclusion of A4.Thm1 stands verbatim.**
- **`A4.Thm2`** (Tarski least fixed point, genuineness gate, Kleene iteration, linear shadow) is unaffected and was verified correct in the original audit.
- **`A4.Ex3`** (nonconvex-control sharpness witness) is unaffected.

**Suggested register text** (proposal only — not applied):

> `A4.Thm1 | Nonlinear assume–guarantee | Monotone depth-feasibility operator; sub-solution ⟹ eroded product invariant with shared controls, via ⟨n_i,f_i⟩ ≤ −α_i + L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i ≤ 0 | PROVEN (repaired) — Step 2's display had α with the wrong sign and the encroachment on the wrong side; as written it admits outward velocities (explicit counterexample). The conclusion is unchanged. See batch 4/A4_THM1_REPAIRED.md`

**Downstream.** `A4.Thm1` is cited by `E4.Thm3`-adjacent composition material, `B_TIER_BRIDGES` B8, and Paper 2's composition chapter. All consume the conclusion, which is unchanged. The one thing to check before Paper 2 is finalised: **grep for `α` appearing with a positive sign in an erosion inequality** anywhere in `revised_articles/`. The same sign convention error is easy to repeat, and in a paper it reads as a bound that licenses unsafe velocities.

---

## 5. Verification

`reaudit/verify_e2b2a_a4_repair.py`, Part B — 17 assertions, exit 0.

| # | Claim | Result |
|---|---|---|
| B1 | packet bound `⟨n,w⟩ ≤ −α + L_G r + Δ = −0.2900 < 0`; erosion condition `0.11 ≤ 0.4` | ✓ |
| B2 | A4's bound `α + L r = +0.4100 > 0` admits outward velocity `w = +0.2050` | exits `K_{−r}` at the first step |
| B2 | that velocity violates the packet bound (`+0.2050 > −0.2900`) | ✓ |
| B3 | corrected chain `= −0.2400 ≤ 0` exactly when `L r + encroach + Δ ≤ α` (`0.16 ≤ 0.4`) | ✓ |
| B4 | Step 1 is an exact rearrangement of `(∗)`; only Step 2 is inconsistent | ✓ |
| B5 | corrected Step 2 + `(∗)` give `⟨n,w⟩ ≤ 0` on every active face ⟹ conclusion stands | ✓ |

**No errors in the Part B checks on first run.** The companion Part A (`E2_B2A_REPAIRED.md`) records one test-range error of mine, caught by the checks failing.

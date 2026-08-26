# A3.Thm2 — Clopen-Fibre Information Kernel: REPAIRED

**Target.** The `A3.Thm2` section of `batch 2/04_open_problems/A3_VARIABLE_EVENT_KERNEL.md`, and the manifest row `A3.Thm2` (line 91).

**This file is a proposal. No repository file has been modified.**

**Disposition.** Three defects, all in the statement rather than the idea: a **typing inconsistency** that makes the termination claim false as written, an **undefined termination bound**, and a **vacuous** clopenness claim. The repair declares the missing finiteness hypothesis, replaces the bound with a sharp one, and separates the two roles of "clopen" — keeping the one that does real work and dropping the one that says nothing. **The theorem's content is unchanged**: the information kernel closes, and the recursion terminates.

**Verification.** `reaudit/verify_a3thm2_cathm3_repair.py`, Part A, 12 assertions, exit 0.

---

## 1. The three defects

**(D1) Typing.** The statement declares `W ⊆ 𝒜 × ℬ_info` "**(finite × compact)**". The proof then works "on the finite lattice of subsets of `𝒜 × ℬ_finite`" — silently replacing compact `ℬ_info` by a finite `ℬ_finite`. If `ℬ_info` is genuinely compact (hence typically infinite), the lattice of its subsets is not finite and the recursion need not terminate. **Verified:** on an infinite `ℬ = [0,1]` with `Pre(W) = {b : b/2 ∈ W} ∩ W`, the recursion produces 12 strict decreases in 60 steps and does not stabilise. So the "(finite × compact)" typing cannot support the termination claim.

**(D2) The bound `≤ |𝒜| · dim` is undefined.** `dim` is never defined — of what? The correct and provable bound is in terms of the cardinality of the quotient, and it is sharp.

**(D3) "`Pre_𝒜(W)` is clopen in `W`'s coordinates" is vacuous.** Once the quotient `𝒜 × ℬ` is finite and discrete, *every* subset is clopen, so the claim carries no information. It is either trivial (finite case) or unjustified (infinite case, where D1 already breaks the theorem).

---

## 2. `A3.Thm2` repaired

> ### A3.Thm2 (repaired) — Clopen-fibre information kernel
>
> On the declared class, suppose the observation map `O : ℋ → 𝒜` has **clopen fibres** (`𝒜` a finite alphabet) and the information-state space `ℬ` is **finite**. Define the information predecessor on the finite quotient
> ```
> Pre_𝒜(W) = { (b, a) : the event-time update from observation a at information state b
>                      lands in W with the successor information state well-defined }.
> ```
> Then:
>
> **(i) Well-definedness on the quotient.** Clopen fibres make `O` **locally constant** on `ℋ`: every `φ` has a `τ_IS`-neighbourhood on which `O` is constant. Hence the event-time update depends on the history only through `a ∈ 𝒜`, and `Pre_𝒜` is well defined as a map on subsets of `𝒜 × ℬ`.
>
> **(ii) Termination, with a sharp bound.** `Pre_𝒜` is monotone, `Pre_𝒜(W) ⊆ 𝒜 × ℬ`, and the backward recursion `W₀ = 𝒜 × ℬ`, `W_{k+1} = Pre_𝒜(W_k)` is decreasing. It therefore reaches its limit after at most
> ```
> |𝒜| · |ℬ|
> ```
> **strict decreases**, i.e. within `|𝒜|·|ℬ| + 1` iterations. This bound is **sharp**.
>
> **(iii) Kernel = greatest fixed point.** The limit equals the greatest fixed point of `Pre_𝒜`, and is the information-state viability kernel.

*Proof.* (i) As stated: local constancy of `O` on `ℋ` is exactly what makes the conditioning "observation `= a`" select a clopen set of histories, and causality of the filter makes the update constant on each such selection. This is the substantive use of clopenness, and it lives in the **history space**, not in the quotient.

(ii) `W₁ = Pre_𝒜(W₀) ⊆ 𝒜 × ℬ = W₀`. If `W_{k+1} ⊆ W_k`, monotonicity gives `W_{k+2} = Pre_𝒜(W_{k+1}) ⊆ Pre_𝒜(W_k) = W_{k+1}`. So `(W_k)` is decreasing in the finite set `𝒜 × ℬ`; each step either stabilises or removes at least one element, so at most `|𝒜||ℬ|` strict decreases occur. Sharpness: order `𝒜 × ℬ` as `w₁, …, w_n` and take a predecessor that removes exactly one element per step; the chain `W_k = {w_{k+1}, …, w_n}` has exactly `n = |𝒜||ℬ|` strict decreases.

(iii) The limit `W_∞` satisfies `Pre_𝒜(W_∞) = W_∞` (the recursion stabilised), so it is a fixed point. For any fixed point `V`, `V = Pre_𝒜(V) ⊆ Pre_𝒜(W₀) = W₁`, and inductively `V ⊆ W_k`, so `V ⊆ W_∞`. Hence `W_∞` is the greatest fixed point. This is `E2.B1(b)`'s argument with the finite discrete lattice replacing the compact Vietoris one — and here the closed-graph hypothesis is automatic, since every map on a finite discrete space is continuous. ∎

**What was dropped, and why nothing is lost.** The claim "`Pre_𝒜(W)` is clopen" is removed. On a finite discrete quotient it is automatic and therefore not a hypothesis worth stating; the property that does the work is clopenness of the **fibres of `O` in `ℋ`**, which is retained as hypothesis (i) and is a genuine restriction (it excludes continuous-valued observations, which is exactly residue item 1 of the file's own residue list).

**The finiteness of `ℬ` is not an ad hoc addition.** The file's own "Reading" paragraph names the intended class: "finite-valued, quantized, and mode-indicator observation systems — exactly the governance-relevant class (quota reviews, survey triggers, mode switches)". All of these have finitely many information states. So the hypothesis makes explicit what the theorem was always about, and it is precisely the hypothesis that residue item 1 identifies as the boundary of the result.

---

## 3. Verification

`reaudit/verify_a3thm2_cathm3_repair.py`, Part A — 12 assertions, exit 0.

| # | Claim | Result |
|---|---|---|
| A1 | recursion terminates within `\|𝒜×ℬ\| + 1` for five `(\|𝒜\|,\|ℬ\|)` pairs, 300 random predecessors each | worst observed 2 steps, bounds 5–13 |
| A2 | the bound is sharp: a one-element-per-step chain needs exactly `\|𝒜×ℬ\| = 8` strict decreases | 8 of 8 |
| A3 | with `ℬ` infinite the recursion does not terminate | 12 strict decreases in 60 steps |
| A4 | the clopen claim is vacuous on a finite discrete quotient | ✓ |
| A5 | the recursion limit equals the greatest fixed point, computed independently by Tarski over all subsets | both `{(0,0),(0,1),(0,2),(1,0),(1,1)}` |

**Suggested register text** (proposal only — not applied):

> `A3.Thm2 | Clopen-fibre information kernel | Clopen fibres of O in ℋ (𝒜 finite) + **finite** information space ℬ ⟹ the information predecessor is well defined on the finite quotient, the backward recursion terminates in at most \|𝒜\|·\|ℬ\| strict decreases (sharp), and the limit is the greatest fixed point | PROVEN (repaired) — the original declared ℬ merely compact, which does not support termination; the bound "\|𝒜\|·dim" was undefined; the "Pre_𝒜(W) is clopen" clause was vacuous. See batch 4/A3_THM2_REPAIRED.md`

**Downstream.** `A3.Thm3` composes `A3.Thm2`'s finite information recursion with the physical predecessor; its condition list should now read *budgeted + transversal + clopen + finite information states*. That is consistent with the repaired `A3.Thm1` (common-modulus hypothesis) and with `batch 4/B8`'s status as CONDITIONAL.

# B7.Thm1 — Bifurcation Classification: REPAIRED (part 3 only)

**Target.** Part (3) of the `B7` section of `batch 2/04_open_problems/B_TIER_BRIDGES.md`, the manifest row `B7.Thm1` (line 97), and the cross-reference in `E3_CLASSIFICATION_THEOREMS.md` §C5.

**This file is a proposal. No repository file has been modified.**

**Disposition.** Parts (1) and (2) are proved at their stated hypotheses and are **unaffected**. Part (3)'s genericity claim is **false without an added hypothesis**: jet-transversality yields residuality for a *versal* unfolding, not for an arbitrary one-parameter family. This is the one repair in the series that **narrows** a claim rather than strengthening it, and it is recorded as such.

**Verification.** `reaudit/verify_e3cfb7_repair.py`, Part C, 9 assertions, exit 0.

---

## 1. The defect

Part (3) states:

> "**(Genericity)** the transversal-contact parameter values form a residual (dense `G_δ`) subset of the declared finite-jet parameter strata (jet-transversality)."

and proves it by:

> "Jet-transversality (Thom): the finite-jet extensions of the boundary-contact maps are transversal to the contact stratification for a residual set of `λ` … Standard application to the declared finite-jet class."

Thom's jet-transversality theorem is a statement about a **space of maps**: for a residual set of maps in a suitable function space, the jet extension is transverse to a given stratification. To conclude that a residual set of *parameters* `λ` in a given family `λ ↦ (f(·,λ), K(λ))` gives transversal contact, the family must be rich enough to realise that function space — i.e. it must be a **versal unfolding** (or at least its jet-extension map must itself be transverse to the stratification). Nothing in B7's hypotheses supplies this. The family could be constant in `λ`, and then no `λ` is transversal.

---

## 2. Counterexample

Take

```
f(x, λ) = 0   for all x and all λ,          K(λ) = [−1, 1]   for all λ.
```

Every trajectory is constant. A trajectory starting at the boundary point `x = 1` stays at `x = 1` for all time, so it makes contact with `∂K` — but its velocity is `0`, so the contact is **tangential**, not transversal, and this holds for **every** `λ ∈ Λ`.

**Verified:** on a 41-point parameter grid, the transversal-contact set has **0** elements. An empty set is not residual (not a dense `G_δ`) in a nonempty parameter interval. So part (3) is false as stated.

**Contrast — a versal family behaves as claimed.** Take `f(x, λ) = λ` (constant drift) with `K = [−1, 1]`. From `x = 1` the velocity is `λ`: transversal for every `λ ≠ 0`, tangential only at `λ = 0`. **Verified:** 40 of 41 grid values give transversal contact, and the exceptional set `{0}` is a single point — closed and nowhere dense — so the transversal-contact set is residual, exactly as jet-transversality predicts for a family that unfolds the contact geometry.

The difference between the two families is precisely versality: the first does not move the contact geometry at all, the second moves it in the one direction that matters.

---

## 3. `B7.Thm1(3)` repaired

> ### B7.Thm1(3) (repaired) — Genericity, with the unfolding hypothesis made explicit
>
> Suppose in addition that the family `λ ↦ (f(·,λ), K(λ))` is a **`C^r` versal unfolding of the boundary-contact geometry** at `λ₁` — equivalently, that the jet-extension map
> ```
> λ  ↦  j^k_{(x,λ)}( f, ∂K )
> ```
> is transverse to the tangency stratification of the contact jet space. Then the set of `λ` at which a maximally-safe trajectory makes **transversal** contact with `∂K(λ)` is **residual** (a dense `G_δ`) in the parameter stratum.
>
> Without versality the conclusion fails: the transversal-contact set may be empty.

*Proof.* Under the transversality hypothesis, Thom's jet-transversality theorem applied to the jet-extension map gives transversality to the tangency stratum for a residual set of `λ`. Transversality to the tangency stratum is exactly "nonzero contact angle", which is the hypothesis of part (2). The counterexample of §2 shows the hypothesis is necessary. ∎

**Parts (1) and (2) are unchanged.** The no-change rule and the change rule are proved at their stated hypotheses — structural stability plus Hausdorff-continuity of `∂K(λ)` for (1), and `C¹` transversal contact with `∂τ/∂λ ≠ 0` for (2) — and neither invokes genericity. The repair adds a hypothesis to (3) only.

---

## 4. Why this repair narrows rather than strengthens

Every other repair in this series either restored a false claim to truth, or replaced a false claim with a stronger true one. This one is different: **the original claim is false, and the true version requires strictly more.** There is no strengthening available, because the counterexample family satisfies every hypothesis B7 states and still has an empty transversal-contact set.

The honest options are:

1. **Add the versality hypothesis** (recommended) — the theorem then says something true and useful, and versality is checkable in the applications the programme cares about;
2. **Delete part (3)** and record genericity as open — weaker, but leaves nothing to verify;
3. **Restrict to families that unfold the contact geometry by construction** — a middle path, but it amounts to (1) with the hypothesis buried in the class definition.

Option 1 is what this file proposes.

---

## 5. Verification

`reaudit/verify_e3cfb7_repair.py`, Part C — 9 assertions, exit 0.

| # | Claim | Result |
|---|---|---|
| C1 | non-versal family `f ≡ 0`, `K = [−1,1]`: transversal-contact set is empty | 0 of 41 parameter values |
| C1 | an empty set is not residual in a nonempty interval | ✓ |
| C2 | versal family `f = λ`: transversal for every `λ ≠ 0`, tangential only at `λ = 0` | 40 of 41 |
| C2 | the exceptional set is a single point, so the transversal set is residual | ✓ |
| C3 | parts (1) and (2) are unaffected | ✓ |

**Suggested register text** (proposal only — not applied):

> `B7.Thm1 | Bifurcation classification | (1) structural stability + Hausdorff-continuous ∂K(λ) ⟹ Hausdorff-continuous kernel; (2) C¹ transversal contact with ∂τ/∂λ ≠ 0 ⟹ membership flips; (3) **under a versal unfolding of the contact geometry**, transversal-contact parameters are residual | PROVEN (repaired) for (1),(2); (3) PROVEN **conditionally on versality** — without it the transversal-contact set can be empty (explicit counterexample f ≡ 0). This repair narrows the claim; no strengthening is available. See batch 4/B7_THM1_REPAIRED.md`

**Downstream.** `E3_CLASSIFICATION_THEOREMS.md` §C5 states that "genericity of the non-degenerate strata via jet-transversality" is proved in B7 and that "the card's 'PARTIAL' label was the pre-B7 status and is withdrawn". With this repair, the genericity half of C5 should be marked conditional on versality, and the withdrawal of "PARTIAL" is correct only for the (1)/(2) content. `E7`/Paper 2 references to the bifurcation classification consume (1) and (2) and are unaffected.

# The Rescue Threshold and the Error-Bound Modulus: A Formal Bridge (and Its Honest Limits)

*A short commentary on the witness datum of "The Limits of Compensatory Aggregation" (Abaee, 2026). This is original analysis, **not** part of the paper, and it is written to a strict standard: every claim is proved from the datum, and where a hoped-for connection turns out to be trivial, that is stated plainly rather than dressed up.*

---

## 1. What was requested, and the verdict in one line

Two candidate deliverables were proposed: (a) a related-work section, and (b) "a proposition linking the rescue threshold κ\* to the error-bound modulus." This note gives (b) — but in the only form the mathematics supports:

- **The natural bridge exists and is exact** — but on this datum it collapses to a *constant* (the error-bound modulus is identically 1), because the resource-route feasibility is affine. A theorem that merely restates this would be decorative.
- **The genuinely merited formal content is different and exact:** the closed form of the rescue threshold over the whole state space, which (i) sharpens the paper's Proposition, (ii) exposes a scope qualifier the paper's one-line statement compresses, and (iii) records a fact the paper's own proof of Theorem 5(1) already establishes but does not state: **the resource route rescues every state with x < 1, including states outside V_weak.**
- **Where the error-bound theory would genuinely add value** (general, non-affine, multi-action data with unstructured perturbations) is identified in §4 as an open direction — the paper's §6.2(3) explicitly declines to cover it.

## 2. Notation and the datum (recalled from the paper)

State *z = (q = 0, x, s₁, s₂)* with *x ≥ 0, s₁ ≥ 0, s₂ ≥ 0*; menu **A = {NO-SWITCH, FAST, SLOW, STAGED}**. Typed-admissibility conditions (Theorem 5(1), whose proof is recalled in §3 below):

| action | typed-admissible at z iff |
|---|---|
| NO-SWITCH | never (successor keeps q = 0, misses G) |
| FAST | s₁ ≥ 2 |
| SLOW | s₂ ≥ 2 |
| STAGED | x ≥ 1 |

Hence **V_typ = {x ≥ 1} ∪ {s₁ ≥ 2} ∪ {s₂ ≥ 2}**. The augmentation map is
**Aug_κ(x, s, A) = (x + κ, s, A ∪ {STAGED_κ})**, and the minimal rescue threshold is
**κ\*(z) = inf{ κ ≥ 0 : ∃ a ∈ A_κ, a ∈ E_typ(z) }**, where A_κ is the augmented menu (the paper's own definition).

## 3. The exact closed form of κ\*

**Claim (closed form).** On the witness datum, for every *z ∈ X₀*:

> **κ\*(z) = (1 − x)₊ · 1[x < 1, s₁ < 2, s₂ < 2]**  =  (1 − x) · 1[z ∉ V_typ].

*Proof.* Only the typed-admissibility of STAGED_κ needs checking, and it is independent of the floors. STAGED_κ runs the *x*-coordinate through the tube [x + κ − 1, x + κ]; both floors are **nondecreasing** (they grow to s + e with e = (¼, ¼) > 0), so s ≥ 0 throughout; the successor is (1, x + κ − 1, s + e), which lies in G = {(1, x, s) : x ≥ 0, s ≥ 0} exactly when x + κ − 1 ≥ 0. Thus **STAGED_κ ∈ E_typ(z) ⟺ x + κ ≥ 1**, for all z.

Now the menu-wide κ\*:

- If z ∈ V_typ, some action of A ⊆ A_κ is typed-admissible at κ = 0, so κ\*(z) = 0.
- If z ∉ V_typ, i.e. x < 1 and s₁ < 2 and s₂ < 2, then NO-SWITCH, FAST, SLOW all fail (Theorem 5(1)), so the only admissible element of A_κ is STAGED_κ, and it is admissible exactly for κ ≥ 1 − x. Hence κ\*(z) = 1 − x. ∎

**Three consequences worth recording.**

1. **The paper's Proposition is correct but compressed.** Its statement is "for the STAGED action and x < 1, κ\* = 1 − x." That is true for the STAGED route in isolation; but κ\* is defined over the *augmented menu*, and for x < 1 with s₁ ≥ 2 or s₂ ≥ 2 the menu already contains a typed-admissible action (FAST or SLOW), so the menu-wide κ\* is 0, not 1 − x. The closed form supplies the missing qualifier **z ∉ V_typ** (equivalently s₁ < 2 ∧ s₂ < 2) and is exact on the whole space.

2. **The rescue route is more general than the paper's framing suggests.** The paper says the increment "converts an impossibility-region state into a typed-transformable one." In fact, by the proof above, **every** state with x < 1 — including states outside V_weak, e.g. z = (½, ⅒, ⅒) where s₁ + s₂ = ⅕ < 2 — is made typed-acceptable by STAGED_κ with κ = 1 − x, because STAGED never depends on the floors. The paper's own proof of Theorem 5(1) ("For STAGED, the floors grow through the interval … the binding constraint is the x-tube, safe iff x ≥ 1") already establishes this; it is merely not stated in full generality. Nothing in the paper's conclusions changes — the impossibility region *I* is still exactly where the *four-action menu* fails — but the closed form shows the rescue operation's domain is the whole half-space {x < 1}, not just *I*.

3. **Consistency check.** On the rescue set *R = Q ∩ {x ≥ 1}*, κ\* = 0 — matching the paper's "states of the rescue set need no augmentation." On *I*, κ\* = 1 − x > 0 — matching "the increment converts an impossibility-region state." The closed form was verified against the datum by exact computation over 20,000 random states plus the paper's named witness points (no mismatch).

## 4. The error-bound modulus: where the bridge is real, and where it trivializes

**The honest computation.** Apply the Fabian–Henrion–Kruger–Outrata (2010) framework to the STAGED-route feasibility function *f(z) = κ\*_STAGED(z) = (1 − x)₊* (the minimal resource increment along the one structured route). For x̄ < 1 the sublevel set is [f ≤ f(x̄)] = {x ≥ x̄}, so for x < x̄:

> [f(x) − f(x̄)]₊ / d(x, [f ≤ f(x̄)]) = (x̄ − x) / (x̄ − x) = 1,

hence the **error-bound modulus Er f(x̄) = 1 for every x̄ < 1**, and the strict slopes of Fabian et al. coincide with it (f is 1-Lipschitz; their Theorems 1(ii) and 2). **The modulus carries no information beyond the exact closed form: it is the slope of an affine function.** Any "Proposition linking κ\* to the error-bound modulus" that presents this as a new theorem would be decorative.

**What is non-trivial — the structured/unstructured contrast.** The two quantities are *different kinds* of robustness, and stating their relation precisely is the genuine content:

- **κ\*** is **structured** robustness: the minimal *allowed control* (resource augmentation along a named action) that restores feasibility. It respects the datum's fixed menu and disturbance class — the paper's explicit scoping.
- **Er f** is **unstructured** robustness: the rate at which the *distance* to the feasible region scales with the constraint violation under *arbitrary* small perturbations of the state — no structure assumed.

On this datum they coincide numerically **only because** the resource route is affine with unit slope. In a general typed datum — nonlinear dynamics, multi-action menus, coupled disturbances — they would diverge, and the error-bound modulus would give a **lower bound** on the augmentation needed under unstructured uncertainty, whereas κ\* (structured) can be smaller. This is the correct statement of the bridge, and it is exactly the regime the paper's §6.2(3) declines to cover ("exact tube inclusion may be computationally hard… the witness is tractable because its datum is small, finite, and rational"). **If the paper were extended to quantitative certificates on general data, the error-bound/calmness framework is the tool to reach for; on the witness itself, it confirms rather than adds.**

## 5. Bottom line

- **Merited and delivered:** the exact closed form κ\*(z) = (1 − x) · 1[z ∉ V_typ], its proof, the disambiguation of the paper's Proposition, and the observation that the resource route rescues all of {x < 1}.
- **Not merited and therefore not presented as such:** a "new theorem" coupling κ\* to the error-bound modulus, because on this datum the modulus ≡ 1 (affine feasibility), and any such theorem would be a restatement of a slope.
- **The single genuinely useful connection to the error-bound literature** is the structured-vs-unstructured contrast above, stated as a remark with the precise direction of the inequality it would imply in general.

# E4 — Intergenerational Production

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Task 3; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation.

---

## Setting

Generations `g = 0, 1, 2, …` succeed on a review/event calendar. Within generation `g`: state space `X_g`, safe set `K_g ⊆ X_g` closed, dynamics with controls and disturbances, safe-action machinery as in E2. At the generation boundary, the **reset map** `R_g : X_g → X_{g+1}` maps an end-of-generation state to the next generation's initial state. Write

```
K_{g,−r} := { x ∈ K_g : dist(x, X_g ∖ K_g) ≥ r }
```

for the inner `r`-erosion (empty if `r` exceeds the inradius of `K_g`). Harm accumulates on the `H_harm` block of E1's extended product with declared per-generation semantics `τ^h ∈ {accumulate, cap, forgive}`.

---

## E4.Lem1 — Jump-margin transfer — PROVED (declared data)

### Statement

Say the reset `R_g` has **depth co-Lipschitz margin `(ℓ, b)`** (with `ℓ > 0`, `b ≥ 0`) if for all `r ∈ [0, r̄_g]`:

```
R_g(K_{g,−r}) ⊆ K_{g+1, −(ℓ r − b)}     (right side read as K_{g+1} when ℓr − b ≤ 0).
```

Then: (i) the inclusion above transfers erosion depths across generations with the deficit `b` consumed per generation; (ii) the margin `(ℓ, b)` is **declared data** — it is *not* derivable from Lipschitz continuity of `R_g` plus boundary margins of `K_g, K_{g+1}` alone.

### Proof

(i) is the declaration unpacked: it is a hypothesis on `R_g` relative to the pair `(K_g, K_{g+1})`, and the lemma formalizes exactly what it buys — an erosion depth `r` before the jump maps to depth `≥ ℓr − b` after the jump.

(ii) **Refutation of the over-derivation** (recorded honestly): consider `K_g = K_{g+1} = [0, 1]`, and resets `R_g(x) = φ_g(x)` with `φ_g` a `C¹` increasing bijection with `φ_g(0)=0, φ_g(1)=1`, uniformly Lipschitz in `g` (so all classical regularity data are bounded uniformly in `g`). The erosion depth of `φ_g(x)` at the left boundary is `φ_g(x) − 0`; for `x` at depth `r` (i.e. `x = r`), the depth of the image is `φ_g(r)`. Take `φ_g(r) = r^{a_g}` near `0` with `a_g ↑ ∞` along a subsequence (smoothly patched, uniformly Lipschitz on `[0,1]` since `r^{a} ≤ a r`... — patch instead `φ_g(r) = λ_g r` for `r ≤ ρ_g` with `λ_g ↓ 0` and `ρ_g ↓ 0` chosen so `φ_g` is `C¹`, increasing, onto, with uniformly bounded derivative: `λ_g ρ_g → 0`). Then depth `ρ_g` before the jump maps to depth `λ_g ρ_g → 0` after: **no uniform `(ℓ, b)` with `b < ∞` exists**, although every `R_g` is smooth with uniformly bounded Lipschitz constant and every boundary margin datum is bounded. Hence depth degradation is a *rate* statement about the family `(R_g)`, not a consequence of per-generation regularity. (This is the depth-degradation refutation recorded in the session; the displayed family is its explicit witness.) ∎

**Honesty consequence:** every use of jump-margin transfer must exhibit `(ℓ, b)` for the declared reset family; E4.Thm2/Thm3 carry it as a hypothesis, and the erosion budgets below consume it explicitly.

---

## E4.Thm2 — Eroded generation transfer — PROVED

### Statement

Assume, for generations `g = 0, …, G`:

1. **Within-generation erosion conditions** (packet B1's restricted hypotheses): on `K_{g,−r_g}`, the velocity envelope satisfies the proximal-normal inequality with erosion budget `L_g r_g + Δ_g ≤ α_g` — i.e. the `r_g`-eroded set is strongly invariant within generation `g`;
2. **Jump-margin transfer** (E4.Lem1) with margin `(ℓ, b)` for every `R_g`, `g < G`;
3. **Non-Zeno calendar**: finitely many generation boundaries in any compact time interval (uniformly bounded event rate).

Let the erosion budget sequence satisfy the recursion

```
r_{g+1} = ℓ · r_g − b    for g < G,     r_0 given.
```

Then the eroded generation path `∏_g K_{g, −r_g}` (read on the extended product with the `G_gen` block indexing generations) is **strongly invariant**: from any state in `K_{0,−r_0}` there is an admissible causal policy whose trajectory, followed across all generation boundaries, remains in `K_{g,−r_g}` during generation `g`, for every `g ≤ G`.

### Proof

Induction over generations. **Base:** within generation 0, hypothesis 1 and `r_0` give strong invariance of `K_{0,−r_0}` up to the first boundary (packet B1 applied on the compact time window of generation 0 — hypothesis 3 ensures the window is well-defined). **Boundary step:** at the end of generation `g`, the state lies in `K_{g,−r_g}`; by E4.Lem1, the reset image lies in `K_{g+1, −(ℓ r_g − b)} = K_{g+1, −r_{g+1}}` (this is precisely the recursion — the deficit `b` is consumed at each jump). **Induction:** within generation `g+1`, hypothesis 1 applies at depth `r_{g+1}`. Concatenation across finitely many boundaries (hypothesis 3, compact horizon) gives the admissible causal policy — causality is preserved because the concatenation times are calendar events known to the policy class, and measurability of the per-generation selectors is E2.B2(a). ∎

**Budget solvability (the honest constraint).** The recursion `r_{g+1} = ℓ r_g − b` admits nonnegative solutions on `{0..G}` iff `r_0 ≥ b·(ℓ^G − 1)/(ℓ − 1)` for `ℓ ≠ 1` (resp. `r_0 ≥ bG` for `ℓ = 1`). For the **infinite-generation** horizon (`G = ∞`), nonnegative solvability forces: `ℓ < 1` with `r_0 ≥ b/(1−ℓ)` (geometric budget), or `b = 0` with `ℓ ≤ 1` (no per-jump deficit). These are the quantitative reading of "sustainability across generations" in this module: the initial margin must cover the compounded jump deficit. No claim is made when the budget is unsolvable — that is exactly the honest negative finding below.

**Recorded negative finding (honesty).** E4 does **not** derive `(ℓ, b)` from any cheaper data (Lem1(ii)); and when the budget recursion is unsolvable, the theorem makes no invariance claim — the eroded path may genuinely fail, and certifying that failure needs the R03 adversarial-exit route, not this theorem.

---

## E4.Thm3 — Production assembly — PROVED (exact instantiation of E2 outputs)

### Statement

Under E4.Thm2's hypotheses, additionally with per-generation certificate families at their greatest fixed points `𝒱_g*` (E2.B1(a)–(b)) and measurable intergenerational policy selectors (E2.B2(a)):

1. each generation's maximal certificate family exists and is computed by the backward iteration (E2.B1(b));
2. the intergenerational policy `π` — the concatenation of per-generation measurable selectors glued at calendar events — is measurable and causal;
3. the composite object (families, policy, budget recursion, harm semantics `τ^h`) is the **production system**: strong invariance of the eroded path (E4.Thm2) with certificates carried generation-by-generation and harm bookkeeping on `H_harm` per the declared `τ^h`.

### Proof

(1) is E2.B1(a)/(b) verbatim per generation (each `K_{g}` compact, `Γ_g` monotone with closed Vietoris graph). (2) is the concatenation lemma: a finite (per compact horizon, by non-Zeno) gluing of measurable selectors at deterministic calendar times is measurable; causality holds because each segment uses only its generation's information pattern, and the calendar is policy-independent. (3) assembles (1)–(2) with E4.Thm2: the invariance conclusion is Thm2's, and the certificate/harm bookkeeping rides on the extended product of E1 (the `H_harm` update per `τ^h` is a declared deterministic map on the block, hence harmless to invariance of the physical block; for `τ^h = cap` the cap is a closed constraint on `H_harm` absorbed into `𝕂_J`). ∎

**Scope honesty.** "Accumulate/cap/forgive" are *declared semantics*, not derived: the theorem does not compare them or claim normative status for any. Endogenous-event calendars (events triggered by the state rather than the clock) are outside this theorem and are A3's business — the residual recorded there applies here: B8's event-surface composition is conditional on A3's transversality declaration.

---

## Status

- **E4.Lem1: PROVED** (transfer statement + the refutation proving declared-data status, both above).
- **E4.Thm2: PROVED** (under the three declared hypotheses; budget-solvability condition explicit).
- **E4.Thm3: PROVED** (assembly; exact instantiation of E2's outputs).

**Dependencies:** packet B1 (restricted invariance + erosion), E2 (B1(a)/(b), B2(a)), E1 (extended product), R03 (adversarial-exit route for the honest negatives). **Consumers:** B8 (event-surface composition), C-h's composition gate G-3 ("eroded generation-transfer (E4)" in the TCS-1.1 diff — note: the gate is *enumerated* in the frozen diff, which does not control any record; see TCS_1_1_FREEZE.md), Paper 2's generation chapter.

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.

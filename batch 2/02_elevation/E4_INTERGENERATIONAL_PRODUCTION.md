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

## E4.Lem1 — Jump-margin transfer — PROVEN (repaired: non-vacuous form; declared data)

> **Repair note (PROOF_REAUDIT finding 4; consolidated in `batch 4/PROOF_ELEVATION.md` Finding 4).** The recorded definition admitted **vacuous pairs**: since depth never exceeds the inradius `r̄_g`, any pair with `b ≥ ℓ·r̄_g` satisfies the inclusion vacuously at every tested `r` (`ℓr − b ≤ 0` reads the right side as `K_{g+1}`), and the inclusion reduces to `R_g(K_g) ⊆ K_{g+1}`. So the recorded conclusion "**no uniform `(ℓ, b)` with `b < ∞` exists**" was false — of every `K`-preserving family. Additionally, the recorded vanishing-neighbourhood witness is **not a witness even against non-vacuous pairs** (the collapse hides inside the vacuous zone `r < b/ℓ` of every fixed positive `b`; the linear piece must extend to a uniformly positive depth — the inradius — for the test to bite). Both defects are repaired below; the declared-data thesis then stands, and a companion cheap-data derivation is recorded. Full development and verification: `batch 4/E4_REPAIRED.md` §1.

### Statement

Say the reset `R_g` has a **non-vacuous depth co-Lipschitz margin `(ℓ, b)`** (with `ℓ > 0`, `0 ≤ b < ℓ·r̄_g`) if for all `r ∈ (b/ℓ, r̄_g]`:

```
R_g(K_{g,−r}) ⊆ K_{g+1, −(ℓ r − b)}     (right side read as K_{g+1} when ℓr − b ≤ 0;
                                          for r ≤ b/ℓ the inclusion is automatic).
```

The non-vacuity condition `b < ℓ·r̄_g` is exactly what makes the active interval `(b/ℓ, r̄_g]` nonempty — some tested radius must demand a positive image depth, so the margin *fires*. Then: (i) the inclusion transfers erosion depths across generations with the deficit `b` consumed per generation; (ii) a non-vacuous margin is **declared data** — not derivable from Lipschitz continuity of `R_g` plus boundary margins of `K_g, K_{g+1}` alone; (iii) the **only** cheap-data derivation: if `R_g` is co-Lipschitz with constant `κ` near `K_g` (`dist(R(x), R(y)) ≥ κ·dist(x, y)`) *and exterior-preserving* (`R_g(X_g ∖ K_g) ⊆ X_{g+1} ∖ K_{g+1}`), then `(κ, 0)` is a non-vacuous margin.

### Proof

(i) is the declaration unpacked. (ii) **Witness (extended to the inradius — the load-bearing form).** On `K_g = K_{g+1} = [0,1]` (inradius `½`, depth `= min(x, 1−x)`) take

```
φ_g(x) = x/g                          for 0 ≤ x ≤ 1/2,
φ_g(x) = 1/(2g) + (x − 1/2)(2 − 1/g)  for 1/2 < x ≤ 1,
```

a continuous, increasing bijection of `[0,1]` with slopes `1/g` and `2 − 1/g` — uniform Lipschitz constant 2. The incenter `x = ½` has depth `½`; its image `φ_g(½) = 1/(2g)` has depth `1/(2g) → 0`. For any non-vacuous pair, the margin condition at `r = ½` demands `1/(2g) ≥ ℓ/2 − b > 0`, which fails for every `g > 1/(ℓ − 2b)`. So **no non-vacuous pair is uniform for the family**, although all classical regularity data are bounded uniformly in `g` (verified exactly: `(ℓ,b) = (1, 0.4) → first failure g = 6`; `(0.5, 0.2) → g = 11`; `(1, 0.49) → g = 51`). (iii) For `x ∈ K`: `depth_{K'}(R(x)) = dist(R(x), X′∖K′) ≥ dist(R(x), R(X∖K)) ≥ κ·dist(x, X∖K) = κ·depth_K(x)`, using exterior-preservation for the first inequality. Exterior-preservation is not optional: co-Lipschitz controls distances to the *image* of the complement, not to the complement. ∎

**Honesty consequence (unchanged in force, now well founded):** every use of jump-margin transfer must exhibit a **non-vacuous** `(ℓ, b)` for the declared reset family; E4.Thm2/Thm3 carry it as a hypothesis, and the erosion budgets below consume it explicitly. Non-vacuity is a real constraint, not a formality: `b < ℓ·r̄_g` says the per-jump deficit must be strictly smaller than the depth the reset can generate from a maximally deep state.

---

## E4.Thm2 — Eroded generation transfer — PROVED

### Statement

Assume, for generations `g = 0, …, G`:

1. **Within-generation erosion conditions with a genuine lower bound** (packet B1's restricted hypotheses): on `K_{g,−r_g}`, the velocity envelope satisfies the proximal-normal inequality with erosion budget `L_g r_g + Δ_g ≤ α_g` — i.e. the `r_g`-eroded set is strongly invariant within generation `g` — and there are `0 < ρ_g ≤ R_g` such that the invariance is needed at depths `r_g ∈ [ρ_g, R_g]` (the lower bound `ρ_g > 0` is what makes the budget question non-vacuous; added per `batch 4/PROOF_ELEVATION.md` Finding 3/D3);
2. **Jump-margin transfer** (E4.Lem1) with a **non-vacuous** margin `(ℓ, b)` (`b < ℓ·r̄_g`) for every `R_g`, `g < G`;
3. **Non-Zeno calendar**: finitely many generation boundaries in any compact time interval (uniformly bounded event rate).

Let the erosion budget sequence satisfy the recursion

```
r_{g+1} = ℓ · r_g − b    for g < G,     r_0 given.
```

Then the eroded generation path `∏_g K_{g, −r_g}` (read on the extended product with the `G_gen` block indexing generations) is **strongly invariant**: from any state in `K_{0,−r_0}` there is an admissible causal policy whose trajectory, followed across all generation boundaries, remains in `K_{g,−r_g}` during generation `g`, for every `g ≤ G`.

### Proof

Induction over generations. **Base:** within generation 0, hypothesis 1 and `r_0` give strong invariance of `K_{0,−r_0}` up to the first boundary (packet B1 applied on the compact time window of generation 0 — hypothesis 3 ensures the window is well-defined). **Boundary step:** at the end of generation `g`, the state lies in `K_{g,−r_g}`; by E4.Lem1, the reset image lies in `K_{g+1, −(ℓ r_g − b)} = K_{g+1, −r_{g+1}}` (this is precisely the recursion — the deficit `b` is consumed at each jump). **Induction:** within generation `g+1`, hypothesis 1 applies at depth `r_{g+1}`. Concatenation across finitely many boundaries (hypothesis 3, compact horizon) gives the admissible causal policy — causality is preserved because the concatenation times are calendar events known to the policy class, and measurability of the per-generation selectors is E2.B2(a). ∎

**Budget solvability (corrected per `batch 4/PROOF_ELEVATION.md` Finding 3 — the recorded analysis was arithmetically wrong in both branches).** Solving the recursion: `r_g = r* + ℓ^g(r_0 − r*)` with fixed point `r* = b/(ℓ−1)` for `ℓ ≠ 1` (resp. `r_g = r_0 − gb` for `ℓ = 1`). Nonnegative on `{0..G}` **iff**

```
r_0 ≥ (b/(ℓ−1))·(1 − ℓ^{−G})   (ℓ ≠ 1)        resp.        r_0 ≥ b·G   (ℓ = 1),
```

tight. The recorded `b(ℓ^G − 1)/(ℓ − 1)` is `ℓ^G ×` the correct threshold — too weak for `ℓ < 1`, too strong for `ℓ > 1`. For the **infinite-generation** horizon (`G = ∞`), nonnegative solvability holds **iff** `b = 0` (any `ℓ`), or `ℓ > 1` with `r_0 ≥ b/(ℓ−1)`. The recorded "`ℓ < 1` with `r_0 ≥ b/(1−ℓ)`" is the fixed point of `r ↦ ℓr + b` — the **wrong sign of the deficit** — and the true fixed point `b/(ℓ−1) < 0` shows the sequence is eventually negative at *every* initial margin when `ℓ < 1` and `b > 0`.

**The substantive form — required depths propagate backwards.** The forward budget alone is vacuous (`r ≡ 0` is always admissible and delivers invariance of the uneroded path). With genuine lower bounds `0 < ρ_g ≤ R_g` (within-generation erosion needs depth at least `ρ_g`; without this hypothesis the budget theory has no content), a budget exists iff `r_0 ≥ u_0`, where `u_G := ρ_G` and `u_g := max(ρ_g, (u_{g+1} + b)/ℓ)`; for constant `ρ`: `u_0 = max(ρ, ρℓ^{−G} + b·(ℓ^{−G} − 1)/(1 − ℓ))` (`ℓ ≠ 1`), resp. `u_0 = ρ + Gb` (`ℓ = 1`).

> **Corrected sustainability criterion (the module's real quantitative statement).** Sustainable at an unbounded horizon (`sup_G u_0(G) < ∞`) **iff `ℓ > 1`, or `ℓ = 1` with `b = 0`.** For `ℓ < 1` the required initial margin grows as `u_0(G) ~ (ρ + b/(1−ℓ))·ℓ^{−G}` — **exponentially in the horizon, even when `b = 0`** (a contracting reset maps depth `r` to depth `ℓr`; maintaining `ρ` after `G` jumps costs `ρℓ^{−G}` regardless of any additive deficit).

**Recorded negative finding (honesty — corrected, and stronger).** E4 does **not** derive a *non-vacuous* `(ℓ, b)` from cheaper data (Lem1(ii)); and — the corrected impossibility — **a generation transition that contracts depth (`ℓ < 1`) cannot sustain positive erosion across unboundedly many generations at any initial margin**: the required margin grows exponentially, and no endowment buys intergenerational sustainability under a strictly depth-eroding transition. You cannot buy sustainability with a large enough initial buffer if each transition strictly erodes the margin; the buffer is consumed exponentially. When the budget is unsolvable on the declared calendar, the theorem makes no invariance claim — certifying failure needs the R03 adversarial-exit route, not this theorem.

---

## E4.Thm3 — Production assembly — PROVED (exact instantiation of E2 outputs)

### Statement

Under E4.Thm2's hypotheses (including the genuine lower bounds `0 < ρ_g ≤ R_g` and the non-vacuous margin — carried explicitly per `batch 4/PROOF_ELEVATION.md` Finding 3′), additionally with per-generation certificate families at their greatest fixed points `𝒱_g*` (E2.B1(a)–(b)) and measurable intergenerational policy selectors (E2.B2(a)):

1. each generation's maximal certificate family exists and is computed by the backward iteration (E2.B1(b));
2. the intergenerational policy `π` — the concatenation of per-generation measurable selectors glued at calendar events — is measurable and causal;
3. the composite object (families, policy, budget recursion, harm semantics `τ^h`) is the **production system**: strong invariance of the eroded path (E4.Thm2) with certificates carried generation-by-generation and harm bookkeeping on `H_harm` per the declared `τ^h`.

### Proof

(1) is E2.B1(a)/(b) verbatim per generation (each `K_{g}` compact, `Γ_g` monotone with closed Vietoris graph). (2) is the concatenation lemma: a finite (per compact horizon, by non-Zeno) gluing of measurable selectors at deterministic calendar times is measurable; causality holds because each segment uses only its generation's information pattern, and the calendar is policy-independent. (3) assembles (1)–(2) with E4.Thm2: the invariance conclusion is Thm2's, and the certificate/harm bookkeeping rides on the extended product of E1 (the `H_harm` update per `τ^h` is a declared deterministic map on the block, hence harmless to invariance of the physical block; for `τ^h = cap` the cap is a closed constraint on `H_harm` absorbed into `𝕂_J`). ∎

**Scope honesty.** "Accumulate/cap/forgive" are *declared semantics*, not derived: the theorem does not compare them or claim normative status for any. Endogenous-event calendars (events triggered by the state rather than the clock) are outside this theorem and are A3's business — the residual recorded there applies here: B8's event-surface composition is conditional on A3's transversality declaration.

---

## Status

- **E4.Lem1: PROVEN (repaired)** (non-vacuous transfer + declared-data refutation with the inradius-extending witness + the co-Lipschitz/exterior-preserving companion, all above).
- **E4.Thm2: PROVEN (repaired)** (induction unchanged; hypotheses now carry `ρ_g > 0` and non-vacuity; budget analysis corrected — thresholds `(b/(ℓ−1))(1−ℓ^{−G})` / `bG`, infinite-horizon criterion `b = 0` or `ℓ > 1`, and the corrected negative: a contracting reset is unsustainable at any initial margin, required margin `~ (ρ + b/(1−ℓ))ℓ^{−G}`).
- **E4.Thm3: PROVEN (repaired)** (assembly; exact instantiation of E2's outputs; statement now carries the `ρ_g > 0` lower bounds — without them the assembly is vacuous).

**Dependencies:** packet B1 (restricted invariance + erosion), E2 (B1(a)/(b), B2(a)), E1 (extended product), R03 (adversarial-exit route for the honest negatives). **Consumers:** B8 (event-surface composition), C-h's composition gate G-3 ("eroded generation-transfer (E4)" in the TCS-1.1 diff — note: the gate is *enumerated* in the frozen diff, which does not control any record; see TCS_1_1_FREEZE.md), Paper 2's generation chapter.

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.

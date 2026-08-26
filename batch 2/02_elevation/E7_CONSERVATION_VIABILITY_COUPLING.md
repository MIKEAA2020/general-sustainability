# E7 — Conservation–Viability Coupling (F1 + F3)

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Task 4; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation.

---

## Setting: the moiety ledger

A **moiety** `L` is a conserved extensive quantity tracked by a ledger: the state component `q_L` (the stock) obeys

```
q_L(t) = q_L(0) + ∫₀ᵗ [F(s) − D(s)] ds,
```

with `F` the inflow (regeneration/transfer-in; declared bounds `F ∈ [F⁻, F⁺]`, with `F⁻ ≥ 0` in the regeneration case) and `D` the outflow (extraction; declared admissible set `D ∈ [D⁻, D⁺]`, `D⁻ ≥ 0` the obligatory minimum). The ledger identity (conservation; packet B6's typed telescoping) is the *only* dynamical fact used: **no model of the rest of the system enters the theorems.** Write

- `F⁺_T` := the maximal cumulative inflow on `[0,T]` (`∫₀^T F⁺ ds`),
- `D⁻_T` / `D⁺_T` := the minimal / maximal cumulative obligatory outflow,
- `Viab_T(K)` := the robust viability kernel of a constraint set `K` on horizon `T` (policies vs. declared disturbance/flow classes as above).

---

## E7.Thm1 — Moiety-barrier production rules — PROVEN

### (a) Balanced-budget inner rule

**Statement.** If the policy class admits the *budget commitment* `∫₀^T D ds ≤ D_T` (a declared admissible budget, e.g. `D ≡ D⁻` gives `D_T = D⁻_T`) and `F ≥ 0` (nonnegative regeneration — a declared conservation fact), then

```
{ x : q_L(x) ≥ D_T }  ⊆  Viab_T({ q_L ≥ 0 }).
```

**Proof.** For any admissible policy honoring the commitment and any flow realization with `F ≥ 0`:

```
q_L(t) = q_L(0) + ∫₀ᵗ F ds − ∫₀ᵗ D ds  ≥  q_L(0) − ∫₀ᵗ D ds  ≥  q_L(0) − D_T ≥ 0    for all t ∈ [0,T],
```

using the ledger identity, `F ≥ 0`, and the commitment. The floor constraint `{q_L ≥ 0}` is therefore maintained on `[0,T]` from every state with `q_L(0) ≥ D_T`. ∎

**Reading.** The rule *produces a kernel inner bound from flux data alone*: the stock covering the committed total outflow is sufficient for floor-viability — regardless of any other structure of the system. It deliberately ignores regeneration (`F` is only used as `≥ 0`), which is why it is conservative whenever regeneration is material.

### (b) Obligatory-outflow emptying rule (automatic adversarial-exit certificate)

**Statement (split per `batch 4/PROOF_ELEVATION.md` Finding 16 — the two hypothesis disjuncts support different conclusions).** Suppose the outflow has the uniform obligatory minimum `D(t) ≥ γ > 0` (policy-independent). Then:

- **(b1) Robust-kernel emptying (adversarial-exit certificate).** If `F ≡ 0` is an admissible inflow realization (or the worst admitted net inflow on `[0,T]` is `≤ 0`), then `Viab_T({q_L ≥ 0}) = ∅` for `T > q_L(0)/γ`. The pair (obligatory drain `γ`, exit time `q_L(0)/γ`) is an **adversarial-exit certificate** in the sense of R03.Thm1's first branch: the nonviability judgment is *certified* (sound) by conservation data alone.
- **(b2) Pathwise exit.** If additionally `F ≤ 0` for **every** admissible realization, then **every** trajectory satisfies `q_L(t) ≤ q_L(0) − γt` and exits the floor by time `q_L(0)/γ`.
- **(b3) Sharp exit time under a general inflow bound.** If `F ≤ F⁺`, every trajectory exits by `q_L(0)/(γ − F⁺)` when `γ > F⁺`, and need not exit at all when `γ ≤ F⁺`.

**Proof.** (b1) Robust viability requires safety against every admissible realization, in particular `F ≡ 0`; under it `q_L(t) ≤ q_L(0) − γt < 0` for `t > q_L(0)/γ`, so no policy is safe. (b2) `q_L(t) = q_L(0) + ∫F − ∫D ≤ q_L(0) − γt`. (b3) `q_L(t) ≤ q_L(0) + F⁺t − γt`. ∎

**Repair note.** The recorded statement fused (b1) and (b2) under a hypothesis ("`F ≡ 0` is possible") that supports only (b1): with `q_L(0) = 10`, `γ = 1`, under `F ≡ 0` exit is at `t = 10`, but under `F ≡ 1` the trajectory never exits and under `F ≡ 3` it grows — the "moreover every trajectory exits" clause needs the universal hypothesis of (b2). Only (b1) is needed for the adversarial-exit certificate.

### (c) Best-case outer rule

**Statement (sharp per `batch 4/PROOF_ELEVATION.md` Finding 16).** If viability of the floor `{q_L ≥ 0}` on `[0,T]` holds at `x`, then necessarily

```
q_L(x)  ≥  D⁻_T − F⁻_T .
```

**This bound is sharp**: for every `q_L(0) ≥ D⁻_T − F⁻_T`, the policy `D ≡ D⁻` keeps `q_L(t) ≥ q_L(0) + F⁻_T(t/T) − D⁻_T(t/T) ≥ 0` against the worst-case inflow `F ≡ F⁻` — the bound cannot be improved. In the ceiling-slack convention (slack `ℓ := c − q_R` for a ceiling `{q_R ≤ c}` with maximal cumulative drain `F⁺_T` and no obligatory inflow, `D⁻ = 0`), the same computation against the fill adversarial to the ceiling gives the sharp form.

**Proof.** The adversary minimises `q_L`, so takes `F ≡ F⁻`; the policy maximises it, so takes `D ≡ D⁻`. Then `q_L(t) = q_L(0) + ∫F⁻ − ∫D⁻`, and safety at the binding time gives the bound. Sharpness is the same computation read forwards. ∎

**Repair note.** The recorded display substituted the **upper** inflow bound `F⁺_T` ("crediting the best-case relief"), giving `D⁻_T − F⁺_T` — true but strictly weaker than what the proof derives (weaker by `F⁺_T − F⁻_T`), and it loosened the sandwich of (d). The proof's own derivation is adversarial-inflow (`F⁻`), and that is the sharp bound now stated.

### (d) The sandwich and the mixed regime (the honesty boundary)

**The sandwich (flux data alone, corrected per `batch 4/PROOF_ELEVATION.md` Finding 16):**

```
{ q_L ≥ D_T }  ⊆  Viab_T({q_L ≥ 0})  ⊆  { q_L ≥ D⁻_T − F⁻_T },
```

with the inner rule using the *committed* budget `D_T` of rule (a) (the recorded `D⁺_T-budget` notation corrected to the committed form) and the outer rule the sharp obligatory-minimum bound of (c). The gap `D_T − D⁻_T + F⁻_T` is exactly the commitment slack plus the regeneration the ledger ignores — the sandwich is honest, never tight by fiat, and tight in the pure-drain, exactly-committed limit (`F ≡ 0`, `D ≡ D⁻`). On the worked numbers of the Thm2 repair (`D⁻ = 0.4`/unit, `F ∈ [0.2, 1.0]`, `T = 10`) the corrected outer bound is tighter than the recorded one by `F⁺_T − F⁻_T = 8.0` (`2.0` against `−6.0`).

**Mixed regime.** When the constraint set couples a floor on one moiety with a ceiling on another (the resource–sink geometry of E5: `S ≥ 2` *and* `K ≤ 2` linked by the extraction `H`), neither rule alone decides viability: the floor wants small `D`, the ceiling (through the sink's loading `θ_K D`) wants large `D`. The ledger sandwich still bounds the kernel from both sides, but the *decision* requires the module's structure (in E5: the three interval-verified conditions). This is the **honesty boundary** of flux-only reasoning, and E5's ceiling constraint is exactly a mixed-regime instance (recorded in the E5 sanity check: the floor's `D_T = 0.4·T` is conservative against the true kernel `S ≥ 2` because regeneration is ignored; the ceiling is where the mixed regime bites).

### E7.Thm2 — Multi-moiety noncompensatory form — PROVEN

**Statement (repaired per `batch 4/PROOF_ELEVATION.md` Finding 15).** For moieties `L₁, …, L_m` with separate ledgers (each with its own flows, no declared conversion pathway between them):

**(i) Product inner rule (unchanged, correct):**

```
∏_i { q_{L_i} ≥ D_{i,T} }  ⊆  Viab_T( ∏_i { q_{L_i} ≥ 0 } )
```

(componentwise application of rule (a)).

**(ii) Sharp noncompensation.** If `q_{L_i}(0) < D⁻_{i,T} − F⁻_{i,T}` for some `i` — a deficit relative to the **sharp outer bound** of rule (c), not the committed budget — then the state lies outside the kernel of the product constraint, and **no cross-moiety transfer can rescue it**: no allocation of moiety `j`'s surplus changes `q_{L_i}(T)`.

**(iii) Certificate.** The certificate is the moiety-`i` ledger identity itself — the coordinate functional `e_i`. Since the declared flow cone has no `i ↔ j` pathway, `⟨e_i, ·⟩` applied to the dynamics depends only on moiety `i`'s flows; the deficit is **structural**, not allocative.

**Proof.** (i) is rule (a) applied componentwise with the product policy. (ii) By the sharp rule (c) applied to moiety `i`, viability requires `q_{L_i}(0) ≥ D⁻_{i,T} − F⁻_{i,T}`; the contrapositive gives non-membership. For the transfer clause: moiety `j`'s flows do not appear in moiety `i`'s ledger identity, so `q_{L_i}(T)` is invariant under arbitrary changes to `(F_j, D_j)` (verified: `q_i(T)` takes exactly one value across 200 random draws of moiety-`j` flows). (iii) `e_i` is the exhibited functional. Sharpness of (ii): `q_{L_i}(0) = D⁻_{i,T} − F⁻_{i,T}` is viable under `D ≡ D⁻` against `F ≡ F⁻` (the minimum is exactly `0`), so the bound cannot be improved. ∎

**Repair notes.** (1) The recorded noncompensation clause used the **committed budget** `D_{i,T}` — deficit relative to an *inner* bound does not exclude kernel membership, because rule (a) is conservative by construction (the same file's E5 sanity check says exactly this: "the floor's `D_T = 0.4·T` is conservative against the true kernel `S ≥ 2`"). Explicit refutation: with `D⁻ = 0.4`/unit, `F ∈ [0.2, 1.0]`/unit, `T = 10`, committed budget `D_T = 4.0` and sharp bound `D⁻_T − F⁻_T = 2.0`: every `q(0) ∈ [2.0, 4.0)` is declared non-viable by the recorded test yet is viable under `D ≡ D⁻` (`min_t q(t) = q(0) − 2.0 ≥ 0`). (2) The recorded Farkas invocation is **unnecessary** and obscured the argument: with no declared pathway, noncompensation is a *conservation* fact, not a feasibility computation — Farkas/B6 re-enters only when a pathway *is* declared (which is B6.Thm1(2)'s setting, where the certificate has explicit multipliers).

### E7.Cor3 — Erosion-calculus geometry for affine barriers — PROVEN (repaired)

> **Repair note (PROOF_REAUDIT finding 13; consolidated in `batch 4/PROOF_ELEVATION.md` Finding 13).** The recorded claim `L_G = 0` is **false of the packet's constant**: `L_G` is the Hausdorff–Lipschitz modulus of the **velocity envelope** `G` (`d_H(G(x), G(p)) ≤ L_G‖x−p‖` in the inner tube — packet 02, Lemma 2), a property of the *dynamics*, and an affine constraint with a Lipschitz-varying envelope has `L_G > 0` (counterexample: the half-space `K = {x₂ ≥ 0}` with envelope `U(x) = [0,1] × [−1−x₁, 0]` has `L_G = 1` exactly). What *is* true — and is the intended point — is a statement about the **barrier geometry**, for which the correct constant is not `L_G`. Restated below with the two constants separated. Full development: `batch 4/E7_REPAIRED.md` §0.

**Statement.** For an **affine** moiety barrier `B(x) = ⟨a, x⟩ − c` (`a ≠ 0`; a half-space):

**(i)** the signed distance `s_K = B/‖a‖` is affine: `∇s_K = a/‖a‖` constant with `‖∇s_K‖ = 1`, `∇²s_K = 0` — `s_K` is `C^{1,1}` **globally** with `C^{1,1}` seminorm `0`;

**(ii)** `K_{−r} = {B ≥ r‖a‖}` for every `r ≥ 0`: each erosion is a half-space, nonempty, with the same outward normal as `K`;

**(iii)** consequently packet Lemma 2's geometric hypotheses hold with **tubular radius `ρ = ∞`**: the erosion condition `L_G r + Δ ≤ α` applies with **no upper bound on `r`** other than the inequality itself — the erosion calculus is **global** for affine barriers. The budget `L_G r + Δ ≤ α` remains **fully operative** (`L_G` is the envelope's modulus and is in general positive; it is *not* a function of the barrier);

**(iv)** the barrier-geometry constant that *does* vanish is the **normal-variation constant** `L_n := sup_{x∈∂K} ‖Dn(x)‖ = 0` (constant normal), strictly positive for strictly convex barriers — the affine/quadratic contrast is a statement about `L_n` and the reach, not about `L_G`;

**(v)** rule (a)'s integral identity is a **ledger** statement. It coincides with Lemma 2 at `L_G = 0` exactly when the `q_L`-velocity is state-independent (translation-invariant `G` near `K`) — under which `L_G = 0` *is* available and the erosion condition reduces to `Δ ≤ α`. That is the true content of the recorded claim.

**Proof.** (i)–(ii) are affine algebra (`dist(x, K^c) = max(0, B(x)/‖a‖)` for a half-space). (iii) follows: `s_K` is `C^{1,1}` on all of `ℝⁿ` and the normal correspondence holds for every `r > 0`. (iv) `n ≡ a/‖a‖` on `∂K`, so `Dn ≡ 0`. (v) as stated. ∎

C-e's quadratic barriers are the contrasting case, restated with the same constants: finite reach `τ = √c·√λ_min/λ_max` and `L_n = 1/τ > 0` — the calculus is confined to the tube `r < τ`. See the C-e repair in `batch 4/E7_REPAIRED.md` §0.2.

---

## Sanity check against E5 (recorded)

E5's module instantiates the ledger: source `S` with regeneration `R = 1.0 ≥ 0` (the `F ≥ 0` hypothesis), obligatory extraction `H_min = 0.4 = γ`. Rule (a): `{S ≥ 0.4·T} ⊆ Viab_T({S ≥ 2})`-translated through the `S_min` shift — conservative against the true kernel `S ≥ 2` for `T > 5` (regeneration ignored), consistent with the sandwich-gap remark. Rule (b): were regeneration absent, every trajectory exits within `S(0)/0.4`. The ceiling `{K ≤ 2}` is the mixed regime (d): the sink loads with `θ_K H`, so the floor (small `H`) and the ceiling (large `H`) pull in opposite directions — the three interval-verified conditions of E5 are the module-structure decision the ledger alone cannot make. Consistent on all three counts.

---

## Status

- **E7.Thm1 (a)–(d): PROVEN (repaired)** ((b) split into (b1) robust-kernel / (b2) pathwise / (b3) sharp exit time; (c) sharp outer bound `D⁻_T − F⁻_T` with sharpness proved; (d) corrected sandwich with the committed `D_T` inner bound).
- **E7.Thm2: PROVEN (repaired)** (componentwise inner rule + sharp noncompensation at `D⁻_{i,T} − F⁻_{i,T}` with the ledger-identity certificate; Farkas invocation removed as unnecessary).
- **E7.Cor3: PROVEN (repaired)** (restated with the barrier constants `L_n` and `ρ = ∞`; `L_G` untouched — the recorded `L_G = 0` withdrawn as false of the packet's constant).

**Dependencies:** packet B6 (typed conservation, Farkas), R03.Thm1 (adversarial-exit soundness branch), E5 (sanity instance), C-e (non-degenerate counterpart). **Consumers:** Paper 3 (the bridge theorem), C-e, E5's interpretation, the D-tier H3 protocol (substitution certificates).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.

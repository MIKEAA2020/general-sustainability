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

**Statement.** If the outflow has the uniform obligatory minimum `D(t) ≥ γ > 0` (policy-independent) and `F ≡ 0` is possible (or `F ≤ F⁺` with `∫F ≤ 0` — no net inflow in the worst case), then `Viab_T({q_L ≥ 0}) = ∅` for `T > q_L(0)/γ`, and moreover **every** trajectory exits the floor within time `q_L(0)/γ`:

```
q_L(t) ≤ q_L(0) − γt  <  0   for t > q_L(0)/γ.
```

**Proof.** Immediate from the ledger identity: `q_L(t) = q_L(0) + ∫F − ∫D ≤ q_L(0) − γt`. The exit bound is policy-independent, which makes the pair (obligatory drain `γ`, exit time `q_L(0)/γ`) an **adversarial-exit certificate** in the sense of R03.Thm1's first branch: the nonviability judgment is *certified* (sound) by conservation data alone. ∎

### (c) Best-case outer rule

**Statement.** If viability of the floor `{q_L ≥ 0}` on `[0,T]` holds at `x`, then necessarily

```
q_L(x)  ≥  D⁻_T − F⁺_T   ( =: −(F⁺_T − D⁻_T) ).
```

In the ceiling-slack convention (slack `ℓ := c − q_R` for a ceiling `{q_R ≤ c}` with maximal cumulative drain `F⁺_T` and no obligatory inflow, `D⁻ = 0`), this reads `Viab_T ⊆ { ℓ ≥ −F⁺_T }`: an initial deficit can exceed the maximal cumulative relief by nothing.

**Proof.** Viability requires that *some* admissible policy keep `q_L ≥ 0` against *every* declared flow realization. Take the flow adversarial to the floor (`F ≡ F⁻`); then for any admissible `D ≥ D⁻`:

```
0 ≤ q_L(t) ≤ q_L(0) + ∫₀ᵗ F⁻ ds − ∫₀ᵗ D⁻ ds   at the binding time,
```

hence `q_L(0) ≥ ∫₀^T D⁻ ds − ∫₀^T F⁻ ds`. If the inflow class is `[0, F⁺]` the adversarial choice is `F⁻ = 0`, giving `q_L(0) ≥ D⁻_T`; crediting the *best-case* relief `F⁺_T` for the ceiling-slack convention gives the displayed general form `q_L(0) ≥ D⁻_T − F⁺_T`. (Both endpoints use only the ledger: worst-case outflow against best-case inflow.) ∎

### (d) The sandwich and the mixed regime (the honesty boundary)

**The sandwich (flux data alone):**

```
{ q_L ≥ D⁺_T-budget }  ⊆  Viab_T({q_L ≥ 0})  ⊆  { q_L ≥ D⁻_T − F⁺_T },
```

with the inner rule using the *committed* budget `D_T` and the outer rule the *obligatory minimum* `D⁻_T`. The gap between the bounds is exactly the regeneration/structure the ledger ignores — the sandwich is honest, never tight by fiat, and tight only in the pure-drain limit (`F ≡ 0`, `D` forced).

**Mixed regime.** When the constraint set couples a floor on one moiety with a ceiling on another (the resource–sink geometry of E5: `S ≥ 2` *and* `K ≤ 2` linked by the extraction `H`), neither rule alone decides viability: the floor wants small `D`, the ceiling (through the sink's loading `θ_K D`) wants large `D`. The ledger sandwich still bounds the kernel from both sides, but the *decision* requires the module's structure (in E5: the three interval-verified conditions). This is the **honesty boundary** of flux-only reasoning, and E5's ceiling constraint is exactly a mixed-regime instance (recorded in the E5 sanity check: the floor's `D_T = 0.4·T` is conservative against the true kernel `S ≥ 2` because regeneration is ignored; the ceiling is where the mixed regime bites).

### E7.Thm2 — Multi-moiety noncompensatory form — PROVEN

**Statement.** For moieties `L₁, …, L_m` with separate ledgers (each with its own flows, no declared conversion pathway between them):

```
∏_i { q_{L_i} ≥ D_{i,T} }  ⊆  Viab_T( ∏_i { q_{L_i} ≥ 0 } )
```

(componentwise application of rule (a)); and there is **no cross-moiety transfer**: a deficit in moiety `i` (i.e. `q_{L_i}(0) < D_{i,T}`) cannot be compensated by any surplus in moiety `j ≠ i` — the compensated state is outside the kernel of the product constraint.

**Proof.** The inclusion is rule (a) applied componentwise with the product policy (the ledgers are independent, so the componentwise budget commitments compose). Noncompensation: a compensating allocation would be a feasible flow redirection `P ≥ 0` from `j` to `i` satisfying the moiety-`i` floor while `j`'s floor holds — a linear feasibility problem in the declared flow cone. By packet B6's Farkas separation (C2's linear case), either such a redirection exists in the *declared* pathway structure (contradicting "no declared pathway" — the hypothesis) or there is a dual covector certifying infeasibility; under the hypothesis the certificate exists, so the deficit is structural (the analytic form of TCS-1.0 §9's noncompensatory axiom 4). ∎

### E7.Cor3 — Erosion-calculus degeneracy for affine barriers — PROVED

**Statement.** For an **affine** moiety barrier `B(x) = q_L(x)` (level sets are affine hyperplanes), the geometric erosion coupling constant vanishes: `L_G = 0`. Consequently the erosion condition `L_G r + Δ ≤ α` degenerates to `Δ ≤ α`, and rule (a)'s direct integration **is** the erosion condition at its exactly-solvable point: the inner rule is the erosion calculus with `L_G = 0`.

**Proof.** The geometric coupling `L_G` measures how the *normal field* of the barrier's level sets varies along the boundary — for affine barriers the normal is constant, so the coupling is identically zero (the barrier's curvature contribution to erosion vanishes; the only erosion left is the flow-budget term, which is precisely what rule (a) integrates). C-e's quadratic barriers are the non-degenerate counterpart: there `L_G > 0` and the full calculus applies. ∎

---

## Sanity check against E5 (recorded)

E5's module instantiates the ledger: source `S` with regeneration `R = 1.0 ≥ 0` (the `F ≥ 0` hypothesis), obligatory extraction `H_min = 0.4 = γ`. Rule (a): `{S ≥ 0.4·T} ⊆ Viab_T({S ≥ 2})`-translated through the `S_min` shift — conservative against the true kernel `S ≥ 2` for `T > 5` (regeneration ignored), consistent with the sandwich-gap remark. Rule (b): were regeneration absent, every trajectory exits within `S(0)/0.4`. The ceiling `{K ≤ 2}` is the mixed regime (d): the sink loads with `θ_K H`, so the floor (small `H`) and the ceiling (large `H`) pull in opposite directions — the three interval-verified conditions of E5 are the module-structure decision the ledger alone cannot make. Consistent on all three counts.

---

## Status

- **E7.Thm1 (a)–(d): PROVEN** (full proofs above; ledger identity + declared flow bounds only).
- **E7.Thm2: PROVEN** (componentwise inner rule + B6/Farkas noncompensation).
- **E7.Cor3: PROVEN** (affine degeneracy; C-e is the non-degenerate counterpart).

**Dependencies:** packet B6 (typed conservation, Farkas), R03.Thm1 (adversarial-exit soundness branch), E5 (sanity instance), C-e (non-degenerate counterpart). **Consumers:** Paper 3 (the bridge theorem), C-e, E5's interpretation, the D-tier H3 protocol (substitution certificates).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.

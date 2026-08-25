# E5 — One Module Admitted with Numbers (A001 §§6–10 Resource–Sink, **Linear Case Only**)

**Provenance:** reconstructed and expanded after the filesystem loss of the long-form original (session worklog Tasks 3, 11; expansion recorded in TRANSFER_AUDIT_RESPONSE Findings 1–2). The numerical artifact and script are **committed** (not lost): `research_program/validated_computations/E5_NUMBERS.json` + `e5_admission.py`.

---

## ⚠ Scope and transfer prohibition (mandatory — read before citing)

1. **The admitted module is the linear A001 §§6–10 resource–sink.** State `(S,K) ∈ ℝ²`, dynamics
   ```
   Ṡ = R − a·S − H(t),      K̇ = θ_K·H(t) − θ_d·K,
   ```
   with `R = 1.0`, `a = 0.1`, `H ∈ [H_min, H_max] = [0.4, 0.8]` the extraction control, `θ_K = 0.5`, `θ_d = 0.2`, safe set `{S ≥ 2, 0 ≤ K ≤ 2}`. This is a **2-D linear ODE toy** — the closed-form module of A001's Sections 6–10 (Theorems 6.1/6.2/6.3), *not* a scored model of any real fishery.
2. **It is not any real system.** The programme's real-system referents are two distinct objects of a different class: the northern-cod fishery (NAFO **2J3KL**; A014/A016 — the G1a case) and the groundwater side (an **Edwards well J-17**-type aquifer system — the G1b referent; the Edwards Aquifer critical-period system was examined as a case candidate in the manuscript's case search and rejected on the confound gate; A005 is the generic typed template, not Edwards-calibrated). A third object, the **A021 C4 J-series**, is *not a real system at all*: it is the A021 joint-decision-docket items (J01–J25; J17 = the BLZ citation-matching disposition) — external-review bookkeeping whose C4 gated DDE is the programme model equation behind the validated computations. **No number in this file or in `E5_NUMBERS.json` is a statement about 2J3KL, about the Edwards J-17 system, about any A021 model, or about any calibrated real system.**
3. **R04 forbids transfer.** By R04.Thm1's converse (batch-2 record, Field 8), no judgment transfers from a module to any other model without the five-map admission certificate (type/unit, phase-space, dynamics, safe-set, policy/information correspondences); `ANALOGY_ONLY` is excluded from transfer *by the theorem*. **No five-map certificate exists from the linear (S,K) toy to the 2J3KL fishery, to any Edwards J-17-type system, to any A021 model, or to any other model.** The only other route is R04.Cor2 approximate admission (dynamics defect `ε` → Grönwall deviation `(ε/L)(e^{LT}−1)` → kernel erosion) — likewise not constructed for any real system (and for an Edwards-type system it would be forecast-map only).
4. **What E5 legitimately is:** the programme's first *complete worked example of the admission method* — five maps exact, interval-verified constants, closed-form kernel, displayed (REG) family — i.e. a **method demonstration and case-screening template** (Paper 5's use), and the worked example for the conservation–viability sandwich (Paper 3's use, with E7). Nothing more.

---

## The admission record (F4-complete, linear case)

### Field 3 — Exact statement

For the module above:

- **Kernel (closed form).** `Viab = [2, ∞) × [0, 2]`, i.e. the safe set itself, with the **order-minimal policy** `H ≡ H_min = 0.4` (A001 Thm 6.3). The kernel equals the safe set because the three conditions below hold simultaneously; each is necessary (drop it and the kernel strictly shrinks or empties — the A001 theorem's content).
- **(REG) exhibition.** The constant policy `H ≡ H_min` is measurable, continuous, Lipschitz, and computable, and its closed loop keeps every state of the safe set in the safe set for all `t ≥ 0` (infinite horizon) — the displayed certificate family is the singleton loop condition, which is a valid (REG) family on the infinite horizon.

### Field 8 — Proof (self-contained)

**Conditions (interval-verified, outward-rounded float64 — `E5_NUMBERS.json` `conditions`):**

1. `H_min ≤ R − a·S_min` (floor feeds): `0.4 ≤ 1.0 − 0.1·2 = 0.8`, rigorous margin `0.4 − ε`.
2. `K† := θ_K·H_min/θ_d ≤ K_max` (ceiling equilibrium under minimal load): `0.5·0.4/0.2 = 1.0 ≤ 2`, rigorous margin `1.0 − ε`.
3. `S_min ≤ S* := (R − H_min)/a` (floor equilibrium above the bound): `2 ≤ 6.0`, rigorous margin `4.0 − ε`.

**Kernel proof.** (⊇) Under `H ≡ H_min`: `Ṡ = R − aS − H_min ≤ 0` only when `S > S*`... precisely: `Ṡ ≥ 0 ⟺ S ≤ S*`; since `S_min = 2 < S* = 6`, the `S`-face `{S = 2}` has inward velocity `R − a·2 − H_min = 0.4 > 0` (condition 1) — no exit through the floor. The `K`-dynamics under `H_min` has the globally attracting equilibrium `K† = 1.0 < K_max` (condition 2) — `K̇ = 0.4·... ` the `K`-face `{K = 2}` has inward velocity `θ_K·H_min − θ_d·2 = 0.2 − 0.4 = −0.2 < 0` — no exit through the ceiling. `K ≥ 0` is preserved (`K̇ = θ_K H − θ_d K ≥ −θ_d K ≥ 0` when `K ≤ 0`... for `K = 0`: `K̇ = θ_K H_min > 0`). So the safe set is invariant under the exhibited policy: `Viab ⊇ [2,∞)×[0,2]`. (⊆) `Viab ⊆` safe set by definition. Hence equality. **Order-minimality:** any policy with `H > H_min` at some time raises the `K`-equilibrium toward `θ_K H_max/θ_d = 2.0 = K_max` and lowers the `S`-equilibrium toward `(R−H_max)/a = 2.5`; the constraint pair forces `H ≤ H_min` a.e. on the infinite horizon for states on the binding faces — the A001 Thm 6.3 argument. ∎

**Face margins, Lipschitz constant, erosion menu (interval-verified — `E5_NUMBERS.json`):**

- `α_S = R − a·S_min − H_min = 0.4` (floor face margin), `α_K = θ_d·K_max − θ_K·H_min = 0.2` (ceiling face margin), joint `α = 0.2`.
- `L = max(a, θ_d) = 0.2` (the field's `∞`-norm Jacobian: the linear system's Lipschitz constant).
- **Erosion menu:** for each `r`, the eroded margins are `α_S − a·r`, `α_K − θ_d·r`, joint `α_r = min(...)`; the erosion condition `L·r + Δ ≤ α_r` is solvable for `Δ > 0` exactly when `r < α/(L + max(a, θ_d)) = 0.2/0.4 = 0.5`... the certified triple found by the sweep: **`L = 0.2, r = 0.05, Δ ≤ 0.18`** (outward-rounded down), eroded kernel `[2.05, ∞) × [0, 1.95]`.
- **Confinement:** `[2, 8] × [0, 2]` is positively invariant under `H ≡ H_min` (`S* = 6 ∈ [2,8]`; at `S = 8`: `Ṡ = 1 − 0.8 − 0.4 = −0.2 < 0`, inward — interval-verified `inward_at_S_hi: true`); this satisfies the confinement mandatory-field rule for infinite-horizon claims.

### Field 9 — Necessity witnesses (why each condition is load-bearing)

- Drop condition 1 (`H_min > R − a·S_min`): the floor face points outward at `S = S_min` under **every** admissible `H ≥ H_min` — the kernel loses the entire face (emptying-type obstruction, cf. E7.Thm1(b)).
- Drop condition 2 (`K† > K_max`): the ceiling equilibrium sits beyond the bound — every policy eventually violates `K ≤ K_max` on the infinite horizon (the mixed regime's honesty boundary, E7.Thm1(d)); finite-horizon viability survives only with the exit-time bookkeeping of R03.
- Drop condition 3 (`S_min > S*`): the floor equilibrium drops below the bound — same structure as condition 1's failure.

### Field 16 — Remaining obligations and revocation triggers

- **Independent rerun: NONE.** The artifact must be recomputed by a second party before any submission (HONEST_DISCLOSURE.md).
- **Revocation triggers:** any change to the A001 §§6–10 source model (the `R, a, θ_K, θ_d, H_min, H_max, S_min, K_max` declarations), or discovery of an arithmetic error in `interval_lib.py`'s outward rounding.
- **Transfer obligations (from the prohibition section):** any use of this module's numbers toward either real system (the 2J3KL cod fishery or an Edwards J-17-type aquifer system) — or toward any other model — requires first constructing the R04 five-map certificate or the Cor2 approximate admission (for an Edwards-type system, Cor2 is forecast-map only); neither exists; the attempt is a registered Wave-0/G1 gating item.

### Field 17 — Dependency edges

R04.Tab3 (the admission classification row: "Fisheries — resource–sink (A001 §§6–10) … **admitted**", the only complete-certificate row) → this file (numerical instantiation) → D-tier G1a track (method template) → Paper 3 (E7 worked example) / Paper 5 (case-screening template). Producers: A001 source §§6–10; `interval_lib.py` (verified against exact rational arithmetic).

---

## Status

**PROVED at declared scope (linear resource–sink module; interval-verified constants; committed artifact).** The five-map admission into the architecture is exact (identity phase map on `(S,K)`); the numbers are the toy's; the transfer prohibition above is part of the record's normative content — citing this module beyond the method demonstration without the R04 certificate is a category error the programme's own theorem forbids.

**Record-format note:** internal admission record; Fields 1–4, 6–9, 16–17 carried (Field 6 = the source declarations above; Field 11 erosion data in the menu); Fields 5, 10, 12–15 N/A or trivial (policy regularity is exhibited: constant).

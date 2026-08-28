# Paper 1 Independent-Result Candidate — The Strengthening

## Typed False Positives: the Assessment Hierarchy Theorem and the Noncompensatory Separation

## Status

**Mathematical status:** self-contained theorems and proofs complete under the stated finite-review, exact-tube assumptions (the same data discipline as `paper1_finite_architecture_transformation_theorem.md`).
**Witness status:** the complete instantiation is EXECUTED as a deterministic exact-rational artifact (`paper1_instantiation/typed_false_positive_instantiation.py` → `typed_false_positive_instantiation.json` + `typed_false_positive_instantiation_report.md`); every theorem claim below is machine-checked there.
**Publication status:** this file is the strengthening requested by `internal_provisional_Paper1_operatorII_novelty_answer.md` §6 ("an algebraic noncompensation result combined with a dynamic transition tube … more distinctive than renaming a predecessor"). The full-text novelty pass is the companion file `paper1_full_text_novelty_pass.md`. Together they close Paper 1's independent-result gate at the internal level; the gate decision is recorded in §10.
**Scope:** `TCS-1.0` Operator II assessment semantics. Nothing here concerns variable events, stochastic chance constraints, partial observation, or infinite horizons.

## 1. Purpose

The provisional novelty answer (§1) held that the finite-architecture exact-tube backward recursion is mathematically correct but **not independently novel**, and that Paper 1 can stand as a journal article only if it adds at least one nontrivial result beyond the standard recursion — proposed target (§6):

> There exist architecture transitions that are physically endpoint-reachable and remain feasible under every positive scalar aggregate of obligations, yet are infeasible under the typed noncompensatory transition-safe registry because one identity/liability component must cross a forbidden region. Exact-tube backward induction rejects precisely those transitions.

This file delivers that theorem in a sharper form than proposed: the separation is proved as a **hierarchy theorem** (endpoint-only ⊇ scalarized ⊇ noncompensatory, with the precise localization of the gap in the action quantifier), realized on an explicit two-architecture datum with closed-form regions, split into a **rescuable part** and a **certified impossibility part**, and propagated through the multi-stage backward induction. The proposed wording "one identity/liability component must cross a forbidden region" is realized verbatim by the FAST/SLOW witnesses (§7).

## 2. Framework and notation

Throughout, fix an exact-tube finite-architecture datum as in `paper1_finite_architecture_transformation_theorem.md` §1: finite architecture set `Q`, fixed review times `t_0 < … < t_m`, disjoint phase state `X`, per-stage admissible meta-action sets `A_k(q,x)`, nonempty declared disturbance sets `D_k(q,x,a)`, exact tubes `Tube_k(q,x,a,d)`, nonempty successor sets `Succ_k(q,x,a,d)`, transition-safe sets `S_k`, and terminal destination set `G`.

**Typed decomposition.** The phase state carries physical coordinates `x` and `n ≥ 2` typed constraint coordinates `s = (s_1,…,s_n)` (in the programme's semantics: floors for protected-group service, liability coverage, obligations, cumulative harm, etc.). The transition-safe registry and the destination set are **typed noncompensatory**:

```
S_k = S_k^phys ∩ {s : s_i ≥ 0 for every i},      G = G^phys ∩ {s : s_i ≥ 0 for every i},
```

where `S_k^phys` is the constraint on physical coordinates and each `s_i ≥ 0` is one floor of the registry (the floor value is normalized to 0 by translation; this loses no generality). Noncompensatory means: conjunction, with no substitution between floors. This is the strong-sustainability registry of the programme; the physical coordinates carry the ordinary state constraints.

**Aggregate weights.** Let

```
C = R^n_+ \ {0}
```

be the closed nonnegative cone of aggregate weight vectors (prices). The closed cone, not the strictly positive orthant, is used for three reasons: (i) zero prices are the honest weak-assessment semantics — aggregate indices routinely price a capital form at zero (uncosted ecosystem services are the canonical sustainability example); (ii) the pointwise equivalence (Lemma 3) holds exactly on the closed cone, which isolates the entire assessment gap in the dynamic quantifier structure (Theorem A(ii)) rather than in a static openness artifact; (iii) the closed cone is the larger — hence more permissive — family of aggregate assessments, so every separation proved against it is a fortiori a separation against any subfamily, including all strictly positive price vectors.

**The three assessments.** For a fixed stage `k`, state `z = (q,x,s)`, and target set `W ⊆ X` for stage `k+1`, define the admissible-action sets:

```
E_phys(z, W) = {a ∈ A_k(z) : ∀d ∈ D_k(z,a),  Tube_k(z,a,d) ⊆ S_k^phys  and  Succ_k(z,a,d) ⊆ W^phys}
E_w(z, W)    = {a ∈ A_k(z) : ∀d,  Tube_k(z,a,d) ⊆ S_k^phys ∩ {w·s ≥ 0}  and  Succ_k(z,a,d) ⊆ W^phys ∩ {w·s ≥ 0}}
E_typ(z, W)  = {a ∈ A_k(z) : ∀d,  Tube_k(z,a,d) ⊆ S_k  and  Succ_k(z,a,d) ⊆ W}
```

for `w ∈ C`, where `W^phys` is the physical projection of `W` (for the terminal stage, `G^phys`; for earlier stages, the corresponding assessment's pulled-back target — see Theorem C). The three **assessment predecessors** are

```
P_phys(z) ⟺ E_phys(z) ≠ ∅,     P_w(z) ⟺ E_w(z) ≠ ∅,     P_typ(z) ⟺ E_typ(z) ≠ ∅.
```

Semantics. `P_phys` is the **endpoint-only physical assessment**: only physical state constraints are enforced, and only at the level of physical coordinates (an endpoint-accounting audit). `P_w` is the **scalarized aggregate assessment** with weight vector `w`: physical constraints plus the single aggregate floor `w·s ≥ 0` on tubes and successors (a weak-sustainability index: robust to the declared disturbances, but compensating across floors at prices `w`). `P_typ` is the **noncompensatory typed assessment** — the exact predecessor of the main theorem, each floor enforced separately. All three retain the same disturbance quantifier `∀d ∈ D_k`; the assessments differ **only** in the constraint structure. That is the point of the theorem: the separation below is attributable to compensation structure alone, not to differing robustness standards.

## 3. Lemma (pointwise closed-cone equivalence)

**Lemma 3.** For `v ∈ R^n`:  `v ≥ 0` componentwise  ⟺  `w·v ≥ 0` for every `w ∈ C`.

*Proof.* (⇒) If `v ≥ 0` and `w ≥ 0`, `w ≠ 0`, then `w·v = Σ_i w_i v_i ≥ 0`. (⇐) Contrapositive: if `v_k < 0` for some `k`, take `w = e_k ∈ C`; then `w·v = v_k < 0`. ∎

**Remark (relationship to the atlas's static result).** Paper 2's Proposition 5.1 [CC-A002-007] states, for strictly positive `w ∈ R^n_{++}`, that `w^⊤Δ ≥ 0` does not imply `Δ ≥ 0` — the static compensation failure on the open cone. Lemma 3 is the complementary closed-cone statement: on `C` the pointwise biconditional holds, so at a **fixed point** (or along a **fixed trajectory**) the aggregate with closed-cone weights is exactly as informative as the vector of floors. The entire dynamic assessment gap of Theorem A is therefore *not* a static scalarization artifact: it lives in the quantifier structure. This is the precise nonduplication seam with Paper 2's family F02, which owns the static compensation logic; the present theorems own the dynamic assessment hierarchy. The two-line Lemma 3 is proved locally and transferred nowhere.

## 4. Theorem A (assessment hierarchy and quantifier noncommutativity)

**Theorem A.** Fix a typed exact-tube datum, a stage `k`, and a target `W ⊆ X` with the typed decomposition above. Then:

**(i) Hierarchy.**
```
E_typ(z) ⊆ E_w(z) ⊆ E_phys(z)   for every w ∈ C,  hence   P_typ ⇒ (∀w ∈ C: P_w) ⇒ P_phys.
```

**(ii) Localization of the gap.** For every state `z`:
```
E_typ(z) = ⋂_{w∈C} E_w(z),
```
so the two assessment predecessors differ exactly by the order of "there exists a plan" and "for all weights":
```
{z : P_typ} = {z : ⋂_{w∈C} E_w(z) ≠ ∅},      {z : ∀w∈C: P_w} = {z : ∀w∈C : E_w(z) ≠ ∅}.
```
The first is "one plan serves every price vector"; the second is "every price vector has its own plan". Existential choice of plan does not commute with the universal quantifier over weights, and the gap between the two sets is precisely the set of states for which the price-vector-optimal plans disagree.

**(iii) Strictness.** Both inclusions in (i) can be strict **simultaneously on one datum** with `|Q| = 2`, `n = 2` typed coordinates, four meta-actions, and a two-point disturbance set — Theorem B exhibits the datum, with nonempty-interior regions for both gaps.

*Proof.* (i) Let `a ∈ E_typ(z)`. Then for every `d`: `Tube_k(z,a,d) ⊆ S_k = S_k^phys ∩ {s ≥ 0}`, and by Lemma 3 (⇒) every point of the tube satisfies `w·s ≥ 0` for every `w ∈ C`; likewise every successor lies in `W ⊆ W^phys ∩ {w·s ≥ 0}` by Lemma 3 applied to the successor states. Hence `a ∈ E_w(z)`. The inclusion `E_w(z) ⊆ E_phys(z)` is immediate from `S_k^phys ∩ {w·s ≥ 0} ⊆ S_k^phys` and `W^phys ∩ {w·s ≥ 0} ⊆ W^phys`.

(ii) `⊆`: if `a ∈ E_typ(z)` then `a ∈ E_w(z)` for every `w` by (i). `⊇`: let `a ∈ ⋂_{w∈C} E_w(z)`; for every `d` and every point `p` of `Tube_k(z,a,d)`, every `w ∈ C` gives `w·s(p) ≥ 0` (the aggregate floor of `S^w` holds on the whole tube), so `s(p) ≥ 0` by Lemma 3 (⇐); hence `Tube ⊆ S_k^phys ∩ {s ≥ 0} = S_k`; the same argument over successor states gives `Succ ⊆ W^phys ∩ {s ≥ 0} = W`. The displayed identification of the two predecessor sets is a restatement. (iii) is Theorem B. ∎

**Corollary A.1 (no price vector rescues the assessment).** On any datum, `P_typ ⇒ P_w` for each `w`; on the datum of Theorem B, `⋂_{w∈C}{P_w} ⊋ {P_typ}` with nonempty interior. Since `⋂_{w∈C} E_w(z) ⊆ E_{w_0}(z)` for every fixed `w_0`, intersecting the scalarized assessments over **any** subfamily of `C` — up to all of `C` — never recovers the noncompensatory predecessor on that datum. The noncompensatory assessment is not the limit of weak assessments.

## 5. The witness datum

**Data `𝒟`.** `Q = {0,1}` (extraction architecture `0`, regenerative architecture `1`); one review interval `[0,1]` (`m = 1`); phase state `(q, x, s_1, s_2)` with physical coordinate `x` (reserve/budget stock) and typed floors `s_1` (protected-group service surplus over its floor) and `s_2` (remediation-liability coverage surplus over its floor):

```
S_0 = {x ≥ 0, s_1 ≥ 0, s_2 ≥ 0},      G = {(1, x, s_1, s_2) : x ≥ 0, s_1 ≥ 0, s_2 ≥ 0}.
```

The destination maintainability condition of the main theorem's `G`-membership is witnessed by the destination hold policy (zero drift; tube and successor of a hold are the singleton state), under which `G` is robustly invariant; this is declared datum. Disturbance set `D = {β, α}` with dip-depth scaling `κ(β) = 1`, `κ(α) = 4/3`, present for every action; the dip-depth scale `D_1 = D_2 = 3/2` (worst case `λD_i = 2`); reset gains `e_1 = e_2 = 1/4`; rescue cost `c = 1`. The triangular bump

```
ψ(t) = 2t  on [0, ½],      ψ(t) = 2 − 2t  on [½, 1]
```

has `ψ(0) = ψ(1) = 0`, `max ψ = 1` at `t = ½`. From every initial state `(0, x, s)` with `x ≥ 0, s ≥ 0`, the admissible meta-actions are:

| action | within-interval trajectory | successor (at `t = 1`) |
|---|---|---|
| `NO-SWITCH` | `(0, x, s)` constant | `{(0, x, s)}` |
| `FAST` | `s_1(t) = s_1 − D_1 κ(d) ψ(t)`, `s_2(t) = s_2`, `x(t) = x` | `{(1, x, s_1 + e_1, s_2 + e_2)}` |
| `SLOW` | `s_1(t) = s_1`, `s_2(t) = s_2 − D_2 κ(d) ψ(t)`, `x(t) = x` | `{(1, x, s_1 + e_1, s_2 + e_2)}` |
| `STAGED` | `s_1(t) = s_1 + e_1 t`, `s_2(t) = s_2 + e_2 t`, `x(t) = x − c t` | `{(1, x − c, s_1 + e_1, s_2 + e_2)}` |

Reading. `FAST` is the immediate full capacity switch: the deployment gap (new capacity not yet online) dips the protected-service surplus mid-interval, while the escrow continues (liability coverage constant), and the transfer completes at the endpoint with destination gains. `SLOW` is the phased switch: service is maintained on the old capacity, but the liability handover opens a mid-interval window in which remediation coverage dips while service does not. `STAGED` is the bridging plan: temporary rented capacity covers the deployment gap and escrow bridging covers the handover window — no typed dip — at physical cost `c` drawn linearly from the reserve stock. `NO-SWITCH` remains transit-safe but lands outside `G`: architecture `0` is not a destination (the phase-out is destination datum).

**Exactness witness.** Every coordinate trajectory is piecewise linear with breakpoints in `{0, ½, 1}` and is monotone on each piece; the exact visited set of a piecewise-monotone continuous scalar function is the union of its closed piece-endpoint intervals, so each per-coordinate tube below is **exact**, not an outer approximation: for `FAST` under `d`: `s_1`-tube `[s_1 − D_1 κ(d), s_1]`, `s_2`-tube `[s_2, s_2]`, `x`-tube `[x, x]`; for `SLOW` the same with coordinates exchanged; for `STAGED`: `[s_1, s_1+e_1]`, `[s_2, s_2+e_2]`, `[x−c, x]`; for `NO-SWITCH`: singletons. The union over `d ∈ D` of the per-`d` tubes is the action's declared exact tube (the solution concept is: deterministic branch per declared disturbance). This satisfies the main theorem's exactness requirement; conservative outer tubes are not used anywhere in the datum.

All constants are rational; the instantiation artifact verifies every region below in exact rational arithmetic.

## 6. Theorem B (false positives, blindness levels, rescue, and impossibility)

**Theorem B.** On the datum `𝒟`, restrict to initial states `X_0 = {(0, x, s) : x ≥ 0, s ≥ 0}`. Then:

**(1) Typed region.**
```
{P_typ} ∩ X_0 = {x ≥ 1} ∪ {s_1 ≥ 2} ∪ {s_2 ≥ 2}.
```

**(2) Aggregate region.**
```
⋂_{w∈C}{P_w} ∩ X_0 = {x ≥ 1} ∪ {s_1 + s_2 ≥ 2}.
```

**(3) Endpoint-only region.**
```
{P_phys} ∩ X_0 = X_0.
```

**(4) False-positive set.** The set of states that every aggregate assessment admits but the noncompensatory assessment rejects is the triangle
```
FP = {x < 1, s_1 < 2, s_2 < 2, s_1 + s_2 ≥ 2},
```
which has nonempty interior (e.g. `(x, s_1, s_2) = (½, 6/5, 6/5)`, since `6/5 + 6/5 = 12/5 ≥ 2` with both coordinates below `2`).

**(5) Both blindness levels, strictly, on one datum.** `W^typ ⊊ ⋂_w W^w ⊊ W^phys`, both inclusions strict on `𝒟`: the point `(½, 1/10, 1/10)` lies in `W^phys \ ⋂_w W^w` (endpoint-feasible, but at the weight `w = (1,1)` no action is aggregate-safe), and every point of `FP` lies in `⋂_w W^w \ W^typ`.

**(6) The per-weight plans disagree.** On the interior of the triangle `{s_1 < 2, s_2 < 2, s_1 + s_2 > 2}` with `s > 0`, the FAST-certifying weights are exactly `{r = w_2/w_1 ≥ ρ_1}` and the SLOW-certifying weights exactly `{r ≤ ρ_2}`, where
```
ρ_1 = (2 − s_1)/s_2 ,      ρ_2 = s_1/(2 − s_2) ,      ρ_2 ≥ ρ_1  ⟺  s_1 + s_2 ≥ 2,
```
and `ρ_1 < ρ_2` on the interior. Hence both weight families are nonempty proper subsets of `[0, ∞]`: low-`s_2`-price assessors license `FAST` only, high-`s_2`-price assessors license `SLOW` only, and **no single action serves every price vector** — which is exactly `E_typ = ⋂_w E_w = ∅` (Theorem A(ii)).

**(7) Rescue split.** Let `FP_0 = {s_1 < 2, s_2 < 2, s_1 + s_2 ≥ 2, s ≥ 0}` (the triangle, `x` unrestricted). Then
```
R = FP_0 ∩ {x ≥ 1}  (the rescue set):  every state of R is typed-transformable, witnessed by STAGED —
      the bridging plan rents temporary capacity at physical cost c = 1, keeps both floors intact
      throughout, and lands in G;
I = FP_0 ∩ {x < 1}  (the impossibility region):  aggregate-feasible for every w ∈ C, yet NO typed-
      admissible action exists — a certified impossibility with four exhibited violations:
        FAST  : the s_1-tube under the adverse disturbance α is [s_1 − 2, s_1] with s_1 < 2  → floor violated;
        SLOW  : the s_2-tube under α is [s_2 − 2, s_2] with s_2 < 2                        → floor violated;
        STAGED: the x-tube is [x − 1, x] with x < 1                                        → physical stock driven negative;
        NO-SWITCH: the successor is (0, x, s) ∉ G                                          → destination architecture not reached.
```

*Proof.* Throughout, initial states lie in `X_0`, and the four actions exhaust `A_0`.

(1) `NO-SWITCH` fails terminal membership (`q = 0 ∉ G`). `FAST` is typed-admissible iff its worst-case tube lies in `S_0`: the `s_1`-tube under `α` is `[s_1 − 2, s_1]`, requiring `s_1 ≥ 2` (the `s_2`- and `x`-tubes are safe on `X_0`; the successor `(1, x, s+e) ∈ G` always). `SLOW` likewise iff `s_2 ≥ 2`. `STAGED` has no typed dip; its `x`-tube `[x−1, x]` requires `x ≥ 1`, and its successor is in `G` iff `x − 1 ≥ 0`. Hence `{P_typ} ∩ X_0 = {s_1 ≥ 2} ∪ {s_2 ≥ 2} ∪ {x ≥ 1}`.

(2) `⊆`: let `x ≥ 1`: `STAGED` is aggregate-safe for every `w ∈ C` (tubes: `w·s(t) = w·s + (w·e)t ≥ 0` since `s ≥ 0`, `e ≥ 0`; `x`-tube in `[0,∞)`; successor aggregate `w·(s+e) ≥ 0` and physical membership). Let `s_1 + s_2 ≥ 2`. If `s_1 ≥ 2` or `s_2 ≥ 2`, `FAST`/`SLOW` is typed-admissible by (1), hence aggregate-safe for every `w` by Theorem A(i). Otherwise `0 < s_1, s_2 < 2` (positivity: `s_i ≥ 0` and `s_1+s_2 ≥ 2` with both below `2` forces both above `0`), and for `w = (w_1, w_2) ∈ C` with `r = w_2/w_1 ∈ [0, ∞]` (the cases `w_1 = 0`, `w_2 = 0` are `r = ∞`, `r = 0`):

  - `FAST` aggregate-safe ⟺ `min_{t,d} [w_1 s_1(t) + w_2 s_2(t)] ≥ 0` ⟺ `w_1(s_1 − 2) + w_2 s_2 ≥ 0` ⟺ `r ≥ ρ_1` (for `w_1 > 0`; for `w_1 = 0` the minimum is `w_2 s_2 ≥ 0`, always safe);
  - `SLOW` aggregate-safe ⟺ `w_1 s_1 + w_2(s_2 − 2) ≥ 0` ⟺ `r ≤ ρ_2` (for `w_2 > 0`; for `w_2 = 0` always safe).

  Since `ρ_2 ≥ ρ_1 ⟺ s_1 s_2 ≥ (2−s_1)(2−s_2) ⟺ s_1 + s_2 ≥ 2` (expand: `s_1s_2 ≥ 4 − 2s_1 − 2s_2 + s_1s_2`), every `r ∈ [0, ∞]` satisfies `r ≤ ρ_2` or `r ≥ ρ_1`. Terminal aggregates: `w·(s+e) ≥ 0` on `X_0`. So every `w ∈ C` admits an aggregate-safe action.
  `⊇`: let `x < 1` and `s_1 + s_2 < 2` (in particular `s_1, s_2 < 2`). At `w = (1,1)`: `FAST` needs `s_1 + s_2 ≥ 2` (fails); `SLOW` needs `s_1 + s_2 ≥ 2` (fails); `STAGED` needs the physical tube safe, i.e. `x ≥ 1` (fails — and `S^w ⊆ S^phys`, so no aggregate floor can compensate a physical violation); `NO-SWITCH` misses `G^w` (`q = 0`). So `P_w` fails at `w = (1,1)` and the state is in no `W^w`.

(3) From any `X_0` state, `FAST` is physically admissible: the `x`-tube is the singleton `{x} ⊆ [0, ∞)`, and the successor's physical coordinates `(1, x)` lie in `G^phys`. So `P_phys` holds on all of `X_0`.

(4) Immediate from (1)–(2): `FP = ({x ≥ 1} ∪ {s_1+s_2 ≥ 2}) \ ({x ≥ 1} ∪ {s_1 ≥ 2} ∪ {s_2 ≥ 2})` and `{s_i ≥ 2} ⊆ {s_1+s_2 ≥ 2}` on `X_0`. The interior point: `6/5 < 2`, `12/5 > 2`, `x = ½ < 1`.

(5) The point `(½, 1/10, 1/10)`: `P_phys` by (3); at `w = (1,1)`, `s_1+s_2 = 1/5 < 2` and `x < 1`, so no aggregate-safe action by the argument of (2)⊇. Hence `⋂_w W^w ⊊ W^phys`. And `FP ⊆ ⋂_w W^w \ W^typ` by (1)–(2), nonempty by (4).

(6) The displayed biconditionals are the two computations of (2) with `w_1, w_2 > 0`. `ρ_2 ≥ ρ_1` is the coverage condition; on the interior it is strict, so `{r < ρ_1} ≠ ∅` (SLOW-only) and `{r > ρ_2} ≠ ∅` (FAST-only), while `[ρ_1, ρ_2] ≠ ∅` (both). If a single action served every `w`, it would lie in `⋂_w E_w = E_typ`, contradicting (1) since `s_1 < 2, s_2 < 2, x < 1`.

(7) On `R`: `STAGED`'s tubes are `[s_1, s_1+e_1]`, `[s_2, s_2+e_2]`, `[x−1, x] ⊆ [0, ∞)` (as `x ≥ 1`), and the successor `(1, x−1, s+e) ∈ G`; so `P_typ` holds. On `I`: the four exhibited violations are the four computations above — each is an exhibited violated constraint of a distinct action, and the actions exhaust `A_0`; this is the negative-certificate form (each rejection is witnessed, not merely asserted). ∎

**Reading of Theorem B.** The aggregate assessment's binding condition on the triangle is the **total-capital budget** `s_1 + s_2 ≥ 2` (at the worst weight `w = (1,1)` the two plans need the same budget, and every other weight is relieved by one plan or the other). The noncompensatory assessment instead requires **one floor to survive its own worst-case dip** (`s_1 ≥ 2` or `s_2 ≥ 2`) or **the bridging resource** (`x ≥ 1`). The triangle between the coordinate thresholds and the budget line is exactly the region where the weak doctrine certifies a transition (per price vector, with price-dependent plans) that the strong doctrine rejects — and the typed recursion does not merely reject: it names the binding resource (`x` at cost `c`) and the exact subregion (`x ≥ 1`) where funding the bridge converts the false positive into a certified typed transformation.

## 7. Theorem C (propagation through the backward induction)

**Theorem C.** Let the datum be extended to `m ≥ 2` intervals by prepending `m−1` **hold intervals**: on `[t_j, t_{j+1})` for `j < m−1` the sole action is `HOLD` with constant tube `{z}` and successor `{z}`, safe set `S_j = S_0`, and the disturbance set unused (declared single benign branch); the last interval carries the datum `𝒟`. Define `W^phys_j, W^w_j, W^typ_j` by each assessment's own backward recursion (`W_m^·` the respective terminal set; `W^w_m = G^phys ∩ {w·s ≥ 0}`, `W^phys_m = G^phys`, `W^typ_m = G`). Then:

**(i)** for every `j`: `W^typ_j ⊆ ⋂_{w∈C} W^w_j ⊆ W^phys_j`;

**(ii)** the stage-0 regions are the stage-`(m−1)` regions pulled back through the holds: `W^·_j = W^·_{j+1} ∩ S_0` for the typed recursion (and the analogous statement with `S^w`, `S^phys` for the scalarized and physical recursions), so the strictness witnesses of Theorem B(5) persist at every stage: a state may hold through the earlier intervals and face the witness interval with the same separation;

**(iii)** the separation is therefore not an artifact of the one-interval framing: the assessment hierarchy holds at every stage of every multi-interval typed exact-tube datum, and the false-positive phenomenon survives arbitrary hold prefixes.

*Proof.* (i) Induction downward. Base `j = m`: `G = G^phys ∩ {s ≥ 0} ⊆ G^phys ∩ {w·s ≥ 0} ⊆ G^phys` by Lemma 3. Step: assume `W^typ_{j+1} ⊆ W^w_{j+1} ⊆ W^phys_{j+1}`. If `z ∈ W^typ_j`, some action `a` has, for all `d`, `Tube ⊆ S_j ⊆ S^w_j` (Lemma 3, ⇒) and `Succ ⊆ W^typ_{j+1} ⊆ W^w_{j+1}`, so `a` witnesses `z ∈ W^w_j`. The second inclusion is identical with `S^w_j ⊆ S^phys_j`. (ii) `HOLD` is the unique action; it is assessment-admissible for assessment `·` iff `{z} ⊆ S_j^·` and `z ∈ W^·_{j+1}`; for the last interval the datum `𝒟` applies. (iii) follows: the strictness witnesses of Theorem B lie in `S_0` (their floors are met initially), so they hold through the prefix and realize the same stage-0 strictness. ∎

The general statement of (i) — hierarchy at every stage of **every** multi-interval datum, not only hold-prefixed ones — uses only the induction step above, which does not reference the hold structure; the hold prefix is needed only for strictness propagation (ii).

## 8. Interpretation for sustainability assessment

1. **Weak vs strong, formalized dynamically.** The scalarized assessments are the weak-sustainability doctrine in its exact robust form: one index `w·s` (prices may be zero — the closed cone), floors substitutable at those prices, disturbances respected. The typed registry is the strong-sustainability doctrine: each critical floor separately binding (noncompensatory). Theorem B then reads: *the two doctrines can disagree on the same transition system with the same robustness standard and the same action set, in the direction weak-accepts/strong-rejects, on a set with interior, and the disagreement is not a knife-edge artifact of one bad price vector — every price vector accepts, each licensing its own physical plan.* The plans are genuinely different transitions (`FAST` and `SLOW` violate different floors at different times — asynchronous dips), which is the dynamic formalization of compensation across incommensurable capitals.
2. **The disagreement's precise seat.** By Theorem A(ii) the gap is *exactly* the noncommutativity of "choose a plan" with "for all prices". At the static level the closed-cone aggregate is lossless (Lemma 3). The weak doctrine's blind spot is therefore not the existence of an aggregate index but the *policy dependence of the aggregate-optimal transition*: there is no single transition that is weakly safe for all prices, precisely because each price vector's optimal transition compensates differently. This sharpens the standard sustainability-economics critique of aggregate indices into a proved feasibility separation.
3. **Endpoint-only accounting is a strictly weaker audit level.** `W^phys` is the endpoint-accounting assessment (arrival feasibility in physical coordinates). Theorem B(5): it is strictly coarser than even the scalarized family — it admits transitions that no aggregate assessment certifies (the `(½, 1/10, 1/10)` witness: every aggregate rejects it, endpoint-only accepts). The three audit levels — endpoint-only, scalarized, noncompensatory — form a strictly decreasing sequence of admitted sets on one transparent datum.
4. **Rejection with a rescue address.** The typed recursion's output on the triangle is not a bare rejection: it is the negative certificate (four exhibited per-action violations) plus the binding resource and price (`x ≥ c`) at which the bridging action converts the false-positive set into certified typed transformations (`R`). This is the assessment-side form of the programme's negative-certificate discipline: complexity is retained only when it is earned — here, the bridge is earned exactly when the physical budget funds it.
5. **No transfer claim.** Theorem B is a theorem about the assessment operators on a declared datum. It transfers to no empirical system and asserts nothing about cod 2J3KL or the Edwards aquifer; its role in the programme is Paper 1's independent mathematical content (the assessment hierarchy) together with its witness instantiation.

## 9. Failure conditions and exclusions

The theorems do not claim, and the proofs do not support:

- **no claim of aggregate blindness at fixed trajectories:** for a *fixed* plan the closed-cone aggregates are lossless (Lemma 3); the gap needs the existential plan quantifier (Theorem A(ii));
- **no separation on every datum:** on data where a single action dominates (e.g. a plan safe for all weights exists), the assessments coincide; the theorem is an existence separation with interior, plus the always-valid hierarchy and localization;
- **no infinite-horizon, stochastic, partial-observation, or endogenous-event extension:** the exclusions of the main theorem file §8 apply verbatim; the disturbance set is finite here and enters only through dip scaling;
- **no claim that the closed-cone choice is the only reasonable aggregate family:** it is the *most permissive* natural family (any subfamily, including strictly positive prices only, is covered a fortiori by Corollary A.1's direction — the intersection over a subfamily is *larger*, so the strictness persists);
- **no measurable-selector claim:** the datum's action sets are finite, so the causal Markov selector of the main theorem exists by choice; no selection theorem is invoked;
- **no welfare or equity claim about the prices:** the weights `w` model assessment doctrines, not normative endorsement; the theorem's content is the separation of the doctrines' feasible sets, not a recommendation among them.

## 10. Paper 1 gate decision

Against the four open items of `paper1_finite_architecture_transformation_theorem.md` §9 and the provisional answer §5's conditions for the broad-methods route:

| gate item | status after this file + companion |
|---|---|
| 1. novelty relative to robust predecessor / reach-avoid-maintain theory | **audited** — the recursion itself remains not-novel (the provisional answer's verdict stands); the present strengthening's novelty is audited at full-text-search level in `paper1_full_text_novelty_pass.md`; the main-theorem file is cited as typed infrastructure, never as a new algorithm |
| 2. nonduplication relative to Paper 2 | **established** — Paper 2's family F02 owns the static compensation logic (its Prop 5.1 is the open-cone static statement; Lemma 3 is its closed-cone complement, proved locally in two lines); the assessment hierarchy, the quantifier localization, the witness datum, the rescue split, and the propagation are stated nowhere in the atlas (verified against the manuscript's §5 and the retained budget) |
| 3. target-journal contribution and length fit | the strengthened contribution profile — a formal separation theorem for sustainability assessment doctrines, with an exact-arithmetic reproducible witness — fits the broad methods/sustainability-theory route named by the provisional answer §5; the manuscript decision is the paper-drafting wave's |
| 4. at least one nontrivial instantiated transformation example | **executed** — the datum `𝒟` is a complete two-architecture instantiation with exact-rational machine verification of every region, witness point, strictness claim, rescue split, and the multi-stage propagation (`paper1_instantiation/`) |

**Decision (internal level):** with the full-text novelty pass recorded in the companion file, Paper 1's independent-result gate is **closed at the internal level**: the strengthened result is (a) mathematically complete, (b) machine-witnessed, (c) nonduplicated within the programme, and (d) audited against the external literatures at the full-text-search level. Paper 1 proceeds to manuscript drafting as a journal article **conditional on the novelty pass's bounded-absence verdicts standing** (see the companion file's status discipline); if external review overturns a bounded-absence verdict, the fallback destination remains the monograph/series introduction, exactly as the architecture doc specifies.

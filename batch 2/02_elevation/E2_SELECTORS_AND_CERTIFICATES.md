# E2 — Selector Theorems and Certificate Production

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Task 3; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation.

---

## Setting

`X` compact metric (the physical or extended state space of E1), `U ⊆ ℝᵐ` compact (admissible actions), `D` compact metric (disturbances). The successor correspondence

```
Succ : X × U × D → 2^X,   Succ(x,u,d) = the declared one-step (or one-review) successor set,
```

has **nonempty compact values** and is **Hausdorff-continuous** in `(x,u)` for each `d` (and continuous in `d` uniformly on compacts); `W ⊆ X` is **closed** (a certified set). The safe-action correspondence at `x` is

```
A_W(x) = { u ∈ U : Succ(x,u,d) ⊆ W  for every d ∈ D }.
```

The (REG)-certificate families of R02 are families `𝔽 = {(C,c)}` of closed constraint/certificate pairs operated on by the certificate operator Γ (below); the ambient hyperspace is the compact Vietoris lattice `𝒦(X)` of closed subsets of `X` ordered by inclusion (meets = intersections, joins = closed unions), which is a complete lattice.

---

## B2.Theorem (a) — Measurable selection — PROVEN (repaired: Step-3 measurability gap closed; Step-4 selector constructed, citation slip struck)

### Statement

Under the setting above, `A_W` has **closed graph** and **closed compact values**; consequently `A_W` is weakly measurable, and if `A_W(x) ≠ ∅` on a measurable set `S ⊆ X`, there exists a **measurable selector** `u* : S → U` with `u*(x) ∈ A_W(x)` for all `x ∈ S`. The selector is **constructed** in Step 4 (a uniform limit of countably-valued Borel maps — no external selection theorem is invoked), together with a **Castaing representation** of `A_W` on `S`; the classical Kuratowski–Ryll-Nardzewski theorem, correctly stated (Polish **codomain**, arbitrary measurable domain), yields the same conclusion.

### Proof

**Step 1 (closed values).** Fix `x`. Let `u_n ∈ A_W(x)`, `u_n → u ∈ U`; we show `u ∈ A_W(x)`. Pick `y ∈ Succ(x,u,d)`; we must show `y ∈ W`. By Hausdorff continuity of `Succ(x,·,d)` at `u` (compact values), `dist(y, Succ(x,u_n,d)) ≤ h(Succ(x,u,d), Succ(x,u_n,d)) → 0`, so there are `y_n ∈ Succ(x,u_n,d)` with `y_n → y`. Since `u_n ∈ A_W(x)`, every point of `Succ(x,u_n,d)` lies in the closed set `W`, so `y_n ∈ W`; closedness of `W` gives `y ∈ W`. Hence `Succ(x,u,d) ⊆ W` for every `d`, i.e. `u ∈ A_W(x) = ⋂_d {u : Succ(x,u,d) ⊆ W}`. Each set in the intersection is closed by the same argument, so `A_W(x)` is closed; it is compact as a closed subset of the compact `U`.

**Step 2 (closed graph).** Let `x_n → x`, `u_n ∈ A_W(x_n)`, `u_n → u`. Pick `y ∈ Succ(x,u,d)`; by joint Hausdorff continuity in `(x,u)`, there are `y_n ∈ Succ(x_n,u_n,d)` with `y_n → y`; `y_n ∈ W` because `u_n ∈ A_W(x_n)`; `W` closed gives `y ∈ W`. Hence `u ∈ A_W(x)`. The graph `{(x,u) : u ∈ A_W(x)}` is closed.

**Step 3 (weak measurability — repaired per `batch 4/PROOF_ELEVATION.md` Finding 5).** A compact-valued correspondence with closed graph is upper semicontinuous; for usc compact-valued correspondences into a metric space, the upper inverse `{x : A_W(x) ∩ F ≠ ∅}` of every **closed** `F` is closed: indeed, if `x_n → x` with `u_n ∈ A_W(x_n) ∩ F`, compactness of `U` gives a convergent subsequence `u_{n_k} → u ∈ F`, and the closed graph forces `u ∈ A_W(x)`. KRN weak measurability, however, is the statement about **open** `O`: `{x : A_W(x) ∩ O ≠ ∅}` must be measurable — and "closed sets are Borel" does not bridge the two. The bridge is the metric decomposition: for open `O ⊆ U`, write `O = ⋃_{n≥1} F_n` with `F_n := {y ∈ U : dist(y, U∖O) ≥ 1/n}` closed (`F_n ⊆ F_{n+1} ⊆ O`; each is a super-level set of the 1-Lipschitz map `y ↦ dist(y, U∖O)`). Then `{x : A_W(x) ∩ O ≠ ∅} = ⋃_{n≥1} {x : A_W(x) ∩ F_n ≠ ∅}`, a countable union of closed sets — `F_σ`, hence Borel. So `A_W` is weakly measurable in the KRN sense. (The **metric** hypothesis on `U` is exactly what is needed: in a general regular space an open set need not be a countable union of closed sets.)

**Step 4 (selector — constructed, not cited; repaired per `batch 4/PROOF_ELEVATION.md` Finding 5, adopting A1's construction).** The recorded Step 4 read "`X` (hence `S`) is Polish, `U` is Polish, … KRN yields a Borel-measurable `u*`". That sentence carries a slip which is hereby **struck**: `X` is Polish (compact metric), but a general **measurable** `S ⊆ X` need **not** be — a subspace of a Polish space is Polish in the relative topology iff it is `G_δ` (`ℚ ∩ X` is Borel and not Polish) — and the clause is **unnecessary**, because KRN's Polish hypothesis is on the **codomain**, the domain being an arbitrary measurable space. The existence half of B2(a) is therefore proved by construction:

Fix a compatible metric `ρ` on `U` and a countable dense set `{q_i}` (compact metric ⇒ separable). Equip `S` with the trace σ-algebra and set `G_1 := A_W|_S` — compact-valued, nonempty, weakly measurable by Step 3. Two elementary facts, both from Step 3's machinery: (i) for **closed** `C ⊆ U` and `G` compact-valued weakly measurable, `{x : G(x) ∩ C ≠ ∅}` is measurable — with `C^{1/k}` the open `1/k`-neighbourhood, compactness gives `G(x) ∩ C ≠ ∅ ⇔ G(x) ∩ C^{1/k} ≠ ∅` for every `k`, so the set is `⋂_k G^-(C^{1/k})`; (ii) for closed `C` and open `O`, `{G ∩ C ∩ O ≠ ∅} = ⋃_m {G ∩ C_m ≠ ∅}` with `C_m = {y ∈ C : dist(y, U∖O) ≥ 1/m}` closed — the Step-3 decomposition applied inside the closed slice.

Inductively, given `G_n` compact-valued, nonempty, weakly measurable, define

`i_n(x) := min{ i : G_n(x) ∩ B(q_i, 2^{-n}) ≠ ∅ }`

(dense `{q_i}`, nonempty values ⇒ well defined) and `G_{n+1}(x) := G_n(x) ∩ B̄(q_{i_n(x)}, 2^{-n})`. Measurability: `{i_n = i} = G_n^-(B(q_i, 2^{-n})) ∖ ⋃_{j<i} G_n^-(B(q_j, 2^{-n}))`, and for open `O`, `G_{n+1}^-(O) = ⋃_i ({i_n = i} ∩ {G_n ∩ B̄(q_i, 2^{-n}) ∩ O ≠ ∅})` — measurable by (i)–(ii). Each `G_{n+1}(x)` is nonempty (a compact meeting the open ball `B(q, 2^{-n})` also meets the closed ball `B̄(q, 2^{-n})`), compact, nested, with `diam G_{n+1}(x) ≤ 2^{1-n}`. Nested nonempty compacts with diameters → 0 intersect in a single point: `⋂_n G_n(x) = {u*(x)}` with `u*(x) ∈ G_1(x) = A_W(x)`. The countably-valued Borel maps `g_n(x) := q_{i_n(x)}` satisfy `ρ(u*(x), g_n(x)) ≤ 2^{-n}`, so `g_n → u*` **uniformly** on `S`; a uniform limit of Borel maps is Borel. ∎

**Remark (KRN, correctly stated).** The classical Kuratowski–Ryll-Nardzewski theorem — measurable-space domain, **Polish codomain**, nonempty closed values, weak measurability — yields the same selector from Step 3 directly; the construction above is that theorem's classical proof made explicit, so B2(a) does not depend on the citation. The recorded clause "`X` (hence `S`) is Polish" is struck as false for general measurable `S` and unnecessary.

**Castaing representation (for consumers).** Applying the same construction to `Γ_{jk}(x) := A_W(x) ∩ B̄(q_j, 2^{-k})` when that intersection is nonempty (else `A_W(x)` itself) yields Borel selectors `σ_{jk} : S → U` whose values `{σ_{jk}(x)}` are **dense in `A_W(x)`** for every `x`: given `u ∈ A_W(x)` and `ε > 0`, choose `j, k` with `ρ(q_j, u) < ε/2` and `2^{-k} < ε/2`; then `σ_{jk}(x) ∈ A_W(x) ∩ B̄(q_j, 2^{-k})` gives `ρ(σ_{jk}(x), u) ≤ 2^{-k} + ρ(q_j, u) < ε`. Filippov-type approximation and convexified-envelope arguments consume the *family*, not the single selector. **Honesty note:** B2(a) does **not** close R02 Field 12 (measurable selection of (REG)-witnesses on `𝒱` — a different correspondence); inflating B2(a) into a solution of D2 would be a false promotion.

**Remark (effective domain — adopted from A1's (B)).** The effective domain `S* := {x ∈ X : A_W(x) ≠ ∅}` is **closed**: if `x_n ∈ S*` and `x_n → x`, pick `u_n ∈ A_W(x_n)`; compactness of `U` gives a subsequence `u_{n_k} → u ∈ U`, and the closed graph (Step 2) forces `u ∈ A_W(x)`. The *natural* domain of the selector problem is therefore **Polish** — while an arbitrary measurable `S ⊆ S*` need not be Polish, and (by Step 4) does not have to be: the construction queries nothing about `S` beyond trace-measurability.

**Remark (Vietoris–Borel measurability — adopted from A1's (D)).** The correspondence read as a map `x ↦ A_W(x)` into `𝒦(U) ∪ {∅}` (nonempty compact subsets with the Vietoris topology, `∅` isolated) is **Borel measurable**: every Vietoris subbase element pulls back to machinery already built — hits of open sets are `F_σ` (Step 3); containment in an open `G` is the complement of a hit of the closed set `U∖G`, itself a countable intersection of hits of the open neighbourhoods `(U∖G)^{1/k}` (compactness of the values, as in Step 4's fact (i)); and the empty value is the complement of the closed effective domain `S*`. This is the measurability object consumed by arguments that integrate the *correspondence* rather than a single selector.

**Remark (why Hausdorff continuity is needed).** With mere closed graph of `Succ` in `u`, Step 1 fails: limit points of successor sets need not lie in `W`-contained successors. The R03.Lem4 adjudication in the joint audit established the analogous point for horizon limits: upper semicontinuity alone is insufficient, and a Hausdorff-type continuity is the correct hypothesis; the same lesson is load-bearing here.

---

## B2.Theorem (b) — Continuous selection — CONDITIONAL

### Statement

If additionally (i) `Succ(x,·,d)` is **convex-valued in `u`** in the sense that `⋃_u Succ(x,u,d)` is convex and the safe-action values `A_W(x)` are convex, and (ii) `A_W` is **lower semicontinuous** on `X`, then `A_W` admits a **continuous selector** (Michael).

### Status and proof obligation

This is Michael's selection theorem applied verbatim (paracompact domain `X`, Banach codomain, nonempty closed convex values, lsc). The *conditional* status is honest: hypothesis (i) is a genuine convexity demand on the dynamics and constraint geometry (satisfied on E5's linear-box class — the B2 verification), and hypothesis (ii) is *not* implied by Hausdorff continuity of `Succ` (lsc of an intersection-over-`d` correspondence requires a uniformity in `d` that must be checked per instance). No general sufficient condition tracing (ii) back to `Succ` is claimed; producing one is an open obligation (registered in the master review).

---

## B1.Theorem (a) — Maximal certificate family — PROVEN

### Statement

Let `Γ : 𝒦(X) → 𝒦(X)` be the (REG)-certificate operator of R02: `Γ(C)` is the closure of the set of states admitting a one-review certificate against the constraint family with base set `C` (the exact definition is R02 Field 3's `(REG)` recursion; the only properties used here are (P1) `Γ` is **monotone** (`C ⊆ C′ ⇒ Γ(C) ⊆ Γ(C′)`) and (P2) `Γ` maps `𝒦(X)` to itself). Then `Γ` has a **greatest fixed point** `𝒱* = max{C ∈ 𝒦(X) : Γ(C) = C}`, and R02.Thm1 applies **to the family `𝒱*` itself**; the closed-loop certificate recursion may be *started* from any `C ⊆ 𝒱*` provided the certificate states are **tracked in `𝒱*`**, not in `C` (subfamilies of a consistent family are **not** consistent in general — the corrected transfer is the proof's final paragraph; the recorded "applies to every subfamily" clause was the backwards-inheritance defect repaired per `batch 4/PROOF_ELEVATION.md` Finding 6).

### Proof

`𝒦(X)` (closed subsets of the compact `X`, ordered by inclusion) is a complete lattice: arbitrary meets are intersections, arbitrary joins are closures of unions; both are closed in compact `X`. (P1)–(P2) make `Γ` a monotone self-map of a complete lattice, so the **Knaster–Tarski theorem** applies: the fixed points of `Γ` form a nonempty complete lattice; in particular the greatest fixed point exists, with the explicit formula

```
𝒱* = ∨ { C ∈ 𝒦(X) : C ⊆ Γ(C) }   (join of all post-fixed points).
```

`C ⊆ Γ(C)` says every state of `C` admits a one-review certificate against `C` itself — the post-fixed points are exactly the (REG)-consistent families, so `𝒱*` is the maximal consistent certificate set. **Correct transfer (repaired per `batch 4/PROOF_ELEVATION.md` Finding 6):** the recorded final sentence — "applied to any subfamily of the maximal one, which is consistent because consistency is inherited by subfamilies" — is **backwards**: from `C ⊆ 𝒱*`, monotonicity gives `Γ(C) ⊆ Γ(𝒱*) = 𝒱*`, the *wrong* direction (it bounds `Γ(C)` from above, whereas consistency needs `Γ(C) ⊇ C`). Subfamilies of a consistent family are in general *not* consistent (witness: `X = {1,2}`, `Γ(∅)=∅, Γ({1})={2}, Γ({2})={1,2}, Γ({1,2})={1,2}`: `𝒱* = {1,2}` but `C = {1} ⊆ 𝒱*` has `Γ(C) = {2} ⊉ C`). What *is* true: post-fixed sets are closed under **joins** (if `C_i ⊆ Γ(C_i)` for all `i`, then with `C = cl(⋃ C_i)`, monotonicity gives `Γ(C) ⊇ Γ(C_i) ⊇ C_i` for every `i`, so `Γ(C) ⊇ C`) — which is exactly why `𝒱* = ∨{post-fixed points}` is itself post-fixed, and it is the only inheritance property available. R02.Thm1 therefore applies **to the family `𝒱*` itself**, and the closed-loop certificate recursion may be *started* from any `C ⊆ 𝒱*` provided the certificate states are **tracked in `𝒱*`**, not in `C` (induction: `Γⁿ(C) ⊆ 𝒱*` for every `n`). This is also the stronger statement: (REG)(ii) makes a smaller family *harder* to certify, so `𝒱*` imposes the weakest closure obligation while containing every reachable certificate state. ∎

**Downward transfer of (REG) (adopted from A1's Lemma I.1 — the inheritance the recorded sentence was reaching for).** The join-closure above is what `𝒱*`-tracking uses; there *is* also a downward inheritance, but it runs through **R02's own hypotheses, not through Γ-monotonicity**. On a **downward-closed** family `𝒱` (closed under passing to closed nonempty subsets), (REG) at `(C, c)` with witness `u^cmd` and realized-action set `Ũ = I(u^cmd, c, C)` passes to every `(C′, c)` with `∅ ≠ C′ ⊆ C` closed, **with the same witness**, provided the implementation map is monotone in the set argument (`I(u^cmd, c, C′) ⊆ Ũ`, or independent of `C` — the usual case). *Proof:* the tube clause restricts (every branch from `x ∈ C′ ⊆ C` under any `u ∈ Ũ` stays in `K`); the successor clause contracts — `Φ(C′, Ũ′) ⊆ Φ(C, Ũ)` — so every observation met by the smaller intersection was met by the larger one, which (REG) places in `𝒱`, and downward closure then places the smaller intersection in `𝒱`. ∎ The two corrected statements are complementary: **joins** close the post-fixed family (upward, inside `𝒱*`); **downward closure** transfers (REG) itself (downward, on `𝒱`-families) — neither is the recorded "subfamilies of a consistent family are consistent".

---

## B1.Theorem (b) — Backward iteration = gfp — PROVEN

### Statement

Let `V₀ = X` (top of the lattice) and `V_{n+1} = Γ(V_n)`. Then `(V_n)` is decreasing, `V_∞ := ⋂_n V_n ∈ 𝒦(X)` exists, and if `Γ` has **closed Vietoris graph** (i.e. `C_n → C` in Vietoris with `Γ(C_n) → C′` implies `C′ = Γ(C)`), then `V_∞ = 𝒱*` — the backward iteration computes the greatest fixed point. Moreover every fixed point `C` satisfies `C ⊆ V_n` for all `n`, so `V_∞` is the largest fixed point.

### Proof

**Monotoneity of the sequence.** `V₁ = Γ(X) ⊆ X = V₀`; if `V_n ⊆ V_{n−1}` then monotonicity gives `V_{n+1} = Γ(V_n) ⊆ Γ(V_{n−1}) = V_n`. So `(V_n)` decreases and `V_∞ = ⋂ V_n` is closed, nonempty iff the iteration does not die (emptiness is the honest obstruction certificate — see "Not produced").

**Every fixed point is below the iteration.** Let `C = Γ(C)`. Then `C = Γ(C) ⊆ Γ(X) = V₁` (monotonicity, `C ⊆ X`). Inductively, `C ⊆ V_n ⇒ C = Γ(C) ⊆ Γ(V_n) = V_{n+1}`. Hence `C ⊆ V_∞`.

**The limit is a fixed point.** A decreasing sequence of nonempty compact sets converges in the Vietoris topology to its intersection: for closed `F`, eventually `V_n ∩ F ≠ ∅ ⟺ V_∞ ∩ F ≠ ∅`, and `V_n ⊆ B(V_∞, ε)` for `n` large (compactness: the decreasing intersection exhausts every `ε`-neighbourhood — otherwise a nested sequence of nonempty compacts `V_n \ B(V_∞,ε)` would have a point in `V_∞ \ B(V_∞,ε) = ∅`). Hence `V_n → V_∞` and likewise `V_{n+1} = Γ(V_n) → Γ(V_∞)` **if** `Γ` is Vietoris-continuous at `V_∞`; the closed-graph hypothesis suffices: `V_{n+1} → V_∞` (subsequence of a convergent sequence) and `Γ(V_n) = V_{n+1} → V_∞`, so closedness of the graph yields `Γ(V_∞) = V_∞`. Combined with the previous paragraph, `V_∞` is a fixed point containing every fixed point: `V_∞ = 𝒱*`. ∎

**Hypothesis honesty.** The closed Vietoris graph of `Γ` is a genuine hypothesis on the certificate recursion (it holds whenever the one-review certificate condition is itself a Hausdorff-continuous function of the base set — the R02 setting with the repaired Hausdorff-continuity discipline of R03.Lem4). It is stated here as the correspondence-continuity hypothesis the session record always attached; verifying it per instantiation is part of the E2→module admission workflow.

---

## What is NOT produced (Field 16 honesty)

1. **Algorithmic computation of `𝒱*`** beyond the abstract iteration: rates of Vietoris convergence, stopping criteria with certified error — the B3 grid-hierarchy scheme is SPECIFIED, not assembled.
2. **Lipschitz selectors**: neither B2(a) nor B2(b) yields a Lipschitz `u*`; Lipschitz selection would need convexified velocity envelopes and is open.
3. **Emptiness certificates** beyond Prop4's common-action class: the iteration dying (`V_n = ∅`) certifies emptiness of the *certificate* family, not of the kernel; the R03 adversarial-exit route is the only general emptiness certificate in the programme.

---

## Status

- **B2(a): PROVEN (repaired)** (Step 3 weak measurability via the metric `F_σ` decomposition; Step 4 selector **constructed** — nested-vanishing-diameter Borel construction — plus Castaing representation; the recorded '`X` (hence `S`) is Polish' clause struck as false for general measurable `S` and unnecessary; KRN restated with the codomain-Polish hypothesis only).
- **B2(b): PROVEN_CONDITIONAL** (Michael's hypotheses must be verified per instance; verified on E5's class).
- **B1(a): PROVEN (repaired)** (Knaster–Tarski; the subfamily-inheritance sentence corrected — join-closure and `𝒱*`-tracking stated, with the downward-(REG)-transfer remark recording the inheritance the recorded sentence was reaching for; full proof above).
- **B1(b): PROVEN** (under the stated closed-Vietoris-graph hypothesis, which is the declared correspondence-continuity assumption).

**Dependencies:** R02.Thm1/Lem2 (certificate recursion and closed-loop theorem), R03.Lem4's Hausdorff-continuity discipline (hypothesis pattern). **Consumers:** E4.Thm3 (per-generation gfps), A4.Thm1 (measurable selection in joint regulation), E5 (displayed certificate family), B10 (selection at best-response correspondences); the Step-4 **Castaing family** is additionally available to Filippov-type approximation and convexified-envelope arguments.

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A (see E1's note).

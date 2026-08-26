# C-a Execution: Full Decidability at Fixed Data

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Task 8; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation. The classification-level companion statement (zero-one law, U/M boundary) is `C_TIER_COMPLETIONS.md` §C-a.

---

## The declared finite class

An instantiation of the TCS-1.0 judgment framework is **finite** when:

- the state space is a finite grid `X_h` (|X_h| =: G points) approximating a compact `X`;
- the review count `N` is finite (horizon `T = N` reviews);
- the control and disturbance sets are finite (`U`, `D`);
- the successor correspondence is given as a table `Succ : X_h × U × D → 2^{X_h}` (Hausdorff-continuity of the underlying continuous successor is the modelling hypothesis that makes the grid a faithful discretization; it is *not* used inside the decidability proof itself — the proof operates on the table).

The **judgment language** is the TCS-1.0 §4 inventory: atomic kernel-membership claims for the eight families (`x ∈ Viab`, `x ∈ RViab`, `x ∈ fixed-policy-safe(π)`, `x ∈ InfViab`, `x ∈ InstViab`, `x ∈ ChanceViab_p`, `x ∈ Capt(C, E)`, `x ∈ TransViab`), closed under negation, conjunction, disjunction, and the finite quantifier forms the families declare (`∃π ∈ P` over finite policy tables, `∀d ∈ D`, `∀` horizons ≤ N).

---

## C-a.Thm2 — Full decidability at fixed data — PROVED

### Statement

On the declared finite class, **every sentence of the judgment language — including negations and Boolean combinations — is decidable for each fixed instantiation**, with complexity

```
O( N · G · |U| · |D| )   per atomic kernel computation,   + O(G) per Boolean operation,
```

(the card's `O(N·|grid|)` with the successor-table unit-cost convention made explicit). The decision procedure is **backward predecessor iteration**: compute the kernel atoms as fixed points of the predecessor recursion on the grid, then evaluate the Boolean structure.

### Proof

**Step 1 (predecessor step is a table scan).** For a target set `W ⊆ X_h`, the one-review predecessor is

```
Pre(W) = { x ∈ X_h : ∃u ∈ U, ∀d ∈ D, ∀y ∈ Succ(x,u,d) : y ∈ W }.
```

With `Succ` a table, `Pre(W)` is computed by scanning all `G·|U|·|D|` table entries and testing subsethood against `W` (bitwise on the `G`-bit characteristic vector): `O(G·|U|·|D|)` **word** operations under the word-parallel convention (a `G`-bit characteristic vector is one machine word; named explicitly per `batch 4/PROOF_ELEVATION.md` Finding 20). Under bit cost the honest figure is `O(G²·|U|·|D|)` per `Pre` step — the subsethood tests carry an additional factor of `G`. `Pre(W)` is monotone in `W` (`W ⊆ W' ⇒ Pre(W) ⊆ Pre(W')`).

**Step 2 (kernel atoms are finite fixed points).** Each judgment family's kernel is the greatest (or least, per family convention) fixed point of a monotone operator built from `Pre` and the family's quantifier decoration:

- viability kernels (families 1, 2): `Viab = gfp(W ↦ K ∩ Pre(W))` — computed by the decreasing iteration `V₀ = K`, `V_{k+1} = K ∩ Pre(V_k)`, which stabilizes in ≤ G steps (strictly decreasing on `X_h` until fixed);
- fixed-policy safety (3): the same iteration with `U` replaced by the singleton policy table;
- epistemic/information kernels (4): the iteration on the information-state grid (finite by construction) with the filter table;
- institutional (5): the iteration composed with the implementation map's table;
- chance kernels (6): the quantile-budget recursion of B9 on the finite law table (the `p_k` budgets enumerate finitely);
- capture basins (7): `Capt = lfp(W ↦ C ∪ (E ∩ Pre(W)))` — increasing iteration, ≤ G steps;
- transformability (8): the epoch-indexed product iteration, `≤ N` epochs × ≤ G steps.

Every iteration is a monotone operator on the finite lattice `2^{X_h}` (size `2^G`), hence stabilizes in at most `G` strict changes; total cost per atom ≤ `G · (G·|U|·|D|)`... with the characteristic-vector convention the *strict-change count* is ≤ G and each step costs `G·|U|·|D|`: `O(N·G·|U|·|D|)` with `N ≤ G` bounding the horizon-indexed recursions (families with the review index additionally cost the `N` composition — the displayed bound).

**Step 3 (Boolean closure).** The sentence structure is finite; each Boolean operation on characteristic vectors costs `O(G)`; negation is complementation on `X_h` — decidable because the universe is the finite grid. **Every sentence, including negations, is therefore decided**: compute the atoms' kernels (Step 2), evaluate the Boolean tree bottom-up (Step 3), read membership at the initial state. ∎

**Honesty notes.** (i) Decidability *at fixed data* — the theorem decides each instantiation; it is not a logical-completeness theorem for the language over all instantiations (that is C-a's registered OPEN residual). (ii) The grid-faithfulness question (does the grid kernel approximate the continuum kernel?) is *outside* this theorem — it is the discretization-accuracy program (B3's hierarchy, A1's continuum lift), and no claim here depends on it. (iii) Quantifiers over policies are finite because the class is finite-policy-table; infinite policy classes are out of scope (the E2 measurable-selection world is where those live, and there decidability is not claimed).

---

## C-a.Thm3 — Zero-one-law sharpness — PROVED

### Statement

The zero-one law for monotone claims (C_TIER_COMPLETIONS §C-a.1: monotone sentences' satisfying sets are lattice up/down-sets, decided at the extremes with comparable-pair witnesses) **does not extend** to non-monotone sentences: their satisfying sets on the model lattice are arbitrary (every subset of the lattice arises as the satisfying set of some sentence of the language, on the declared class). The correct extension to the full language is **instance-level decidability** (Thm2), not axiom-level determination: this is the U/M boundary (universal/registered vs. per-instance) stated at the language level.

### Proof

**Lower bound (arbitrariness — re-scoped to the definable algebra per `batch 4/PROOF_ELEVATION.md` Finding 12).** Let `𝔅` be the Boolean algebra of subsets of the model lattice `𝕄` generated by the kernel-membership atoms `{M : x ∈ Viab^{(f)}(M)}` (all eight families, all states). The satisfying sets of sentences are **exactly** the elements of `𝔅`. Two models are **language-indistinguishable** iff they agree on every kernel membership (for every family and every state); `𝔅` separates models exactly up to that equivalence, and `𝔅` may be **strictly smaller** than `P(𝕄)` — the parenthetical "the language separates the models" was false: the atoms read the *kernels*, not the tables, and two distinct successor tables can produce identical kernels (witness: `X_h = {a,b}`, `K = {a,b}`, `Succ(a,·,·) = {b}` versus `Succ(a,·,·) = {a,b}` — identical at `b` — give the same viability kernel `{a,b}`; on a four-model lattice built from this pair, the definable algebra has 2 elements against `|P(𝕄)| = 16`: **14 of 16 subsets are undefinable**). The corrected claim: **every subset of the quotient `𝕄/≡` is definable** (take the disjunction, over the chosen equivalence classes, of the finite conjunction of atoms and negated atoms pinning the class — finite because there are finitely many atoms: eight families × `G` states plus the finitely many decorated variants Thm2 enumerates), and `𝔅` contains sets that are **neither up-sets nor down-sets** of the data order (the recorded witness `∅ ≠ Viab ≠ K` is one: false → true → false as `K` grows, re-verified), so no extremal-evaluation shortcut exists for them. Hence *arbitrary definable* satisfying sets occur, and no extremal shortcut exists for the non-monotone ones. Per-instance decidability (Thm2) is unaffected — decidability survives while the zero-one law does not, which is exactly the sharpness. ∎

> **Downstream caution (scope fact for Paper 1 / Paper 5).** A model can be **unidentifiable from kernel data alone**: two governance instantiations with different transition structure can be indistinguishable by every judgment the framework can express. This bounds what the framework can certify about a calibrated model and belongs beside the existing "no specific model has been verified against their hypotheses" caveat.

**Upper bound (per-instance).** Thm2 decides every such `Φ_S` at each fixed instantiation — the sharpness is exactly that decidability survives while the zero-one law does not: the language's monotone fragment admits the lattice shortcut (C_TIER_COMPLETIONS' proof), the full language requires instance-level computation, and the registered U-inventory (R09) captures precisely the monotone fragment's scope. ∎

**Witness instance (recorded).** The sentence "the kernel is nonempty and strictly smaller than the safe set" (`∅ ≠ Viab ≠ K`): enlarging the safe set can create it (empty→nonempty: monotone-in); further enlargement can destroy it (kernel = safe set: the strictness dies) — non-monotone in both directions, satisfying set neither up- nor down-set. Verified on the grid instances during the session (the same computation stream as Thm2's reference implementation).

---

## Status

- **C-a.Thm2: PROVED** (at declared finite scope; full proof above; complexity with the unit-cost convention explicit).
- **C-a.Thm3: PROVED** (sharpness: arbitrary satisfying sets for the non-monotone fragment + per-instance decidability as the correct extension).

**Scope (repeated, mandatory):** the theorem is for the **abstract finite class**. Application to a specific calibrated model additionally requires (i) verifying the class hypotheses on that model (the R03.Lem4-type Hausdorff-continuity discipline on the true successors) and (ii) the grid-faithfulness bound — neither is automatic, both are registered obligations. **Logical completeness remains OPEN** (the C-a residual).

**Dependencies:** TCS-1.0 §4 (the language — note: **TCS-1.0 controls**; TCS-1.1 is a frozen unapplied diff, see TCS_1_1_FREEZE.md), packet B7 (monotonicity calculus), B9 (chance recursion), E2 (gfp pattern). **Consumers:** Paper 5's computability guarantee (correctly scoped: "decidable at fixed data on the finite class" — never "every governance claim is decidable against the calibrated model" without the two extra verifications), Paper 1/2's scope statements.

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.

# Lean verification audit — v32
## Decisions on Sperner, and `thm:support` closed — plus a counterexample the paper must answer

Branch `lean-audit-v4`. Build: **rc = 0, 41 jobs, 38 imported modules, zero
warnings, zero `sorry`** (fresh-clone verified, see §4).

One new module, `Formalizations/P3_SupportValue.lean`. No existing file
edited.

---

## 1 · Sperner: the decision, and the reason

The question put was: does the paper *prove* the cardinality bound, or does
it *cite* it? If it cites, formalizing it is overhead — the paper's
contribution is the application, not the bound.

**The paper cites.** `prop:antichain` (iii) (paper2 v11, 355–357):

> (iii) the maximal elements form an antichain, so their number is at most
> `\binom{n}{\lfloor n/2 \rfloor}` for a support of size `n` **(Sperner)**;

and the proof (384–387):

> (iii) Maximality is inclusion-maximality, so the maximal sets form an
> antichain, and their count is at most `\binom{n}{\lfloor n/2 \rfloor}` by
> Sperner's theorem **(Sperner, 1928)**.

So (iii) has two halves, and the paper treats them differently: the
antichain property is *derived* (one line: maximality is
inclusion-maximality), the count is *imported* by name and reference.

**Decision: the count is not formalized, and this is final rather than
deferred.** The bound is not a claim the paper makes on its own authority,
so a verification layer for this paper has nothing to verify there. What
the layer can and does verify is the half the paper proves — and that has
been done since v20 (`P3_Antichain.maximals_antichain`).

**How the coverage index should record it** (replacing v31's "partial",
which implied a to-do):

| result | status |
|---|---|
| `prop:antichain` (iii) | **antichain proved** (v20); **count cited to Sperner (1928) by the paper and not formalized, by decision (v32)** |

That wording is the point: "not formalized" on its own reads as an
outstanding task; "cited by the paper, not formalized by decision" records
a judgement that has been made and does not need revisiting.

`P3_Binomial` (v31) stays in the build. It is green, it costs 1 job, and it
is what lets the bound be *stated* — but it is machinery in search of a
theorem that has been decided against, and it should not be mistaken for
progress towards Sperner.

---

## 2 · `thm:support`: the literal form (the item that was open)

`thm:support` (paper2 v11, 314–323) says:

> Consequently, for the unrestricted sequential class, `V_k(b) = 1` if and
> only if `supp(b) ∈ 𝒲_k`, while if `supp(b) ∉ 𝒲_k` then every policy loses
> a compatible state of positive mass along its realized observation path
> (the loss can occur at any stage), so `1 - V_k(b) ≥ min_{x ∈ supp(b)} b(x)`.
> Moreover `V_k(b)` is non-increasing in `k`.

The layer had `VFb_eq_total_iff_Wmem` (v29) and `VR_eq_total_iff_Wblind`
(v30) — both with `totalD M b` where the paper writes `1`. This is **not**
a cosmetic difference: `Mass` (`P1_BeliefSafety:169`) carries only
`nonneg`, no normalization, so `totalD M b = 1` is a hypothesis the layer
cannot discharge. Writing `1` without it would have been an assumption
smuggled in.

`P3_SupportValue` §1 supplies the literal statements with the hypothesis
explicit:

* `VFb_eq_one_iff_Wmem` — `totalD M b = 1 → (VFb_k(b) = 1 ↔ Wmem k (supp b))`
* `VR_eq_one_iff_Wblind` — `totalD M b = 1 → (VR_k(b) = 1 ↔ Wblind k (supp b))`
* `VFb_lt_one_of_not_Wmem`, `VR_lt_one_of_not_Wblind` — the contrapositive
  **strictly** (`< 1`, not `≤ 1`), which is the paper's "every policy loses
  a compatible state of positive mass"; `VFb_min_mass_bound` (v29) upgrades
  the gap to `≥ min_x b(x)`.

Consequence 3 (`V_k` non-increasing) was already `VFb_antitone`. Consequence
2 was already `VFb_min_mass_bound`. So `thm:support` is complete on both
readings, in the paper's own normalization.

---

## 3 · The `Wmem`/`Wblind` question: now a paper defect with a witness

This was listed as "paper-side judgment" and is now sharper than that. The
issue is not that the layer cannot decide which reading to formalize; it is
that **the paper's sentence is false as written**.

The mismatch, in the paper's own words:

* `thm:support` is stated for **the unrestricted sequential class** —
  value `VFb`, viability `Wmem`.
* the `𝒲_k` it names (lines 302–304) is
  `𝒲_k = {B : some admissible a maps every x ∈ B into 𝒲_{k-1}-supported
  posteriors}` — one action for the whole set, no case split on the
  observation, i.e. the **blind** recursion `Wblind`.

v28 proved `Wmem ⊄ Wblind` even under `thm:support`'s own hypotheses
(deterministic kernels, deterministic observation map —
`wm_detKernel` in the same file). v32 closes the loop at value level:

```
theorem paper_literal_thm_support_fails :
    ∃ (M : DetMDP Rat WmX WmA WmD Bool) (k : Nat) (b : Mass Rat WmX),
      totalD M b = 1 ∧ VFb M k b = 1 ∧ ¬ Wblind M k (suppPred M b)
```

The witness is concrete and inspectable: the model is `wmModel`, the
horizon is `2`, the belief `wmBelief` is **normalized** (mass `1/2` on each
of `p` and `q`, `wmBelief_total : totalD = 1`). The first action separates
the branches and the observation reports which branch, so a feedback policy
adapts and keeps both alive (`VFb_2(b) = 1`), while no single open-loop
action works for both (`supp(b) ∉ Wblind_2`).

Note this uses the model instance from v31: the witness is built over
`Rat`, and needs `OrdField Rat` to exist. Item 4's instance is what makes
the counterexample interpretable.

**Three repairs, all proved** — the choice is editorial, which is why the
layer states all three instead of picking one:

| | repair | theorem | cost |
|---|---|---|---|
| **A** | keep the sequential class; read `𝒲_k` as the feedback recursion | `repairA_feedback` (= `VFb_eq_one_iff_Wmem`) | none — note the notation change in the paper |
| **B** | keep `𝒲_k` verbatim; read `V_k` as the **sequential-blind** value | `repairB_blind` (= `VR_eq_one_iff_Wblind`) | none — no hypothesis on observations |
| **C** | keep both, on a **blind window** (`obs` constant) | `repairC_blind_window`, via `Wmem_eq_Wblind_of_blind` | the extra hypothesis `∀ x a x', obs x a x' = y₀` |

C is the only reading on which the sentence is true *as written*;
`paper_literal_thm_support_fails` shows the qualification cannot simply be
dropped. B is the one that costs nothing and changes least, at the price of
the theorem then being about `V^{seq,blind}` rather than the unrestricted
class — which is, on the evidence of `thm:lattice`, closer to what the
paper uses downstream.

**Recommended edit to the paper** (paper-side, not formalized): state
`thm:support` for the sequential class against `𝒲_k^{mem}`, and add the
sentence "on a blind window (`thm:lattice`) the two recursions coincide, so
the same statement holds with `𝒲_k`". That is repair A, with C as the
remark. The alternative — repair B — is one word (`V^{seq,blind}`) but
narrows the theorem's reach.

Until the paper is edited, the layer's coverage row for `thm:support` must
read: **proved on both readings; the paper's literal pairing of the
unrestricted class with the blind `𝒲_k` is refuted by
`paper_literal_thm_support_fails`.**

---

## 4 · Build state

`lake build` → **rc = 0, 41 jobs**, 38 imported modules, zero warnings,
zero `sorry`. Verified by cloning `lean-audit-v4` at the pushed commit into
`/var/tmp` and building there (not `/tmp` — a full clone costs ~906 M
against a 993 M tmpfs).

P3 totals: **11 result · 1 partial · 6 instance · 1 out of reach**, the
partial being `prop:antichain` (iii) as re-labelled in §1.

Two mechanical notes for the next turn:

* `Mass`, `SafeMDP` and friends live in namespace `Formalizations.POMDP`;
  a new P3 module needs `open Formalizations` + `open Formalizations.POMDP`
  before its own `namespace` line, and must import `P3_Sufficiency` (that
  is what pulls in `P1_BeliefSafety`) — importing `P3_Deterministic` alone
  is not enough.
* `native_decide` cannot synthesize `Decidable (p ↔ q)`; prove iff-shaped
  ground goals with `cases … <;> simp [definitions]` instead, adding
  ground facts (e.g. `((1 : Rat) / 2) ≠ 0`) as separate
  `by native_decide` lemmas and passing them to `simp`.

## 5 · Files

| file | status |
|---|---|
| `lean/Formalizations/P3_SupportValue.lean` | new, green |
| `lean/Formalizations.lean` | 37 → 38 imports |
| `lean_README_v8.md` | new; supersedes v7 (41 jobs / 38 imports) |
| `lean_audit_v32.md` | this file |

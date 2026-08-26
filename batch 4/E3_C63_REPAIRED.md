# E3.C6.3 — Delayed-Revelation Lemma: REPAIRED

**Target.** The `C6.3` subsection of `batch 2/02_elevation/E3_CLASSIFICATION_THEOREMS.md`, and the manifest row `E3.C6.3` (line 80).

**This file is a proposal. No repository file has been modified.**

**Disposition.** The forward direction is essentially correct. The converse is **not proved** — it is supported by citing `R02.Prop3` as a witness, which is an example, not an argument. The repair replaces the informal "iff" with an **exact characterisation** whose two directions are both proved directly, and identifies the correct hypothesis, which is neither the one stated nor as strong.

**Verification.** `reaudit/verify_e3cfb7_repair.py`, Part A, 12 assertions, exit 0.

---

## 1. The defect

The record states inertness — `Viab_del = Viab_full` — "iff no trajectory starting in the kernel can hit the obstruction set `X ∖ K` before `t_d` under *any* policy admissible for the prior", and proves:

- **(⟸)** by concatenating "any safe prior-admissible policy on `[0,t_d)`" with the full-information policy afterwards;
- **(⟹)** by assertion: "the uninformed policy must hedge against all revelations … and the `R02.Prop3` construction … exhibits a strictly smaller delayed kernel."

Two problems. The (⟹) direction is an example, not a proof. And the (⟸) argument is incomplete: concatenating a prior-admissible policy that merely stays in `K` does not guarantee the state at `t_d` is still **full-viable**, which is what the second half of the policy needs. The hypothesis as stated ("no trajectory under *any* prior-admissible policy hits `X ∖ K`") is also far stronger than the conclusion requires — it quantifies over *all* prior-admissible policies, when only one is needed.

---

## 2. `E3.C6.3` repaired

> ### E3.C6.3 (repaired) — Delayed-revelation lemma
>
> Let the observation reveal a hidden parameter/disturbance at time `t_d`: before `t_d` the policy sees only the prior information, from `t_d` onward the full state. Write `Viab_full` for the full-information viability kernel and `Viab_del` for the delayed-observation kernel. Then:
>
> **(i) Inclusion.** `Viab_del ⊆ Viab_full` always, since the delayed policy class is a subclass.
>
> **(ii) Exact characterisation.** Define the **truncated kernel**
> ```
> T_del := { x₀ : ∃ a prior-admissible policy π with x(t) ∈ K on [0, t_d]
>                                     and x(t_d) ∈ Viab_full }.
> ```
> Then `Viab_del = T_del`. Consequently
> ```
> Viab_del = Viab_full    ⟺    Viab_full ⊆ T_del,
> ```
> i.e. **every full-viable state admits a prior-admissible policy that stays safe until `t_d` and remains full-viable there.**
>
> **(iii) Sufficient condition.** If `Viab_full` is **invariant under prior-admissible policies up to `t_d`** — for every `x₀ ∈ Viab_full` there is a prior-admissible policy keeping the trajectory inside `Viab_full` on `[0, t_d]` — then `Viab_del = Viab_full`.

*Proof.* (i) Immediate.

(ii) `⊇`: let `x₀ ∈ T_del` with witnessing policy `π₁`. At `t_d` the full state is revealed and `x(t_d) ∈ Viab_full`, so there is a full-information policy `π₂` keeping the trajectory in `K` thereafter. The concatenation uses only prior information on `[0,t_d)` and only revealed information after, so it is admissible for the delayed class; it keeps the trajectory in `K` throughout. Hence `x₀ ∈ Viab_del`.

`⊆`: let `x₀ ∈ Viab_del` with witnessing delayed policy `π`. Restrict `π` to `[0,t_d]`: it is prior-admissible and keeps the trajectory in `K`. Its continuation after `t_d` is a full-information policy keeping the trajectory in `K` from `x(t_d)`, so `x(t_d) ∈ Viab_full`. Hence `x₀ ∈ T_del`.

The equivalence `Viab_del = Viab_full ⟺ Viab_full ⊆ T_del` combines (i) and (ii).

(iii) Under the hypothesis, for each `x₀ ∈ Viab_full` the invariance policy stays inside `Viab_full ⊆ K` on `[0,t_d]` and lands in `Viab_full`, so `x₀ ∈ T_del`. Hence `Viab_full ⊆ T_del`, and (ii) gives equality. ∎

**What changed.** The vague "obstruction unreachable before `t_d`" is replaced by a condition on the existence of a *witnessing policy* — which is what the concatenation argument actually consumes. The (⟹) direction no longer needs an example: it is the `⊆` half of (ii), proved directly. `R02.Prop3` remains a legitimate **sharpness witness** — it exhibits a case where `Viab_full ⊄ T_del` and the inclusion is strict — and should be recorded as such rather than as the proof.

**Note on the record's hypothesis.** "No trajectory under *any* prior-admissible policy hits `X ∖ K`" is a universal quantifier over policies, which is much stronger than the existential quantifier (iii) needs, and it is also not obviously the right notion: it constrains *unsafe* policies, which are irrelevant to viability. The repaired (iii) quantifies existentially and targets `Viab_full` rather than `K`, which is what makes the concatenation work.

---

## 3. Verification

`reaudit/verify_e3cfb7_repair.py`, Part A — 12 assertions, exit 0. Finite model: states `{A, B, U}`, `K = {A, B}`, hidden mode `m ∈ {L, R}` revealed after one step, actions `{a, b}`.

| # | Claim | Result |
|---|---|---|
| A1 | `Viab_del ⊆ Viab_full` | ✓ in both cases |
| A2 | strict inclusion is possible: `Viab_full = {A,B}`, `Viab_del = {B}` | `A` full-viable, not delayed-viable |
| A3 | the truncated-kernel characterisation reproduces `Viab_del` exactly | both cases match |
| A4 | equality under prior-admissible invariance | both `{A, B}` |
| A5 | the (⟹) direction is the contrapositive of (ii), not an example | ✓ |

Case 1 is the hedging obstruction: `u = a` sends mode `R` to `U` and `u = b` sends mode `L` to `U`, so no mode-blind action is safe and `A ∉ Viab_del`, while a mode-aware policy saves both. Case 2 makes `u = a` safe for both modes, and equality is restored.

**Suggested register text** (proposal only — not applied):

> `E3.C6.3 | Delayed-revelation lemma | Viab_del ⊆ Viab_full always; Viab_del equals the truncated kernel T_del = {x₀ : some prior-admissible policy stays in K to t_d and lands in Viab_full}; inertness ⟺ Viab_full ⊆ T_del, and in particular holds if Viab_full is prior-admissible-invariant up to t_d | PROVEN (repaired) — the original's converse was supported by an example (R02.Prop3) rather than a proof, and its hypothesis was both stronger than needed and quantified over the wrong policies. See batch 4/E3_C63_REPAIRED.md`

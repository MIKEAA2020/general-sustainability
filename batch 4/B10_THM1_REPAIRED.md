# B10.Thm1 — Strategic-Implementation Docket: REPAIRED

> **ERRATUM (joint-assessment adjudication; see `batch 4/PROOF_ELEVATION.md` §I.3, Finding 10).** §1's claim "**Both leader objectives are usc** … Both therefore attain their maxima on compact `C`" and the repaired theorem (1)'s unconditional "**Both `V_pes` and `V_opt` are attained**" are **false in the pessimistic half** and are hereby struck. The pessimistic objective `ψ(c) = min_{π∈BR(c)} v_l(c,π)` is **lower** semicontinuous (min-attaining selections pass to the graph limit from below), attains its *minimum*, and its **maximum need not be attained**: attempt A1's witness (`batch 4/agent 1 attempt/CLASS_2_3_ELEVATIONS.md` §V — `v_f(c,a) = 0`, `v_f(c,b) = c−1`, `v_l(c,a) = c`, `v_l(c,b) = 0`; `BR(c) = {a}` for `c < 1`, `BR(1) = {a,b}`; `ψ(c) = c` for `c < 1`, `ψ(1) = 0`; `sup ψ = 1` not attained; verified numerically in `reaudit/verify_joint_disputes.py`) refutes it. This also corrects the audit's own Finding 10 parenthetical ("in fact continuous by Berge"). The corrected statement: optimistic existence unconditional; pessimistic existence **conditional** on `BR` lsc / single-valuedness / `v_l` constant on fibres; the displayed equation requires `π*` to attain the inner minimum. D1's coincidence characterisation, D2's closed-set analysis, and the reduction-license table of §3 stand as written. The consolidated statement is `batch 4/PROOF_ELEVATION.md` Finding 10.

**Target.** The `B10` section of `batch 2/04_open_problems/B_TIER_BRIDGES.md`, the manifest row `B10.Thm1` (line 99), and the status row in `OPEN_PROBLEMS_REGISTER.md` line 25.

**This file is a proposal. No repository file has been modified.**

**Disposition.** Both defects have a single root: the record does not distinguish the **optimistic** (existential) from the **robust** (universal) reading, and then claims properties that hold for one while stating the other. Separating them repairs everything without weakening anything:

| # | Defect | Repair |
|---|---|---|
| D1 | "the *optimistic* and *pessimistic* readings coincide under the closedness below" | false in general; exact characterisation given, plus sufficient conditions. The record's *displayed equation* is correct and is retained |
| D2 | "`{c : BR(c) ⊆ W-successors}` inherits closed graph by the same two-step limit argument as E2's Step 2" | false under Berge alone; but the **existential** form — which is what the record's own governance question asks — *is* closed with no extra hypothesis, and the universal form is closed under one named extra hypothesis |

**Verification.** `reaudit/verify_b10_repair.py`, 30 assertions, exit 0. Output: `reaudit/b10_output.txt`.

---

## 0. Setup

Leader command `c ∈ C` (compact metric), follower policy set `Π` (compact), follower payoff `v_f : C × Π → ℝ` continuous, leader payoff `v_l : C × Π → ℝ` continuous. Best response `BR(c) = argmax_{π ∈ Π} v_f(c, π)`, follower value `v̄_f(c) = max_π v_f(c, π)`.

Two leader values:

```
V_pes = max_{c ∈ C} min_{π ∈ BR(c)} v_l(c, π)        (pessimistic / robust)
V_opt = max_{c ∈ C} max_{π ∈ BR(c)} v_l(c, π)        (optimistic)
```

Always `V_pes ≤ V_opt`.

**Two safe-command sets**, for a closed set `Safe ⊆ Π` of viability-keeping follower policies:

```
E_Safe = { c : BR(c) ∩ Safe ≠ ∅ }     (existential — "some response is viable")
U_Safe = { c : BR(c) ⊆ Safe }         (universal  — "every response is viable")
```

---

## 1. D1 — the optimistic and pessimistic readings do **not** coincide

**What the record gets right.** `BR` has nonempty compact values and **closed graph**: for `π_n ∈ BR(c_n)` with `(c_n, π_n) → (c, π)`, continuity of `v_f` gives, for every `π' ∈ Π`,

```
v_f(c, π) = lim v_f(c_n, π_n) ≥ lim v_f(c_n, π') = v_f(c, π'),
```

so `π ∈ BR(c)`. (For finite `Π` this is immediate: the graph is the zero set of the continuous function `(c,π) ↦ v_f(c,π) − v̄_f(c)` on the compact `C × Π`; verified — off-graph points are separated by a positive gap.) Both leader objectives are **usc**: taking `π_n ∈ BR(c_n)` attaining the min (resp. max) and passing to a limit, closedness of the graph gives `π ∈ BR(c)` and hence `limsup m(c_n) ≤ m(c)`. Both therefore attain their maxima on compact `C`.

**The record's displayed equation is correct.** Choosing `c*` to maximise `m` and `π* ∈ BR(c*)` to *attain the inner minimum* gives `v_l(c*, π*) = V_pes` exactly. Nothing needs repairing there.

**What is false is the parenthetical.** "(the *optimistic* and *pessimistic* readings coincide under the closedness below)" — closedness of the graph does not imply `V_pes = V_opt`.

**Counterexample (minimal).** One command, `C = {c₀}`; `Π = {a, b}`; `v_f(c₀, a) = v_f(c₀, b) = 0`, so `BR(c₀) = {a, b}`; `v_l(c₀, a) = 0`, `v_l(c₀, b) = 1`. Then

```
V_pes = min(0, 1) = 0  <  1 = max(0, 1) = V_opt.
```

`BR` is constant, so its graph is trivially closed. Closedness is present and equality fails.

**Exact characterisation (verified on 200 random instances).**

> `V_pes = V_opt` **iff** `v_l(c*_opt, ·)` is constant on `BR(c*_opt)`, where `c*_opt` is any optimistic maximiser.

**Sufficient conditions worth declaring.** Equality holds if either

- **(S1)** `BR` is single-valued (the follower's best response is unique — e.g. `v_f(c, ·)` strictly concave on a convex `Π`); or
- **(S2)** the leader is indifferent among the follower's best responses at the optimum, i.e. `v_l(c*_opt, ·)` is constant on `BR(c*_opt)`.

Neither is implied by continuity and compactness. **(S1) is the hypothesis the record should have named.**

---

## 2. D2 — which safe-command set is closed

The record's `E2`-style "two-step limit argument" does not transfer, because `E2`'s Step 2 used **Hausdorff continuity** of the successor correspondence (both directions), whereas Berge supplies only **upper** semicontinuity. The two safe-command sets behave differently, and the difference is exactly the optimistic/robust distinction.

### 2.1 The universal form is **not** closed under Berge alone

**Characterisation.** `c ∈ U_F ⟺ v_f(c, π) < v̄_f(c)` for every `π ∉ F`. That is a **strict** inequality between continuous functions, so `U_F` is **open** — generally not closed.

**Counterexample (verified).** `C = [−1, 1]`, `Π = {a, b}`, `v_f(c, a) = 0`, `v_f(c, b) = −|c|`. Then `BR(c) = {a}` for `c ≠ 0` and `BR(0) = {a, b}`. With `F = {a}`:

```
U_F = { c : −|c| < 0 } = { c ≠ 0 },
```

which is open and **not closed** — `0` is a limit point that is missing. Verified on a 2001-point grid: the set contains 2000 of 2001 points, missing exactly `0`, with grid points `0.001, 0.002, 0.003, …` approaching it from inside the set.

`BR` here is usc with compact values (Berge) but **not lsc** at `0`: the open set `{b}` meets `BR(0)` but no `BR(c)` for `c ≠ 0`. That failure of lower semicontinuity is precisely what breaks closedness.

### 2.2 The existential form **is** closed under Berge alone

**Characterisation.** `c ∈ E_F ⟺ v_f(c, π) = v̄_f(c)` for some `π ∈ F`. That is an **equality** between continuous functions, so `E_F` is a level set, hence **closed**. No lower semicontinuity is needed.

Equivalently, in correspondence language: for usc `BR` with compact values, the upper inverse `{c : BR(c) ∩ F ≠ ∅}` of a closed set `F` is closed. This is the standard fact, and it is the one that actually applies.

**Verified.** For `F = {a}` the existential set is all of `C` (2001 of 2001 grid points); for `F = {b}` it is exactly `{0}` — both closed.

**This is the form the record's own question asks for.** The stated governance question is:

> "does the leader have a command after which **some** follower response keeps the system viable?"

That is `E_Safe ≠ ∅`, and it is available with no extra hypothesis. The record wrote `U_Safe` — the universal set — and then claimed a property it does not have.

### 2.3 The universal form **is** closed under one extra hypothesis

> **Proposition 2.1.** If `BR` is additionally **lower semicontinuous** (hence continuous, since Berge already gives usc), then `U_F` is closed for every closed `F`.

*Proof.* Let `c_n → c` with `BR(c_n) ⊆ F`, and take `x ∈ BR(c)`. By lower semicontinuity, every neighbourhood `V` of `x` meets `BR(c_n)` for all large `n`; since `BR(c_n) ⊆ F`, `V ∩ F ≠ ∅`. So `x ∈ cl(F) = F`. Hence `BR(c) ⊆ F`. ∎

**Verified.** For the continuous correspondence `BR(c) = [0, c]` on `[0,1]`, `U_{[0,h]} = [0, h]` is closed for `h = 0.25, 0.5, 0.75` — while the same construction with the usc-but-not-lsc `BR` of §2.1 fails.

---

## 3. `B10.Thm1` repaired

> ### B10.Thm1 (repaired) — Strategic implementation
>
> Under the setup of §0:
>
> **(1) Existence, both readings.** `BR` has nonempty compact values and closed graph. Both `V_pes` and `V_opt` are attained. Moreover there exist `c* ∈ C` and `π* ∈ BR(c*)` with
> ```
> v_l(c*, π*) = V_pes = max_c min_{π ∈ BR(c)} v_l(c, π),
> ```
> namely `c*` an optimiser of the pessimistic objective and `π*` a minimiser of `v_l(c*, ·)` over `BR(c*)`.
>
> **(2) The two readings.** `V_pes ≤ V_opt`, with equality **iff** `v_l(c*_opt, ·)` is constant on `BR(c*_opt)`. In particular equality holds under **(S1)** `BR` single-valued, or **(S2)** leader indifference at the optimum. Without (S1) or (S2) the gap `V_opt − V_pes > 0` is the **price of follower non-uniqueness**, and it is a genuine governance quantity, not an artefact.
>
> **(3) Reduction, optimistic form.** For closed `Safe ⊆ Π`, the set `E_Safe = {c : BR(c) ∩ Safe ≠ ∅}` is **closed**, under the standing hypotheses alone. Since `BR` has closed graph and nonempty compact values, Kuratowski–Ryll-Nardzewski (`E2.B2(a)`) yields a measurable selector `c ↦ π(c) ∈ BR(c)`; restricting to `E_Safe` gives a measurable viable-response selection.
>
> **(4) Reduction, robust form.** For closed `Safe`, the set `U_Safe = {c : BR(c) ⊆ Safe}` is **open** in general, and **closed** if `BR` is lower semicontinuous. It is `U_Safe`, not `E_Safe`, that licenses the all-branches theorems.

**Why (4) matters for the reduction licence.** The record claims "all non-strategic theorems (`R02.Thm1`, `B1`, `E2`) apply with `U := C` and `Succ := BR`-composed successors." But `R02.Thm1` is an **all-branches** theorem — it quantifies over every implementation branch, every deployment branch, every disturbance. Transferring it through `BR` therefore requires the **universal** safe-command set, i.e. part (4), i.e. **lower semicontinuity of `BR`**. That hypothesis is not implied by the record's assumptions and must be declared.

So the honest reduction licence splits:

| target theorem | quantifier | set needed | hypothesis needed |
|---|---|---|---|
| `E2.B2(a)` measurable selection | existential | `E_Safe` | Berge alone ✓ |
| `B1.Thm1` (repaired, two-depth) | existential in the follower, universal in the disturbance | `E_Safe` + the disturbance quantifier handled inside `Safe` | Berge alone ✓ |
| `R02.Thm1` closed-loop robust viability | **universal** over follower branches | `U_Safe` | **+ `BR` lower semicontinuous** |

**Suggested sufficient condition for (S1) and lsc together.** If `Π` is compact convex and `v_f(c, ·)` is strictly concave for each `c`, then `BR` is single-valued; a single-valued usc correspondence with compact values into a Hausdorff space is continuous, hence lsc. So **strict concavity of the follower's payoff in its own argument** delivers (S1), (S2) trivially, and the lsc hypothesis of (4) at once. That is the clean hypothesis to declare, and it is the standard one in the Stackelberg literature.

---

## 4. What is unchanged

- The existence half of the record is correct and is retained verbatim, including the displayed equation.
- `BR`'s closed graph and compact values are correct; the garbled fragment "(Berge's maximum theorem: the argmax correspondence is usc; with unique-valued... generally upper semicontinuous...)" should be cleaned up but states nothing false.
- The scope note is correct: game-dynamic refinements (subgame perfection, information asymmetry beyond the leader–follower order) remain outside and OPEN.

**Suggested register text** (proposal only — not applied):

> `B10.Thm1 | Stackelberg equilibrium and strategic reduction | Existence of both the pessimistic and optimistic values; `V_pes = V_opt` iff the leader is indifferent on `BR(c*_opt)` (in particular if `BR` is single-valued); the optimistic safe-command set is closed under Berge alone, the robust one requires `BR` lower semicontinuous | PROVEN (repaired) — the original claimed optimistic/pessimistic coincidence and closed-graph inheritance for the universal set; both are refuted by explicit counterexamples. See `batch 4/B10_THM1_REPAIRED.md`

---

## 5. Verification

`reaudit/verify_b10_repair.py` — 30 assertions, exit 0. Reads and writes no repository file.

| # | Claim | Result |
|---|---|---|
| N1 | `BR` matches the analytic description; closed graph via the level-set characterisation | off-graph gap `1.000000 > 0` |
| N2 | both leader objectives attain their maxima | `V_pes = 0.0`, `V_opt = 1.0` |
| N3 | the record's displayed equation holds with `π*` the pessimistic response | `v_l = 0.0 = V_pes` |
| N4 | `V_pes < V_opt` although the graph is closed; single-command counterexample | `0 < 1` |
| N5 | equality ⟺ `v_l(c*_opt,·)` constant on `BR(c*_opt)` | 200/200 random instances agree |
| N6 | `U_{ {a} } = {c ≠ 0}` — open, not closed; `BR` usc but not lsc at `0` | 2000 of 2001 grid points, missing exactly `0` |
| N7 | `E_{ {a} }` = all of `C`; `E_{ {b} } = {0}` — both closed (equality level sets) | 2001/2001 and `{0.0}` |
| N8 | with continuous `BR(c) = [0,c]`, `U_{[0,h]} = [0,h]` is closed | `h = 0.25, 0.5, 0.75` |
| N9 | KRN applies to `BR` itself; the reduction survives in the existential form | ✓ |

**Three errors in my own tests, all caught by the checks failing.**
1. My first `closed_graph` helper took the three *nearest* grid points and treated proximity as convergence, falsely reporting a violation.
2. I then switched to testing whether each fibre `{c : p ∈ BR(c)}` was closed *on the grid* — but a finite grid carries the discrete subspace topology, in which **every** subset is closed, so the test was vacuous. Replaced with the analytic level-set characterisation on a 2001-point grid, which is what actually distinguishes the two forms.
3. A leftover reference to a renamed variable (`ok` → `okg`) surfaced only at the last check.

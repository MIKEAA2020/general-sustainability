# Lean audit v7 — `thm:pomdp` (belief-state safety value)

**Target:** `general-sustainability` → `lean/`, against the latest edition
`paper2_obstruction_calculus_v55_Automatica_routes.tex` §10.
**Branch:** `lean-audit-v4` (additive; nothing on `main` disturbed).
**Toolchain:** `leanprover/lean4:v4.34.1` (pinned, as in v1–v6).
**Build:** `lake build` → rc = 0, 15 jobs, **zero warnings** from the new module.

This is item (1) of the work order — obstr's five theorems by fault-risk.
v6 triaged `thm:exit`, `thm:delayed` and `thm:static-complete` out of reach
(`OrdField` has no completeness/topology/measure, so those statements would
be **false** as interface-level claims, not merely unprovable) and delivered
`thm:lp-instant`. This v7 delivers the second feasible item, **`thm:pomdp`**.

---

## 1. What the paper actually claims

Verbatim from v55 §10. The preamble defines the value over **policies**:

> The *safety value* is the maximal survival probability
> $V_k(b) = \max_{\pi}\ \mathbb{P}_{\pi}(x_t \in \mathcal{V}\ \text{for } t = 0,\dots,k \mid b)$.

and then:

> **Theorem (belief-state safety value)** `thm:pomdp`. $V_0(b) = b(\mathcal{V})$
> (the horizon counts the current state), and for $k \ge 0$
> $$V_{k+1}(b) = \max_{a \in A}\ \sum_{y \in Y} \mathbb{P}(y \mid b, a)\ V_k(\tau(b,a,y)).$$
> The recursion is exact on every finite horizon; it is the Smallwood–Sondik
> belief-state value iteration specialized to the absorbing safety reward.

So the theorem has **two** parts, and they are not symmetric:

- **(a)** the *recursion identity* $V_{k+1} = \max_a \sum_y \ldots$;
- **(b)** the *content* — that this recursion computes $\max_\pi \mathbb{P}_\pi(\text{survive }k)$,
  i.e. Smallwood–Sondik, the thing actually being asserted.

## 2. What was formalized

New module **`lean/Formalizations/P1_BeliefSafety.lean`** (11,418 B),
namespace `Formalizations.POMDP`, 19 declarations (11 theorems, 2
structures, 6 definitions).

| Result | Statement | Status |
|---|---|---|
| `one_step_le_total` | $\sum_y \lVert m_{a,y}\rVert \le \lVert m\rVert$ for every $a$ | **proved** |
| `V_zero` | $V_0(m) = $ total safe mass (the paper's $b(\mathcal{V})$) | **proved** |
| `V_mono_succ` | $V_{k+1}(m) \le V_k(m)$ | **proved** |
| `V_nonneg` | $0 \le V_k(m)$ | **proved** |

Supporting machinery: `list_max_exists`, `lmax`/`lmax_isMax`/`le_lmax`/
`lmax_le`/`lmax_mono` (finite maxima, which `Prelude` carries only as
hypotheses), `lsum_map_zero`, `lsum_lsum_comm` (Fubini for finite sums),
`Mass`, `SafeMDP`, `obsMass`, `step`, `total`, `V`.

`V_mono_succ` is the fact the paper's own proof of `prop:chance` leans on —
quoted verbatim: *"Since $V_{k+1} \le V_k$ — more steps cannot raise the
survival probability."* That line was previously an appeal to intuition; it
is now a theorem.

## 3. Honest scope — three things NOT proved

### 3.1 The recursion is a *definition* here, so (a) carries no content

`V` is defined **by** the recursion. So `thm:pomdp` part (a) is true by
`rfl` in this module and proves nothing. This is worth saying plainly,
because it is exactly the audit failure mode this project exists to remove:
a statement that looks like a theorem but is a definitional restatement.

Part **(b)** — that the recursion equals $\max_\pi \mathbb{P}_\pi$ — is
where the real content lives, and it is **not** proved. Doing it requires
defining history-dependent policies, a policy-evaluated survival
probability, and an induction on the horizon with an interchange of `max`
and `sum`. That is a substantial next module, not a patch.

### 3.2 The normalization bridge

Bayes' rule divides by $\mathbb{P}(y \mid b,a)$, which is zero on impossible
observations. To avoid a case split at every step, the module works with
**unnormalized sub-probability masses** and the positive-homogeneous
recursion $V_{k+1}(m) = \max_a \sum_y V_k(m_{a,y})$,
$m_{a,y}(x') = \sum_x m(x)\,T(a,x,x')\,g(a,x,x',y)$.

This agrees with the paper's normalized recursion because
$\lVert m_{a,y}\rVert = \mathbb{P}(y \mid m,a)$, so
$V_k(m_{a,y}) = \mathbb{P}(y \mid m,a)\cdot V_k(\tau(m,a,y))$ — **but that
homogeneity lemma is not yet proved.** Exit is modelled by
$\sum_{x'} T(a,x,x') \le 1$, so the deficit $1 - \sum_{x'} T(a,x,x')$ is the
paper's one-step exit probability $p(x,a)$; the absorbing state $\bot$ is
untracked.

### 3.3 `prop:chance` is not yet derived

`prop:chance` needs $V_1(b) \le 1-\delta$ from
$\sum_x b(x)\,p(x,a) \ge \delta$. The machinery is now all present
(`one_step_le_total` plus a horizon-monotonicity lift
$V_n \le V_k$ for $k \le n$), but the one-step bound is currently proved
only as an inequality; deriving the quantitative $1-\delta$ form wants the
equality version of `one_step_le_total`. Left as the next batch rather than
bolted on half-done.

## 4. Axiom accounting

```
one_step_le_total  →  [propext, Quot.sound]
V_zero             →  [propext, Classical.choice]
V_nonneg           →  [propext, Classical.choice, Quot.sound]
V_mono_succ        →  [propext, Classical.choice, Quot.sound]
```

`one_step_le_total` — the substantive inequality — is **free of
`Classical.choice`**. Choice enters the rest only through `lmax`, which
selects a maximum of a finite list via `Classical.choose`; it is used to
*pick* a maximum, never to prove the inequality. `propext`/`Quot.sound` are
inherited from `Prelude`'s list reasoning. No `sorry`, no axioms beyond
these.

## 5. Reproducing this, incl. on `live.lean-lang.org`

The module imports **only `Formalizations.Prelude`** — no mathlib — so it
is self-contained and pastes straight into the web playground: paste
`Formalizations/Prelude.lean` followed by `Formalizations/P1_BeliefSafety.lean`
into one buffer and it will compile. Two caveats: (i) the playground runs a
recent Lean, not our pinned `v4.34.1`, so minor tactic/API drift is
possible; (ii) `Prelude` shadows `Nat` order lemmas — inside this layer,
qualify as `Nat.lt_of_lt_of_le` / `Nat.le_trans` whenever an `OrdField`
variable and a `Nat` index are both in scope, or resolution picks the
`OrdField` version and fails.

## 6. Verdict

`thm:pomdp` is **sound as stated**, with a real gap in exposition rather than
in mathematics: the theorem is presented as one claim but is two, and the
hard half (Smallwood–Sondik optimality, part (b)) is discharged in the paper
by a citation and the phrase "standard value iteration". The half that *is*
formalized — horizon monotonicity — is correct and is what the paper goes on
to use.

**Next batch, in order:** (a) the homogeneity bridge of §3.2; (b) the
equality form of `one_step_le_total` + horizon monotonicity → `prop:chance`;
(c) the max-over-policies definition that gives (a) of §3.1 real content.

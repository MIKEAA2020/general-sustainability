# Paper 1 Instantiation Report — The Typed False-Positive Theorem, Machine-Witnessed

**Companion files:** `research_program/paper1_typed_false_positive_theorem.md` (the theorems and proofs) · `typed_false_positive_instantiation.py` (the committed runner) · `typed_false_positive_instantiation.json` (the results artifact).

**Execution record:** run 2026-08-28, deterministic, exact integer arithmetic throughout (scale 40; no floats, no tolerances, no randomness, no outer tube approximation). Runtime ≈ 36 s; **25/25 machine checks pass**; exit 0. Grid: `[0,3]³` at step 0.1 in `(x, s_1, s_2)` = 29,791 states; the false-positive set occupies **1,900 grid states**.

## The witness datum in one paragraph

Two architectures (extraction `q=0` → regenerative `q=1`), one review interval, a physical reserve stock `x`, two typed floors — protected-group service `s_1` and remediation-liability coverage `s_2` — a two-point disturbance set (dip-depth scaling benign/adverse, worst-case dip 2), destination reset gains 1/4, rescue cost `c = 1`, and four meta-actions: `NO-SWITCH` (transit-safe, misses the destination), `FAST` (immediate switch: the `s_1`-floor dips mid-interval under the adverse disturbance), `SLOW` (phased switch: the `s_2`-floor dips), `STAGED` (the bridging plan: no typed dip, at physical cost `c` drawn from `x`). All trajectories piecewise linear on breakpoints `{0, ½, 1}` and monotone per piece, so every tube below is the **exact** visited set.

## The three assessment regions (Theorem B(1)–(3)), machine-confirmed

| assessment | admissible region (on initial states `x ≥ 0, s ≥ 0`) |
|---|---|
| noncompensatory typed | `{x ≥ 1} ∪ {s_1 ≥ 2} ∪ {s_2 ≥ 2}` |
| scalarized aggregate, every weight `w` in the closed nonnegative cone | `{x ≥ 1} ∪ {s_1 + s_2 ≥ 2}` |
| endpoint-only physical | all of `X_0` |

The machine layer confirms each identity on **every** grid state: the typed region by direct per-action tube checks; the aggregate region by per-weight action search over a dense critical weight set (`r = k/20`, `k = 0..40`, plus `r = ∞`, the exact boundary weights `ρ_1 = (2−s_1)/s_2`, `ρ_2 = s_1/(2−s_2)`, and the adversarial midpoint `(ρ_1+ρ_2)/2` — all exact integer pairs); the endpoint-only region trivially. The structural layer confirms the FAST/SLOW per-weight safety biconditionals (`FAST`-safe ⟺ `r ≥ ρ_1`; `SLOW`-safe ⟺ `r ≤ ρ_2`) on every grid state over the dense weight grid, including the `r = 0`/`r = ∞` edges.

## The false-positive set and its split (Theorem B(4)–(7))

```
FP = {x < 1, s_1 < 2, s_2 < 2, s_1 + s_2 ≥ 2}   — the triangle between the coordinate
     thresholds and the aggregate budget line; 1,900 grid states; interior points exist
R  = FP_0 ∩ {x ≥ 1}   — RESCUED: typed-transformable via STAGED (bridging at cost c = 1)
I  = FP_0 ∩ {x < 1}   — IMPOSSIBILITY: aggregate-feasible for every cone weight, yet no
                        typed-admissible action exists
```

Named witnesses, all machine-classified:

- **`(x, s_1, s_2) = (½, 6/5, 6/5)`** — interior false positive: aggregate-feasible for every critical weight, typed-infeasible, endpoint-feasible; all ±0.1 neighbours remain in FP (genuine interior). In the impossibility region (`x < 1`), its four-action rejection is the negative-certificate form — each action with its exhibited violated constraint: `FAST` → protected-service floor `s_1` dips to −0.8 under the adverse disturbance; `SLOW` → liability-coverage floor `s_2` dips to −0.8; `STAGED` → physical stock driven to −0.5; `NO-SWITCH` → destination architecture not reached.
- **`(½, 1/10, 1/10)`** — the endpoint-only blindness witness: endpoint-feasible while **no** action is aggregate-safe at `w = (1,1)` — the scalarized family already rejects it; endpoint-only accounting still accepts. This makes both hierarchy inclusions strict on one datum.
- **`(3/2, 6/5, 6/5)`** — the rescued witness: `STAGED` keeps both floors intact throughout and lands in `G` at physical cost `c = 1`.

**Per-weight plan disagreement (Theorem B(6))** at `(½, 6/5, 6/5)` (`ρ_1 = 2/3`, `ρ_2 = 3/2`): at `r = ½` only `SLOW` is aggregate-safe; at `r = 1` both; at `r = 2` only `FAST`. No action serves every critical weight — the machine verification of `E_typ = ⋂_w E_w = ∅`, i.e. the quantifier noncommutativity of Theorem A(ii) in its purest form: *every price vector has a plan, no plan serves every price vector.*

## Multi-stage propagation (Theorem C)

With two hold intervals prepended, each assessment's backward recursion (its own safe set per interval, `HOLD` the unique action) reproduces its one-interval region on every grid state; the hierarchy `typed ⊆ all-weights-aggregate ⊆ endpoint-only` holds at stage 0; and both strictness witnesses survive the holds. The separation is not an artifact of the one-interval framing.

## Development note (honest record)

Two defects were caught and fixed during the artifact's construction, both before any register entry was written: (i) the critical-weight builder initially added the `ρ_1` boundary weight even when `s_1 ≥ 2`, which places it **outside** the closed nonnegative cone (a negative weight) and produced 31 spurious region mismatches at the `s_1 = 3.0` grid edge — fixed by adding `ρ_1` only when `s_1 < 2` (there `FAST` is safe at every cone weight anyway); (ii) the structural-biconditional predictions initially special-cased the `r = 0` / `r = ∞` edges with the FAST/SLOW roles interchanged — fixed by using the unified inequalities (`b·s_1 + a·s_2 ≥ b·80` / `≥ a·80`), which are valid at both edges. After the fixes, 25/25.

## Status discipline

A machine pass here is a confirmation of the theorem file's closed-form proofs at the sampled/exact-integer level stated per check (dense weight grids plus the exact boundary and adversarial weights; full grid state coverage); the closed-form proofs themselves live in the theorem file. No theorem status outside this instantiation is changed by this artifact; the novelty positioning is the companion `research_program/paper1_full_text_novelty_pass.md`.

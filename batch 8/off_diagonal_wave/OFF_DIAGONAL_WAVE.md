# The Off-Diagonal Geometric Residual and the Full 2-D σ\*-Landscape — Research Wave Record

**Task 110 / batch 8 / paper 1 (*Ecological Indicators*).** This wave executes the σ-wave's recorded residual (SIGMA_SPECTRUM_WAVE.md §7.1, honest-limits item 1; QUEUE_REVERIFICATION_AND_PLAN.md Part E): *the off-diagonal geometric decisions are log-transcendental — `ln(s₁−1)·ln(s₂−1) ≤ ln(s₁+1)·ln(s₂+1)` — and if a future round wants the full 2-D σ\*-landscape map, that is its own exact wave (the −m rungs are already fully decidable off the diagonal; only the geometric member is not).* The owner directed this wave as **the third exact wave** (after the σ-wave, Task 105, and the middle-regime wave, Task 108).

**Audited state.** All manuscript facts are verified against the current version `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v54.tex` (the §4.5 datum, §6.3 fishery reading, §5.8 σ-subsection and §5.9 common-shock extension unchanged from v53 in everything this wave touches). Wave-1's verifier, ladder conventions, rung labels and 64-state grid are inherited verbatim and cross-checked against its committed run log (Part 0 of the machine log).

**Standing rules honored.** New files only (no existing file modified); no legitimate content removed or condensed; the manuscript v54 is untouched — this wave is research, not a manuscript edit; a future implementation round (owner-gated) will carry the results into a new version under the never-overwrite rule.

**Artifacts in this folder.**
- `off_diagonal_verify.py` — the fail-loud exact verifier (standard library only; `fractions.Fraction` exclusively; no floats, no tolerances, no randomness; deterministic; any failed gate exits nonzero).
- `off_diagonal_run_log.txt` — the committed run output: **50/50 checks pass** (`ALL CHECKS PASS`, exit 0), byte-reproducible (0.55 s).

---

## 1. The program being executed

Wave 1 left exactly one undecidable surface in the σ-spectrum program: off the diagonal, the geometric member's cover comparison is a product of two logarithms of rationals — log-transcendental, undecidable by finite rational arithmetic as such. Wave 1 squeezed it between a proven-sufficient rational condition (both cross-products `(s₁−1)(s₂+1) ≥ 1`, `(s₁+1)(s₂−1) ≥ 1` — equivalently, both plans serve the midpoint weight) and a proven-necessary one (`max(s₁,s₂) ≥ √2`), and reported ten honestly-undecided cells in the 64-state grid. The queue's framing of this wave: *the full 2-D σ\*-landscape map* — which additionally needs the θ = 1/2 and θ = 2/3 rungs decided off the diagonal (wave 1 had no general deciders for them either; its Part-4 nesting check ran on the rational rungs only).

This wave closes all three gaps with one method: **certified rational enclosures** — every transcendental or algebraic constant is bracketed between two rationals carrying a checkable certificate, and every cover decision becomes a certified comparison of a multilinear form over the enclosure box (a multilinear form attains its extrema on a box at the vertices). The log-transcendental is thereby not approximated — it is *decided*, with a finite rational proof attached to every verdict.

## 2. The exact off-diagonal cover criteria (the derivations)

Protocol 2 at rung θ, state (x, s₁, s₂), x < 1, both plans viable (FAST needs s₁ > 1, SLOW needs s₂ > 1; the collapse convention kills a plan whose tube touches λ ≤ 0). FAST's worst tube point is λ^F = (s₁−1, s₂+1), SLOW's the mirror. FAST's per-weight acceptance set is a downward interval [0, U], SLOW's an upward interval [L, 1] (wave-1 Lemma C); the cover is L ≤ U.

**The geometric member (θ = 0, σ = 1, the LPI functional structure).** FAST serves p iff `p·ln(s₁−1) + (1−p)·ln(s₂+1) ≥ 0`, so `U = B/(B−A)` with `A = ln(s₁−1)`, `B = ln(s₂+1)`; SLOW gives `L = −D/(C−D)` with `C = ln(s₁+1)`, `D = ln(s₂−1)`. Cross-multiplying (both denominators positive — `B−A > 0` because `s₁−1 < s₂+1` always on the datum, `C−D > 0` likewise):

**Cover ⟺ A·D ≤ B·C** — wave 1's log-transcendental comparison, now derived in full. Both sides are bilinear in the four certified ln-enclosures, so the vertex ranges decide: ACCEPT-certified iff max(A·D) < min(B·C), REJECT-certified iff min(A·D) > max(B·C).

**The θ ∈ (0,1) rungs (labels "1/2", "2/3").** With `A = (s₁−1)^θ`, `B = (s₂+1)^θ`, `C = (s₁+1)^θ`, `D = (s₂−1)^θ` (A < 1 < B, D < 1 < C on the core quadrant): `U = (B−1)/(B−A)`, `L = (1−D)/(C−D)`, and the same cross-multiplication gives

**Cover ⟺ F := C·(B−1) + A·(1−D) − (B−D) ≥ 0** — multilinear in (A, B, C, D), so the 16-vertex range over the enclosure box decides exactly. On the diagonal (A = D, B = C) this reduces to `(B−A)(A+B−2) ≥ 0`, i.e. the wave-1 master equation `A + B ≥ 2` — θ = 1/2: s ≥ 5/4; θ = 2/3: the cubic isolation. The machine checks this reduction at every diagonal state (checks 4.1–4.2).

**Lemma G0 (the boundary, elementary).** A coordinate `sᵢ ≥ 2` makes its own plan serve *every* weight: its tube's low λ is `sᵢ−1 ≥ 1`, so the aggregate at that coordinate is ≥ 1 at every p (for θ = 0 the log is ≥ 0; for θ ∈ (0,1) the power is ≥ 1). Hence cover follows from `max(s₁,s₂) ≥ 2`, and the residual decision problem lives on the open quadrant (1,2)², where additionally the sign structure `A, D < 0 < B, C` holds. (Machine: check 2.5 — at every grid cell with a coordinate ≥ 2 the raw log-comparison also certifies ACCEPT, A·D ≤ 0 there.)

## 3. The certificate machineries (and why every decision is a proof)

**ln-enclosures.** For rational q > 0, reduce exactly `q = 2^k·m` with m ∈ [1,2), and write `ln m = 2·artanh(y)` with `y = (m−1)/(m+1) ∈ [0, 1/3)`:
`ln m = 2·Σ_{j≥0} y^{2j+1}/(2j+1)` — an **all-positive-term** series, so the partial sum `2S_N` is a strict lower bound, and the tail is dominated geometrically: `Σ_{j≥N} y^{2j+1}/(2j+1) ≤ y^{2N+1}/((2N+1)(1−y²))`, a rational upper bound. ln 2 (y = 1/3) is certified once and combined with the sign of k. Certificate: the pair of rationals with the two inequalities re-derivable from the series. Fixed schedule N = 40 (width < 10⁻³⁰ at y ≤ 1/3). Self-consistency gates: scaling, reciprocity, addition, multiplicativity, monotonicity (checks 1.1–1.7).

**Radical brackets.** For `q^{1/k}`: `lo = r/10^W`, `hi = (r+1)/10^W` with `r = iroot(⌊q·10^{kW}⌋, k)` an integer k-th root (deterministic integer Newton, certificate `r^k ≤ n < (r+1)^k` checked); then `lo^k ≤ q < hi^k` is verified exactly. θ = 1/2 uses k = 2; θ = 2/3 uses `(s²)^{1/3}` (exact for s > 0). W = 36.

**The vertex principle.** A multilinear form (each variable to at most the first power) attains its extrema over a box at the vertices — elementary induction on the variables. Both comparison forms (A·D vs B·C; F over (A,B,C,D)) are multilinear, so their exact ranges over the enclosure boxes are finite rational computations. Every ACCEPT/REJECT below is therefore a finite rational proof; anything the schedule cannot decide fails loud (check 8.1 asserts zero such events).

**Independence.** The decisions are cross-validated against wave-1's *independent* per-weight algebra (`perp_plan`, the double-squaring and cube-isolation code paths): every REJECT carries an exhibited rational witness weight served by neither plan (derived from the certified threshold bounds `U ≤ u_max < l_min ≤ L`), and every ACCEPT serves every sampled weight (checks 2.6–2.7, 4.4). The geometric per-weight test itself is decided by the ln-enclosures (the p-combination of certified intervals).

## 4. The theorems

**Theorem G1 (the exact criterion and the boundary curve).** *On the viable quadrant with both coordinates in (1,2): the geometric member's cover holds iff `r(s₁)·r(s₂) ≤ 1`, where `r(s) = ln(1/(s−1))/ln(s+1)`. Equivalently the acceptance region is `{(s₁,s₂) : s₂ ≥ ρ(s₁)}` where `ρ = r⁻¹∘(1/r)` is a strictly decreasing **involution** (`ρ(ρ(s)) = s`, by the criterion's symmetry) with the unique fixed point `ρ(√2) = √2` (since `r(s) ≤ 1 ⟺ s² ≥ 2`, an exact rational equivalence) and limits `ρ(s) → 2⁻` as `s → 1⁺`, `ρ(s) → 1⁺` as `s → 2⁻` (r maps (1,2) onto (0,∞), strictly decreasing, with r(1⁺) = ∞, r(2⁻) = 0).* Consequences: the two wave-1 rational lemmas are the two sides of the pivot — `min(s) ≥ √2 ⟹ r(s₁)r(s₂) ≤ 1` (sufficient) and `r(s₁)r(s₂) ≤ 1 ⟹ max(s) ≥ √2` (necessary); the residual wedge `{min < √2 < max}` is split by the curve ρ, which is transcendental — the wave brackets it at rational columns (§5). Machine: checks 2.4 (symmetry), 2.9 (the fixed point), 3.2 (the pivot brackets), 3.3 (involution reciprocity: for a column bracket (rej, acc], the cells (rej, s₁) reject and (acc, s₁) accept), 3.5 (the near-1 limit evidence).

**Lemma G2 (r strictly decreasing).** `r(s) = ln(1/(s−1))/ln(s+1)`: the numerator is strictly decreasing and positive, the denominator strictly increasing and positive, on (1,2). Machine: check 2.8 — adjacent 1/20-grid enclosures strictly ordered.

**Theorem G3 (up-closure; the monotone landscape).** *For every rung θ, the acceptance region is up-closed in each coordinate: increasing s₁ helps both plans' worst tubes (λ₁^F = s₁−1 and λ₁^S = s₁+1 both increase), so per-weight acceptance grows, so the cover grows. Consequently σ\*(z) is nonincreasing in each coordinate on the gap region.* Machine: check 5.2 — every comparable grid pair, all 13 rungs.

**The wedge witnesses (the residual is genuine).** The two wedge cells (5/4, 3/2) and (3/2, 5/4) **REJECT** (certified margins ≈ 0.218; witness weights ≈ 0.398/0.461 apart, both plans failing), while (5/4, 7/4) and (7/4, 5/4) **ACCEPT** (margins ≈ 0.422): no purely per-coordinate rational condition separates them — the curve ρ does. Together with G0's six (5/4, ≥2)-family ACCEPT cells, all ten wave-1 residual cells are decided (check 2.3).

**The four-regime fixed-sum structure (machine-certified).** Slice the gap quadrant by total margin `s₁+s₂ = 2s̄` (the anti-diagonals). Elementary anchors: the balanced point (s̄, s̄) accepts iff `s̄² ≥ 2` (the diagonal closed form); the `sᵢ = 2` edge accepts (G0); for s̄ < 3/2 the near-`s = 1` edge rejects (r(s₂-edge) fixed positive while r(s₁) → ∞). The machine then maps the scanned slices into four regimes (checks 6.2–6.7):

| regime | totals (scanned evidence) | slice behaviour at the geometric member |
|---|---|---|
| **R1** | 2s̄ ≤ 141/50 = 2.82 (incl. the canonical 12/5) | every scanned point rejects — no asymmetry saves the total |
| **R2** | 141/50 < 2s̄ < 2√2 (exemplar 707/250 = 2.828) | **interior window**: the balanced point rejects, moderate asymmetry accepts, edges reject |
| **R3** | 2√2 ≤ 2s̄ < 3 (exemplar 71/25 = 2.84) | **anchored window**: the balanced point accepts, strong asymmetry rejects |
| **R4** | 2s̄ ≥ 3 | the whole scanned slice accepts |

The regime boundaries at `2√2` (the balanced-point flip) and `3` (the edge flip) are elementary; the **slice-flip total** `2s̊\*` — where the first accepting point appears — is transcendental and machine-bracketed: at 141/50 all 40 scanned points reject, at 353/125 = 2.824 there are already 11 acceptors, so `2s̊\* ∈ (141/50, 353/125]` on the scanned 1/50 grids — strictly below 2√2 = 2.8284… (certified by the 707/250 acceptor). The striking content of R2: **moderate concentration of the deficit is *more* certifiable than balance** — the balanced point is not the slice's best point below 2√2.

## 5. The map (the new exact witness data)

**The ten decided cells** (wave-1's residual, all certified strict): (5/4, 3/2), (3/2, 5/4) REJECT; (5/4, 7/4), (7/4, 5/4) ACCEPT; the six (5/4, 2), (2, 5/4), (5/4, 9/4), (9/4, 5/4), (5/4, 5/2), (5/2, 5/4) ACCEPT by G0.

**The ρ-curve brackets** (1/20 columns, single-flip monotone scans, up-closure-guaranteed):

| column s₁ | ρ(s₁) ∈ | | column s₁ | ρ(s₁) ∈ |
|---|---|---|---|---|
| 101/100 | (37/20, 19/10] | | 29/20 | (27/20, 7/5] |
| 11/10 | (17/10, 7/4] | | 3/2 | (13/10, 27/20] |
| 6/5 | (8/5, 33/20] | | 31/20 | (5/4, 13/10] |
| 5/4 | (31/20, 8/5] | | 8/5 | (6/5, 5/4] |
| 13/10 | (3/2, 31/20] | | 17/10 | (11/10, 23/20] |
| 27/20 | (29/20, 3/2] | | 7/4 | (21/20, 11/10] |
| 7/5 | (7/5, 29/20] | | 9/5, 39/20 | (1, 21/20] |

The involution is visible in the data (ρ(7/5) ∈ (7/5, 29/20] against ρ(29/20) ∈ (27/20, 7/5]; ρ(5/4) ∈ (31/20, 8/5] against ρ(8/5) ∈ (6/5, 5/4]).

**The complete 2-D σ\*-landscape** (all 13 rungs decided at all 64 grid states, zero undecided; prefix nesting at every state; up-closure over all comparable pairs — checks 5.1–5.2). The 22 gap states: 13 only-linear (σ\* = ∞ — the min ≤ 1 boundary states and (1,1)); 9 finite, forming clean off-diagonal bands:

| state | σ\* | | state | σ\* |
|---|---|---|---|---|
| (5/4, 5/4) | **= 2 exactly** (rung equality) | | (3/2, 3/2) | ∈ (1/2, 1) |
| (5/4, 3/2), (3/2, 5/4) | ∈ (1, 2) | | (3/2, 7/4), (7/4, 3/2) | ∈ (1/3, 1/2) |
| (5/4, 7/4), (7/4, 5/4) | ∈ (1/2, 1) | | (7/4, 7/4) | ∈ (1/4, 1/3) |

Off-grid specials: (6/5, 7/5) ∈ (1,2); (13/10, 3/2) ∈ (1,2); the relevance pair below. The landscape is consistent with the diagonal ladder at every comparable state (the diagonal brackets of wave 1 sit inside the off-diagonal bands' monotonicity).

**The θ = 1/2, 2/3 off-diagonal data.** Both rungs now decided at all 64 states (check 4.3: acceptance at 1/2 implies acceptance at 2/3 everywhere — the nesting, previously unverifiable off the diagonal, now machine-complete); diagonal agreement with the closed forms including the (5/4,5/4) θ = 1/2 equality state (checks 4.1–4.2); per-weight cross-validation both directions (4.4).

## 6. The relevance test — all four components, machine-anchored (Part 7)

**(1) Named ecological decision.** The §6.3 benchmark's **asymmetric-allocation licensing decision**: a two-stock transition at total margin `s₁+s₂ = 707/250` (total biomass `1707/250` kt = 6.828 kt at B_lim = 2 kt per stock) — does the composite certification under the LPI-structured (geometric) form license the plan without triggering the mandatory below-LRP response, and how does the answer depend on the **allocation of the deficit across the stocks**? Both allocations are gap states (typed-reject, linear-accept). The balanced allocation (707/500, 707/500): **REJECT** — the diagonal closed form, `(707/500)² = 499849/250000 < 2` exactly (excess 151/250000). The concentrated allocation (607/500, 807/500): **ACCEPT** — the certified log-comparison, margin ≈ 1.17×10⁻² (r-product ≈ 0.9847). *The same total margin, opposite verdicts* (check 7.1).

**(2) Changes what an actual indicator reports.** The equal-weight report table at the same total: the balanced FAST-trough λ = (207/500, 1207/500) — geometric √(249849/250000) < 1, a decline signal; the concentrated FAST-trough λ = (107/500, 1307/500) — √(139849/250000) < 1, also decline; **but** the concentrated state's SLOW-trough λ = (1107/500, 307/500) — √(339849/250000) > 1, certified. *Which stock bears the pulse flips the equal-weight LPI report at the same state*; the linear dashboard reports **literally the same number** (707/500 ≥ 1) at both troughs — sum-blind (check 7.2).

**(3) New exact witness datum.** The ten decided cells with certificates; the fifteen ρ-brackets; the completed 13-rung landscape with the nine-band σ\* table; the four-regime slice structure with the slice-flip bracket `2s̊\* ∈ (141/50, 353/125]`; the per-rung witness weights — every number an exact rational, every decision a certified comparison (check 7.3).

**(4) Alters at least one management action.** At total margin 707/250 the allocation choice flips the mandatory below-LRP response under the LPI-structured composite: balanced → REJECT → the closure/rebuilding response triggers (the reserve top-up κ\* = 1 − x = 1/2 financing STAGED, the wave-1 chain); concentrated → ACCEPT → the transition is licensed with no mid-transition response. The linear dashboard licenses **both** allocations — the false certification is now visibly two-dimensional: it is blind to the *distribution*, not only to the total. And at the concentrated state the pulse-allocation choice (FAST on the low stock versus SLOW on the high stock) flips the equal-weight report (7.2) — a plan-design decision with certification content (check 7.4).

## 7. Honest limits and scope

1. **The boundary curve ρ is transcendental.** No closed form is claimed; the map gives rational brackets at rational columns (1/20 resolution) with certified endpoints. The same holds for the slice-flip total `2s̊\*` and for every interior σ\* value (brackets between adjacent rungs only, as in wave 1).
2. **Slice scans certify scanned points.** The R1/R2 bracket and the slice-flip bracket are statements about the scanned 1/50 grids; the continuum slice minimum (a transcendental inequality in general) is an honest open residual. The interval-ness of the accepting windows on a slice is machine-evidenced, not proved. The R3/R4 boundary at total 3 is elementary at the edges; its interior is scan-certified.
3. **The certificates' scope.** Every decision is a finite rational proof *relative to* the enclosure lemmas (§3) and the vertex principle — both proved here — and the fail-loud discipline (check 8.1: zero undecided events; 8.2: determinism).
4. **The datum only.** The §4.5 menu, disturbance convention and horizon; the LPI-identification caveats of wave 1 (functional form under Protocol 2's adversarial cone; ratio-scale inputs; published weighting as one cone point) carry over verbatim; no transfer to the coupled-shock or infinite-horizon regimes (§5.5 delimitations); nothing here is an empirical claim.
5. **The display-ghost caution.** Wave 1's log carried two display-layer ghost labels; this wave's log was checked at the byte level (the one suspicious-looking check name in the rendered log, `7.4 [management action]`, is correct in the committed bytes — a rendering artifact eats the two characters `[m` in some terminal displays).

## 8. What a future manuscript round can transcribe (owner-gated; additive only)

Under the never-overwrite rule this is a sketch for an additive extension of §5.8 (or a new labelled paragraph beside it), not an edit made now: (i) the exact off-diagonal criterion (A·D ≤ B·C with the derivation) and the r-function/ρ-curve with its properties (involution, the (√2,√2) pivot, the limits) — one display plus two sentences; (ii) the residual wedge witnesses ((5/4,3/2) rejects, (5/4,7/4) accepts — the two rational tests' gap is genuine) and the ten-cell completion; (iii) the completed 2-D σ\*-landscape sentence (the off-diagonal bands (1,2)/(1/2,1)/(1/3,1/2)/(1/4,1/3) mirroring the diagonal ladder); (iv) the four-regime fixed-sum tolerance structure as a labelled remark — the distribution-vs-total finding, with the 707/250 report/action pair as the anchor and the plan-design (FAST/SLOW trough-report) flip; (v) a pointer to this folder's verifier as the datum's companion extension (a fifth check list under the family's non-pooling policy — the numbering to be settled by that round). All additive; every existing sentence of v54 stays.

## 9. Reproduction

```
python3 "batch 8/off_diagonal_wave/off_diagonal_verify.py"   # exit 0
```
Standard library only; deterministic; `off_diagonal_run_log.txt` is the committed output of exactly this invocation (50/50 checks, `ALL CHECKS PASS`). Re-running reproduces it byte-identically (no timestamps, no randomness, no floats; runtime ≈ 0.55 s).

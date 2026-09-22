# The Continuum Slice-Minimum — Research Wave Record

**Task 114 (re-executed as Task 115) / batch 8 / paper 1 (*Ecological Indicators*).** This wave closes the off-diagonal wave's recorded honest residual (OFF_DIAGONAL_WAVE.md §7 item 2; the v58 Limitations registry's item (xiii)): *the slice scans certify the scanned 1/50-grid points only — the continuum slice-minimum (where a slice's first accepting point lies, whether the accepting windows are intervals, where the total-3 regime boundary sits in the interior) is an honest open residual.* The owner directed its closure ("close the continuum slice-minimum") as **the fourth exact wave** (after the σ-wave, Task 105; the middle-regime wave, Task 108; the off-diagonal wave, Task 110).

**Provenance (recorded plainly).** The original Task-114 execution of this wave was committed locally but never pushed (the round's PAT was not re-supplied) and was lost with its sandbox in a recycle. This folder is a fresh re-execution to the same standard; its headline brackets reproduce the original round's recorded numbers (t\* inside (2.8225697640, 2.8225697655); the tangent pair matching 1.14796785…/1.67460191…; the circle identity; the sandwich; σ_min(707/250) in [12/13, 1]; the m-side flip total exactly 3).

**Standing rules honored.** New files only (no existing file modified); no legitimate content removed or condensed; the manuscript v58 untouched by the research wave — the transcription into **v59** was a separate implementation round (batch 8/v59_implementation_wave/, also in this commit) under the never-overwrite rule.

**Artifacts in this folder.**
- `slice_minimum_verify.py` — the fail-loud exact verifier (standard library only; `fractions.Fraction` exclusively; no floats in decisions, no tolerances, no randomness; deterministic; any failed gate exits nonzero).
- `slice_minimum_run_log.txt` — the committed run output: **44/44 checks pass** (`ALL CHECKS PASS`, exit 0), byte-reproducible (runtime ≈ 9 min; the deep critical-adjacent chases dominate — see the device notes below).

---

## 1. The program being executed

The off-diagonal wave left the fixed-sum (anti-diagonal) tolerance structure certified at scanned points only: the four regimes R1–R4, the slice-flip bracket `2s̊* ∈ (141/50, 353/125]`, and the interval-ness of the accepting windows were scan evidence. The queue's framing of this wave: decide the **continuum** — where the flip lies, what shape the windows have, where the total-3 boundary runs — by certified rational proof, no closed form expected or claimed.

## 2. The mathematics (the derivations)

Throughout, `r(s) = ln(1/(s-1))/ln(s+1)`, `ρ = r⁻¹∘(1/r)` the geometric member's boundary involution (Theorem G1 of the off-diagonal wave), and `M_θ` the CES family on floor-referenced indices. **The φ-reduction:** a point `(s, t-s)` of the total-`t` slice accepts at the geometric member iff `r(s)·r(t-s) ≤ 1` iff `φ(s) := s + ρ(s) ≤ t`. So the whole slice program — windows, flips, regime boundaries — is the sublevel-set program of ONE explicit scalar function φ on (1,2), with `φ(1⁺) = φ(2⁻) = 3` and `φ(√2) = 2√2` (the fixed point).

**The tangency identity.** From `ρ = r⁻¹∘(1/r)`: `ρ'(s) = −h(s)/h(ρ(s))` with `h := r'/r` (differentiate `r(ρ(s))·r(s) = 1` and use `r(ρ(s)) = 1/r(s)`). Hence `φ'(s) = 1 + ρ'(s)` has exactly the sign of `D(s) := h(s) − h(ρ(s))`: the stationary points of φ are the zeros of D. Three zeros exist: the fixed point `√2` (elementary — `r(√2) = 1` exactly, and D vanishes identically at any fixed point), and the **tangent pair** `a* < √2 < b*` with `ρ(a*) = b*`, `ρ(b*) = a*`, `ρ'(a*) = ρ'(b*) = −1` (the involution forces slope ±1 at the fixed point of the reflection; the pair structure gives `D(a*) = D(b*) = 0` via `h(a*) = h(b*)`).

**The four-phase shape.** `D < 0` on (1, a\*), `D > 0` on (a\*, √2), `D < 0` on (√2, b\*), `D > 0` on (b\*, 2): φ descends from its limit 3 to the minimum at a\*, rises through the local maximum 2√2 at the fixed point, descends to the equal minimum at b\*, climbs back to 3. Consequences: the sublevel set `{φ ≤ t}` is, per monotone phase, a single interval — **every accepting window is an interval** (no internal holes); two windows on R2 slices (one per tangent branch), one on R3 (merged at the balanced point), and `t* := min φ = a* + b*` is the **slice-flip total** — attained at the tangent pair, where the ρ-curve touches the anti-diagonal.

**The near-1 lemma (PROVED).** For `ε ∈ (0, eps]` (eps ≤ 1/2): `h(1+ε) ≤ −1/(16·eps·ln(1/eps)_hi)`. Chain: `N' = −1/ε ≤ −1/eps`, `D ≥ ln2 ≥ 1/2`, `−N·D' ≤ 0`, `D² ≤ (ln3)² ≤ 4` give `r' ≤ −1/(8 eps)`; `r = N/D ≤ 2 ln(1/ε)` (N ≤ ln(1/eps), D ≥ 1/2); the negative-by-positive quotient is maximized at max-numerator/max-denominator; `x ln(1/x)` increasing on (0, 1/e] orders the eps-dependence. This bounds the h-image of ρ-cells whose lower end approaches 1 (where h diverges and no finite box exists) — the phase-4 certification near s = 2 runs through it.

**The ln ≤ x−1 lemma (PROVED).** `ln x ≤ x−1` for rational `x ≥ 1`: `ln x = 2 artanh(y)`, `y = (x−1)/(x+1)`, and `artanh(y) = Σ y^{2j+1}/(2j+1) ≤ Σ y^{2j+1} = y/(1−y)` (term-by-term, all terms nonnegative), so `ln x ≤ 2y/(1−y) = x−1` exactly (the certificate is the rational identity; the domination is the enclosure lemma's own). This powers the semi-bounded end chains: on `(1, 1+δ]` of the total-3 slice, `r(s)r(3−s) = N₁N₂/(D₁D₂)` with `N₁ = ln(1/ε) = 2 ln(1/√ε) ≤ 2(√(1/ε)−1)`, `N₂ = −ln(1−ε) ≤ ε/(1−ε)`, `D₁D₂ ≥ ln2·ln3`, giving the product `≤ 2√δ/((1−δ) ln2 ln3) < 1` at δ = 10⁻⁴ — the ends accept robustly.

**The circle theorem (m = 1).** Clearing the four positive linear denominators of the harmonic criterion `(1−D)(B−A) ≤ (B−1)(C−D)` at θ = −1 leaves `Q(u,v) := (v−2)(u−v−2)(u+1) + v(v−u−2)(u−1) = −2(u²+v²−u−v−2)` — an exact polynomial identity, machine-verified symbolically and on grids. So the harmonic member's off-diagonal acceptance region is exactly the **exterior of (2s₁−1)² + (2s₂−1)² = 10**: a circle through (1,2), (√2,√2) [the golden-ratio diagonal floor 2s̄ = 1+√5], and (2,1).

**The convexity lemma.** Along an anti-diagonal of total t, `f(u) = (2u−1)² + (2(t−u)−1)²` satisfies `f(u) − f(1) = 8(u−1)(u−(t−1))` exactly; on the segment u ∈ [1, t−1] both factors have constant sign, so f is maximized at the segment endpoints: any total-t ≤ 3 sub-segment's circle value is at most `1 + (2t−3)² < 10` for t < 3, equality only at the t = 3 corners. Hence **every gap point with total < 3 lies strictly inside the circle** — the harmonic member strictly rejects it, and (the ladder nesting) so does every θ = −m and the Leontief member.

**The corner-cusp asymptotics.** Near (2, 1+ε), the θ = −m criterion reduces (in the ε → 0, δ → 0 regime) to `m·δ·ε^m ≲ (1−3^{−m})(1−2^{−m})·ε^m`, i.e. the acceptance wedge is a cusp of width `δ ~ ε^m/m` — sub-geometric in m via the 1/m prefactor. Certified witnesses: `(2 − δ_m, 6/5 + δ_m)` on the total-16/5 slice accepted by rung −m for every tested m, with δ_m = 10⁻² … 10⁻¹⁴.

**The up-closure domination (triangles → slices).** For `T₀ < 3`, every point (a, b) of the sub-triangle `{s₁+s₂ ≤ T₀} ∩ [1,2]²` is dominated by the slice point `(T₀−b, b)` (which lies in `[1,2]²` whenever `a+b ≤ T₀` and `b ∈ [1,2]`) — so a whole-slice rejection at T₀ plus up-closure (Theorem G3) rejects the entire sub-triangle. The flip-total ladder's shallow rungs are certified by 1-D slice tests, not 2-D scans.

## 3. The certified devices

- **Subdivision exhaustion with derivative monotonicity** (the whole-slice rejections near the minimum): per cell, a 16-vertex box of `g'(s) = r'(s)r(t−s) − r(s)r'(t−s)` (each factor endpoint-boxed; multilinear → vertices); `g' > 0` certifies the min at the low endpoint (a tight point-enclosure product), `g' < 0` at the high endpoint; a straddling cell uses the midpoint value minus a Lipschitz correction `max|g'|·(cell/2)` — at the parabolic minimum the correction is quadratic in the cell width, so the chase converges where naive product boxes (virtual-corner slack, linear in the width) cannot.
- **The crossing-chase ledger**: every subdivision event is ledgered (2,103 in the committed run); every chase either resolved by a certified box or a Lipschitz-corrected midpoint, with the ρ-bracket width adapting to the cell (the h-image slack must shrink with the cell near the critical points). Sign stalls inside certified critical brackets are the only terminations.
- **Semi-bounded end chains** (the ln ≤ x−1 lemma) for the geometric ends, and **one-sided monotone boxes** for the rung criteria's unbounded powers (`∂G/∂A = −(1−D) > 0`, `∂G/∂D = A−1 > 0` on the quadrant — exact).
- **Two independent code paths** for t\*: the tangency bisection on D, and the direct slice bisection (whole-slice certified rejection below, exhibited strict acceptor above) — the brackets overlap.

## 4. The theorems (machine-certified)

**Theorem T1 (the φ-minimum).** *`t* = min φ = a* + b*` with the tangent pair certified: `a* ∈ (1.147967853904, 1.147967853977]`, `b* = ρ(a*) ∈ (1.674601910855, 1.674601910929]`, `t* ∈ (2.822569764760, 2.822569764906]` — inside the original round's recorded bracket (2.8225697640, 2.8225697655), five orders inside the scan bracket (141/50, 353/125], strictly below 2√2 (certified straddle), cross-validated by the independent slice bisection.*

**Theorem T2 (the four-phase shape and the interval character).** *D's sign pattern as above; consequently every accepting window on every slice is a sublevel interval of one monotone phase of φ — the off-diagonal wave's scan-evidenced interval-ness is proved. (Anchored: the 707/250 slice carries exactly two windows, the 71/25 slice exactly one.)*

**Theorem T3 (the total-3 boundary, interior).** *`φ < 3` on (1,2): every interior point of every total-3 slice accepts at the geometric member (middle by 200 product cells, ends by the semi-bounded chains), and with it the whole R4 regime — for every t ≥ 3 the entire slice accepts, since `φ(s) < 3 ≤ t`.*

**Theorem T4 (the circle; the m-side flip).** *The harmonic region is exactly the circle exterior (the polynomial identity); nothing at or below θ = −1 covers anything below total 3 (the convexity lemma + nesting); the m-side flip total is exactly 3, attained at the corners (1,2)/(2,1), which every rung accepts.*

**Theorem T5 (the sandwich).** *`σ_min(t) ∈ (1/2, 1]` for every `t ∈ (t*, 3)`: the lower end the circle's strict interior (every gap point below total 3 is strictly inside), the upper end the φ-minimum (every slice above t\* contains a strict geometric acceptor near the tangent branch). Column anchors: `σ_min(707/250) ∈ [12/13, 1]` (the θ = −1/12 rung rejects the whole anchor slice; the concentrated allocation is a committed strict acceptor); `σ_min(71/25) ∈ [12/13, 1]`; `σ_min(299/100) ∈ (1/2, 2/3]`. The best point slides from the tangent branch (near a\*) toward the corners as t climbs to 3 — the tangency sweep.*

**Theorem T6 (the corner cusps).** *For every tested m, explicit rational states of a total-16/5 slice are accepted by rung −m with δ_m down to 10⁻¹⁴ — the wedges are corner cusps of width ~ε^m/m, so `inf σ* = 0` on every total-t > 3 slice.*

**Theorem T7 (the flip-total ladder).** *Assembled, all certified: the linear member exactly **2** (the dashboard identity `cover ⟺ s₁+s₂ ≥ 2`, a polynomial identity); θ = 2/3 exactly **2 × (the cubic master root)** (master root in (1.179959679543, 1.179959679618]; slice + domination + the diagonal equality); θ = 1/2 exactly **5/2** (the rung's own equality state (5/4, 5/4) — rational); θ = 0 the transcendental **t\*** (the tangent pair — moderate concentration beats balance from the geometric member down); every θ = −m and the Leontief member exactly **3** (the circle; the corners). Strictly increasing in depth, nesting-consistent.*

## 5. The relevance chain (Part 7 of the run)

**(1) Named decision.** The asymmetric-allocation licensing decision at total margin 707/250 now carries a continuum certificate: the interior window is an interval, its existence at every total in (t\*, 2√2) is the φ-minimum theorem, and it dies at t\* (the tangent pair). **(2) Indicator report.** Unchanged and inherited (the SLOW/FAST trough-report flip; the sum-blind dashboard). **(3) New exact datum.** The tangent pair and t\* to ten-eleven places (two code paths); the circle identity; the four-phase shape; the sandwich and column brackets; the corner witnesses; the flip-total ladder. **(4) Management action.** The interior window's ecological content — *moderate concentration of a deficit is more certifiable than balance* — now holds on the continuum: below 2√2 the balanced point is not the slice's best point; at 707/250 the balanced allocation triggers the mandatory response while the concentrated one is licensed.

## 6. Honest limits and scope

1. **The tangent quantities are transcendental.** a\*, b\*, t\*, ρ, and every interior σ\* carry certified rational brackets only — no closed form is claimed (the brackets are the data; t\* to ~10⁻¹⁰ here).
2. **The end segments (1, 1+1/100] and [2−1/100, 2) of the four-phase claim** are certified by value anchors plus the record's elementary asymptotics (D < 0 near 1 by the chain comparison `1/(ε ln(1/ε)) > ln(1/ε)/(ln2 ln3)`), not by derivative boxes (h diverges at both ends); the machine certificate covers the working interval [1+1/100, 2−1/100], and the zeros' brackets pin the criticals. No window of any tested column reaches the end segments (value anchors).
3. **The certificates' scope.** Every decision is a finite rational proof relative to the enclosure lemmas (the atanh series, integer roots, the two PROVED lemmas) and the vertex principle — all proved or inherited — and the fail-loud discipline (zero undecided events in the committed run; determinism re-verified).
4. **The datum only.** The §4.5 menu, disturbance convention and horizon; the LPI-identification caveats of the earlier waves carry over verbatim; no transfer to coupled-shock or infinite-horizon regimes; nothing here is an empirical claim.
5. **Display-layer note.** The rendered log's check `7.4 [management action]` may display as `7.4 anagement action]` in some terminals — the same `[m`-eating display artifact the off-diagonal wave recorded; the committed bytes are correct.
6. **Runtime.** The committed run takes ≈ 9 minutes (the original lost round reported ≈ 17 s; the difference is engineering, not mathematics — the deep critical-adjacent chases at the 10⁻¹⁰–10⁻¹² scales dominate). Deterministic and byte-reproducible.

## 7. What the manuscript round transcribed (owner-gated; additive only)

Executed in the same commit as this wave, under the never-overwrite rule, as **PAPER 1 v59** (batch 8/v59_implementation_wave/): (i) the continuum-slice closure addendum at the end of §5.8's off-diagonal closure block — the φ-reduction, the tangency identity and the four-phase shape, t\* with the tangent pair (two code paths), the circle theorem, the m-side flip total exactly 3, the total-3 interior proof, the interval character, the sandwich with the column brackets, the corner cusps (inf σ\* = 0 beyond 3), the flip-total ladder, and the sixth check list under the family's non-pooling policy; (ii) the Limitations registry item (xiv) recording the closure of item (xiii)'s residual. All additive; every existing sentence of v58 stays.

## 8. Reproduction

```
python3 "batch 8/slice_minimum_wave/slice_minimum_verify.py"   # exit 0
```
Standard library only; deterministic; `slice_minimum_run_log.txt` is the committed output of exactly this invocation (44/44 checks, `ALL CHECKS PASS`). Re-running reproduces it byte-identically (no timestamps, no randomness, no floats in decisions; runtime ≈ 9 min).

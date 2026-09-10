# Generalization Protocol for E3 and E4 — Claim Schemas, Scope Conditions, and a Verified Margin Lemma

**Date:** 10 Sep 2026
**Status:** exploratory framework, **machine-checked** (`exploratory_second_pool/src/claim_schema.py`). Nothing here alters `paperE3`/`paperE4` as published; it specifies what a `SPECIFICATION_v3.md` would have to pre-register.

---

## 0. Objects and notation

A **pool** \(P\) is indexed by a **well** \(w\). No pooling across wells; each pool is its own object.

| Symbol | Meaning |
|---|---|
| \(H_t, R_t, P_t\) | head, recharge driver, pumpage driver |
| \(\rho_H, \rho_R\) | AC(1) of head (= 1 − whiteness of head) and of recharge (= whiteness) |
| \(\mathcal{M}\) | forecast ladder; \(K\) a threshold; \(F\) a recharge floor |
| \((a, \alpha, \beta, \gamma, \delta)\) | the affine map \(H_{t+1}=aH_t+\alpha+\beta R+\gamma P\), with \(a = 1+\delta\) |
| \(H^{*}(P,F)\) | fixpoint under floor \(F\) and pumping \(P\) |
| **\(m(P,K,F) = K - H^{*}_0(P,F)\)** | **attractor-to-threshold margin** (zero pumping) |

---

## 1. The margin lemma (proved, and machine-verified)

The source framework asserts: *if \(m>0\) no positive pumping rule can bridge the gap.* That is true, but only under two hypotheses which the source statement leaves implicit. They matter, so they are stated.

> **Lemma (emptiness from a positive margin).**
> Suppose **H1** \(0 < a < 1\), and **H2** \(\gamma < 0\). For any threshold \(K\), floor \(F\) and pumping rule \(P(\cdot)\ge 0\),
> \[
> m(P,K,F) \;=\; K-H^{*}_0(P,F) \;>\; 0 \quad\Longrightarrow\quad H^{*}_{P(\cdot)} \le H^{*}_0 < K .
> \]
> Hence the trajectory converges monotonically to a level strictly below \(K\), so the infinite-horizon robust kernel at \(K\) is **empty** — for **every** rule, not merely the declared family.
>
> *Proof.* Under **H2**, \(P\mapsto H^*(P,F)=(\alpha+\beta F+\gamma P)/(1-a)\) is strictly decreasing in \(P\); since \(P(\cdot)\ge 0\) pointwise, \(H^*_{P(\cdot)}\le H^*(0,F)=H^*_0\). Under **H1**, \(a\in(0,1)\) makes \(H\mapsto aH+c\) a monotone contraction towards its fixpoint, so \(H_t\to H^*_{P(\cdot)}\le H^*_0<K\); the set \([K,\infty)\) is therefore not invariant, and its largest invariant subset is empty. \(\square\)

Three consequences worth stating explicitly, because they sharpen the source framework:

1. **E4-negative\* is family-free.** The lemma quantifies over *all* rules with \(P\ge0\), not just the declared family. So "no **declared** policy holds \(K\)" is weaker than the truth: no *conceivable* non-negative pumping rule does. This makes E4-negative\* the more portable of the two E4 legs.
2. **H2 is load-bearing and is a fitted-sign assumption.** If \(\gamma\ge0\) (more pumping does not lower the fixpoint), the argument collapses and a positive margin no longer implies emptiness. Both pools satisfy H2 — J-17 \(\gamma=-0.0284\), Uvalde \(\gamma=-0.0102\) — and both are checked programmatically (§5).
3. **The converse does not hold.** \(m<0\) is *necessary* but **not sufficient** for a constructive kernel: it says zero pumping could hold \(K\), which is distinct from *some member of the declared family* doing so within the family's structure. Construction always requires policy-family analysis. (The source framework says this informally; it is a formal two-part statement.)

**Machine check.** Enumerating every (pool × threshold × floor) pair and every policy of the declared family: **15 cases tested, 0 violations** of \(m>0\Rightarrow\) empty. (`claim_schema.py`, §5.)

---

## 2. Two quantitative successors to the margin

The source framework treats \(m\) as an existence test. It also yields two sharp, pre-registrable numbers.

### 2.1 The time-to-emptiness \(T^*\) (the margin in *time*)

Since \(H_t-H^*=a^t(H_0-H^*)\), the latest horizon at which any starting head can still be above \(K\) is

\[
T^*(P,K,F) \;=\; \frac{\ln\!\big[(K-H^*_{P})/(H_{\text{top}}-H^*_P)\big]}{\ln a},
\qquad H^*_P<K,
\]

with \(T^*=\infty\) when the fixpoint clears \(K\). This converts "the kernel is empty" into "the kernel empties by year \(T^*\)" — which is the form E4 actually reports for the J-17 institutional line.

**Verification against E4's published number.** For J-17, training-mean pumping, \(K=618\), perpetual-1956 floor: \(a=0.74609\), \(H^*=615.72\), \(H_{\text{top}}=710\), giving

\[
T^* = 12.70 .
\]

E4 and the frozen specification state the *"continuous crossover is 12.7"* under the paper's own convention, with the \(T=12\) boundary at 692.6 ft and the \(T=13\) kernel empty. The analytic value **reproduces the published constant exactly**, and the empirical first-empty horizon (kernel non-empty at \(T=12\), empty at \(T=13\)) straddles it correctly. \(T^*\) is therefore a validated, transferable statistic, not a new assumption.

### 2.2 The critical floor \(F^*(K)\) (the margin in *recharge*)

Setting \(m=0\) and solving for the floor:

\[
F^*(K) \;=\; \frac{K\,(1-a)-\alpha}{\beta}.
\]

Below \(F^*\) the threshold is out of reach; above it, construction becomes possible. This makes "no margin is floor-free" (the source framework's phrasing) into a specific, pre-registrable threshold, and it *predicts* where the floor-crossing happens.

**Uvalde Pool, verified:**

| \(K\) | \(F^*(K)\) | drought-of-record (19.8) | q05 (54.7) | q10 (71.6) |
|---|---|---|---|---|
| 835 | 28.10 | out of reach → **empty** ✓ | reachable → **non-empty** ✓ | reachable → **non-empty** ✓ |
| 840 | 56.38 | out of reach → **empty** ✓ | out of reach → **empty** ✓ | reachable → **non-empty** ✓ |
| 845 | 84.67 | out of reach → **empty** ✓ | out of reach → **empty** ✓ | out of reach → **empty** ✓ |

Every entry matches the observed kernel table. The \(K=840\) row is the delicate one: \(F^*(840)=56.38\) sits just **1.68 above** the q05 floor (54.7), which is why q05 is empty and q10 is not. That is not a numerical coincidence to be smoothed over — it is a knife-edge, and §4 makes it a reporting requirement.

---

## 3. The generalized claim schemas

Each of E3 and E4 decomposes into a portable and a non-portable part. The Uvalde port decides which is which.

### 3.1 E3*

**E3-mechanism\*** — *portable.*
> For a pool with near-white recharge (\(\rho_R\approx0\)) **and** persistent head (\(\rho_H\) high), persistence is a strong baseline: added stock-flow structure does not robustly improve out-of-sample forecast. Short-horizon gains from *any* temporally structured exogenous regressor are artifacts and are not evidence that structure earns its keep.

**E3-verdict\*** — *portable only as a conjunction.*
> A stock-flow model is retained only if **all** of: (i) Diebold–Mariano significant at the pre-declared level; (ii) bootstrap CI on the RMSE gap excluding zero; (iii) sub-period sign stability; (iv) for mechanism claims, driver-dependence. Point-RMSE ordering alone is **not** a verdict.

*Scope condition for E3-mechanism\*:* near-white recharge **and** persistent head. *Failure mode now documented:* Uvalde satisfies both (\(\rho_R=0.168\), \(\rho_H=0.844\)) yet flips the **point rule** — which is precisely why the conjunction, not the point rule, is the portable statistic.

### 3.2 E4*

**E4-constructive\*** — *scoped.*
> If a pool has a **physical threshold** \(K_{\text{phys}}\) (ecological or legal referent: spring cessation, ESA-listed-species flow requirement) **and** \(m(P,K_{\text{phys}},F)<0\) under the stated floor \(F\), then a non-empty robust kernel **may** exist; policy-family analysis is required to construct it.

*Scope conditions, both required:* (i) a physical threshold must **exist**; (ii) the margin must be **negative**. Condition (i) is structural and is *not* a numerical result.

**E4-negative institutional\*** — *broad, and family-free by the lemma.*
> If a pool has an institutional threshold \(K_{\text{inst}}\) and \(m(P,K_{\text{inst}},F)>0\) under floor \(F\), then **no** non-negative pumping rule holds \(K_{\text{inst}}\). The kernel is empty by structure, and the line is protected by wet years rather than by the pumping family.

The recharge floor \(F\) must be stated explicitly in both; neither statement is floor-free.

---

## 4. Reporting requirements (additions the source framework did not have)

1. **Report \(m\) with its sign, magnitude and the floor.** A bare "empty/non-empty" hides the knife-edge. **Knife-edge rule:** treat \(|m| \lesssim 2\) ft as *indeterminate* and report it as such rather than as a clean binary. (The Uvalde \(K=840\), q05 case has \(m=+0.30\) ft — inside the rule.)
2. **Report \(F^*(K)\)** alongside \(m\), so the distance to the floor-crossing is visible.
3. **Report \(T^*\)** whenever a negative result is quoted, so "empty" carries a horizon.
4. **Verify H1 and H2 for every pool.** The lemma is void if either fails; both are fitted-sign assumptions and must be asserted, not assumed.
5. **State the domain used for the kernel.** The domain floor \(H_{\text{LO}}\) and top \(H_{\text{HI}}\) enter both the kernel recursion and \(T^*\); a domain change can silently change an emptiness verdict. Pre-register the domain with the clip bounds.

> **Worked example of why (5) matters.** During the implementation of this protocol, a kernel port that omitted the domain floor \(H_{\text{LO}}\) from the policy piece-splitting routine collapsed every *constant* (no-threshold) policy to a degenerate point interval. The effect was to report **every flat policy kernel as empty** — a false negative that would have inverted the construction verdict at Uvalde \(K=835\)/q05 and \(K=840\)/q10. It was caught only because the margin framework *predicted* non-emptiness in those cells. The framework thus served as its own test: a structural prediction falsified a numerical implementation.

---

## 5. Machine-checked status

| Check | Result |
|---|---|
| Lemma hypotheses H1 (0<a<1) | holds for both pools |
| Lemma hypotheses H2 (γ<0) | holds for both pools (J-17 −0.0284; Uvalde −0.0102) |
| Lemma violations, \(m>0\Rightarrow\) empty | **0 / 15 cases** |
| \(T^*\) vs E4's published crossover | **12.70 vs 12.7 — exact** |
| \(F^*(K)\) vs observed kernel table | **9 / 9 (×3 thresholds ×3 floors) correct** |
| E4-constructive\* definable on Uvalde? | **No** — no physical threshold |
| E4-negative\* holds on Uvalde? | **drought ✓, q05 ✓, q10 ✗** (m = −2.69) |
| E3-mechanism\* in scope, both pools | **Yes** |

Reproduce: `python3 src/claim_schema.py` → `results/claim_schema_results.json`.

---

## 6. Pre-registration requirements for a v3

A `SPECIFICATION_v3.md` should be written **before any confirmatory score**:

1. **Name the transferable invariant.** It is the **margin \(m(P,K,F)\)**, together with its two quantitative successors \(F^*(K)\) and \(T^*\). Physical-threshold **existence** is a scope condition, not an invariant.
2. **Pre-specify the E3 decision rule** as the four-part conjunction (§3.1). Any conjunct failing ⇒ verdict **not met**, regardless of point-RMSE ordering.
3. **Pre-register the free porting parameters:** clip bounds, the domain \((H_{\text{LO}},H_{\text{HI}})\), the recharge-driver mapping, and the pumpage driver.
4. **Control multiplicity** across pools × thresholds × horizons × floors × driver definitions, and state the correction.
5. **State scope limits up front.** E4-constructive\* generalizes only to pools with a physical threshold and \(m<0\); the Uvalde Pool is **out of scope for that claim by construction**.
6. **Adopt the §4 falsification conditions as v3 acceptance tests**, written before scores are computed.

---

## 7. What the Uvalde port establishes for generalization

1. **E3-mechanism\* replicates** (\(\rho_R=0.168\), \(\rho_H=0.844\)); **E3-verdict\* does not** (the point rule flips, non-robustly).
2. **E4-negative\* replicates** and, by the lemma, is *stronger* than the declared-family statement: at Uvalde's 840 ft and 845 ft lines no non-negative rule holds either line under any tested floor.
3. **E4-constructive\* does not transfer**, for a structural reason: the pool has **no physical threshold**, and \(m(840)=+6.47\) ft under the drought floor.
4. The narrow \(K=835\) non-emptiness under milder floors is an honest consequence of \(F^*(835)=28.10\) falling below the q05 floor — **a predicted crossing, not a replication**.
5. **The decisive blocker is structural, not numerical:** physical-threshold existence and the sign of the margin are the transferable scope conditions.

---

## 8. Bottom line

Separate each paper into its portable and non-portable part.

- **E3:** generalize the **mechanism**; reject the **point-rule verdict** in favour of the conjunction.
- **E4:** generalize the **negative institutional** verdict broadly (it is family-free by the lemma); generalize the **constructive** leg only to pools with a **physical threshold** and a **negative margin**, always stating the recharge floor.

The Uvalde Pool is comparable for the forecast-ladder and institutional-threshold questions, and out of scope for the constructive intervention question by construction. The margin \(m\) is the comparator that decides this; \(F^*\) and \(T^*\) are how it is reported.

---

## 9. Which v3? (rev 5 — see `V3_SELECTION.md`)

This document specifies *how* a v3 would have to be written. `V3_SELECTION.md` decides *which* v3 to write, in response to the `generalizing2` review. Headline: **pursue v3-C restated as the margin specification (which absorbs v3-B as its other sign); decline v3-A**, on power grounds rather than taste. The review's premise that **no third pool exists** is false — the **Barton Springs segment** (BSEACD, index well Lovelady, physical threshold = Barton Springs flow 6.5 cfs per the GMA-10 drought-of-record DFC and the 2018 HCP) is a distinct, separately regulated, **still-unanalyzed** pool of the right structural kind. Two caveats are carried there and both must clear before a v3 is written: Lovelady's short continuous annual coverage, and unvalidated machine retrieval. The review's own strongest point — **the exploratory pool (Uvalde) is spent as a confirmatory object** — is adopted verbatim; Uvalde is demoted to motivating case.

**Rev 5 (post-review) — the verdict is now *conditional*, and two gates are open.** `V3_SELECTION.md` rev 2
closes three of five gates and leaves two binding:

| gate | status |
|---|---|
| R04 case — *no judgment transferred*, only the scalar relation `m = K − H*₀`, every parameter pool-local | argued (the jurisdictional argument alone was insufficient) |
| **Declared-family equivalence** — BSEACD's curtailment rule vs E4's `P ∈ [0, K_PHYS]` | **RESOLVED (rev 6).** Same functional shape (multiplicative piecewise-constant cuts off an authorized baseline, ρ=0 admitted; cuts 20/30/40/50% vs E4's 20/30/35/40%), but a strict **superset**: two trigger variables (Q, H_L) and **hysteresis** (enter on either, exit on both). **B clears unconditionally** — the lemma bounds *any* non-negative pumping sequence, so it subsumes multi-variable and path-dependent rules. **C clears only under the E4-comparable subfamily restriction** (single state variable, memoryless, cuts at declared triggers), which makes a positive result conservative. |
| H1/H2 failure decision rules (scope exclusion vs falsification) | **closed** — machine-encoded, `src/v3_gate_checks.py` |
| **Springflow map-form pre-check** — fit the map to springflow and verify H1/H2 *before* any sign test | **RUN, FAILED (rev 7).** Record starts **1978-03-01** (49 annual obs — the "long record" premise was false); **â = 0.178, CI [−0.109, 0.465] contains zero** so the attractor collapses to the mean and the lemma's dynamical content is absent; **H2 unverifiable** (no machine-retrievable BSEACD pumpage); the **1950s drought-of-record lies outside the gauge**. |
| Multiplicity enumerated — **120** cells (gate 2 replaced guessed thresholds with BSEACD's five *declared* triggers), Holm–Bonferroni within specification-family, α = **0.00083** | **closed** |

Three further changes: **v3-B is now scored, not assumed** (`m > 0` for institutional thresholds is an empirical
regularity, not a definition); the **fallback to v3-B on Barton Springs is withdrawn** (if the gates fail, write
no v3 — a weak v3 spends the pool and buys little); and the **E3 half** is stated rather than left silent — E3
does not generalize in *verdict* form (scope limit) but does in *mechanism* form (recharge whiteness, head AC(1)
moderator, M1 convergence), as a theoretical extension outside v3-C's claim set.

**Rev 7 — FINAL: no v3.** All five gates have now been run. Gates 1, 2, 3 and 5 clear; **gate 4 fails on four
independent grounds** (see table). Under the pre-committed rule *"if the gate fails, do not write a v3"*, the
outcome is **do not promote v3** — now a demonstrated conclusion rather than a default. Barton Springs remains
**naive** and available for a properly powered future test.

Two results survive the closure and are worth carrying forward independently of the v3 question:

1. **E4-negative\* is family-free even against a strict superset.** Gate 2 established that BSEACD's declared
   family is a superset of E4's — two trigger variables and **hysteresis** — and the margin lemma still
   subsumes it, because it bounds *any* non-negative pumping sequence. This strengthens E4's negative leg.
2. **The M1-loss mechanism** (record §3.2a): AR(1) converges on persistence as head AC(1) → 1, which predicts
   the retention flip's direction without fitting the flip. An E3 mechanism note, not a v3.

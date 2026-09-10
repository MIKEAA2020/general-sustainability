# Exploratory Second-Pool Record — Uvalde Pool (J-27)

**Date:** 10 Sep 2026 (revision 3 — margin framework verified and implemented; see revision log)
**Status: EXPLORATORY. NOT FROZEN.** Outside `wave_e_edwards/protocol.md`; may **not** alter any conclusion of `paperE3`/`paperE4` as they stand. Purpose: generate evidence for or against a later pre-registered `SPECIFICATION_v3.md`.

**Terminology.** The *object* is the **Uvalde Pool** of the Edwards (Balcones Fault Zone) Aquifer; its **index well is J-27** (TWDB state well 6950302, Uvalde County, EAA cooperator ID J27; record 1940-10-24 → 2026-09-03). The no-pooling/no-transfer discipline (R04, `SPECIFICATION_v2.md`) is about *pools*, not wells; this record therefore speaks of **pools**, indexed by **wells**. Scored as its own pool — **no pooling**, exactly as Northern cod is scored as its own object.

**Port validation (two independent anchors).**
1. *Ladder port:* reproduces every frozen J-17 value exactly — persist 13.23, M1 12.84, M2 14.70, M2m 12.28, oracle 7.55; h5 M2m 17.44, persist 21.11.
2. *Intervention port:* reproduces the published E4 worst-case attractor for training-mean pumping, **H\* = 615.72 ft**, to the cent.

**Multiplicity note (exploratory).** This record makes many uncorrected comparisons (6 recharge-driver definitions × 2 horizons × 2 pools; 3 thresholds × 3 floors × 6 policies; 4 clip settings). Every p-value and interval below is **exploratory and uncorrected**; none may be read as a confirmatory result. Multiplicity control for a v3 is specified in §6.2.

---

## 3.0 Falsification conditions, stated in advance of the findings

To keep the conclusion auditable rather than rhetorical, these were the conditions that would have counted as **robust** replication. **Neither was met.**

| Claim | Would count as a robust replication | Met? |
|---|---|---|
| **E3** (persistence beats added stock-flow structure) | On J-27: DM significant at the pre-declared level, **and** bootstrap CI on the RMSE gap excluding zero, **and** sub-period sign stability, **and** D5-style driver dependence (mismatched driver changes the result) | **No** — all four fail (§3) |
| **E4** (reactive rules earn a nominal supply margin at the *physical* threshold; nothing protects the *institutional* threshold) | On the Uvalde Pool: a **non-empty** robust kernel at a declared threshold under the drought-of-record floor, i.e. an analog of E4's constructive leg | **No** — no construction is possible; the deeper reason is structural (§4, §5.0) |

Two further pre-stated conditions, both of which **were** met, and which are therefore load-bearing below:

- **E3 mechanism** (recharge is near-white, so persisting it fails): would replicate if Uvalde recharge is also near-white. **Met** (§2).
- **E4 institutional verdict** (the line is protected by wet years, not the pumping family): would replicate if no declared policy holds the institutional threshold under the drought floor. **Met, more strongly than on J-17** (§4).

---

## 1. Data and declared porting choices

| Element | J-17 pool (frozen) | Uvalde Pool (this record) |
|---|---|---|
| Head | `j17_twdb_6837203_raw.csv` | `j27_twdb_6950302_raw.csv` (TWDB 6950302; pulled from `waterdatafortexas2.org` — the primary `waterdatafortexas.org` data endpoints returned HTTP 503 on 2026-09-10) |
| Annual rule | mean of daily highs; year dropped if < 240 days | identical |
| Domain | 1934–2023 (90 usable years) | 1941–2023 (81 usable years) |
| Recharge driver | `Total` (San Antonio area) | `Basin_1 + Basin_2` (Nueces-West Nueces + Frio-Dry Frio = Uvalde-area basins) — **weakest comparability link**, see §3.3 |
| Pumpage driver | `wells_kaf` | `uvalde_kaf` |
| Clip bounds | [610, 710] ft (model domain) | [820, 890] ft (rounded observed extremes; **verdict-insensitive**, §3.4) |
| Thresholds | 618 (physical/Comal-cessation), 660 (institutional) | 840 (Uvalde Stage V), sweep {835, 840, 845} |

All driver series are the **committed** ones in `wave_e_edwards/data/`; no new driver data was introduced.

---

## 2. Result A — the E3 *mechanism* replicates

| Statistic | J-17 pool | Uvalde Pool |
|---|---|---|
| recharge AC(1) | 0.172 | **0.168** |
| corr(ΔH, R) | 0.739 | 0.485 |
| head AC(1) | 0.644 | **0.844** |
| head SD (ft) | 14.78 | 14.77 |

Near-white recharge is **not** a San Antonio peculiarity. Note the useful accident that the two head series have **essentially identical SD (14.78 vs 14.77)**, so their RMSEs are directly comparable — and that Uvalde's higher head AC(1) makes persistence a **stronger** baseline there (`§3`, D6).

---

## 3. Result B — the E3 **point-rule retention nominally flips**, but is not a verdict

Applying the *same* frozen retention rule to J-27 (h = rolling-origin out-of-sample):

| model | h=1 RMSE | h=5 RMSE |
|---|---|---|
| naive_persist | 8.09 | 18.16 |
| naive_mean | 13.98 | 14.29 |
| M1 (AR1) | 8.23 | 17.18 |
| **M2 (stock-flow)** | **7.25** | 21.70 |
| M2m | 8.10 | 16.71 |
| oracle | 7.40 | 13.43 |

`retained_as_structure = ['M2']` — the **point rule** retains structure on the pool, whereas on J-17 it retained only M1. **The verdict does not flip; the point rule does** — and the record shows the point rule is not a reliable verdict statistic on this sample:

| Diagnostic | Result | Reading |
|---|---|---|
| **D1** Diebold–Mariano, M2 vs persist (h=1) | z = **−1.256** | insignificant (\|z\| < 1.96) |
| **D2** moving-block bootstrap, RMSE gap (10k, block 8) | 95% CI **[−1.77, +0.94] ft** | **covers zero** |
| **D3** origin-level | M2 wins **38/66** (58%) | barely above a coin flip |
| **D4** sub-period | early gap **−0.15**, late −1.56 | essentially zero for half the sample |
| **D5** driver independence | see §3.3 | the flip is **not** attributable to the recharge series |
| **D6** head/recharge persistence | head AC(1): J-17 **0.644**, J-27 **0.844**; recharge AC(1): 0.172 / 0.168 | persistence is a *stronger* baseline on Uvalde, which makes the flip more surprising, not less |

### 3.2 The h1-vs-h5 divergence, and a hypothesis that fails

A natural hypothesis is that M2's h1 edge is the **δ·H mean-reversion term** absorbing one-step noise, which would also explain why it dies at h=5. **C4 tests this directly and falsifies it.**

Decomposing M2 by which driver column it is given (gain = persist RMSE − M2 RMSE at h=1; positive = M2 better):

| M2 variant | Uvalde gain (h1) | Uvalde M2 (h5) | J-17 gain (h1) |
|---|---|---|---|
| full (R + P) | **+0.84** | 21.70 | −1.47 |
| **R only** | **+0.99** | 21.08 | −0.74 |
| P only | −0.14 | 16.56 | −0.23 |
| **neither (constant R, P → pure δ·H mean reversion)** | **−0.18** | 18.41 | +0.75 |

The mean-reversion-only variant **loses** on Uvalde (−0.18). So the h1 edge requires an **actual exogenous regressor column**, not the δ·H term. The correct reading is:

- The edge is a **short-horizon artifact of including any exogenous regressor with real temporal structure**, which reduces one-step predictive variance; it is why the point rule flips at h = 1 and why it reverses at h = 5 (M2 is **+3.53 ft worse** than persistence at h5).
- Pumpage (P) does **not** carry it (P-only −0.14); recharge (R) does (R-only +0.99).
- On J-17 the R column makes M2 **worse** (−0.74), the opposite sign — the structural difference between the pools is real, and it is *not* explained by the mean-reversion hypothesis.

**These are the E3 results that were NOT met:** a flipped point rule is not a replication, and the one candidate mechanism for the flip is falsified.

#### 3.2a Erratum (rev 5) — a mechanism for the flip *does* exist, and it is M1's loss, not M2's gain

Revisions 1–4 glossed the flip as "persistence is a stronger baseline on Uvalde, which makes the flip more
surprising, not less." **That reads the sign backwards.** The flip's proximate cause is not that M2 improved but
that **M1 (AR1) stopped beating persistence**:

| pool | head AC(1) | persist h1 | M1 h1 | M1's edge |
|---|---|---|---|---|
| J-17 (full window) | 0.6437 | 13.2301 | 12.8391 | **+0.391** (M1 wins) |
| J-17 (matched 1941–) | 0.6437 | 13.7623 | 13.1265 | **+0.636** (M1 wins) |
| Uvalde (native window) | 0.8442 | 8.0933 | 8.2250 | **−0.132** (M1 loses) |

As head AC(1) → 1 an estimated AR(1) converges on persistence, so its RMSE edge decays into estimation noise.
High head persistence therefore **predicts** M1's failure and hence the ladder's escalation to M2 — it does not
make the flip surprising. Verified in `src/v3_gate_checks.py` (`erratum_M1_edge`); holds under both J-17 windows,
so it is not a window artifact.

**Scope of this correction.** It does **not** overturn C4 (§3.2 above): C4 falsifies mean reversion as the source
of M2's *gain* (−0.18 for the mean-reversion-only variant), which is a **different event** from M1's *loss*. Both
findings stand. The correction is to the interpretive gloss only; no numbers in §3 change.

Because the mechanism is monotone in AC(1) and mechanistic rather than statistical, it is carried forward as a
**secondary prediction** for any future third pool — see `V3_SELECTION.md` §6.2.

### 3.3 Driver choice — the weakest comparability link

`Basin_1 + Basin_2` was asserted as the Uvalde analog of San Antonio `Total`. Disclosure of the criterion: B1 and B2 are the two drainage basins whose gaged outlets lie on the Nueces/West Nueces and Frio/Dry Frio rivers **within or immediately upstream of Uvalde County** (USGS stations 08190000/08190500/08192000 and 08195000/08196000/08197500); B3 (Sabinal) and B4 (inter-basin) extend past Uvalde toward Medina. Full ladder:

| R definition | M2 h1 | M2 h5 | M2 retained? |
|---|---|---|---|
| Basin_1 only | 7.22 | 21.17 | yes |
| Basin_2 only | 7.22 | 22.10 | yes |
| **Basin_1+2** | 7.25 | 21.70 | yes |
| Basin_1–4 | 7.11 | 22.26 | yes |
| **San Antonio `Total` (mismatched)** | 7.05 | 22.33 | **yes** |
| **shuffled (null)** | 8.40 | 16.66 | **no** |

Two disclosures follow. First, the h1 "win" survives **every** real driver, including the explicitly mismatched one — so the chosen mapping is *not* load-bearing, and this is the reason the comparison is not about recharge. Second, the shuffled null **does** destroy it (8.40 > 8.22), which sharpens §3.2: the edge needs *some* temporally structured exogenous column, not the *correct* one. Comparability risk attached to the driver mapping is therefore **low for the E3 leg** — and correspondingly, the driver mapping cannot be credited for the flip either.

### 3.4 Clip bounds — a free parameter that is not load-bearing

`[820, 890]` was rounded observed extremes; unlike J-17's [610, 710] (a declared model domain tied to spring elevation and aquifer base), the Uvalde clip has **no named physical referent**. It is therefore a **free comparability parameter**. Sensitivity:

| clip | M2 h1 | M1 h1 | persist h1 | M2 retained? |
|---|---|---|---|---|
| [820, 890] | 7.25 | 8.23 | 8.09 | yes |
| [800, 920] | 7.74 | 8.24 | 8.09 | yes |
| [822.7, 884.9] (exact observed) | 6.99 | 8.20 | 8.09 | yes |
| [700, 1000] (effectively unclipped) | 7.74 | 8.24 | 8.09 | yes |

The retention outcome is **invariant** to the clip; only the M2 magnitude moves (7.0–7.7). The clip is a free parameter that a v3 should pre-register, but it does **not** drive the conclusion.

### 3.7 Effect size — is 0.84 ft meaningful?

- The h1 gap is **0.84 ft**, i.e. **5.7%** of the head-series SD (14.77 ft).
- Operational thresholds are declared in **whole feet** (845 / 840 / 835), and the EAA's actual rule is a **10-day average**; a 0.84 ft RMSE edge is far below the quantity that decides protection.
- For contrast, the quantities that *do* decide protection in this system are **attractor-to-threshold gaps of roughly 6–45 ft** (§5.0). The E3 effect is an order of magnitude smaller than the E4 effects, which is consistent with E4's results mattering for management and E3's not.

### 3.8 The two missing controls — D5 applied to J-17, and the matched window
Both were named in review as "the single most important missing diagnostic" and "cheap and decisive". Both were run.

**(a) Matched-window control (J-17 restricted to 1941–2023, the Uvalde window).** The 1930s drought of record sits in J-17's window but not Uvalde's, so this tests whether the cross-pool comparison is confounded by window.

| J-17 window | n | persist | M1 | M2 | M2m | retained_as_structure |
|---|---|---|---|---|---|---|
| 1934–2023 (frozen) | 90 | 13.23 | 12.84 | 14.70 | 12.28 | `['M1']` |
| **1941–2023 (matched)** | 83 | 13.76 | 13.13 | 15.74 | 12.95 | **`['M1']`** |

**The E3 verdict is unchanged by the window.** The cross-pool comparison is **not** confounded by the window difference. (Magnitudes shift upward by ~0.3–1.0 ft, i.e. the 1930s drought makes the ladder look *better*; the ordering and outcome do not move.)

**(b) Mismatched-driver control applied to the home pool.** This is the direct test of whether E3's mechanism is about recharge at all:

| driver given to M2 on J-17 | M2 h1 | M2 retained? |
|---|---|---|
| `R_total` (correct) | 14.70 | **no** |
| Uvalde `Basin_1+2` (mismatched) | 13.84 | **no** |
| shuffled (null) | 13.46 | **no** |

**E3's non-retention is driver-independent on its own pool** — M2 fails to beat persistence under the correct driver, a mismatched driver, and a shuffled null alike. That **strengthens** E3: the claim "structure does not earn its keep" does not depend on the recharge series being right.

A secondary observation worth recording: on J-17 the **correct** driver gives M2 *worse* h1 error (14.70) than a **shuffled** one (13.46). That is consistent with E3's own diagnosis that the pumpage/recharge coefficients carry simultaneity contamination (paper §5.2) — the fitted recharge association is not a clean forecasting channel on J-17.

---

## 4. Result C — the E4 *institutional* verdict replicates; the *constructive* leg does not transfer for a structural reason

Port of the intervention leg (affine map fitted on transitions to ≤ 1990, n = 48; audit 1991–2023, n = 32):

- Fit signs match E4's: **a = 0.857** (contraction), **β(R) = +0.0253**, **γ(P) = −0.0102**.
- Declared defect: train \|resid\| max = **24.03 ft**; OOS max 15.66 ft.
- Floors (Uvalde recharge): drought-of-record 19.8, q05 54.7, q10 71.6 (×10³ acre-ft).
- Institutional threshold: **840 ft** (Uvalde Stage V); historic stages 845 (I) / 840 (II) / 835 (III).

### 4.0 **Corrections to revisions 1 and 2 (kernel status under all three floors)**

> **Revision 3 supersedes both.** Rev 1 said "every kernel is empty at every Uvalde threshold" (wrong). Rev 2 corrected it to "`cpm_uv` alone is non-empty at 835 under q05/q10" — **also wrong**, because of an implementation defect described below. The table below is the verified one.

**Implementation defect found and fixed.** My kernel port omitted the model-domain floor \(H_{\text{LO}}\) from the policy piece-splitting routine (`_pieces`), collapsing every *constant* (no-threshold) policy to a degenerate point interval. That reported **every `flat_*` and BAU kernel as empty** — a false negative. It was caught by the margin framework (§4.1), which *predicted* non-emptiness in exactly the cells that came back empty. After aligning `_pieces` and `_normalize` with the frozen implementation (`wave_e_edwards/src/run_intervention.py`), the port reproduces E4's published J-17 behaviour exactly (BAU at 618 empty; every flat cut of 10% or deeper giving `[618, 710]`).

**Corrected table** (nominal robust kernels, Uvalde Pool):

| threshold | drought-of-record (19.8) | q05 (54.7) | q10 (71.6) |
|---|---|---|---|
| **835** (Stage III) | *none* | flat_0, flat_50–80, S1uv, cpm_uv | + flat_90, **BAU** (all policies) |
| **840** (Stage V) | none | none | **flat_0, flat_50** |
| **845** (Stage I) | none | none | none |

The verified reading is **monotone in both directions — the margin theory's prediction**: raising \(K\) shrinks the constructive set; lowering the floor (milder recharge) grows it. At the current institutional line (840) and Stage I (845) nothing is holdable under any tested floor; at 835 the constructive set appears once the floor passes \(F^*(835)=28.10\). This is a *narrower and better-explained* analog of E4's constructive leg than either rev 1 or rev 2 reported. The Uvalde Pool is not "nothing works" — it is "nothing works at a margin, and the margin is the whole story".

### 4.0b The margin \(m\) — the general rule the corrections obey

Both rev-1 and rev-2 errors are explained, and can be *predicted*, by one quantity:

\[
m(P,K,F) = K - H^{*}_0(P,F), \qquad H^{*}_0 = \frac{\alpha + \beta F}{1-a}
\]

the distance from the **zero-pumping** drought-floor fixpoint to the threshold. Since \(\gamma<0\) (both pools), zero pumping is the **most protective** policy, so \(H^*_0\) is the largest achievable attractor. Hence (Lemma, proof and machine check in `GENERALIZATION_PROTOCOL.md` §1):

> \(m>0\) ⟹ the infinite-horizon kernel at \(K\) is empty for **every** non-negative rule, declared family or not.

Verified: **15 (pool × threshold × floor) cases, 0 violations.** This is a *family-free* statement, so it strengthens E4's negative leg beyond "no declared policy holds \(K_{\text{inst}}\)".

The companion quantity is the **critical floor** \(F^*(K)=\big(K(1-a)-\alpha\big)/\beta\), the recharge floor at which \(m=0\). It **predicts** the corrected table above:

| \(K\) | \(F^*(K)\) | prediction | observed |
|---|---|---|---|
| 835 | 28.10 | empty at drought (19.8); non-empty at q05/q10 | ✓ |
| 840 | 56.38 | empty at drought **and q05** (54.7, just below); non-empty at q10 | ✓ |
| 845 | 84.67 | empty at every tested floor (all < 84.67) | ✓ |

**9/9 rows correct.** The \(K=840\)/q05 cell is a **knife-edge**: \(F^*(840)\) sits only 1.68 above the q05 floor (\(m=+0.30\) ft). It is reported as *indeterminate*, not as a clean "empty".

A third quantity makes negative results carry a horizon: the **time-to-emptiness** \(T^*=\ln[(K-H^*)/(H_{\text{top}}-H^*)]/\ln a\). For J-17, BAU at \(K=618\) under the perpetual-1956 floor it evaluates to **12.70**, reproducing E4's published "continuous crossover is 12.7" exactly (empirical first-empty horizon: \(T=13\)). Uvalde \(K=840\): \(T^*=15.1\) (drought), 34.4 (q05), \(\infty\) (q10).

### 4.1 Where the constructive leg fails, and why — the attractor-to-threshold gap

The decisive structural variable is the **distance from the map's drought-floor attractor to the threshold**. Under the drought-of-record floor, with zero pumping (no policy can do better):

| pool | threshold | zero-pumping fixpoint H\* | gap (K − H\*) | holdable? |
|---|---|---|---|---|
| **J-17** | 618 (physical) | 647.32 | **−29.32** | **YES** — cutting pumping is sufficient |
| J-17 | 618, at BAU | 615.72 | +2.28 | no |
| J-17 | 660 (institutional) | 615.72 | +44.28 | no |
| **Uvalde** | 840 (institutional) | 833.53 | **+6.47** | **NO** — even zero pumping falls short |

This single comparison explains the whole pattern:

- E4's constructive result exists on J-17 because the **physical threshold sits 29 ft below** the zero-pumping drought-floor attractor — there is a margin for a pumping rule to buy. (It reproduces E4's own "a 7.2% mean cut secures the threshold".)
- On the Uvalde Pool, the analogue fails at the **first** step: the zero-pumping attractor is itself **6.5 ft short** of 840. No pumping rule can bridge a gap that zero pumping cannot. Hence empty kernels at 840/845 — and hence the narrow `cpm_uv` survival at 835, which is *below* 833.53+2.3 and therefore inside reach under the milder floors.

**This is the load-bearing comparable quantity a v3 must formalize** — more explanatory than raw fixpoints, and it is a property of the pool's hydrology plus its threshold choice, not of the policy family.

### 4.5 Is there a Uvalde physical/ecological threshold? — surveyed, and there is none

Revision 1 asserted Uvalde "has no spring-cessation analog". That claim was load-bearing for E4's constructive leg, so it was surveyed:

- The **EAHCP covers only Comal and San Marcos Springs**. Its stated purpose is "to provide assurance that suitable habitat for covered species will remain in both the San Marcos and Comal Springs"; the covered species (fountain darter, Comal Springs riffle beetle, Texas blind salamander, etc.) are Comal/San Marcos species; flow-protection measures (ASR, VISPO) are for those two springs. The EAHCP FAQ frames Uvalde and Medina counties explicitly as **contributors to protecting Comal & San Marcos**, not as protected systems.
- The San Antonio Pool's 618 ft line exists because Comal Springs approaches **cessation**, which is an ESA-listed-species limit. The Uvalde Pool has **no analogous endangered-species springflow requirement**, and therefore no physical/ecological threshold of the Comal kind.
- The **nearest candidate is rejected as unsuitable**: an EAHCP alternative proposed a Uvalde trigger at **865 ft MSL**, but (i) it was part of an alternative that was **not pursued**, and (ii) it was keyed to the long-term average flows of *Comal and San Marcos*, not to Uvalde's own springs. It is not a Uvalde physical limit.
- The Uvalde Pool's own critical-period triggers (845/840/835) are **purely institutional** stage levels, with no underlying physical-cessation referent.

**Conclusion (demonstrated, not asserted):** the Uvalde Pool has **no physical-threshold analog**, so E4's constructive leg is **not definable** there. This is a *structural* non-comparability — not a numerical failure of the port. The generalization of E4's constructive claim is therefore to pools that **have** a physical threshold with positive margin, and the Uvalde Pool is **out of scope for that claim by construction**.

---

## 5.0 Comparability audit table

The artifact a v3 would inherit — one row per porting choice.

| Choice | Pool-invariant? | Evidence | Residual risk |
|---|---|---|---|
| Head series (annual mean of daily highs, ≥240-day year) | **Yes** | identical construction; TWDB/ EAA serve both wells on the same schema and datum convention | low |
| Annual rule (calendar-year mean) | **Yes** | verbatim port; both validated against frozen anchors | low |
| Domain / window | **Yes** | C1: J-17 verdict unchanged on the matched 1941–2023 window | low |
| Recharge driver mapping | **Partly** | C3: the conclusion is *not* sensitive to the mapping (survives B1, B2, B1+2, B1–4, and mismatched). But this also means the mapping cannot be *credited* for the E3 flip | **low for E3; unusable for v3 credit** |
| Pumpage driver (`uvalde_kaf` vs `wells_kaf`) | **Untested** | C4 shows P does not carry the h1 edge on either pool | moderate — untested as a standalone comparison |
| Head AC(1) (0.644 vs 0.844) | **No — differs** | C8/D6; makes persistence a stronger baseline on Uvalde, so the pools are **not** exchangeable baselines | **high** — a real structural difference |
| Clip bounds | **No — free parameter** | C5: verdict invariant across four settings | low for conclusions; must be pre-registered |
| **Attractor-to-threshold gap** | **No — decisive** | C7: J-17 flat-0 clears 618 by 29 ft; Uvalde flat-0 misses 840 by 6.5 ft | **decisive** — determines whether any constructive claim is definable |
| Physical threshold existence | **No — absent on Uvalde** | §4.5 (EAHCP covers Comal/San Marcos only) | **decisive** — E4 constructive leg out of scope |
| **Kernel domain (H_LO, H_HI)** | **No — free, destructive if wrong** | rev-3 bug: omitting H_LO from `_pieces` emptied every constant-policy kernel | **high** — must be pre-registered with the clip bounds |
| Recharge floor F | **No — decisive** | F*(K) locates every crossing; no margin is floor-free | **decisive** — must be stated with every claim |
| Institutional thresholds (840 vs 660) | **Partly** | both are declared stage levels, and both sit *above* their own zero-pumping drought-floor attractors — Uvalde by **+6.47 ft**, J-17 by **+12.68 ft**. Same qualitative role, different margins | low (same qualitative role; margins differ) |

**Read-out:** the two objects are comparable for the **forecast-ladder** question and for the **institutional-threshold** question, and are **not** comparable for the **constructive intervention** question. The comparator that decides this is the attractor-to-threshold gap.

---

## 6. Bottom line

**Recommendation unchanged and now better supported: do not promote a v3 on this evidence.**

1. The apparent E3 success is a **point-rule flip**, not a verdict; it is within noise (D1–D4), driver-independent (C3), and its only candidate mechanism was **falsified** by the component decomposition (C4). Meanwhile E3 is **strengthened** on its home pool: its non-retention survives the matched window (C1) *and* mismatched and null drivers (C2).
2. The one clean replication is E4's **negative** institutional verdict, which is already E4's content and which replicates *more strongly* on Uvalde.
3. The corrected kernel table (§4.0) shows the non-emptiness is **monotone in \(K\) and in the floor, exactly as the margin theory predicts**, with the crossings located by \(F^*(K)\) — enough to make the negative result honest, not enough to replicate.
4. The decisive blocker is **structural**: the Uvalde Pool has no physical threshold (§4.5), and its zero-pumping drought-floor attractor falls 6.5 ft short of its own institutional line — so E4's constructive leg cannot be defined there at all.
5. The two rev-1/rev-2 kernel errors were **caught by the margin framework itself**, which predicted non-emptiness in cells the buggy code called empty. A structural prediction falsifying an implementation is the strongest available check on a port of this kind, and it is why the margin is the right transferable object.

### 6.2 What a v3 would need (proposal only)

A `SPECIFICATION_v3.md` should, *before* any confirmatory score:

1. **Justify comparability formally under R04.** This record supplies the audit in §5.0: the transferable quantity must be named, and it is *not* "pools of the same aquifer". The candidate invariant is the **attractor-to-threshold gap**, and the physical-threshold **existence** requirement must be stated as a scope condition.
2. **Pre-specify the replication statistic and decision rule.** Given D1–D3, a point-RMSE comparison is underpowered and non-robust. Require a conjunction: DM significant at the pre-declared level **and** bootstrap CI excluding zero **and** sub-period sign stability **and** (for mechanism claims) driver-dependence — decided in advance.
3. **Pre-register the porting parameters** that §5.0 flags as free or untested: clip bounds, driver mapping, and the pumpage-driver comparison.
4. **Control multiplicity** across pools × thresholds × horizons × floors × driver definitions, and state the correction explicitly.
5. **State the scope limit up front:** if the constructive claim requires a physical threshold with positive gap, the generalization is to pools *with* such a threshold; the Uvalde Pool is out of scope for that claim by construction.
6. **Adopt the falsification conditions of §3.0 as the v3 acceptance test**, written before scores are computed.

Until such a v3 exists and its pre-registered tests are run, these Uvalde Pool results stay **exploratory**.

---

## 7. Reproducibility

| Artifact | Path |
|---|---|
| Port + Uvalde ladder | `exploratory_second_pool/src/run_j27_exploratory.py` |
| Diagnostics D1–D6 | `exploratory_second_pool/src/diagnose_j27.py` |
| Intervention-leg port | `exploratory_second_pool/src/run_j27_intervention.py` |
| **Controls C1–C9 (this revision)** | `exploratory_second_pool/src/controls_and_strengthening.py` |
| **Machine-checkable claim schema (rev 3)** | `exploratory_second_pool/src/claim_schema.py` → `results/claim_schema_results.json` |
| **Generalization protocol / v3 pre-registration (rev 3)** | `exploratory_second_pool/GENERALIZATION_PROTOCOL.md` |
| Inputs | `exploratory_second_pool/data/` |
| Machine-readable results | `exploratory_second_pool/results/*.json` |
| Uvalde annual panel | `exploratory_second_pool/results/j27_annual_panel.csv` |

Deterministic; seeds fixed (bootstrap 20260910; shuffles 7 and 11). Sources for §4.5: EAA/EAHCP public materials on the Covered Species, the flow-protection measures, and the Comal/San Marcos scope of the plan; USGS recharge basins (`usgs_recharge_basin_inputs.txt`, committed); TWDB well records.

### Revision log

**Rev 10 (10 Sep 2026) — content-loss audit after the repo cleanup. FOUR real losses found and RESTORED.**
The cleanup deleted only GitHub-tracked files, so nothing was unrecoverable — but four items the papers
genuinely need had been removed, and one deeper problem was uncovered:
1. **All six figures E3/E4 include** (`figs_e3/fig1_series … fig5_fibre`, `figs_e4/fig1_attractors`) were
   deleted. Without them **neither paper compiles.** Restored from GitHub; all six `\includegraphics` targets
   now resolve.
2. **`wave_e_edwards/data/` (11 files) and `results/` (21)** were never in the local clone at all. Restored,
   together with `manuscript/` (16). Every non-generated asset the `src/` pipeline reads now resolves
   (`annual_panel_hrp.csv` is a generated scratch file, not content).
3. **The `.md` sources of both papers and the `wave13/` build toolchain** (`build_latex_v13.py`,
   `apply_md_doi.py`) were deleted. Restored.
4. **DIVERGENCE DISCOVERED (pre-existing, not caused by this session).** The `.tex` files are *generated* from
   the `.md` sources, but the `.md` files are **stale by far more than this session's edits** — they lack the
   "Generalizability boundary" and "Practical reading" paragraphs from the earlier strengthening campaign as
   well as all rev-8/9 material (~120–136 content words present in `.tex`, absent in `.md`). **A rebuild would
   silently delete all of it.** Rather than half-port, the `.md` files were restored pristine and each given a
   `SUPERSEDED SOURCE — DO NOT REBUILD` banner itemising exactly what is `.tex`-only. **The `.tex` files are
   the authoritative manuscripts.**
Verification: no numeric token present before this session's edits is missing now (`.tex` diff audit, both
papers, zero losses); the four removed lines were line-continuation artifacts plus the one deliberately
replaced abstract sentence. E4's cited fit values verified against committed `results/intervention_results.json`
(`a = 0.7460941`, `γ = −0.0284398`, `gamma_negative = True`). Repo now 275 files / 17 MB.

**Rev 9 (10 Sep 2026) — consistency sweep after the rev-8 insertions.** The rev-8 paragraphs created two real
internal contradictions with text already in the papers; both are now repaired, plus two propagation gaps:
1. **E4 Discussion contradiction.** The existing boundary paragraph says "the protocol generalizes; **the
   verdicts do not**" — which the new margin paragraph appeared to violate by generalizing a verdict. Repaired
   by distinguishing two senses: general across **rules** (a theorem about *this* calibrated map — proved), vs
   general across **pools** (depends on each pool's own fitted `(a,α,β,γ)` — not claimed).
2. **E3 contradiction.** The boundary paragraph says "no transfer to the Uvalde Pool (J-27) is claimed," while
   the new §6 paragraph cites Uvalde's AC(1)=0.84. Repaired by stating that the Uvalde figure gives a mechanism
   *direction* only: no Uvalde result enters the retention verdicts and the records are not pooled.
3. **E4 abstract** Implications updated to carry the stronger negative ("defeats every non-negative pumping
   rule … not by policy"), trimmed across three passes to land at exactly **265** words (the cap).
4. **E3 Practical reading** gained a fourth manager-facing item: the AR(1)'s retention is a
   weak-autocorrelation phenomenon; a district with a more autocorrelated record should **re-score, not inherit**.
Checks: braces balanced, `\(`/`\)` matched, no `\citep{}`, abstracts **229/265**, E4 title 78, E3 title 100.

**Rev 8 (10 Sep 2026) — surviving upgrades landed in the frozen papers.** With v3 closed, the two results that
survive independently of the v3 question were written into E3/E4 (the first substantive edits to either paper
since the J-27 work began):
- **E4 §3.2** — new margin paragraph: with `a = 1+δ = 0.7461` and `γ = −0.02844` (the paper's own §2.2 fit),
  `γ<0` gives `H_{t+1} ≤ aH_t + α + βF` for *any non-negative pumping sequence*, and `0<a<1` contracts to
  `H*₀ = (α+βF)/(1−a)`; so `m = K − H*₀ > 0` defeats every non-negative rule, not just the declared family. At
  660 ft the margin is positive under all three floors (zero-pumping attractors 647.32/656.91/657.90 — verified
  against the paper's own Table). Adds that the bound is over *sequences*, hence indifferent to functional form:
  it covers multi-variable and **hysteretic** rules the declared family cannot express (gate 2's finding,
  stated generically without naming BSEACD). Converse explicitly denied: emptiness generalizes, construction
  does not. Discussion sentence sharpened to match.
- **E3 §6** — new mechanism paragraph: an AR(1) nests persistence at ρ=1, so its edge decays toward
  estimation noise as head AC(1)→1; J-17 AC(1)=0.64 leaves a slim 0.39 ft margin. Directional prediction stated;
  the second pool (AC(1)=0.84, AR(1) *loses* by 0.13 ft) is cited as **consistent direction, not a test**, and
  labelled exploratory. Conclusion: the AR(1)'s retention is a weak-autocorrelation phenomenon.
Checks: braces balanced, no `\citep{}`, abstracts 229/257 words (≤265), E4 title 78 chars. Titles, thanks-note,
and all locked framing untouched. **Corrected during drafting:** a first draft of the E4 paragraph asserted
`a = 0.9716`, which contradicted the paper's own fit (`δ = −0.2539 ⇒ a = 0.7461`); caught by checking against
§2.2 before finalizing.

**Rev 7 (10 Sep 2026) — v3 question CLOSED: no v3.** Gate 4 (springflow map-form pre-check) was run against
USGS 08155500 and **failed on four independent grounds**: (G1) period of record begins **1978-03-01**, giving
only **49** usable annual observations — the "long record" premise behind the springflow mitigation was false;
(G4) **â = 0.178, 95% CI [−0.109, 0.465] contains zero**, so annual springflow is near-white, the attractor
collapses to the unconditional mean and the lemma's dynamical content is absent (contrast head AC(1) 0.644/0.844);
(G2) **H2 unverifiable** — no machine-retrievable BSEACD pumpage series, so γ cannot be signed; (G3) the **1950s
drought-of-record**, from which the 6.5 cfs DFC and 5.2 cfs MAG derive, lies **entirely outside the gauge record**.
Per the pre-committed rule, **no v3 is written**; Barton Springs remains naive. Surviving results: gate 2's
family-free finding (E4-negative holds against a superset family with hysteresis) and the §3.2a M1-loss mechanism.
See `src/gate4_springflow_precheck.py`, `results/gate4_springflow_precheck.json`, `V3_SELECTION.md` rev 4.

**Rev 6 (10 Sep 2026)** — **gate 2 (declared-family equivalence) resolved, documents-only.** BSEACD's curtailment
family shares E4's functional shape (multiplicative piecewise-constant cuts off an authorized baseline, ρ=0
admitted; 20/30/40/50% vs E4's 20/30/35/40%) but is a strict **superset**: two trigger variables (Barton Springs
flow *Q*, Lovelady head *H_L*) and **hysteresis** (enter a stage on either indicator, exit only on both).
Consequence: **B clears unconditionally** (the lemma is family-free and subsumes multi-variable/path-dependent
rules); **C clears only under the E4-comparable subfamily restriction**. Declared triggers recovered
(Q = 38/20/14/10 cfs; H_L = 478.4/462.7/457.1/453.4 ft-msl), which raised the pre-registered multiplicity from 72
to **120 cells** (α = 0.00083). See `src/gate2_family_equivalence.py`, `results/gate2_family_equivalence.json`,
`V3_SELECTION.md` rev 3. **No Barton Springs or Lovelady statistic computed.**

**Rev 5 (10 Sep 2026)** — post-review of `deepseek e3 and e4.txt`. Added **§3.2a erratum**: the retention flip's
proximate cause is **M1's loss** (AR1 → persistence as head AC(1) → 1), not M2's gain; the earlier "more
surprising, not less" gloss read the sign backwards. C4 is unaffected (different event) and **no numbers in §3
change**. Added `src/v3_gate_checks.py` / `results/v3_gate_checks.json` (erratum verification, H1/H2 decision
table, multiplicity enumeration). `V3_SELECTION.md` rev 2 makes the v3-C verdict **conditional** on five gates,
two of which (family equivalence, springflow map-form) remain **open**. No Barton Springs statistic computed.
- **rev 1** — first exploratory record; concluded "do not promote a v3".
- **rev 2** — added §3.0 falsification conditions; §3.2 component decomposition (falsifies the mean-reversion hypothesis); §3.3 full driver ladder + inclusion criterion; §3.4 clip sensitivity; §3.7 effect size; **§3.8 J-17 matched-window and mismatched-driver controls**; **§4.0 corrected kernel table under all three floors** (rev 1 overstated); §4.1 named the attractor-to-threshold gap; **§4.5 surveyed the Uvalde physical-threshold question**; §5.0 comparability audit table; terminology standardized to pool/well; multiplicity note added. Recommendation unchanged.
- **rev 3** — added **§4.0b** (the margin rule \(m\), critical floor \(F^*\), time-to-emptiness \(T^*\)); **corrected §4.0 again** after fixing an `_pieces`/`_normalize` port defect that had falsely emptied every flat-policy kernel (rev 1 overstated emptiness; rev 2 both under- and over-stated it differently); \(T^*\) validated against E4's published 12.7 and \(F^*\) against 9/9 kernel cells; added the kernel-domain row to §5.0; added BL-5 to §6. Cross-references `GENERALIZATION_PROTOCOL.md`.

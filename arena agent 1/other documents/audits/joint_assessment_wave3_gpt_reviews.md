# Joint assessment, wave 3 — the GPT audits (P1, E1, E2, E3, E4)

Status: **COMPLETE** (verification + implementation). This report records the joint evaluation of the
three audits per paper (two Grok audits, already processed in wave 2 and implemented in the `*_v2.md`
drafts; one GPT audit per paper, new this wave) **before** implementing anything. Every GPT claim was
checked line-by-line against the current v2 drafts, which already carry the wave-2 (Grok) corrections.
The GENUINE items below are implemented in **new `*_v3.md` files**; the v2 files the user has read are
not modified (standing rule: never overwrite a version the user may have read).

Classification key: **GENUINE** = valid finding not already in v2, implement now; **GENUINE (micro)** =
same, one-clause edit; **STALE** = already fixed in v2 (usually by the Grok wave) or the draft already
contains the substance; **DISPOSED** = rejected with reason; **DEFERRED** = valid content, reserved for
the venue pass (framing upgrades, not correctness items).

---

## Paper 1 — `paper1_assessment_separation_v2.md` (Grok items A1/A2 + GPT passes 1–3)

| GPT item | Grok overlap | v2 status check | Class | Action |
|---|---|---|---|---|
| P1.1 "FP_0 misnomer" (FP_0 contains the rescue set; rename to Δ_0) | A1/1, A2/1.1 | v2 §4.6 defines FP_0 with the explicit note "This is **not** entirely a false-positive set" and Figure 1's caption: "not to be labelled 'false positive' without fixing x". The genuine gap FP_agg = I is already separated. | **STALE** | None. The draft already pre-empts the misnomer; renaming would churn notation the Grok wave settled. |
| P1.2 "Disturbance scaling contradiction" (α "scales" the dip vs proof hardcodes dip 2) | A1/7 (action-indexed assumption now stated) | v2 §4.5 convention says "α scales the depth of the worst-case dip"; the action table fixes the dip at exactly 2 (s₁ − 4t ⇒ dip 2). The word "scales" invites a free-depth reading the model does not have. | **GENUINE (micro)** | Change "scales the depth" → "triggers the worst-case dip — of fixed depth 2". |
| P1.3 HOLD prefix "timeline semantics" (does HOLD advance the stage?) | Thm 6 reworked in wave 2 | v2 Thm 6 states HOLD has constant tube {z}, successor {z}, "the final interval carries the witness"; proof (ii) says the regions are pulled back "through the (identity) holds". Backward induction is stage-indexed and finite by construction. | **STALE** | None. |
| P1.4 Boundary weights (w₁ = 0 ⇒ r → ∞) waved away as "limiting cases" | not raised by Grok | v2 proof still says "covered by the limiting cases". | **GENUINE (micro)** | Spell out both boundaries explicitly (w₁ = 0: SLOW strictly rejected on s₂ < 2, FAST licensed iff s₂ ≥ 0; w₂ = 0 symmetric). |
| P1.5 §4.9 weight discretisation (how does the integer grid validate the continuum?) | A1/14 (grid 31³, verification levels) | v2 §4.9 already says the verification set contains the critical ratios ρ₁, ρ₂ and their midpoint "for every enumerated grid state" — the exact sentence GPT asks for, in substance. | **STALE** | None. |
| P1.6 Minimax/game framing (Assessor vs Policymaker) | — | §1.2 frames quantifier noncommutation; §5.1 fixes the doctrinal reading. The game gloss is an accessibility upgrade, not a repair. | **DEFERRED** | Venue pass (SVA readers know the min–max link; one optional sentence). |
| P1.7 "Shadow Price of Commensurability" branding of r* = 1 − x | A2/1.1 region | v2 §5.5 defines r* as the minimal resource increment and turns the implication into a theorem. r* is a primal increment, not a dual price; the proposed name is a misnomer and promotional branding, which the style constraints exclude. | **DISPOSED** | None. |
| P1.8 E_end vs E_tube ESG bullet in §5.4 | A1/10 (tube/endpoint collapse) | v2 §3.1 already contains the endpoint-accounting paragraph ("the index is evaluated on audited snapshots... sees only its photograph") and the inclusion chain. | **STALE** | Optional §5.4 cross-reference deferred to venue pass. |
| P1.9 Linear-substitution scope (CES excluded) | A1/2 (doctrine disclaimer) | v2 §5.1 scopes the doctrine and the price sentence covers endogenous/state-dependent weights, but nowhere states that the scalarization is linear and nonlinear aggregators are outside the operators. | **GENUINE (micro)** | Add one clause to §5.1's closing paragraph. |
| P1.10 Prop 1 "compactness/closedness imprecise" | A1/11 | v2 Prop 1 deliberately imposes no topology and states the FIP + compactness/closedness conditions "are not needed anywhere in this paper and are stated only to delimit the mechanism"; GPT's closed-graphs version would contradict that design choice. | **STALE** | None. |
| P1.11 Orthogonal/coupled disturbance blind spot | A1/7 | v2 §4.5's action-indexed convention covers label-sharing, but the scenario of a disturbance class that simultaneously collapses **all** floors (both actions fail together, the per-weight licensing degenerates) is not declared anywhere. | **GENUINE** | Add a §5.3 bullet (conditional, datum-level statement). |
| P1.12 Exact-tube vs integrated-tube rigidity | A1/8-family scope items | v2 §5.3 bullet 3 already scopes every statement to finite-horizon exact-tube data; §3.1 defines the tube semantics. | **STALE** | None (optional contrast deferred). |
| P1.13 One-shot rescue (STAGED spends x; infinite horizon) | A1/8 (menu-relative impossibility) | v2 §6.2(iii) excludes infinite horizons; §5.5 states R needs no augmentation; §5.3 keeps the impossibility menu-relative. The draft nowhere claims R is permanently safe. | **STALE** | None. |
| P1.14 Exogeneity of weights (constant w over [0,1]) | A1/2 | v2 §5.1: "actual prices may be strictly positive, endogenous, dynamically determined, state-dependent... the theorems require none of those properties." | **STALE** | None (folded into P1.9's clause wording). |
| P1.15 Convexification of the menu (mixed strategies could collapse the gap) | — | v2 §2.7 declares "policy classes larger than the menu" unused; §5.3's impossibility bullet is menu-relative, but the convexification/time-sharing stress-test is not named. | **GENUINE** | Add a §5.3 bullet. |
| P1.16 Information-asymmetry reading of quantifier order | — | §5.1 gives the doctrinal reading; the information-set gloss is an interpretation upgrade. | **DEFERRED** | Venue pass. |
| P1.17 "Temporal Reconvergence" naming for Thm 6(iii) | Thm 6 (iii) kept in wave 2 | The mechanism is already stated ("a later stage can erase the gap"); a branded name is unnecessary. | **DISPOSED** | None. |

Implementation (P1): §4.5 wording (P1.2), §4.6 boundary weights (P1.4), §5.1 linearity clause
(P1.9/P1.14), two §5.3 bullets (P1.11, P1.15) — plus two verification catches (see Section 6): the
leftover $C$-vs-$W_+$ weight-cone collision in §1.2 and §5.1, and a label-sharing disambiguation of the
§4.5 convention sentence.

---

## E1 — `paperE1_cod_forecast_ladder_v2.md` (Grok items + GPT passes 1–3)

| GPT item | Grok overlap | v2 status check | Class | Action |
|---|---|---|---|---|
| E1.1 Information asymmetry persist vs M4 | Grok "M4 lacks delayed-persist control" | v2 §4 frames M4's gap as "the information cost of the one-year delay" and registers the separating control (persistence issued from S_{t−1}). | **STALE** | None. |
| E1.2 Allee term deformation (s → 0 changes the curve globally; cubic ≠ Schaefer) | — | v2 §2.2 **already** contains exactly this: "setting s = 0 gives a(S_t) = S_t/K (a cubic modification of the logistic surplus), not the Schaefer law". | **STALE** | None. |
| E1.3 Catch endogeneity (1992 drop is an endogenous response; exogenous C forces the rebound) | — | v2 §3.1 has the conditional test ("If the crash were a catch-regime event... M2 would improve") but not the endogeneity reading. | **GENUINE (micro)** | One clause in §3.1's M2 sentence. |
| E1.4 Certificate scope ("autonomous, time-invariant" narrowing) | Grok "Certificate scope" | v2 abstract already scopes to "the scored one-step least-squares Schaefer/Allee ladder on these two unpooled series"; the ladder is autonomous/time-invariant by construction. | **STALE** | None. |
| E1.5 DOF starvation (r, K, b on 8 training years) | — | v2 §3.4 describes the module and origins but does not state the overfitting risk. | **GENUINE (micro)** | One sentence in §3.4. |
| E1.6 ±17 kt solver instability belongs in Discussion | Grok data-avail/29-of-29 fixes | v2 Data availability documents the ±17 kt variance and cross-links it to the declared identification fragility, which §4/§3.3 discuss. | **STALE** | None (optional summary deferred). |
| E1.7 Epistemological loop (predictand is a smoother; persistence inherits its autocorrelation) | — | v2 §4 **already** contains this caveat nearly verbatim: "The predictand is an assessment smoother (NCAM/xteNCAM SSB), not a raw observation... persistence inherits the smoother's autocorrelation". | **STALE** | None. |
| E1.8 Cost-function mismatch (one-step LS training vs h = 5 scoring) | — | v2 names the estimator in the certificate scope but nowhere states the training/testing mismatch. | **GENUINE (micro)** | One disclosure sentence in §2.3. |
| E1.9 RMSE blindness; elevate sign-hit rate | — | v2 reports Direction in Table 3 but §4 does not interpret it. | **GENUINE (micro)** | One clause in §4's first paragraph (values 0.00–0.50 verified against Table 3). |
| E1.10 h = 5 persistence is biologically absurd (generational stasis) | — | v2 §4 defends the persistence comparison on statistical grounds; the demographic point is absent. | **DEFERRED** | Venue pass (interpretive, not a correctness item). |
| E1.11 M1's failure is an a priori algebraic inevitability | — | v2 §4 opens with the obstruction framing ("An exact fixed autonomous scalar trajectory cannot reproduce it"); the paper does not present the failure as a surprise empirical discovery. | **STALE** | Optional intro sentence deferred. |
| E1.12 Markov violation / ghost momentum (SSB is a 1D projection of age structure) | — | v2 §4: "One-dimensional surplus production is not NCAM: age structure, migration, and survey catchability are omitted." | **STALE** | None. |
| E1.13 Ergodic fallacy in rolling-origin CV across the singularity | — | v2 §4: "Autoregressive residuals fitted on short, regime-changing windows persist the wrong sign" + the rolling-origin redesign disclosures. | **STALE** | None. |
| E1.14 s → 0 is topographically forced by the stock's survival | — | v2 says "unidentified Allee parameter, not a biological threshold" but not the mechanism. | **GENUINE (micro)** | One clause in §3.1's M1b sentence (any s above the training minimum makes a(S) negative on part of the window). |
| E1.15 "Martingale advantage" naming | — | §4 has the smoother-autocorrelation explanation; the martingale gloss is optional vocabulary. | **DEFERRED** | Venue pass. |

Implementation (E1): five edits — §3.1 M2 endogeneity clause (E1.3), §3.1 M1b mechanism clause (E1.14),
§3.4 DOF sentence (E1.5), §2.3 cost-function disclosure (E1.8), §4 sign-hit clause (E1.9).

---

## E2 — `paperE2_cod_intervention_v2.md` (Grok items + GPT passes 1–2)

| GPT item | Grok overlap | v2 status check | Class | Action |
|---|---|---|---|---|
| E2.1 Growth-vs-control clash (contracting closed loop is antagonistic to surplus production) | — | v2 §4 states it: the certified-layer machinery assumes a contracting loop; "This cod object is the first scored instance in which the contraction form is provably inapplicable"; growth is steepest where the stock is scarcest. | **STALE** | None. |
| E2.2 Perpetual shock > g_max makes emptiness a scale proof, not a governance failure | Grok "harsh-class tautology" | v2 §3.1/§4 have the critical-floor axis ē = g_max = 296 kt yr⁻¹ separating vacuous from informative classes, and §4 calls the harsh-class emptiness vacuous as a productivity statement. | **STALE** | None. |
| E2.3 Reactive-rule penalty (clause (a) biases against any rule that harvests at the boundary) | — | v2 §3.2 states the mechanics for S1/cascade ("their 60-kt cap removes catch exactly where the moratorium already sits at 5 kt") and §4 keeps the verdict system-dependent. The generalization is not needed and risks over-claiming. | **STALE** | None. |
| E2.4 K bound dictates the theorem (F′ > 1 contingent on K = 5000 pinned) | Grok "K pinned" disclosure | v2 §2/§4 declare "K is pinned at its optimization bound" but do not connect it to the expansive classification. Arithmetic check: F′(K*) = 1 + r(1 − 2K*/K) > 1 iff K > 2·884.6 = 1769.2 kt — GPT is right. | **GENUINE (micro)** | One sentence in §4. |
| E2.5 57.6 kt topography unexplained | — | v2 §3.3 **displays** the decomposition: g(K*) − |e_q10| = 172.47 − 114.85 = 57.62 kt yr⁻¹. | **STALE** | None. |
| E2.6 Replay starts outside the safe set | Grok "1990 replay starts outside the safe set" | v2 §3.5 labels the replay "uncontrolled shock accounting rather than a kernel-membership test". | **STALE** | None. |
| E2.7 Falsified-plant paradox | Grok companion-import fixes | v2 §1/§4 scope the object as the companion study's fitted model scored as a closed-loop governance object; §4 declares the certified layer vacuous at observed stock levels. The draft's scoping is more honest than a retreat to "synthetic object". | **STALE** | None. |
| E2.8 Additive shock compounded geometrically | Grok harsh-class/persistent-floor wording | v2 declares the classes as persistent additive floors; for a persistent annual input to the expansive map the geometric sum is the correct worst case, so the formula matches the declared class. §4 states the floors are "deliberately harsh (a perpetual floor, not an independent draw)". | **STALE** | None. |
| E2.9 Omniscience fallacy (no observation/assessment lag in the control loop) | — | v2 does not declare the perfect-observation assumption anywhere; the companion study's M4 module models exactly this lag. | **GENUINE (micro)** | One sentence in §4 (kernels are perfect-observation upper bounds). |
| E2.10 Half-space absurdity (kernel extends to 10⁴ > K) | Grok "safe-set edge 10^4" | v2 §4: the upper edge "is never approached and exists only so that kernels can be written [s, ∞); the positive-part floor never binds". | **STALE** | None. |

Implementation (E2): two edits — §4 K-bound contingency (E2.4), §4 observation-lag declaration (E2.9).

---

## E3 — `paperE3_edwards_forecast_ladder_v2.md` (Grok items + GPT passes 1–2)

| GPT item | Grok overlap | v2 status check | Class | Action |
|---|---|---|---|---|
| E3.1 Oracle paradox (structural vs informational certificate) | — | v2 abstract gives the oracle rent (7.55 vs 13.23 ft) and §6 states the timing-bound reading: "the same structure that cannot forecast next year certifies this year". | **STALE** | None. |
| E3.2 γ = +0.021 as simultaneity bias, not merely a short window | — | v2 §5.2 says "pumping rose as the drought deepened, so the short window cannot identify a supply response" — the mechanism is gestured at but the aliasing is not named. | **GENUINE (micro)** | Reword the §5.2 sentence (behavioral coupling, coefficient aliasing). |
| E3.3 Bounded-oscillator caveat for the h = 5 climatology win | — | v2 scopes to "this basin" but does not say why mean reversion works here and not in fossil aquifers. | **GENUINE (micro)** | One sentence in §6. |
| E3.4 Low-pass filter of the annual mean vs 10-day triggers | — | v2 §2: "a coarse proxy for the Authority's 10-day declaration, not the declaration itself"; §5.3 repeats it. | **STALE** | None (optional framing deferred). |
| E3.5 Constant specific yield (topological mis-specification) | Grok "water-balance label" fix | v2 §6: "The annual affine one-pool specification is not a karst model: conduits... remain in the residual". The specific-yield instance is one member of that family. | **STALE** | None. |
| E3.6 Weather vs climate (why ENSO fails) | — | v2 §5.4: "autoregression on nearly white recharge is not a recharge forecast"; "La Niña (−0.92) does not announce R₁₉₅₇ = 1143"; "misses 1957-scale extremes". | **STALE** | None. |
| E3.7 Confined/artesian pressure-vs-mass category error | — | v2 §6 lists what remains in the residual but not the confined-zone pressure response. | **GENUINE (micro)** | Add the item to the residual list (one clause). |
| E3.8 AR(1) = exact solution of spring drainage (φ = e^{−k}) | — | v2 reports φ̂ = 0.66 but classifies M1 as output-only with no drainage reading. Darcy drainage toward the spring level gives an affine AR(1), so the reading is physically coherent and worth stating as interpretation. | **GENUINE (micro)** | One interpretive sentence in §6 (module stays output-only in the protocol sense). |
| E3.9 M4 one-year delay is fictional for a telemetered gauge | — | v2 §6 only says "M4 is a one-year information delay, not a conservative filter" — no justification for the module's presence. | **GENUINE (micro)** | Extend that sentence (ladder symmetry; prices a theoretical lag). |
| E3.10 Persistence win = dynamic equilibrium, not inertia | — | v2 §5.3/§6 interpret the persistence results at length (recharge events, mean reversion). | **DEFERRED** | Venue pass (optional gloss). |

Implementation (E3): five edits — §5.2 simultaneity (E3.2), §6 bounded-oscillator sentence (E3.3),
§6 residual-list clause (E3.7), §6 AR(1) drainage sentence (E3.8), §6 M4 justification (E3.9).

---

## E4 — `paperE4_edwards_intervention_v2.md` (Grok items + GPT passes 1–2)

| GPT item | Grok overlap | v2 status check | Class | Action |
|---|---|---|---|---|
| E4.1 Lucas-critique violation in counterfactual governance | — | v2 nowhere acknowledges the 1934–1990 fit → regulated-rules swap as a behavioral-stability assumption. | **GENUINE** | One §4 sentence + Lucas (1976) reference. |
| E4.2 660-ft certificate is a category error (CPM surrenders 660 by design) | Grok "every policy ≡ BAU" split | v2 §3.2/§4 **already** carry the design-property reading: the certificate "is exactly the frequency-management rationale the actual CPM rule implements"; "the rule cannot make wet years, it prices dry ones". | **STALE** | None. |
| E4.3 OOS defect paradox (21.81 breaches the 15.41 training defect) | — | v2 §2.1 records the breach; §4 states the certified emptiness with the breach cited, but does not draw the consequence that the true certified horizon is narrower still. | **GENUINE (micro)** | One clause in §4. |
| E4.4 8.1-ft bias vs 10-ft trigger resolution inflates supply | — | v2 §3.5 discloses the bias and §4 repeats it; supply is scored on the **actual-head** replay, so the model bias cannot inflate the supply column — GPT's specific claim does not apply. The bias does shrink the open-loop diagnostic's margins, which v2 already states. | **DISPOSED** | None. |
| E4.5 Degeneracy of the viability formalism (deterministic policies ⇒ fixed-point analysis) | E2's Aubin-scope fix (not yet mirrored in E4) | v2 §2.3 computes kernels by iterating the worst-case closed loop and §3.2 reasons in attractor terms, but the closed-loop-vs-Aubin scoping sentence that E2 carries is absent from E4, and E4's references lack Aubin (1991). | **GENUINE** | One §2.3 scoping sentence (folding the degeneracy point) + Aubin (1991) reference. |
| E4.6 Phantom water (affine intercept props up the flat-0 attractor at 647.32) | — | The flat-0/UC-min equilibrium implies model spring discharge ≈ 164 kaf yr⁻¹ at 647 ft, which is within the plausible range for Comal + San Marcos at that head; the "must empty" claim is not established. v2 already labels the floors and attractors "certification geometry, not forecasts". | **DISPOSED** | None. |
| E4.7 T ≈ 13 emptiness is an artifact of the 710-ft ceiling | Grok "domain-top" fix | v2 §3.2: "the emptiness is a domain-top event: the boundary reaches the declared safe-set ceiling (710 ft)... rather than an attractor event". | **STALE** | None. |
| E4.8 Open-loop erosion formula ignores feedback dampening | — | v2 §2.4 applies the uniform conversion (autonomous rate a = 0.7461) to every policy and nowhere states the asymmetry for state-dependent rules. | **GENUINE (micro)** | One §4 sentence (the certified comparison is conservative against reactive rules). |
| E4.9 Transmissivity/flat-cut contrast in the conclusions | — | v2 §4 states the reactive result "is system-dependent, not architectural" with the cod mirror; the specific transmissivity mechanism is optional. | **DEFERRED** | Venue pass. |

Implementation (E4): four edits + two references — §2.3 closed-loop scoping (E4.5), §4 OOS-horizon clause
(E4.3), §4 feedback-conservatism sentence (E4.8), §4 Lucas sentence (E4.1); references Aubin (1991),
Lucas (1976).

---

## Cross-cutting decisions

1. **Implementation target.** All GENUINE edits are applied to new `*_v3.md` copies of the five papers;
   the v2 files remain untouched (standing rule: never overwrite a version the user may have read).
   P2, P4, P5 receive no GPT audit this wave and are not copied.
2. **Stale-vs-implement discipline.** GPT items whose substance already exists in v2 are not re-edited;
   where the v2 wording differs from GPT's preferred phrasing, the v2 wording stands unless it is wrong.
3. **Numeric deltas introduced deliberately:** E2 adds 1769.2 (= 2 × 884.6, the K < 2·LRP contraction
   threshold); E3 re-quotes 0.66 and adds 0.34 (= 1 − 0.66, the drainage-decay coefficient). All other
   significant-number multiset changes are expected to be empty (checked with the numdiff harness).
4. **Deferred list (venue pass) grows by:** P1 minimax framing, P1 information-asymmetry reading,
   P1 §5.4 ESG cross-reference, P1 integrated-tube contrast; E1 martingale naming, E1 h=5 demographic
   realism, E1 intro null-space sentence, E1 ±17 kt Discussion summary; E3 low-pass-filter framing,
   E3 persistence-as-equilibrium gloss; E4 transmissivity mechanism in the conclusions.
5. **Disposed with reasons:** P1 "Shadow Price of Commensurability" (misnomer + branding), P1 "Temporal
   Reconvergence" (mechanism already stated), E4 phantom-water mechanism (arithmetic unsupported;
   attractors already labelled certification geometry), E4 supply-inflation claim (supply uses actual
   heads, not model heads).
6. **Verification catches (found during the joint check, from neither audit):** P1 §1.2 and §5.1 still
   named the weight cone $C$, although §2.2 declares the cone is $W$ / $W_+$ and reserves $C$ for the
   command architecture (a leftover of the wave-2 rename) — fixed in v3. The §4.5 disturbance-convention
   sentence's "shared disturbance hitting both coordinates" phrasing was disambiguated to "disturbance
   label shared across the two actions" so it cannot be misread against the new coupled-shock bullet.

---

## Implementation record (all applied to the new `*_v3.md` files)

| Paper | Edits | Contents |
|---|---|---|
| P1 | 9 | §1.2 cone name ($C$→$W_+$); §4.5 "scales"→"triggers, fixed depth 2"; §4.5 label-sharing disambiguation; §4.6 explicit boundary weights; §5.1 cone name + linearity/CES scope clause; two §5.3 bullets (coupled all-floor shocks; convex hull of the menu) |
| E1 | 5 | §2.3 one-step-LS vs h=5 cost-function mismatch disclosure; §3.1 catch-endogeneity clause; §3.1 M1b topographic-identification clause; §3.4 degrees-of-freedom starvation sentence; §4 sign-hit (0.00–0.50) directional clause |
| E2 | 2 | §4 expansion classification contingent on the pinned $K$ ($F'(K^*)>1$ iff $K>2K^*=1769.2$ kt); §4 perfect-observation declaration (assessment-lag kernels would be smaller or empty) |
| E3 | 5 | §5.2 simultaneity-bias reword of the γ = +0.021 sentence; §6 bounded-oscillator scope of the h=5 climatology win; §6 AR(1) spring-drainage reading ($\hat k\approx0.34$ yr⁻¹); §6 M4 telemetered-gauge justification; §6 confined-zone pressure response added to the residual list |
| E4 | 6 | §2.3 closed-loop-vs-Aubin scoping sentence (folds the degeneracy point); §4 out-of-sample-defect ⇒ narrower certified horizon clause; §4 uniform-erosion conservatism against feedback rules; §4 Lucas-critique boundary; references Aubin (1991) and Lucas (1976) added |

Numeric-fidelity check (numdiff v2→v3): P1 and E4 multisets identical; E1 +0.00/+0.50 (sign-hit range),
E2 +1769.2 (2×884.6), E3 +0.34/+0.66 (drainage coefficient and its re-quote) — all deliberate, nothing
else moved. Math-delimiter balance even in all five v3 files. No abstract, table, or figure content
changed; abstract word counts and structure are untouched.

---

## Remaining-points sweep (post-implementation review, same wave)

A sweep of every open item from waves 2–3 (Grok deferred list + GPT DEFERRED list + registered
revision requirements). Disposition:

**Implemented now (7 text-level items → new `*_v4.md` files for P1, E1, E2, E4; E3 unchanged):**
1. P1 §1.2 — minimax reading of the quantifier noncommutation (the binary payoff "a is admissible at
   z under w"; the witness exhibits the interchange failing strictly).
2. P1 §5.1 — information reading (∃a∀w = commitment before the weight is known; ∀w∃a_w = action chosen
   after; the gap measures the value of weight information).
3. P1 §5.4 — Fourth implication: endpoint-only reporting regimes evaluate the weakest operator of the
   §3.1 chain and cannot detect mid-interval typed violations; kept conditional ("asserts nothing
   empirical about any particular reporting regime").
4. E1 §1 — the a priori structural bar front-loaded (1D autonomous maps in the monotone regime cannot
   reproduce a crash-then-recover path; the test measures the penalty, not the bar's existence).
5. E1 §4 — the h = 5 persistence baseline's demographic reading declared not-asserted (perfect
   compensation over a generation); retention is a scoring benchmark, not a biological projection.
6. E2 §4 — the retention rule's protective clause is structurally conservative toward the moratorium
   (CORRECTED form of GPT's generalization: sub-boundary cuts cannot compensate on a threshold
   constraint because a violation is already fatal — GPT's "any rule permitting harvest above the LRP"
   version was over-broad).
7. E4 §4 — the mechanism of the reactive advantage named (transmissivity + rapid recharge; the supply
   margin exists only in wet years, per §3.4).

**Dropped with reasons:** E1 "Martingale Advantage" naming (jargon from a different field; the smoother
autocorrelation explanation already does the work); E1 ±17-kt §4 summary (already cross-linked in the
data statement and §4); E3 low-pass-filter and persistence-as-equilibrium glosses (already covered by
the proxy statements and §6); P1 integrated-tube contrast (covered by §5.3 exact-tube scope bullet);
P1 §2→supplement relocation (declined under the no-condensation directive; §2 stays with the
instantiation table).

**Recommended as dedicated passes (new mathematics/analysis — not safe for a text sweep):**
- P1: two-stage erasure witness for Theorem 6(iii) (makes "a later stage can erase the gap" concrete)
  and BLEND_δ (a blended action would answer the new §5.3 convexification bullet directly);
  x-in-aggregate variant (re-derived thresholds) — lower priority.
- P4: exact-hold monodromy (the standout: genuine novel mathematics for the delay paper), then
  stochastic/regime-shift disturbance classes and the complete crossing enumeration.
- P2: predecessor/fixed-point architecture and monotonicity Theorems F/G — structural, belongs to the
  P2 venue pass.
- P5: factorial operator comparison and cross-spectral gain–phase targets.
- E-papers: the registered recomputation campaigns (E1: Spec-B baselines on twelve-year origins, Table
  8 baselines, M4 separating control, Table 3 persistence rows, M1/M1b reconciliation; E2: one-row
  depensation sensitivity; E4: Stage II–IV occupancy figures). Feasibility confirmed: the repo clone
  carries both studies' data + src scripts and the reaudit rerun campaigns
  (reaudit/intervention_rerun*, postv10_rerun). This is the highest-value open work — it converts
  declared mismatches into verified numbers — and should be run as its own verified-rerun pass with
  byte-level reconciliation before any table changes.
- P3: canonical-file decision still pending the user's call.

Checks: numdiff v3→v4 identical significant-number multisets for all four edited papers; math-delimiter
counts even; no table, figure, or abstract content touched.

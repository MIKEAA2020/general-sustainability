# Batch 8 — Paper 1 Queue Cross-Check Against the Latest Versions of the Other Papers

**Date:** 2026-09-21. **Basis:** repo commit `8343206` (Task 105's sigma-spectrum wave, pushed this round). **Task:** the owner's directive — *check paper1 v52, `BATCH8_PAPER1_ECOLOGICAL_INDICATORS_JOINT_ASSESSMENT.md`, `QUEUE_REVERIFICATION_AND_PLAN.md`, and the findings from the previous two turns against the latest versions of the other papers in the repo: `arena agent 1/paper rewrites/latex` and `agent 2 productivity illusion/manuscript_ECOMOD_v35.tex`.*

**Standing rules honored.** No existing repository file was modified in this round; this report is the round's only creation besides the worklog appends. Nothing from the audit, the manuscripts, or the previous rounds' deliverables is removed or condensed. All findings below are **additive**: they annotate, reinforce, or owner-gate — they do not retract any of the 42 consolidated points or any Task-104/105 adjudication.

---

## 1. The checked set (latest versions, verified this round)

| Paper | Latest version checked | Lines | Role for this check |
|---|---|---|---|
| Paper 1 (the audited manuscript) | `latex/paper1_assessment_separation_v52.tex` | 1,817 | The baseline; unchanged since Tasks 104/105 (still current) |
| Paper 2 (obstruction calculus, Automatica routes) | `latex/paper2_obstruction_calculus_v43_Automatica_routes.tex` + `…_supplementary.tex` | 1,783 + 841 | The family's viability/quantifier paper |
| SafeTransition EMS (software description) | `latex/paper1_safetransition_ems_v8.tex` (+ `paper1_safetransition_ems_supplementary_v7.md`, S1–S11) | 1,056 + 457 | P1's software companion; shares the witness datum |
| SafeTransition master | `latex/paper1_safetransition_master_v2.tex` | 1,056 | Verified a **formatting variant only** of EMS v8 (58 diff lines, all preamble/frontmatter: elsarticle→article, venue-neutral title block); same body — no separate findings |
| Productivity illusion (composition illusion) | `agent 2 productivity illusion/manuscript_ECOMOD_v35.tex` | 774 | The two-land biocapacity paper; the family's other composite-index paper |

Method: targeted line-level verification (grep with line evidence, then full reading of every hit passage), the same discipline as Tasks 104/105. Every quote below was located in the named file at the named line.

---

## 2. Findings that change or enrich the queue

### 2.1 Queue 3.A-7 (positioning: Becker et al. 2017) — the entry already exists in the family, in ECOMOD v35

ECOMOD v35 cites **Becker et al. (2017)** in text — "reporting only the total can therefore send a misleading policy signal (Becker et al., 2017; Fischer et al., 2022)" (line 65) — with the full entry: *Becker, W., Saisana, M., Paruolo, P. & Vandecasteele, I. (2017). Weights and importance in composite indicators: Closing the gap. **Ecological Indicators**, 80, 12–22* (line 698). The planned P1 use is **orthogonal and consistent**: ECOMOD uses Becker for weights-as-trade-offs (with Nardo et al., 2008, line 732, the OECD handbook); P1's point is that *even if weights perfectly reflect importance, the quantifier order can still produce the gap*. No conflict; the exact entry is importable into P1's reference list verbatim; and the orthogonality sentence P1 plans to add is *reinforced* by the family split of labour (ECOMOD owns the weights side, P1 the quantifier side). Optional (owner-gated): the same ECOMOD cluster carries **Nardo et al. (2008)** and **Fischer et al. (2022)** (line 711), either importable if the owner wants the positioning paragraph to cover the full composite-indicator methodology cluster.

### 2.2 Queue 3.A-13 (in-text citations for uncited entries) — De Lara & Doyen (2008) has a direct family precedent in P2 v43

P2 v43 cites **De Lara and Doyen (2008)** in text as the viability anchor — "(Béné, Doyen, and Gabay, 2001; De Lara and Doyen, 2008; Doyen et al., 2012; Doyen and Gajardo, 2020)" (lines 87–88) — with the full entry: *De Lara, M., Doyen, L.: Sustainable Management of Natural Resources: Mathematical Models and Methods. Springer, Berlin (2008)* (line 1703). This is both (i) the precedent for P1's planned in-text use at the §5.2 viability positioning, and (ii) an importable entry. P2 also carries the **ecosystem-based fisheries management** entry the P1 positioning cluster wants to lean on: *Doyen, L., Thébaud, O., Béné, C., Martinet, V., Gourguet, S., Bertignac, M., Fifas, S., Blanchard, F.: A stochastic viability approach to ecosystem-based fisheries management. Ecol. Econ. **75**, 32–42 (2012)* (lines 1709–1711). **Rockström et al. (2009) and Raworth (2012)** have no family precedent (zero hits across all five files; the only Rockström in the set is as co-author of Donges et al. 2017 in ECOMOD, line 707) — P1's planned in-text uses at the safe-operating-space/critical-natural-capital statements stand alone, as planned.

### 2.3 Queue 3.A-12 (Filippov & Warga entries) — no family precedent; proceed as planned

Zero hits for Filippov or Warga in any of the five files. P1 adds the entries from the primary literature; nothing to import, nothing to conflict.

### 2.4 Queue 3.A-9 (reserve-stock institutional forms) — partially pre-implemented in the EMS companion

EMS v8 already realizes the fund/buy-back institutional mapping on the same datum: "a pulse-plus-closed-season quota plan, a mid-season heatwave strike, and a staged rebuild **financed by a fund buy-back**" (line 497–498); "the rescue threshold κ\* = 1 − x on the non-typed-viable region, **truncated at zero (κ\* = max(0, 1−x)) once the fund covers the buy-back**, with shortfall 1/2 at the false-positive witness and full financing at the rescue witness x = 3/2" (lines 519–521); the plan-menu figure: "FAST (pulse 1463/125 plus closed season), SLOW/NO-SWITCH (sustained yield 1088/125), and **STAGED (quota σ − 1/2, rebuild to 69/20), with the fund schedule x(t) under STAGED**" (lines 577–579); "buy-back with 1/2 remaining" (line 649). Consequences for the queue point: (i) P1's v53 institutional paragraph should **align its terminology and quantities with the EMS realization** (fund level x, buy-back financing, the κ\*-truncation-at-zero rule) rather than invent a parallel vocabulary; (ii) it can point to the EMS companion as the software-side realization (owner-gated citation); (iii) the licence-buy-back / transition-assistance / quota-banking *mapping beyond the fund* remains P1-additive — no other family paper covers it.

### 2.5 Queue 3.A-2 (evaluation-semantics table) — the five operators are a family-shared structure; the table must match EMS's presentation

EMS v8 presents the **same five operators, "following Abaee 2026a"** (= P1): "the noncompensatory typed operator… the scalarized aggregate operator… the exact-tube physical operator… the endpoint-only physical operator… and the typed-endpoint operator," with the same inclusion chain `E_typ ⊆ E_w ⊆ E_tube,phys ⊆ E_end` (lines 179–200), and its Table `tab:verdicts`; EMS supplementary S1 is "The five assessment operators, as implemented." P1's planned compact table (floors × tube/endpoint) therefore formalizes a structure the family already shares — the operator **names must match EMS's** (they do in v52's prose; the table should keep them). ECOMOD independently states the same semantics in its own setting: "Under **exact-tube semantics** (a transition is safe only if every state along it, not merely the endpoint, satisfies the constraints), the intermediate passage where A_c falls is itself a violation even if the endpoint recovers" (line 439). Consistent family doctrine; no conflict; the table gains a family anchor.

### 2.6 Queue 3.C-29 (natural body uses for MSY/PROMETHEE) — MSY has a family precedent; PROMETHEE stands alone

ECOMOD v35 uses MSY naturally, twice: "the classical surplus-production/MSY curve rest on May (1973) and Schaefer (1954)" (line 73) and "Its equations, MSY/fold, equilibrium family P = B(A)/e…" (line 478). P1's planned use at the §6.3 sustained-yield quota discussion is the same Schaefer/MSY world — consistent. PROMETHEE has zero family hits; P1's planned use at the §5.2 Cinelli/Schär compensability sentence remains P1-local. No conflicts either way.

### 2.7 The cod datum is family-shared, and the kt-convention adjudication is reinforced family-wide (Queues 3.A-14, 3.B-23; Task-104 §1.3a)

EMS v8 deposits the **same benchmark datum with the same kt convention**: "stock biomass with Schaefer surplus σ(B) = rB(1 − B/K) (r = 4, K = 10, B_lim = 2)" (lines 496–497); the enclosure "on the adverse recovery leg biomass lies in [6/5, 16/5] ⊂ (0, K/2)" with "σ(6/5) = 528/125 = 4.224" (lines 510–512); "the sustained-yield alternative at σ(16/5) = 1088/125" (line 567); the licensing thresholds ρ₁ = 2/3, ρ₂ = 3/2 cross-checked against the tube geometry (lines 515–517); the index blindness at w = (1,1) (min 2/5 vs floor −4/5) (lines 513–514). All of this is deposited in the EMS 24-check suite (Table `tab:qa`, 24/24 pass). **Consequence:** the Task-104 adjudication — P1's kt-margin convention is internally consistent and qwen's normalized-biomass rewrite is defective — now holds *family-wide*: the EMS companion's deposited exact values (16/5, 6/5 in kt) are additional evidence that the kt chain is the family's convention. Queue point 3.B-23's explicitness sentence (b(0) = B(0)/B_lim = 8/5 = 1.6) is consistent with EMS usage and safe to implement as planned. One typesetting note: EMS writes `B_{\mathrm{lim}}`, P1 v52 writes `B_lim` — same quantity, same value; worth aligning only if the owner wishes (cosmetic; owner-gated).

### 2.8 Queues 3.A-14 / 3.B-24 (exact DFO values; critical-zone precision) — P1-only material; no cross-paper counterpart, and no collision with ECOMOD's "critical slowing down"

The DFO/LRP/884.6-kt/mid-1980s/2015-one-third material has **zero hits** in EMS, ECOMOD, and P2: the historical anchoring layer is P1's alone (EMS carries the Schaefer realization without the DFO history; ECOMOD's fishery content is recovery-timescale fitting on RAM Legacy B/BMSY, line 538 — a different object). The motivation paragraph and the critical-zone precision sentence therefore have nothing to import and nothing to conflict with. Terminology check: ECOMOD's "**critical slowing down**" (CSD; its no-CSD negative result, lines 77, 268, 324, 353) is a *different concept* from P1's "**critical zone**" (the LRP-based zone) — the phrases do not collide, but a family reader should not conflate them; noted here so the v53 critical-zone sentence need not worry about ECOMOD's usage.

### 2.9 Queue 3.A-6 / 3.E-42 (three-regime disturbance sensitivity; the middle cell) — no family pre-computation; the exact task stays P1's

No family paper contains a common-shock analysis of the P1 witness datum: zero hits for common/coupled shock in EMS and ECOMOD; P1 §5.5's coupled-shock delimitation (with Lade et al. 2020) remains the only family statement; ECOMOD's declared disturbance classes are a different axis ("persistent productivity, b_f or ρ_c shocks", line 429); P2's disturbances live in its hidden-regime systems. The middle-regime cell (common biomass shock) therefore remains **P1's own small exact-arithmetic task** exactly as the queue plan (Part E) records — nothing in the family pre-answers or pre-computes it, and nothing conflicts with computing it.

### 2.10 Queue 3.A-10 (conservatism caveats) — a stylistic precedent for the depensation caveat in ECOMOD

ECOMOD explicitly discloses its Allee-free scope: "the consequences of the deliberately minimal, **Allee-free** choices are discussed in § Model scope and § Limitations" (line 77) and the scope table row "Allee-type rescue threshold & No & …" (line 464). P1's planned depensation caveat (the certified tubes' conservatism invalidated under depensational stock-recruitment) is the same disclosure genre — the family already treats "state the absent biology explicitly" as the house style. The heatwave convention is shared with EMS (the mid-season heatwave strike, line 498), which does not model amplification either — P1's heatwave-amplification caveat is additive family-new content, as planned.

### 2.11 Queue 3.A-11 (dashboard-only-architecture disclaimer) — the EMS companion is the software-side realization of the same architecture

EMS v8's "Dashboard readings" section (line 555 onward) implements the dashboard the P1 benchmark assumes, including "the **index-blindness alarm**, which fires exactly when the composite minimum stays nonnegative … while a floor minimum is negative" (lines 592–595). P1's planned disclaimer ("a deliberately adverse reporting architecture, not a claim about current fisheries assessment practice") is the manuscript-side statement of the same deliberately-adverse architecture; the two are consistent by construction. The disclaimer may point to the EMS companion as the realization (owner-gated).

---

## 3. σ-spectrum cross-paper findings (Queue 3.A-8; the Task-105 wave)

### 3.1 No pre-emption — the wave's results are family-new

None of the other papers contains CES/power-mean/geometric-mean aggregation theory: EMS's operators are P1's five (linear scalarized and typed); P2's substitution content is linear-algebraic (Farkas/Gale pathways); ECOMOD's aggregate B = b_f·A_f + [b_c + b_{G,c}G_c(q)]·A_c is exactly the **linear member** plus an identifiability analysis. The wave's master equation, the critical-floor ladder {1, 5/4, √2, φ, √3, …} → 2, the σ\*(z) landscape, and Theorems S1/S2 have no family counterpart. All Task-105 results stand.

### 3.2 ECOMOD's composition illusion is the continuous-time instance of the compensatory-aggregation gap — mutual reinforcement

ECOMOD v35 states: "**The illusion is an instance of the compensatory-aggregation gap.** … The weighted composite B is the weak-sustainability index: it satisfies its aggregate floor while the **typed floor** on ecological capital A_c is violated. … The aggregate that an index reads is a weighted sum over several typed floors, so a deficit in one (the capital book) can be masked by a surplus in another (the yield), and **a transition can satisfy the aggregate all the way along while it never satisfies the individual floors**" (line 437, citing the companion compensatory-aggregation work as "Abaee, 2026b"). This is precisely P1's Protocol-2-vs-typed separation instantiated in a continuous-time two-land model — i.e., ECOMOD's B is the θ=1 (σ=∞) member of the wave's family acting on land books, and ECOMOD's typed floor is the σ=0 side. The wave's Theorem S2(ii) — *only σ = 0 is uniformly safe on the gap region; V⁰ = V_typ* — is the aggregator-side theorem behind ECOMOD's instance. **No conflict; a natural two-way cross-citation** (owner-gated): the P1 σ-subsection can cite ECOMOD's composition-illusion instance as the continuous-time companion, and a future ECOMOD version can cite the σ-spectrum as the exact elasticity analysis of its linear member.

### 3.3 ECOMOD's identifiability limit and P1's certification gap are complementary (inverse vs forward problem)

ECOMOD's "minimal formal anchor": "Aggregate biocapacity B is a scalar projection of a vector of land-type components … A scalar time series therefore cannot, without additional independent restrictions, recover the vector that produced it" (line 517; developed at 499–516 with the Nardo et al. 2008 conventions anchor at 504). This is the **inverse problem** (cannot recover components from the aggregate); P1's separation and the σ-wave's relevance-test component (2) are the **forward problem** (the aggregate falsely certifies unsafe transitions, and the report flips as a function of σ). The two claims are logically independent and jointly stronger; the family division of labour is clean. No action needed; recorded so the v53 σ-subsection's framing ("the report is a function of σ") does not drift into identifiability language that ECOMOD owns.

### 3.4 P2's substitution-feasibility caveat is the feasibility-side complement of the σ-spectrum

P2 v43's supplementary, "(d) The linear substitution alternative," states the Farkas/Gale certificate for substitution pathways and adds: "The multipliers are a separation certificate, **not universal exchange rates**: nonlinear, nonconvex, path-dependent, spatial, or irreversible technologies require their own feasibility analysis, and **an elasticity fitted near one operating point cannot establish global substitutability**" (supplementary lines ~491–494). The σ-wave is the exact, witness-datum version of the assessment-operator side of exactly this caveat: P2 bounds what *material pathways* can achieve; the wave computes exactly *which aggregator elasticities false-certify* (σ\*(z), Theorem S2). This also resonates directly with queue point **3.A-15** (the pre-Theorem-9 implementability/feasibility limitation paragraph) — the family already carries the feasibility-qualification discipline, so P1's paragraph will be consistent with P2's phrasing genre ("exhibit the separator rather than assert impossibility", P2 supplementary line ~494). Optional owner-gated cross-citation in the σ-subsection or the 3.A-15 paragraph.

### 3.5 σ-notation: four distinct σ's in the family — a disambiguation clause is advisable

| Paper | σ denotes | Evidence |
|---|---|---|
| P1 σ-wave (and the planned v53 subsection) | elasticity of substitution, σ = 1/(1−θ); the wave already guards P1-internal collisions by using θ for the exponent (vs the manuscript's ρ weight-ratios) | `SIGMA_SPECTRUM_WAVE.md` §2 |
| P2 v43 | **σ\*(B₀) = the guaranteed blind-window survival time** (the timing certificate) | lines 842–849; Remark `rem:sigma`; the summary-table row "delayed information … σ\*(B₀) < T_obs" (line 1367); the hidden-regime fishery instance σ\* = z₀ − 1 (lines 1557–1561) |
| EMS v8 | **σ(B) = the Schaefer surplus function** | σ(16/5) = 1088/125, σ(6/5) = 528/125 (lines 374, 496, 511–512, 567) |
| ECOMOD v35 | **σ_f, σ_c = human-available flow shares** (and the Half-Earth reservation share in E ≤ σB) | lines 128, 157, 199, 299, 422 |

Each is internally consistent in its own paper — but a reader moving across the family meets four σ's, and P2's σ\* is *also* a critical-threshold symbol of a certification theory (as is the wave's σ\*). Recommendation (owner-gated, one clause): the v53 σ-subsection's notation guard should add a sentence distinguishing P1's σ (substitutability elasticity) from the family's other σ uses — in particular from the software companion's surplus function σ(B) and P2's timing threshold σ\*(B₀). Note also P2 uses φ_U as a map symbol (line 1115) where the wave uses φ for the golden ratio — different scopes, no action beyond the same clause's spirit.

### 3.6 "Spectrum" terminology — distinct referents, already disambiguated by qualifiers

ECOMOD's "Scope of the spectra" (line 228) and its characteristic-equation/eigenvalue spectrum (lines 270–274) refer to its analytic spectra; the wave's object is the *substitutability* spectrum (the elasticity ladder). The P1 subsection title "The substitutability spectrum on the witness datum" carries its own disambiguating qualifier; no action needed beyond this record. (Family word note: "ladder" is a family term — E1/E3's forecast ladders, ECOMOD's identifiability-ladder table (`tab:ladder`), and the wave's critical-floor ladder — all ordered-rung structures; consistent usage, no collision.)

### 3.7 The LPI identification — family-new; no conflict

No family paper uses the Living Planet Index (zero hits); ECOMOD's empirical programme is the ecological-footprint (NFA) side. The wave's LPI identification (σ = 1 member = the LPI functional form on floor-referenced indices, with its two caveats) stands as family-new content; no other paper's claims constrain it.

---

## 4. The family cross-reference web

### 4.1 The Abaee letter mapping is per-paper (legitimate), and diverges across the family — a navigation note

| Citing paper | its 2026a | its 2026b | its 2026c |
|---|---|---|---|
| EMS v8 | **P1** — *Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility* ("Manuscript submitted for publication", bibitem lines 964–967) | **P2** — *An Obstruction Calculus for Viability under Incomplete Observation* (lines 969–971) | — |
| ECOMOD v35 | **P4** — *Delay-Induced Regime Change in Harvested Stocks: … the Review Interval as Control* (Zenodo 22554217, line 694) | **P1 (superseded title)** — *The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment* (Zenodo 22545740, line 695) | **P3** — *Typed Flux Ledgers and Depletion Arithmetic* (Zenodo 22554177, line 696) |
| P1 v52 | cites companions **by title, unlettered**: P3 (*Typed Flux Ledgers…*, lines 109/158/339/1654), E1 (*Does a surplus-production ladder improve forecasts of Northern cod?*, lines 1148/1299/1652), E3 (*Does a one-pool water-balance model improve forecasts of Edwards Aquifer head?*, lines 1148/1650), plus its own figshare verification deposit (line 1656) | | |

Author–year lettering is assigned per reference list, so the divergence is standard practice, not an error. The **navigation hazard** is real, though: "Abaee, 2026a" means P1 in EMS and P4 in ECOMOD; "2026b" means P2 in EMS and P1 in ECOMOD. Recorded so that any future cross-reading or cross-citation is done by **title + DOI**, never by letter.

### 4.2 ECOMOD v35 cites P1 under a superseded title (stale cross-reference; owner-gated)

The batch-7 implementation scripts prove the superseded title is P1's own md-lineage title: `apply_batch7_wave2.py` sets P1's title line to "# The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment" (lines 248–251), and `apply_batch7_wave4_p1.py` asserts the v20 title line starts with exactly that string (lines 888–889). The current title — in the tex lineage (v52 line 20) and in EMS's bibliography entry — is *Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility*. ECOMOD's "Abaee, 2026b" entry (Zenodo 22545740) therefore cites the compensatory-aggregation companion **under the title that manuscript has since superseded** — consistent with the Zenodo deposit it points to (the deposit presumably preserves the deposit-time title; whether it is a deposit of the old-titled P1 or of a distinct companion document is owner-side knowledge to confirm), but no longer matching the current manuscript. **Consequences:** (i) nothing is changed this round (the isolation rule: ECOMOD is another paper's file); (ii) the finding is recorded for a **future ECOMOD version of its own** (new version, never overwrite) to update the entry and its "aggregation theorem (Prop 1)" forward reference (ECOMOD has no proposition environments — "Prop 1" is the old deposit's internal numbering, a dangling reference in the current manuscript); (iii) when P1 v53 adds positioning or σ-subsection cross-references, it must cite the EMS companion and other family works by **current titles**, not by any letter.

### 4.3 The deposit-sharing and check-list-separation discipline is family policy; the σ-wave already complies

P1 v52's data-availability statement: "the software companion's archive — the SafeTransition library (with its own separate 24-check benchmark suite), whose master deposit this shared item also is. **The two check lists are distinct and are not pooled**" (line 1796). The σ-wave's verifier (57/57, `batch 8/sigma_spectrum_wave/`) is a third, likewise separate, check list. Consistent; no action.

### 4.4 The three-illusions doctrine is consistent across the family

P1 v52: the separation datum "is distinct from the *productivity illusion* — adequate delivery from a reduced productive base — treated in Abaee (2026, *Typed Flux Ledgers…*)" (line 158). ECOMOD v35: "The term is deliberately *composition* illusion here … which the companion frames as the yield-inflation sense of its 'productivity illusion'" (lines 495–497, citing its 2026c = P3), and "the aggregate rises *not* merely because technology outpaces degradation (the productivity illusion as Abaee, 2026c, defines it), but because the two books are re-weighted" (line 71). The family's three masking concepts — P1's quantifier-order separation gap, P3's productivity illusion, ECOMOD's composition illusion — are explicitly mutually distinguished by the papers themselves. Consistent; the v53 additions (σ-subsection, positioning) should preserve these distinctions verbatim (in particular, the σ-subsection's "false certification" language should not be re-labelled "illusion").

---

## 5. The 42-point queue × cross-paper status (compact)

| Queue point(s) | Cross-paper status this round |
|---|---|
| 1 (four-protocol table), 3 (interpretation box) | **NO INTERACTION** — protocol numbering is P1-local; EMS uses operator names, P2 certificate names; P2's summary table (`tab:summary`, lines 1358–1375: certificate / emptied correspondence / design consequence) is the family's formatting precedent for such tables |
| 2 (semantics table) | **PRE-ANCHORED** — EMS's five-operator presentation + chain (§2.5 above); names must match |
| 4 (validity section + 4 design tests), 5 (10-point checklist) | **NO FAMILY PRECEDENT** — no checklist or validity-test section anywhere in the checked set (EMS suppl S1–S11 is a software supplement); P1-original additions, no conflict |
| 6 (three-regime disturbance sensitivity; middle cell unanalyzed) | **NO PRE-COMPUTATION** (§2.9); the exact middle-cell task stays P1's |
| 7 (positioning: Becker 2017, EBFM, Table-2 fisheries column; Gao 2023 already closed) | **IMPORTABLE + PRECEDENT** (§2.1, §2.2): Becker entry importable from ECOMOD line 698; the EBFM viability entry importable from P2 lines 1709–1711; optional Nardo/Fischer cluster (owner-gated); no conflicts |
| 8 (σ-spectrum labelled extension) | **ENRICHED, NOT PRE-EMPTED** (§3): wave results stand; optional cross-citations to ECOMOD's instance (line 437) and P2's substitution caveat; the σ-notation disambiguation clause (owner-gated) |
| 9 (reserve institutional forms) | **PARTIALLY PRE-IMPLEMENTED** in EMS (§2.4): align terminology + owner-gated pointer |
| 10 (conservatism caveats) | **CONSISTENT + STYLE PRECEDENT** (§2.10: ECOMOD's Allee-free disclosure) |
| 11 (dashboard disclaimer) | **CONSISTENT** — EMS's Dashboard readings/index-blindness alarm is the realization (§2.11) |
| 12 (Filippov/Warga entries) | **NO PRECEDENT** (§2.3); proceed as planned |
| 13 (in-text citations: De Lara & Doyen 2008; Rockström 2009; Raworth 2012) | **PREEDENT + IMPORTABLE** for De Lara & Doyen (§2.2); Rockström/Raworth P1-local as planned |
| 14 (exact-DFO motivation paragraph) | **P1-ONLY** (§2.8); nothing to import or conflict |
| 15 (pre-Thm-9 limitation paragraph) | **RESONATES** with P2's substitution-feasibility caveat (§3.4); consistent genre |
| 16–24 (precision rewordings) | **NO INTERACTION** except 23: **REINFORCED** family-wide by EMS's deposited kt values (§2.7); 24: P1-only, no CSD collision (§2.8) |
| 25–31 (mechanical fixes) | **NO INTERACTION** (P1-internal); 29's MSY has the ECOMOD precedent (§2.6) |
| 32–37 (OVERRIDDEN, standing) | **UNAFFECTED** — the standing no-removal rule is orthogonal to the other papers |
| 38–39, 42 (REJECTED, standing) | **UNAFFECTED** — and §2.7 strengthens 38/39's rejection basis (the family's kt deposit) |
| 40–41 (DISCHARGED by the wave) | **STAND** — no family pre-emption (§3.1) |

**Net effect on the queue: zero removals, zero downgrades, zero conflicts; four importable items (Becker entry; De Lara & Doyen entry; the EBFM viability entry; the EMS institutional alignment), two enrichment opportunities (ECOMOD/P2 cross-citations for the σ-subsection), one advisable clause (σ-notation disambiguation), one cosmetic option (B_lim typesetting alignment), and one recorded stale cross-reference in ECOMOD for a future round of *that* paper.**

---

## 6. Impact on the incorporation plan (`QUEUE_REVERIFICATION_AND_PLAN.md` Part D)

The ordered plan (mechanical → precision → additive; owner-gated decisions; never-overwrite; re-verify-first) is **unchanged in structure**. Additions to the owner-gated list, from this round:

1. **σ-notation disambiguation clause** in the v53 σ-subsection (distinguish P1's substitutability elasticity σ from EMS's surplus σ(B), P2's timing σ\*(B₀), ECOMOD's flow shares σ_f/σ_c) — one sentence, additive.
2. **Cross-citation options for the σ-subsection**: ECOMOD's composition-illusion instance (its line 437) as the continuous-time companion; P2's linear-substitution alternative (its supplementary (d)) as the feasibility-side complement. Both additive; both strengthen the relevance chain without new claims.
3. **Institutional-paragraph alignment with EMS v8** (terminology/quantities; optional pointer to the software companion).
4. **Optional positioning-cluster extension**: Nardo et al. (2008) and Fischer et al. (2022), importable from ECOMOD's entries (lines 732, 711), if the owner wants the full composite-indicator methodology cluster beside Becker 2017 and Gao 2023.
5. **For a future ECOMOD round (its own new version, not this repo round)**: update its P1 entry to the current title; resolve the "Prop 1" dangling reference; note its per-paper lettering will then need recomputing.
6. The wave's §8 transcription sketch gains (owner-gated) the same optional pointers as (2).

## 7. Honest residuals

- This check is **static at commit `8343206`**. Per the standing re-verification protocol (queue plan Part A), if any companion moves (P2 v44+, EMS v9 / master v3, ECOMOD v36+), re-run this cross-check against the then-current versions before implementing anything that depends on it.
- Whether Zenodo 22545740 is a deposit of the old-titled P1 or of a distinct companion document is **owner-side knowledge**; this round's evidence (the batch-7 scripts) establishes only the title's provenance in P1's md lineage.
- The middle-regime disturbance cell and the off-diagonal geometric residual remain open exactly as the queue plan Part E records — nothing in the family pre-computes them.
- No file outside this report and the worklogs was created or modified; `paper1_assessment_separation_v52.tex` is untouched; every other paper's latest version is untouched.

## 8. Implementation record

- This round began by pushing the previous turn's unpushed creation: commit `8343206` (Task 105's `batch 8/sigma_spectrum_wave/` deliverables) — pushed to `origin/main` with the owner's PAT (as supplied this round, no suffix issue; in-memory use only, temp askpass outside the repo, chmod 600, deleted after use, output redacted, zero residue; rotation remains advisable).
- This file — `BATCH8_PAPER1_CROSS_PAPER_CONSISTENCY_CHECK.md` (repo root, beside the joint assessment) — is the round's only other creation. Line-level evidence: all quotes located in the named files at the named lines this round.
- Verification artifacts: the greps and passage readings of §1–§5 were performed directly against the five latest-version files at commit `8343206`.

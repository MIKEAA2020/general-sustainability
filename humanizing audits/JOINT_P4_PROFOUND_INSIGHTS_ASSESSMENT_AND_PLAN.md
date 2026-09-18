# Joint evaluation, verification, and implementation plan — the six "P4 profound insights" audits (batch 8)

**Task:** Owner-directed (fresh PAT, redacted): "evaluate and verify 6 repo audits in general-sustainability/batch 8/p4 profound insights.txt. provide joint assessment and implementation plan, strengthening, augmenting, improving, correcting and completing weaker suggestions and defects, while adjudicating contradictory points."

**Date:** 2026-09-18 (Task 92).

**Baseline under verification:** `arena agent 1/paper rewrites/paper4_delay_dynamics_v35.md` (md5 `e9c99edbcf59cce80f2bd08c2966a74b`; tex md5 `f1bdcd666b…` per the wave18 triple-build record; 44 pp). v35 is the current latest P4 version; v31–v34 remain untouched on disk and in history.

**Source file:** `batch 8/p4 profound insights.txt` (5,440 lines, md5 `a52af3038216d7603f01735c7da7b90f`). The six audits and their line ranges:

| # | Label | Lines | Character |
|---|---|---|---|
| 1 | `sol:` | 1–1209 | "Bird's-eye assessment and upgrade strategy" — 19-section strategic review |
| 2 | `grok:` | 1210–1264 | Seven compact theses with economic/ecological analogues |
| 3 | `gemini:` | 1265–1736 | "Phase-Stabilisation Trap" etc. — line-level mathematical re-derivations plus policy packaging |
| 4 | `qwen:` | 1737–3888 | The correction audit — 20 sections of "corrected and strengthened core claims" |
| 5 | `sol2:` | 3889–5106 | "Generalized assessment and upgrade strategy" — 22 sections |
| 6 | `deepseek:` | 5107–5440 | "Genuine Improvements: What the Existing Analyses Miss" — meta-critique of the other five |

**Verification protocol.** Every checkable claim about the paper (numbers, quoted sentences, theorem forms, certification tiers, section references) was checked against v35 directly (targeted reads and greps of the md source; the wave18 ledger already certifies md↔tex↔PDF parity). The verdict vocabulary: **VERIFIED** (claim matches v35), **STALE** (claim matches an older version or a phantom, not v35), **DEFECT** (claim is wrong as stated), **NEW** (proposal not present in v35). Contradictions between audits are adjudicated in Part II with the paper's own text as the referee.

---

## Part 0 — The headline finding

Measured against v35, the six audits are, in weight order:

1. **A large already-implemented fraction.** The audits' central demands — the governance-loop framing, delay-type separation, sign/gain/cadence as design coordinates, the hybrid (not discretisation) reading of periodic review, the Euler-artefact warning, inter-review safety flagged as the uncertified criterion, cod as timescale grounding rather than calibration, the "mechanism transfers, thresholds do not" generality statement, certification-tier discipline, well-posedness (invariance/boundedness/smoothness scope), the gain-based (not sign-based) no-Hopf theorem, the critical-gain/small-gain exclusion, ℓ₁ values with method and status, the three-scheme sampled-data record, and the fold/capture certification scoping — are all already in v35, most of them since v31–v33. Part III is the ledger.

2. **A correction-of-each-other layer.** qwen corrects gemini (correctly, on the mathematics); sol2 corrects sol (correctly, on lag additivity); deepseek critiques all five (partly correctly, on identification). In every adjudicated contradiction, the paper's existing text already takes the correct side. Part II.

3. **A stale-phantom layer.** Several "corrections" quote or characterise text that does not exist in v35 (the v3/v30-era "even multiplicity" abstract; a title with "formatting problems"; an "E described as three things" ambiguity that §6.1 already disciplines; deepseek's "claims it applies to everything"). These are recorded so the rejection discipline can cite them.

4. **A genuine-residual layer — small.** What actually survives verification as new and actionable at revision scale: (a) two dangling cross-references in §1.2(4) (a paper defect the audits missed); (b) a §11.8(ii) completion naming the delay stages the single lag compresses; (c) a §11.9 completion registering parameter-box certification as a stated open task. Everything else the audits propose is either new science requiring its own certification (safe-cadence computation, viability, stochasticity, parameter boxes, strategic behaviour, multi-actor models) or uncited interpretive packaging. Part IV.

5. **No numeric fabrication found.** Every one of the ~45 checkable numeric/verbatim claims about the paper's content checks out against v35 (3.67/150.36; 5.5128/80.4245; the 13-digit enclosures; ℓ₁ = +5.75×10⁻⁵ and +3.55×10⁻⁴; 2.306; 6.50; 47.536/79.143 with exact radii 0.786/0.597; 5.5872362; 64.4023272; [148.6, 149.5]; the rg ≈ 1.5–1.6 locus; the g-band τ-windows; 2–13 yr; 358.8 yr; 16.96 yr; N ≈ 33/10; 158/430; ρ records 0.9838/0.9967/1.00055/1.00035; loop gain 0.08011; the C_Z, B_N, B_E, L(λ) formulas verbatim; Moxnes 1998 cited). This file is unlike earlier audit batches: nothing landed on the rejection list for fabrication. The defects are of overstatement and staleness, not invention.

---

## Part I — Audit-by-audit evaluation

### 1. `sol` (bird's-eye assessment) — **sound diagnosis, stale in part, over-prescriptive in structure**

**What verifies.** The paper *is* organised around exactly the "deepest idea" sol names — §1.1: "The delay studied in this paper sits elsewhere: in the *institutional* loop"; the abstract: "Institutional form and timing, not ecological lag, decide whether governance stabilises or destabilises the stock." The certification discipline is praised accurately (§11.5's three tiers). The "13-digit certificates… certify arithmetic, not policy robustness" point is the paper's own §11.5(2) sentence. The cod discipline demanded (Level 1 illustration / Level 2 mechanism / no Level 3 calibration) is implemented: §11.4 — "the northern cod record is a timescale grounding and a caution, not a calibration… No stock, effort law, or delay value in this paper is calibrated to a named fishery." The stock-agnosticism critique ("needs a sharper boundary") is already answered by §11.3: "What transfers to other periodically reviewed renewable-resource regimes is therefore the mechanism's form, not the numerical thresholds" — almost word-for-word sol's demanded sentence. The "phase management has costs" message is the paper's §8 Governance warning ("Local spectral stability is not governance… inter-review tube safety… is the additional criterion… not certified here") and §11.3's second caution.

**What is stale.**
- *"The current title… contains formatting problems"* — **STALE/DEFECT.** The v35 title is clean; no formatting defect exists. (A claim carried from an old draft.)
- *"The variable E is described as institutional deployment effort, industry effort, or quota utilisation"* — **PARTIALLY STALE.** §6.1 already carries the interpretation discipline ("these interpretations are not interchangeable; the quota-tracking law is an institutional control law"), and §2.2 fixes "institutional deployment intensity." What sol adds — a one-line narrow definition ("effective harvest pressure") — is a phrasing choice, not an unresolved ambiguity.
- *Abstract advice* ("avoid listing every certification tier and every numerical threshold") — the v35 abstract lists exactly the load-bearing thresholds under the owner's 260-word cap, each with its caveat inline. Already satisfied.

**What is over-prescriptive.** The four-papers split (§3) and the single-spine reorganisation (§12–§14, §16–§18: new title, new abstract logic, new section plan) are owner-level restructuring decisions, and they collide with two facts: (a) the companion ecosystem already exists — the paper explicitly defers to "the companion sampled-governance paper" (§11.4), "the companion analyses of sampled governance and assessment architectures" (§9.5), "the companion flow-balance framework" (§9.6), and "the separate companion of Section 7.5"; the splitting sol demands has largely happened *around* P4; (b) the registered-record density (§7, §9) is the deliberate product of the owner's v32–v33 rounds, and deleting it to slim the main text would destroy verified records the owner chose to keep. The defensible core of sol's structural demand — *state which tier each result belongs to* — is already implemented (§2.3 registered family, §11.5 levels, §11.8 limitations).

**Strengthened residue (adopted into the plan).** The delay-decomposition taxonomy (§5.1) is sol's best genuinely-new item; strengthened and grounded in §11.4's own cod chronology it becomes edit **E2** of Part IV. Its parameter-set robustness demand (§7.3) becomes open-task edit **E3**.

### 2. `grok` (seven theses) — **fully verified numerically; interpretive extensions properly hedged**

Every load-bearing numeric claim checks against v35: the 3.7–150 gated-A and 5.5–80 Candidate-B windows (§5.1 table); the protective delay-independence ("modulus cubic has no positive roots, loop gain ≪ 1, Descartes plus Routh–Hurwitz… for every delay" — Theorem 6.1 with Γ sup 0.08011); the interpolation corollary ("delay-induced instability requires a sufficiently large mobilising weight… cannot be produced by decreasing τ_p alone" — Corollary 5.1, with the paper's own sufficient-condition caveat); the subcritical lower crossing and fragile window; the folds "certified only at discrete-collocation level; continuum residuals and the delay-equation lift remain open" (§9.2, §11.5(3)); "capture onto a large-amplitude face cycle near 149 yr is a basin-boundary event, not a fold; the cycle itself could not be Fourier-collocated" (§9.2: [148.6, 149.5], two recorded collocation failures); "the returning arm… is not generically reachable near the fold" (§9.2 verbatim); "an apparent 2.3 yr threshold is an Euler artefact" (§6.4: 2.306); "a restabilising complex unit-circle crossing (Neimark–Sacker signature) appears near 6.5 yr under the exact held-measurement update" (Proposition 8.1: 6.50 yr); "Euler-reported half-century and period-doubling crossings are command-step artefacts" (Remark 8.1: 47.536/79.143 → exact 0.786/0.597); Moxnes laboratory experiments (cited: §1.1, §11.1, references); the rg ≈ 1.5–1.6 locus, the g-window/2–13-yr placement, the 358.8-yr cohort cycle, the 16.96-yr loop cycle (§7.3–§7.4, §11.7). grok also correctly hedges the NS reading ("signature") where the paper reserves the bifurcation name.

**Interpretive extensions (NEW, not in the paper).** The countercyclical-buffer/procyclical-lending analogy; "many tragedies of the commons are tragedies of procyclical governance"; the climate-drift item (§7: parameter drift moving the window — grounded in §9.5's r-dependence of τ± but not narrated in the paper); the dual-hysteresis institutional reading. These are discussion-grade material, correctly framed by grok himself as transferable-architecture talk. **Adjudicated: recorded as future-work/owner-optional narrative, not revision content** (they would import unverified institutional claims into a paper whose discipline is registered records).

**One nuance to keep.** grok's "The undelayed system is already unstable" is true for the gated mobilising law at both candidates (§5.1); his window fragility reading matches §5.2's subcriticality record *including* its status caveat ("computational results, stated as such") — grok does not overstate it. Best audit of the six on fidelity.

### 3. `gemini` (phase-stabilisation trap) — **formulas verified verbatim; two mathematical overstatements; packaging contributions**

**What verifies (all verbatim against §2–§9).** The undelayed Routh–Hurwitz failure mechanism ("the linear term is depressed below the threshold required to balance the constant term A_N d C_E" — §5.1's own derivation); τ₋ ≈ 3.67, τ₊ ≈ 150.36; ℓ₁(τ₋^A) = +5.75×10⁻⁵; the amplitude scaling ‖·‖ ∝ √(τ − τ₋) (§5.2: slope 29.8 in amplitude-squared, R² = 0.994); the even-pairs algebra — B_N = −A_N/(2τ_m), B_E = −A_E/(2τ_m), sp_k'(0) = 1/2, A_E B_N − A_N B_E ≡ 0, L(λ) = B_Eλ, H(x) = (x + A_N²)(x + d²)(x + C_E²) − C_Z²B_E²x, H(0) > 0, cardinality {0, 2} generically (Corollary 4.1 — including the "generically zero or two distinct simple roots" form); the mobilising-law formula and its C_Z with the δ₀ Z_ref/(Z_ref + δ)² term (§3.2, verbatim); the M3-LC two-channel equation and its ψ-invariance claim (§2.3: "the equilibrium, the Jacobian, the characteristic equation, and both Hopf points are independent of ψ and κ. Local equality does not imply excursion equality" — gemini's §5 is a re-derivation of the paper's own registered statement, down to the culling-vs-suppression divergence); the 6.5-yr NS crossing and the 2.3-yr Euler artefact (Proposition 8.1, §6.4).

**Defect 1 — the "Sign Separation Theorem".** gemini's §6 opens: "The central theoretical result of the paper is the **Sign Separation Theorem**: C_Z > 0 ⟹ two subcritical Hopf…; C_Z < 0 ⟹ No-Hopf Theorem; absolute, delay-independent stability." **This theorem does not exist in the paper, and the paper refutes it.** Proposition 6.1 (iso-gain sign flip) proves that the modulus cubic depends on C_Z only through C_Z², so "feedback sign alone cannot create or eliminate Hopf-frequency families over the unrestricted delay axis, and the protective no-Hopf property of Theorem 6.1 is a property of the quota law's modulus (its direct damping and delayed gain), not of its sign." §11.1: "the sign alone does not decide… of which the sign is one ingredient among three (modulus, phase placement, and digital implementation)." Theorem 6.1 is pointwise in the declared coefficients with the Descartes/Routh–Hurwitz gain certificate; Theorem 10.1 is the small-gain exclusion. Also "absolute" is wrong twice: the paper claims pointwise-in-τ exponential stability "without a delay-uniform decay rate being claimed," and the gated-A subcriticality does not generalise (the ungated Candidate-B lower crossing is *supercritical*, ℓ₁ = −9.84×10⁻⁵, §5.2 — which falsifies gemini's categorical table "Subcritical entry at τ₋, subcritical exit at τ₊"). qwen and sol2 both correct this; the correction is right and already embedded in the paper.

**Defect 2 — settledness overclaims.** gemini narrates the basin-evaporation reading ("sheathed by an unstable periodic orbit that acts as the separatrix… basin shrinks to zero") as established, and "Viability Bleed" as a demonstrated computation ("If the review cadence is too long, N(t) can drop below N_lim… even while ρ(M) < 1"). The paper keeps both at their declared status: the saddle-node-vs-crisis alternative "survives as a reading of the archived record" (§9.2), and inter-review safety is explicitly *not certified* (§8 warning; §11.4 supplies the cod instance — "a stock falling by a factor of more than twenty between annual assessments" — as the documented counterpart). The naming contributions ("phase-stabilisation trap", "viability bleed", "administrative hunting", "basin lock-in") re-brand phenomena the paper already states in plain words; under the rejection-list discipline (no decorative coinage without new content) they are **not adopted**, but the phenomena they name are confirmed real in the paper's records.

**Strengthened residue.** gemini's microfoundations section (capital fixity, debt ratchet, stranded capital) is genuinely absent from the paper — but it is entirely uncited formalism (Π = P(Y)qEN − c_vE − r_dD_b etc.), and the audits supply no source for it. Under the no-unverified-import rule it cannot enter the paper as claims. The *grounded* fraction — why mobilising signs arise — is already present at the paper's chosen resolution: §1.1 (Moxnes 1998 misperception; Ostrom 1990 institutional design), §5's behavioural reading ("a fleet expansion, a subsidy release, an open-access licence issuance"), §11.4's cod record (overexploitation under sustained pressure; incremental institutional response — Walters and Maguire 1996). **Adjudicated: future work with citations required; not v36 content.**

### 4. `qwen` (the correction audit) — **the most important audit; its corrections are mostly right, mostly already in the paper, and partly aimed at phantoms**

qwen's structure is "the upgrade plan contains claims; correct them." Since the "upgrade plan" is gemini's text, qwen's corrections land on gemini, not on v35. Verification of each numbered correction:

- **2.1 "positive roots come in even multiplicity" — STALE PHANTOM (verbatim-verified).** No v31–v35 abstract contains that sentence; it is the v3/v30-era phrasing — and qwen's quote is *verbatim* from the v30 abstract ("a filter identity implies that positive roots come in even multiplicity"), i.e. qwen was auditing an abstract six major versions old. The precise form qwen proposes ("the total algebraic multiplicity… is even; generically zero or two distinct simple roots") *is* Corollary 4.1, verbatim, since v31. Correction valid against the phantom; nothing to do.
- **2.2 "C_Z < 0 implies no Hopf" is too strong — CORRECT, and already the paper's position.** Theorem 6.1 is modulus/gain-based and pointwise; Proposition 6.1 proves the sign-insufficiency; Theorem 10.1 is exactly the "critical gain theorem" qwen proceeds to propose in §5.4 (its C_*² infimum is the paper's (H1) supremum bound in reciprocal form). qwen's "gain–phase stability theorem" already exists as §10.1–§10.2 plus the Halanay-type companion certificate.
- **2.3 "delay stabilises is dangerous unless qualified" — already implemented.** §8's warning, §11.3's caution ("Local spectral stabilisation is not governance"), the abstract's "more frequent assessment is not always safer… a local spectral design parameter."
- **2.4 "five-regime attractor topology too strong" — substance already scoped.** §9.2: "on the explored fundamental-delay range — 0 < τ ≲ 160 yr, before the first recurrent branch (≈253 yr, Theorem 4.1)… a statement about the declared domain… not the entire positive delay axis"; every regime cell reads "the only attractor found from the declared tested histories"; §1.2(6) adds the uncollocatable-capture caveat. The abstract's compressed noun phrase carries its caveats in-sentence ("two folds certified at the discrete collocation level (continuum stages open)… an unverified large-amplitude attractor"). qwen's rephrase ("five numerically observed dynamical regimes…") would re-say what the body already says; under the owner's just-settled 258-word abstract, **not recommended**.
- **2.5 folds: Path A vs Path B — the paper already chose.** §11.5(2)–(3) declares the Church–Lessard upgrade "a stated open task," carries the discrete-collocation certificates with both open stages named, and §11.9 registers the upgrade as the first open theorem. qwen's Path B wording is the paper's current wording.
- **2.6 sample-and-hold scheme-dependence — already implemented, more completely than demanded.** §8's opening ("not the delay equation… sampled at τ = T_r"); the three-scheme record (Euler / exact held-measurement / native ZOH, 6.50–6.73-yr band) in the scheme-dependence remark and the consolidated table; Remark 8.1's artefact labelling. qwen's §11.3 asks for exactly this trio.
- **2.7 subcriticality certification — already implemented.** §5.2 reports both ℓ₁ values, the method (Hassard–Faria–Magalhães cubic from exact derivatives), the status ("numerical evaluations… stated as such"), and two further status distinctions (branch-scaling vs centre-manifold; the k-regularisation caveat with the sp_k''(0) = k/4 dependence). qwen's fallback wording is weaker than what is there.
- **2.8 cod not calibration — already implemented** (§11.4, quoted in Part I.1).
- **§5.1 well-posedness — already implemented.** Theorem 2.1 (forward invariance of the admissible box), Corollary 2.1 (boundedness, global continuation, compact set, local-Lipschitz), the C¹/floor-inactive scope ("the C¹ statements are needed only where bifurcation coefficients are computed, and there the floor-inactive parameter sets of Section 5.2 are the declared scope"), the equilibrium-away-from-nonsmooth-boundary checks (the M3-LC floor "never binds at the interior equilibrium"; the (1) floor cancels at δ = log2/k). qwen's "do not apply smooth Hopf formulas uncritically to a nonsmooth system" is precisely the paper's declared-scope discipline.
- **§5.5 phase condition separation — already implemented** (Theorem 4.1 separates modulus (6) and phase (7); §6.3's iso-gain flip is the sign-lives-in-the-phase demonstration).
- **§5.7 parameter-box robustness — GENUINE PARTIAL GAP.** §9.5 has one-at-a-time windows (τ₋ ∈ 4–25 yr across the full (r, η) rectangle; the r-window (0.008, 0.06)), and §11.5(2) concedes the point ("they do not represent parameter-estimation uncertainty… must add a sensitivity layer"). Box-level interval certification is absent — because it is new computation with its own certification. **Adjudicated: register as a stated open task (edit E3); do not compute in a revision round.**
- **§11.1 evidence-status framework — present in prose** (§11.5's three tiers, maintained claim by claim). A letter-code table is cosmetic relabelling; **not adopted.**
- **§14 reorganisation / §16 roadmap / §15 nine principles — owner-level restructuring; not adopted** (same adjudication as sol's split).
- **qwen's proposed abstract** (§14) is a *longer* restatement of v35's existing abstract elements; v35 already implements the five-element logic under the owner's 260-word cap.

**qwen's own defects.** (i) It attributes the "even multiplicity" quote to "the original abstract" without a version — the phantom problem. (ii) It proposes proving a critical-gain theorem and an exact-monodromy definition that are already Theorem 10.1 / Theorem 8.1 + Proposition 8.1 — it did not check the paper's §8/§10. (iii) Its §2.4 recommendation ignores that the body already carries the demanded scoping. Net: qwen is right wherever it corrects gemini; it is redundant wherever it corrects the paper.

### 5. `sol2` (generalized assessment) — **sound; adds little beyond sol + qwen; its two unique mathematical cautions are already in the paper**

- *"The total institutional lag need not be a simple arithmetic sum"* — correct as against sol's serial-sum presentation, with the caveat that purely serial discrete delays *do* add; the non-additivity claim is right for filtered, parallel, adaptive, or distributed components. The paper needs no adjudication here because §11.8(ii) keeps the single-lag limitation and defers distributed/variable-time lags. **Adjudicated: sol2 over sol on the taxonomy; no paper change beyond E2's stage-naming.**
- *"Avoid claiming that paired frequencies automatically imply exactly two delay thresholds; each frequency generates a family of admissible delays"* — already Theorem 4.1's own clause ("higher branches recur within a family as τ_{n,0} + 2πk/ω_n and are not additional frequencies") plus the branch-separation statement.
- Its gain-bound g_crit formalism is again Theorem 10.1; its subcriticality caution ("does not by itself prove the global destination") is §9.2's discipline; its evidence codes duplicate §11.5; its Tier hierarchy duplicates §2.3's registered family + §11.8; its safety hierarchy (10 levels) is a longer restatement of the paper's caution chain (§8 warning → §11.3 → §11.5) — the paper deliberately keeps three named levels rather than ten.
- Its genuinely useful framing — "Choose the response direction → bound the gain → design the cadence → verify safety → test robustness" — is the paper's Conclusion in imperative form ("The laws differ not merely in sign but in modulus, damping, phase placement, and digital implementation… the review interval is a control variable… the institutional coefficients… to be identified, bounded, and designed against"). **No change.**

### 6. `deepseek` (genuine improvements) — **the only audit adding a genuinely new *category* (identification); its charges against the paper are largely stale; its programme is future work**

**What is already in the paper against deepseek's charges.** The identification problem: §11.8(i) ("the institutional coefficients have not been identified from field data; the results are theorems about the declared class"), §11.4 ("the institutional coefficients — the gains, delays, and cadences of the governance loop — remain to be identified from field data before any threshold of the declared class is read against a fishery"), §9.5 ("the separate effort scale is not identifiable from (N, Z) alone… treated in the companion analyses"), §11.4's structured-search null result ("A structured search across more than thirty resource systems for an unconfounded instance… found no eligible case"), and the Conclusion's closing programme sentence. deepseek's demand "state clearly that the model is structural and theoretical, not estimated" is §11.8(i) verbatim in substance. Its "the paper presents its results as general properties… claims it applies to everything" is **STALE** — §11.3/§11.8 are precisely scoped (mechanism-form transfer, thresholds-don't, single-lag, scalar-logistic, provisional-global caveats). Its smoothness charge ignores §2.2's declared-scope discipline; its stochasticity charge is §11.6's candidate-diagnostics caveat territory; its "signal construction" critique overlooks §11.6's epistemic-divergence discussion (true vs estimated state, observable substitutes).

**What is genuinely new and meritorious.** The three-layer identification anatomy (observational equivalence of (τ_m, τ, C_Z) triples; endogeneity/simultaneity; non-stationarity) and the "mechanism identification, not parameter estimation" framing; the anticipation/strategic-compliance layer (preemptive harvesting as an effective forward-looking term — the paper has no such content); endogenous signal manipulation; multi-actor heterogeneity; the normative-objective gap; the claim that even a perfectly identified parameter triple underdetermines the functional form. All of these are *correct observations about the research programme*, none are revision-scale: they are open-problem register material. **Adjudicated: E4 records the identification-layer statement (the one item groundable purely in the paper's own existing admissions); the rest is future work for the owner to commission as separate research.**

---

## Part II — Contradiction adjudication (with the paper as referee)

| # | Contradiction | Sides | Verdict |
|---|---|---|---|
| C1 | Sign vs gain as the protective no-Hopf mechanism | gemini: "Sign Separation Theorem" ⟷ qwen §2.2, sol2 §3.1: sign alone insufficient | **qwen/sol2 correct.** The modulus condition depends on C_Z²; the paper's Proposition 6.1 proves sign-flips translate delay families by odd half-periods without creating/destroying them; Theorem 6.1 is gain/modulus-based and pointwise; Theorem 10.1 is the small-gain certificate. gemini's "absolute, delay-independent stability" additionally conflicts with the paper's "without a delay-uniform decay rate being claimed." |
| C2 | Categorical subcriticality | gemini's table: subcritical entry/exit ⟷ the paper's variant-dependent record | **Paper correct.** Gated Candidate A: both subcritical (+5.75×10⁻⁵, +3.55×10⁻⁴); ungated Candidate B lower crossing supercritical (−9.84×10⁻⁵, "hence no lower fold for that class"). Any v36 language must keep the variant scoping. |
| C3 | Structure: split into four papers (sol) vs one spine with tiers (qwen/sol2) vs narrow to fisheries (deepseek) | three-way | **None adopted.** The paper's actual position — one paper with a registered model family (§2.3), certification levels (§11.5), companion ecosystem already spun off (sampled-governance, flow-balance/scaffold, two-stage companions), stock-agnostic class with fisheries as motivating instance — is the defensible middle and the deliberate product of the owner's v31–v35 rounds. Restructuring is an owner decision; the audits' shared valid core (state the tier of each result) is already implemented. deepseek's "narrow to fisheries" additionally contradicts the stock-agnostic design coordinates the paper certifies. |
| C4 | Institutional lag = arithmetic sum (sol) vs composite phase (sol2) | two-way | **sol2 correct with a caveat** (serial discrete delays do add; non-additivity holds for filtered/parallel/adaptive components). The paper needs no change: §11.8(ii) keeps the single-lag limitation; E2 names the stages without endorsing either arithmetic. |
| C5 | Fold certificates: complete them (qwen Path A) vs downgrade (qwen Path B) | internal to qwen | **The paper already took both:** Path-B wording in §11.5(3)/§9.2 + Path-A registered as the first open theorem in §11.9 (Church–Lessard upgrade + continuum off-grid residual stage). |
| C6 | "Five-regime" phrasing | sol/qwen: rephrase as numerically-observed ⟷ paper: scoped noun phrase with inline caveats | **Paper's form stands.** The body already carries the full scoping (declared domain, tested histories, certification tiers); the abstract's compressed phrase carries both caveats in-sentence and was just rebuilt under the owner's 260-word cap. No change without owner direction. |
| C7 | Whether inter-review safety should be *computed* | gemini/qwen/sol/sol2 programs ⟷ paper's "not certified here" | **Paper's discipline stands.** Computing N_min(T_r), safe-cadence sets, or viability kernels is new science requiring its own certification — registered as future work, not smuggled into a revision. The audits themselves disagree on its priority (qwen: Phase 4 "essential"; sol/sol2: "ambitious"). |
| C8 | Abstract design | sol §18/qwen §14: five elements, fewer thresholds ⟷ owner's Task-91 cap | **Owner's cap governs.** v35's 258-word abstract already implements the five-element logic with the load-bearing thresholds and caveats. |
| C9 | Retitle | sol §17, qwen §14, sol2 §22 propose titles ⟷ frozen title | **No change.** The title is frozen across v31–v35; retitling is an owner decision, and sol's "formatting problems" premise is stale. |
| C10 | Empirical strategy | sol/qwen/sol2: comparative institutional-delay database ⟷ deepseek: identification makes it infeasible as stated | **deepseek's caveat is correct and already reflected:** the paper itself records the structured-search null result (no eligible unconfounded case among 30+ systems) and keeps the empirical programme prospective. The audits' database proposal is future work that must internalise deepseek's identification layers. |

---

## Part III — The already-implemented ledger (demand → v35 location)

| Audit demand | Where it already lives in v35 |
|---|---|
| Frame as governance-loop theory, not "another Hopf study" | Title, §1.1, abstract, §12 |
| Separate biological / institutional / review-cadence delays | §1.1 loop; §7 (maturation vs institutional); §8 (cadence); §11.7(ii) compartments |
| Sign, gain, cadence as design coordinates | §11.3 ("three coordinates"); Conclusion ("modulus, damping, phase placement, and digital implementation") |
| Sign alone does not suffice | Proposition 6.1; §11.1; §10 intro |
| Critical-gain / no-Hopf sufficient condition | Theorem 6.1; Theorem 10.1 (+ Halanay-type certificate, §10.2) |
| Even-parity stated precisely | Corollary 4.1 |
| Delay families (2πk), not "exactly two thresholds" | Theorem 4.1 clause |
| Periodic review is a hybrid system, not a discretisation | §8 opening; Theorem 8.1 |
| Exact vs Euler vs native-ZOH record | Proposition 6.2, Theorem 8.1, Proposition 8.1, scheme-dependence remark, consolidated table |
| Euler artefact labelled | §6.4, Remark 8.1, §11.3 first caution |
| Inter-review safety flagged as uncertified | §8 Governance warning; §11.3; §11.4 cod instance |
| ℓ₁ values + method + status | §5.2 (with the k-regularisation caveat) |
| Well-posedness: invariance, boundedness, continuation, smoothness scope | Theorem 2.1, Corollary 2.1, §2.3 floor-inactive checks |
| Fold certification tiers + open stages | §9 opening, §9.2, §11.5(3), §1.2(6) |
| Five-regime scoping to declared domain/tested histories | §9.2 regime definitions + Figure 1 caption |
| Cod = timescale grounding, not calibration | §11.4 (twice), §11.8(i) |
| Behavioural basis (misperception experiments; institutional design) | §1.1 (Moxnes 1998; Ostrom 1990), §11.1 |
| Generality = mechanism form, not thresholds | §11.3, abstract ("stock-agnostic… design coordinates"), §12 |
| Management translation of vocabulary | §11.3 table |
| Certification-level framework | §11.5 three-tier list, claim-by-claim |
| Parameter sensitivity windows | §9.5 (+ §11.5(2) policy caveat) |
| Identification not performed; coefficients latent | §11.8(i), §11.4, §9.5, §12; structured-search null result |
| Culling vs suppression: local invariance, global divergence | §2.3, §9.3, §11.7(iii) |
| Single-lag / single-memory limitation | §11.8(ii) |
| Scheme-dependence limitation | §11.8(iii) |
| Provisional global classification | §11.8(iv) |
| Maturation-delay analogue with life-history selection | §7, §11.7(i) |
| Early-warning indicators tied to mechanisms, capture ≠ fold | §11.6 |

---

## Part IV — Implementation plan (proposed **v36**, wave 19) — consolidation-only, owner-commission pending

The plan inherits the standing constraints: new version file only (never overwrite); all wave18 fail-loud gates inherited; math-span byte-fidelity vs v35; numeric discipline (no new numeric values — every number in the new sentences is reused verbatim from §5.1/§11.4/§9.5); frozen blocks byte-identical (title, keywords, references 36 entries, declarations, supplementary, figure block, abstract untouched at 258 words); three byte-identical tectonic builds; PyMuPDF + VLM verification; rejection list extended, not shortened.

### E1 — Cross-reference repair in §1.2 (accuracy defect found by this verification, missed by all six audits)

Two dangling references have been present since v31 (checked: §4 has only ever had subsection 4.1, in every version v3 through v35):

1. §1.2, contribution 4: `both crossings subcritical (Section 4.2)` → `both crossings subcritical (Section 5.2)`.
2. §1.2, contribution 4: `requires a sufficiently large mobilising weight (Section 4.4)` → `requires a sufficiently large mobilising weight (Section 5.4)`.
3. §1.2, contribution 5: `provably not a Hopf of the continuous system (Section 6.2)` → `provably not a Hopf of the continuous system (Sections 6.2 and 6.4)` — the artefact record itself lives in §6.4. (gemini's audit repeats the same stale "Section 6.2" pointer for the 2.3-yr artefact, which corroborates that the audits read the paper's own §1.2 rather than §6.4.)

**New permanent gate (cross-reference resolver):** every `Section N.M` string in the md must resolve to an existing `### N.M` heading (and every `Section N` to a `## N` heading), else fail-loud. This gate would have caught the v31 defect on day one.

### E2 — §11.8(ii) completion: name the delay stages the single lag compresses (sol's best item, grounded)

Current: "(ii) The delay is a single discrete lag; distributed delays and variable-time institutional lags require separate analysis."

Proposed: "(ii) The delay is a single discrete lag — a reduced compression of the observation, assessment, decision, deployment, and compliance stages that a multi-stage institution carries separately; the documented cod chronology of Section 11.4 (the annual assessment cycle, the 1992 moratorium decision, the 2024 reopening) is a record of such stages at management scale, and what the single lag absorbs is their composite timing, not any one stage. Distributed delays and variable-time institutional lags require separate analysis."

No new numeric values (annual, 1992, 2024 all already in §11.4); no additivity claim either way (adjudicated C4); pure consolidation of §11.4 + §1.1 into the limitation that owns it.

### E3 — §11.9 completion: parameter-box certification as a stated open task (qwen's genuine gap)

Append one sentence after the two registered open theorems: "A third stated open task is parameter-box certification: the interval enclosures of Section 5.1 certify the registered decimal parameter vector, and the one-at-a-time windows of Section 9.5 are not boxes — extending the interval-Newton stage from the point vector to declared parameter boxes is the upgrade that would carry the threshold statements from arithmetic precision to the policy robustness that Section 11.5 reserves to a sensitivity layer."

### E4 — §11.8(i) or §12 completion: the identification layer (deepseek's grounded core, one sentence)

Append to §11.8(i): "Identification is its own layer: different gain–delay–memory triples can realise similar observed harvest trajectories, so the institutional coordinates are latent structural parameters — separable only through exogenous variation or direct process measurement, not read off landings — and the functional form of the response law is identified, if at all, separately from its parameters."

This states no new model claim; it consolidates the paper's existing admissions (§11.8(i), §11.4, §9.5) into the explicit identification caveat the audits converged on. **Flagged for owner approval** as the only item with any new conceptual content; E1–E3 are strictly accuracy/consolidation.

### Explicitly rejected (with reasons — the rejection list for this round)

1. **The "Sign Separation Theorem" coinage and any sign-based restatement of Theorem 6.1** — mathematically false (Proposition 6.1).
2. **Categorical subcriticality language** — falsified by the ungated-Candidate-B supercritical record.
3. **Safe-cadence/viability/metrics computations (N_min(T_r), 𝒯_safe, welfare, closure frequency…)** — new science requiring its own certification; the paper's correct current stance is the §8 warning.
4. **Stochastic extensions, strategic/anticipatory users, endogenous signal manipulation, multi-actor models, legitimacy/compliance dynamics, normative objective functions** — future research programmes (deepseek's catalogue), not revision content; several would change the declared model class.
5. **Economic formalism (Π, W integrals, debt/capital-fixity equations)** — uncited in the audits; violates the no-unverified-import rule.
6. **New conceptual figures (governance-loop diagram, viability-bleed schematic, climate-drift figure)** — new display content; the figure block is frozen; the paper's austere one-figure design is deliberate.
7. **Restructuring/splitting/retitling/abstract redesign** — owner-level decisions colliding with the companion-ecosystem and registered-record design (C3, C6, C8, C9).
8. **Evidence-status letter codes; ten-level safety hierarchy; nine-principles list** — cosmetic relabelling of §11.5 and the existing caution chain; the paper's three-tier prose is the chosen resolution.
9. **Management reference-point formalism (B_MSY/B_lim HCRs), delay-decomposition tables with intervention columns, institutional-delay databases** — new modelling/empirical programmes (future work); the §11.3 translation table is the implemented equivalent.
10. **Coinages "phase-stabilisation trap", "viability bleed", "administrative hunting", "basin lock-in"** — the phenomena are the paper's own registered content in plain words; coinage without new content is decorative (the owner's Task-91 meta-commentary standard applies).

### Verification battery for v36 (wave 19)

- `make_v36.py`: four surgical edits (E1×3 anchors, E2, E3, E4-pending), each anchor count == 1, idempotent, v35 byte-identical on disk after the run; md battery: math spans byte-identical to v35 (empty whitelist); numeric multiset unchanged (zero new values — all E-sentence numbers pre-exist); heading skeleton unchanged; frozen blocks byte-identical; abstract word count 258 unchanged; **cross-reference resolver gate** (new); rejection strings zero-hit (inherited list + "Sign Separation Theorem", "viability bleed", "phase-stabilisation trap", "administrative hunting" as banned coinages).
- `build_latex_v19.py`: wave18 pipeline retargeted; tex-level numeric discipline vs v35 tex; the three corrected cross-references present in tex; three byte-identical tectonic builds; overfull count expected unchanged (10).
- `check_pdf_v36.py`: wave18 PyMuPDF battery + the corrected cross-references in the rendered text + §11.8/§11.9 completions rendered clean.
- `review_v36.py`: cross-version ledger vs v35/v34/v33/v32/v31 with the E-edit deltas declared (four sentence-level insertions, three in-place reference repairs); prior-version checksums frozen.
- VLM page verification: the Contributions page, the Limitations/Open-problems pages.
- Deliverable record: `humanizing audits/V36_CONSOLIDATION_IMPLEMENTATION_AND_REVIEW.md`.

---

## Part V — Honest residuals

1. **This round delivers assessment + plan only** (the Task-89 pattern); implementation of E1–E4 awaits the owner's commission, per the standing two-step protocol.
2. **E4 is judgement-laden**: the identification-layer sentence is the single item that adds conceptual content rather than repairing or consolidating; the owner may prefer to drop it and keep v36 strictly at E1–E3.
3. **The audits' biggest proposals are structurally unresolved by design**: the split/restructure/retitle family and the compute-safety family are recorded as adjudicated-and-rejected *for a revision round*, not as verdicts that the underlying research directions lack merit — several (parameter boxes, safe cadence, stochastic safety) are strong candidates for separately commissioned work with their own certification pipelines.
4. **The DOI substitution item remains blocked** on the owner-supplied DOI list (standing item since the v32 round; never guess).
5. The six audits demonstrably reviewed a **moving target** (several against pre-v31 text, qwen and deepseek partly against each other rather than the paper); any future audit round should pin the baseline version in the prompt to avoid the phantom-quote class of defect.

---

*Verification artifacts of this round: the reads/greps against `paper4_delay_dynamics_v35.md` cited inline above; baseline md5s recorded in the header. No paper file was modified in this round.*

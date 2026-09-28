# V45 — Theoretical Ecology out-of-scope rejection: adjudication and the four-venue transfer evaluation

- **Round:** Task 133, 2026-09-28. Trigger: the owner reports that paper 4 v41 ("Governance delay and the stability of harvested stocks: mobilising and protective feedback rules, and the review interval as a design parameter") was **rejected by *Theoretical Ecology* as out of scope**, with four Springer transfer suggestions: *Environmental Modeling & Assessment* (EMA), *Journal of Dynamics and Differential Equations* (JDDE), *International Journal of Applied and Computational Mathematics* (IJACM), *Operations Research Forum* (ORF).
- **Owner question:** "is that true?!!!" — i.e., is the out-of-scope call defensible against the paper's actual character and the journal's actual scope?
- **Baseline:** `arena agent 1/paper rewrites/paper4_delay_dynamics_v41.md` / `latex/paper4_delay_dynamics_v41.tex` (45 pp), submission package `submission_zips/paper4_delay_dynamics_v41_TE.zip` (sha256 `e0379e93a122cc58…`, the post-Task-116 build: funding declaration + Tehran affiliation verified present), supplementary `paper4_supplementary_v8.zip` (venue-neutral), cover letter `latex/COVER_LETTER_paper4_delay_dynamics_TE.md`.
- **Method:** every scope statement below was fetched from the journal's own aims-and-scope page on 2026-09-28 (records in the round's fetch set: `link.springer.com/journal/{12080,10666,10884,40819,43069}/aims-and-scope`; publishing-model lines from the journal home pages; OR-Forum APC context from Springer-Nature library-agreement lists). No impact factors quoted (standing discipline).

---

## Part I — the verdict on "is that true?!!!"

**Verdict: the rejection is a defensible scope-emphasis call, not a factual error — and it is not a quality judgment. It was also, in substance, anticipated by our own V37 evaluation.**

### I.1 What *Theoretical Ecology*'s scope actually says (verified 2026-09-28)

> "Theoretical Ecology publishes innovative research in theoretical ecology, broadly defined. Papers should use theoretical approaches to answer questions of ecological interest and **appeal to and be readable by a broad audience of ecologists**. Work that uses mathematical, statistical, computational, or conceptual approaches is all welcomed, **provided that the goal is to increase ecological understanding**."

followed immediately by the journal's named exclusion class:

> "**Papers that only use existing approaches to analyze data, or are only mathematical analyses that do not further ecological understanding, are not appropriate.**"

and, cutting the other way, a bridging clause:

> "Work that bridges disciplinary boundaries, such as the **intersection between quantitative social sciences and ecology**, or physical influences on ecological processes, will also be particularly welcome."

### I.2 The adjudication

The paper sits **exactly on the seam between the bridging clause and the exclusion clause**, and the editor weighed it onto the exclusion side:

- **For "in scope" (our V37 argument, which remains genuine):** governance delay *is* the quantitative-social-science/ecology intersection the bridging clause names; the Adamson & Hilker (2020, *Theoretical Ecology* 13, 425–434) delayed-knowledge resource-harvester precedent is real and was verified in V37 Part I; TE publishes population-management theory.
- **For "out of scope" (the editor's side, which is defensible):** (i) the exclusion clause names "only mathematical analyses that do not further ecological understanding" — a 45-page theorem-proof paper whose load-bearing sections (§4–§8: Hopf cubic, even-pairs algebra, Lyapunov coefficients, interval-certified enclosures, Moore–Spence/Krawczyk fold certificates, sampled-data monodromy) are dynamical-systems methodology applied to a *stylised, deliberately not-calibrated* three-state model can be read as precisely that class, with the ecological content illustrative rather than advancing; (ii) the scope's "readable by a broad audience of ecologists" requirement is one the certification apparatus visibly does not meet; (iii) the A&H precedent is a compact modelling paper — citing a precedent tradition does not settle where a 45-page mathematics-first manuscript sits on it.
- **V37 said so in advance.** The evaluation that recommended TE-first recorded, as caveats (a) and (b): "*a 45-page theorem-proof paper with a certification apparatus is heavier than TE's typical fare — A&H itself is a compact modelling paper*" and "*the mathematics-first sections (§4–§8) will read as unusually formal for some TE referees*." The desk decision landed exactly on the flagged risk. The recommendation was not wrong on the evidence available (the precedent and the bridging clause are real), but the risk it carried was realised.
- **What the decision is NOT.** An out-of-scope desk rejection is a *fit* judgment made (typically) without review. It says nothing about correctness, novelty, or quality — and the transfer suggestions themselves (four applied-mathematics/environmental-modelling venues) confirm what V37's own profile paragraph said the paper is: applied dynamical-systems mathematics with an environmental-management application. The paper should be *re-placed*, not revised in response.

**Practical consequences:** (i) no appeal — scope calls are editorial discretion and the paper genuinely lives on the seam; appealing costs weeks and signals misjudgment; (ii) nothing is lost by the transfer route, because a desk rejection carries no reviews anyway; (iii) no manuscript change is warranted for the re-placement decision — v41 stands.

---

## Part II — the four transfer venues, verified against the paper's profile

The paper's profile (V37 Part II, current for v41): DDE bifurcation theory + certified computation (interval Hopf enclosures, Krawczyk/Moore–Spence fold certificates) + sampled-data/hybrid monodromy analysis + global attractor numerics (five-regime topology) + a stylised fisheries-governance application with the northern-cod record; 45 pp; theorem-proof density with management translation tables; explicitly a parameterisation, not a calibration.

### II.1 Environmental Modeling & Assessment — **STRONGEST FIT; RECOMMENDED**

Verified scope (journal/10666, fetched 2026-09-28):

> "Environmental Modeling & Assessment will publish high quality papers on **all aspects of environmental problems that contain a significant quantitative modeling or analytic component, interpreted broadly**. … We invite models of environmental problems and phenomena that **utilise, in an original way, the techniques of ordinary and partial differential equations, simulation, statistics and applied probability, control theory, operations research, mathematical economics, and game theory**. Emphasis will be placed on **the novelty of the model, the environmental relevance of the problem, and the generic applicability of the techniques used**. Generally, papers should be written in a manner that is accessible to a wide interdisciplinary audience. However, Environmental Modeling & Assessment will also **provide a forum where researchers can publish a complete mathematical description of important environmental models together with the accompanying analysis and underlying assumptions**. Occasionally, **papers that are primarily theoretical will be accepted, provided that the results deliver conceptual insight into some environmental problem**."

Clause-by-clause against the paper:

| EMA scope clause | Paper 4 v41 |
|---|---|
| "environmental problems … significant quantitative modeling or analytic component" | harvested renewable-resource governance; a 45-pp analytic component |
| "ordinary and partial differential equations … control theory, operations research, mathematical economics" | DDE system; review interval as a sample-and-hold control; bioeconomic framing — the clause lists this paper's exact toolkit |
| "novelty of the model" | governance delay as the analysed delay class; the two-rule comparison; the review interval as a design parameter |
| "environmental relevance" | managed renewable resources; the documented northern-cod timeline grounds scales |
| "generic applicability of the techniques" | the framework is stock-agnostic by construction (§12) |
| "complete mathematical description of important environmental models together with the accompanying analysis and underlying assumptions" | this is *literally the paper's format*: 45 pp of statement–proof mathematics with explicit assumption registers, certification records, and declared open items |
| "primarily theoretical … accepted, provided the results deliver conceptual insight into some environmental problem" | intermediate delay stabilising the loop; the five-regime attractor topology; more-frequent-assessment-is-not-always-safer |

The sentence "a forum where researchers can publish a complete mathematical description of important environmental models together with the accompanying analysis and underlying assumptions" reads as if written for exactly the objection TE raised: EMA is the venue where the paper's *weight* is an asset, not a liability. Hybrid publishing model (no mandatory APC). **No manuscript changes are needed for an EMA submission — v41 stands as shipped.**

### II.2 Journal of Dynamics and Differential Equations — real but narrower; the conditional second

Verified scope (journal/10884, fetched 2026-09-28):

> "…high-quality, peer-reviewed original papers in the field of dynamical systems and differential equations, **especially those concerning the dynamics of differential equations and their discrete analogs**. **Special emphasis is given to theoretical studies proving new approaches and/or techniques** to higher dimensional or infinite dimensional problems, including those which appear in new and emerging areas of science."

- **The fit:** the paper's continuous-delay vs periodic-review structure is literally "differential equations and their discrete analogs," and the no-Hopf theorem, the Hopf cubic, and the Neimark–Sacker-type crossing are dynamics results.
- **The misfit:** the emphasis clause — "theoretical studies proving new approaches and/or techniques" — points at *general methodology*, whereas this paper proves theorems about a specific three-state governance family, with the certified-numerics apparatus (not a JDDE staple) doing the heavy lifting at the fold points. A JDDE referee pool can plausibly return "too applied, too system-specific."
- **The cost:** a mathematics-first repositioning (governance framing recedes to motivation) — the mirror image of what TE demanded in the other direction. This was Task-95's mathematics-first alternate ("JDDE for the DDE-theory community") and remains the right venue *if the owner decides the DDE-theory community is the target readership*.

### II.3 International Journal of Applied and Computational Mathematics — the safe fallback

Verified scope (journal/40819, fetched 2026-09-28):

> "…publishing original research that advances applied, computational, and numerical mathematics. … **Studies demonstrating innovative applications of mathematical techniques to real-world and interdisciplinary problems**. Original research articles presenting new analytical, computational, and numerical methods … Contributions that integrate theoretical development with computational or practical implementation…"

- **The fit:** the certified-computation layer (interval Hopf enclosures, Krawczyk certificates, validated monodromy) is squarely "computational mathematics"; the governance application is the "real-world interdisciplinary problem."
- **The trade-off:** very broad scope (lowest out-of-scope risk of the four) but the least targeted community of the three plausible ones — a general applied-mathematics readership rather than either the environmental-modelling community (EMA) or the dynamics community (JDDE). Choose if the goal is a low-friction, in-scope landing rather than a community.

### II.4 Operations Research Forum — weakest methodological fit; not recommended

Verified scope (journal/43069, fetched 2026-09-28):

> "…serves the Operations Research community by addressing a broad range of topics, perspectives, methodologies, and industry applications … The journal covers the entire spectrum of topics … including, but not limited to: Algorithms, Analytics, Artificial Intelligence, Computational Economics, Data Mining, Data Sciences, Discrete Mathematics, Financial Engineering, Forecasting, Linear Programming, Logistics, Optimization (Mathematical, Robust, Stochastic), Machine Learning, Management Science, Mathematical Programming, Networks, Scheduling, Simulation, Supply Chain Management, Sustainability, Theoretical Computer Science …"

- **The misfit:** "Sustainability" and "Environment" appear on the *applications* list, but the journal's center of gravity is OR/MS *methodology* — optimisation, simulation, scheduling, forecasting. This paper contributes no OR methodology; its DDE-bifurcation/certified-numerics machinery is methodologically foreign to that referee pool, and the "review interval as a design parameter" message, while decision-relevant, is not an OR contribution. Submitting it there risks a second mis-fit cycle.
- **Cost note:** OR Forum launched fully open access (2020) and its OA arm carries an APC (Springer-Nature library-agreement lists put it around €1.7–2.1k across recent agreement years — verify the current figure on the journal's fees page if ever needed). The home page's publishing-model line currently reads "Hybrid" (recently converted), so a non-OA route may exist, but the methodological misfit alone rules it out.

### II.5 Ranking

**EMA (clear first) > JDDE (conditional second — only if the DDE-theory community is preferred, accepting the repositioning cost) > IJACM (safe fallback) > OR Forum (decline).**

---

## Part III — the recommendation and the transfer mechanics

1. **Transfer to *Environmental Modeling & Assessment*.** The scope text matches the paper clause-for-clause, including the format clause that neutralises the exact objection TE raised. The desk rejection left no reviews behind, so nothing rides on the transfer mechanism — it is purely convenience (files carried over, submission partially pre-filled). The manuscript needs no changes for EMA.
2. **Materials shipped this round (all new files; nothing overwritten):**
   - `arena agent 1/paper rewrites/latex/COVER_LETTER_paper4_delay_dynamics_EMA_v1.md` — the EMA-aimed cover letter, house style; the quantitative claims are reused verbatim from the 17/17-verified TE letter (Task 100), so the grounding carries over; the venue hook is rewritten from the TE precedent argument to EMA's own scope clauses; suggested reviewers re-aimed (Hocherman; Adamson/Hilker; Bence/Brenden — all in or adjacent to the citation base, and all venue-appropriate for EMA's interdisciplinary pool).
   - `arena agent 1/paper rewrites/submission_zips/paper4_delay_dynamics_v41_EMA.zip` — the EMA-named package: the four payload files byte-identical to `paper4_delay_dynamics_v41_TE.zip` (tex, pdf, figure at both resolution paths — the Task-101 lesson), with a re-aimed README. For the transfer-portal route the files carry over automatically; this zip exists for the fresh-upload route and for archive symmetry with the TE package.
   - The supplementary package `paper4_supplementary_v8.zip` is venue-neutral and stands.
3. **If the owner prefers the mathematics to lead instead:** JDDE via the same transfer mechanism, accepting the repositioning cost (II.2) — that decision changes the cover letter, not the manuscript.
4. **Beyond the four suggestions (honest note):** the transfer list is not exhaustive. V37's second choice, *Bulletin of Mathematical Biology* (also Springer — requestable through the transfer route even though not auto-suggested, or fresh), remains arguably the best non-listed alternative if the owner wants the mathematical-biology community; *Natural Resource Modeling* (Wiley) and *Ecological Modelling* (Elsevier) remain V37's subject-first non-Springer alternates. None of these beats EMA's scope-text fit; they are recorded for completeness.

---

## Part IV — honest residuals

1. **The rejection notice itself was not seen.** The adjudication in Part I is scope-text-based. If the editor's notice names a specific concern (e.g., length, format, "primarily mathematical"), forward it — nothing in this record expects it to change the recommendation, but it should be archived with the V-series.
2. Venue author guidelines (length policy, citation style, supplementary policy) change; verify at the EMA submission portal before submitting. EMA's format clause makes the 45-pp length low-risk, but the portal checklist governs.
3. The OR-Forum APC figure is approximate (agreement-list range); it is recorded only to close out that option, not for use.
4. No impact factors quoted (standing discipline). No claims are made about relative selectivity beyond what the scope texts themselves support.
5. Verification artifacts: the 2026-09-28 fetch set for all five aims-and-scope pages (tool-results/venue_round/ of the session workspace) + the publishing-model lines + the Springer-Nature agreement-list hits for the OR-Forum APC context.
6. Standing owner-side items carried unchanged: the Zenodo deposit-title refresh; the JMCDA SI submission (deadline 2027-01-31); the lake-build gold-standard run.

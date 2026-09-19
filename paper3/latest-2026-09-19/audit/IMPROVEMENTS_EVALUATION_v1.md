# Evaluation, verification and strengthening of `p3 improvements.txt`

**Basis.** The current v49 shipped set was read, not just the abstract and introduction: the main article, the supplementary, Companion A (methods/software) and Companion B (standards commentary). Counts below are approximate where a markdown/math-excluding word count is used. No manuscript text was changed by this evaluation.

## Executive verdict

The attached memo is useful as an outside **positioning and accessibility review**, but it is not a reliable description of the current manuscript. It saw the abstract and introduction and then inferred that the paper is “almost purely formal”, lacks a worked example, lacks a practitioner procedure, lacks software/reproduction, and lacks applied material. Those inferences are false or materially incomplete:

- The article already has Sections 6.1–6.5 on the three depletion quantities and their application classifications; it gives actual G3P, phosphate and fisheries records, including the four-basin G3P values, the approximately 309-year phosphate reserve-life ratio, and the fisheries medians under both the selected and broad cohorts.
- Section 8 already contains registered templates for phosphorus, groundwater and bioeconomic harvesting. These are deliberately not advertised as calibrated case studies or forecasts.
- Section 3 already separates the three certification layers and the certification state. Companion A supplies the practitioner-facing input schema, eight predicate procedures, three solver programmes, failure readings, vintage protocol and reproduction bundle.
- The deposit contains executable reproduction exhibits and analysis records. Companion A explicitly says that the current code is a **reproduction exhibit, not a supported package**: no installation, API or test suite beyond printed assertions. That is why a software-journal recommendation is conditional, not automatic.
- The article is not short. It has 1,693 markdown lines, about 25,100 words through the Conclusion (excluding mathematics by a simple token count), 54 compiled pages, 64 numbered formal statements, 70 markdown table rows and no figures. The supplementary is about 8,500 words; Companion A about 4,500; Companion B about 4,000.

The memo's best contribution is therefore not “add a case study because there is none.” It is: **make the existing formalism and application records easier to enter, compare and use, and choose a journal whose length and readership can actually accommodate the contribution.**

## What is already present, what is genuinely missing

| Memo's diagnosis | Verification against v49 | Correct disposition |
|---|---|---|
| The paper is almost purely formal | False as stated. It contains descriptive public-data records, three application classifications, domain templates, a worked aggregation witness, data/code availability and two companions. It is nevertheless formal-dominant and does not contain a conventional calibrated case study. | Reframe as **formal framework plus bounded application records**. Do not call the records forecasts or full case studies. |
| The three depletion times need simple examples | Partly valid. Definitions 3–5, the comparison table, the uniform-drift propositions, the G3P table, phosphate ratio and fisheries pressure time already exist. What is missing is one compact, side-by-side reader-facing calculation using a common toy ledger or one clearly labelled existing record. | Add one crosswalk box/table; do not add a new empirical claim merely to satisfy the review. |
| Add groundwater, fisheries and mineral case studies | Partly already present. All three domains are in Sections 6.5 and 8, with explicit limits. What is absent is the narrative shape and decision output of a conventional case study. | Improve the presentation of the existing records first. Add a full case study only for a chosen target journal, with data, boundary, validation and policy decision specified in advance. |
| The certification layers need a practitioner recipe | Already supplied in Companion A: Protocol 1 input schema, Protocol 3 predicate battery, Protocols 4–6 programmes, status vocabulary, failure interpretation and reproduction bundle. | Add a short pointer/roadmap in the main article if desired; do not duplicate the companion's 4,500-word procedure. |
| The paper needs a diagram | Valid. The four shipped markdown documents contain no figure or TikZ diagram. | Add one restrained figure: typed compartments and donor-limited fluxes, service readout outside the conserved state, and the two failure routes (compensation and support-pool drawdown). It must not imply that a service is mass or that the three application records are one dynamical model. |
| The paper needs more non-compensatory/strong-sustainability literature | The core canon is already present: Martinez-Alier/Munda/O'Neill, Munda/Nardo, Ekins, Neumayer, Daly, Brunner/Rechberger and Fischer-Kowalski. Pollesch, Costanza, Godley/Lavoie and Dafermos are not currently in the main article. | Add only sources that support a precise new comparison. Do not bulk-cite names. The current non-compensation theorem must remain an algebraic result, not a claim that the literature proves the theorem. |
| The paper needs a formal weak/strong-sustainability proposition | The regimes are already defined in §1.1 and interpreted in the Conclusion. A theorem would require formal definitions of closure, throughput, substitutions, time horizon and admissible boundary flows that are not currently part of the result. | Do not promote the current conceptual synthesis to a theorem without adding those assumptions. A conditional operational definition or a clearly labelled sufficient-condition proposition is safer. |
| Add GitHub/software for Environmental Modelling & Software | The deposit has code, manifests, outputs and reproducible analysis records, but Companion A expressly disclaims a supported package, installation, API and test suite. | EMS is conditional. It becomes a serious target only after a user-facing implementation, tests, benchmark, input example, documentation, licensing and quantitative verification are added. |

## Journal-fit decision

### 1. Ecological Economics — conceptual fit, current form not submission-ready

The journal's official scope covers integrated ecological-economic modelling, natural-resource valuation, environmental accounts, critical assessment of economic/ecological paradigms, policy methods and case studies. That is a real intellectual fit. Its current guide, however, lists maximum lengths of 8,000 words for both “Methodological and Ideological Options” and “Analysis”; the present article is roughly 25,100 words through its Conclusion. See the journal's official guide: [Ecological Economics aims, article types and limits](https://www.sciencedirect.com/journal/ecological-economics/publish/guide-for-authors).

**Decision:** a credible first-choice venue only after a major compression or a deliberate article/companion split. The memo's “add more formalism” direction is not the priority for this target; **selection, compression, accessibility and ecological-economic stakes** are.

### 2. Journal of Industrial Ecology — strongest topical fit, but needs an outcome-facing version

The journal's official scope explicitly covers stocks and flows of material, energy and other resources, MFA, socio-economic metabolism, systems-based and methodologically novel research, and significant outcome-focused contributions: [Journal of Industrial Ecology aims and scope](https://link.springer.com/journal/44498/aims-and-scope).

The typed ledger, moiety discipline, double-counting rules and MFA references fit well. The risk is that the current paper asks the reader to move through a large theorem system without a single visual or compact material-flow application that demonstrates what changes in an industrial-ecology decision. The target-specific strengthening is therefore a crosswalk and one application record, not a wholesale new theory section.

**Decision:** probably the best subject fit if the author wants the material-accounting/MFA identity to lead. Ask the editor about the unusually long theorem-driven format before investing in a target-specific full rewrite.

### 3. Environmental Modelling & Software — conditional, not a current first choice

The journal's official scope is environmental modelling and software; its author-facing description expects model/software objectives, development, testing and evaluation, and clearly specified licensing/open-source access: [Environmental Modelling & Software scope](https://www.elsevier.com/journals/institutional/environmental-modelling-and-software/1364-8152).

The present bundle is reproducible but deliberately not a supported software product. A reproduction exhibit is not the same as a general implementation of the typed ledger. The memo is right that software would materially improve this route, but it understates the size of the work.

**Decision:** keep as a conditional route only if the author wants to build and maintain the software artifact. Do not add a GitHub URL as a cosmetic gesture.

### 4. Royal Society A / Interface — mathematically possible, strategically different

The formal statements could interest a mathematical or cross-disciplinary venue, but the paper would need a much tighter mathematical novelty claim, a reduced application narrative and a proof architecture aimed at that readership. The present combination of ecological accounting, public-data classifications, standards commentary and companion methods is not automatically a Royal Society paper.

### 5. Resource and Energy Economics, Ecological Indicators, JEM, PLOS ONE and Scientific Reports

These are not equivalent alternatives. The phosphate reserve classification is only one of three application records, so Resource and Energy Economics is a partial fit. Ecological Indicators is plausible if the classification framework is made into a clearly usable indicator-assessment method with a decision example. JEM and broad multidisciplinary venues would need a stronger empirical or policy result than the current descriptive classifications provide. These should be screened against the exact current author guidelines only after the author chooses the paper's centre of gravity.

## Recommendation-by-recommendation disposition

### 1. Position against SEEA, EW-MFA and stock–flow–fund work

This is the most valuable substantive recommendation, but it needs precision.

- The article already positions itself against MFA through Brunner & Rechberger, Eurostat and Fischer-Kowalski, and Companion B already explains what the accounting standards settle and what they leave open.
- The main article uses `SEEA` only once and does not give a compact mapping table.
- It does not explicitly position the ledger against ecological stock–flow–fund modelling or Godley–Lavoie SFC terminology.
- The suggested phrase “ecosystem services as observable readouts” must not be written as if SEEA treated every service as a stock. The official SEEA material distinguishes environmental/ecosystem assets and stocks from service flows and records both in a broader accounting framework: [SEEA 2012 official text](https://unstats.un.org/unsd/envaccounting/seearev/eea_final_en.pdf).
- The Eurostat document is a strong primary comparator for economy-wide MFA: the [2018 EW-MFA Handbook](https://ec.europa.eu/eurostat/documents/3859598/9117556/KS-GQ-18-006-EN-N.pdf/b621b8ce-2792-47ff-9d10-067d2b8aac4b) describes EW-MFA as an accounting framework for the physical interaction of the economy with the environment and the rest of the world.
- The suggested ecological SFF comparator is real and relevant, but the linked item is a 2015 preliminary draft by Dafermos, Galanis and Nikolaidi, not a standard: [ecological stock–flow–fund framework](https://www.postkeynesian.net/downloads/soas15/YD290515.pdf).

**Disposition:** author decision, not an automatic repair. If this comparison is chosen, add a one-page table with columns `framework / object recorded / boundary / what it certifies / what the typed ledger adds / what neither claims`. Do not silently use this new passage to resolve the two existing open UN reference items; the paper's decision whether those entries should be cited remains the author's at-submission call.

### 2. Make the three depletion quantities operational

The memo is directionally right but overlooks the work already done. Section 6.1 already provides the definitions and a question-by-question table; §6.5 then gives:

- G3P anomaly-persistence values of approximately 2.7, 7.9, 9.5 and 21.4 years for the four named basins;
- the USGS phosphate reserve-life ratio of approximately 309 years, alongside the resource-based comparison and its boundary conditions;
- the fisheries removals-only pressure calculation, including the selected-cohort median of approximately 1.8 years, the positive sub-cohort median of approximately 2.9 years, and the public-release broad-cohort comparison of 3.39 years.

The genuine usability gap is that a reader does not get one compact, side-by-side calculation with identical fields. The strongest addition is a single table or boxed exhibit:

| record | input object | computed quantity | unit | question answered | explicitly not answered |
|---|---|---|---|---|---|
| G3P | anomaly series, reference window, fitted trend | record-relative persistence index | years | when the fitted anomaly reaches the record minimum under the declared fit | physical aquifer exhaustion |
| phosphate | economic reserve class / annual production | reserve-life ratio | years | arithmetic size of the declared reserve class at the quoted rate | geological exhaustion or forecast |
| fisheries | SSB, reference biomass and current fishing mortality | removals-only pressure time | years | isolated gross-loss margin under the stated comparison process | demographic or population-model hitting time |

Use the existing values and source vintages. Do not add a synthetic “realistic” number unless it is labelled as an example and independently checked.

### 3. Non-compensatory aggregation and strong sustainability

The memo correctly identifies the paper's central ecological-economics audience, but it recommends several names as if they were all missing. The article already cites the key works that carry the actual argument: weak comparability, noncompensatory aggregation, critical natural capital and weak/strong sustainability. Add a source only where it changes the comparison or addresses a reviewer-visible gap.

The safe strengthened claim is narrower than “the framework operationalizes strong sustainability by construction”: the ledger **refuses cross-type substitution as a certification rule unless a declared conversion and admissible routing are present**. That is a formal property of the declared ledger, not a universal empirical proof that every strong-sustainability question has been solved.

### 4. Add a case study

A new case study is not needed to repair the reviewer's factual description. The paper already has three bounded application records and registered templates. A conventional case study would be a substantial new research contribution requiring:

1. a named system and data vintage;
2. a declared boundary and type structure;
3. parameter/data identification and uncertainty;
4. a comparison against a baseline method;
5. a decision or policy question whose answer changes under the typed ledger; and
6. a claim that stays within the paper's explicit non-claims.

If the author wants one, groundwater is the most natural accessibility example, but the current manuscript expressly says the two-pool groundwater model is not empirically identified. It must not be relabelled as an empirical case without closing that gap. The lower-risk improvement is to make the existing three records read as a **comparative application exhibit**, not to pretend they are calibrated case studies.

### 5. Make certification practical

Already done in the companion architecture. The main article needs at most a short “reader route” sentence:

> Declare the typed compartments and fluxes; construct and check the incidence operator; run the separately reported balance, conservation, positivity, admissibility, safety, service and closure predicates; then attach a vintage and a status to every empirical readout.

That is a navigation aid, not a second methods paper. Companion A already supplies the exact schema and negative-output semantics, including the important distinction between `not established`, `not applicable` and `refuted`.

### 6. Tighten the productivity-illusion narrative

This recommendation is valid, but the manuscript already distinguishes the arithmetic and dynamical senses in §1.1. The improvement should be editorial and visual:

- retain one compact definition of the arithmetic sense: a surplus masks a deficit in a scalar aggregate;
- retain one compact definition of the dynamical sense: observed yield is supported by drawdown of an unmodelled or slowly replenishing pool;
- add the proposed stock–flow schematic only if it can show the donor/support pool, throughput, yield readout and sink without suggesting that yield is itself conserved mass;
- move any extended policy interpretation to the discussion/target-specific version.

Do not add a third “productivity” concept or use the phrase as a forecast claim.

### 7. Weak/strong sustainability as a proposition

Do not turn the current synthesis into a theorem by re-labelling it. The manuscript has not yet defined the complete class of closure maps, substitution routes, boundary flows and throughput horizons needed for such a theorem. A rigorous future version could state sufficient conditions, but those conditions would be new mathematics and must be proved.

For the present article, the defensible strengthening is to label the weak/strong distinction as an **operational regime interpretation** and point to the exact ledger objects that determine it: declared conversion coefficients, closure capacity, donor limitation, boundary flows and componentwise barriers. That makes it useful without overclaiming.

## Source-quality audit of the attached memo

| Memo source or move | Finding |
|---|---|
| `revistes.ub` / `Audens` used to support the Ecological Economics fit | Not suitable as a journal-authority source. The search result identifies Audens as a student social-sciences/humanities journal that ceased publication in 2021: [UB journal record](https://revistes.ub.edu/index.php/audens/user/setLocale/it_IT). Use the target journal's official aims and author guide instead. |
| Springer DOI `10.1007/s11205-022-02886-w` | The DOI resolves to Ricciolini et al., “Assessing Progress Towards SDGs Implementation Using Multiple Reference Point Based Multicriteria Methods,” a relevant weak/strong composite-indicator study, not evidence for the scope of Ecological Indicators: [article record](https://link.springer.com/article/10.1007/s11205-022-02886-w). |
| Eurostat PDF | A sound primary/official comparator for EW-MFA; retain it, but cite the handbook by title, edition and DOI rather than by a bare link. |
| Post-Keynesian SFF PDF | Relevant conceptual comparator, but a 2015 preliminary draft; describe it as such and do not present it as a settled standard. |
| Scribd and generic link collections | Do not use for a central theoretical or standards claim when the official SNA/SEEA, publisher or DOI record is available. |
| “Add Pollesch/Mori/Costanza/Godley/Lavoie” | Verify the exact work and the proposition it supports first. A longer reference list is not a stronger positioning argument by itself. |

## Target-specific minimum viable revisions

### Route A — Ecological Economics

1. Choose “Methodological and Ideological Options” or “Analysis” only after checking the current guide; the listed maximum is 8,000 words.
2. Build a short core article around the typed ledger, one certification result, the aggregation obstruction and one comparative application exhibit.
3. Move detailed proofs, status inventories, data-vintage records and procedures to supplementary/companion material where the journal permits it.
4. Add one diagram and one policy-facing crosswalk, not several new empirical claims.
5. Keep the conclusion focused on ecological-economic significance: what a conventional scalar or reserve-life reading cannot certify, and what the typed record can certify.

### Route B — Journal of Industrial Ecology

1. Lead with the material-flow problem and the physical-accounting contribution rather than the full theorem inventory.
2. Add the one-page framework crosswalk and the comparative application exhibit.
3. Make the “what changes in practice” output explicit: boundary declaration, double-counting test, componentwise deficit, and status of the resulting time-like quantity.
4. Ask the editor about length and article type before doing a full restructure.

### Route C — Environmental Modelling & Software

1. Treat the supported ledger implementation as a separate deliverable, not as a URL appended to the paper.
2. Add a documented input format, installation, API/CLI, tests, solver requirements, example dataset, benchmark, failure fixtures, versioning and licence.
3. Quantitatively evaluate correctness, runtime and failure reporting against hand-checked examples.
4. Keep the current reproduction bundle as a provenance/reproduction layer; do not call it a supported package until the above exists.

## Acceptance checklist for the next revision

- [ ] One target journal selected; article type and word limit recorded from its current official guide.
- [ ] The three depletion records appear in one compact crosswalk with input, output, units, question and non-question.
- [ ] One figure shows the typed ledger, the readout layer and the support-pool/productivity-illusion distinction without conflating them.
- [ ] The main article points to Companion A for the exact procedure instead of duplicating it.
- [ ] Any SEEA/EW-MFA/SFF comparison is source-backed, bounded and treated as a new author decision; no open UN-entry decision is silently resolved.
- [ ] Any new case study has a data vintage, boundary, identification statement, baseline and policy decision.
- [ ] Weak/strong sustainability remains a scoped operational interpretation unless a new proposition is formally defined and proved.
- [ ] Software claims match the actual artifact: reproduction exhibit versus supported implementation.
- [ ] All new mathematical, numerical and descriptive prose is line-read and page-verified; no build-time normalization of reused mathematics.
- [ ] The package is rebuilt only after the author approves the content decisions, then the exact-path archive/blob check and sidecar digest check are rerun.

**Bottom line:** keep the memo's accessibility and positioning instincts; reject its inaccurate “nothing applied exists” premise; make one visual crosswalk and one practical reader route; treat a full case study, SFF/SEEA expansion, theorem promotion and software product as separate author decisions rather than automatic repairs.

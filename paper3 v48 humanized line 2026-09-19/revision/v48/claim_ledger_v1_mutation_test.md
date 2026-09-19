# Did the instrument see the defects planted in it?

The ledger’s headline is `0 contradicted: value` and `0 contradicted: causality`. 21 defects were written into a copy of the draft and the same `build()` was run over it, to find out whether that is a finding about the draft or a blind spot in the rules.


| planted | class | found under this heading | flagged, but filed elsewhere | not flagged at all | what the misses were |
|---|---|---|---|---|---|
| 3 | attribution | 1 | 0 | 2 | no flag; verdict supported (near-verbatim); no flag; verdict supported (reworded)
| 3 | causality | 1 | 0 | 2 | no flag; verdict supported (reworded); the edit made the sentence the deposit’s own wording, which the ledger excludes
| 4 | scope | 0 | 0 | 4 | no flag; verdict supported (near-verbatim); no flag; verdict supported (reworded)
| 3 | strength | 2 | 0 | 1 | the edit made the sentence the deposit’s own wording, which the ledger excludes
| 8 | value | 4 | 0 | 4 | no flag; verdict not a claim (signposting); no flag; verdict supported (reworded)
| **21** | | **8** | **0** | **13** | |


The three outcomes for a planted defect: the rule that owns that dimension raised it; a rule raised something on the row but filed it under another heading, which still puts the pair in front of the author; or nothing fired, which is the number that says how far the zero can be trusted. A row that reads `not flagged at all` after an edit which made the draft sentence identical to the deposit’s own wording is a limit of the test, not of the rules - those sentences are excluded from the ledger by design - and they are named in the list below the table.


## Every planted defect, and what came back

- **attribution** `D0114` (the citation to Feinberg, 2019 was stripped)
  - was: Its wiring is shared with reaction-network theory, where the signs in the stoichiometric matrix are themselves a conservation object (Feinberg, 2019).
  - became: Its wiring is shared with reaction-network theory, where the signs in the stoichiometric matrix are themselves a conservation object .
  - ledger said: `supported (reworded)`
- **attribution** `D0631` (the citation to Clark, 1990 was stripped)
  - was: In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock
  - became: In the open-access equilibrium of a single-species fishery , the bioeconomic equilibrium stock
  - ledger said: `needs check: attribution` — the sentence this one restates cites Clark, 1990; the draft dropped the source
- **attribution** `D0050` (the citation to Meadows, 1972 was stripped)
  - was: The systems-dynamics overshoot models raise the same aggregation question in a moving form (Meadows et al., 1972).
  - became: The systems-dynamics overshoot models raise the same aggregation question in a moving form .
  - ledger said: `supported (near-verbatim)`
- **value** `D0529` (the figure 2026 becomes 2063, which the deposit never states)
  - was: Rows marked with a dagger (†) are quarantined and must not be taken at face value: the Australia phosphate row dates to a pre-2026 reserve vintage (§6.5.3), and the Indo-
  - became: Rows marked with a dagger (†) are quarantined and must not be taken at face value: the Australia phosphate row dates to a pre-2063 reserve vintage (§6.5.3), and the Indo-
  - ledger said: `supported (reworded)`
- **value** `D0127` (the figure 2013 becomes 2050, which the deposit never states)
  - was: It is not the received distinction in the literature, which turns on whether natural capital can be substituted (Neumayer, 2013; Ekins et al., 2003).
  - became: It is not the received distinction in the literature, which turns on whether natural capital can be substituted (Neumayer, 2050; Ekins et al., 2003).
  - ledger said: `supported (reworded)`
- **value** `D0109` (the figure 2003 becomes 2040, which the deposit never states)
  - was: The same point is standard in mineral economics, where the reserves-versus-resources distinction has been central at least since Tilton (2003).
  - became: The same point is standard in mineral economics, where the reserves-versus-resources distinction has been central at least since Tilton (2040).
  - ledger said: `needs check: attribution` — this sentence cites Tilton, 2040, Srivastava & Vegi, 2061, which the deposit never cites at all
- **value** `D0555` (the figure 2026 becomes 2063, which the deposit never states)
  - was: at approximately 74,000,000 kt (74,000 Mt) of world reserves and 240,000 kt/yr of production (U.S. Geological Survey, 2026) this is approximately 309 years.
  - became: at approximately 74,000,000 kt (74,000 Mt) of world reserves and 240,000 kt/yr of production (U.S. Geological Survey, 2063) this is approximately 309 years.
  - ledger said: `needs check: attribution` — this sentence cites Geological & Survey, 2063, which the deposit never cites at all
- **value** `D0370` (the figure 1990 becomes 2027, which the deposit never states)
  - was: The boundary discipline this proposition fixes is the ecological-economics one of Daly (1990): depletion is not loss of matter.
  - became: The boundary discipline this proposition fixes is the ecological-economics one of Daly (2027): depletion is not loss of matter.
  - ledger said: `needs check: attribution` — this sentence cites Daly, 2027, which the deposit never cites at all
- **value** `D0108` (the figure 2024 becomes 2061, which the deposit never states)
  - was: Illakwahhi, Vegi and Srivastava (2024) show that influential "depletion within a century" estimates rest on single-source US Geological Survey data of questionable credib
  - became: Illakwahhi, Vegi and Srivastava (2061) show that influential "depletion within a century" estimates rest on single-source US Geological Survey data of questionable credib
  - ledger said: `contradicted: value` — the draft states 2040, which the deposit never states in any form
- **value** `D0161` (the figure 2004 becomes 2041, which the deposit never states)
  - was: Non-negative primitive fluxes connect compartments through a signed incidence matrix — the compartment-and-flow bookkeeping of material flow analysis (Brunner and Rechber
  - became: Non-negative primitive fluxes connect compartments through a signed incidence matrix — the compartment-and-flow bookkeeping of material flow analysis (Brunner and Rechber
  - ledger said: `excluded: shared verbatim`
- **value** `D0131` (the figure 1990 becomes 2027, which the deposit never states)
  - was: Natural regeneration is far slower, sometimes on geological timescales, and it is included for physical completeness rather than as a co-equal mechanism (Daly, 1990).
  - became: Natural regeneration is far slower, sometimes on geological timescales, and it is included for physical completeness rather than as a co-equal mechanism (Daly, 2027).
  - ledger said: `not a claim (signposting)`
- **scope** `D0096` (the condition `when it comes…` was removed)
  - was: The snap, when it comes, is sudden and total.
  - became: The snap, , is sudden and total.
  - ledger said: `supported (near-verbatim)`
- **scope** `D0012` (the condition `admissible flow can do…` was removed)
  - was: Third, an envelope theorem that bounds what any admissible flow can do, with a safety-barrier corollary.
  - became: Third, an envelope theorem that bounds what any , with a safety-barrier corollary.
  - ledger said: `supported (reworded)`
- **scope** `D0685` (the condition `conditional form is not an accident of a par…` was removed)
  - was: The conditional form is not an accident of a particular domain.
  - became: The .
  - ledger said: `excluded: shared verbatim`
- **scope** `D0206` (the condition `when its donor compartment is empty…` was removed)
  - was: Every primitive outflow must vanish or be limited when its donor compartment is empty, and a target-relaxation flux from a finite donor is admissible only after donor lim
  - became: Every primitive outflow must vanish or be limited , and a target-relaxation flux from a finite donor is admissible only after donor limitation is made explicit.
  - ledger said: `excluded: shared verbatim`
- **strength** `D0646` (the hedge `may` becomes `always`, where the passage hedges)
  - was: The identity is the one object both analyses may use without substantive duplication.
  - became: The identity is the one object both analyses always use without substantive duplication.
  - ledger said: `needs check: strength` — the passage hedges with ['may']; this sentence asserts without a hedge
- **strength** `D0629` (the hedge `may` becomes `always`, where the passage hedges)
  - was: The registered identification requirements for closing the gap are: geological geometry (aquitard depth and extent); multi-depth heads; pumping tests; tracer, isotope or 
  - became: The registered identification requirements for closing the gap are: geological geometry (aquitard depth and extent); multi-depth heads; pumping tests; tracer, isotope or 
  - ledger said: `excluded: shared verbatim`
- **strength** `D0122` (the hedge `may` becomes `always`, where the passage hedges)
  - was: Task two is non-compensation. Ecological economics has a thesis called weak comparability: the values that matter in environmental decisions may not be commensurable in o
  - became: Task two is non-compensation. Ecological economics has a thesis called weak comparability: the values that matter in environmental decisions always not be commensurable i
  - ledger said: `needs check: scope` — the sentence this one restates is conditioned by ['at the level of']; the draft states it unconditionally
- **causality** `D0664` (an association in the passage turned into an asserted consequence)
  - was: The mapping type for exact dynamic reduction is rejected.
  - became: Therefore, the mapping type for exact dynamic reduction is rejected.
  - ledger said: `contradicted: causality` — the deposit passage says ['corresponds to'], this sentence says ['therefore']
- **causality** `D0665` (an association in the passage turned into an asserted consequence)
  - was: The permitted relation is analogy for shared mechanism language, plus diagnostic reconstruction of omitted mass flows.
  - became: Therefore, the permitted relation is analogy for shared mechanism language, plus diagnostic reconstruction of omitted mass flows.
  - ledger said: `excluded: shared verbatim`
- **causality** `D0054` (an association in the passage turned into an asserted consequence)
  - was: The word "illusion" is doing real work here.
  - became: Therefore, the word "illusion" is doing real work here.
  - ledger said: `supported (reworded)`


## Reading

A miss is not automatically a defect in the rules: `strength` is judged against the draft’s paragraph, so a sentence whose neighbour still hedges is left alone, which is the deliberate choice that stopped the first version of this file flagging a third of its rows. Those misses are counted with the rest and labelled, so the number can be argued with.


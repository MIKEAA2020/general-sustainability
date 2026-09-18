# v37 journal-fit evaluation: adjudication of the owner-supplied five-venue analysis

- **Round:** Task 96, 2026-09-18. Owner directive: *evaluate* the supplied five-journal analysis — *Theoretical Ecology* (recommended first), *Bulletin of Mathematical Biology*, *Journal of Mathematical Biology*, *Ecological Modelling*, *Journal of Theoretical Biology* — against the paper's actual character, alongside the Task-95 ranking (JMB primary; Natural Resource Modeling; Mathematical Biosciences; Journal of Dynamics and Differential Equations; SIADS; `humanizing audits/V37_SUPPLEMENTARY_ALIGNMENT_AND_HUMANIZING_AUDIT.md`, Part IV).
- **Companion directive:** "why Adamson & Hilker not in reference list? should we cite it?" — answered in Part V with the verification record.
- **Baseline:** `paper4_delay_dynamics_v37.md` (md5 `f32ef08f15fc3fdfacdc041d6d15a51b`), 45 pp, 1 figure, 36 references (frozen v32==…==v37), abstract 258 journal words.

---

## Part I — the load-bearing factual claim, verified this round

The supplied analysis's central claim: *"This journal [Theoretical Ecology] has published almost exactly the kind of paper you are describing: Adamson & Hilker (2020), 'Resource-harvester cycles caused by delayed knowledge of the harvested population state can be dampened by harvester forecasting'."*

**VERIFIED TRUE.** The bibliographic record, established by web search on 2026-09-18:

> Adamson, M.W., Hilker, F.M., 2020. Resource-harvester cycles caused by delayed knowledge of the harvested population state can be dampened by harvester forecasting. *Theoretical Ecology* **13**, 425–434. doi:10.1007/s12080-020-00462-x (issue date September 2020).

Evidence (independent corroboration, five sources):
1. The Springer article page itself — `link.springer.com/article/10.1007/s12080-020-00462-x` ("by MW Adamson · 2020 · Cited by 5 — Cite this article. Adamson, M.W., Hilker, F.M. … Issue date: September 2020. DOI: https://doi.org/10.1007/s12080-…"). The `12080` prefix is *Theoretical Ecology*'s journal code.
2. Hocherman (2025), "Time lags in environmental governance: a critical review," *Ambio* — cites it in full: "… dampened by harvester forecasting. *Theoretical Ecology* **13: 425–434**."
3. Scilit — "Matthew W. Adamson … Published by Springer Nature in *Theoretical Ecology*."
4. ORCID (Frank Hilker) — the 2020 *Theoretical Ecology* entry on the author's record.
5. A Cambridge University Press book bibliography ("*Theoretical Ecology*, Vol. …").

So *Theoretical Ecology* demonstrably publishes delayed-knowledge resource-harvester dynamics — the exact modelling tradition the supplied analysis names. Two corroborating observations:
- Hilker's group also published "Threshold harvesting as a conservation or exploitation tool" in *Theoretical Ecology* (2020, doi:10.1007/s12080-020-00465-8) — harvesting-control dynamics is a recurring topic there, not a one-off.
- The paper already stands in the same literature: the supplementary's governance-lag anchor (Hocherman 2025, *Ambio*) itself cites Adamson & Hilker — the governance-lag conversation already touches this work.

**The one sub-claim NOT verified this round:** "Bulletin of Mathematical Biology … has also published work on delayed knowledge and resource-harvester cycles." Searches returned bioeconomic fishery-delay models generally, not a specific BMB delayed-knowledge precedent. This is not load-bearing: BMB's documented scope (bioeconomic/resource models with delay, effort constraints) covers the paper regardless. Recorded as unverified-but-immaterial.

---

## Part II — per-venue adjudication (against v37's actual character)

The paper's profile: DDE bifurcation theory (Hopf cubic, even-pairs algebra, Lyapunov coefficients, a no-Hopf theorem) + certified computation (interval Hopf enclosures, Moore–Spence/Krawczyk fold certificates at the discrete level) + sampled-data/hybrid monodromy analysis (exact held-measurement monodromy, Neimark–Sacker-type crossing) + global attractor numerics (five-regime topology) + a stylized fisheries-governance application with the northern-cod record; 45 pages; theorem-proof density with management translation tables; a separate supplementary file and (this round) a deposited code-and-records package.

| # | Venue | The supplied analysis's claim | Adjudication |
|---|---|---|---|
| 1 | **Theoretical Ecology** | "strongest fit … the natural home for a paper that treats governance timing as a dynamical parameter" | **ENDORSED as the first-choice target, with caveats.** The precedent is now verified fact (Part I), and the framing fit is genuine: v37's delay is institutional by construction — the title names "Institutional Feedback … the Review Interval as Control"; §1.1 (line 26) positions the delay as "the lag between the institution's observation of a decline and the response that finally acts on it"; §12 (line 808) draws the ecological-vs-institutional contrast explicitly. The two-rule comparison and the cod record speak directly to TE's renewable-resource-systems audience. **Caveats:** (a) a 45-page theorem-proof paper with a certification apparatus is heavier than TE's typical fare — A&H itself is a compact modelling paper; the length policy and supplementary policy must be checked at submission; (b) the mathematics-first sections (§4–§8) will read as unusually formal for some TE referees — mitigable by cover-letter positioning and by the deposited package; (c) TE is a selective, lower-volume journal: expect a slower route. |
| 2 | **Bulletin of Mathematical Biology** | "strong fit … regular bioeconomic fishery models with delay … slightly broader than JMB in its tolerance for management and governance framing" | **ENDORSED as the strongest second.** Scope fit is real: long rigorous dynamics papers with electronic supplements are normal at BMB; the management framing is admissible; the five-regime topology and certified Hopf crossings match its methodological expectations. The specific delayed-knowledge precedent claim is unverified (Part I) but not needed for the fit. If the owner wants the mathematics to lead rather than the framing, BMB is arguably co-first with TE. |
| 3 | **Journal of Mathematical Biology** | "appropriate but less targeted … JMB's ecological papers typically treat delay as a biological delay" | **The critique is fair, and Task-95's JMB-primary ranking is revised accordingly.** The paper's delay is institutional, and JMB's delay tradition is life-history (maturation, recruitment — which is precisely the paper's *comparison* system of §9, not its subject). JMB remains viable with deliberate positioning (frame governance as a control layer on population dynamics, lead with the no-Hopf theorem, the discretisation artefact, the basin-boundary transition) — but that is a real positioning cost, and with the TE precedent now verified the framing argument outweighs the rigor-culture argument that drove the Task-95 ranking. |
| 4 | **Ecological Modelling** | "good fit if you foreground management … the practical message — more frequent assessment is not always safer — is exactly the kind of counterintuitive result that journal values" | **AGREED.** Long applied DDE models with sample-and-hold / periodic-review structure are in EM's tradition; the abstract's design message and §11.2–§11.4's translation layer suit its audience; the not-a-calibration stance is safer there than at any fisheries-science venue. Honest counterweight: the referee pool is more applied and less certification-oriented — the interval apparatus will read as unusual (admissible, but expect requests to soften §8). A strong subject-first alternative for reach into the management audience. |
| 5 | **Journal of Theoretical Biology** | "solid but generic … lacks the specific concentration of delayed-knowledge/resource-harvester papers" | **AGREED** — reliable venue, no specific precedent concentration; not the most strategic placement. |

---

## Part III — what the supplied analysis omits

1. **Natural Resource Modeling** (Wiley) — Task-95's #2 and *the strongest subject-community fit for the governance message*: mathematical modeling of renewable-resource management is the journal's literal scope, and §11.2–§11.4 (the practical reading, the translation table, the cod record) is exactly its audience. The supplied analysis does not consider it. Verify by recent issues whether the interval-certification density suits its norm before committing.
2. **Mathematical Biosciences / Journal of Dynamics and Differential Equations / SIADS** — the Task-95 mathematics-first alternates (JDDE for the DDE-theory community; SIADS if the sampled-data monodromy and certified global numerics should lead). Omitted by the supplied analysis, correctly so *if* the framing-first route is taken.
3. Both analyses implicitly agree on the exclusions: **fisheries-science venues** stay excluded (the paper's not-a-calibration stance; "Fisheries Research" and "ICES" are already banned strings in the rejection scanner) and **control-theory venues** stay reserved for paper2 (the companion already occupies the Automatica routes; portfolio diversification).

---

## Part IV — the reconciled recommendation

1. ***Theoretical Ecology* first** — the precedent is verified, the framing is native, and the readership is the interdisciplinary one the paper is actually written for. Submit with a cover letter that positions the contribution as the extension from *knowledge delay* (Adamson & Hilker 2020: delays in the spread of information about the resource state destabilise bioeconomic equilibria and induce harvesting cycles, dampened by harvester forecasting) to *institutional/governance delay* (this paper: the lag from observed decline to institutional response, with the review interval as a control variable) — and cite A&H in the paper itself (Part V) so the hook is visible.
2. ***Bulletin of Mathematical Biology* second** — if TE declines, or if the owner prefers the mathematics to lead.
3. ***Natural Resource Modeling* third (the omitted candidate)** — the subject-first alternative for the governance message.
4. ***Ecological Modelling*** — the management-foregrounded alternative; interchangeable with NRM in rank depending on whether reach (EM) or community fit (NRM) is preferred.
5. ***Journal of Mathematical Biology*** — viable with deliberate repositioning (governance as a control layer on population dynamics); JDDE/SIADS beyond that if the DDE-theory community becomes the target.

Practical notes: (i) verify each venue's current author guidelines at submission time (length policy, citation style, supplementary policy) — TE's length norms in particular; (ii) no impact factors are quoted, by standing discipline; (iii) the pending owner-level **retitle** could sharpen the fit either way (a governance-leaning title → TE/NRM; a DDE-leaning title → JMB/JDDE); (iv) this round's `submission_zips/paper4_supplementary_v6.zip` is the code-and-records availability package for any of these venues (Data-availability statement satisfied by a concrete, re-execution-verified deposit); (v) suggested reviewers for a TE route: Adamson and/or Hilker (the precedent authors), Hocherman (the governance-lag synthesis the paper already relies on), and an assessment-frequency author (Li/Bence/Brenden or Peterson) — all already in or adjacent to the paper's citation base.

---

## Part V — the Adamson & Hilker citation question (owner directive 4)

**Why it is not in the reference list.** Three reasons, all structural: (i) the 36-entry list was assembled in the v31/v32 rounds from sources actually consulted and verified in-session — A&H was not among them; (ii) the list is machine-frozen v32==v33==v34==v35==v36==v37 (review_v37 gate C1), so any reference change is a version-boundary event, never a silent edit; (iii) the standing rules — *no-unverified-import* and *never-guess-references* — blocked exactly this import when the batch-8 audits introduced "Adamson & Hilker" by name without bibliographic verification. This round's verification (Part I) removes that blocker.

**Should we cite it? YES — genuinely merited, non-decorative.**
1. **It is the closest methodological precedent.** Delayed knowledge of the harvested population state → destabilised bioeconomic equilibria and harvesting cycles, dampened by harvester forecasting — versus this paper's institutional response delay, two-rule comparison, and review-cadence control. The pair (their knowledge delay / our governance delay; their forecasting damping / our cadence design) is the exact novelty boundary of the paper.
2. **The natural anchor already exists.** §1.1 (line 26) is the lineage paragraph: behavioural misperception (Moxnes, 1998) → institutional design (Ostrom, 1990) → the field record (Hutchings and Myers, 1994; Walters and Maguire, 1996) → assessment frequency (Li, Bence, and Brenden, 2016; Peterson et al., 2022). The *delayed-knowledge modelling lineage is the missing link in that chain*, and A&H is its canonical recent statement. A second, optional mention fits §7 (their forecasting-damping result vs the review-interval-as-control finding) and/or §11.4.
3. **It strengthens a TE submission** (venue engagement — the precedent is that venue's own literature).
4. **One exactness item to re-check at commission:** the abstract's opening (line 5) — "Delays destabilise renewable-resource systems; those studied so far are ecological." With A&H cited, "those studied so far" spans knowledge delays too; the sentence remains defensible under the §12 reading (ecological = the biological-dynamics delays of delayed-logistic/delayed-recruitment analysis, contrasted explicitly with the institutional loop), but a v38 would re-check the phrase for exactness (e.g. "ecological or informational") — an owner decision at commission time.

**A second, related finding this round — the dangling Hocherman citation.** The supplementary (S4, line 73) cites "the Hocherman (2025) synthesis of 101 studies as a lower-bound proxy" for the response-lag distribution; the main text uses "the documented 2–13 yr governance-lag distribution" at three sites (§9.3 line 654; §11.4 line 764; §11.7 line 786) — but Hocherman appears in **neither** the main reference list (36 entries; verified zero matches in v37) **nor** any supplementary reference section (the supplement has none). Verified this round: Hocherman, T., 2025, "Time lags in environmental governance: a critical review," *Ambio* (Springer + PMC records; cited-by 31) — real and apt; volume/pages/DOI to be pinned from the Ambio record at commission time.

**The recommended v38 reference round (single commission, both citations):**
- Add **Adamson & Hilker (2020)** at §1.1's lineage paragraph (line 26), optionally echoed at §7/§11.4.
- Add **Hocherman (2025)** and cite it at the three "documented … governance-lag distribution" sites (§9.3, §11.4, §11.7), which simultaneously resolves the supplementary S4 dangling citation.
- References 36 → 38; the frozen-reference gates re-baselined (v38 == v37 + the two declared additions); the abstract's opening phrase re-checked for exactness; the full wave-pipeline battery re-run (make/build/check/review + VLM). Version discipline: new files only; v37 untouched.
- This is the same class of round as the v37 alignment repair: small, surgical, error-fixing. **Awaits the owner's word.**

---

## Part VI — honest residuals

1. The BMB delayed-knowledge sub-claim is unverified (Part I) — immaterial to the ranking.
2. Venue guidelines change; the length-policy concern for TE is real and must be checked at submission.
3. Impact factors deliberately not quoted.
4. The retitle and the DOI substitution remain the standing owner-level items; the Task-94 commission paths (parameter-box campaign, economics reading list) remain open.
5. Verification artifacts of this round: the web-search records quoted in Part I (URLs inline), `submission_zips/paper4_supplementary_v6.zip` + its README/MANIFEST/verification records, and the re-run `review_v37.py` ledger (ALL CHECKS PASS, 2026-09-18).

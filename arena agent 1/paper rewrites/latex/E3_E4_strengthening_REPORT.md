# E3 & E4 — Compliance Edits + Strengthening Plan

**Date:** 10 Sep 2026
**Target journal:** *Groundwater* (Wiley/NGWA) — both E3 and E4 are already formatted for it.
**Files edited:** `/home/user/gs_clone/arena agent 1/paper rewrites/latex/`

---

## Part 1 — Compliance edits (done, verified by recompiling)

### Abstract word counts (Groundwater limit = 250; you asked ≤265)
| Paper | Target | **After edit** | Status |
|---|---|---|---|
| E3 | ≤265 | **232** | ✅ |
| E4 | ≤265 | **259** | ✅ |

Verified from the **actual compiled PDF** (pymupdf text extraction between `Problem.` and `Keywords:`), not a crude text counter — authoritative for the journal. Both abstracts render in full with no truncation.

### Title (Groundwater limit = 100 chars)
| Paper | Original title | chars | New title | chars | Status |
|---|---|---|---|---|---|
| E3 | Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17 | 100 | *(unchanged)* | 100 | ✅ at cap |
| E4 | Governance operators and viability kernels of the Edwards Aquifer: an intervention-selection test at J-17 | 105 | **Governance operators and viability kernels of the Edwards Aquifer: a J-17 test** | 78 | ✅ |

The E4 retitle keeps both core concepts ("governance operators", "viability kernels") and the J-17 location, drops the long "intervention-selection test" tail, and parks it in a parallel form to E3's "…at J-17" title.

### Compile status
`rc=0` for both E3 and E4 after the edits.

---

## Part 2 — How E3 and E4 can be strengthened / broadened

Both papers are deliberately conservative, single-system, single-well studies. For *Groundwater*'s bar — **"theory with practical application; case studies accepted only if they add new information of general interest"** — the single highest-leverage move is to **elevate the transferable methodology/lesson above the case**, and to **test whether the findings are specific to J-17 or hold across the class of systems described**. Concrete, grounded suggestions:

### A. Make the generalizable contribution lead (both papers)
- **E4** already does this well: the Discussion frames the result as "system-dependent, not architectural" and cross-references the Northern-cod companion (E2) as the opposite end of the design space. **Push this to the abstract/implications.** Lead with the method — *an intervention-selection protocol (governance operators + robust viability kernels + declared-defect erosion + frozen retention rule) that scores any rule family against a fixed criterion* — with Edwards as the demonstration. That is Groundwater's "theory with practical application."
- **E3** currently reads as a single-basin forecast comparison. **Reframe the abstract to lead with the general lesson** — *deliberately simple process-based water-balance models are rarely tested against naive benchmarks under a locked retention rule, and here they lose to persistence because annual recharge is near-white; climatological baselines beat persisted recharge at long horizons.* Then J-17 is the concrete instance. This makes E3 a "research paper" (method + transferable insight) rather than a case study.

### B. Strengthen across multiple wells / systems (highest-value broadening)
- **E3:** the finding hinges on J-17's annual recharge being near-white. Add a **second well or a second aquifer segment** in a different recharge regime. If the naive-benchmark/persistence result *replicates elsewhere*, the "burden of proof on added structure" message becomes general, not well-specific. (The Edwards system has multiple index wells; the paper's own caveat notes the San Antonio Pool is "rapidly recharged, institutionally bounded" — a *contrasting* segment would test the recharge-whiteness mechanism directly.)
- **E4:** the trigger-design finding ("reactive rules are invisible to the kernel of their own trigger") and the "660-ft line is protected by wet years, not the pumping family" result would be far stronger with a **second threshold or second well** — showing the geometric property survives, or revealing it is specific to on-level triggers. Consider an analytical appendix on a **stylized trigger-based system** to show the geometric property generally, not just by example.

### C. Cross-system synthesis (leverages work already done)
- **E3 ↔ E1 (Northern cod forecast ladder):** same design, two very different systems (groundwater head vs. fish biomass), both yield "added structure rarely beats a naive benchmark." A short **"companion system" subsection** shows the lesson is not discipline-specific — a strong general-interest draw.
- **E4 ↔ E2 (cod intervention):** E4's Discussion already names the cod companion as the opposite end of the design space. **Make this a first-class framing**: the *framework* is the deliverable, demonstrated on two systems at opposite extremes. Frame the submission as presenting the general protocol.

### D. Harden robustness & address the reviewer-visible weak spots
- **E3:** the M2m model is the best one-step forecaster (12.28 ft, the only margin separating from noise) yet is *declined by a protocol class clause*. Add a **sensitivity/robustness analysis** showing the retention ordering is stable under alternate retention rules — this strengthens the method *and* broadens its value.
- **E4:** add a **sensitivity sweep of the interpolated 7.2% securing cut** across the declared defect and floor-class assumptions; the "nothing retained at 660 ft" and "certified claims limited to T≤3" boundaries are the natural place for a robustness table. Explicit "what-would-change-the-conclusion" bounds are valued by reviewers and add general insight.

### E. Practical/managerial bridge (Groundwater emphasizes practical application)
- Add a short **decision-focused paragraph** in each Discussion tying the result to what a manager actually does: for E3, *which forecasting tool to choose for annual vs. multi-year planning*; for E4, *which rule type to prefer under a drought-of-record and why the institutional (660-ft) threshold is not demand-manageable*. This directly serves the "practical application" requirement.

### F. Submission logistics (format/structure)
- **Designate the paper type explicitly** (Groundwater requires Research Paper vs. Case Study): submit **E4 as a Research Paper** (a methods paper applied to a real system) and **E3 as a Research Paper or Case Study** depending on how far you take the multi-well/cross-system broadening.
- Both already carry a **"Prepared in the format of Groundwater"** header and an **Article Impact Statement** — keep these; sharpen the Impact Statement to lead with the transferable message.

---

### Recommendation
Think of E3 and E4 as a **matched pair demonstrating a method on two opposite systems**, rather than two standalone single-system cases. If you broaden E3 to a second well / contrasting segment and elevate the framework in both abstracts, both clear the "general interest" bar as research papers rather than teetering as case studies.

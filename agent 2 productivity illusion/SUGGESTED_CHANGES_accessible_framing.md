# Suggested changes — v13 (FINAL: Composition title + sweep of my own versions)

**Status:** Recommendations only. **No manuscript, SI, or deliverable file has been edited.**
**Decision recorded:** title → **Composition** framing (over "Decline"), with **Drawdown** (not "Collapse").

---

## Part 1 — The chosen title, and the full propagation map

**Recommended title:**
> **How Aggregation Can Conceal Composition: Aggregate Biocapacity and the Identifiability of Modelled Ecological-Capital Drawdown**

Rationale: leads with the accessible idea ("aggregation can conceal"), uses the paper's own coined terms (aggregate, biocapacity, composition, identifiability), and replaces "Collapse" with the model-scoped "Modelled Ecological-Capital Drawdown" — avoiding the "overly speculative" charge. "Composition" is the exact methodological result (not the more sensational "Decline"). It also keeps the `\thanks{}` footnote.

**Because the paper's current title is cited in 5 places, renaming requires propagating ALL of the following.** I verified each:

| Location | Current value | Must change to |
|---|---|---|
| `manuscript_ECOMOD_v34.tex` line 34 `\title{...\thanks{...}}` | "…Two-Land Conversion and the Identifiability of Collapse\thanks{…}" | new title text, **keeping `\thanks{...}` verbatim** |
| `manuscript_ECOMOD_v34.tex` line 31 `\hypersetup{pdftitle={...}}` | "Emergent Carrying Capacity and the Composition Illusion" | new title text |
| `manuscript_ECOMOD_v34.tex` line 30 `pdfauthor` | Amin Abaee | unchanged (author unchanged) |
| `supplementary/ABSTRACT_submission.tex` lines 2–5 (comment header) | old title | new title text (comment only) |
| `deliverables/00_REVIEWER_RESPONSE.md` line 3 | old title | new title |
| `deliverables/INDEX.html` line 39 | old title | new title |
| `deliverables/01_BEFORE_AFTER_v34_vs_original.md` lines 10, 18 | old title | new title |

**Critical guardrail:** the title line in the manuscript carries the `\thanks{Data vintages and consistency...}` footnote (committed in `e00a50d`). A title swap that drops it silently deletes that note. **Keep `\thanks{...}` byte-for-byte.**

---

## Part 2 — Sweep of my own earlier versions (v1–v11): what still to implement

I reviewed my own accumulated recommendations. Here is the honest inventory, split by action.

### ✅ Worth implementing — as is (no correction)

| Item | From | Where it goes |
|---|---|---|
| **Recursive-identifiability paragraph** | v6–v12 | Discussion / §12.3 / SI §S5.3b |
| **Non-cropland cancellation caveat** (built-up offset; kept out of abstract) | v7→v8 (corrected) | §12.3 / SI §S5.3b |
| **SI table + two Total rows + Carbon/vintage footnote** | v10–v12 | SI §S5.3b |
| **Operationalise the policy rule** ("report component endpoint ratios, log contributions, attribution shares, data vintage, endpoint sensitivity") | v10 + Qwen v11 | §Policy extensions |
| **§1 empirical-grounding sentence** | v2–v12 | Introduction, after orchard |
| **§Policy extension plain line** (report the components) | v2–v12 | §Policy extensions |
| **Endpoint/path fix** ("non-cropland flat at the endpoint; intra-period index reaches ≈1.024") | v8–v12 | §12.3 / SI wording |

### 🔧 Worth implementing — after a correction

| Item | Correction needed | Result |
|---|---|---|
| **Abstract rewrite** | Must use "**annual index of bioproductive supply**" opening (not "ecological capacity"); evidence → mechanism → identifiability; close with not-a-forecast. Keep ≤300 words (final is ~250). | Final abstract in Part 3 |
| **Scalar-projection identifiability anchor** | Qwen's version omits that the weights are **convention-dependent**. | Corrected anchor in Part 4 |
| **§1 indicator-implication paragraph** | Combine "index, not a state variable" + corrected scalar-projection + composite citations (inline form). | Final in Part 5 |
| **Title** | Now decided: Composition + Drawdown. | Part 1 |

### ❌ From my own earlier versions — DO NOT resurrect

| Item | Why | Correct handling |
|---|---|---|
| **v7's "non-cropland ecological components declined −7.6%" as an abstract claim** | Over-reach; the −7.6% is an NFA *accounting-flow* net, not a measured ecological-capital decline. | Keep it as the body/SI **caveat only** (already in Part 2 "as is"). Never in the abstract. |
| **v2 "Abstract B" (~150-word lay summary)** | Not a journal abstract; reads as retreating toward "speculative." | Keep as a separate author summary / press note, **not** the submitted abstract. |
| **"How Aggregation Can Conceal Decline" (Decline) title** | More sensational; "Composition" is the exact result. | Superseded by Composition (Part 1). |
| **"who should act" map** | Mildly decorative for the paper itself; better as cover-letter framing than in the manuscript. | Optional; skip unless putting in cover letter. |

---

## Part 3 — Final abstract (corrected; ≤300 words; ~250 verified)

> Humanity's headline **index of annual bioproductive supply** — total biocapacity — is a single number built from heterogeneous land accounts: cropland, grazing land, forest products, fishing grounds, and built-up land. This paper asks whether that single number can conceal the composition of what is growing. It can, and the concealment is structural. From 1961 to 2022, global biocapacity grew about 23%, but measured land-type accounts show that this growth came almost entirely from cropland, whose biocapacity grew 2.85×, while the non-cropland book remained essentially flat at the endpoint. Over the same period, per-capita biocapacity fell by about half as population grew. A deliberately simple two-land model then makes the mechanism precise: conversion from ecological-capital land to provisioning land can raise the measured total while the model's capital book falls; the drawdown is demand-driven and approaches a floor rather than showing slow precursors; and recovery requires an explicitly gated restoration flow. The deeper point is measurement. Because aggregate biocapacity combines areas, yields, and equivalence factors, the aggregate does not identify its own composition; a rising total may reflect broad growth, fast-provisioning expansion, or offsetting changes among components, and these cannot be separated from the total alone. Identifying composition requires independent land-cover and yield data, and global sustainability indicators should therefore report components alongside totals. These results establish an identifiability property of aggregate biocapacity and a measured composition pattern for 1961–2022; they are not a forecast and do not show a measured decline in the model's ecological-capital book.

*(The opening is now "annual index of bioproductive supply," matching the manuscript's "annual flow, not a standing stock" at line 199. The non-cropland clause is endpoint-anchored. The stock/flow, analogue/identity, aggregate/vector distinctions are all respected.)*

---

## Part 4 — Corrected scalar-projection identifiability anchor (add to the indicator section)

> Aggregate biocapacity is a **scalar projection** of a vector of land-type components: it is a weighted sum over those components, with weights given by **convention-dependent** yield and equivalence factors. A scalar time series therefore cannot, without additional independent restrictions, recover the vector that produced it — and the projection weights are themselves modelling choices, not fixed constants.

*(Qwen's axiom, strengthened with the convention-dependence point it omitted. Adds rigor, no new claim, no new equation.)*

---

## Part 5 — §1 indicator-implication paragraph (final, inline citations)

> This has a direct consequence for how sustainability is measured. Aggregate biocapacity is an **annual flow index**, not a state variable and not a direct measure of ecological-capital stock: it combines land areas, yield factors, and equivalence factors into one number. The composite-indicator literature warns that in additive aggregation weights act as trade-offs, allowing a deficit in one dimension to be offset by a surplus in another (Nardo et al., 2008). Formally, aggregate biocapacity is a scalar projection of a vector of land-type components; without independent restrictions, the projection is not invertible. Biocapacity is exactly such a composite, so the same structural risk applies; reporting only the total can send a misleading policy signal (Becker et al., 2017; Fischer et al., 2022). The aggregate remains useful as a headline indicator, but only if its components are reported alongside it.

*(Uses the manuscript's inline citation form `(Nardo et al., 2008)` — **not** `\citep{}` — and the corrected scalar-projection anchor.)*

---

## Part 6 — The remaining insertions (as-is, from Part 2)

- **§1 grounding sentence:** "That this is not merely a theoretical possibility is the empirical core of the paper. In the measured National Footprint and Biocapacity Accounts, aggregate biocapacity rose from 1961 to 2022, but land-type attribution shows that this growth came almost entirely from cropland, whose biocapacity grew 2.85×, while the non-cropland book remained essentially flat at the endpoint. The two-land model then asks whether a still-rising aggregate could, under sustained demand, coexist with a declining ecological-capital book in a way the aggregate cannot detect."
- **§Policy extension line:** "The practical reporting rule is elementary: report the components alongside the aggregate. At minimum, report component endpoint ratios, log contributions, attribution shares, data vintage, and endpoint sensitivity. A growth headline for total biocapacity carries no information about whether fast-provisioning cropland growth is compensating for stagnation or offsetting changes in other components."

---

## Part 7 — The honest "what NOT to change" (final, consolidated)

1. Keep the **identifiability claim** and the new **recursive** form.
2. Keep the **separation** between NFA accounting categories and the model's A_c. **Never** write that the data measured ecological-capital decline.
3. Keep "**not a forecast**."
4. Keep the **NFA limitations** (no soil erosion, deforestation, groundwater degradation captured).
5. Keep **built-up land outside ecological-capital framing.**
6. Keep the **endpoint/path distinction** (do not return to "non-cropland stayed within 0.99–1.01× throughout").
7. Keep the **abstract ≤300 words** (final ~250).
8. Do **not** reintroduce meta/editorial labels ("this is the hard part," "an accessible reading," etc.).
9. Do **not** present the −7.6% NFA-flow net as an ecological-capital decline.
10. Use **inline citations**, never `\citep{}` (the manuscript has no natbib).

---

## Part 8 — What to actually apply (final, ordered)

1. **Title → Composition + Drawdown**, keeping `\thanks{}`, and propagate to all 5 cited locations (Part 1 table).
2. **Abstract** → Part 3 (corrected; ~250 words).
3. **Recursive-identifiability paragraph** → Discussion/SI.
4. **Non-cropland cancellation caveat** → §12.3/SI (not abstract).
5. **Scalar-projection anchor (corrected)** → indicator section.
6. **§1 grounding sentence + §1 indicator paragraph** (Part 5) → Introduction.
7. **SI table + Total rows + footnote** → SI §S5.3b.
8. **Operationalise the policy rule** → §Policy extensions.
9. **Endpoint/path wording fix** → §12.3/SI.
10. Update `ABSTRACT_submission.tex` (title comment + the abstract), since it's a separate submission file carrying the old abstract.

---

*No manuscript, SI, or deliverable file was edited. All numbers verified against the two NFA files. Decisions now locked: title = Composition + Drawdown; abstract = annual-index framing; recursive identifiability + corrected scalar-projection + SI Total rows + operationalised policy rule are the substantive additions. If you want, I can apply Part 8 to a copy of `manuscript_ECOMOD_v34.tex` (and a copy of `ABSTRACT_submission.tex`), preserving `\thanks{}` and updating `pdftitle`, then compile both.*

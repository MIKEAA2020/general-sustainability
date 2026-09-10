# Full Source-Content Reconciliation Audit — v34 vs. ALL Prior Sources

**Scope.** Compare the live manuscript `manuscript_ECOMOD_v34.tex` (two-land) against *every*
available source of record: the **original ECOMOD-26-1191 submission** (`/home/user/fulltext.txt`,
`/home/user/uploads/ECOMOD-26-1191.pdf`), the retained intermediate manuscripts
(v30, v31, v32, v33), the two Supplementary Information files (SI v1, v2), the figure-caption set,
and the audit/review/report tree. Target: **content loss, accidental condensation, and anything
worth restoring** — scientific content, expository/analogy material, tables, figures, citations.

---

## Executive verdict

The **scientific core is intact** and *not* condensed. The two-land model, its analytic results
(composition diagnostic `Δb_conv`, monotone `B_eq(A_c)`, `E_ceil≈1.138` floor collision, no-CSD
`≈−0.0537 yr⁻¹`, identifiability ladder), the National-Footprint aggregation decomposition, the
recovery/gate-sign asymmetry, the 7 falsifiable predictions, and the 5 labeled in-text tables are all
present and consistent with v30–v33 (the v33→v34 transition is a verified, loss-free editorial pass —
see `audits/v33_vs_v34_CONTENT_LOSS_AUDIT.md`).

**What *was* lost is in three buckets**: (1) **didactic analogies** (dropped at the v32→v33
restructure, not the v33→v34 edit), (2) **expository framing themes** (the weak-⇄-strong
sustainability reconciliation), and (3) **citations** (12 of the original's references no longer
appear). A fourth, smaller bucket is the **original's six-scenario curated table + six figures**,
which were replaced by a different one-stock comparator set rather than carried over.

None of these are scientific *errors* or damaged the results. Several are **genuinely worth
restoring** because they cost almost nothing and materially improve communication.

---

## Bucket 1 — Didactic / analogy content dropped at v32 → v33

These were present in v30–v32 but were removed during the restructure that produced v33/v34:

| Element | v30 | v31 | v32 | v33 | v34 | Verdict |
|---|---|---|---|---|---|---|
| **bank-account** analogy ("drawing down a bank account") | ✔ | ✔ | ✔ | ✘ | ✘ | **Worth restoring** |
| **elevator** analogy ("rated for ten, manages fourteen… the cable gives way") | ✔ | ✔ | ✔ | ✘ | ✘ | **Worth restoring** |
| **Tainter (1988) / Diamond (2005)** attribution for civilizational collapse | ✔ | ✔ | ✔ | ✘ | ✘ | **Worth restoring** (citation) |
| **strong-sustainability** term | ✘ | ✘ | ✘ | ✘ | ✘ | — (only ever present in the *original*) |
| **Liebig's Law of the Minimum** | ✘ | ✘ | ✘ | ✘ | ✘ | — (original only) |
| **apples** ("the apples from the orchard / apples harvested") | ✘ | ✘ | ✘ | ✘ | ✘ | — (original only) |

**The v32 wording worth restoring (verbatim, from v32 Introduction):**

> "The orchard also has an everyday analogue. A system can bear overload for a while — an
> elevator rated for ten people will still manage fourteen, showing little visible strain before
> the cable gives way — while its underlying integrity is quietly eroding. Judged by what it
> delivers (biocapacity, the harvest) the elevator still runs; judged by its reserve (the stock,
> the cable) it is already failing. This gap is the productivity illusion…"

This is the single most valuable didactic passage dropped. It takes the *conceptual* gap that the
paper's whole argument rests on and makes it concrete in one sentence. The v34 Introduction keeps the
orchard framing but drops this everyday analogue, so the *general* illusion (masking) is explained
only through the orchard, not through an intentionally unrelated image that clarifies the
mechanism.

Also worth restoring (v32 wording):

> "When the footprint exceeds biocapacity, an ecological deficit occurs, analogous to drawing down
> a bank account: the annual balance is a flow, but its cumulative effect erodes the underlying
> stock of natural capital…" — this is exactly the "flows vs. accumulation" convention that v34
> still states in §Model formulation, and the analogy makes it land.

**Note on scope discipline:** the v33→v34 editorial audit intentionally removed a rhetorical
trailing clause ("…so the question is not whether the index rises, but whether the trees are still
standing") from the Conclusions. That was a deliberate condensation decision, *not* an accidental
loss — do **not** restore it. The orchard-vs-fruit *concept* is retained; only the rhetorical
flourish was trimmed.

---

## Bucket 2 — Expository theme: the weak-sustainability ⇄ strong-sustainability reconciliation

The original's central expository result (Abstract, Discussion §5, Conclusion §6) was the
**formal reconciliation of the weak- and strong-sustainability paradigms:**

> "Technology can temporarily mask environmental decline by raising productivity faster than debt
> erodes it — the weak-sustainability regime… But this substitution is bounded: the irreversible
> accumulation of ecological debt and the limits of logistic regeneration reassert themselves over
> the long run — the strong-sustainability regime… The model does not take sides… It shows that
> both views are valid, but at different timescales."

In v34 this survives only as a single phrase in §Demonstration ("…the weak-sustainability index…")
and one clause in the Introduction ("…between those who hold that technology can always substitute
for natural capital and those who argue that substitution has hard limits"). The **reconciliation
framing and the "both views are correct, at different timescales" resolution are gone** (search
`reconcil` → 0, `strong-sustainability` → 0).

**Assessment:** Understandable, because v34 re-frames the result as the *composition* illusion
(identifiability of the aggregate), which is a distinct and more specific claim. But the
weak/strong reconciliation is **model-agnostic and still true** and gives readers a familiar
anchor. **Recommendation:** restore a short "reconciliation" paragraph (3–4 sentences) in §Discussion
or §Conclusions, keeping the existing composition framing as the primary result. This is *not*
contradicted by the two-land model — the substitution buffer (fast-land yield gain masking a falling
capital book) *is* the weak-sustainability mechanism operating at the book level.

---

## Bucket 3 — Citations dropped (original-only, 12)

Programmatic surname + author-year scan against v34 text and reference list:

| Missing from v34 | Original reference | Still relevant to v34's topic? |
|---|---|---|
| **Wilson, E. O. (2016). Half-Earth.** | §2.5 Policy extensions | **YES — v34 §Policy extensions is literally titled "Half-Earth & reservation" but never cites Wilson** |
| **Diamond, J. (2005). Collapse.** | §1 Introduction | Yes — collapses/civilizational decline |
| **Tainter, J. A. (1988). The Collapse of Complex Societies.** | §1 Introduction | Yes — same |
| **Motesharrei, S., et al. (2016).** | §1 Introduction (Earth System models w/ bidirectional feedbacks) | Yes — v34 talks about coupled feedbacks |
| **Donges, J. F., et al. (2017).** | §1 Introduction | Yes |
| **Calvin, K., & Bond-Lamberty, B. (2018).** | §1 Introduction | Yes |
| **Henderson, K., & Loreau, M. (2018).** | §1 Introduction | Yes |
| **United Nations (2022). World Population Prospects.** | §1 Introduction (exogenous-UN-projection critique) | Yes |
| **Haberl, H., & Aubauer, H. P. (1992).** | §1 Introduction; §4 numerics | Partly — historical DDE-population root |
| **May, R. M. (1973). Stability & Complexity in Model Ecosystems.** | §4/reference list | Borderline |
| **Pearl, R. (1925). The Biology of Population Growth.** | §2.3 population logistics | Yes — original source of logistic growth |
| **Shampine, L. F., & Thompson, S. (2001). Solving DDEs in MATLAB.** | §4 numerics | Yes — v34's numerics/verification section |

Note: v34 uses **Haberl, H., et al. (2007)** (a *different* Haberl paper — land-use/NPP) and
**Cohen, Meyer, van den Bergh, Motesharrei**-adjacent authors in places, so the *surname* alone is
misleading; the **author+year** identity above is the correct test, and these 12 are genuinely absent.

**Recommendation (highest value, lowest risk):**
- **Wilson (2016)** must be added — the "Half-Earth" section borrows its very name and concept from
  it, and citing it is a correctness/fairness matter, not mere polish. Add the citation to the
  §Policy extensions heading/body.
- **Diamond (2005) + Tainter (1988)** restore the civilizational-collapse grounding that v34 already
  asserts ("…societies can prosper for long periods while quietly undermining their productive base,
  only to suffer abrupt decline") but now makes without a citation.
- **Motesharrei (2016) / Donges (2017) / Calvin & Bond-Lamberty (2018) / Henderson & Loreau (2018) /
  United Nations (2022)** restore a literature paragraph v34 compressed to one clause.
- **Pearl (1925)** restores the logistic-growth attribution.
- The rest (May 1973, Shampine & Thompson 2001, Haberl & Aubauer 1992) are optional; add only if a
  host sentence returns.

---

## Bucket 4 — The original's curated six-scenario table + six figures

The original had a **single curated scenario table** with six contrast scenarios (A Sustainable,
B overshoot-no-lag, C env-lag-only, D both-lags, E technology-wave, F Half-Earth) and the numeric
final states/final max-Ω per scenario, plus **Figures 1–6** (M, P, K, Ω, D time series and the
`(τ_m, τ_p)` stability map).

**Status in v34/SI:** These were **replaced** by a *different* one-stock-comparator figure set —
S1–S13 (feedback diagram, macro-ratio plane, flow-share separation, delay-boundary cliff,
representative overshoot, masking window, recovery-vs-collapse, recovery insight, characteristic
spectrum, `a11` vs delay, sustainable-yield regimes, basin heatmap, basin delay response). The
stability-map concept survives as **S2** (basin in `R_B–R_A` plane) and **S9** (characteristic
spectrum). The regime table survives as **SI §S4.2**.

**What's genuinely not carried:**
- The **six-scenario comparison table** (A–F, with `M_final/P_final/D_final/max Ω`). The SI has
  separate parameter and regime tables (§S4) but not the single A–F contrast table with its
  half-Earth Scenario F row and its "debt repayment at η≥0.02 shifts collapse → oscillation" insight.
- The **Half-Earth simulation result** (`K_Half-Earth = 0.5 B / r_opt`; `M_HE=0.970, P_HE=0.243,
  Ω_HE=0.575`, "Scenario F prevents collapse"). v34's §Policy extensions discusses Half-Earth as a
  policy *concept* but has no numeric Half-Earth scenario/result.

**Assessment:** The six-scenario table is largely superseded — v34's demonstration uses a different
(computed) composition-illusion run and a flood-based floor-collision result instead. The one item
genuinely worth considering is the **numeric Half-Earth scenario**, because v34 has a Half-Earth
policy section and would be stronger if it carried the single quantitative Half-Earth outcome
(it is one line and directly supports the section). Optional, not required.

---

## What was NOT lost (verified intact) — do not touch

- **All 5 in-text tables** (`tab:regime`, `tab:conv`, `tab:basin`, `tab:neg`, `tab:ladder`) and
  Figure 1 (`fig:aggregation`) — present and referenced.
- **All 7 falsifiable predictions** and the prediction-to-section map (§S6).
- The **orchard / two-kinds-of-ground** framing (retained, in fact extended to two books).
- **Identifiability ladder** and the value-weighted-composite argument (Nardo, Becker, Fischer).
- The **one-stock comparator is retained in full** in SI §S1–S4 and its figures S1–S13, with an
  explicit "one-stock, not two-land" scope note. This is where v30–v32's robustness content lives
  now (`$b_G$` grid, `ρ`-independence, fast–slow validity) — it was **moved**, not lost.
- The **delay structure, debt equation, technology wave `T_b`**, and the **bounded-mask theorem**
  (debt compounds while technology saturates) — all in §Governing equations / §Falsifiable
  predictions.
- v30–v32's **"Robustness of the main results"** subsection content is folded into SI §S5.

---

## Priority-ranked restoration list (actionable)

**Do now (correctness / obvious value):**
1. **Add Wilson (2016)** to §Policy extensions and the reference list — the section's title and
   concept depend on it.
2. **Add Diamond (2005) and Tainter (1988)** to the Introduction's civilizational-collapse sentence.
3. **Add Pearl (1925)** to the population-logistics statement.
4. Add the **Motesharrei / Donges / Calvin & Bond-Lamberty / Henderson & Loreau / United Nations (2022)**
   cluster to the literature paragraph v34 compressed.

**Do if prose review supports it (high value, low risk):**
5. **Restore the elevator analogy** (one sentence pair) in the Introduction's "productivity illusion"
   paragraph, immediately after the orchard framing. Keep the scoped terminology (general
   *productivity illusion* vs. two-land *composition illusion*).
6. **Restore the bank-account / drawing-down** analogy next to the flows-vs-accumulation convention.
7. **Add a short weak-⇄-strong sustainability reconciliation paragraph** in §Discussion or
   §Conclusions, framed as model-agnostic and clearly subordinate to the composition result.

**Optional / leave as-is:**
8. Six-scenario table + Half-Earth numeric scenario — restore only if the Half-Earth policy section
   is to be quantitative; otherwise the current demonstration suffices.
9. May (1973), Shampine & Thompson (2001), Haberl & Aubauer (1992) — restore only if host sentences
   return.

**Deliberate — do NOT restore:** the rhetorical trailing clause removed from the Conclusions
("so the question is not whether the index rises, but whether the trees are still standing").
It was removed deliberately in the editorial pass (see the v33→v34 loss audit); the orchard/fruit
*concept* is retained.

---

## Method & evidence

- **Versions compared by structure**: v30/v31/v32/v33/v34 section outlines + the original fulltext.
- **Word/character guardrails**: the v33→v34 audit confirms a −1.0–1.1 % delta entirely
  attributable to removed change-log/self-referential phrasing, **no** whole-line deletions, and a
  word-level sequence-similarity of 0.9744.
- **Citation identity test**: author+year regex on v34 text and reference list; 12 of the original's
  ~26 references are absent.
- **Analogy-presence matrix**: `bank account` / `elevator` / `Tainter` / `apples` / `Liebig` /
  `weak-sustainability` / `strong-sustainability` counted across all five retained versions.
- **SI coverage**: confirmed the one-stock comparator robustness/figures moved into SI v2 §S1–§S7;
  the A–F scenario table and Half-Earth numeric result are not present there.

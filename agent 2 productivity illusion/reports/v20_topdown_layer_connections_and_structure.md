# Strengthening internal connections & structure with the added top-down layer (v20)

Scope. Q2 — how the manuscript's **internal connections** can be tightened now that the macro-ratio /
bookkeeping ("top-down") layer is in. Q3 — how that layer should reshape the **ideal structure and
presentation**. Each recommendation is mapped to a concrete edit at a named location. This is advisory;
nothing here is minted/pushed. (Q1 — the `eval` R@3 note — was resolved by strengthening §4.3's knife-edge
statement; see commit `7142b55`.)

---

## Q2 — Strengthening internal connections

The top-down layer's central object is **`R_B = 1`** (footprint = total biocapacity = the neutral family
`P = B(A)/e` = the basin separator = the §4.2 fold threshold). Today §4.5 states this; the sections it
unifies do not yet point back. Eight concrete cross-links:

| # | Link | What to add | Where |
|---|---|---|---|
| JL-1 | **§4.5 "one object, many faces" summary** | A 5–6 line block at the end of §4.5: "`R_B=1` is simultaneously (a) the bookkeeping trigger `dA/dt<0⟺E>B̃` [§2.2/§4.3], (b) the basin separator `P=B(A)/e` [§4.3, §8], (c) the §4.2 interior-MSY fold threshold when `b_Gρ>b`, (d) the target of prediction #8 [§6], and (e) the object whose *long-lag* failure is the §13(9) silent-collapse / measure-zero-rescue negative." | §4.5 (tail) |
| JL-2 | **ψ defined once, used twice** | Add a forward-ref at §3(B) and §2.2: "`ψ = bA*/B*`, defined here; its operational role (master parameter separating `R_A` from `R_B`, and locating the mask) is §4.5." | §2.2, §3 (B) |
| JL-3 | **Fold ↔ `R_B=1`, regime-scoped** | Make §4.5's fold note read as one statement with §4.1's regime table + §4.2's "scope it correctly": both say the fold/MSY exists **only when `b_Gρ>b`**; add "see §4.1/§4.2" to §4.5 and vice versa. | §4.1, §4.2, §4.5 |
| JL-4 | **`R_B=1` locus = neutral continuum** | In §4.3 (or §8 R2 note) add: "the `R_B=1` locus of §4.5 **is** the neutral continuum on which `D(0)=0`; the separator and the continuum are the same object." | §4.3, §8 |
| JL-5 | **§5 honest-rebuttal ↔ §4.5** | The §5 row "\"`E>bA` is the trigger\" → **No**, `R_B=1`" is exactly §4.5's trigger claim. Add "formalised in §4.5" to that row. | §5 (table row) |
| JL-6 | **Predictions ↔ §4.5** | Pred **#8** already cites §4.5. Add to **#5** (`ψ` locates the mask): "here `ψ` is the §4.5 master parameter"; to **#6** (`τ_g` sets recovery): "the necessary-but-not-sufficient reading of §4.5 — `R_B=1` is necessary, but not sufficient once `τ_g` is long." | §6 (preds 5, 6, 8) |
| JL-7 | **Macro-ratio numerics ↔ §8** | In the §8 A1/A5 bullet, add: "the `R_B=1` onset (`R_B=1.000`, `R_A=1.01–1.06`), the silent-collapse %, and the separator balanced-accuracy are all `topdown.py` (§4.5) and corroborate the R2 neutral-continuum / no-Hopf result." | §8 |
| JL-8 | **§13(9) ↔ §4.5 & §4.2** | Add explicit pointers: "silent collapse (36.5 %) targets prediction #8 (§6/§4.5); the measure-zero rescue set ties to the absorbing collapse §13(8)(v); the nonlocal-not-map cliff (AI-C6) is the *delay* crisis, distinct from the §4.2 `E`-fold." | §13(9) |

**Single highest-value move: JL-1.** It turns "the spine is in §4.5" into "the manuscript shows the spine is
one object," which is what makes the added layer read as a *unification* rather than an extra §.

---

## Q3 — Effect on ideal manuscript structure & presentation

The top-down layer is **bookkeeping/monitoring** content, which is a different *kind* of object from the
**dynamical** content (stability, Hopf↔no-Hopf, basin erosion). Reshaping around that distinction is the
single most informative structural change.

1. **Make the two-view structure explicit.** Label the analytic core as **two views of one object**:
   - §4.1–§4.4, §8, §13 — the *dynamical* view (regime, fold, neutral continuum, no-Hopf, basin crisis, negative results).
   - §4.5, §6, §13(9) — the *observable / monitoring* view (ratio safe-operating space, `R_A` leading-indicator, silent-collapse, class-imbalance-aware accuracy).
   Add one sentence at the start of §4 and twice in §7 didactics: *"the balance point is `R_B=1`; `R_A=1` is a leading but non-causal signal; when the regeneration lag is too long neither ratio warns — the lag, not the ratio, is the controlling variable."* (This is JL-1's headline reused as a thesis.)

2. **Tag each falsifiable prediction [dynamical] or [observable].** Represents the dual contribution without
   renumbering: predicate 1–3, 7 are dynamical; 5–6 straddle; **#8 is the observable/monitoring one**. This
   makes the "eight predictions" read as one coherent family in two registers. (Abstract already says eight.)

3. **Figure placement & captions.** Put `scans/topdown_macro_ratios.png` + `scans/topdown_ratio_separation.png`
   in §4.5, and `scans/topdown_delay_boundary.png` in §8 (it already is referenced there). Give each a caption
   naming the two-view role (e.g., the ratio figure "shows the `R_B=1` boundary as both separator and
   safe-operating boundary, and the `R_A>1` buffer").

4. **Receipt & attribution.** §12 already rows the macro-ratio result. Add one attribution row in the
   §13 tail's "attribution in an appendix": the §4.5/§13(9) top-down numbers come from the **corrected AI
   top-down (`model_sims/topdown.py`, Parts A–E)** cross-checked with **Lens-1/‑4** — cite as such, so nothing
   is claimed as novel that came from the AI/Lens analysis.

5. **Abstract phrase.** Insert one short clause after "no imaginary-axis crossing": *"the operating boundary
   is the biocapacity ratio `R_B=1`; the flow-yield ratio `R_A=1` is a leading, non-causal signal; and for a
   long regeneration lag neither ratio forecasts collapse."* Keeps the abstract's promise aligned with the
   now-eight predictions.

6. **Structure recommendation (risk-ranked).**
   - **Low-risk (recommended now):** keep §4.5 as a subsection, add the two-view label, JL-1 summary, an
     abstract clause, tags on predictions, and the figure/caption polish. Minimal renumbering (± no cross-refs break).
   - **Higher-risk (optional future):** split the analytic core into a *dynamical* section and a separate
     *bookkeeping/monitoring* section, and move §6 predictions into a single consolidated list. This is the
     "ideal" architecture but renumbers everything; it is best deferred until the §4.5/§13(9) content is
     judged stable.

---

## Summary
- **Q2:** eight concrete cross-links (JL-1…JL-8); the highest-value one is a §4.5 "one object" summary that
  names `R_B=1` as simultaneously the trigger, separator, fold, prediction target, and long-lag failure.
- **Q3:** reframe the paper as **two views (dynamical vs observable) of one object**, tag predictions by view,
  place figures by view, attribute the new numbers to their source, and add the headline thesis to §4/§7/abstract.
  Recommend the low-risk restructuring now; the full re-architecture can wait.

**Files:** this note (`reports/v20_topdown_layer_connections_and_structure.md`); v20 revision at
`data/revisions/IMPLEMENTED_revision_ECOMOD_v20.md` (commit `7142b55`). **No further mint/push made** — these
are recommendations; say the word and I'll apply them and re-verify/re-push.

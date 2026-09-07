# Line-Level Audit of ECOMOD v32 ("agent 2 productivity illusion")

**Task:** read v32 thoroughly at line level for flaws and internal inconsistencies (manuscript, data, revisions).
**Audited object:** `agent 2 productivity illusion/` at commit `ca70b4d` (ECOMOD v32) —
`data/revisions/IMPLEMENTED_revision_ECOMOD_v32.md` (1272 lines), `manuscript_ECOMOD_v32.tex` (592 lines),
`supplementary/SUPPLEMENTARY_information.md` (Rev-32 stamp), `reviews/VERIFICATION_of_tau_g_anchoring.md`,
`reviews/VERIFICATION_of_notation_and_math_audit.md`, `reviews/RESPONSE_to_reviewer.md`,
`data/topdown_results.json`, `data/r1_r2_sensitivity_results.json`, `reports/empirical_tau_g_sweep.json`,
`reports/empirical_tau_g_tau_p_grid.json`, `model_sims/` code.
**Method:** full line-level read of the v32 md; v31→v32 and v30→v31 diffs; md↔tex numeric-token parity
(Unicode subscripts accounted); every load-bearing number re-checked against the registered JSONs; the
model itself **re-run in-memory** (documented 13×16 grid, 6×8 COARSE_GRID, `corrected_basin_fraction`
default 23×28, floor-recovery t50/ρ sweep, failed-recovery A_peak); the four v32 empirical sources
web-verified. **Read-only:** no file in the agent-2 folder was modified (working tree clean throughout);
this report lives in a new folder, per the batch-7 audit convention.

Severity classes: **A** = v32-specific flaw (introduced by the v31/v32 revisions); **B** = carried-in flaw
(pre-v32, still live in v32); **C** = records/package hygiene. All md line numbers refer to
`data/revisions/IMPLEMENTED_revision_ECOMOD_v32.md`.

---

## Part 1 — Findings

### A1. [HIGH — data integrity] The v32 verification record's coarse-grid recover-fraction table does not reproduce, and it contradicts the manuscript's registered result

`reviews/VERIFICATION_of_tau_g_anchoring.md` §4 ("I ran the model ... at fixed τ_p = 25", "coarse grid,
baseline params") states:

| τ_g | 0 | 10 | 17 | 18 | 19 | 20 | 25 | 30 | 33 |
|---|---|---|---|---|---|---|---|---|---|
| recover | 0.54 | 0.54 | 0.54 | 0.54 | 0.51 | 0.21 | 0.00 | 0.00 | 0.00 |

These numbers are quoted **verbatim into the published SI §S5.1** ("coarse grid 0.54 at τ_g = 18 → 0.21 at
τ_g = 20 → 0.00 at τ_g ≥ 25"). I re-ran the repo's own tools on every registered grid/configuration:

| run (all τ_p=25) | τ_g=18 | 19 | 20 | 25/30 |
|---|---|---|---|---|
| documented 13×16 grid (`r1_basin`, dt 0.5 / T 1200) | 0.3942 | 0.2404 | 0.0529 | 0.0529 |
| 6×8 `COARSE_GRID` (dt 0.5 / T 1200 **and** dt 0.2 / T 2000) | 0.4167 | 0.2292–0.2500 | 0.1042 | 0.1042 |
| `corrected_basin_fraction` default 23×28 (dt 0.2 / T 2000) | 0.4115 | 0.1894 | 0.0326 | (not run to 25/30) |

No grid or integration setting reproduces 0.54 / 0.51 / 0.21 / 0.00; the record does not state the grid or
script that produced them. Worse, **"recover = 0.00 at τ_g ≥ 25" contradicts the manuscript's own
registered result** — the recover fraction at τ_g ≥ 20 is 0.0529 (11/208 cells; the rescue strip
A₀ = A_max with P₀ ≲ B(A_max)/e; §8 line 779, §12.1, `topdown_results.json` `rescue_set`) — which my re-runs
confirm. The error direction is uniform: the table overstates the recover fraction at low τ_g (0.54 vs
~0.40) and overstates the completeness of collapse at high τ_g (0.00 vs 0.053/0.104). Because the SI
presents these as model outputs, a reader takes away "nothing recovers beyond τ_g = 25", which the paper
elsewhere explicitly denies (measure-zero strip, §12.1). **Fix for v33:** re-generate the coarse numbers
from a stated grid with the registered code (or delete them from SI §S5.1 and the verification record,
keeping only the fine/registered values, which the SI already quotes).

### A2. [MODERATE] Prediction 6's forest clause is unsupported by the SI and mislabels the source

md lines 585–588: the empirically anchored band is "≈25–33 yr ... **with primary forests at the top of that
range** and many soils and (non-recovered) fisheries in or beyond it." But SI §S5.1 builds the 25–33 band
from **soils only** (17–23 yr → 1.44× → 25–33 yr) plus fisheries (≈20 → ≈29 yr); the forest statistic is
never converted into the band, and Poorter et al. (2016)'s median **66 yr to 90 %** of old-growth would map
to ≈95 yr under the same 1.44 heuristic — beyond, not "at the top of", 25–33. The soils, which *define* the
band, are described as "in or beyond it" (circular). And "primary forests" is wrong terminology: Poorter's
study is of **secondary**-forest regrowth (the paper's own SI table and verification record both say
"Tropical secondary forest"). **Fix:** rewrite the clause from the SI table (soils anchor 25–33; fisheries
≈29 with the non-recovered tail beyond; secondary-forest biomass recovery far slower, ≈66–95 yr effective).

### A3. [MODERATE] Reviewer response: "the anchored band brackets [the cliff]" is false; bullet 4 conflates the model's cliff with the empirical band

`reviews/RESPONSE_to_reviewer.md`, item (e) bullet 5: "the recover-vs-collapse outcome switches at the
≈18–20 yr cliff **that the anchored band brackets**." The anchored band is ≈25–33 yr; it lies entirely
**above** 18–20 and brackets nothing (only the reviewer's original, superseded 17–33 band straddled the
cliff — and the verification record itself correctly says the corrected anchor "lies at or above the
collapse threshold"). Bullet 4 of the same item says "The critical time scale — the regeneration lag that
flips recovery into collapse at ≈18–20 yr — is *not fitted* from the model; it is taken from independent
ecological field studies": the 18–20 yr cliff **is** a model output (§8 sweep), while what comes from the
field studies is the 25–33 yr value of the lag; as written it hands the model's own computed threshold to
the literature. **Fix:** "the ≈18–20 yr cliff, which the anchored band (≈25–33 yr) lies above" and split
bullet 4 into "threshold = model output; lag value = field-anchored".

### A4. [LOW-MODERATE] SI §S5.1's rate/lag caveat rests on a number the paper's own experiment contradicts

SI §S5.1: "the regeneration rate ρ ... sets *how long* recovery takes (the recovery timescale ≈ 1/ρ = 20 yr
at the baseline ρ = 0.05)". §12.2's own measured time to 50 % of A_max from the floor at ρ = 0.05 is
**142 yr** (my re-run from (A₀=0.02, P₀≈0.01): 141.2 yr; τ_g=10: 105.4 ≈ the table's 106). The e-folding
1/ρ is not the model's recovery time; the caveat built on "1/ρ = 20 yr" understates the measured recovery
time by a factor of ~7 and thereby understates how slow the ρ-lever actually is. **Fix:** state the
measured t50 (≈105–142 yr at ρ=0.05) alongside 1/ρ, or drop the "= 20 yr" gloss.

### A5. [LOW] SI §S5.1's fine-value sequence is misaligned with SI §S4.3's own table

SI §S5.1 pairs "(coarse 0.54 at τ_g = 18 → 0.21 at 20 → 0.00 at ≥25; reported fine values 0.399 → 0.240 →
0.0529)". SI §S4.3 (and §8) has **four** values — 0.399 (τ_g ≤ 17), **0.394 (18)**, 0.240 (19), 0.0529
(≥20). The three-value "fine" sequence omits 0.394@18, so juxtaposed against the coarse (18, 20, ≥25) it
implies fine@18 = 0.399, contradicting §S4.3. The verification record's parenthetical "(Reported fine-mesh
values in §S4.3 are 0.399 → 0.240 → 0.0529)" repeats the same misquote. **Fix:** quote all four values in
column alignment.

### A6. [CITATION] Neubauer et al. (2013) reference entry has wrong title and journal

md line 1193: "Neubauer, P., et al. (2013). *Resilience of recovering fish populations*. **Fish and
Fisheries, 14(3)**." The actual paper is Neubauer, Jensen, Hutchings & Baum (2013), "**Resilience and
recovery of overexploited marine populations**", ***Science* 340(6130): 347–349** (verified). The paper is
cited in §7 (line 645), §8 (line 753), §12.2 (line 999) and SI §S5.1. Also low-confidence: the H&R claim
"only 29 % of collapsed stocks recovered to 50 % within 5–15 yr" is not in the Hutchings & Reynolds (2004)
abstract, whose own quantification is "five years after collapse, 41 % of the 90 populations continued to
decline, 51 % exhibited some recovery, and 8 % had fully recovered" — the 29 % may paraphrase an internal
figure, but it is presented as the source's headline. (The Poorter 2016 and Poeplau 2011 readings were
verified faithful: 122 Mg/ha within 20 yr + median 66 yr to 90 %; SOC equilibrium after 23 yr
(deforestation) and 17 yr (grassland→cropland).) **Fix:** correct the Neubauer entry; source or soften the
29 % figure.

### B1. [MODERATE] "b_G ρ ⋚ b (equivalently ψ ⋚ 1/2)" — contradicted by the paper's own closed form (twice: §4.1 and SI §S2)

md line 322 ("The single testable condition `b_G ρ ⋚ b` (equivalently `ψ ⋚ 1/2`)") and SI §S2 line 86 ("the
two regime classes are separated at `b_G ρ = b`, equivalently `ψ = 1/2`"). By the paper's own closed form
(§4.5 line 479: ψ* = 2/(1 + b_Gρ/b)) — ψ* = 1 at b_Gρ = b and ψ* = 1/2 only at b_Gρ = **3b**; and the §4.1
regime table (lines 327–329) itself labels the marginal row "ψ → 1" and flow-dominated "ψ → 1", while §4.5
says the two ratios coincide at "ψ → 1 (baseline)". Under every reading the equivalence is wrong (b_Gρ ⋚ b
corresponds to ψ ⋚ 1, i.e. the boundary/marginal case is ψ = 1, where G(A_max) = 0). **Fix:** "(equivalently
ψ ⋚ 1, with ψ → 1 at the marginal/boundary case)" or drop the parenthetical; fix the SI line likewise.

### B2. [MODERATE] §4.3's "det = r·ρ·A*/A_max > 0 (never a saddle)" is false on the equilibrium family it linearises

md line 391 (and the same line in SI §S3.4): "det = r·ρ·A*/A_max > 0 (never a saddle) → zero-delay
condition is a₁₁ < r". At any point of the σ = 1 family P = B(A)/e the Jacobian is **exactly singular**:
a₂₁ = r·B′(A*)/e and a₁₂ = −e/b_G give det = a₁₁a₂₂ − a₁₂a₂₁ = (r/b_G)[B′(A*) − b − b_G G′(A*)] = **0** —
as the same section's own "D(0) = 0 on the whole family (neutral continuum)" (line 399) and the v31
verification's zero-delay polynomial λ(λ + r − S) (product of roots = det = 0) both already establish. The
*conclusion* survives (the non-neutral root is a₁₁ − r, so "a₁₁ < r" is right), but the "never a saddle /
det > 0" justification is mathematically false and contradicts the neutral-continuum result stated 8 lines
later. **Fix:** replace the det line with "the family is a neutral continuum: the zero-delay Jacobian has
det = 0 (one zero root along the family); the non-neutral root is a₁₁ − r, so the zero-delay condition is
a₁₁ < r".

### B3. [MODERATE] §8: "the collapse basin is robust (≈5 %)" — mislabels the quantity and the band

md line 760: "the collapse basin is robust (≈5 %) across the whole field-supported band." ≈5 % is the
**recover** fraction (the collapse fraction is ≈94.7 %); and under the section's own "Core band ≈ 10–40 yr"
(line 753) the recover fraction is 0.399 at τ_g = 10–17 — not ≈5 %. The sentence is only true if silently
re-read as "the recover basin shrinks to ≈5 % for τ_g ≳ 20". **Fix:** "the recover fraction is pinned at
≈5 % for τ_g ≳ 20 yr".

### B4. [MODERATE] §8: "The field-supported band lies entirely in the collapse regime" contradicts the same section's core band

md line 774 vs line 753: the field-derived **core band is ≈ 10–40 yr** (raw recovery statistics), of which
10–19 yr is the recovery regime (recover fraction 0.24–0.40); only the *effective* (1.44×) anchored band
25–33 yr lies entirely in the collapse regime. The section calls both objects "the field-supported band"
two paragraphs apart. **Fix:** name them distinctly ("the raw field band 10–40 yr straddles the cliff; the
effective anchored band ≈25–33 yr lies in the collapse regime").

### B5. [MODERATE] §12.2: "t50 ≈ 145/ρ yr" contradicts its own table

md line 1005: "the time to 50 % of `A_max` scales roughly inversely with `ρ` (t50 ≈ 145/ρ yr: 203 at
ρ=0.03, 142 at 0.05, 105 at 0.08, 82 at 0.12, at `τ_g=30`)". 145/ρ at ρ = 0.05 is **2900 yr**, not 142; at
ρ = 0.03 it is 4833, not 203. The table itself follows ≈ ρ^(−2/3) (a 4× ρ range gives a 2.5× t50 change;
least-squares on the table gives t50 ≈ const·ρ^(−0.65)), so even "roughly inversely" mischaracterises it.
The **table values are genuine** (I reproduce them from the extinction floor, P₀ ≈ 0.01: 141.2/105.4 at
ρ=0.05 vs 142/106 claimed). The same wrong formula has stood since the v18 report
(`reports/v18_recovery_ecology_insights.md` line 13). **Fix:** "t50 ≈ 145·(0.05/ρ)^(2/3) yr" (or
"t50·ρ^(2/3) ≈ const"), or simply quote the table and drop the formula.

### B6. [MODERATE] The demographic Hopf delay is stated as two different numbers

md line 667: "The leading Hopf delays are τ_g* = 85.4 yr and **τ_p* ≈ 231 yr**" vs md line 694 "τ_P ≈
**225** yr (slow ω ≈ 0.011 yr⁻¹)" and the comparison table (lines 716, 726): "τ_g*≈85, **τ_P*≈225**". The
same quantity is 231 in one bullet and 225 in two others (τ_g* is consistent: 85.4 ≈ 85). **Fix:** pick the
registered value and use it in all three places.

### B7. [MODERATE] §8's delay-response sweep (flat 0.0529 for τ_g 20–60) and §12.2's "delay-response non-monotonicity" (re-opening to 0.21–0.32) are two different curves under the same name, never reconciled

§8 (τ_p = 25): recover fraction 0.0529 for all τ_g ∈ [20,60] — **I re-ran it: 0.0529 at τ_g = 20, 30, 40,
50, 60 ✓** (also registered in `empirical_tau_g_sweep.json`). §12.2 (τ_p = 0 slice): "deep minimum at
τ_g=30 (≈0.03) and re-opens to ≈0.21 (40), ≈0.30 (50), ≈0.32 (60)" — also real (`r1_r2_sensitivity_results.json`
`grid_check`). But §12.2's bullet is headed "**The delay-response non-monotonicity** at τ_g ≈ 40–60 is
real, not a grid artifact" and never restates that it is the **τ_p = 0** slice, while §8's identically
named "Delay-response sweep" at τ_p = 25 is flat. The deep-τ_g re-opening is therefore τ_p-dependent to a
dramatic degree (0.32 at (60, τ_p=0) vs 0.053 at (60, τ_p=25) — a 6× effect) that the manuscript never
states, and which sits in unexplained tension with §8's "the cliff is not a τ_p artefact" (true for the
18–20 cliff, silent about the re-opening). A reader comparing §8's table with §12.2's numbers (0.053 vs
≈0.03 at τ_g=30) sees an unreconciled 2× discrepancy. **Fix:** scope the §12.2 bullet ("at τ_p = 0, the
recover fraction re-opens at long τ_g; at baseline τ_p = 25 it stays pinned at 0.053 — the re-opening is
τ_p-dependent") and reconcile the 0.053/0.027 difference explicitly (grid and τ_p both differ).

### B8. [LOW-MODERATE] §2.2's σ-prose contradicts Eq. (4)'s σ (σ·B vs σ·bA)

md lines 183–186 (the v31 notation block): "σ < 1 reserves a share **(1−σ)B** ... and σ is then set
together with the population cap so that **E ≤ σ·B**" — but the factor in Eq. (4) is **σ b A(t)** ("the
safe flow harvest", the very next sentence), and §4.3/§S3.3 (v31's own correction) say the reservation
"removes **(1−σ)bA** from the sustainable population". Reserving a share of the total biocapacity B and a
share of the flow yield bA are different policies (the former still permits liquidating capital growth);
the block conflates them. §9's "Cap the human-available flow at σ B" carries the same conflation ("flow"
and "B" in one phrase). **Fix:** make the prose read (1−σ)·bA and E ≤ σ·bA, or define the §9 cap as a
distinct policy on B.

### B9. [LOW-MODERATE] Dangling internal references to removed content

- md line 905: "**The 1961–2022 sentence** is a qualified observation" — no sentence about 1961–2022
  exists anywhere in v32 (grep: only lines 905 and 913); the sentence lives only in the reviewer's quote of
  the original submission. The response (d) tells the reviewer the claim is now "qualified rather than
  asserted", but the manuscript only *alludes* to it. **Fix:** state the qualified observation ("the GFN
  1961–2022 series shows biocapacity growing modestly while overshoot persisted; this is consistent with,
  but does not demonstrate, the illusion reading") instead of referring to a sentence that is not there.
- md line 813: "This removes the impossible '`Ω = 0.575`, `D = 0`' pair" — refers to an artifact of a
  pre-v30 computation no longer present in the manuscript.

### B10. [LOW-MODERATE] Undefined symbols in the final text; unresolved directive register in §8

- **Ω** is used (md lines 699, 811–814: "Ω peaks at ≈5.0 on D, ≈4.1 on E, clipped at 8.5", "Ω → 0.500")
  but never defined in the manuscript or the SI symbol tables.
- **r_opt** (md lines 424, 448, 814), **q** (424), **χ/Λ** (425–442) appear in §4.3/§4.4/§9 and SI §S2 but
  in no symbol table (§2.1 / §S1.2 gained a σ row in v31; r_opt never).
- §8's "Reporting rigour" bullet (md lines 688–699) is still written as author-directed imperatives —
  "(iii) Complete the scenario/parameter table...", "(iv) Analyse the trivial equilibrium (A,P)=(0,0) and
  the no-recovery region", "(v) Reconcile the 'max Ω not reported' footnote" — i.e. unresolved
  review-instruction register inside the submitted manuscript (the Ω footnote it says to reconcile is not
  reconciled; the trivial-equilibrium analysis is not present).
  **Fix:** define Ω, r_opt, q, χ, Λ in §2.1/S1.2; convert the §8 bullet to completed statements or delete
  the unresolved items.

### B11. [LOW] Small numeric/rounding and overstatement slips

- md line 1021: "`A_peak` = **1.21** (`τ_g=10`)" — the registered value is 1.2046
  (`topdown_results.json` `overshoot`), which rounds to 1.20 (the 15/18 values 1.25/1.28 are correctly
  rounded from 1.246/1.2819; "up to +0.08" ✓).
- md line 585 (prediction 6) and §12.2 line 1003: "recovery only for `τ_g ≲ 18`" — the paper's own sweep
  has recover = 0.240 at τ_g = 19 (a quarter of ICs still recover); "only" overstates the binary.
- md line 586: "≈25–33 yr ... **at or above** the collapse threshold" — the whole band is above ≈20; "at"
  is inapposite (minor).

### B12. [LOW] Reference-list formatting

Haberl & Aubauer (1992) and Gu, Niculescu & Chen (2005) are description-only placeholders (no
journal/volume/pages — "*(Application of the delayed-logistic framework ...)*", "*(Crossing-curve
formalism.)*"); Lin et al. (2018) and Wackernagel et al. (2002) lack article numbers/pages; Neubauer (see
A6) is wrong. The nine Abaee Zenodo entries are appended after Wackernagel rather than alphabetically —
this mirrors the owner's own ECOMOD-v30 treatment, so it is presumed intentional (noted, not flagged).

### C1. [RECORDS] The live manuscript pointer is 11 revisions stale

`data/IMPLEMENTED_revision_ECOMOD.md` is a symlink to `revisions/IMPLEMENTED_revision_ECOMOD_**v21**.md`
while `VERSION` says `revision=32`. The v11 convention ("live path is a symlink pointer to the latest
immutable version") was last honoured at v21; anyone following the live path reads the pre-finalization
baseline. **Fix:** re-point to v32 (one `git rm + ln -s`).

### C2. [RECORDS] `data/revisions/CHANGELOG.md` stops at v19

The "Revision / Master changelog" ends at revision v19; v20–v32 (13 revisions, including the two
mathematically load-bearing corrections of v31 and the anchoring of v32) are unlogged. Git commit messages
carry the record, but the in-package changelog contradicts the folder's actual contents.

### C3. [RECORDS] `supplementary/ABSTRACT_submission.tex` is two revisions stale and now contradicts the corrected abstract

It is still the Revision-30, 300-word abstract — i.e. it asserts, unscoped, "every interior point is
monotonically unstable (a positive real eigenvalue for every delay, with no imaginary-axis crossing)" —
exactly the claim v31 corrected with the σ = 1 and `b/b_G + G′(A*) > r` scoping (the v31 verification
record's own "Change made" list includes "The abstract now reads 'for the representative parameter set …
provided b/b_G + G′(A*) > r'"). The v32 md abstract (312 words by whitespace ✓, matching the v31 claim) is
the corrected one. The md's supplementary-material list (line ~1258) still describes the file as "300
words". Submitting the package as-is sends the unscoped abstract. **Fix:** regenerate
`ABSTRACT_submission.tex` from the v32 abstract and update the "300 words" description.

### C4. [REPRODUCIBILITY] Two of the three named drivers do not exist

The Reproducibility block (md lines 1244–1248) says the model is implemented by `model_sims/corrected.py`,
`topdown.py`, `r1_basin.py`, `char_eq.py` "(drivers `model_sims/_run_topdown.py`, **`demo_unified.py`**,
**`mask_rk4.py`**)"; §10 (line 847) says the demo figure is "generated by `demo_unified.py`". A repo-wide
find returns **no** `demo_unified.py` and **no** `mask_rk4.py`. The §10 masking-window result (5.4-yr
window at deficit 0.06, vanishing at 0.075, the 7,128-case scan) is therefore not rebuildable from the
package as committed. (All *other* referenced artefacts exist: the 8 `scans/*.png` figures, the two JSON
registries, the model_sims modules.) **Fix:** commit the two drivers or re-point the §10/Reproducibility
text at whatever produced the registered numbers.

### C5. [LOW] md↔tex: the deposit sentence exists only in the tex

`manuscript_ECOMOD_v32.tex` line 581 (Data availability): "A version of this manuscript together with the
supplementary package is deposited at `https://zenodo.org/records/22554480`" — no such sentence in the v32
md (nor v31/v30 md; inherited from the owner's v30 tex). The md↔tex numeric parity is otherwise exact
(every number in the tex matches the md once Unicode subscripts are accounted for; the v31→v32 tex diff
mirrors the md's two v32 hunks verbatim). Given the md is the version-of-record source, the package's own
deposit statement should be in both.

---

## Part 2 — What was checked and held (verified clean)

1. **§8 delay-response sweep table** (0.399 / 0.394 / 0.240 / 0.0529 at τ_g ≤ 17 / 18 / 19 / ≥20, τ_p =
   25): re-run on the documented grid — reproduces to 4 decimals; flat 0.0529 confirmed at τ_g = 20, 30,
   40, 50, 60; matches `reports/empirical_tau_g_sweep.json` (1-yr steps to 25, 5-yr to 60).
2. **τ_p-flatness** (§8): `empirical_tau_g_tau_p_grid.json` matches the text exactly (0.399@10–15 all τ_p;
   0.399–0.394@18; 0.2452–0.2692@19 = "0.245–0.269"; 0.0529–0.0577@20 = "0.053–0.058"); last recovering
   τ_g = 18 for every τ_p ∈ {0,5,10,15,20,25,40,60} (`topdown_results.json` `delay_cliff`).
3. **Failed-recovery A_peak** 1.31/1.45/1.60/1.88 at τ_g = 20/30/40/60: re-run — 1.3082/1.4504/1.5970/1.8818 ✓.
4. **Settling-overshoot series** and the §12.1 power law: the least-squares log-log fit of
   `topdown_results.json` `overshoot` (0.00383/0.01423/0.03831/0.06829 at τ_g = 10/12/15/18) is exactly
   **0.0047·(τ_g/10)^4.84** — the registered fit is genuine (only the 1.21 rounding slips, B11).
5. **t50/ρ table** (§12.2): reproduces from the extinction floor (A₀ = 0.02, P₀ ≈ 0.01): 141.2/105.4 yr at
   ρ = 0.05 vs 142/106 claimed (B5 concerns only the formula).
6. **Macro-ratio block** (§4.5): R_B = 1.000 onset with R_A = 1.01–1.06 across A₀ ∈ [0.30, 1.05] verified
   analytically (ψ(A₀) = 0.943–0.990); ψ*/R_A^eq closed-form samples (2→0.667/1.50; 37.5→0.052/19.25;
   150→0.013/75.5) and `flow_share_closed_form` JSON agree; fold↔R_B=1 check at b = 0.02 (A* = 0.900,
   B_max = E_sn = 0.0270) re-derived by hand ✓.
7. **Basin/separator block** (§12.1): 83/11 recover, 125/197 collapse, 72/197 silent = 36.5 % (and 1.6 % at
   τ_g=10), separator balanced 99.2 → 81.2, linear raw 94.7 % = majority class, map fixed points
   (0.15→0.283; 0.30→0.576; 0.50→0.986), Re λ 0.5917→0.6250 constant, recovery-overshoot power law — all
   match `topdown_results.json` exactly.
8. **Sensitivity tables** (§12.3): b_G table and fast–slow a₁₁ column (0.618/0.608/0.592/0.458/0.125) match
   `r1_r2_sensitivity_results.json` to the digit; a₁₁ = 0.625 − ρ/3 identity holds.
9. **v31 math corrections**: σ = 1 requirement (dA/dt = 0 forces G(A*) = G(A*) + (1−σ)bA*/b_G) — algebra
   checked; −a_E·a₄ = r·S identity checked; zero-delay λ(λ + r − S) checked; max F′(0) = −0.5883 at origin
   checked; S = 0.6083, a₁ = −0.0167 at A* = 0.8 consistent with ρ = 0.05, A_max = 1.2.
10. **Baseline regime arithmetic** (§4.1/§4.2): b_Gρ = 0.04 < b = 0.5; A_c(E) roots (0.283/0.576/0.986);
    B(A) = 0.54A − 0.0333A²; B(0.8) = 0.4107, P* = 0.7467 (v31 verification table) ✓.
11. **Masking-window internal consistency** (§10): B(0) = 0.578 with T_b(0) = 0.0712 ✓; peak rise 0.069 =
    0.647−0.578 ✓; A fall 0.142 ✓; 0.075/0.5 = 15 % ✓; abstract's "about five years" = 5.4 ✓.
12. **Abstract**: 312 words by whitespace ✓ (matches v31's claim; ≤ 315 ✓) — but see C3 for the stale
    submission-abstract file.
13. **md↔tex**: v31→v32 tex diff mirrors the md's two v32 hunks verbatim; numeric-token parity exact
    (modulo Unicode subscripts and front matter); the one content divergence is C5 (deposit URL).
14. **Nine companion Zenodo DOIs** (references): all nine present, each mapped to the correct paper
    (22545740 P1, 22554177 P3, 22552616 P2, 22554217 P4, 22554297 P5, 22552060 E2, 22553609 E1, 22553311
    E4, 22552680 E3), descriptor tails intact — consistent with the owner's v30 registry.
15. **Empirical sources**: Poorter 2016 (122 Mg/ha within 20 yr; median 66 yr to 90 % of old-growth) and
    Poeplau 2011 (new SOC equilibrium after 23 yr deforestation / 17 yr grassland→cropland) verified
    faithful to the sources — v32's two corrections were genuine corrections. (Neubauer entry wrong, A6;
    H&R 29 % unconfirmed, A6.)
16. **Non-destructive versioning**: v31 and v32 are new immutable files; v30 untouched; VERSION bumped
    correctly (revision=32); the v32 changes to the md are surgical (2 hunks: prediction 6, §8 empirical
    grounding) and were propagated to the tex and SI consistently.

---

## Part 3 — Recommended v33 fix list (priority order)

1. Regenerate or delete the unreproducible coarse-grid table in `VERIFICATION_of_tau_g_anchoring.md` §4
   and SI §S5.1 (A1) — highest priority: it currently contradicts the registered rescue-strip result.
2. Correct prediction 6's forest/soils/fisheries sentence from the SI table (A2) and the response's
   "brackets" sentence + bullet 4 split (A3).
3. Fix the three formula/label errors: "t50 ≈ 145/ρ" (B5), "equivalently ψ ⋚ 1/2" in both §4.1 and SI §S2
   (B1), "det = r·ρ·A*/A_max > 0" in §4.3 and SI §S3.4 (B2).
4. Reconcile §8's flat sweep with §12.2's τ_p=0 non-monotonicity (B7) and fix the "collapse basin ≈5 %"
   mislabel (B3) and the "field-supported band entirely in collapse" vs "core band 10–40" clash (B4).
5. Unify τ_p* (231 vs 225) (B6).
6. Records: re-point the live symlink to v32 (C1), append CHANGELOG v20–v32 (C2), regenerate
   ABSTRACT_submission.tex from the v32 abstract and fix its "300 words" description (C3), commit
   `demo_unified.py`/`mask_rk4.py` or re-point the Reproducibility text (C4), add the deposit sentence to
   the md (C5).
7. Citations: fix the Neubauer entry (A6); complete Haberl & Aubauer and Gu et al.; source or soften the
   H&R "29 %" figure.
8. Polish: σB→σbA in §2.2 prose (B8); state the qualified 1961–2022 observation instead of alluding to the
   removed sentence (B9); define Ω/r_opt/q/χ/Λ and resolve the §8 directive-register bullet (B10); A_peak
   1.21→1.20 and "recovery only for τ_g ≲ 18" softening (B11).

*Audit conducted read-only; no agent-2 file was modified. Re-runs were performed in-memory from the
registered code and grids.*

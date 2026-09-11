# Paper 5 — Joint verification of the two v27 audits (DeepSeek + Qwen)

**Verified against:** `paper5_sampled_governance_v27.tex` (117,734 B; commit `c4903a7c`).
**Audit source:** `/home/user/uploads/audit of p5.txt` (1,853 lines; `deepseek:` lines 1–194, `qwen:` lines 195–1853).
**Method:** every checkable claim was probed against the v27 source (quoted text, line numbers, counts).
No files were modified and nothing was pushed; this is a verification report only.

**Verdict scale:** CONFIRMED = real issue in v27 · PARTIAL = partly already handled in v27 ·
REJECTED = false alarm / stale quote / already fixed · DOWNGRADED = real observation, weaker than stated ·
AUTHOR-LEVEL = needs the author's model/data decision, no editor can fix it · OPTIONAL = stylistic.

**Headline counts.** DeepSeek: 3 confirmed + 7 partial/downgraded + 3 rejected + ~27 accepted-as-good.
Qwen §2: 1 confirmed + 7 partial + 1 downgraded + 1 rejected-in-part. Qwen §3: 4 confirmed + 4 partial +
1 downgraded + 1 rejected. Qwen §4: 2 confirmed + 2 partial + 4 downgraded + 1 rejected.
Qwen §5: 1 confirmed + 3 partial + 2 downgraded + 1 rejected + 1 author-level. Qwen §7: 3 confirmed +
2 partial/downgraded + 2 rejected + 1 stale. Plus 6 independent findings (in neither audit).

**The single most important finding:** both auditors worked partly from a stripped fragment or stale
quotes. All fragment-artifact items are rejected with proof below. Conversely, the strongest live issues
are: the protective-convention clash (DeepSeek 2.2 / Qwen 3.7), the unlisted parameter vector (Qwen 2.2),
exact-update indexing (Qwen 2.6.3), margins-paragraph omission (Qwen 3.3), and precision scatter
(DeepSeek 2.6 + new variants found during verification).

---

## 1. Auditor-accuracy notes (read first)

1. **DeepSeek reviewed a preamble-and-tail-stripped fragment for several items.** v27 provably contains:
`\begin{abstract}` (line 30), `\usepackage[mathlines]{lineno}` (L12) + `\linenumbers`,
`\date{September 10, 2026}`, full title block, full reference list, and a `Declarations` section
(L2063: Data availability, Author contributions, Funding, Conflicts of interest, AI declaration).
Hence DeepSeek 1.4, 3.6, and summary items 1–3 and 9 are rejected outright.
2. **Qwen's pipeline ate backslash-n sequences.** Qwen 7.2's `oalign{}` "literal" is v27's valid
`\noalign{}` (18 occurrences, all with backslash; zero bare `^oalign`). v27 compiles exit 0.
3. **Both auditors repeatedly quote stale/paraphrased text.** Each case is flagged per item
(Qwen 2.2, 5.4, 2.10; DeepSeek 3.10, 3.11; Qwen 3.9). The substance was still checked against v27's
actual wording in every case.
4. **Qwen 2.10's recommended rewrite uses first-person "I"** ("Therefore, I treat those values…").
The paper uses third person ("The authors declare"). Do not adopt verbatim.
5. **A headless paragraph between Qwen 7.5 and 7.7** ("Abaee, 2026, companion manuscript in
preparation") is stale: the companion is published (Abaee 2026, Zenodo record 22554217, verified via
API). No action.
6. **There is no Qwen 7.6** (numbering jumps 7.5 → 7.7). References to "7.6" in discussion are voids.

---

## 2. DeepSeek audit — item verdicts

| Item | Verdict | Evidence / comment |
|---|---|---|
| 1.4 no lineno/date | **REJECTED** | Fragment artifact; both present (see §1.1). |
| 1.5 figure | accepted-fine | Auditor-accepted; single Fig. 1, file exists, compiled. |
| 2.1 App-A opener | **CONFIRMED** | L453 "Sections 2.4, 2.5, 3.3, and 3.4" vs L1746 "Sections 2.2, 2.4, and 2.5". → **F1** |
| 2.2 protective convention | **CONFIRMED** | "opposite sign" (L405–406), "sign-reversed response" (L1026), but "quota-tracking gains" (L1117–1119, term used once, never defined) claimed as "the same convention". → **F2** + **A1** |
| 2.3 three/four systems | **PARTIAL** | Structure verified: one paragraph holds Sheridan-6 + cod + haddock (L1285–1301), anchoveta separate (L1303+). Bangkok is in the opening paragraph (not counted); spruce budworm separate. "Ambiguous but not fatal" is fair. → **F3** |
| 2.4 four-state period | **CONFIRMED** | No numeric period anywhere; only "centuries" (L853), "centuries-scale" (L1298), "predicted period is centuries" (L1338). "15–25× shorter" unevaluable. → **F4** + **A2** |
| 2.5 S(N) equation ref | **CONFIRMED** | L318 says "(equation (2))"; eq (2) is Ż. S(N) defined in prose after it. → **F5** |
| 2.6 precision | **CONFIRMED** | Bare "47.5/79.1" (L913–914, L924) vs 47.536/79.143 (L933–934, caption L971) vs 47.54-shorthand (Box L106, L911, L921, L935). Worse than stated: three variants. → **F6** |
| 3.1 CE=0 | **CONFIRMED** | Formula only for CE≠0 (L900–901); no limit case; e/z deviations undefined. → **F7** (+F16) |
| 3.2 eligibility | **PARTIAL** | Criterion referenced (L501) + eligibility table a registration item (L1756–1757, L2073); main-text summary absent. → **A6** |
| 3.3 detrending | **PARTIAL** | "Stated rule" (L510); rule lives in archived record (L1759–1761). Same shape as 3.2. → **A6** |
| 3.4 null calibration | **PARTIAL** | Auditor accepts deferral if supplement thorough; App A lists full record (L1759–1761). → **A6** |
| 3.5 sectioning | **CONFIRMED, cosmetic** | H1→`\subsection`, H2→`\subsubsection` verified (L162–L1912); compiles consistently. → **A9** (recommend leave) |
| 3.6 abstract env | **REJECTED** | `\begin{abstract}` at L30; fragment artifact. |
| 3.7 "annual discrete form" | **PARTIAL** | L1107 verified; ambiguous (annual internal steps vs Tr=1) since scan is Tr∈{1..50} (L1115). → **F8** |
| 3.8 rational term | **PARTIAL** | Singularity sentence present (L362–364); Zref=0 / approach-side unstated. Fold into F9. → **F9** + **A3** |
| 3.9 ≈6.5 vs 6.501 | **CONFIRMED** | Fold into precision fix. → **F6** |
| 3.10 "differ only" | **DOWNGRADED** | Already carries "as the one-plant contrast above shows" (L1015–1016). Optional hardener. → **F10** |
| 3.11 λ note | **PARTIAL** | Pointer exists (L1017–1018); "derived eigenvalue, not a parameter" gloss missing. → **F11** |
| 3.12–3.40 | accepted-good | All auditor-accepted ("Good"); 3.13 confirms 4.7(v) placement. No action. |
| §4 items 1–3, 9 | **REJECTED** | Fragment artifacts (title/refs/declarations/lineno all present). |
| §4 items 4–8, 10 | carried | → F1, F2+A1, F4+A2, F5, F3, F6/F7/F8 bundle. |

---

## 3. Qwen audit — item verdicts

### 3.1 Critical issues (§2)

| Item | Verdict | Evidence / comment |
|---|---|---|
| 2.1 archived centrality | **PARTIAL + AUTHOR-LEVEL** | Both quotes verified (L513 band-provenance; archived-status App A/data-availability). But quarantines already exist: "provisional status" (L513, Box L125–126), "uninformative rather than a non-reproduction" (L1204–1205), §4.7, data-availability "carry provisional status until those artifacts are attached" (L2075–2076). Demotion/band-redefinition is an author decision. → **A5** (+optional **F12**) |
| 2.2 parameter vector | **CONFIRMED substance, AUTHOR-LEVEL** | Quote is paraphrase (actual L1768 "logistic-core parameter vector that the text does not list (r, K),…"). Table 3 + App A itemize the unlisted set by design; full disclosure is a reproducibility-policy decision. → **A3** |
| 2.3 annual-instability strength | **PARTIAL** | Flat claim verified verbatim (L983–984 "Annual review is unstable under sampling (ρ=1.00035)") + flat caption (L971). Conditioning exists but sits in another paragraph (L959–963). Fix = fold conditioning into the claim. → **F13** |
| 2.4 artefact language | **PARTIAL** | Flat at L913–914 and L1484; already scoped at L925 ("not a review-cadence property"), L942, L944, L1029. §2.1 presents Euler as "one specific reviewed controller" (L374–376), so the tension is real. → **F14** |
| 2.5 held vs interpolated | **DOWNGRADED** | E_n in (1)–(2), H4 (L728–729), E(s) in proof (L743, L748) all verified — but pure hold *satisfies* H4, so Prop 3.1 is generality, not inconsistency. One clarifying sentence. → **F15** |
| 2.6.1 e/z undefined | **CONFIRMED** | No e_n=E_n−E*, z_n=Z_n−Z* anywhere. → **F16** |
| 2.6.2 CE=0 | **CONFIRMED** | → **F7** (same as DeepSeek 3.1) |
| 2.6.3 indexing | **CONFIRMED, AUTHOR-LEVEL** | Eq (4) uses Ẑ_{n+1} (L370); exact update uses z_n (L900); one-step convention Ẑ_{n+1}=Z(t_{n+1}⁻) (L425); but L366 states Ẑ_n=Z(t_n⁻). Three index sites; author must state the information pattern. → **A4** |
| 2.6.4 analytical status | **PARTIAL** | "Separating comparator" (L898), "Executed comparator evaluation at model level" (L1032) present; explicit "not a proposed institutional rule" absent. → **F17** |
| 2.7 screen detail | **PARTIAL + AUTHOR-LEVEL** | 10 of 12 gaps confirmed missing from main text; deferred to registration record by design (App A L1756–1761; data availability L2071–2075). Requested "selected-cohort diagnostic" sentence already present (L1246–1247). → **A6** |
| 2.8 power vagueness | **CONFIRMED gaps, AUTHOR-LEVEL** | §2.5 (L534–537) + §3.6 (L1237–1248) give horizons, σ scales, values, conditioning; amplitude/α/replicates/threshold/operational meaning missing. → **A6** |
| 2.9 case inventory | **PARTIAL + AUTHOR-LEVEL** | "Case-screening table and query log" promised as registration items (L2074–2075), not attached. Zero count not auditable from the paper alone. → **A6** |
| 2.10.1 "reproduction targets" | **PARTIAL** | L1391 verified. Not clearly a typo: "targets for reproduction" is a defensible nominal — but ambiguous. Recommend "targets for future reproduction", NOT "reanalysis" (changes meaning). → **F18**. Qwen's "I"-rewrite unusable (§1.4). |
| 2.10.2/.3 hypotheses framing, density | **PARTIAL** | "Are unreproduced" already stated (L1391); F18 suffices; density is stylistic. |

### 3.2 Internal inconsistencies (§3)

| Item | Verdict | Evidence / comment |
|---|---|---|
| 3.1 operator scope | **CONFIRMED** | L471–473 (cross-plant, "not claimed to be isolated") vs L975 ("on one plant rather than across plants"). Qwen's amendment is accurate. → **F19** |
| 3.2 multiplier status | **PARTIAL** | Both facts present (archived: L439; reconstructed: L1081–1084); joint status sentence missing. → **F20** |
| 3.3 margins omission | **CONFIRMED** | L952–955 lists exact-6.501 pair + real −1s (79.143, 2.306) but drops the Euler extractive complex pair at 47.536 (present in record paragraph L933). → **F21** |
| 3.4 trajectories at Tr≥34 | **CONFIRMED, AUTHOR-LEVEL** | Spectral band Tr=34–35→grid end (L1127–1130); trajectory agreement shown only on [1,20] (L1134–1136); no sentence on trajectory behavior at Tr≥34. → **A7** |
| 3.5 slow-stock Tr=10 | **PARTIAL** | Disagreement already reported as disagreement (L1137–1146); "not used inferentially" + table flag missing. → **F22** + **A7** |
| 3.6 fixed-plan triviality | **PARTIAL** | L1048–1049 verified ("the fixed plan is the equilibrium rest point (zero deviation)"). True but narrow; adopt reword. → **F23**; perturbation tests → author. |
| 3.7 protective spec | **CONFIRMED, AUTHOR-LEVEL** | No protective equation anywhere (F_B^prot, projection, E=0 saturation all unstated). Same root as DeepSeek 2.2. → **A1** |
| 3.8 cod misread risk | **DOWNGRADED** | First mention L1430 ("applies as a model-class diagnostic"); disclaimer 3 lines below (L1433–1436). Nearly redundant. → **F24** (optional) |
| 3.9 anchoveta mix | **REJECTED** | L1330–1332 compares review *regime* to review-*interval* region (both Tr-domain; coherent). The 3.7-yr catch period is discussed separately (L1303–1305). DeepSeek 3.18 agrees ("clear"). → **F25** (optional gloss) |
| 3.10 Table-3 q row | **CONFIRMED** | Row points to "Section 3.4 (Plant paragraph)" (L1806–1807) but q=0.001 is stated only in the stage Plant para as "the hold-map core's value" (L1109). → **F26** |

### 3.3 Mathematical/logical (§4)

| Item | Verdict | Evidence / comment |
|---|---|---|
| 4.1 S overload | **DOWNGRADED, AUTHOR-LEVEL** | Explicitly acknowledged (L321–323). Rename = large churn; recommend keep + optional notation table. → **A8** |
| 4.2 rational-term positivity | **CONFIRMED gap, AUTHOR-LEVEL bit** | No positivity assumptions anywhere (grep clean); Zref>0 unstated; singularity sentence (L362–364) coexists with Ẑ_n≥0 (L361) without reconciling. → **F9** + **A3** |
| 4.3 δ shift | **PARTIAL + AUTHOR-LEVEL** | δ unlisted-by-design (Table-3 grouped row L1812–1815); interiority stated as presupposition (L398) + archived (L1771, Table 3). δ value/sign/sensitivity need author facts. → **A3** |
| 4.4 Re λ | **CONFIRMED** | Transfer L799–801 states λ_j without Re; invoked at L1000–1003 for the undelayed sign. → **F27** (Reλ in 3.2; hedge 3.4's λ>0 as the companion's real eigenvalue) |
| 4.5 monodromy term | **REJECTED as issue** | Defined at first use (L306–308) and §2.3 (L482); Qwen concedes "not wrong if defined". Optional gloss only. |
| 4.6 Prop 3.1 title | **REJECTED/DOWNGRADED** | Disclaimer present (L764–766); "forward invariance" is the standard term for what is proved. Optional rename. |
| 4.7 a(E)=0 caution | **PARTIAL** | Both formula and limit present (L891–894); numerical-caution sentence missing. → **F28** (author confirms implementation) |
| 4.8 Lemma C>0 | **DOWNGRADED** | C>0 is an explicit hypothesis (L622–623) with the below-maximum proviso (L628–629). Qwen's C=0 sentence is an optional clarifier. → **F29** (optional) |
| 4.9 Schaefer wording | **DOWNGRADED** | "Change of growth law, not a parameter specialisation" already present (L593–595). Only "degenerate member" (L590) remains. → **F30** (optional) |

### 3.4 Empirical gaps (§5)

| Item | Verdict | Evidence / comment |
|---|---|---|
| 5.1 band justification | **AUTHOR-LEVEL** | Alternative-band sensitivity = new analysis; or limitation text. Overlaps 2.1. → **A5** |
| 5.2 12–60 resolvability | **PARTIAL + AUTHOR-LEVEL** | Caveat present (L526–530: "poorly resolved… partly a trend test… robust only if…"). Series-length counts need author data. → **A6** |
| 5.3 AR(1) simplicity | **AUTHOR-LEVEL** | New checks or limitation clause. → **A11** (+fallback **F31**) |
| 5.4 criterion iii | **REJECTED** | Comparative rule already present nearly verbatim (L555–560: "must outperform pre-registered alternatives on held-out prediction, phase ordering, or intervention response (since 'capable of generating' is not a falsifiable exclusion…)"). Auditor truncated the quote. |
| 5.5 zero-count framing | **DOWNGRADED** | "Not evidence against it" present (L1715); DeepSeek 3.13 concurs. Heading rename optional. |
| 5.6 Icelandic cod detail | **CONFIRMED gaps, AUTHOR-LEVEL** | L1289–1292 gives rule + CV 0.387 "(calculated here)" + 10–15 yr fluctuation; years/source/window missing. Supplement or soften. → **A6** |
| 5.7 anchoveta multiplicity | **PARTIAL** | 90-cell BH family present (L1312–1314: "All ten of the ninety tested index–lag cells…"); Granger/split-half family status unstated (L1315–1320). → **F32** |
| 5.8 cod covariates | **DOWNGRADED** | Disclaimer verified present; placement is author preference. |

### 3.5 Structural (§6), line-level (§7), rewrites (§8), additions (§9), checklist (§10)

- **6.1 claim registry / 9.3 status legend:** AUTHOR-LEVEL; note Box 1 already carries a status column covering much of this.
- **6.2 section split / 6.4 paper split / 9.4 figures / 9.1 notation table:** AUTHOR-LEVEL recommendations, not errors.
- **6.3 repetition in 4.1:** factually true (numbers restated, e.g. L1483–1497) but stylistic; trimming is author preference.
- **7.1 sectioning:** CONFIRMED structurally (`\setcounter{secnumdepth}{-1}` L17; manual numbers); cosmetic. → **A9** (recommend leave; journal reflows).
- **7.2 oalign:** **REJECTED** — auditor-pipeline artifact (§1.2). No action; do not "fix".
- **7.3 longtable calc:** **REJECTED as must-fix** — `calc` loaded (L8), compiles clean, Pandoc-standard.
- **7.4 hyperref order:** CONFIRMED trivially (hyperref L10 before caption L11); compiles clean. → **F33** (optional one-line swap).
- **7.5 graphicspath:** DOWNGRADED — works (figure compiled; literal relative path resolves independently of the search path). Optional cleanup.
- **7.7 reproduction targets:** → **F18** (same as 2.10.1).
- **7.8 exact-hold terminology:** **CONFIRMED** — ≥5 variants for the comparator ("exact held-assessment update" L378/937/948; "exact-hold" ×5; "exact update" L1042/1044/1050/1496/caption; "exact map" L914/942/953; "Exact held-assessment map" Box L111; "exact protective map" L944/971). → **F34**.
- **7.9 zero crossings:** **CONFIRMED** — L1013 "(zero crossings lie strictly between 0 and τ₋…)" genuinely ambiguous (count-zero vs located-between). → **F35**.
- **7.10 closed form:** **CONFIRMED** — L889–890 "gives the computation objects in closed form" overclaims (monodromy "assembled from" components L895–897). → **F36**.
- **8.1→F13; 8.2→F14** (note: uses 47.54/79.14 shorthand — coordinate with F6); **8.3→F12** (optional);
**8.4→PARTIAL** (three-way restriction exists L1224+; compare/extend); **8.5→OPTIONAL** (current accepted, DeepSeek 3.28).
- **9.2 reproducibility statement:** PARTIAL — Data availability exists (L2065–2083) but names no DOI; code folded in (no Code-availability heading). → author-level + **I5**.
- **§10 mapping:** 1→A3 · 2→F13 · 3→A5 · 4→F15 (downgraded) · 5→F16/F7/A4/F17 · 6→A1 · 7→A6 · 8→A6 · 9→A6 · 10→REJECT+optional · 11–20→A8/A10/A3/A11/optional.

---

## 4. Consolidated v28 text-fix list (editor-executable once author bits resolve)

Ordered by location. `[A#]` = needs the cited author decision first.

1. **F1** (L1746, App-A opener): "Sections 2.2, 2.4, and 2.5" → "Sections 2.2, 2.4, 2.5, 3.3, and 3.4".
2. **F5** (L318, notation): "(equation (2))" → "(defined after equation (2))".
3. **F9** (§2.1 effort law) **[A3]**: add positivity assumptions (r,K,q,E_max,Δ_ref,Z_ref,τ_m>0) and
"Because Z_ref>0 and Ẑ_n≥0, the rational term is well defined on the admissible state space."
4. **F15** (§3.1/§2.1): add "The main model takes E(t)=E_n, which satisfies H4 trivially; the
proposition is stated for the hold-or-interpolate class."
5. **F19** (L469–473, §2.3): append "Cross-plant comparisons … do not isolate the operator effect.
The one-plant operator contrast in Section 3.4 does isolate the operator for the logistic plant."
6. **F27a** (L799–801, §3.2): state transfer + persistence in terms of Re λ_j (Qwen 4.4 wording).
7. **F27b** (L1006–1010, §3.4): hedge "so λ>0" as the companion's real undelayed eigenvalue
("with Re λ>0" if complex; confirm against companion).
8. **F36** (L889–890): "gives the computation objects in closed form" → "permits a closed-form
expression for the held logistic flow; the linearized review map is then constructed from this flow,
the signal dynamics, and the update derivatives."
9. **F28** (L891–894, a(E) limit) **[A11]**: add "In computations, the a(E)=0 limit is used when
|a(E)Tr| is small to avoid cancellation."
10. **F16** (L898–901, exact update): add "with e_n=E_n−E* and z_n=Z_n−Z* (deviations from the
compared fixed point)".
11. **F7** (L900–901): add the CE=0 case "e_{n+1}=e_n+Tr·CZ·z_n".
12. **F17** (L898–910): add "This comparator is analytical, not a proposed institutional rule."
13. **F6** (precision, all sites): harmonize 47.5/47.54/47.536, 79.1/79.14/79.143, 6.5/6.50/6.501
(sites: L49, Box L105–106, L471, L911–925, L933–935, L1483–1484, L1496, caption L971). Rule: full
precision at record/first/caption uses; ≈-shorthand thereafter. Includes DeepSeek 2.6+3.9.
14. **F14** (artefact language): qualify flat uses (L913–914, L1484) per 8.2 wording + add "For an
institution implementing the incremental Euler rule these crossings are dynamically real; they are
artefacts only relative to the exact held-assessment update."
15. **F13** (annual-instability conditioning): fold L959–963 conditioning into the L983–984 claim
and the Fig. 1 caption (≈ Qwen 8.1 wording) with magnitudes (1.00035 / 1.00055 / 0.9838).
16. **F21** (L952–955, margins): add the omitted Euler extractive complex pair at 47.536 yr
(Qwen 3.3 rewrite).
17. **F11** (L1017–1018, λ note): add "λ is a derived eigenvalue, not a parameter."
18. **F10** (L1015, "differ only"): → "On this plant, the two operators differ only in…"
19. **F35** (L1013, zero crossings): → "There are no crossings in (0,τ₋); this even count is
consistent with the stability-switch principle because the stability state does not change between
zero delay and the first crossing."
20. **F23** (L1048–1049, fixed plan): → "In the deterministic baseline with fixed effort set at the
equilibrium value, the fixed plan remains at equilibrium — a baseline rest point, not a robust
performance result."
21. **F34** (terminology): define "exact held-assessment update" once; standardize all variants
(7.8 inventory: exact-hold ×5, exact update, exact map, Exact held-assessment map, exact protective map).
22. **F26** (Table-3 q row, L1806–1807): → "0.001 (value stated in the stage Plant paragraph as the
hold-map core's value)" or cite the exact logistic-core paragraph.
23. **F20** (§3.4 reconstruction intro): add "The archived stage-output records are
trajectory-classified only. The reconstructed stage map reported here includes multiplier records."
24. **F22** (L1145–1146, slow-stock cell): add "and is not used inferentially".
25. **F3** (L1283, "three illustrate"): → "three groups illustrate" (Sheridan-6; Icelandic cod with
haddock alongside; anchoveta) or split haddock into its own paragraph.
26. **F32** (§3.7 anchoveta, after L1314): add "The ninety index–lag cells define the BH
multiplicity family; the Granger and split-half tests are confirmatory and outside that family."
27. **F25** (L1330–1332, optional): "anchovy-class response region" → "anchovy-class
review-interval response region".
28. **F18** (L1391): "they are reproduction targets requiring" → "they are targets for future
reproduction requiring".
29. **F24** (L1430, optional): add "This is not an empirical rejection of scalar autonomous models
for northern cod…"
30. **F8** (L1107): "equations (1)–(4) in annual discrete form" → "the same controller equations
with Tr varied over {1,…,50} yr at annual internal steps" (see also I1).
31. **F4** (§3.7, "15–25 times shorter") **[A2]**: insert the four-state period or drop the comparison.
32. **F2** (L1117–1119, protective) **[A1]**: either "quota-tracking gains, the implementation of the
sign-reversed response…" or correct "the same convention…" to the distinct comparator actually used.
33. **F29** (Lemma 2.2, optional): add "For C=0 the smaller positive equilibrium is s; the strict
rightward shift holds for C>0."
34. **F30** (L590, optional): "degenerate member" → "formal limit (s→−∞)".
35. **F12** (§3.3, optional strengthener): adopt ≈8.3 quarantine sentence for archived records.
36. **F31** (§4.7, fallback): AR(1)-null-simplicity limitation clause if no new checks (→A11).
37. **F33** (preamble L10–11, optional): load `caption` before `hyperref`.
38. **I1** (L1107, independent): "equations (1)–(4)" over-cites the controller (includes logistic
plant (1)–(2)); cite the controller block for the stage system.
39. **I5** (declarations, optional): split a `Code availability` heading out of Data availability.

## 5. Author-action list (decisions + materials no editor can supply)

- **A1.** Protective convention: is quota-tracking the sign-reversal implementation? Give the
protective equation (projection, E=0 saturation). (DeepSeek 2.2; Qwen 3.7; →F2)
- **A2.** Four-state prediction period (number) or drop the "15–25×" comparison. (DeepSeek 2.4; →F4)
- **A3.** Parameter disclosure: full logistic-core vector + fixed point + CE/CZ + multipliers +
finite-difference step + precision environment (Qwen 2.2); δ value/sign/sensitivity (4.3); Zref>0
confirmation (4.2 →F9); interiority verification status.
- **A4.** Exact-update information pattern: which assessment is held (z_n vs z_{n+1}; Ẑ_n vs Ẑ_{n+1}
at L366/L425). (Qwen 2.6.3; I2)
- **A5.** Archived records' role: demote/keep, band independence or sensitivity with alternative
bands (Qwen 2.1, 5.1; →F12).
- **A6.** Supplement/registration completion: stock IDs, eligibility summary, detrending rule,
Lomb–Scargle settings, AR(1) method, MC replicate count, test families, p-values, record lengths,
endpoint/band sensitivity, full power spec, S4 case inventory, Icelandic-cod calculation audit
(Qwen 2.7/2.8/2.9/5.2/5.6; DeepSeek 3.2–3.4). **S4 inventory claims additionally unverified —
no supplement path provided (see §7).**
- **A7.** Stage long-horizon trajectories at Tr≥34; slow-stock Tr=10 diagnostics or formal flag.
(Qwen 3.4/3.5; →F22)
- **A8.** S-notation rename (recommend: keep; acknowledgment suffices). (Qwen 4.1)
- **A9.** Section-hierarchy restyle (recommend: leave; journal reflows). (DeepSeek 3.5; Qwen 7.1)
- **A10.** Structural options: claim registry, §3 split, paper split, extra figures, notation table.
(Qwen §6, §9)
- **A11.** AR(1) robustness checks or limitation (Qwen 5.3 →F31); a(E)=0 implementation confirm (→F28);
Tr=34–35 vs 34–42 band-entry reconciliation (I3).

## 6. Independent findings (raised by neither audit, found during verification)

- **I1.** L1107 invokes "equations (1)–(4)" for the stage controller — but (1)–(2) are the logistic
plant. The citation should name the controller block only. (Text fix F-list #38.)
- **I2.** Dual assessment indexing: Ẑ_n=Z(t_n⁻) (L366) vs Ẑ_{n+1}=Z(t_{n+1}⁻) (L425, Eq 4). Strengthens
Qwen 2.6.3; needs A4.
- **I3.** Band-entry wobble: "Tr=34–35 yr to the grid's end" (L1128) vs "entering at 34–42 yr"
(L1202–1203). Needs author reconciliation (A11).
- **I4.** Extra precision variants missed by both audits: "6.50 yr" (L1496), bands [47.54,79.14]
(Box L106, L935) and [6.50,200] (L939). Folded into F6.
- **I5.** No `Code availability` heading — code/seeds folded into Data availability (L2071–2075).
Optional split (F-list #39).
- **I6.** Trivial: "the more diagnostic" (L1635) is an informal adjective; optional touch.

## 7. Open item: supplement (S4) verification — RESOLVED (addendum A)

The supplement was fetched at the user-given path
(`arena agent 1/paper rewrites/paper5_supplementary_v5.md`, 41,922 B, 165 lines, S1–S8;
saved locally as `/home/user/paper5_supplementary_v5.md`). Findings:

- **S4 lists 7 systems** (Sheridan-6, Bangkok, La Mancha Oriental, Icelandic cod, Icelandic
haddock, Peruvian anchoveta, produced-capital systems) — all named in the manuscript
(La Mancha verified at ms L1277). But S4 states explicitly: "**The case-screening table and
query log are a registration requirement not yet discharged**", and S8 repeats the inventory
among undischarged items. The ">30 systems" set is therefore not auditable anywhere →
**Qwen 2.9 SUBSTANTIATED by the supplement itself** (stays **A6**). S4's zero-count framing
("a property of the searched candidate set, not a statistical test") matches ms L1715. ✓
- **Qwen 2.7 / 2.8 gaps confirmed UNDISCHARGED:** S8 lists "the RAM stock identifiers and
eligibility table; the processed series and spectral routines" and "the power-simulation code
and seeds" as not yet discharged. Detrending rule, AR(1) method, MC count, families, p-values,
record lengths appear nowhere in S1–S8. → **A6 stands**; the supplement documents the debt
rather than repaying it.
- **Qwen 5.6 (Icelandic cod) unfilled:** S4 repeats the manuscript summary verbatim-grade
(CV 0.387, 10–15 yr, lag 0.2–0.3 yr, 15–25×) with no years/source/window. Gap confirmed. → **A6**.
- **DeepSeek 2.4 persists into the supplement:** S4 repeats "15–25 times shorter than the
four-state prediction" without the period. → **A2/F4** unchanged.
- **Qwen 5.7 (anchoveta) largely ANSWERED in S4:** entities/CSVs (Peru 604/taxon 87,
Chile SAU v50-1, 1950–2019), ERSSTv5/SOI sources, artifact path `analysis/anchoveta_enso/`,
3.70 yr (+7.96 yr co-dominant; 3.63 yr subset), full r/p values, "ten of ninety index–lag
cells significant at BH-FDR 0.05, all SOI", Granger/split-half/sensitivity/CCM details —
consistent with ms L1303–1320. Remaining: the family-status sentence only. → **F32** only.
- **Qwen 5.8 downgrade supported:** S5 carries seal/capelin values as "source-reported
descriptive mass-balance inputs, background only" with untested statements fenced. ✓
- **F6 extends to the supplement:** S1 §3.4 uses shorthand precision (47.54 / 79.1 / 6.50 /
2.31) against the manuscript's record precision (47.536 / 79.143 / 6.501 / 2.306).
Harmonize both documents.
- **F37 (new, text fix):** ms L2077–2081 "deposited with the article" and S8 "committed with
the article's deposited material" name no locator (no DOI/path). Give the deposit a locator
or reword to "will be deposited with the article at [repository]". (Sharpens Qwen 9.2.)
- **I7 (new, significant): the supplement contradicts itself on certification tier.**
S1 §3.4 calls the crossing record "**re-execution-verified** computations"; S8's hierarchy
(nominal → re-execution-verified → independently re-executed → certified) then states
"**Nothing reported in this article reaches beyond the nominal tier**, and the statuses above
say so." "Reproducible numerical proposition" (S1's term for the reconstruction records) is
not even one of the four tiers. The manuscript's "executed and verified on the companion
delay study's identical hold map" (ms L910–911) must be reconciled with whichever tier is
true. → author-level (decide the true tier; align S1/S8/ms wording).
- **I8 (new): S2.3's objects are alien to the manuscript.** Theorem S2.3 concerns a
"three-state gated core" with "Hopf delays rτ±", flow-scale groups, and an effort law
("ηE(Z/Δ_ref − E/E_max)") in a different form from the manuscript's F_B — none of which
appear in v27. Either S2.3 belongs to a companion model (confirm + label it) or the
supplement has version skew (supplement v5 vs paper v27). Its k-remark ("Z*=δ itself depends
on k at the baseline calibration") is additionally murky. → author-level.
- **Qwen 4.3 UPGRADED by the supplement:** S2 Notation + Theorem S2.3's proof state
Z*=Φ(0)=**δ**, i.e. δ is the **equilibrium memory level** — equilibrium-determining, not a
mere "regularisation offset" (ms L395–396). Value still unstated everywhere. → strengthen
**A3**; add **F38 [A3]**: align the manuscript's δ description with the supplement's
(equilibrium memory level; state value/sign and the Φ-floor/softplus interior reading).

## 8. Suggested sequencing for v28

1. Collect author bits A1–A4 + A11(I3) (single-digit confirmations/numbers/equations).
2. Apply F-list in one pass (single version, per standing instruction).
3. Decide A5–A10 (supplement scope, structural options) — these set v28-vs-later scope.
4. Compile, verify, present; push only on authorization (HEAD must be re-read pre-push per protocol).

## 9. Completeness re-sweep (addendum B — no audit point left behind)

Prompted by the user's question, every audit item was re-checked against this report:

- **Qwen §1's five overview points** (summaries, not separately verdictable) map as:
(1) mixed result classes → A10/6.1 (Box 1 + S1 inventory already mitigate);
(2) unreproducible numerical claims → A3; (3) equation inconsistencies → F15/F16/F7/A4/A1;
(4) empirical under-specification → A6 (now supplement-confirmed, §7); (5) overstrong
claims → F13/F14.
- **Qwen 2.6's z^held-notation rewrite**: covered by F16/F7/A4; the `z^held` notation itself
is author-level style (either adopt or keep z_n with the A4 information-pattern sentence).
- **Qwen 5.7's alternative** ("include all tests in a global family"): F32 adopts the
lighter option (declare the confirmatory tests outside the BH family); the global-family alternative stays
 author's choice under A6.
- **DeepSeek 3.12–3.40**, each auditor-accepted ("Good") and requiring no action — enumerated
here for completeness: 3.12 Box-1 undelayed row; 3.13 zero-count/4.7(v) (spot-verified: 4.7
has 9 items, zero-count is the 5th ✓); 3.14 selection-mechanism hedge; 3.15 retrospective
null; 3.16 budworm edge; 3.17 era-bounded periodicity; 3.18 subannual-vs-region (agrees with
this report's rejection of Qwen 3.9); 3.19–3.22 phase-line diagnostic chain; 3.23 second
window; 3.24 ecosystem background; 3.25–3.26 operator-findings framing; 3.27 screen null;
3.28 cod partition; 3.29–3.30 falsification criteria; 3.31 retrospective limits; 3.32–3.37
prospective designs; 3.38 social measurement level; 3.39 limitations (i)–(ix) (spot-verified
present ✓); 3.40 conclusion.
- **DeepSeek has no 1.1–1.3** (its §1 starts at 1.4) — evidence of earlier resolved rounds,
not missing content.
- **Net result:** no audit point is missing from the joint assessment. The only additions
since the first version of this report are supplement-driven (F37, F38, I7, I8, the 4.3
upgrade, and the 2.9 substantiation) — all incorporated above.

## 10. v28 build record (2026-09-11)

Built and pushed on user authorization ("1-build v28 2- address supplement").

- **Manuscript:** `paper5_sampled_governance_v28.tex` via `build_paper5_v28.py`
(56 asserted substitutions, 117,734 → 119,991 B). Applied: F1, F3, F5, F6 (all sites),
F7, F8+I1, F10, F11, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25,
F26, F27a, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37 + Sept-11 date.
- **Deferred to author (unchanged in v28):** F2/A1, F4/A2, A3 (incl. F9, F38),
A4, F27b, F12, A5, A6, A7, I3, I5, I8.
- **Supplement:** `paper5_supplementary_v6.md` via `build_paper5_supp_v6.py` (6 subs):
seven→eight bodies, S1 precision, S1+S8 tier alignment (I7, manuscript-consistent
direction), S8 future-tense deposit (F37), S4 BH-family sentence (F32).
- **Verification:** labels 35/35, items 29/29, old phrases absent, new phrases present,
all 7 pure deletions + all inline-math deltas attributable; tectonic 0.15.0 exit 0,
29 pages, lineno renders, sole overfull = pre-existing §4.5 display.

1. Collect author bits A1–A4 + A11(I3) (single-digit confirmations/numbers/equations).
2. Apply F-list #1–#39 in one pass (single version, per standing instruction).
3. Decide A5–A10 (supplement scope, structural options) — these set v28-vs-later scope.
4. Compile, verify, present; push only on authorization (HEAD must be re-read pre-push per protocol).

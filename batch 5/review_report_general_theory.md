# Line-Level Review: the general-theory monograph family (flagship versions and ms_part series)

**Repository:** `MIKEAA2020/general-sustainability`, branch `main`, commit `8a286c4` (Task 58, HEAD at time of review).
**Scope:** the seven requested files, read line by line (5,742 lines / ≈37.0k words):

| File | Lines | Role (per repo registers) |
|---|---|---|
| `general_theory_of_sustainability_manuscript.md` | 1,399 | Flagship working manuscript (v-history: v0.1 → v0.2 → this); superseded, archival |
| `general_theory_of_sustainability_v0.1.md` | 968 | Earlier flagship version; superseded, archival |
| `general_theory_of_sustainability_v0.2_comprehensive.md` | 1,464 | Earlier flagship version; superseded, archival |
| `ms_part1.md` … `ms_part4.md` | 469+429+494+519 | Four part files of a *separate* 14 Aug 2026 manuscript ("An Architectural Kernel and Composition Language…"); superseded, archival |

**Method.** Every line of all seven files was read. All version relationships were established by byte-level diff (v0.1 → v1.0 is purely additive plus two word-level edits; v0.2 = v1.0 + Appendix D traceability matrix, otherwise byte-identical). Every checkable count was recomputed (contributions, principles, lemmas, conjectures, obligations, diagnostic steps, certification levels, indicator lists and their rationale clauses, Ω/registry/module tuple arities, reference-list identities). Every mathematical claim was re-derived (average-balance necessity, the growth bound, Lemma 1's liminf argument, slack normalizations, the efficiency identity, corridor and commons inequalities, all instantiation ODEs). Mechanical sweeps were run for raw control bytes, escape-loss patterns, lone trailing backslashes, unbalanced math delimiters, duplicate-word typos, and unresolved internal "Section N" references (script: `scripts/scan_manuscripts.py`, `scripts/check_refs.py`). Cross-layer checks were made against the current monograph (`revised_sustainability_manuscript.md`), Paper 1, the external review packet, and the pending-publications register, because the seven files are the archival ancestors of those live artifacts.
**Focus (per reviewer instruction):** math & logic flaws and internal inconsistencies; every finding carries file + line + verbatim quote + reason + suggested fix.
**Companion reports:** `review_report.md` (five core papers, 26 findings), `review_report_wave_e.md` (four Wave E manuscripts, 13 findings).

---

## 1. Executive summary

The good news first, because it is substantial. The flagship version chain (v0.1 → v0.2 → v1.0) is **exactly additive and internally consistent**: v0.1 is a strict subset of v1.0 (434 lines added, two word-level edits, no silent rewording), v0.2 is byte-identical to v1.0 except for its header, two of those word-level edits reverted, and an appended traceability appendix. Every enumerated list in all seven files matches its announced count (six contributions, twelve principles, ten substitution tests, eight hypotheses, Levels 0–6, twelve-step diagnostic, nine obligations, eight conjectures, ten limitations, Boxes 1–13, sections 1–33). Every internal cross-reference resolves. Every derivation I re-checked is correct, including the liminf impossibility argument (Lemma 1), the growth bound, and both slack normalizations. The reference lists are byte-identical across all four files that carry one.

The defects concentrate in three places. First, a **byte-level corruption**: `ms_part2.md:26` contains two literal carriage-return bytes where `\rightarrow`'s `\r` belongs, breaking the hybrid-trajectory formula — the core object of Operator II — and the same corruption has **propagated into the repo's current citable deliverable** (`revised_sustainability_manuscript.md` and its `.docx`), where the CR became a line break leaving bare `ightarrow` tokens inside the display math (G01). Second, a set of **specification-completeness gaps** in the more formal ms_part architecture: an "epistemic" constraint type promised three times but never given a projection or judgment component (G03); both manuscripts' own specification templates omit slots of their own Ω definitions (G04); and the §27 indicator list gives causal rationale for only six of its ten members while the pending-publications register promises "complete causal rationale" (G07). Third, **continuity and description errors**: the ms_part series says the flagship's twelve principles are "retained" when two were replaced, and the certification hierarchy "renamed" when two levels were redefined (G06); the external review packet describes ms_part1–4 as "Part files of the 14 August 2026 working manuscript", conflating two different manuscripts (G05).

**Severity counts: 1 HIGH · 6 MODERATE · 7 MINOR = 14 numbered findings**, plus micro-notes (§4.8).

| # | Sev. | File(s) | Finding (short) |
|---|------|---------|-----------------|
| G01 | HIGH | `ms_part2.md:26` → `revised_sustainability_manuscript.md:970-971` (+ its `.docx`) | Two raw CR bytes replace `\r` of `\rightarrow` in the hybrid-trajectory definition τ=(q₀,z₀)→(q₁,z₁)→⋯; broken formula propagated into the **current** monograph and its committed docx |
| G02 | MOD | `ms_part4.md:389-393` | Boxed conclusion formula: five lone `\` where `\\` row-breaks belong (aligned block collapses to one row; single `\`+newline is a control space, not a break) |
| G03 | MOD | `ms_part1.md:12,259` vs `273-319`; `ms_part4.md:454` | "Epistemic" constraint type declared in the abstract, in τ_j's enumeration, and in the Appendix B template — but §6.2 defines only four projections (K_P,K_F,K_N,K_R) and §6.3's judgment vector has only four components; the type is orphaned |
| G04 | MOD | flagship Appendix A (v1.0:1298-1361; v0.1:880-943); `ms_part4.md:436-448` | Each series' specification template omits a first-class slot of its own Ω: the flagship's template has no normative-authority (𝒩) field; the ms_part template has no typed-constraint-registry (𝒞) field |
| G05 | MOD | `external_review_packet/README.md:39-41`; `research_program/pending_separate_publications_register.md:3` | Packet calls ms_part1–4 "Part files of the 14 August 2026 working manuscript" — they are a *separate* manuscript (different subtitle, 33 sections, different architecture, opposite position on the flagship's central conjecture); "flagship" has two different referents across repo documents |
| G06 | MOD | `ms_part3.md:4,13-14`; `ms_part4.md:34,39,41` | "Retained but reclassified"/"retained but renamed" overstate continuity: principles #8/#9 were substantively replaced (Nested-systems→Typed-dependency; Burden-displacement→Burden-allocation), and certification Levels 3 and 5 were redefined, not merely renamed |
| G07 | MOD | `ms_part4.md:112-129`; register line 18 | §27 lists ten leading indicators but supplies causal rationale for only six (missing: recovery time, boundary-interface reliability, kernel contraction, transformation-option narrowing); the register promises "the ten leading indicators with their complete causal rationale (§27)" |
| G08 | MIN | v0.1:852, v0.2:1271, v1.0:1270, ms_part4:408 | Chen et al. (2019) is in all four reference lists and cited in none of the seven bodies (mirror of the papers' F11) |
| G09 | MIN | `ms_part1.md:427-451` | §7.3 defines σ_i⁻ and σ_i⁺ but the bottleneck diagnostic M(t)=min_i σ_i(t) uses an undefined bare σ_i (well-typed in the flagship, which has only the lower-bound σ) |
| G10 | MIN | `ms_part4.md:502-504` | Appendix G claim-ledger template: column headed "Status" carries the type alphabet "D/L/P/E/M/N" in the sample row; no Type column (the flagship's Appendix B separates them correctly) |
| G11 | MIN | `ms_part2.md:39-48`; v1.0:746,779 | Undefined symbols: T′ (post-arrival horizon) and total consumption C ("C_g=θ_gC"); V_g used in §11.3's constraints before its §11.9 definition; systematic symbol overloading (τ, σ, ρ, θ, F, λ) |
| G12 | MIN | v1.0:1044; v0.2:1045 | Twelve-step diagnostic item 8 begins lowercase ("restrict the policy set…") while the other eleven are capitalized |
| G13 | MIN | all seven | Mixed orthography: flagship mixes BrE "modelling"/"labour" with AmE "behavior"/"program"; ms_part series mixes AmE "behavior"/"labor"/"modeling" with BrE "programme" |
| G14 | MIN | v0.1:762-766, v0.2:1137-1141, v1.0:1136-1140 vs `ms_part4.md:179` | The flagship's *central* conjecture (§16.1, "adequate scale and resolution") is asserted in all three flagship versions but explicitly retired in ms_part4 §28.1 and excluded in the current monograph and Paper 1 §10.4 — a documented supersession the archival layer carries without a marker (ties into G05) |

---

## 2. HIGH-severity finding

### G01 — Raw CR bytes corrupt the hybrid-trajectory formula in ms_part2, and the corruption propagated into the current monograph and its .docx

**Location:** `ms_part2.md`, line 26 (§8.1 "Architecture graph"). Raw bytes (od -c):

```
(q_0,z_0)\r i g h t a r r o w (q_1,z_1)\r i g h t a r r o w \ c d o t s
```

**What happened.** The definition of the hybrid trajectory was written

```latex
\tau=(q_0,z_0)\rightarrow(q_1,z_1)\rightarrow\cdots .
```

Somewhere in the file's generation, the two-character escape `\r` was interpreted as a carriage return: each `\rightarrow` lost its `\r`, leaving a literal CR byte (0x0D) followed by the letters `ightarrow`. This is not a renderer quibble — the committed file contains two raw control bytes, and the token `ightarrow` is not a command, so the formula renders as `(q_0,z_0)ightarrow(q_1,z_1)ightarrow\cdots` (or, in renderers that treat CR as a break, a visibly garbled two-line mess). This is the *defining formula of Operator II's state object* — the hybrid trajectory — in the manuscript that introduces the two-operator architecture.

**Propagation (this is what raises the severity).** The same corrupted line, minus the raw CR (converted to a line break), is present in the repo's **current** monograph working preprint v1.0 — `revised_sustainability_manuscript.md`, lines 966–971:

```
A hybrid trajectory is

\[
\tau=
(q_0,z_0)
ightarrow(q_1,z_1)
ightarrow\cdots .
```

and I verified it is baked into the committed `revised_sustainability_manuscript.docx` (paragraph text `\tau=\n(q_0,z_0)\nightarrow(q_1,z_1)\nightarrow\cdots .`). The current monograph is the repo's designated citable record ahead of peer review (README: "a public, citable record of the architectural kernel"), so the defect is live in the artifact of record, with its origin in the reviewed file. No uploaded source (`uploads/*.txt`) contains this line, so the corruption was introduced during manuscript generation, not inherited.

**Fix.**

1. In `ms_part2.md:26`, replace the two CR bytes with the characters `\r`, i.e. restore `(q_0,z_0)\rightarrow(q_1,z_1)\rightarrow\cdots .` on one line.
2. Apply the same repair in `revised_sustainability_manuscript.md` (~lines 970–971) and regenerate `revised_sustainability_manuscript.docx`.
3. Add a build-time lint that rejects raw control bytes (other than `\n`) in manuscript files; this class of bug (`\r`, and see G02's `\` loss) is invisible in casual proofreading.

---

## 3. MODERATE findings

### G02 — ms_part4 §33: the boxed conclusion formula has lone `\` where `\\` row breaks belong

**Location:** `ms_part4.md`, lines 384–396.

**Verbatim (lines 386–394):**

```latex
\boxed{
\begin{aligned}
\text{Sustainability architecture}
={}&
\text{typed admissible viability}\
&+\text{architecture-sensitive transformation}\
&+\text{interdependent composition}\
&+\text{commons-aware responsibility}\
&+\text{auditable boundary assumptions}\
&+\text{prospectively declared identity and legitimacy}.
\end{aligned}}
```

**Reason.** Each of the five summand lines ends with a single backslash followed by the newline. In LaTeX, `\\` is the row separator inside `aligned`; a single `\` immediately before a newline is a control-space token, not a row break. As committed, the environment declares one row with six alignment points (`&`), so the "boxed summary of the architecture" — the manuscript's closing formula — either errors or renders as a single overlong line, not the six-term display the layout clearly intends. The flagship's own bmatrix (v1.0:272) shows `\\` surviving intact elsewhere in the same family, so this is a localized escape-eating defect of the same family as G01 (in a Python layer, `"...\\\\"` vs `"...\\"`).

**Fix.** Double each of the five trailing backslashes (lines 389–393).

### G03 — The "epistemic" constraint type is promised three times and never operationalized

**Locations and verbatim:**

- `ms_part1.md:12` (abstract): "One typed constraint registry distinguishes physical feasibility, functional viability, normative admissibility, relational responsibility, **and epistemic status** without reducing them to one kind of fact."
- `ms_part1.md:259` (§6.1): "`τ_j`: physical, functional, normative, relational, **or epistemic** type;"
- `ms_part4.md:454` (Appendix B template): the Type column sample is "P/F/N/R/**Epistemic**".

**Why this is an inconsistency.** §6.2 (ms_part1:269–298) defines exactly four typed projections — K_P, K_F, K_N, K_R — and gives a four-entry list of what leaving each projection means ("physical infeasibility…; loss of declared function…; normative inadmissibility; externalization, burden-allocation failure…"). §6.3 (ms_part1:300–321) defines the typed judgment vector as `(P_Ω(τ), F_Ω(τ), N_Ω(τ), R_Ω(τ))` — again four components. Consequently a constraint registered with τ_j = epistemic has: no projection, no component in the judgment vector, and no defined consequence for leaving it. The abstract's five-way "without reducing them to one kind of fact" promise is delivered as a four-way machinery. (The epistemic *claim-type* discipline of §3 — D/L/P/E/M/N — is a different axis, carried by ρ_j "provenance… and claim type"; as written, τ_j's epistemic value duplicates that axis while lacking any of its downstream machinery.)

**Fix (either direction).** (a) Operationalize: add K_E = ⋂_{τ_j=E}{z:p_j(z)}, a fifth judgment component E_Ω(τ), and a reason line ("leaving K_E: insufficient evidential basis for the declared confidence — the certificate's maturity level is capped"); or (b) delete "epistemic" from the abstract, from τ_j's enumeration, and from the Appendix B sample, noting that epistemic status is carried by ρ_j.

### G04 — Each series' specification template omits a first-class slot of its own Ω definition

**(a) Flagship: the normative authority 𝒩 is missing from Appendix A.** §5.2 (v1.0:289–298) defines the complete sustainability claim as Ω=(S,I,B,K,W,U,T,𝒟,𝒩), where "𝒩 [is] the normative authority or procedure used to choose social constraints." Appendix A, the "Sustainability specification template" (v1.0:1298–1361; v0.1:880–943), provides fields covering S, I, B, T (A1), K (A2), U (A3), 𝒟 (A4), W (A5) — but **no field for the normative authority or procedure**. A user completing the template produces an Ω-incomplete assessment with no prompt that the authority slot is unfilled. (The ms_part series fixed this — its §4.4 is devoted to 𝒩 — which makes the flagship's omission more visible as a gap the successor already knew about.)

**(b) ms_part series: the typed constraint registry 𝒞 is missing from Appendix A.** §4.1 (ms_part1:129–145) defines Ω with eleven slots, including "𝒞 is the typed constraint registry"; §6.1 calls 𝒞 "the official source of constraints." ms_part4's Appendix A "Sustainability specification template" (lines 436–448) lists ten Ω-slots (S, z₀, I^H, I^L, 𝒱, B, T, W, 𝒩, ℛ_A) plus the current architecture 𝒜_q — but **no constraint-registry line**. The registry presumably lives in the Appendix B template, but the specification template itself silently drops a first-class Ω slot, and nothing in Appendix A points to Appendix B.

**Fix.** Add the missing template line to each: "- Normative authority or procedure used to set social constraints:" (flagship A1); "- Typed constraint registry 𝒞 (Appendix B):" (ms_part Appendix A).

### G05 — The external review packet conflates the two 14 August 2026 manuscripts; "flagship" has two referents

**Verbatim.** `external_review_packet/README.md:39-41`:

> | `general_theory_of_sustainability_manuscript.md` | The flagship working manuscript of 14 August 2026 | Superseded (archival; v-history: v0.1 → v0.2 → this) |
> | `general_theory_of_sustainability_v0.1.md`, `general_theory_of_sustainability_v0.2_comprehensive.md` | Earlier flagship versions | Superseded (archival) |
> | `ms_part1.md`–`ms_part4.md` | **Part files of the 14 August 2026 working manuscript** | Superseded (archival) |

**Reason.** ms_part1–4 are not parts of the flagship. They are a **separate manuscript** with a different subtitle ("An Architectural Kernel and Composition Language for Ecological, Economic, and Social Systems" vs the flagship's "Robust Viability in Dependency-Closed Ecological, Economic, and Social Systems"), a different architecture (33 sections in six Parts; Operators I/II; typed constraint registry with a fourth relational projection; interface adequacy *replacing* the flagship's causal-closure axiom; commons nodes), and the **opposite position on the flagship's central conjecture** (retired, ms_part4:179). A reviewer using the packet as "the entry point into the repository as the single source of truth" would reasonably conclude ms_part1–4 are the flagship split into four files, and then be confused when §14 speaks of "the previous manuscript's twelve principles" and §28.1 retires a conjecture the "same" manuscript asserts in its §16.1. Compounding the ambiguity, `research_program/pending_separate_publications_register.md:3` calls `revised_sustainability_manuscript.md` "the flagship" — so "flagship" denotes the old monograph in the packet and the current monograph in the register.

**Fix.** Reword the packet row, e.g.: "Part files of a *separate* 14 August 2026 manuscript (the architectural-kernel version; successor to the flagship v-history, whose §16.1 conjecture it retires at Part VI §28.1)". Standardize "flagship" to one referent across repo documents (or say "the 2026-08-14 flagship" vs "the current monograph").

### G06 — "Retained but reclassified/renamed" claims overstate continuity between the flagship and the ms_part series

**(a) Principles.** `ms_part3.md:4`: "The previous manuscript's twelve principles are **retained but reclassified** as interface or operational principles rather than undifferentiated axioms." In fact ten of the twelve are retained (with type tags added), and **two are substantively replaced**:

| # | Flagship §8.9 (v1.0:561-562) | ms_part3 §14 (lines 13-14) |
|---|---|---|
| 8 | **Nested-systems principle:** a subsystem is not sustainable if it destroys a necessary containing or supporting system | **Typed-dependency principle [D/N]:** obligations follow declared support, impact, and normative edges *rather than mere nesting* |
| 9 | **Burden-displacement principle:** shifting risk or depletion across space, population, domain, or time does not remove it from the complete account | **Burden-allocation principle [D/N]:** transferring risk or depletion does not discharge responsibility unless the transfer satisfies the registered allocation and affected-population constraints |

These are not reclassifications; #8 inverts the flagship's rule (nesting alone no longer creates obligation), and #9 converts a conservation principle into an allocation-permissibility rule. The replacement is deliberate and defensible — the sentence describing it is not.

**(b) Certification levels.** `ms_part4.md:34`: "The earlier certification hierarchy is **retained but renamed** so that preliminary accounting is not confused with sustainability." Beyond the L1/L2 renamings to "preflight", **two levels change content**: Level 3 goes from "at least one policy maintains constraints in a dynamic model" (v1.0:1017) to "the actual initial state belongs to an estimated viability kernel under an implementable policy" (ms_part4:39 — a semantic strengthening, consistent with ms_part1 §7 but not a renaming); Level 5 goes from "Dependency-closed viability: external supports, displaced burdens, distribution, and delayed liabilities are included" (v1.0:1019) to "Embedded viability: boundary interfaces, dependencies, commons, distribution, and delayed liabilities are represented" (ms_part4:41 — re-scoped to the interface-adequacy doctrine).

**Fix.** "Ten of the previous manuscript's twelve principles are retained with type tags; two are replaced to match the typed-dependency architecture" / "retained with renaming of Levels 1–2 and redefinition of Levels 3 and 5."

### G07 — §27's indicator list has rationale for six of ten indicators; the register promises "complete causal rationale"

**Verbatim.** `ms_part4.md:114-125` lists ten candidate indicators: declining minimum slack; falling capacity-to-load ratio; **increasing recovery time**; rising control effort; greater dependence on buffers; increasing T_r/T_c; **declining boundary-interface reliability**; increasing burden transfer; **contraction of the current architecture's viability kernel**; **narrowing of viable transformation options** (boldface = the four with no rationale clause). The rationale paragraph (ms_part4:127) explains only six: "declining slack approaches a binding constraint; falling capacity-to-load ratio removes response room; rising control effort can reveal hidden deterioration; buffer dependence finances recurring load from finite reserves; rising delay ratio indicates dynamically inadequate governance; burden transfer converts local improvement into relational failure."

The flagship's §14.1 gives a rationale for **all seven** of its indicators (v1.0:1060 — including "Increasing recovery time suggests weakening restorative dynamics"), so the recovery-time rationale existed and was dropped in the architectural rewrite, and the three new architectural indicators never received one. This matters beyond the archival file because `research_program/pending_separate_publications_register.md:18` (A-1, a pending companion publication) promises "the ten leading indicators **with their complete causal rationale** (§27)", and the current monograph's §27 — the register's declared carrier — carries the identical six-of-ten rationale.

**Fix.** Add four rationale clauses in §27 of both carriers (ms_part4 and `revised_sustainability_manuscript.md`), e.g.: increasing recovery time indicates weakening restorative dynamics; declining interface reliability indicates boundary assumptions approaching violation; kernel contraction indicates shrinking within-architecture options; narrowing transformation options indicates the architecture graph itself is closing. Or correct the register to "six of ten."

---

## 4. MINOR findings

### G08 — Chen et al. (2019) is listed and never cited, in all four reference-carrying files

**Locations:** v0.1:852, v1.0:1270, v0.2:1271, ms_part4:408. The entry: "Chen, Y., Anderson, J., Kalsi, K., Low, S. H., & Ames, A. D. (2019). Compositional set invariance in network systems with assume–guarantee contracts. In *Proceedings of the American Control Conference*." Grep confirms no in-text citation anywhere in the seven bodies; assume–guarantee reasoning is discussed without citation (flagship §2.6:66 and §9:574-598; ms_part1 §2.6:73). This is the mirror image of the papers' F11 (74 of 95 bibliography entries uncited) — here a single orphan entry repeated in four files. **Fix:** cite it at the §2.6/§9.1 assume–guarantee passages, or drop it from all four lists (the lists are otherwise byte-identical, so one edit propagates trivially).

### G09 — M(t)=min_i σ_i(t) uses an undefined σ_i

**Location:** `ms_part1.md:427-451` (§7.3). The section carefully defines *two* normalizations — σ_i⁻ = (z_i−z_i^min)/(z_i^ref−z_i^min) for lower bounds and σ_i⁺ = (z_i^max−z_i)/(z_i^max−z_i^ref) for upper bounds (both correctly mapping ref→1, bound→0) — and then writes "The bottleneck diagnostic is M(t)=min_i σ_i(t)" with a bare σ_i that matches neither. (The flagship's §5.5 defines only the lower-bound σ_i, so its identical formula is well-typed there; the defect is introduced by the ms_part generalization.) **Fix:** M(t)=min(min_i σ_i⁻(t), min_i σ_i⁺(t)) over the respective bound families.

### G10 — ms_part4 Appendix G: header says "Status", sample row carries the type alphabet

**Verbatim** (ms_part4:502-504):

```
| ID | Claim | Status | Assumptions | Evidence/derivation | Counterexample sought | Owner | Revision trigger |
|---|---|---|---|---|---|---|---|
| CL1 | [Claim] | D/L/P/E/M/N | [List] | [Source] | [Test] | [Researcher/module] | [Condition] |
```

The third column is headed "Status" but the sample places the claim-type enumeration (D/L/P/E/M/N) there; there is no Type column at all. The flagship's Appendix B (v1.0:1367-1369) gets this right with separate Type ("D/L/P/E/M/N") and Status ("Proposed/Supported/Rejected") columns. A filled-in ledger following the ms_part template would conflate a claim's epistemic type with its verification status — precisely the conflation §3's discipline exists to prevent. **Fix:** split into Type and Status columns as in the flagship.

### G11 — Undefined symbols and systematic overloading

- **T′ undefined** — `ms_part2.md:39-48` (§8.2): "a candidate meta-policy Π seeks some q′ and time T\* such that z(T\*) ∈ Viab_{𝒜_{q′}}(K\*_{q′}, W_{q′}, **T′**; U_{q′}^impl)". T\* is the arrival deadline; T′ (evidently the post-arrival maintenance horizon) is never defined anywhere in the series. Also, z(T\*) is a q′-space state only via the reset map R_{qq′}, which the formula leaves implicit.
- **C undefined** — v1.0:746 / v0.1:572 / v0.2:747 ("With distribution shares θ_g, C_g=θ_g**C**, ∑θ_g=1") and ms_part3:443: total consumption C is never introduced (and collides with capacity C_i, §4.6, and with C the treatment capacity of §11.9/ms_part3 §22).
- **V_g used before definition** — v1.0:779 / v0.2:780: §11.3's constraint block includes "V_g ≤ V_g^max" but V_g (procedural violations) is first defined in §11.9 (v1.0:877); ms_part3 defines it properly in §22 before use at line 380.
- **Overloading across sections** — τ: delay (v1.0:174), measurement delay τ_i (v1.0:947; ms_part3:201), constraint type τ_j (ms_part1:259), trajectory τ (ms_part1:305; ms_part2:25); σ: slack (v1.0:348) vs indicator uncertainty σ_i (v1.0:947); ρ: stress ratio (v1.0:162) vs indicator resolution ρ_i (v1.0:947); θ: distribution shares (v1.0:746) vs indicator thresholds θ_i (v1.0:947); F: dynamics (v1.0:284), forbidden set (v1.0:648), production function (v1.0:735); λ: latent liabilities (v1.0:254), assimilation λ(E) (v1.0:717; ms_part3 writes λ_E(E), a notation drift between the two series for the same object), incoming demand λ(t) (v1.0:880). Each use is locally defined, but the reuse rate is high enough to impede the cross-referencing reader. **Fix:** subscript or rename the collisions (e.g., 𝒯_r for response time is already used; use ℋ(z) for the forbidden set; Θ_g for shares).

### G12 — Lowercase list item in the twelve-step diagnostic

**Verbatim** — v1.0:1044 (v0.2:1045; v0.1 has no §13.5): "8. **restrict** the policy set to technically feasible, legally admissible, institutionally available, and implementable action." The other eleven items begin with a capital ("Specify… Identify… Map… Conduct… Issue…"). Pure typography, but in the flagship's most-templated list. **Fix:** capitalize "Restrict".

### G13 — Mixed British/American orthography within each series

- Flagship (all three versions): BrE "modelling" (v1.0:12, 38, 1260) and "labour" (v1.0:588, 623, 627, 1339) alongside AmE "behavior" (v1.0:179, 687, 796, 928, 1192) and "program" (v1.0:12, 1085, 1111, 1152).
- ms_part series: AmE "behavior" (ms_part1:61, 232; ms_part2 ×6; ms_part4 ×5), "labor" (ms_part2:335, 339), "modeling" (ms_part3) alongside BrE "programme" (ms_part1:12; ms_part4:183, 219, 255).

Notably, the two series chose *opposite* dominant conventions (flagship leans British in the same words where ms_part uses American — labour vs labor — yet the flagship uses the American "program" where ms_part uses "programme"). **Fix:** one convention per manuscript; since these are archival, fixing only the current monograph's descendants matters more (the current monograph inherits "programme" + "behavior", the same mix).

### G14 — The archival layer carries opposite positions on the flagship's central conjecture, unmarked

All three flagship versions present §16.1 as the **first central conjecture** ("Every persistent sustainability failure can be represented, at an adequate scale and resolution, as the loss or anticipated loss of robust controlled invariance…" — v0.1:762-766, v0.2:1137-1141, v1.0:1136-1140). ms_part4 §28.1 (line 179) then retires exactly this claim: "The former unrestricted claim that every sustainability failure can be represented at an 'adequate scale and resolution' is retired because it is too elastic to falsify." The retirement is the program's standing position — propagated to the current monograph (revised_sustainability_manuscript.md:2857: "No unrestricted claim … is adopted, because such a statement is too elastic to falsify") and to Paper 1 §10.4 (manuscript.md:351). The same layering applies to the flagship's Axiom 3 (causal closure), which ms_part2 §9 explicitly replaces ("'Causal closure' is replaced by a property-relative interface principle"). This is a *documented* supersession, not a live error — but nothing in the seven files marks it, and the packet's one-line descriptions (G05) do not record it either, so a reader of the archival layer alone takes §16.1 as the standing central conjecture. **Fix:** none needed inside archival files; record the supersession in the packet inventory (folds into G05's rewording).

---

## 5. Positive verifications (what was checked and found correct)

1. **Version lineage is exactly additive.** diff shows v0.1 → v1.0 = +434 lines, −3 lines (header line, and two word-level edits: "The current proposal" → "The proposed framework" at §2.3, "the current proposal" → "the proposed account" at §17). v0.2 = v1.0 + header/scope note + Appendix D traceability matrix, with Appendix E ≡ v1.0's Appendix D byte-for-byte and §§1–19 byte-identical. No silent rewording anywhere in the chain — an unusually clean version history.
2. **All announced counts are correct.** Flagship: six contributions (v1.0:38); 7 gap items (§2.7); 6 claim types (§3); 12 principles (§8.9); 10 substitution tests (§8.7); 4 dimensions (§4.9); 9 certificate contents (§13.1); 8 impossibility patterns (§13.2); Levels 0–6 ≡ 7 grades ≡ the §13.1 prose grading (§13.3); 6 proof obligations (§13.4); 12-step diagnostic (§13.5); 7 leading indicators **with 7 rationale clauses** (§14/§14.1 — complete, unlike ms_part4's §27); 8 hypotheses H1–H8 (§14); 4 nested models (§15); 5-item test suite (§15); 7 falsification sweeps (§15.1); 6 limitations (§17); 4 workflow roles (§18); 10 shortest-path controls, 8 rigor layers (§18.2–18.3); 4 concluding operations (§19). ms_part series: 11 Ω slots ≡ §4.1's list; 7 architecture-tuple components ≡ §5.1's list; 8 registry components ≡ §6.1's list; 5 interface-contract components ≡ §9's C_e; 6 hypergraph edge types ≡ §10's table; 5 contract modalities (§12.1); 10 outputs (§24); 12 certificate contents (§25.1); 9 impossibility patterns (§25.2); 9 obligations (§26); 12-step template (Box 13); 8 conjectures (§28); 8 falsification tests (§29); 4 nested approaches + 6-case suite (§30); 7 formal-work priorities (§30.1); 9 evaluation criteria (§30.2); 10 limitations (§32); 10 spine elements (§33); appendices A–H present.
3. **Numbering is continuous and every internal reference resolves.** ms_part series: sections 1–33 across the four files with no gaps or duplicates; Boxes 1–13 sequential; §17.2's "Section 7.3", Lemma 8's "Section 7.2" (both in ms_part1) resolve. Script-verified: zero unresolved "Section N(.M)" references in all seven files. v0.2's Appendix D traceability matrix: every row's claimed location (Sections 3, 16; 18.3; 11.10; 4.9; 5.4; 5.5/9.3/14; 8.9; 8.7; 4.10/9; 4.11; 4.12; 9.5–9.8; 9.9; 10; 10.1; 11.6–11.9; 12; 12.3; 12.4–12.5; 12.6; 12.7–12.8; 13.1–13.5; 14; 15.1; 15.2; 16.1; 18; 17; Appendices A–C) exists and matches the stated treatment; the standalone `general_theory_of_sustainability_traceability.md` carries the identical matrix (only the first column header differs: "Source concept" vs "Dialogue element").
4. **Mathematics re-derived and confirmed.** §7.1's necessity claim (liminf-average of net input < 0 ⟹ s(T) ≤ s(0) − δT ⟹ threshold crossing) and ms_part3 Lemma 1's strict version (liminf > 0 of average net depletion ⟹ impossibility) are both correct as stated; the growth bound L(Y) ≥ αY ∧ C ≤ C̄ ⟹ Y ≤ C̄/α (flagship §7.7, Lemma 7) is correct with its hedge; both slack normalizations map ref→1 and bound→0 (ms_part1 §7.3's σ⁺ is well-formed given z_ref < z_max, with the degenerate case explicitly handled at line 447); the efficiency identity L_tot = Y_tot/η follows from η = Y/L; the corridor condition and ms_part1 §7.2's strengthened transformation criterion are mutually consistent with Lemma 8; the control-hierarchy inclusions U_impl ⊆ U_inst ⊆ U_tech ⊆ U_theor (ms_part1 §5.2) are the same set relations as the flagship's reversed chain (v1.0:923); the commons block (L_C = Σl_i ≤ C_C, Σb_i ≤ C_C, violation l_i > b_i, non-pivotal actor still violable) is internally consistent; every instantiation ODE set (flagship §11.1–11.3, §11.6–11.9 ≡ ms_part3 §19–§23) is dimensionally and structurally coherent, and the two series' versions of each model agree term-for-term (modulo the λ(E)/λ_E(E) notation drift).
5. **No other mechanical defects.** Beyond G01's two CR bytes and G02's five lone backslashes: no other raw control bytes in any of the seven files; all `\[ \]` and `\( \)` delimiters balanced; no duplicate-word typos ("the the" etc.); reference lists byte-identical across the four files that carry them; all in-text citations resolve to the list (sole exception G08); the four docx artifacts built from the flagship files are free of the G01 corruption (checked programmatically).
6. **Cross-layer supersession is otherwise orderly.** The ms_part → current-monograph inheritance is faithful where I spot-checked it: the current monograph's §27–29 reproduce ms_part4's Part VI (with the same 6-of-10 rationale gap, G07), its twelve principles are the ms_part versions (Typed-dependency #8, Burden-allocation #9), and its conjecture section adds Conjecture 3A to ms_part4's eight — which is why the register's "nine architecture-level conjectures" is right for the current monograph (its §28 has 9) even though "the flagship's Part VI" phrasing points a reader at ms_part4, which has 8 (see G05).

---

## 6. Suggested fix order

1. **G01** — repair the CR bytes in `ms_part2.md:26` and the propagated copies in `revised_sustainability_manuscript.md`/`.docx` (the only finding touching a *current* deliverable; add a control-byte lint to the build).
2. **G02** — double the five backslashes in `ms_part4.md:389-393` (same escape-loss family; one-minute fix).
3. **G03 / G04** — close the specification gaps (K_E or delete the epistemic type; add the 𝒩 line to the flagship's Appendix A and the 𝒞 line to ms_part4's Appendix A). These are the two findings that affect a *user* following the templates.
4. **G05** — reword the packet's ms_part1–4 row and standardize "flagship" (the packet is the reviewer's entry point; the conflation actively misleads).
5. **G06 / G07** — correct the two "retained/renamed/complete" overstatements and add the four missing rationale clauses in §27 (both carriers), or adjust the register's A-1 text.
6. **G08–G13** — batch of small editorial fixes (uncited Chen entry; σ definition; Appendix G columns; T′/C/V_g and symbol collisions; item 8 capitalization; orthography) — best done in one pass per file.
7. **G14** — no file change; covered by G05's packet rewording.

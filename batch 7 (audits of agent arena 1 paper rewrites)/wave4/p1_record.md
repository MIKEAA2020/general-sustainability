# P1 wave-4 record — paper1_assessment_separation_v20.md (Task 74-a)

Build: `apply_batch7_wave4_p1.py` (fail-loud; 35+ anchored `sub1`/`subn` edits + the
version-log splice + the one allowed append (S8) to `paper1_supplementary_v2.md`).
Runs clean three times — byte-identical rebuild: v20 MD5
`6264d9d13fda4f40b0bbe5ecd95fcc6a`, supplementary MD5
`300d6f24b640b52043e6c9b67e79b46c` (the S8 append is verified byte-identical on
re-runs; no double-append). v19 untouched. 161 changed lines in 66 diff hunks, all
read line by line and itemized below.

Resumption note: the build agent was interrupted after producing the script and
v20-in-progress; the resumed pass diagnosed the failing mechanical check (the
'typed-endpoint' count: the build legitimately carries **7** body occurrences — §2.8
notation list, §3.1 five-operators intro, §3.1 photograph pointer, §3.1 the Definition,
§3.1 machine-scoping sentence, §5.4 operator citation, §5.4 witness statement — the
check expected 6 and its error message said 5), audited every count-based check for
the same staleness, fixed five more stale checks and one broken idempotency check, and
completed the build. No build edit was added or removed in the process: the source
edits are exactly the interrupted script's edits; only the checks and the version log's
vocabulary-count claim were corrected to match the actual (intended) build.

## Per-item disposition

| Item | Endorsement | Decision | Exact wording / notation chosen | v20 line evidence | Verification |
|---|---|---|---|---|---|
| R8 [standing] abstract length | standing cap ≤300 | IMPLEMENTED | 310 → **298 words** by whitespace count; four redundancy trims (the "in which" → colon connective; "which has" → "with"; "admitting" dropped before "convexified actions"; the menu-geometry apposition "— a property of the menu's geometry —" dropped) — no claim removed | abstract L5–13 | machine-pinned: `abstract is 298 words, expected 298`; v19 pinned at 310 |
| (1) E_end,typ typed-endpoint operator | grok A3 / claude §5.4-Fourth [both — consensus 4] | IMPLEMENTED (Definition deposit, no computation) | §3.1 header "Four operators" → "Five operators"; the fifth **typed-endpoint** operator deposited as a Definition — $E_{\mathrm{end,typ}}(z) = \{a : \forall d,\ \mathrm{End}(a,d) \subseteq S \text{ and } \mathrm{Succ}(a,d) \subseteq G\}$ — between the chain's first and last links; one-line witness from the recorded action table + Theorem 5(1)'s proof (FAST typed-endpoint-admissible at every state of $X_0$, typed-tube-admissible only for $s_1 \ge 2$); the machine artifact's coverage scoped ("checks the physical endpoint operator only; … not machine-verified"); §5.4's Fourth implication cites it with the same witness and the "not one of the artifact's 25 checks" scoping; §2.8 lists the operator | §3.1 L121–145 (Definition L143–145, display L144); §5.4 L409; §2.8 L107 | script: display present; "not machine-verified" + "checks the physical endpoint operator only" present; witness sentence present; E_end,typ ×5, 'typed-endpoint' ×7 (all seven itemized intentional), all message/count mismatches fixed |
| (2) §1.1 companion-prose strip | grok §1.1 + claude §1.1 [both — the cross-paper exposure] | IMPLEMENTED (strip-to-citation, cite-don't-drop) | The cycle-closure/waste regime paragraph → one crisp statement + "developed for the companion ledger study (Author, A., et al., in review) and is not re-argued here; no theorem of this paper touches material cycles"; the hen/orchard/productivity-illusion block (7 v19 lines) → one sentence + the same citation, with the witness-inconsistent base-vs-services reading corrected to the floor-mid-interval reading ("what it fails to see is not the base but the individual floor mid-interval") | §1.1 L25 (regimes), L35 (masking) | script: stripped-prose needles all 0 ("waste-in-waiting", "no substance is waste by its nature", "An apple crop renews within a year", "not a strict membership test"); ledger-companion citation ×5 (4 in-text + 1 entry); productivity-illusion mentions = 2 (1 spaced §1.1 + 1 hyphenated §3.1) |
| (3) §2 13-slot tuple cut | grok D3 + claude [both — consensus 6] | IMPLEMENTED (named record, cite-don't-drop) | §2.2 "The canonical tuple" → "The canonical datum as a named record": the display $\mathfrak{S} = (T, Z, \dots)$ is withdrawn from the main text, the thirteen fields named in prose, "The field-by-field definitions are carried by the Supplementary Material (S1), and Section 2.7 records the witness's instantiation field by field"; "a model is a specified record; a claim … about a record"; §2.7 "tuple is a specialization map" → "datum is…" | §2.2 L73–75; §2.7 L95; §2.8 L93 | script: named-record header present; the 13-slot display absent from the main text; S1 pointer present |
| (4) notation pass (FP₀/r/R/A/e) | grok notation table + claude C [both — consensus 5] | IMPLEMENTED | $\mathrm{FP}_0 \to \mathcal{Q}$ at all 11 sites (grok's $D_{\mathrm{agg}}$ rejected: $D$ names the disturbance class; Figure 1's image carries $I = \mathrm{FP}_{\mathrm{agg}}$ and $R$ only — no image-text mismatch; $\mathrm{FP}_{\mathrm{agg}}$ kept, figure-pinned); $r$ frozen to $w_2/w_1$ ("and frozen to that reading"; the resource increment re-lettered $\kappa$: $\mathsf{Aug}_\kappa$, $\mathcal{A}_\kappa$, $\kappa^*$, $\mathrm{STAGED}_\kappa$; "the letter $r$ never denotes the increment"); the action-set drift sites $|A| = 4$ and "whether $A$ is exhaustive" written on $\mathcal{A}$; §2.8 gains the two-scope fences ($R$ deployment/reset vs rescue set — "every theorem reference and Figure 1 use the rescue-set reading"; $A$ assessment operator vs $\mathcal{A}$ action set; $e$ gain vector vs $e_k$ basis vector) and the $S = S_0$ identification | §2.8 L95–111; §4.1 L164; §5.5 L414–417; §5.6 L421; Figure 1 caption L276; region defs L232–234 | script: FP₀ 0 in body, $\mathcal{Q}$ ×11, FP_agg retained; all $\kappa$ forms present / all $r$-increment forms 0; $|\mathcal{A}| = 4$ present; fences present |
| (5) demotions | grok D + claude E [both — consensus 2] | IMPLEMENTED (status relabels on the unchanged 1–9 counter) | Proposition 1 → **Remark 1**, Lemma 2 → **Remark 2**, Theorem 3 → **Proposition 3**, Theorem 6 → **Remark 6** — headers relabelled, every cross-reference updated, no renumbering, no proof change; §4.1 header "proposition" → "remark"; §1.3/§5.2 contribution lists updated; §4.9 listings updated; one-line reasons in the version log (the inclusion is elementary; the equivalence is the dual-cone fact; the identity is that fact applied pointwise plus constraint-set monotonicity; the hold-prefix result is an identity pullback) | Remark 1 L160–162; Remark 2 L172; Proposition 3 L181; Remark 6 L282; §4.9 L314; §6.1 L375–376 | script: old labels 0; counts pinned (Remark 1 ×7, Remark 2 ×8, Proposition 3 ×15, Remark 6 ×10, Theorem 5 ×24, Theorem 7 ×4, Theorem 8 ×9, Proposition 4 ×7, Proposition 9 ×7); relabelled statement headers present; proofs byte-identical except cross-reference labels (diff-verified hunk by hunk) |
| (6) title/§7 doctrinal sound | grok D + claude E6 [both] | IMPLEMENTED (title unchanged — decision recorded; §7 scoped) | Title unchanged: "no specific retitle is endorsed by the joint evaluation, and the title's claim is the operator-level separation the theorem literally proves" (version log). §7's opening scoped: "the divergence of the two doctrines **as formalized here** — the scalarized-aggregate and typed operators of Section 3.1 on a common action menu and disturbance class — … a theorem about those operators. **The theorem ranks no doctrine**: Section 5.1 scopes the formalizations, and after Theorem 8 the structural character of the separation is a property of the finite deterministic menu, not of weak or strong sustainability as traditions" | §7 L443; title L1 | script: "The theorem ranks no doctrine" present; title byte-identical to v19 |
| (7) the 25 checks | grok + claude [both] | IMPLEMENTED (enumerated in the appended S8) | The artifact's 25 machine checks enumerated one by one in the new S8 of `paper1_supplementary_v2.md`, each quoting the check's recorded name verbatim from the committed results JSON (`research_program/paper1_instantiation/typed_false_positive_instantiation.json`, execution 2026-08-28, exact integer arithmetic at scale 40, exit 0) with its main-text mapping; nothing recomputed (all recorded pass statuses True, 25/25); naming notes for the artifact's own "FP/FP0" tokens and S7's "Theorem 6" vs v20's "Remark 6" relabel; the main text keeps the count + a one-sentence pointer | S8 (supplementary, 35 inserted lines); §4.9 L315–317 | script: 25 enumerated items counted by regex; "25/25" + "verbatim" provenance note present; §4.9 pointer present; git diff add-only (35 insertions, 0 deletions); re-run verifies the appended block byte-identical (no double-append) |
| (8) §6.1 unpublished-companion dependence | grok + claude [both, cross-cutting] | IMPLEMENTED (cited + scoped) | The scored forecast-evaluation companions named and cited in text + References (Author, B. = the cod ladder study, Author, C. = the Edwards Aquifer study — both real repo titles, fresh letters per the E1-v11/P5-v21 pattern); the explicit no-dependence statement: "No result of this article depends on an unpublished companion: the separation results rest on their displayed proofs, the machine artifact of Section 4.9 is deposited independently, and this manuscript's companion dependence is confined to the introduction's citation of the ledger study and the disciplinary analogy of this paragraph"; the unscoped "(each under review)" withdrawn | §6.1 L433; References L473–477 | script: no-dependence statement present; Author B ×2 (1 in-text + 1 entry), Author C ×2 (body), "(each under review)" 0; the three entry titles verified against the repo's actual paper titles |
| (10) preregistration-vocabulary consolidation | [both, cross-cutting] | IMPLEMENTED (Appendix A + four echo trims) | New Appendix A ("Declaration and registration vocabulary (consolidated)") defines the three register words once (**Declared** = fixed in this article's own record; **Registered** = attached to an archived record; **Preregistered** = the companions' scoring disciplines only, "nothing in this article is itself preregistered"); one §2.8 pointer; four body echoes trimmed ("without a declared map" → "except along one of the four"; "declared action space" ×2 → "action space"; "declared datum" → "specified datum"); strict main-body count 26 → 22 (the like-for-like region ahead of the statements; v19's full body is 28, of which 2 uses sit in the Supplementary-Material section after the References and are untouched) | Appendix A L449–454; §2.8 L115; trims at L83, L346, L397, L419 | script: Appendix A exactly once; pointer present; vocab counts pinned (v19 full body 28; v19 main body 26; v20 main body 22 — the original check's 28→24 compared unlike regions and was corrected, with the version-log claim updated to the true 26→22) |
| Housekeeping: supplementary pointer | — | IMPLEMENTED | `paper1_supplementary.md` → `paper1_supplementary_v2.md` with S8 named ("the machine artifact's twenty-five checks are enumerated in its S8") | L529 | script: stale v1 name 0, v2 name present, S8 named |

## Non-destructiveness

- Every markdown table line byte-identical, in order (machine-checked: the §4.5 action
  table and the §4.9 table).
- Frozen-value needles pinned with correct counts: $31^3 = 29{,}791$-state grid; scale 40;
  $e = (1/4, 1/4)$ ×2; rescue cost $c = 1$; $\rho_1 = \frac{2-s_1}{s_2}$; the witness
  tuples $(\tfrac12, \tfrac1{10}, \tfrac1{10})$ ×4 and $(\tfrac12, \tfrac65, \tfrac65)$;
  $(s_1, s_2) = (6/5, 6/5)$; the region displays; NO-SWITCH ×7; $r = w_2/w_1$ ×4; the
  $\delta$-range display. (Five needles were mis-spelled against the paper's actual
  notation and three expected counts were stale — all corrected to the paper's real
  forms and real counts; src = new for every needle.)
- No proof body changed beyond the mandated cross-reference relabels
  (Proposition 1/Lemma 2/Theorem 3/Theorem 6 → their new labels) — diff-verified hunk
  by hunk; Theorem 5's set displays and every recorded value byte-identical.
- The supplementary edit is append-only: 35 insertions, 0 deletions (git-verified);
  re-runs verify the S8 block byte-identically and never re-append.
- No new computations: the 25 checks' names and statuses are quoted verbatim from the
  committed results JSON; the E_end,typ witness is an inspection of the recorded
  action table, explicitly scoped as not machine-verified.

## Declines and partials

- **grok's $D_{\mathrm{agg}}$ re-letter for FP₀** — DECLINED: $D$ already names the
  disturbance class throughout; $\mathcal{Q}$ chosen instead (the audits' only
  constraint was one-letter-one-object).
- **The abstract's "a property of the menu's geometry" apposition** — trimmed under R8
  as redundancy (an apposition restating "structural", not a separate claim); recorded
  in the version log as the menu-geometry apposition trim.
- **Title change** — DECLINED with the reason recorded: no specific retitle is endorsed
  by the joint evaluation, and the title's claim is the operator-level separation the
  theorem literally proves; the §7 scoping sentences carry the anti-doctrinal reading
  instead.
- **Re-lettering $K$/$\varepsilon$ or renaming further collision letters inside frozen
  theorem statements** — out of scope (statement changes); the residual collisions are
  fenced in §2.8's scope paragraph instead.
- **S7's internal "Theorem 6" tokens** — left untouched (the supplementary is
  append-only under the repo rule); the S8 preamble records the naming note ("where
  S7's existing text says 'Theorem 6' the v20 status relabel reads Remark 6 — the
  statement numbers are unchanged, so every reference resolves by number").

## Check-audit log (the resumed pass)

Five stale count checks and one broken idempotency check were reconciled — every fix
makes the check's expected number and error message consistent with the actual
intended build (no build edit added or removed):

1. `'typed-endpoint' count` — expected 6 (message said 5); actual and intended **7**
   (all seven deposits itemized in the check's comment).
2. `E_end,typ count` — expected 5 was correct (message said 4); message fixed.
3. `productivity-illusion` — expected 2 of the spaced form; the intended build carries
   1 spaced (§1.1) + 1 hyphenated (§3.1); the check now counts both forms == 2.
4. vocabulary — expected 28 → 24 compared unlike regions (v19 full body vs v20
   pre-appendix); the like-for-like comparison is main-body 26 → 22; the version log's
   claim corrected accordingly.
5. frozen-needle expected counts — five needles mis-spelled against the paper's actual
   notation ($\rho_1$, the witness tuples, the region displays, the $\delta$-range) and
   three stale counts ($e = (1/4,1/4)$, NO-SWITCH, $r = w_2/w_1$); all corrected to the
   paper's real forms/counts.
6. S8 idempotency — the re-run recomputed `expected_supp` on the already-appended file
   and always failed ("divergent S8"); the check now verifies the file ends with the
   byte-identical S8 constant, exactly once, and never re-appends.

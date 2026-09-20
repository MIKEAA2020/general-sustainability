# Paper 1 (v47→v48) — residual audit round: second pass over `p1 audit.txt` (v1)

**Scope.** A second, place-by-place pass over the same three audit
streams (gemini / grok / deepseek), looking for remaining implementable
points after the v47 wave, plus bookkeeping corrections to the v47
verdicts report and an EMS-paper impact analysis.

**Numbering note.** The instruction said "v49"; the current line was
v47 (no v48 existed), so this residual round ships as
**`paper1_assessment_separation_v48.tex`/`.pdf`** (34 pp., compiled
clean). Nothing was skipped.

---

## 1. NEW genuine finding (own re-examination, cross-verified)

**§6.3 plan-menu glossary assigns FAST the wrong trough.** v46–v47
glossed "**FAST** (an immediate large quota cut … accepting a
mid-season **income** trough)". But the certified datum — verified in
the package benchmark (`FAST tubes: … s2 flat 6/5`) and stated in §6.3
itself ("with the income floor protected by its quota schedule, FAST's
exposure is the ecological floor") — has FAST's income floor **flat**
along the plan. The income trough is **SLOW**'s exposure (s₂: 6/5 →
−4/5 → 6/5, §6.3 mirror sentence). The three audits missed this; it is
the same exposure-swap class as the witness-assignment item grok
checked on the software side. **Fixed in v48**: FAST "accepting a
mid-season trough on the ecological floor, the plan's certified
exposure"; SLOW "shifting the burden onto the income floor".

## 2. Remaining audit points now implemented

| Item (stream) | v48 fix |
| --- | --- |
| Shared-DOI role distinction (grok): deposit descriptions overlap without distinguishing "this manuscript's artifact" from "the software library's checks" | §7 Availability rewritten: two explicit roles — (i) the 25-check exact-integer grid verifier + figures + search records for this paper; (ii) the SafeTransition library archive (its own separate 24-check benchmark suite); "the two check lists are distinct and are not pooled". Complements v47's §4.9 note |
| B-vs-s₁ unit mixing, residual site (deepseek C.17) | Strike sentence: "from the trough 17/10 kt to 6/5 kt" |
| LRP-anchor unit consistency (deepseek C.17 aftermath) | "opening stock (1.6 LRP units, …)" (was "1.6 floors"; matches the v47 "0.6 LRP units" fix) |

## 3. Bookkeeping correction to the v47 verdicts report

The v47 report omitted one deepseek finding from its tables:
**A.3/"missing Section 4.11 header"** (also deepseek E.21, "Sections
4.10–4.11 broken"). Verification during the v47 round had in fact
checked it — the compiled v46 PDF contains the header "4.11. The
converse: discrete time-sharing does not erase the gap" immediately
before Proposition 9, so the cross-reference "Sections 4.10–4.11"
resolves — but the refutation was not tabled. Recorded here:
**REFUTED** (header present; reference resolves). The v48 renumbering
does not affect this (the subsection remains §4.11, now containing
Proposition 10).

## 4. Re-examined and left unchanged, with reasons

| Item (stream) | Decision |
| --- | --- |
| Filippov/Warga given as textual eponyms in the v47 precision passage, without bibliography entries (gemini 2A aftermath) | Kept textual: both are pre-DOI-era monographs (Filippov 1988; Warga 1972); formal entries for one and not the other would be inconsistent referencing, and the names-as-notation convention ("the chattering limit of classical relaxed-control theory (Filippov; Warga)") is standard. A venue's copy-editor may request entries; deferring to that stage |
| Full-title parenthetical citations (gemini 3E-1, deepseek E.23) | Still declined — deliberate one-time disambiguation of four distinct 2026 companions before any lettered series exists |
| Elsevier footer date (gemini 3E-2, deepseek E.22) | Still declined — automatic class footer, correct at submission |
| Post-1975 "reachability" language, grid-verifier S8 pointer, S9/S10 pointers | Verified already correct; no action |

## 5. EMS-paper impact analysis (`p1 audit.txt` × the SafeTransition paper)

Audited item by item, the streams touch the EMS paper at exactly three
points, and none requires an EMS revision now:

1. **24-vs-25 check counts (gemini 3D, deepseek D.18).** The only
   cross-document item. The EMS paper's own claim ("twenty-four exact
   checks re-derive the companion deposit's benchmark") is accurate —
   24 is the fishery benchmark suite; 25 is paper 1's separate grid
   verifier. Paper 1 v47 (§4.9) and v48 (§7) now carry the full
   explanation on the side that raised it. *Optional symmetric
   one-clause note for the next scheduled EMS revision* ("the companion
   manuscript's separate grid verifier contributes a further 25
   checks"); not worth an EMS re-version on its own.
2. **Figure/witness cross-paper items (grok).** The alleged software
   Fig. 2(a) caption mismatch and the x = 3/2-vs-1/2 witness assignment
   were verified **stale**: both were already corrected in the 1.3.0 /
   EMS-v7 round ("at least one plan is aggregate-licensed at every
   admissible ratio"; FP witness at x = 1/2, rescue witness at x = 3/2).
   No action.
3. **Shared-DOI role overlap (grok).** Already addressed on the deposit
   side (master-deposit README's explicit role separation and dual
   citation entries); v48's availability rewrite completes the paper-1
   side. The EMS paper's availability section already cites the deposit
   for the software only. No action.

Everything else in `p1 audit.txt` (operator theory, blend window,
modulus, impossibility-region wording, chattering, section
numbering/cross-references, figure-pixel claims) is internal to paper 1
and has no statement in the EMS paper that depends on it — verified by
searching the EMS v7/master source for the affected phrases
("impossibility region", κ\* wording, tube-table lines, theorem
numbering): the EMS paper cites the companion results without
restating them, and its κ\* = max(0, 1−x) statement ("on the
non-typed-viable region") matches the v48-corrected failure-set
formulation exactly.

**EMS verdict: no changes required; the audit's only live cross-document
thread is now closed from the paper-1 side.**

## 6. Ship state

- `paper1_assessment_separation_v48.tex` / `.pdf` (34 pp.; v47
  preserved).
- New-file finding logged in §1 above (income-trough swap) — the one
  point all three audits missed, caught by checking the glossary
  against the certified tube data.
- Deposit and EMS paper: unchanged this round.

*Residual round: 1 new own finding fixed, 3 remaining audit points
implemented, 1 bookkeeping omission corrected, 4 items re-examined and
declined with reasons, EMS impact assessed as nil.*

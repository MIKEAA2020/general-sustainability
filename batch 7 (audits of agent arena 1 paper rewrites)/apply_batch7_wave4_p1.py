#!/usr/bin/env python3
"""
apply_batch7_wave4_p1.py — fail-loud build of paper1_assessment_separation_v20.md
from v19, plus the one allowed append (S8) to paper1_supplementary_v2.md.

Implements the wave-4 P1 docket (owner-directed, "cite, don't drop",
non-destructive):

  R8 [standing]  Abstract length: 310 -> 298 words by whitespace count (the
                 cap is <= 300); redundancy trimmed (menu-geometry apposition,
                 connective echoes), no claim removed. Count pinned below.
  (1) [both]     E_end,typ typed-endpoint operator: a Definition (not a
                 computation) deposited in Section 3.1 where the photograph
                 claim is used, with its one-line witness taken from the
                 recorded action table and the proof of Theorem 5(1), and the
                 machine artifact's coverage stated (physical endpoint only).
                 Section 5.4's Fourth implication cites it.
  (2) [both]     Section 1.1 companion-prose strip: the cycle-closure/waste
                 paragraph and the hen/orchard/productivity-illusion block
                 are stripped to one crisp statement each plus a citation of
                 the companion ledger study (Author, A., et al., in review;
                 reference entry added); the witness-inconsistent
                 base-vs-services sentence corrected to the floor reading.
  (3) [both]     Section 2's 13-slot tuple display restructured as a named
                 record (the typed assessment datum S) with the fields defined
                 in the Supplementary Material (S1) and instantiated field by
                 field in Section 2.7 — cite, don't drop.
  (4) [both]     Notation pass: FP_0 re-lettered Q (11 sites; the figure image
                 carries I = FP_agg and R only, verified, so no image-text
                 mismatch); r frozen as the weight ratio w2/w1 with Section
                 5.5's resource increment re-lettered kappa (Aug_kappa,
                 A_kappa, kappa*, STAGED_kappa); the action-set drift |A|=4
                 and "whether A is exhaustive" written on cal(A); Section 2.8
                 gains the two-scope fences (R; A vs cal(A); e vs e_k) and the
                 S = S_0 identification.  FP_agg kept (figure-pinned, glossed
                 at every site; the docket names FP_0 only).
  (5) [both]     Demotions: Proposition 1 -> Remark 1, Lemma 2 -> Remark 2,
                 Theorem 3 -> Proposition 3, Theorem 6 -> Remark 6 — status
                 relabels on the UNCHANGED 1-9 statement counter, no
                 renumbering, no proof changes, every cross-reference updated
                 (counts pinned below), one-line reason per demotion in the
                 version log.
  (6) [both]     Title/Section 7 doctrinal sound: no specific retitle is
                 endorsed by the joint evaluation, so the title is unchanged
                 (decision recorded) and Section 7 gains scoping sentences;
                 Theorem 8 stated as the paper's own delimitation.
  (7) [both]     The 25 checks: enumerated one by one in the appended S8 of
                 paper1_supplementary_v2.md (values verbatim from the
                 committed results JSON, nothing recomputed); the main text
                 keeps the count and a one-sentence pointer.
  (8) [both]     Section 6.1 unpublished-companion dependence scoped: the
                 scored forecast-evaluation companions cited in text and in
                 the References (Author, B./C., et al., in review), plus the
                 explicit no-dependence statement.
  (10) [both]    Preregistration-vocabulary consolidation: Appendix A carries
                 the declared/registered/preregistered convention once, with
                 one Section 2.8 pointer and four body echo trims (strict
                 main-body count, the article text ahead of the statements and
                 references: 26 -> 22, pinned; the full body incl. the
                 Supplementary-Material section is 28 at v19, 2 of which sit
                 after the References).
  Housekeeping   Supplementary pointer paper1_supplementary.md ->
                 paper1_supplementary_v2.md with S8 named.

Non-destructive: no frozen verdict, region identity, table row, or recorded
number changes anywhere. The action table and the Section 4.9 table are
byte-identical (pinned). Every anchored edit asserts its anchor occurs
exactly once; every mechanical check fails loudly. Re-running the script
rebuilds v20 byte-identically and re-verifies the (idempotent) S8 append.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper1_assessment_separation_v19.md")
DST = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper1_assessment_separation_v20.md")
SUPP = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                    "paper1_supplementary_v2.md")


def sub1(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [anchor {label}]: expected exactly 1 occurrence, found {n}")
    return text.replace(old, new)


def subn(text, old, new, expected, label):
    n = text.count(old)
    if n != expected:
        raise SystemExit(f"FAIL [anchor {label}]: expected {expected} occurrences, found {n}")
    return text.replace(old, new)


def body_of(text, log_tag):
    """The main body: everything except the (single) version-log line."""
    lines = text.splitlines()
    logs = [i for i, l in enumerate(lines) if l.startswith(f"*Version log ({log_tag}).*")]
    if len(logs) != 1:
        raise SystemExit(f"FAIL: version log ({log_tag}) not exactly once")
    return "\n".join(l for i, l in enumerate(lines) if i != logs[0])


def vocab_count(text):
    """Strict preregistration-vocabulary hits (the joint evaluation's count)."""
    return len(re.findall(r"declared|registered|preregistered|pre-registered", text))


def abstract_text(text):
    i = text.find("## Abstract")
    j = text.find("**Keywords:**")
    if i == -1 or j == -1 or j < i:
        raise SystemExit("FAIL: abstract boundaries")
    return text[i + len("## Abstract"):j].strip()


# --------------------------------------------------------------------- S8 block
S8 = """

---

## S8. The 25-Check Enumeration (Wave-4 Deposit)

*Appended at the wave-4 revision (main-text v20), on the joint audit's "which 25 checks?" item. The machine checks of the verification artifact (main-text Section 4.9; S7 above) are enumerated here one by one. Each entry quotes the check's recorded name verbatim from the committed results file (`research_program/paper1_instantiation/typed_false_positive_instantiation.json`, execution of 2026-08-28, deterministic, exact integer arithmetic at scale 40, exit 0) and states the main-text claim it maps to. Nothing is recomputed here and no value is new; every check's recorded pass status is True (25/25). Two naming notes: the artifact's own tokens "FP" and "FP0" name the discrepancy region $\\mathcal{Q}$ of the main text's v20 notation (formerly $\\mathrm{FP}_0$), and where S7's existing text says "Theorem 6" the v20 status relabel reads Remark 6 — the statement numbers are unchanged, so every reference resolves by number.*

1. *FAST breakpoint table exact (dip at t=1/2, recovery at t=1)* — the FAST row of the main-text Section 4.5 action table.
2. *STAGED breakpoint table exact (linear spend/growth)* — the STAGED row of the same table.
3. *per-coordinate exact ranges = breakpoint extremes (piecewise monotone)* — Section 4.5's declaration that every worst-case tube is the exact visited set.
4. *worst-case dip constants: benign 3/2, adverse 2, floor threshold 2* — Section 4.5's disturbance convention (worst-case dip of fixed depth 2; the artifact's benign 3/2 scaling is part of its configuration).
5. *machine typed-feasibility == {x>=1} ∪ {s1>=2} ∪ {s2>=2} on every grid state* — Theorem 5(1).
6. *machine all-weights admissibility == {x>=1} ∪ {s1+s2>=2} on every grid state* — Theorem 5(2).
7. *FAST/SLOW per-weight safety biconditionals confirmed on every grid state (dense r-grid)* — Theorem 5(6).
8. *boundary weights exact: FAST safe at r=rho_1, SLOW safe at r=rho_2 (witness state (1/2, 6/5, 6/5))* — Theorem 5(6), with the boundary conventions of Section 4.6.
9. *machine endpoint-only feasibility == all of X_0 on every grid state* — Theorem 5(3) (the physical endpoint operator).
10. *typed ⇒ all-weights-aggregate ⇒ endpoint-only (no violations on the grid)* — the hierarchy of Proposition 3(i).
11. *false-positive set nonempty on the grid* — Theorem 5(4); the artifact records 1,900 grid states in the set.
12. *interior witness (1/2, 6/5, 6/5): aggregate-feasible for every critical weight, typed-INfeasible, endpoint-feasible* — Theorem 5(4)–(5), first strictness.
13. *witness is an interior point (all ±0.1 neighbors remain in FP)* — Theorem 5(4)'s nonempty open interior.
14. *endpoint-only witness (1/2, 1/10, 1/10): endpoint-feasible, aggregate-INfeasible (no action safe at w=(1,1))* — Theorem 5(5), second strictness.
15. *aggregate-vs-typed strictness witness (the FP interior point above)* — Theorem 5(5).
16. *r=1/2: SLOW-only (FAST unsafe, SLOW safe)* — Theorem 5(6), per-weight plan disagreement.
17. *r=1: both plans safe* — Theorem 5(6).
18. *r=2: FAST-only (SLOW unsafe, FAST safe)* — Theorem 5(6).
19. *E_typ = ∩_w E_w = ∅ machine-verified (no action serves every critical weight)* — Proposition 3(ii) on the witness.
20. *R witness (3/2, 6/5, 6/5): typed-transformable via STAGED (bridging plan at physical cost c=1)* — Theorem 5(7), the rescue.
21. *I witness (1/2, 6/5, 6/5): all four actions rejected, each with its exhibited violated constraint (negative-certificate form)* — Theorem 5(7), the impossibility.
22. *rescue split verified on the whole grid: FP0∩{x>=1} typed-feasible via STAGED; FP0∩{x<1} typed-infeasible* — Theorem 5(4) and (7).
23. *stage-0 hierarchy holds and regions are preserved through two hold intervals (every grid state)* — Remark 6.
24. *FP strictness witness survives the holds at stage 0* — Remark 6(ii).
25. *endpoint-only strictness witness survives the holds at stage 0* — Remark 6(ii).

Every recorded pass status is True, and re-execution reproduces the outputs exactly (S7). The main text keeps the count and the pointer; this deposit is the enumeration.
"""

S8_HEADER = "## S8. The 25-Check Enumeration (Wave-4 Deposit)"

# --------------------------------------------------------------- Appendix A
APPENDIX_A = """## Appendix A. Declaration and registration vocabulary (consolidated)

This appendix consolidates the declaration and registration vocabulary that the body uses, so that each register word carries one fixed meaning and one home. **Declared** fixes an object in this article's own record: the witness datum, its disturbance class, action menu, safe and destination sets, reset, and the model maps of Section 2.4 are declared at their use sites (Sections 2 and 4.5); at any other site, "declared" means exactly this — an explicit, checkable specification. **Registered** attaches a computational or policy object to an archived record: the machine artifact's grid, box endpoints, and verification set are registered with the artifact (Section 4.9; Supplementary S7), and the action-set completeness statuses of Section 5.5 — an exhaustive set, a registered policy menu, a sampled subset, an inner approximation — are the empirical-application registers. **Preregistered** appears in this article only for the companion studies' scoring disciplines (Section 6.1), which belong to those analyses; nothing in this article is itself preregistered. The claim-status rules of Section 2.5 — no promotion, no silent transfer — govern the labelling throughout.

---

"""


def main():
    t = open(SRC, encoding="utf-8").read()
    src_text = t

    # ================= stage 1: global relabels (count-asserted) =================
    # (5) demotions: status relabels on the unchanged 1-9 counter.
    t = subn(t, "Proposition 1", "Remark 1", 7, "demote P1->R1")
    t = subn(t, "Lemma 2", "Remark 2", 7, "demote L2->R2")
    t = subn(t, "Theorem 3", "Proposition 3", 13, "demote T3->P3")
    t = subn(t, "Theorem 6", "Remark 6", 8, "demote T6->R6")
    # (4) FP_0 -> Q (grok's D_agg rejected: D names the disturbance class;
    # the figure image carries only I = FP_agg and R, verified by OCR).
    t = subn(t, "\\mathrm{FP}_0", "\\mathcal{Q}", 11, "reletter FP0->Q")

    # ================= stage 2: R8 abstract cut (310 -> 298) =====================
    t = sub1(t,
        "under exact-tube semantics, in which a transition is safe only if "
        "every state along the path, not merely the endpoint, satisfies the "
        "constraints.",
        "under exact-tube semantics: a transition is safe only if every state "
        "along the path, not merely the endpoint, satisfies the constraints.",
        "abs-1")
    t = sub1(t,
        "is exactly this impossibility region, which has nonempty open interior.",
        "is exactly this impossibility region, with nonempty open interior.",
        "abs-2")
    t = sub1(t,
        "menu convexification — admitting convexified actions whose worst-case "
        "tubes are convex combinations of the primitive ones —",
        "menu convexification — convexified actions whose worst-case tubes are "
        "convex combinations of the primitive ones —",
        "abs-3")
    t = sub1(t,
        "The \"only\" claim is scoped to the deterministic menu, within which "
        "the separation is structural — a property of the menu's geometry — "
        "not an artefact of a poor choice of weights",
        "The \"only\" claim is scoped to the deterministic menu, within which "
        "the separation is structural, not an artefact of a poor choice of "
        "weights",
        "abs-4")

    # ================= stage 3: (2) Section 1.1 companion-prose strip ============
    t = sub1(t,
        "Read in this paper's terms, the two traditions are not competing "
        "philosophies but regimes of one system. They are distinguished not by "
        "whether substitution alone keeps pace with depletion, but by whether "
        "the material cycle can be closed at the rate of use. The "
        "weak-sustainability regime is the idealized one in which humans "
        "consume and populate slowly enough that technological substitution "
        "and natural regeneration together redistribute matter so that it is "
        "used as it arises. On human-relevant timescales substitution is the "
        "dominant term, with natural regeneration acting far more slowly — "
        "often on deep-time scales — and included for physical completeness "
        "rather than as a co-equal mechanism (Daly, 1990). In this idealized "
        "closure the byproducts of use — carbon drawn from the atmosphere, "
        "chemical substances released to air, water, and soil — are returned "
        "to use in time and are therefore not waste. Waste is here a "
        "relational status, not an intrinsic property of any material: it is "
        "the matter that, under the present relation and circumstances, "
        "accumulates because it cannot be put to immediate use for lack of "
        "knowledge, technology, or timely redistribution. A chemical substance "
        "that is a product in one context is waste-in-waiting in another, and "
        "no substance is waste by its nature. The strong-sustainability "
        "regime is the one in which that closure fails: the rate of use "
        "exceeds the rate at which substitution and regeneration can re-loop "
        "the matter, so what would have dissolved into use instead "
        "accumulates as waste or shows up as a local depletion. The driver is "
        "the consumption rate — the same substances close the loop at a rate "
        "the cycle can absorb and fail to close it at one it cannot.",
        "Read in this paper's terms, the two traditions are distinguished by "
        "whether compensatory substitution keeps pace with depletion. The "
        "material-cycle reading of that distinction — waste as a relational "
        "status, the closure of the material cycle at the rate of use, "
        "substitution against deep-time renewal — is developed for the "
        "companion ledger study (Author, A., et al., in review) and is not "
        "re-argued here; no theorem of this paper touches material cycles. "
        "The doctrines this paper does compare are the formalized operators "
        "of Section 5.1.",
        "s11-strip-regimes")

    t = sub1(t,
        "The masking this paper formalises has a concrete picture. A farm may "
        "keep one healthy hen — or one full orchard — while the pond behind "
        "it is drained and the soil is mined to keep it that way. The "
        "productive base — the hen, the trees, the aquifer — can be read in "
        "more than one way at once: as natural capital, as a stock, and as a "
        "slowly regenerating flow of services. These are not mutually "
        "exclusive interpretations but different lenses on the same asset. "
        "Reading the hen or the tree as a slow-generating flow is "
        "instructive precisely because it shows that the flow–stock "
        "distinction is not a strict membership test.\n\n"
        "Against any single asset the operative question is why a use is "
        "sustainable. A use that falls on the yield leaves the base intact, "
        "while one that falls on the base itself is liquidation. Across "
        "assets, what makes the distinction a continuum rather than a hard "
        "line is the regeneration timescale relative to the rate of use. An "
        "apple crop renews within a year, a forest within decades, an aquifer "
        "over years to centuries, and a fossil-fuel or mineral deposit over "
        "geological time. A fast-recovering base therefore behaves as a flow; "
        "a geologically slow one as a stock. If a base regenerates too slowly "
        "for the rate at which it is taken, drawdown is still liquidation.\n\n"
        "An aggregate of services can therefore appear adequate while it is "
        "read off a single component and the supporting base is reduced "
        "quietly. Measured output need not fall in the present even as the "
        "condition of the system that produces it declines, provided the "
        "decline is not yet reflected in the measured service or is offset by "
        "higher per-unit service. Otherwise output falls with the base. A "
        "\"still delivering\" signal at the level of output can thus mask a "
        "decline at the level of the productive base. Call this the "
        "*productivity illusion*: the appearance of adequate delivery while "
        "the base that sustains the delivery is being reduced.\n\n"
        "The compensatory form singled out here is the illusion as it arises "
        "in aggregation. It is an aggregate of services read as adequate "
        "while the supporting base of one component is liquidated. This is "
        "the structure the separation results of this paper examine: for "
        "every nonnegative scalarization weight, some action can hold the "
        "weighted aggregate floor along its tube while no single action holds "
        "every typed floor — the acceptance gap of Theorem 5(4), the "
        "impossibility region. The component the aggregate does not see is "
        "the typed floor that the common-plan criterion refuses to "
        "compromise. On the witness, that floor is a constraint on the "
        "productive base itself, not on the services it happens to yield.",
        "The masking this paper formalises needs one sentence, not a parable: "
        "an aggregate of two typed floors can stay nonnegative along its "
        "worst-case tube while each floor in turn takes a dip that no common "
        "plan accepts. The narrative that usually carries the point — the "
        "farm that keeps one healthy hen or one full orchard while the pond "
        "behind it drains and the soil is mined, the *productivity illusion* "
        "of adequate delivery from a quietly reduced base — belongs to the "
        "companion ledger study (Author, A., et al., in review), where the "
        "productive base sits inside the ledger. On this paper's witness the "
        "aggregate is taken over the two service floors $s_1, s_2$ "
        "themselves; what it fails to see is not the base but the individual "
        "floor mid-interval — the compensatory form of the illusion as it "
        "arises in aggregation, the acceptance gap of Theorem 5(4).",
        "s11-strip-masking")

    # ================= stage 4: (3) Section 2.2 named record =====================
    t = sub1(t,
        "### 2.2 The canonical tuple\n\n"
        "The canonical object is the tuple\n"
        "$$\\mathfrak{S} = (T, Z, S_{st}, B_{out}, V, \\Gamma, O, A, C, R, D, "
        "K, P),$$\n"
        "comprising a type system $T$; state space $Z$; stock–flux structure "
        "$S_{st}$; boundary interface $B_{out}$; constitutive laws $V$; "
        "service–technology correspondence $\\Gamma$; observation operator "
        "$O$; assessment operator $A$; command architecture $C$; "
        "deployment/reset architecture $R$; disturbance class $D$; "
        "safe-and-just set $K$; and policy class $P$. A model is a specified "
        "tuple; a claim is a statement about a tuple with a status; an "
        "application is a tuple plus data. Throughout this paper $P$ denotes "
        "the policy class; accepted-state sets use the distinct notation "
        "$\\mathcal{V}[\\cdot]$ introduced in Section 3.2. The weight cone of "
        "Section 3.1 is written $W$, the command architecture keeps the "
        "letter $C$, and the action set of Section 5.5 is written "
        "$\\mathcal{A}$ — the three objects never share a symbol.",
        "### 2.2 The canonical datum as a named record\n\n"
        "The canonical object is a named record — the typed assessment datum "
        "$\\mathfrak{S}$ — whose thirteen fields are the type system, state "
        "space, stock–flux structure, boundary interface, constitutive laws, "
        "service–technology correspondence, observation operator, assessment "
        "operator, command architecture, deployment/reset architecture, "
        "disturbance class, safe-and-just set, and policy class. The "
        "field-by-field definitions are carried by the Supplementary Material "
        "(S1), and Section 2.7 records the witness's instantiation field by "
        "field. A model is a specified record; a claim is a statement about a "
        "record with a status; an application is a record plus data. The "
        "results consume the essential typed fields — the state space $Z$ "
        "with its typed floors, the action menu, the disturbance class $D$, "
        "the safe-and-just set $K$ (the witness's transition-safe set $S_0$), "
        "and the destination set $G$, under the tube and successor semantics "
        "of Section 3.1. Throughout this paper $P$ denotes the policy class; "
        "accepted-state sets use the distinct notation $\\mathcal{V}[\\cdot]$ "
        "introduced in Section 3.2. The weight cone of Section 3.1 is written "
        "$W$, the command architecture keeps the letter $C$, and the action "
        "set of Section 5.5 is written $\\mathcal{A}$ — the three objects "
        "never share a symbol.",
        "s22-named-record")
    t = sub1(t,
        "the mapping is recorded here so that the tuple is a specialization "
        "map rather than parallel text",
        "the mapping is recorded here so that the datum is a specialization "
        "map rather than parallel text",
        "s27-harmonise")

    # ================= stage 5: (4) notation pass — Section 2.8 ==================
    t = sub1(t,
        "$P$: policy class. The full tuple is $\\mathfrak{S}$ (Section 2.2).",
        "$P$: policy class. The full record is $\\mathfrak{S}$, its fields "
        "defined in the Supplementary Material (S1).",
        "s28-record-tail")
    t = sub1(t,
        "$r = w_2 / w_1$: the weight ratio used on the witness.",
        "$r = w_2 / w_1$: the weight ratio used on the witness and frozen to "
        "that reading (the resource increment of Section 5.5 is $\\kappa$).",
        "s28-r-frozen")
    t = sub1(t,
        "$S^{\\mathrm{phys}}, G^{\\mathrm{phys}}$: their physical counterparts.",
        "$S^{\\mathrm{phys}}, G^{\\mathrm{phys}}$: their physical counterparts; "
        "on the witness $S = S_0$, the transition-safe set of Section 4.5, "
        "while $s$ is the floor vector and $S_{st}$ the tuple's stock–flux "
        "field — distinct objects, never shared.",
        "s28-S-fence")
    t = sub1(t,
        "$E_{\\mathrm{end}}(z)$: the four assessment operators of Section 3.1.",
        "$E_{\\mathrm{end}}(z)$, $E_{\\mathrm{end,typ}}(z)$: the assessment "
        "operators of Section 3.1 — the last the typed-endpoint Definition "
        "deposited for the photograph reading of Section 5.4.",
        "s28-operators")
    t = sub1(t,
        "- $\\mathcal{A}$: action set of Section 5.5; $\\mathsf{Aug}_r$: the "
        "resource-augmentation map; $r^*$: the minimal rescue threshold.",
        "- $\\mathcal{A}$: the action set (Sections 4.1 and 5.5); "
        "$\\mathsf{Aug}_\\kappa$: the resource-augmentation map, with "
        "increment $\\kappa$ and minimal rescue threshold $\\kappa^*$; the "
        "letter $r$ never denotes the increment.\n"
        "- Two letters carry two scopes, never in the same equation: $R$ is "
        "the tuple's deployment/reset architecture (Sections 2.2 and 2.7; "
        "Supplementary S1) and the rescue set of Theorem 5 — every theorem "
        "reference and Figure 1 use the rescue-set reading; $A$ is the "
        "tuple's assessment operator, while the action set is "
        "$\\mathcal{A}$; the gain vector $e$ of the witness datum (never "
        "subscripted) and the standard basis vector $e_k$ of Remark 2's "
        "proof are distinct objects.",
        "s28-kappa-fences")
    t = sub1(t,
        "The four-symbol display on the witness (Section 4.5) uses "
        "$\\beta, \\alpha$ for the action-indexed disturbances; these are not "
        "reused elsewhere.",
        "The four-symbol display on the witness (Section 4.5) uses "
        "$\\beta, \\alpha$ for the action-indexed disturbances; these are not "
        "reused elsewhere.\n\n"
        "The declaration, registration, and preregistration vocabulary of "
        "this article is consolidated in Appendix A.",
        "s28-vocab-pointer")

    # ================= stage 6: (1) E_end,typ in Section 3.1 =====================
    t = sub1(t, "### 3.1 Four operators", "### 3.1 Five operators", "s31-header")
    t = sub1(t,
        "Four operators are distinguished; they share the same disturbance "
        "quantifier and differ in constraint structure, with one additional "
        "difference for the fourth: the endpoint operator also replaces the "
        "tube evaluation map by the endpoint map.",
        "Five operators are distinguished; they share the same disturbance "
        "quantifier and differ in constraint structure, with one additional "
        "difference for the fourth: the endpoint operator also replaces the "
        "tube evaluation map by the endpoint map. The fifth, defined after "
        "the chain, is the typed-endpoint operator deposited so that the "
        "photograph reading of Section 5.4 states its own witness.",
        "s31-five")
    t = sub1(t,
        "A photograph of output cannot in general certify the condition of "
        "the system that produced it, since output can be maintained in the "
        "present while the productive base is being reduced (Section 1.1).",
        "A photograph of output cannot in general certify the condition of "
        "the system that produced it — the productivity-illusion reading "
        "developed for the companion ledger study (Author, A., et al., in "
        "review) — and the typed-endpoint operator defined below makes the "
        "floor-level version of the claim exact on the witness.",
        "s31-photograph")
    t = sub1(t,
        "holds for every $w \\in W_+$ (Proposition 3(i) below). The last "
        "inclusion is strict in general, though it collapses on the witness "
        "of Section 4.5 because the witness's physical constraint touches "
        "only the monotone reserve stock.",
        "holds for every $w \\in W_+$ (Proposition 3(i) below). The last "
        "inclusion is strict in general, though it collapses on the witness "
        "of Section 4.5 because the witness's physical constraint touches "
        "only the monotone reserve stock.\n\n"
        "The **typed-endpoint** operator (typed floors at endpoints only) is "
        "deposited here as a Definition, so that the photograph reading of "
        "Section 5.4 states its own witness:\n"
        "$$E_{\\mathrm{end,typ}}(z) = \\{ a : \\forall d,\\; "
        "\\mathrm{End}(a,d) \\subseteq S \\ \\text{ and } \\ "
        "\\mathrm{Succ}(a,d) \\subseteq G \\}.$$\n"
        "It sits between the chain's first and last links, "
        "$E_{\\mathrm{typ}}(z) \\subseteq E_{\\mathrm{end,typ}}(z) \\subseteq "
        "E_{\\mathrm{end}}(z)$, by the recorded inclusions "
        "$\\mathrm{End}(a,d) \\subseteq \\mathrm{Tube}(a,d)$, $S \\subseteq "
        "S^{\\mathrm{phys}}$, and $G \\subseteq G^{\\mathrm{phys}}$ — "
        "one-line set facts, not part of Proposition 3(i). On the witness "
        "datum of Section 4.5 it carries a one-line witness of the photograph "
        "claim: FAST's endpoint values of $s_1$ equal the initial $s_1$, and "
        "its successor lies in $G$ whenever $x \\ge 0$ (the action table and "
        "the proof of Theorem 5(1)), so $E_{\\mathrm{end,typ}}(z) \\neq "
        "\\varnothing$ at every $z \\in X_0$, while $E_{\\mathrm{typ}}(z)$ "
        "requires $s_1 \\ge 2$ (Theorem 5(1)). The machine artifact of "
        "Section 4.9 checks the physical endpoint operator only; this "
        "typed-endpoint observation is asserted by inspection of the "
        "recorded action table, not machine-verified.",
        "s31-endtyp-block")

    # ================= stage 7: (5) demotion descriptors =========================
    t = sub1(t,
        "### 4.1 A general quantifier-separation proposition",
        "### 4.1 A general quantifier-separation remark",
        "s41-header")
    t = sub1(t,
        "(ii) A general quantifier-separation proposition (Remark 1).",
        "(ii) A general quantifier-separation remark (Remark 1).",
        "s13-claimed-ii")
    t = sub1(t,
        "(ii) The general quantifier-separation proposition (Remark 1).",
        "(ii) The general quantifier-separation remark (Remark 1).",
        "s52-claimed-ii")

    # ================= stage 8: (4) kappa re-letter in Section 5.5 ===============
    t = sub1(t,
        "$$\\mathsf{Aug}_r : (x, s, \\mathcal{A}) \\mapsto (x + r,\\; s,\\; "
        "\\mathcal{A} \\cup \\{\\mathrm{STAGED}_r\\})$$",
        "$$\\mathsf{Aug}_\\kappa : (x, s, \\mathcal{A}) \\mapsto (x + "
        "\\kappa,\\; s,\\; \\mathcal{A} \\cup \\{\\mathrm{STAGED}_\\kappa\\})$$",
        "s55-aug")
    t = sub1(t,
        "$$r^* = \\inf\\{\\, r : \\exists a \\in \\mathcal{A}_r,\\; a \\in "
        "E_{\\mathrm{typ}}(z) \\,\\},$$",
        "$$\\kappa^* = \\inf\\{\\, \\kappa : \\exists a \\in "
        "\\mathcal{A}_\\kappa,\\; a \\in E_{\\mathrm{typ}}(z) \\,\\},$$",
        "s55-kstar")
    t = sub1(t,
        "where $\\mathcal{A}_r$ denotes the augmented menu. On the witness, "
        "for the STAGED action and $x < 1$: $r^* = 1 - x$, the exact resource "
        "increment",
        "where $\\mathcal{A}_\\kappa$ denotes the augmented menu. On the "
        "witness, for the STAGED action and $x < 1$: $\\kappa^* = 1 - x$, the "
        "exact resource increment",
        "s55-kstar-witness")
    t = sub1(t, "$|A| = 4$", "$|\\mathcal{A}| = 4$", "A-drift-1")
    t = sub1(t, "whether $A$ is exhaustive",
             "whether $\\mathcal{A}$ is exhaustive", "A-drift-2")

    # ================= stage 9: (1) Section 5.4 Fourth implication ===============
    t = sub1(t,
        "Under those semantics they license transitions that violate typed "
        "floors mid-interval without the assessment detecting it; the "
        "per-floor reporting of the Third implication is what detects the "
        "discrepancy.",
        "Under those semantics they license transitions that violate typed "
        "floors mid-interval without the assessment detecting it (the "
        "typed-endpoint operator $E_{\\mathrm{end,typ}}$ of Section 3.1 is "
        "the one-line witness: on the witness datum, FAST is "
        "typed-endpoint-admissible at every state of $X_0$ while "
        "typed-tube-admissible only for $s_1 \\ge 2$ — an inspection of the "
        "recorded action table, not one of the artifact's 25 checks); the "
        "per-floor reporting of the Third implication is what detects the "
        "discrepancy.",
        "s54-fourth")

    # ================= stage 10: (7) Section 4.9 pointer + listings ==============
    t = sub1(t,
        "The continuum statements of Theorems 3, 5–8 and Proposition 4 are "
        "established by the displayed proofs.",
        "The continuum statements of Proposition 3, Proposition 4, Theorem 5, "
        "Remark 6, and Theorems 7–8 are established by the displayed proofs.",
        "s49-listing-1")
    t = sub1(t,
        "checks the finite rational instance of Proposition 3, Proposition 4, "
        "and Theorems 5–6:",
        "checks the finite rational instance of Proposition 3, Proposition 4, "
        "Theorem 5, and Remark 6:",
        "s49-listing-2")
    t = sub1(t,
        "All 25 checks pass; re-execution reproduces the outputs exactly.",
        "All 25 checks pass; re-execution reproduces the outputs exactly; the "
        "checks are enumerated one by one, with their recorded pass status, "
        "in the Supplementary Material (S8).",
        "s49-s8-pointer")

    # ================= stage 11: (8) Section 6.1 companion scoping ===============
    t = sub1(t,
        "The admission discipline is the same one the empirical companion "
        "analyses (each under review) instantiate — preregistered scoring "
        "against declared baselines, held-out defect audits, frozen retention "
        "rules — and those empirical results belong to those analyses, not "
        "here.",
        "The admission discipline is the same one the empirical companion "
        "analyses of this research programme instantiate — preregistered "
        "scoring against declared baselines, held-out defect audits, frozen "
        "retention rules — and those empirical results belong to those "
        "analyses, not here (the scored forecast-evaluation studies of the "
        "cod and Edwards Aquifer systems, each under separate review: "
        "Author, B., et al., in review; Author, C., et al., in review). No "
        "result of this article depends on an unpublished companion: the "
        "separation results rest on their displayed proofs, the machine "
        "artifact of Section 4.9 is deposited independently, and this "
        "manuscript's companion dependence is confined to the introduction's "
        "citation of the ledger study (Author, A., et al., in review) and the "
        "disciplinary analogy of this paragraph.",
        "s61-companions")

    # ================= stage 12: (6) Section 7 scoping ===========================
    t = sub1(t,
        "This paper shows that their divergence survives translation into "
        "assessment mechanics, at the level of a theorem.",
        "This paper shows that the divergence of the two doctrines as "
        "formalized here — the scalarized-aggregate and typed operators of "
        "Section 3.1 on a common action menu and disturbance class — "
        "survives translation into assessment mechanics, at the level of a "
        "theorem about those operators. The theorem ranks no doctrine: "
        "Section 5.1 scopes the formalizations, and after Theorem 8 the "
        "structural character of the separation is a property of the finite "
        "deterministic menu, not of weak or strong sustainability as "
        "traditions (Sections 4.10–4.11).",
        "s7-scoping")

    # ================= stage 13: (10) Appendix A + echo trims ====================
    t = sub1(t, "## Data availability statement",
             APPENDIX_A + "## Data availability statement", "appendix-A-insert")
    t = sub1(t,
        "This paper needs only the taxonomy and the discipline it enforces. "
        "The discipline is that no claim transfers from one model to another "
        "without a declared map.",
        "This paper needs only the taxonomy and the discipline it enforces. "
        "The discipline is that no claim transfers from one model to another "
        "except along one of the four.",
        "trim-s24")
    t = sub1(t,
        "The nonconvexity at work is menu geometry — the finiteness and "
        "determinism of the declared action space — not the Pareto-frontier "
        "geometry",
        "The nonconvexity at work is menu geometry — the finiteness and "
        "determinism of the action space — not the Pareto-frontier geometry",
        "trim-s410")
    t = sub1(t,
        "Fractional action policies are not members of the declared action "
        "space, and every stated separation is scoped to the finite "
        "deterministic menu.",
        "Fractional action policies are not members of the action space, and "
        "every stated separation is scoped to the finite deterministic menu.",
        "trim-s53")
    t = sub1(t,
        "The theorem is a result about assessment operators on a declared "
        "datum. Empirical application requires, in addition",
        "The theorem is a result about assessment operators on a specified "
        "datum. Empirical application requires, in addition",
        "trim-s55")

    # ================= stage 14: references + supplementary pointer ==============
    t = sub1(t,
        "Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). *Viability "
        "Theory: New Directions*, 2nd ed. Birkhäuser, Boston.\n\nBen-Tal, A.,",
        "Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). *Viability "
        "Theory: New Directions*, 2nd ed. Birkhäuser, Boston.\n\n"
        "Author, A., et al., in review. Typed flux ledgers and depletion "
        "arithmetic: conservation, componentwise diagnostics, and the "
        "semantics of depletion horizons. Companion material-ledger study.\n\n"
        "Author, B., et al., in review. Does a surplus-production ladder "
        "improve forecasts of Northern cod? A scored test on NAFO 2J3KL. "
        "Companion scored forecast-evaluation study (the cod side).\n\n"
        "Author, C., et al., in review. Does a one-pool water-balance model "
        "improve forecasts of Edwards Aquifer head? A scored test at J-17. "
        "Companion scored forecast-evaluation study (the Edwards Aquifer "
        "side).\n\nBen-Tal, A.,",
        "refs-companions")
    t = sub1(t,
        "are provided in the accompanying supplementary file "
        "`paper1_supplementary.md`, together with their status declarations.",
        "are provided in the accompanying supplementary file "
        "`paper1_supplementary_v2.md`, together with their status "
        "declarations; the machine artifact's twenty-five checks are "
        "enumerated in its S8.",
        "supp-pointer")

    # ================= stage 15: version log (last) ==============================
    old_log_start = "*Version log (v19).*"
    idx = t.find(old_log_start)
    if idx != t.find("\n*Version log") + 1 or t.count(old_log_start) != 1:
        raise SystemExit("FAIL: v19 version log anchor")
    log_end = t.find("\n\n## Abstract", idx)
    if log_end == -1:
        raise SystemExit("FAIL: version log terminator")
    new_log = (
        "*Version log (v20).* Implements the wave-4 items of the joint-audit "
        "evaluation's P1 remaining-points list (R8 and the eight structural "
        "docket items plus the preregistration-vocabulary consolidation), "
        "owner-directed as cite-not-drop and non-destructive. (R8) The "
        "abstract is cut from 310 to 298 words — the menu-geometry apposition "
        "and connective echoes trimmed, no claim removed — and the count is "
        "pinned in the build. (Docket 1, typed endpoint) Section 3.1 defines "
        "the fifth operator $E_{\\mathrm{end,typ}}$ (typed floors at "
        "endpoints only) with its one-line witness — on the witness datum "
        "FAST is typed-endpoint-admissible at every state of $X_0$ while "
        "typed-tube-admissible only for $s_1 \\ge 2$ — and Section 5.4's "
        "Fourth implication cites it; the observation is an inspection of the "
        "recorded action table, not one of the artifact's 25 checks. (Docket "
        "2, Section 1.1 strip) The hen/orchard/cycle-closure/"
        "productivity-illusion narrative is stripped to one crisp statement "
        "per block plus a citation of the companion ledger study (Author, "
        "A., et al., in review; reference entry added in alphabetical "
        "position), and the witness-inconsistent sentence reading the typed "
        "floor as a base constraint is corrected to the floor-mid-interval "
        "reading. (Docket 3, Section 2 tuple) The 13-slot tuple display is "
        "restructured as a named record — the typed assessment datum "
        "$\\mathfrak{S}$ — with the fields defined in the Supplementary "
        "Material (S1) and instantiated field by field in Section 2.7. "
        "(Docket 4, notation) $\\mathrm{FP}_0$ is re-lettered $\\mathcal{Q}$ "
        "at all eleven sites (the false-positive flavour removed; Figure 1's "
        "image carries $I = \\mathrm{FP}_{\\mathrm{agg}}$ and $R$ only, so "
        "no image-text mismatch); the weight ratio $r$ is frozen to "
        "$w_2/w_1$ and Section 5.5's resource increment is re-lettered "
        "$\\kappa$ ($\\mathsf{Aug}_\\kappa$, $\\mathcal{A}_\\kappa$, "
        "$\\kappa^*$, $\\mathrm{STAGED}_\\kappa$); the drift sites "
        "$|A| = 4$ and \"whether $A$ is exhaustive\" are written on "
        "$\\mathcal{A}$; and Section 2.8 gains the two-scope fences ($R$; "
        "$A$ vs $\\mathcal{A}$; $e$ vs $e_k$) and the $S = S_0$ "
        "identification. (Docket 5, demotions) Proposition 1 $\\to$ Remark 1, "
        "Lemma 2 $\\to$ Remark 2, Theorem 3 $\\to$ Proposition 3, Theorem 6 "
        "$\\to$ Remark 6 — status relabels on the unchanged 1–9 statement "
        "counter with every cross-reference updated (Remark 1 ×7, Remark 2 "
        "×8, Proposition 3 ×15, Remark 6 ×10) and no proof touched; reasons: "
        "the inclusion is elementary, the equivalence is the dual-cone fact, "
        "the identity is that fact applied pointwise plus constraint-set "
        "monotonicity, and the hold-prefix result is an identity pullback. "
        "The title is unchanged — no specific retitle is endorsed by the "
        "joint evaluation, and the title's claim is the operator-level "
        "separation the theorem literally proves — while Section 7 gains the "
        "scoping sentences that keep the conclusion from reading as a "
        "doctrinal ranking (Theorem 8 is the paper's own delimitation, not "
        "an objection to it). (Docket 7, 25 checks) The artifact's "
        "twenty-five machine checks are enumerated one by one, with their "
        "recorded pass status, in the Supplementary Material (S8, appended "
        "at this revision; values verbatim from the committed results JSON) "
        "and Section 4.9 keeps the count and a one-sentence pointer. (Docket "
        "8, companions) The Section 6.1 dependence is scoped: the scored "
        "forecast-evaluation companions carry in-text citations and "
        "reference entries (Author, B. and Author, C., et al., in review), "
        "and the paragraph states that no result of this article depends on "
        "an unpublished companion. (Vocabulary) Appendix A consolidates the "
        "declaration/registration/preregistration convention with one "
        "Section 2.8 pointer, and four body echoes are trimmed (strict "
        "main-body count 26 $\\to$ 22 — the article text ahead of the "
        "statements and references; the two Supplementary-Material uses "
        "are unchanged). Housekeeping: the supplementary pointer now "
        "cites `paper1_supplementary_v2.md` with S8 named (the stale v1 "
        "name). No frozen verdict, region identity, table row, or recorded "
        "number changes: the action table, the Section 4.9 table, Theorem "
        "5's set displays, and every recorded value are byte-identical; all "
        "edits are presentation, scoping, relabelling, and citation."
    )
    t = t[:idx] + new_log + t[log_end:]
    v20 = t

    # ================= mechanical checks =================
    body = body_of(v20, "v20")
    src_body = body_of(src_text, "v19")

    # R8: abstract length pinned (310 -> 298)
    ab_words = len(abstract_text(v20).split())
    if ab_words != 298:
        raise SystemExit(f"FAIL [R8]: abstract is {ab_words} words, expected 298")
    if len(abstract_text(src_text).split()) != 310:
        raise SystemExit("FAIL [R8]: v19 abstract not 310 words")

    # (5) demotions: old labels absent, new labels pinned
    for old_label in ["Proposition 1", "Lemma 2", "Theorem 3", "Theorem 6",
                      "Theorems 3", "Theorems 5–6"]:
        if old_label in body:
            raise SystemExit(f"FAIL [demotions]: '{old_label}' still present in body")
    for new_label, expected in [("Remark 1", 7), ("Remark 2", 8),
                                ("Proposition 3", 15), ("Remark 6", 10),
                                ("Theorem 5", 24), ("Theorem 7", 4),
                                ("Theorem 8", 9), ("Proposition 4", 7),
                                ("Proposition 9", 7)]:
        n = body.count(new_label)
        if n != expected:
            raise SystemExit(f"FAIL [demotions]: '{new_label}' count {n}, expected {expected}")
    # labels retain their proofs
    if "**Remark 1.**" not in body or "**Remark 2 (full-cone pointwise equivalence).**" not in body \
       or "**Proposition 3 (assessment identity and hierarchy).**" not in body \
       or "**Remark 6 (propagation).**" not in body:
        raise SystemExit("FAIL [demotions]: a relabelled statement header is missing")

    # (4) notation
    if "\\mathrm{FP}_0" in body:
        raise SystemExit("FAIL [notation]: FP_0 still present")
    if body.count("\\mathcal{Q}") != 11:
        raise SystemExit(f"FAIL [notation]: Q count {body.count('\\mathcal{Q}')}, expected 11")
    if "$\\mathrm{FP}_{\\mathrm{agg}}$" not in body:
        raise SystemExit("FAIL [notation]: FP_agg must remain (figure-pinned)")
    for gone in ["$\\mathsf{Aug}_r$", "$r^*$", "$\\mathcal{A}_r$",
                 "\\mathrm{STAGED}_r", "$|A| = 4$", "whether $A$ is exhaustive"]:
        if gone in body:
            raise SystemExit(f"FAIL [notation]: '{gone}' still present")
    for present in ["$\\mathsf{Aug}_\\kappa$", "$\\kappa^* = 1 - x$",
                    "$\\mathcal{A}_\\kappa$", "\\mathrm{STAGED}_\\kappa",
                    "$|\\mathcal{A}| = 4$",
                    "whether $\\mathcal{A}$ is exhaustive"]:
        if present not in body:
            raise SystemExit(f"FAIL [notation]: '{present}' missing")
    if body.count("E_{\\mathrm{end,typ}}") != 5:
        raise SystemExit(
            f"FAIL [notation]: E_end,typ count "
            f"{body.count('E_{\\mathrm{end,typ}}')} != 5 "
            "(§2.8 list, display, 2 chain links, §5.4 citation)")
    # 'typed-endpoint' x7 — all intentional deposits of docket item (1):
    # §2.8 notation list; §3.1 five-operators intro; §3.1 photograph
    # pointer; §3.1 the Definition; §3.1 machine-scoping sentence; §5.4
    # operator citation; §5.4 witness statement.
    if body.count("typed-endpoint") != 7:
        raise SystemExit(
            f"FAIL [notation]: 'typed-endpoint' count "
            f"{body.count('typed-endpoint')} != 7")
    if "the rescue set of Theorem 5 — every theorem reference and Figure 1 use the rescue-set reading" not in body:
        raise SystemExit("FAIL [notation]: R-scope fence missing")
    if "the standard basis vector $e_k$ of Remark 2's proof are distinct objects" not in body:
        raise SystemExit("FAIL [notation]: e/e_k fence missing")

    # (1) E_end,typ definition + scoping
    if "$$E_{\\mathrm{end,typ}}(z) = \\{ a : \\forall d,\\; \\mathrm{End}(a,d) \\subseteq S \\ \\text{ and } \\ \\mathrm{Succ}(a,d) \\subseteq G \\}.$$" not in body:
        raise SystemExit("FAIL [docket 1]: E_end,typ display missing")
    if "not machine-verified" not in body or "checks the physical endpoint operator only" not in body:
        raise SystemExit("FAIL [docket 1]: machine-artifact scoping missing")
    if "FAST is typed-endpoint-admissible at every state of $X_0$ while typed-tube-admissible only for $s_1 \\ge 2$" not in body:
        raise SystemExit("FAIL [docket 1]: one-line witness missing")

    # (2) Section 1.1 strip
    for gone in ["waste-in-waiting", "no substance is waste by its nature",
                 "An apple crop renews within a year",
                 "not a strict membership test"]:
        if gone in body:
            raise SystemExit(f"FAIL [docket 2]: stripped prose still present: {gone!r}")
    if body.count("Author, A., et al., in review") != 5:  # 4 in-text + 1 entry
        raise SystemExit("FAIL [docket 2]: ledger-companion citation count != 5")
    # 2 mentions of the illusion survive the strip: 1 spaced (the noun
    # phrase in §1.1) + 1 hyphenated (the compound modifier in §3.1).
    n_illus = body.count("productivity illusion") + body.count("productivity-illusion")
    if n_illus != 2:
        raise SystemExit(
            f"FAIL [docket 2]: productivity-illusion mentions {n_illus} != 2 "
            "(1 spaced in §1.1 + 1 hyphenated in §3.1)")
    if "what it fails to see is not the base but the individual floor mid-interval" not in body:
        raise SystemExit("FAIL [docket 2]: corrected masking statement missing")
    if "no theorem of this paper touches material cycles" not in body:
        raise SystemExit("FAIL [docket 2]: regimes-pointer statement missing")

    # (3) Section 2.2 named record
    if "### 2.2 The canonical datum as a named record" not in body:
        raise SystemExit("FAIL [docket 3]: named-record header missing")
    if "$$\\mathfrak{S} = (T, Z, S_{st}, B_{out}, V, \\Gamma, O, A, C, R, D, K, P),$$" in body:
        raise SystemExit("FAIL [docket 3]: 13-slot display still in the main text")
    if "field-by-field definitions are carried by the Supplementary Material (S1)" not in body:
        raise SystemExit("FAIL [docket 3]: S1 pointer missing")

    # (7) 25-check pointer
    if "the checks are enumerated one by one, with their recorded pass status, in the Supplementary Material (S8)" not in body:
        raise SystemExit("FAIL [docket 7]: S8 pointer missing")
    if body.count("All 25 checks pass") != 1:
        raise SystemExit("FAIL [docket 7]: 'All 25 checks pass' count != 1")

    # (8) companion scoping
    if "No result of this article depends on an unpublished companion" not in body:
        raise SystemExit("FAIL [docket 8]: no-dependence statement missing")
    if body.count("Author, B., et al., in review") != 2:  # 1 in-text + 1 entry
        raise SystemExit("FAIL [docket 8]: cod-companion citation count != 2")
    if body.count("Author, C., et al., in review") != 2:
        raise SystemExit("FAIL [docket 8]: Edwards-companion citation count != 2")
    if "(each under review)" in body:
        raise SystemExit("FAIL [docket 8]: unscoped '(each under review)' remains")

    # (6) Section 7 scoping; title unchanged
    if "The theorem ranks no doctrine" not in body:
        raise SystemExit("FAIL [docket 6]: Section 7 scoping missing")
    if v20.splitlines()[0] != src_text.splitlines()[0]:
        raise SystemExit("FAIL [docket 6]: title changed")

    # (10) vocabulary consolidation
    if v20.count("## Appendix A. Declaration and registration vocabulary (consolidated)") != 1:
        raise SystemExit("FAIL [docket 10]: Appendix A missing")
    if "The declaration, registration, and preregistration vocabulary of this article is consolidated in Appendix A" not in body:
        raise SystemExit("FAIL [docket 10]: Section 2.8 pointer missing")
    if vocab_count(src_body) != 28:
        raise SystemExit(f"FAIL [docket 10]: v19 body vocab count {vocab_count(src_body)} != 28")
    # like-for-like: the article text ahead of the statements/references
    # (v19's 28 includes 2 Supplementary-Material uses that sit after the
    # References and are untouched by the four trims).
    src_main = src_body.split("## Data availability statement")[0]
    if vocab_count(src_main) != 26:
        raise SystemExit(f"FAIL [docket 10]: v19 main-body vocab count {vocab_count(src_main)} != 26")
    body_no_appendix = body.split("## Appendix A.")[0]
    if vocab_count(body_no_appendix) != 22:
        raise SystemExit(f"FAIL [docket 10]: v20 main-body vocab count {vocab_count(body_no_appendix)} != 22 (four trims)")

    # Housekeeping
    if "paper1_supplementary_v2.md" not in body or "`paper1_supplementary.md`" in body:
        raise SystemExit("FAIL [housekeeping]: supplementary pointer")
    if "the machine artifact's twenty-five checks are enumerated in its S8" not in body:
        raise SystemExit("FAIL [housekeeping]: S8 named at the pointer")

    # Non-destructiveness: every markdown table line byte-identical, in order
    def table_lines(text):
        return [l for l in text.splitlines() if l.startswith("|")]
    if table_lines(src_body) != table_lines(body):
        raise SystemExit("FAIL [non-destructive]: table lines changed")

    # Frozen-value needles (counts must match v19 exactly; needles taken
    # from the paper's actual notation, several without $-delimiters)
    for needle, expected in [
        ("$31^3 = 29{,}791$-state grid", 1),
        ("scale 40", 1),
        ("$e = (1/4, 1/4)$", 2),
        ("rescue cost is $c = 1$", 1),
        (r"\rho_1 = \frac{2 - s_1}{s_2}", 1),
        (r"(\tfrac12, \tfrac1{10}, \tfrac1{10})", 4),
        (r"(\tfrac12, \tfrac65, \tfrac65)", 1),
        ("$(s_1, s_2) = (6/5, 6/5)$", 1),
        (r"\{ x \ge 1 \} \cup \{ s_1 \ge 2 \} \cup \{ s_2 \ge 2 \}", 1),
        (r"\{ x \ge 1 \} \cup \{ s_1 + s_2 \ge 2 \}", 3),
        ("NO-SWITCH", 7),
        ("$r = w_2 / w_1$", 4),
        (r"\delta \in \left[\,1 - \frac{s_2}{2},\; \frac{s_1}{2}\,\right]", 1),
    ]:
        n_src, n_new = src_body.count(needle), body.count(needle)
        if n_src != expected or n_new != expected:
            raise SystemExit(f"FAIL [frozen {needle!r}]: {n_src} -> {n_new}, expected {expected}")

    # Version log sanity
    if v20.count("*Version log (v20).*") != 1:
        raise SystemExit("FAIL: v20 version log not exactly once")
    if not v20.startswith("# The Limits of Compensatory Aggregation"):
        raise SystemExit("FAIL: title line damaged")

    open(DST, "w", encoding="utf-8").write(v20)

    # ================= supplementary: the one allowed append (S8) ================
    supp = open(SUPP, encoding="utf-8").read()
    if S8_HEADER in supp:
        # idempotent re-run: the file must be exactly (base) + S8, with the
        # appended block byte-identical to the constant and present once.
        if supp.count(S8_HEADER) != 1 or not supp.endswith(S8):
            raise SystemExit("FAIL [S8]: supplementary already carries a divergent S8")
        supp_base = supp[:len(supp) - len(S8)]
        supp_action = "S8 already present — verified byte-identical, no write"
    else:
        supp_base = supp.rstrip("\n") + "\n"
        supp = supp_base + S8
        open(SUPP, "w", encoding="utf-8").write(supp)
        supp_action = "S8 appended"
    # S8 mechanical checks
    s8 = supp[supp.find(S8_HEADER):]
    items = re.findall(r"^\d+\. \*.*$", s8, flags=re.M)
    if len(items) != 25:
        raise SystemExit(f"FAIL [S8]: {len(items)} enumerated checks, expected 25")
    if "25/25" not in s8 or "verbatim" not in s8:
        raise SystemExit("FAIL [S8]: provenance note incomplete")
    if supp.count(S8_HEADER) != 1:
        raise SystemExit("FAIL [S8]: header not exactly once")
    # the pre-existing supplementary content is untouched (base = file minus
    # the appended S8 on re-runs; original content on the first append)
    if not supp.startswith(supp_base.rstrip("\n")):
        raise SystemExit("FAIL [S8]: pre-existing supplementary content modified")

    wc = len(v20.split())
    wc_old = len(src_text.split())
    print(f"OK: wrote {DST}")
    print(f"    words: {wc_old} -> {wc} (delta {wc - wc_old})")
    print(f"    lines: {len(v20.splitlines())} (v19: {len(src_text.splitlines())})")
    print(f"    abstract: 310 -> {ab_words} words (pinned)")
    print(f"    demotion cross-references: Remark 1 x7, Remark 2 x8, "
          f"Proposition 3 x15, Remark 6 x10")
    print(f"    Q sites: 11; E_end,typ sites: 5; typed-endpoint mentions: 7; "
          f"companion entries: 3 (A/B/C)")
    print(f"    vocabulary main-body count: 26 -> 22 (v19 full body 28, of "
          f"which 2 sit in the Supplementary-Material section); Appendix A "
          f"+ 1 pointer")
    print(f"    supplementary: {supp_action}; 25 checks enumerated")


if __name__ == "__main__":
    main()

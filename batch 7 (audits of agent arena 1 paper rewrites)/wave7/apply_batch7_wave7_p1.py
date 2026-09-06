#!/usr/bin/env python3
"""Wave-7 build: paper1_assessment_separation v20 -> v21 (+ supplementary v2 notation harmonisation).

Quality-scan fixes, presentation-layer only:
1. §5.2: 'menu convexification of the menu' restored to §1.3's parallel 'witness menu'.
2. Abstract: 'artefact' -> 'artifact' (the body's spelling); 'nonempty open interior' ->
   'nonempty relative interior' (Theorem 5's own proof term; word-count preserving).
3. Theorem 5(4): 'open interior (in the state space)' -> 'relative interior (in the q=0 slice)'.
4. §2.8's W-fence corrected (the body writes the cone as W+; subfamilies W).
5. §1.3(i): the intersection display written over W+ (the full-cone reading its own text names).
6. §1.3's novelty paragraph trimmed to a single sentence with a Section 5.2 pointer.
7. §4.11's proof tombstone $\\square$ unified with the other proofs' unicode form.
8. 'tuple' remnants -> 'record' (3 sites); the 'four-symbol display' -> the two symbols.
9. 'price family' harmonised to 'weight family' (4 sites: the 4.4 heading, Prop 4's name,
   the 4.4 reading, and the 5.2 item).
10. §1.1: the answer-before-question sentence's operator pointer corrected (Section 3.1);
    the quantifier-fact sentence reworded (action-set identity; Remark 1 once).
11. §7: 'twenty-five' -> '25'; Remark 8's 'now explicit' -> 'explicit'.
12. Daly (1990) cited at the strong-sustainability sentence and the entry moved to its
    alphabetical position (before Das and Dennis).
13. Supplementary: S1's 'canonical tuple S' -> the named record S-fraktur; S6's retired
    r* -> kappa* (2 sites); a revision note appended.
Non-destructive: no frozen verdict, region identity, or table row changes; the action table,
the 4.9 table, and Theorem 5's set displays byte-identical; abstract word count preserved.
"""
import hashlib

SRC = "../../arena agent 1/paper rewrites/paper1_assessment_separation_v20.md"
DST = "../../arena agent 1/paper rewrites/paper1_assessment_separation_v21.md"
SUP = "../../arena agent 1/paper rewrites/paper1_supplementary_v2.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag, t=None):
    global text
    t = t if t is not None else text
    assert t.count(old) == 1, f"FAIL [{tag}]: count {t.count(old)}: {old[:80]!r}"
    return t.replace(old, new, 1)

def edit(old, new, tag):
    global text
    text = sub_once(old, new, tag)
    edits.append(tag)

# --- 1. witness menu ---
edit("menu convexification of the menu closes the gap exactly at the compensatory region (Theorem 8)",
     "menu convexification of the witness menu closes the gap exactly at the compensatory region (Theorem 8)",
     "witness menu")

# --- 2. abstract fixes ---
edit("not an artefact of a poor choice of weights", "not an artifact of a poor choice of weights", "artefact->artifact")
edit("is exactly this impossibility region, with nonempty open interior.",
     "is exactly this impossibility region, with nonempty relative interior.",
     "open->relative interior (abstract)")

# --- 3. Theorem 5(4) ---
edit("it is nonempty, and its open interior (in the state space) is $\\{ 0 < x < 1,\\ 0 < s_1 < 2,\\ 0 < s_2 < 2,\\ s_1 + s_2 > 2 \\}$",
     "it is nonempty, and its relative interior (in the $q = 0$ slice) is $\\{ 0 < x < 1,\\ 0 < s_1 < 2,\\ 0 < s_2 < 2,\\ s_1 + s_2 > 2 \\}$",
     "open->relative interior (Thm 5)")

# --- 4. W fence ---
edit("The weight cone of Section 3.1 is written $W$, the command architecture keeps the letter $C$",
     "The weight cone of Section 3.1 is written $W_+$ (a subfamily $W$, as in Proposition 4), the command architecture keeps the letter $C$",
     "W fence")

# --- 5. §1.3(i) display over W+ ---
edit("The action-set identity $E_{\\mathrm{typ}}(z) = \\bigcap_{w \\in W} E_w(z)$, with the full-cone choice",
     "The action-set identity $E_{\\mathrm{typ}}(z) = \\bigcap_{w \\in W_+} E_w(z)$, with the full-cone choice",
     "W -> W+ display")

# --- 6. novelty trim ---
edit("To our knowledge this provides an explicit exact-tube witness for this dynamic separation in a compensatory/noncompensatory assessment setting. We do not assert priority over the elementary quantifier fact $\\exists a\\, \\forall w \\neq \\forall w\\, \\exists a_w$, which is standard.",
     "To our knowledge, this provides an explicit exact-tube witness for this dynamic separation in a compensatory/noncompensatory assessment setting; the elementary quantifier fact behind it is standard, and Section 5.2 states the full novelty qualification.",
     "novelty trim")

# --- 7. tombstone ---
edit("under sequential time-sharing. $\\square$", "under sequential time-sharing. □", "tombstone")

# --- 8. tuple remnants + four-symbol ---
edit("The remaining tuple slots — multi-command architectures", "The remaining record slots — multi-command architectures", "tuple->record (2.7)")
edit("while $s$ is the floor vector and $S_{st}$ the tuple's stock–flux field", "while $s$ is the floor vector and $S_{st}$ the record's stock–flux field", "tuple->record (2.8a)")
edit("$R$ is the tuple's deployment/reset architecture", "$R$ is the record's deployment/reset architecture", "tuple->record (2.8b)")
edit("$A$ is the tuple's assessment operator", "$A$ is the record's assessment operator", "tuple->record (2.8c)")
edit("The four-symbol display on the witness (Section 4.5) uses $\\beta, \\alpha$ for the action-indexed disturbances",
     "The disturbance convention on the witness (Section 4.5) uses the two symbols $\\beta, \\alpha$ for the action-indexed disturbances",
     "four-symbol")

# --- 9. price family -> weight family (4 sites) ---
edit("### 4.4 Price-family monotonicity", "### 4.4 Weight-family monotonicity", "4.4 heading")
edit("**Proposition 4 (price-family monotonicity).**", "**Proposition 4 (weight-family monotonicity).**", "Prop 4 name")
edit("Proposition 4 makes precise the claim that *restricting* the price family *enlarges* the compensatory accepted set.",
     "Proposition 4 makes precise the claim that *restricting* the weight family *enlarges* the compensatory accepted set.",
     "4.4 reading")
edit("(iii) The price-family monotonicity proposition (Proposition 4).", "(iii) The weight-family monotonicity proposition (Proposition 4).", "5.2 item")

# --- 10. §1.1 fixes ---
edit("The doctrines this paper does compare are the formalized operators of Section 5.1.",
     "The doctrines this paper does compare are the operators formalized in Section 3.1 and read doctrinally in Section 5.1.",
     "operator pointer")
edit("proves the pointwise identity of the noncompensatory accepted set with the common-plan set over the full cone (Proposition 3(ii)), isolates the general mechanism in Remark 1",
     "proves the pointwise action-set identity of the noncompensatory operator with the common-plan set over the full cone (Proposition 3(ii)) and isolates its mechanism (Remark 1)",
     "identity wording")

# --- 11. numeral + now ---
edit("the machine artifact's twenty-five checks are enumerated in its S8", "the machine artifact's 25 checks are enumerated in its S8", "25 numeral")
edit("the two mechanisms are distinct, and both are now explicit", "the two mechanisms are distinct, and both are explicit", "now trim")

# --- 12. Daly cited + refiled ---
edit("critical natural capital whose loss cannot be compensated at any price (Ekins et al., 2003).",
     "critical natural capital whose loss cannot be compensated at any price (Daly, 1990; Ekins et al., 2003).",
     "Daly cited")
daly_entry = "Daly, H. E. (1990). Toward some operational principles of sustainable development. *Ecological Economics*, 2(1), 1–6.\n\n"
assert text.count(daly_entry.strip()) == 1
text = text.replace(daly_entry, "", 1)
das_line = [l for l in text.split("\n") if l.startswith("Das")][0]
text = text.replace(das_line, daly_entry + das_line, 1)
edits.append("Daly refiled")

# --- version log ---
OLD_LOG_PREFIX = "*Version log (v20).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v21).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no frozen verdict, region identity, or table row changes; the "
"abstract's word count is preserved (298; 'open interior'→'relative interior' and 'artefact'→'artifact' are "
"word-count-neutral). (1) §5.2(vii)'s degraded 'menu convexification of the menu' restored to §1.3's 'witness menu' "
"parallel. (2) Theorem 5(4)'s 'open interior (in the state space)' corrected to 'relative interior (in the q=0 "
"slice)' — the proof's own term — with the abstract's echo matched. (3) §2.8's weight-cone fence corrected (the cone "
"is $W_+$; subfamilies $W$), and §1.3(i)'s identity display written over $W_+$, the full-cone reading its own text "
"names. (4) §1.3's novelty paragraph trimmed to one sentence with a Section 5.2 pointer (the duplicated two-sentence "
"statement remains in full in §5.2). (5) §4.11's proof tombstone unified with the other eight proofs. (6) Three "
"'tuple' remnants re-lettered 'record' (§2.7/§2.8, the v20 named-record rename's stragglers); the 'four-symbol "
"display' corrected to the two symbols the convention uses. (7) 'price family' harmonised to 'weight family' at four "
"sites (the §4.4 heading, Proposition 4's name, the §4.4 reading, the §5.2 item), respecting §4.4's own reservation "
"of 'prices' for the interpretive register. (8) §1.1's doctrine-comparison pointer corrected (the operators are "
"formalized in Section 3.1); the quantifier-fact sentence now names the action-set identity and cites Remark 1 once. "
"(9) 'twenty-five' → '25' and 'both are now explicit' → 'both are explicit'. (10) Daly (1990) cited at the "
"strong-sustainability sentence and its entry moved to its alphabetical position (it had been filed after Das & "
"Dennis with no in-text citation). The action table, the Section 4.9 table, Theorem 5's set displays, and every "
"recorded value are byte-identical. The supplementary's S1 opening and S6 conjectures C2/C9 are re-lettered to the "
"named record $\\mathfrak{S}$ and $\\kappa^*$ (the v20 declarations' own notation), with a revision note appended there."
)
text = text[:i] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
assert body_new.count("tuple") == 0 and body_new.count("price famil") == 0
assert body_new.count("artefact") == 0
assert body_new.count("$W_+$") == body_old.count("$W_+$") + 1 and "subfamily $W$" in body_new
aw = len(body_old[body_old.index("## Abstract"):body_old.index("**Keywords:**")].split())
aw_new = len(body_new[body_new.index("## Abstract"):body_new.index("**Keywords:**")].split())
assert aw == aw_new, f"FAIL abstract words {aw}->{aw_new}"
def table_lines(s):
    return [l for l in s.split("\n") if l.startswith("|")]
assert table_lines(src) == table_lines(text), "FAIL table lines changed"
assert "$\\square$" not in text and text.count("□") == 9

open(DST, "w", encoding="utf-8").write(text)

# --- supplementary (idempotent) ---
sup = open(SUP, encoding="utf-8").read()
NOTE = ("\n\n---\n\n*Revision note (wave-7 build, v21).* Notation harmonised with the main text's v20/v21 declarations: "
        "S1's opening now names the object $\\mathfrak{S}$ (the named record; bare $S$ remains the typed safe set), and "
        "S6's conjectures C2 and C9 write the resource-increment rescue threshold as $\\kappa^*$ (the letter $r$ is the "
        "weight ratio $w_2/w_1$). No content, status, or value changes.")
if "*Revision note (wave-7 build, v21).*" in sup:
    assert sup.count("The named record $\\mathfrak{S} = (T, Z, S_{st}, B_{out}, V, \\Gamma, O, A, C, R, D, K, P)$ (main text, Section 2.2)") == 1
    assert sup.count("for the named record (the thirteen-field framework object") == 1
    assert sup.count("the rescue threshold $\\kappa^*$") == 2
    sup2 = sup
    print("    supplementary already updated — verified, no write")
else:
    sup2 = sup
    sup2 = sub_once("The canonical tuple $S = (T, Z, S_{st}, B_{out}, V, \\Gamma, O, A, C, R, D, K, P)$ (main text, Section 2.2) is expanded here with the full definitions of its thirteen slots",
                    "The named record $\\mathfrak{S} = (T, Z, S_{st}, B_{out}, V, \\Gamma, O, A, C, R, D, K, P)$ (main text, Section 2.2) is expanded here with the full definitions of its thirteen fields", "S1 opening", sup2)
    sup2 = sub_once("We write $S = (T, Z, S_{st}, B_{out}, V, \\Gamma, O, A, C, R, D, K, P)$ for the canonical tuple (the thirteen-slot framework object defined in the main text, Section 2.2)",
                    "We write $\\mathfrak{S} = (T, Z, S_{st}, B_{out}, V, \\Gamma, O, A, C, R, D, K, P)$ for the named record (the thirteen-field framework object defined in the main text, Section 2.2)",
                    "S1 notation", sup2)
    c = sup2.count("the rescue threshold $r^*$")
    assert c == 2, f"FAIL r* count {c}"
    sup2 = sup2.replace("the rescue threshold $r^*$", "the rescue threshold $\\kappa^*$")
    sup2 = sup2.rstrip("\n") + NOTE + "\n"
    open(SUP, "w", encoding="utf-8").write(sup2)

print(f"OK  P1 v21 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")
print(f"    supplementary updated (S1 x2, r*->kappa* x2, note appended); MD5 {hashlib.md5(sup2.encode()).hexdigest()}")

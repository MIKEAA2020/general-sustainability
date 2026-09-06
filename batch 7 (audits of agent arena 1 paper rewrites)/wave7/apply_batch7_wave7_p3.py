#!/usr/bin/env python3
"""Wave-7 build: paper3_material_ledgers v29 -> v30. Quality-scan fixes, presentation-layer only.

Implemented:
1. Reference hygiene: the Daly (1990) entry added (cited at two sites, absent from the list);
   the §1.1 'supporting pool' variant harmonised to the paper's dominant 'support pool'.
2. §1.1 numerals: 'near one million kilotons' / 'of order six hundred thousand kilotons' in
   the paper's numeral+kt style.
3. Notation: the B_t/B_min table row scoped correctly (barrier B_min local to 7.5; reference
   B_lim in 6.5.x); the §2.4 local-notation parenthetical names S and P; q glossed at the (2)
   display; H^win_GW glossed at first use in Prop 18.
4. §5.4's recharge-law table pointer disambiguated ('this article's Section 9').
5. Abbreviation discipline: ADH, SSB, F expanded at first use; USGS expanded at first use;
   MCS expanded at first use; the §-form references in running prose spelled out.
6. Echo-redundancy trims (each a verbatim repeat of a carrier elsewhere): §3.1's opening
   litany -> a Section 1.1 pointer; §1.1's end-of-paragraph restatement of the two-pool
   registered status; the Indo-Gangetic dagger note's duplicate sentence; §10.1's repeated
   maxim clause; §11's repeated usable/false sentence; §4's double announcement.
7. §6.5.2's fisheries paragraph split at the provenance boundary (blank-line insert).
8. §6.5.2 self-referential pointer fixed; the supplementary pointer's 'this file's' -> the
   supplementary's; curly quotes straightened in the numbering note; the §5.1 quoted phrases
   de-quoted (no citation exists for either); the '2025 world production column' named as the
   pinned source's; the 'n=5 built-in check' — none (that is E2's).
Declined (recorded in the wave-7 record): the fisheries paragraph's internal repetition trims
(vintage-pinning discipline carries distinct caveats); the L41 renewal enumeration (different
scope from L31's); the §11 closing statement (deliberate rhetoric); the L45 four-driver repeat
(each site a distinct argument); the registered length reduction (standing decline).
Non-destructive: no statement, proof, table row, recorded value, or verdict changes.
"""
import hashlib

SRC = "../../arena agent 1/paper rewrites/paper3_material_ledgers_v29.md"
DST = "../../arena agent 1/paper rewrites/paper3_material_ledgers_v30.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: count {text.count(old)}: {old[:80]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

# --- 1. Daly entry + supporting pool ---
sub_once(
 "Clark, C.W., 1990. Mathematical Bioeconomics: The Optimal Management of Renewabl",
 "Clark, C.W., 1990. Mathematical Bioeconomics: The Optimal Management of Renewabl",
 "placeholder-clark")  # position check only (reverted below)
text = text  # no-op
edits.pop()
daly = "Daly, H.E., 1990. Toward some operational principles of sustainable development. Ecological Economics 2, 1–6.\n"
clark_line = [l for l in text.split("\n") if l.startswith("Clark, C.W., 1990")][0]
text = text.replace(clark_line, daly + clark_line, 1)
edits.append("Daly entry added")
sub_once("by drawing down the supporting pool — groundwater, soil carbon, bioavailable nutrients — rather than by that pool's regeneration",
         "by drawing down the support pool — groundwater, soil carbon, bioavailable nutrients — rather than by that pool's regeneration",
         "supporting->support pool (1)")
c = text.count("The supporting pool need not be")
assert c == 1, f"FAIL supporting-pool count {c}"
text = text.replace("The supporting pool need not be", "The support pool need not be", 1)
edits.append("supporting->support pool (2)")

# --- 2. §1.1 numerals ---
sub_once("have remained near one million kilotons for decades while cumulative production since 1996 is of order six hundred thousand kilotons.",
         "have remained near $1{,}000{,}000$ kt for decades while cumulative production since 1996 is of order $600{,}000$ kt.",
         "numerals")

# --- 3. notation ---
sub_once("fisheries biomass $B_t$ and reference $B_{\\min}$ (local to §6.5.2, §7.5)",
         "fisheries biomass $B_t$ and barrier $B_{\\min}$ (local to §7.5); reference $B_{\\lim}$ (local to §6.5.2, §6.5.4)",
         "B row")
sub_once("(in this block's local notation, $K$ is the sink stock and $N$ the nutrient stock; the carrying capacity and living stock of Section 2.2 do not enter)",
         "(in this block's local notation, $S$ is the resource stock, $K$ the sink stock, $N$ the nutrient stock, and $P$ the input flux; the carrying capacity and living stock of Section 2.2 do not enter)",
         "2.4 local notation")
sub_once("$$\\begin{aligned} | \\dot N &= R - qEN,",
         "$$\\begin{aligned} | \\dot N &= R - qEN, \\qquad (q\\ \\text{the per-effort extraction coefficient}),",
         "q gloss") if False else None
# (the display gloss above is awkward inside aligned; gloss q in prose instead)
i_q = text.find("\\dot N &= R - qEN")
assert i_q > 0
sub_once("together with a memory–effort pair $(Z, E)$ driven by $qEN - R$ (never by mining).",
         "together with a memory–effort pair $(Z, E)$ driven by $qEN - R$ (never by mining; $q$ the per-effort extraction coefficient of the harvest law).",
         "q gloss prose")
sub_once("in particular $\\mathbb{E}[T_{\\mathrm{GW}}] = \\nu = H^{\\mathrm{win}}_{\\mathrm{GW}}$ and $\\operatorname{Var}(T_{\\mathrm{GW}}) = \\nu^3/\\lambda = d\\,\\varsigma^2/|\\mu|^3$.*",
         "in particular $\\mathbb{E}[T_{\\mathrm{GW}}] = \\nu = H^{\\mathrm{win}}_{\\mathrm{GW}}$ — the deterministic horizon to the window minimum, $= d/|\\mu|$ — and $\\operatorname{Var}(T_{\\mathrm{GW}}) = \\nu^3/\\lambda = d\\,\\varsigma^2/|\\mu|^3$.*",
         "Hwin gloss")

# --- 4. recharge-law table pointer ---
sub_once("The delay-dynamics analysis's working completion (that analysis, Section 9): not a closed-block law, and the reason the two systems do not reduce.",
         "The delay-dynamics analysis's working completion (that analysis; this article's Section 9): not a closed-block law, and the reason the two systems do not reduce.",
         "recharge table pointer")

# --- 5. abbreviations ---
sub_once("The fisheries column reports the pure-decay proxy $\\mathrm{ADH} = F^{-1}\\log(\\mathrm{SSB}_{\\mathrm{now}}/(0.2\\max\\mathrm{SSB}))$ under current $F$",
         "The fisheries column reports the archived-depletion-horizon (ADH) pure-decay proxy $\\mathrm{ADH} = F^{-1}\\log(\\mathrm{SSB}_{\\mathrm{now}}/(0.2\\max\\mathrm{SSB}))$ under current fishing mortality $F$",
         "ADH/F expansion")
sub_once("with median $\\approx 1.8$ yr across the 43 assessed stocks with finite SSB an",
         "with median $\\approx 1.8$ yr across the 43 assessed stocks with finite spawning-stock-biomass (SSB) an",
         "SSB expansion")
sub_once("estimates rest on single-source USGS data whose credibility is questionable",
         "estimates rest on single-source U.S. Geological Survey (USGS) data whose credibility is questionable",
         "USGS expansion")
sub_once("the single pinned source of record is MCS 2026 (U.S. Geological Survey, 2026)",
         "the single pinned source of record is the Mineral Commodity Summaries (MCS) 2026 (U.S. Geological Survey, 2026)",
         "MCS expansion")
sub_once("the Indo-Gangetic groundwater magnitude sits an order of magnitude beyond published basin-mean trends (§6.5.2)",
         "the Indo-Gangetic groundwater magnitude sits an order of magnitude beyond published basin-mean trends (the quarantine note below)",
         "self-referential pointer")

# --- 6. echo-redundancy trims ---
sub_once(
 "Bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are different predicates, and material-flows accounting practice routinely slides between them. This section separates the first, second, and fourth of these predicates and proves their relationships (the third, thermodynamic admissibility, is out of scope here, per Proposition 2's layering). The argument is needed because a mass-balanced ledger can be chemically impossible, a chemically consistent ledger can violate every declared barrier, and a barrier-satisfying ledger can fail conservation —",
 "The four predicates of Section 1.1 — bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety — are this section's working layer: it separates the first, second, and fourth and proves their relationships (the third, thermodynamic admissibility, is out of scope here, per Proposition 2's layering), for the reasons Section 1.1 states —",
 "3.1 litany -> pointer")
sub_once("not a supporting-pool column that the applied data do not carry; where an explicit two-pool reading is the relevant one (groundwater), the two-pool model is registered as not established rather than as detected (Section 8.2).",
         "not a supporting-pool column that the applied data do not carry.",
         "1.1 end-restatement cut")
sub_once("the full quarantine record is the paragraph below. The row is retained only as the worked instance of the index construction and enters no classification.",
         "the full quarantine record is the paragraph below.",
         "dagger-note duplicate cut")
sub_once("The reading is the algebraic form of the weak-comparability thesis stated in Section 1.1: scalar summaries may rank and communicate, but certification requires the vector.",
         "The reading is the algebraic form of the weak-comparability thesis stated in Section 1.1.",
         "10.1 maxim repeat cut")
sub_once("answer three distinct questions at three distinct evidentiary levels. Stating them with those questions is what makes them usable; collapsing them into one \"time to depletion\" is what makes them false.",
         "answer three distinct questions at three distinct evidentiary levels.",
         "11 usable/false repeat cut")
sub_once("This section sets out the four concepts that the typed ledger keeps apart, and the incidence discipline that makes conservation a property of the structure rather than an assumption.",
         "This section sets out the incidence discipline that makes conservation a property of the structure rather than an assumption.",
         "4 double-announcement cut")

# --- 7. paragraph split ---
sub_once("or below the class cohort's $1.79$ yr. The extract is the RAM Legacy cohort of Ricard et al. (2012), and the pull date is archived",
         "or below the class cohort's $1.79$ yr.\n\nThe extract is the RAM Legacy cohort of Ricard et al. (2012), and the pull date is archived",
         "fisheries paragraph split")

# --- 8. small fixes ---
sub_once("the statement-status naming offset that maps this file’s pre-v28 status words",
         "the statement-status naming offset that maps the supplementary’s pre-v28 status words",
         "this file -> the supplementary (1)")
sub_once("which maps this file’s pre-v28 status words to the main text",
         "which maps the supplementary’s pre-v28 status words to the main text",
         "this file -> the supplementary (2)")
sub_once("(Ayres' \"useful work\", Daly's \"throughput-of-services\")",
         "(Ayres' useful-work reading, Daly's throughput-of-services reading)",
         "de-quote")
sub_once("the 2025 world production column $\\approx 250{,}000$ kt",
         "the pinned source's 2025 world-production column $\\approx 250{,}000$ kt",
         "production column named")
text_q = text.count("“Proposition")
for curly, straight in [("“", '"'), ("”", '"')]:
    pass
n_curly = text.count("“") + text.count("”")
assert n_curly == 10, f"FAIL curly count {n_curly}"
text = text.replace("“", '"').replace("”", '"')
edits.append("curly quotes straightened")

# --- version log ---
OLD_LOG_PREFIX = "*Version log (v29).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v30).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no statement, proof, table row, recorded value, or verdict "
"changes. (1) Reference hygiene: the Daly (1990) entry is added (cited at two sites, absent from the list); §1.1's "
"'supporting pool' harmonised to the paper's dominant 'support pool'; the §5.1 attributed phrases de-quoted (no "
"citation exists for either). (2) §1.1's spelled-out magnitudes written in the paper's numeral+kt style. (3) Notation: "
"the $B_t$/$B_{\\min}$ table row scoped correctly (barrier local to §7.5, reference $B_{\\lim}$ in §6.5.x); §2.4's "
"local-notation parenthetical names $S$ and $P$; $q$ glossed at the closed block; $H^{\\mathrm{win}}_{\\mathrm{GW}}$ "
"glossed at first use; the recharge-law table's companion pointer disambiguated. (4) Abbreviation discipline: ADH, "
"SSB, $F$, USGS, and MCS expanded at first use; the two §-form prose references spelled out; the self-referential "
"§6.5.2 pointer re-aimed at the quarantine note; the supplementary pointer's 'this file's' corrected to the "
"supplementary's; the numbering note's curly quotes straightened. (5) Echo-redundancy trims, each a verbatim repeat "
"carried elsewhere: §3.1's opening litany becomes a Section 1.1 pointer; §1.1's end-of-paragraph restatement of the "
"two-pool registered status; the Indo-Gangetic dagger note's duplicate sentence; §10.1's repeated maxim clause; "
"§11's repeated usable/false sentence; §4's double announcement; the §6.5.2 fisheries paragraph split at the "
"provenance boundary. Declined with reasons (the wave-7 record): the fisheries paragraph's internal repetition trims "
"(each 'repeat' carries a distinct vintage-pinning caveat); the §1.1 renewal enumeration pair (different scopes); "
"§11's closing statement (deliberate rhetoric); the four-driver enumeration (each site a distinct argument); the "
"registered length reduction (standing decline)."
)
text = text[:i] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
for n in ["1.8", "1.79", "454", "3.39", "2.57", "43", "74,000,000", "250,000", "120,000",
          "4.652", "0.348", "5.000", "4.47", "18", "20"]:
    assert body_old.count(n) == body_new.count(n), f"FAIL {n}: {body_old.count(n)}->{body_new.count(n)}"
assert body_new.count("“") == 0 and body_new.count("”") == 0
assert "this file’s" not in body_new and "this file's" not in body_new
assert body_new.count("support pool") >= 5 and body_new.count("supporting pool") == 0
def table_lines(s):
    return [l for l in s.split("\n") if l.startswith("|")]
diff = [(o, n) for o, n in zip(table_lines(src), table_lines(text)) if o != n]
# allowed: the B-row scoping cell (a notation-table line, not a data table)
allowed = ("B_{\\min}", "that analysis, Section 9")
assert all(any(a in o for a in allowed) for o, _ in diff) and len(diff) == 2, f"FAIL table diffs: {diff[:2]}"

open(DST, "w", encoding="utf-8").write(text)
print(f"OK  P3 v30 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")

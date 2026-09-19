#!/usr/bin/env python3
"""paper3_supplementary_v9.md = the repository's v8 verbatim + Part II (S7-S9), whose content is
taken from revision/v5/supplementary_v5_additions.md with its section cross-references re-pointed to
the numbering of the repository manuscript. v8 is never modified."""
import json, os, re, sys
SRC8 = "github/gs/arena agent 1/paper rewrites/paper3_supplementary_v8.md"
ADDS = "revision/v5/supplementary_v5_additions.md"
DST  = "revision/v6/paper3_supplementary_v9.md"

v8 = open(SRC8, encoding="utf-8").read()
add = open(ADDS, encoding="utf-8").read()
parts = re.split(r"^## ", add, flags=re.M)
blocks = {}
for p_ in parts[1:]:
    title, rest = p_.split("\n", 1)
    blocks[title.split(" \u00b7 ")[0].strip()] = (title, rest.rstrip() + "\n")
want = ["S-A", "S-B", "S-C", "S-D", "S-E", "S-F"]
assert all(w in blocks for w in want), sorted(blocks)

MAP = {"\u00a71.5": "\u00a71.2", "\u00a72.2, \u00a73.4 flux-reconstruction identity": "\u00a73.3",
       "\u00a72.1, \u00a72.2 incidence discipline": "\u00a72.1", "\u00a72.2)": "\u00a73.4)",
       "\u00a73.3": "\u00a73.2", "\u00a73.4": "\u00a73.3", "\u00a73.5": "\u00a73.4",
       "\u00a73.6": "\u00a73.5", "\u00a73.7": "\u00a73.6",
       "\u00a78.1\u20138.3": "\u00a76.5.1\u20136.5.4", "\u00a78.1": "\u00a76.5.1", "\u00a78.2": "\u00a76.5.3",
       "\u00a78.3": "\u00a76.5.4", "\u00a78.4": "\u00a76.5.2", "\u00a78 ": "\u00a76.5 ",
       "\u00a77.1": "\u00a710.1", "\u00a77.2": "\u00a710.1", "\u00a77.3": "\u00a710.2",
       "\u00a79.6": "\u00a77.6", "\u00a79.7": "\u00a77.7", "\u00a710.1": "\u00a79"}
KEYS = sorted(MAP, key=len, reverse=True)

report = []
def repoint(txt, tag):
    for k in KEYS:
        while k in txt:
            i = txt.index(k)
            ctx = re.sub(r"\s+", " ", txt[max(0, i-55):i+len(k)+15])
            j = txt.index(k); txt = txt[:j] + MAP[k] + txt[j+len(k):]
            report.append((tag, k, MAP[k], ctx))
    return txt

out = []
for key, title in [("S-A", "S7 \u00b7 Proof obligations of the certification state (\u00a73.1)"),
                   ("S-B", "S8 \u00b7 The linear programmes, their inputs, and the reading rule"),
                   ("S-C", "S9.1 \u00b7 Worked ledger exhibit"),
                   ("S-D", "S9.2 \u00b7 Promotion-rule table"),
                   ("S-E", "S9.3 \u00b7 Reproduction"),
                   ("S-F", "S9.4 \u00b7 Statement inventory at v33")]:
    _, body = blocks[key]
    body = repoint(body, key)
    body = body.replace("at v5", "at v33").replace("in v5:", "in this version:")
    body = re.sub(r"\s*the disturbance-budget note\s*\(\u00a73\.\d\)", "", body)
    out.append("## " + title + "\n\n" + body.strip() + "\n")

head = ("\n\n---\n\n# Part II \u2014 additions at v9\n\n"
        "Part I above is the file `paper3_supplementary_v8.md`, carried unchanged. The three sections\n"
        "below accompany manuscript version v33 and hold the material that the article points to\n"
        "rather than carries: the proof obligations of the certification state (S7), the linear\n"
        "programmes of the closure-cone, deficit and critical-margin statements with the reading rule\n"
        "for an infeasible programme (S8), and the worked exhibits, promotion rules, reproduction\n"
        "record and extended statement inventory (S9). Section references are to the v33 numbering of\n"
        "the article; the statement labels of S9.4 are the article's own.\n")
part2 = "\n".join(out)
# the statement-inventory cells carry a bare main-text section number per row
def fix_cell(m):
    key = "\u00a7" + m.group(2)
    return m.group(1) + (MAP[key].lstrip("\u00a7") if key in MAP else m.group(2)) + m.group(3)
part2 = re.sub(r"(^\| (?:Definition|Proposition|Theorem|Remark|Corollary|Lemma)[^|]*\|\s*)(\d+(?:\.\d+)*)(\s*\|$)",
               fix_cell, part2, flags=re.M)
part2 = re.sub(r"\s*the disturbance-budget note\s*\(\u00a7\d(?:\.\d)?\),?", "", part2)
part2 = re.sub(r"Unnumbered statements added in this version:[^\n]*(?:\n[^\n]*)*?\)\.",
               "Two unnumbered notes are added alongside them: *Certification state* in \u00a73.1 and\n*Antecedents* in \u00a71.2, together with the refute/alarm clause in \u00a710.1, the\njoint-minimal reporting note in \u00a76.3, and the review-interval note in \u00a79. The\ndisturbance/residual material is not unnumbered: it is Definition 23 in \u00a73.4.",
               part2, count=1, flags=re.S)
part2 = part2.replace("| Remark 33 (One-signed bias of an aggregate overshoot date) | 6.5.2 |",
                   "| Remark 33 (One-signed bias of an aggregate overshoot date) | 10.2 |")
part2 = part2.replace("Proposition 21 (Closure capacity of the declared cycle) | 2.1 |", "Proposition 21 (Closure capacity of the declared cycle) | 2.1 |")
part2 = part2.replace(", ,", ",").replace(",,", ",").replace(" .", ".").replace("(\u00a76.3),  ", "(\u00a76.3), ")
t = v8.rstrip("\n") + "\n" + head + "\n" + part2
open(DST, "w", encoding="utf-8").write(t)
json.dump(report, open("revision/v6/supp_v9_repoint_log.json", "w"), ensure_ascii=False, indent=1)
print("v8 chars %d -> v9 chars %d (+%d)" % (len(v8), len(t), len(t)-len(v8)))
print("re-pointed %d references" % len(report))
seen = {}
for tag, k, new, ctx in report:
    seen.setdefault((k, new), 0); seen[(k, new)] += 1
for (k, new), n in sorted(seen.items()):
    print("   %-14s -> %-14s x%d" % (k, new, n))
print("--- contexts containing a section symbol not in the map ---")
left = sorted(set(re.findall(r"\u00a7\d+(?:\.\d+)*", t[len(v8):])) - set())
print("  refs present in Part II:", left)

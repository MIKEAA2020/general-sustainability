#!/usr/bin/env python3
"""Generate the authoritative statement register from the LaTeX of record, and check that the markdown
mirror and the supplementary agree with it. This is the machinery that replaces the hand-maintained
numbering note and the supplementary's S6 status-word offset: one file, derived, that all three read.

Run from the workspace root:  python3 revision/v7/label_register.py"""
import json, os, re, sys
WS = os.environ.get("WS", "/home/user")
TEX = os.path.join(WS, "revision/v7/paper3_material_ledgers_v34.tex")
MD  = os.path.join(WS, "revision/v7/paper3_material_ledgers_v34.md")
SUPP= os.path.join(WS, "revision/v6/paper3_supplementary_v9.md")
HEADS = r"(Theorem|Proposition|Definition|Remark|Corollary|Lemma|Example)"
def scan(src, pat):
    out = []
    for m in re.finditer(pat, src):
        out.append((m.group(2), int(m.group(3))))
    return out
tex = open(TEX, encoding="utf-8").read()
md  = open(MD, encoding="utf-8").read()
supp= open(SUPP, encoding="utf-8").read()
tt = scan(tex, r"\\textbf\{(" + HEADS + r") (\d+)[^}]*\}")
mm = scan(md,  r"\*\*(" + HEADS + r") (\d+)[. ]")
def keyed(rows):
    d = {}
    for kind, num in rows:
        d.setdefault(int(num), []).append(kind)
    return d


def pairs(rows):
    seen = {}
    for kind, num in rows:
        seen[(kind, int(num))] = seen.get((kind, int(num)), 0) + 1
    return seen
tk, mk = keyed(tt), keyed(mm)
print("tex statement heads: %d   md: %d" % (len(tt), len(mm)))
nums = sorted(tk)
print("tex labels:", "%d..%d, %d distinct" % (nums[0], nums[-1], len(nums)))
gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in tk]
dups = {n: v for n, v in tk.items() if len(v) > 1}
print("gaps:", gaps or "none")
print("labels introduced more than once as heads:", dups or "none")
pp = pairs(tt)
rep = {k: v for k, v in pp.items() if v > 1}
print("tex (kind, number) pairs introduced more than once:", rep or "none")
print("per-kind maxima:", {k: max(n for kk, n in pp if kk == k) for k in sorted({kk for kk, _ in pp})})
print("md and tex agree on the label set:", sorted(mk) == nums)
# every label cited in prose must exist as a head
cited = {int(c) for c in re.findall(r"\\(?:theorem|proposition)?\s*(?:Theorem|Proposition|Definition|Remark|Corollary)\s\((\d+)\)", tex)}
cited |= {int(c) for c in re.findall(r"(?:Theorem|Proposition|Definition|Remark|Corollary)\s+(\d+)\b", tex)}
missing = sorted(c for c in cited if c not in tk)
print("cited-but-unintroduced labels:", missing or "none")
# the supplementary's inventory rows must name sections that exist
heads_txt = " | ".join(re.sub(r"\s+", " ", m.group(1)).strip() for m in re.finditer(r"\subsubsection\{([^}]*(?:\n[^}]*)?)\}", tex))
def num_of(title):
    m = re.match(r"\s*(\d+(?:\.\d+)*)", title)
    return m.group(1) if m else None
sections = sorted({num_of(h) for h in re.findall(r"([0-9]+(?:\.[0-9]+)*)\s", heads_txt)})
inv = re.findall(r"^\| (?:Definition|Proposition|Theorem|Remark)[^|]*\|\s*([0-9.]+)\s*\|$", supp, re.M)
bad = [v for v in inv if v not in sections]
print("supplementary inventory rows: %d, pointing at sections that do not exist: %s" % (len(inv), bad or "none"))
json.dump({"tex": {str(k): v for k, v in sorted(tk.items())}, "labels": nums,
           "count": len(tt), "gaps": gaps, "sections": [s for s in sections if s]},
          open(os.path.join(WS, "revision/v7/labels_v34.json"), "w"), indent=1)
print("wrote revision/v7/labels_v34.json")

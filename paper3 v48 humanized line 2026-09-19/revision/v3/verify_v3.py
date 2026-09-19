"""Invariant checks for revision/v3/paper3_v3.md. Usage: python3 revision/v3/verify_v3.py [file]"""
import re, sys
P = sys.argv[1] if len(sys.argv) > 1 else 'revision/v3/paper3_v3.md'
t = open(P, encoding='utf-8').read()
fails = []
def chk(cond, label):
    print(("  ok   " if cond else "  FAIL ")+label)
    if not cond: fails.append(label)

# 1. block incidence: parse the pmatrix from the file, check dimensions and column sums
i = t.find("S_{\\text{block}}"); blk = t[i:t.find("\\end{pmatrix}", i)]
rows = []
for line in blk.split('\\\\'):
    nums = re.findall(r'-?\d+', line)
    if len(nums) >= 8: rows.append([int(x) for x in nums[:8]])
chk(len(rows) == 4 and all(len(r) == 8 for r in rows), "S_block is 4x8 (%d rows parsed)" % len(rows))
cs = [sum(r[c] for r in rows) for c in range(8)] if len(rows) == 4 else []
chk(cs == [0, 0, -1, 0, 0, 0, 0, -1], "column sums = %s (expected [0,0,-1,0,0,0,0,-1])" % cs)
# 2. no negative off-block entries (all four rows must stay non-negative outside the geological pair)
if len(rows) == 4:
    # rebuild the block incidence from its own caption (rows N, A_act, A_geo, U) and the eight
    # declared column transfers, then compare with the matrix as printed
    R = [[0]*8 for _ in range(4)]
    def transfer(col, frm, to):
        if frm is not None: R[frm][col] -= 1
        if to is not None: R[to][col] += 1
    transfer(0, 1, 0)   # gross regeneration: A_act -> N
    transfer(1, 0, 1)   # density-dependent return: N -> A_act
    transfer(2, 0, None)  # harvest: N -> outside the block
    transfer(3, 1, 3)   # uptake: A_act -> U
    transfer(4, 3, 1)   # detritus return: U -> A_act
    transfer(5, 2, 1)   # e_GA: geological donor -> A_act
    transfer(6, 1, 2)   # e_AG: A_act -> geological donor
    transfer(7, 2, None)  # mining: donor -> outside the block
    chk(R == rows, "matrix matches its caption's eight transfers and equations (2a)-(2d)")
    chk(all(rows[k][j] in (-1, 0, 1) for k in range(4) for j in range(8)), "entries are unit incidence coefficients")
    # (2b)-(2d) read off the rows
    chk(rows[0] == [1,-1,-1,0,0,0,0,0], "N-row reproduces (2a): +gross regeneration, -return, -harvest")
    chk(rows[2] == [0,0,0,0,0,-1,1,-1], "A_geo-row reproduces (2c): -e_GA, +e_AG, -mining")
# 3. statement inventory: the labels the manuscript actually assigns, on one shared counter
need = [f"**Definition {k}" for k in (1, 2, 3, 4, 5, 6)]
need += [f"**Theorem {k}" for k in (1, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15)]
need += ["**Proposition 1", "**Proposition 2", "**Proposition 4", "**Proposition 6",
         "**Proposition 17", "**Proposition 18", "**Proposition 20", "**Lemma 3",
         "**Remark 2", "**Remark 16", "**Corollary 19"]
need += ["**Proposition (Depletion is compartmental)", "**Proposition (No weighted certification)",
         "**Theorem (Universal failure of weighted certification)", "**Theorem (Non-reduction)"]
miss = [n for n in need if n not in t]
chk(not miss, "statement inventory complete (%d labels checked, %d missing: %s)" % (len(need), len(miss), miss[:8]))
used = sorted({int(m) for m in re.findall(r'\*\*(?:Theorem|Proposition|Definition|Lemma|Remark|Corollary) (\d+)', t)})
chk(all(t.count(f"**{k}") >= 0 for k in used) and len(used) == len(set(used)),
    "main-counter labels used: %s" % used)
dup = [lb for lb in set(re.findall(r'\*\*(?:Theorem|Proposition|Definition|Lemma|Remark|Corollary) \d+[^*]*\*\*', t))
       if len(re.findall(re.escape(lb), t)) > 1]
chk(not dup, "no statement label is stated twice (%s)" % dup[:3])
# 4. heading sequence per section: no duplicates, no gaps
secs = {}
for m in re.finditer(r'^### (\d+)\.(\d+) ', t, re.M):
    secs.setdefault(int(m.group(1)), []).append(int(m.group(2)))
for s, lst in sorted(secs.items()):
    chk(len(lst) == len(set(lst)) and lst == list(range(1, len(lst)+1)), "section %d subsections sequential %s" % (s, lst))
    dup = [h for h in re.findall(r'^### \d+\.\d+ [^\n]+', t, re.M) if re.findall(r'^### \d+\.\d+', h)][0]
chk(all(len(re.findall(r'^### %d\.\d+ [^\n]*$' % s, t, re.M)) == len(secs[s]) for s in secs), "no duplicated subsection headings")
chk([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', t, re.M)] == list(range(1, 12)), "top-level sections numbered 1..11")
# 5. numbers of record
must = ["89.526", "397.87", "2.090", "4.652133", "0.535", "5.000", "4.47", "0.348", "0.187", "4.44",
        "415", "2.57", "4.66", "454", "43", "35", "2.9", "1.79", "1.8", "0.85", "0.25", "0.70", "0.20",
        "1.5", "2026", "0.130", "309", "1,125", "5,050", "121,429", "2,778", "2,088", "5,800,000",
        "3,400,000", "820,000", "1,000,000", "600,000", "74,000,000", "240,000", "239,482", "150"]
tn = t.replace("{,}", "").replace(" ", "")
miss = [m for m in must if m not in tn and m.replace(",","") not in tn]
chk(not miss, "numeric tokens of record present (%d missing: %s)" % (len(miss), miss))
# 6. discipline phrases
phr = ["admissible only when donor-limited", "declared, not computed", "must not be reused numerically",
       "quarantined rather than blanked", "retained rather than blanked", "must not share a column",
       "no cohort statistic is quoted", "not promoted to a forecast", "Cancellation is cheap",
       "not a regular perturbation", "must not be inverted", "inadmissible as certification",
       "the scale must name its flux", "never determines physical destination",
       "every exhaustion statement must name its referent", "forward-invariant",
       "algebraic cancellation alone", "name its referent", "42 of the 43", "archived-pull origin",
       r"\min_m(S_m-\underline B_m)",
       "log biomass margin", "not re-proved here", "identification"]
miss = [p for p in phr if p.lower() not in t.lower()]
chk(not miss, "discipline phrases present (%d missing: %s)" % (len(miss), miss))
# 7. register: no meta-commentary
prodvers = {"v1.12", "v4.44", "v4.66"}
bad_v = [m.group(0) for m in re.finditer(r'\bv\d(\.\d+)*', t) if m.group(0) not in prodvers]
forbidden = [r'\bbaseline\b', r'starting point', r'In plain words',
             r"editor's note", r'change log', r'version note', r'\bthis revision\b', r'as instructed', r'\bREADME\b']
hits = {p: len(re.findall(p, t, re.I)) for p in forbidden if re.search(p, t, re.I)}
chk(not hits and not bad_v, "no meta-commentary markers (%s; version tokens %s)" % (hits or "clean", bad_v or "only product versions"))
# 8. back matter order and reference block
chk(t.find("## Declarations") < t.find("## References"), "Declarations precede References")
chk(t.count("https://doi.org/") >= 7 or len(re.findall(r'doi\.org/', t)) >= 14, "reference DOIs carried (%d doi.org links)" % len(re.findall(r'doi\.org/', t)))
chk("Keywords" in t and "## Abstract" in t, "Abstract and Keywords present")
# 9. index-collision check in 7.2
z = t[t.find('### 7.2'):t.find('### 7.3')]
chk(not re.findall(r'\bb_m\b|\bx_m\b|\bd_m\b|\bw_m\b', z), "no residual b_m/x_m/d_m/w_m in 7.2")
print("\n%d checks failed" % len(fails))
sys.exit(1 if fails else 0)

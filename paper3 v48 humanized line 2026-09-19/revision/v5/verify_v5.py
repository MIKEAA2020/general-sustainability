r"""Checks for revision/v5/paper3_v5.md.  Usage: python3 revision/v5/verify_v5.py [file]

Design: v5 must be v4 plus insertions. Two things are proved about it.
  (1) CONTAINMENT: every sentence unit of v4 appears verbatim in v5, except the two authorised
      replacements, which are whitelisted and must each be present in v5 in their new form.
  (2) INVARIANTS: the v4 invariant suite (numbers of record, discipline phrases, statement
      inventory, heading sequence, register) re-run with the new labels and the new numeric tokens
      admitted.
"""
import re, sys
V4 = 'revision/v4/paper3_v4.md'
P  = sys.argv[1] if len(sys.argv) > 1 else 'revision/v5/paper3_v5.md'
v4 = open(V4, encoding='utf-8').read()
t  = open(P, encoding='utf-8').read()
fails = []
def chk(cond, label):
    print(("  ok   " if cond else "  FAIL ") + label)
    if not cond: fails.append(label)

# ---------------------------------------------------------------- 1. insert-only proof
# Delete every logged insertion (and invert every logged replacement) from v5; the result must be
# byte-identical to v4. This is the strongest available statement of "nothing was subtracted or
# altered": it fails if any existing sentence was touched, duplicated, or reordered.
import json
log = json.load(open('revision/v5/insert_log.json', encoding='utf-8'))
r = t
amb = []
for e in log:
    if r.count(e["text"]) != 1:
        amb.append((e["tag"], r.count(e["text"]))); continue
    r = r.replace(e["text"], e.get("old", ""), 1)
chk(not amb, "every logged block found exactly once on removal (%s)" % (amb or "clean"))
chk(r == v4, "reconstruction of v4 from v5 is byte-identical (%d vs %d chars; delta %d)" % (len(r), len(v4), len(r) - len(v4)))
if r != v4:
    for k in range(min(len(r), len(v4))):
        if r[k] != v4[k]:
            print("      first divergence at %d :: v5-side %r vs v4-side %r" % (k, r[k:k+90], v4[k:k+90])); break
chk(len(log) == 28, "logged operations: 25 insertions + 3 logged repairs/replacements (%d)" % len(log))
chk(t.count("in review") == 0, "no 'in review' placeholder left (%d)" % t.count("in review"))
for frag in ["Abaee, 2026, doi:10.5281/zenodo.22554217", "Definitions 1\u20136 and 21\u201323, Theorems 1\u201315 and 24",
           "\\(i\\ne j\\). Choose any"]:
    chk(frag in t, "authorised replacement present in its new form: %s" % frag[:44])

# ---------------------------------------------------------------- 2. nothing added that is not logged
u5 = re.sub(r'\s+', ' ', t).split('. ')
suspect = [u[:70] for u in u5 if re.search(r'staaged|staged|proposed_inserts|to be verified|Author input|not yet applied', u)]
chk(not suspect, "no staging vocabulary in any sentence (%s)" % suspect[:2])

chk(t.count("\\(") == t.count("\\)"), "inline math delimiters balanced (%d open / %d close; v4 was %d/%d)" % (t.count("\\("), t.count("\\)"), v4.count("\\("), v4.count("\\)")))
chk(t.count("$") == v4.count("$"), "no new math-mode dollars introduced")

# ---------------------------------------------------------------- 3. statement inventory, both counters
need = [f"**Definition {k}" for k in (1,2,3,4,5,6,21,22,23)]
need += [f"**Theorem {k}" for k in (1,5,7,8,9,10,11,12,13,14,15,24)]
need += ["**Proposition 1.", "**Proposition 2.", "**Proposition 4", "**Proposition 6",
         "**Proposition 17", "**Proposition 18", "**Proposition 20", "**Lemma 3",
         "**Remark 2", "**Remark 16", "**Corollary 19"]
need += [f"**Proposition {k}" for k in (25,26,27,28,29,30,31,32)] + ["**Remark 33"]
need += ["**Proposition (Depletion is compartmental)", "**Proposition (No weighted certification)",
         "**Theorem (Universal failure of weighted certification)", "**Theorem (Non-reduction)"]
miss = [n for n in need if n not in t]
chk(not miss, "statement inventory complete incl. v5 labels (%d checked, %d missing: %s)" % (len(need), len(miss), miss))
used = sorted({int(m) for m in re.findall(r'\*\*(?:Theorem|Proposition|Definition|Lemma|Remark|Corollary) (\d+)', t)})
chk(used == list(range(1, 34)), "main counter is exactly 1..33, no gaps and no reuse (%s)" % (used if used != list(range(1,34)) else "1..33"))
dups = [lb for lb in set(re.findall(r'\*\*(?:Theorem|Proposition|Definition|Lemma|Remark|Corollary) \d+[^*]*\*\*', t))
        if len(re.findall(re.escape(lb), t)) > 1]
chk(not dups, "no statement label stated twice (%s)" % dups[:3])
chk(t.count('\\square') == 30, "proof QED marks 24 -> 30, six new proofs (%d)" % t.count('\\square'))
chk(not re.search(r'\(\\square\)\s*\(\\square\)|\u25a1', t), "no duplicated QED mark, no stray box glyph")

# ---------------------------------------------------------------- 4. headings and cross-references
secs = {}
for m in re.finditer(r'^### (\d+)\.(\d+) ', t, re.M):
    secs.setdefault(int(m.group(1)), []).append(int(m.group(2)))
for s, lst in sorted(secs.items()):
    chk(lst == list(range(1, len(lst)+1)), "section %d subsections sequential %s" % (s, lst))
chk([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', t, re.M)] == list(range(1, 12)), "top-level sections numbered 1..11")
refs = t[t.find('## References'):]
body = t[:t.find('## References')]
cited = set(re.findall(r'\(([A-Z][A-Za-z\u00c0-\u00de\'\-]+)(?:,? (?:et al\.|and [A-Z][A-Za-z\u00c0-\u00de\'\-]+))?, (19|20)\d\d', body))
surn = {m.group(1) for m in re.finditer(r'([A-Z][A-Za-z\u00c0-\u00de\'\-]{2,}), (?:[A-Z]\.\.)?', refs)}
newcites = ['Ahuja','Baez','Gale','Prajna','Smith','United Nations','Jacquez','Feinberg','Aubin','Ekins',
            'Neumayer','Munda','Wackernagel','Lin','Blomqvist','Clark','Tilton','Meadows','Daly','Redner',
            'Chhikara','\u00d8ksendal','Brunner']
unresolved = [c for c in newcites if c not in refs]
chk(not unresolved, "every v5 in-text citation has a reference entry (%s)" % (unresolved or "clean"))
still = [c for c in ['Aubin','Blomqvist','Chhikara','Ekins','Lin','Meadows','Munda','Neumayer','Redner','Tilton','Wackernagel','Clark','Smith','Gale','Ahuja','Prajna','Jacquez'] if len(re.findall(re.escape(c), body)) == 0]
chk(not still, "no lineage reference left body-mentionless among those v5 cites (%s)" % (still or "clean"))
chk(len(re.findall(r'\bSEEA\b', body)) >= 1, "SEEA positioned in the body (%d hits)" % len(re.findall(r'\bSEEA\b', body)))
chk(len(re.findall(r'System of National Accounts 2025', body)) >= 1, "SNA 2025 named in the body")
chk(len(re.findall(r'zenodo\.22554217', t)) >= 2, "companion DOI appears in text and reference list (%d)" % len(re.findall(r'zenodo\.22554217', t)))
chk("Compositional Resource Flow Accounting" not in t, "the audits' non-existent title is nowhere in the manuscript")

# ---------------------------------------------------------------- 5. numbers of record (v4 set + v5 additions)
must = ["89.526","397.87","2.090","4.652133","0.535","5.000","4.47","0.348","0.187","4.44","415","2.57","4.66",
        "454","43","35","2.9","1.79","1.8","0.85","0.25","0.70","0.20","1.5","2026","0.130","309","1,125","5,050",
        "121,429","2,778","2,088","5,800,000","3,400,000","820,000","1,000,000","600,000","74,000,000","240,000",
        "239,482","150",
        # v5: computed on the article's own pinned record, and the reported simulation
        "4.6","77.6","0.2","400","6.5","3.7","1073","477","1415","77\u201396"]
tn = t.replace("{,}","").replace(" ","")
miss = [m for m in must if m not in tn and m.replace(",","") not in tn]
chk(not miss, "numeric tokens of record present incl. v5 (%d missing: %s)" % (len(miss), miss))

# ---------------------------------------------------------------- 6. discipline phrases, incl. the new ones
phr = ["admissible only when donor-limited","declared, not computed","must not be reused numerically",
       "quarantined rather than blanked","must not share a column","no cohort statistic is quoted",
       "not promoted to a forecast","Cancellation is cheap","not a regular perturbation","must not be inverted",
       "inadmissible as certification","the scale must name its flux","never determines physical destination",
       "forward-invariant","algebraic cancellation alone","42 of the 43","archived-pull origin",
       r"\min_m(S_m-\underline B_m)","log biomass margin","not re-proved here","identification",
       "two disciplines attach","regime-shift threshold","minimum service-supporting stock",
       # v5 additions, in the article's own register
       "not established","declared with the model","reported as not established","its infeasibility is no evidence of safety",
       "not a scalar certificate","neither is called the other","no product of marginal probabilities",
       "not thereby competent","registered obligation","not a free parameter","not available by inference",
       "rather than closing it","no premium figure is reported"]
miss = [p for p in phr if p.lower() not in t.lower()]
chk(not miss, "discipline phrases present (%d missing: %s)" % (len(miss), miss))

# ---------------------------------------------------------------- 7. register: no meta-commentary
prodvers = {"v1.12","v4.44","v4.66"}
bad_v = [m.group(0) for m in re.finditer(r'\bv\d(\.\d+)*', t) if m.group(0) not in prodvers]
forbidden = [r'\bbaseline\b', r'starting point', r'In plain words', r"editor's note", r'change log',
             r'version note', r'\bthis revision\b', r'as instructed', r'\bREADME\b', r'\bstaged\b',
r'to be verified', r'\bTODO\b', r'\[fix', r'Author input',
             r'not yet applied', r'this file', r'proposed_inserts']
hits = {p: len(re.findall(p, t, re.I)) for p in forbidden if re.search(p, t, re.I)}
chk(not hits and not bad_v, "no meta-commentary or staging vocabulary in the manuscript (%s; version tokens %s)" % (hits or "clean", bad_v or "none"))

# ---------------------------------------------------------------- 8. symbol hygiene in the new blocks
z = t[t.find('### 7.1'):t.find('### 7.3')]
chk(not re.findall(r'\bb_m\b|\bx_m\b|\bd_m\b|\bw_m\b', z), "no residual b_m/x_m/d_m/w_m collision in 7.1-7.2")
s13 = t[t.find('### 1.3'):t.find('## 2. ')]
chk("\\tau_{\\mathrm{use}}" in s13, "the use timescale is declared where it is first used (Section 1.3)")
chk(s13.count("Definition 21") + s13.count("Definition 22") == 2, "new definitions stated in 1.3")
chk("\\sigma_{\\mathrm{liq}}" not in t, "fable T9's colliding sigma not adopted (renamed or dropped)")
chk("A(0)-A(T)" in t or "A(0)-A(T)" in t.replace(" ", ""), "Proposition 25 identity present")

# ---------------------------------------------------------------- 9. back matter
chk(t.find("## Declarations") < t.find("## References"), "Declarations precede References")
for d in ["**Data availability.**","**Supplementary material.**","**Code availability.**",
          "**Declaration of competing interest.**","**AI declaration.**"]:
    chk(d in t, "declarations item present: %s" % d.strip("*").rstrip('.'))
chk(t.find("**Code availability.**") > t.find("**Supplementary material.**") and
    t.find("**Code availability.**") < t.find("**Declaration of competing interest.**"),
    "Code availability sits between Supplementary material and competing interest")
chk(len(re.findall(r'doi.org/', t)) >= len(re.findall(r'doi.org/', v4)), "reference DOIs carried (%d doi.org links)" % len(re.findall(r'doi\.org/', t)))
for e in ["Ahuja, R.K.","Baez, J., Li, X.","Gale, D., 1957","Prajna, S., Jadbabaie, A., 2004",
          "Smith, H.L., 1995","SEEA Central Framework","System of National Accounts 2025"]:
    chk(e in t, "reference entry present: %s" % e)
# alphabetical order of the reference list, first-author surnames
NEIGH = [("Ahuja, R.K.", "Aubin, J.-P."), ("Baez, J., Li, X.", "Blomqvist, L."),
         ("Gale, D., 1957", "G\u00fcntner, A."), ("Prajna, S., Jadbabaie, A., 2004", "Redner, S., 2001"),
         ("Smith, H.L., 1995", "Tapley, B.D."), ("United Nations, 2025.", "Wackernagel, M., Beyers, B., 2019."),
         ("Feinberg, M., 2019", "Gale, D., 1957"), ("\u00d8ksendal, B., 2003", "Prajna, S., Jadbabaie, A., 2004")]
pos = {a: refs.find(a) for a, _ in NEIGH}
pos.update({b: refs.find(b) for _, b in NEIGH})
order_ok = all(0 <= pos[a] < pos[b] for a, b in NEIGH if pos[a] >= 0 and pos[b] >= 0)
chk(all(p >= 0 for p in pos.values()), "new reference entries located (%d/%d found)" % (sum(1 for p in pos.values() if p >= 0), len(pos)))
chk(order_ok, "each new entry sits in its correct alphabetical neighbourhood")
for e in ["Ahuja, R.K.", "Baez, J., Li, X.", "Gale, D., 1957", "Prajna, S., Jadbabaie, A., 2004",
          "Smith, H.L., 1995", "SEEA Central Framework", "System of National Accounts 2025", "United Nations, 2025."]:
    chk(refs.count(e) == 1, "reference entry appears exactly once: %s" % e)

print("\n%d checks failed" % len(fails))
if fails:
    for f in fails: print("  -", f)
sys.exit(1 if fails else 0)

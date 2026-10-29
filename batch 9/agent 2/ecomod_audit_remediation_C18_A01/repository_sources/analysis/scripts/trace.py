import re, csv
MAST="MASTER_joint_assessment_and_implementation_plan.md"
REV ="IMPLEMENTED_revision_ECOMOD.md"
mast=open(MAST).read(); rev=open(REV).read()
KW=['jevons','hutchinson','brander','wackernagel','borucke','lin','galli','blomqvist','giampietro',
    'saltelli','may','antibiotic','basin_shrinkage','shampine','dde23','pydelay','half','omega','saddle',
    'separatrix','one-sided','clamp','ramp','knife','blow','method-dependent','interpol','metadata',
    'hygiene','keywords','modelling','modeling','period','lag','rebound','dimensionless','chi','lambda',
    'transcendental','eigenvalue','spurious','trivial','recovery','grid','footnote','multiplicative',
    'additive','asymmetr','debt','productivity','illusion','residual','basin','mask','deficit',
    'carrying','overshoot','floor','falsifiable','stable','frac','non-generic','non-lipschitz','nonlipschitz']

def nums(t): return set(re.findall(r'\d+\.\d+|\d+',t))
def overlap(item_text):
    return (sum(1 for n in nums(item_text) if n in rev),
            sum(1 for w in KW if w in item_text.lower() and w in rev))

# ---------- extract items from section bodies ----------
sec_pat=re.compile(r'^### 12([A-H])\.\s*(.+)$', re.M)
secs={}
for m in sec_pat.finditer(mast):
    nxt=sec_pat.search(mast,m.end())
    secs[m.group(1)]=mast[m.end(): nxt.start() if nxt else len(mast)]
raw=[]
for lbl in "ABCD":
    if lbl not in secs: continue
    b=secs[lbl]
    pat=re.compile(r'(?:^|\n)\s*(\d{1,2})\.\s+', re.M)
    st=[m for m in pat.finditer(b)]
    for i,m in enumerate(st):
        seg=b[m.start(): st[i+1].start() if i+1<len(st) else len(b)]
        # first non-empty line as title
        for line in seg.split('\n'):
            if line.strip() and not re.match(r'^\s*\d+\.\s*$',line):
                title=re.sub(r'[*_#]','',line).strip()[:80]; break
        raw.append((f"12{lbl}.{m.group(1)}",title,seg))
if "G" in secs:
    b=secs["G"]; pat=re.compile(r'\*\*12G\.(\d{1,2})\b\s*[-\u2013\u2014]\s*([^\n]+)')
    for m in pat.finditer(b):
        nxt=pat.search(b,m.end())
        seg=b[m.start(): nxt.start() if nxt else len(b)]
        raw.append(("12G."+m.group(1), re.sub(r'[*_#]','',m.group(2)).strip()[:80], seg))
if "E" in secs:
    raw.append(("12E.1","PRESERVE (verified-correct; do not fix)", secs["E"]))

# ---------- curated STATUS + REVISION LOCATION (verified by hand + numerics) ----------
CUR={
"12A.1":("SUPERSEDED-num","§10, §5, §1. Master's head numbers were computed on the ORIGINAL gross-depletion model; they do NOT reproduce under (1‴). Mechanism retained as narrow/transient & deficit-limited (≈5.4 yr, vanishes > deficit 0.075; converged RK4)."),
"12A.2":("COVERED","§2.2 (A_ext extinction floor + clamps), §3, §8. Non-Lipschitz K→0 blow-up → bounded minimum-viable K."),
"12A.3":("COVERED","§8. Endpoint D_E method-dependent (5.26/6.74/18.70); 5.240 not robust. Verified 5.26 via sim.py."),
"12A.4":("COVERED","§4.3. Knife-edge χ=1 ⇔ ρ=3q flagged as non-generic."),
"12B.5":("COVERED","§3 (per-capita footprint constant; endogenising e, r_opt offered)."),
"12B.6":("COVERED","§2.2 (gross γE retained as named supplement variant; γ=1/b_G)."),
"12B.7":("COVERED","§2.1/§3/§5 (K is algebraic, not a state; system 3-D)."),
"12C.8":("COVERED","§8 reporting-rigour (ii): state no interpolation / use non-multiple step."),
"12C.9":("COVERED","§8 reporting-rigour (i): state grid range; normalise Re λ by r."),
"12C.10":("COVERED","§8 reporting-rigour (iii): complete scenario/parameter table."),
"12D.11":("COVERED","§7 (cite Hutchinson 1948; soften Haberl & Aubauer novelty)."),
"12D.12":("COVERED","§7 (correct Brander–Taylor characterisation)."),
"12D.13":("COVERED","§7 (GFN reference list adopted)."),
"12D.14":("COVERED","§7 (E5 cleanliness: antibiotic, elevator, per-year, units, tense, truncated sentence)."),
"12E.1":("COVERED","§8 'Verified correctness (do not fix)' list."),
"12G.1":("COVERED","§6 (four falsifiable predictions)."),
"12G.2":("COVERED-RELABEL","§8. Numbers are ORIGINAL-model S0 (0.506→0.044, std IC flips S→C). Corrected S0 has a structurally different (one-sided/deg.) equilibrium → the corrected basin must be recomputed & reported separately; see risk register R1."),
"12G.3":("COVERED","§4.4 (full dimensionless set s,g,f,θ,τ̂)."),
"12G.4":("COVERED","§5 (B/C = environment recovers, humans collapse; opposite of orchard framing). Verified via sim.py B/C M→1.19, P collapse."),
"12G.5":("COVERED-NOTE","§8. (20,20) recovers (min M 0.63–0.64), (30,25) collapses (min M<0.6). Verified; note min-M is grid/dt sensitive, original-model provenance."),
"12G.6":("COVERED","§7 (May orphan, Modeling/Modelling, keywords, .py/.pdf, metadata 233, submission URL/callout grid)."),
"12G.7":("COVERED","§5 (Jevons rebound), §3 (τ_D asymmetry option), §8 (ω=0 spurious, trivial equilibrium/no-recovery, Ω footnote, dde23/Shampine). The second masking set (e=1.15…118 sets) is SUPERSEDED-num."),
}
DEFSTATUS="MISSING"

rows=[]
for idstr,title,seg in raw:
    nb,pw=overlap(seg)
    status,loc=CUR.get(idstr,(DEFSTATUS,"—"))
    typ="ACTIONABLE"
    if 'preserve' in seg.lower() or 'do not' in seg.lower(): typ="INFO-preserve"
    rows.append([idstr,title,typ,status,nb,pw,loc])

with open("SCAN_traceability_matrix.md","w") as o:
    o.write("# MASTER → REVISION TRACEABILITY MATRIX (formal, auditable)\n\n")
    o.write("Generated by `trace.py` from MASTER Parts 12A–12G. **Status is curated/verified** (hand-checked + numeric\n")
    o.write("re-computation), and the `#num`/`#kw` columns give the *automated* evidence (how many of the item's\n")
    o.write("distinctive numbers/keywords appear in the revision). Types: **ACTIONABLE** = a to-do;\n")
    o.write("**INFO-preserve** = a verified-correct statement.\n\n")
    o.write("| ID | Master item | Type | Status | #num | #kw | Revision location + note |\n")
    o.write("|---|---|---|---|---|---|---|\n")
    for r in rows:
        o.write(f"| {r[0]} | {r[1].replace('|','/')} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6].replace('|','/')} |\n")
    o.write("\n## Part 10 checklist (`[ ]`) — keyword-coverage hint only\n\n| Checklist | #kw |\n|---|---|\n")
    for c in re.findall(r'\[ \]([^\n]+)', mast):
        o.write(f"| {c.strip()[:85]} | {overlap(c)[1]} |\n")
    o.write("\n## Part 6 forks\n\n| fork | Option A | Option B | default |\n|---|---|---|---|\n")
    for f in re.findall(r'\| (F\d+) \|([^|]*)\|([^|]*)\|([^|]*)\|', mast):
        o.write(f"| {f[0]} | {f[1].strip()[:42]} | {f[2].strip()[:42]} | {f[3].strip()[:42]} |\n")
with open("SCAN_coverage.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["id","type","status","nums","kw"])
    for r in rows: w.writerow([r[0],r[2],r[3],r[4],r[5]])

from collections import Counter
print("Items:",len(rows),"| types",dict(Counter(r[2] for r in rows)))
print("statuses:",dict(Counter(r[3] for r in rows)))
print("\nItems not COVERED / with a trace flag:")
for r in rows:
    if not r[3].startswith("COVERED"):
        print(f"  {r[0]:7s} {r[3]:20s} {r[1][:50]}")

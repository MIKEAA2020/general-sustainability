import io, re, os

D = '/home/user/papers/'
SIB = {1:(2,3,4,5), 2:(1,3,4,5), 3:(1,2,4,5), 4:(1,2,3,5), 5:(1,2,3,4),
       6:(1,), 7:(8,9), 8:(7,9), 9:(7,8), 10:(11,), 11:(10,)}
TIT = {1:"Obstruction Certificates under Incomplete Observation",
       2:"Exact Probabilistic Sufficiency",
       3:"Computational Certification of Obstruction",
       4:"Minimax Dual Certificates", 5:"Exact Belief Computation",
       6:"Quantifier-Order Separation in Assessment", 7:"Sampled Governance",
       8:"Governance Delay", 9:"Certified Horizons on a Real Record",
       10:"What Depletion Numbers Can Certify", 11:"Forecasting Baselines and the Null"}

def sibblock(n):
    s = ", ".join("Paper %d (%s)" % (m, TIT[m]) for m in SIB[n])
    return ("%% SIBLING PAPERS: %s.\n"
            "%% Cross-cite, do not re-derive: the selector principle, the epistemic kernel\n"
            "%% and the observation structure are defined in Paper 1. Papers 2-5 cite it.\n" % s)

OW = {7: "%% OWNERSHIP: Paper 7 computes the 6.5-year crossing on the sampled map and OWNS it.\n"
         "%%           Paper 8 must cite Paper 7 for that number, not re-derive it.\n",
      8: "%% OWNERSHIP: the 6.5-year crossing is computed and owned by Paper 7 (sampled map).\n"
         "%%           Cite Paper 7 for it. Remove any independent re-derivation here.\n"}

BRIDGE = {
 9: ("Two papers in this family read the same Northern cod record and answer opposite\n"
     "questions, and they are placed together here because the pair is the result. Part~I is\n"
     "constructive: from a Schaefer fit over a stated window it builds a management bound and a\n"
     "certified horizon. Part~II is obstructive: in exact rational arithmetic, with no fitted\n"
     "model, it certifies that specific historical collapse steps were contractions regardless\n"
     "of removals. The two are complementary rather than competing, and there are no numbers to\n"
     "reconcile between them. The link worth drawing runs the other way: that a record's\n"
     "collapse steps were harvest-free contractions is evidence that it is not one stationary\n"
     "production regime, which is the reason the constructive bound is regime-dependent."),
 10: ("Part~I sets out the typology: three widely used depletion diagnostics, what each can and\n"
      "cannot certify, and the readings commonly misattributed to them. Part~II applies it to a\n"
      "worked intervention. The typology is a clarification unless it is tied to a measurable\n"
      "consequence, so the case is not decoration: it is what converts the framework into a claim\n"
      "with a falsifiable output."),
 11: ("Three forecasting studies are collected here because they share one question --- what a\n"
      "baseline can certify --- and because one of them carries a null result that should lead.\n"
      "On a locked retention rule, simple benchmarks beat deliberately simple process-based\n"
      "models. That is reported in Part~II and it is a finding, not a limitation: it constrains\n"
      "what any process-based depletion model can claim to add over a naive baseline, and it is\n"
      "the reason the remaining parts are presented as evidence rather than as new machinery."),
}

HDR_END = "%% ============================================================\n\n"

def after_header(txt, block):
    i = txt.find(HDR_END)
    if i < 0:
        return block + "\n" + txt
    j = i + len(HDR_END)
    return txt[:j] + block + "\n" + txt[j:]

DIV = re.compile(r'% ===== PART: ([^ ]+)  \(source: ([^)]+)\) =====\n\\clearpage\n')

def nice(lab):
    return re.sub(r'_v\d+$', '', lab).replace('_', ' ').title()

report = []
for n in range(1, 12):
    fn = [f for f in os.listdir(D) if f.startswith("paper%02d_" % n) and f.endswith(".tex")][0]
    t = io.open(D + fn, encoding='utf-8').read()
    t = after_header(t, sibblock(n))
    if n in OW:
        t = after_header(t, OW[n])
    if n in BRIDGE:
        seen = [0]
        def rep(m):
            seen[0] += 1
            head = "\\part{%s}\n\\label{part:p%d-%s}\n\n" % (nice(m.group(1)), n, chr(96 + seen[0]))
            if seen[0] == 1:
                head += "\\paragraph{How the parts fit together.} " + BRIDGE[n] + "\n\n"
            return head
        t2 = DIV.sub(rep, t)
        if seen[0] == 0:
            report.append((n, fn, 0, 'NO DIVIDERS FOUND - bridge not inserted'))
            continue
        t = t2
    io.open(D + fn, 'w', encoding='utf-8').write(t)
    dup = 0
    if n in (9, 10, 11):
        lines = [l.strip() for l in t.split('\n') if len(l.strip()) > 40]
        dup = len(lines) - len(set(lines))
    report.append((n, fn, len(re.findall(r"[A-Za-z']+", t)), dup))

for r in report:
    print("  %2d  %-42s %7s w   duplicate long lines: %s" % (r[0], r[1], r[2], r[3]))

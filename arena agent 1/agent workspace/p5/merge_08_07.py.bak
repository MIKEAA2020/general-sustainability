"""Merge paper 8 (Governance Delay) + paper 7 (Sample-and-Hold Governance)
into ONE two-regime paper on institutional latency.

Guarantees: every section, table, figure, result and sentence of both sources is
preserved verbatim, including both original abstracts. The merged file is a NEW
version; neither source is modified.

Structure produced:
    combined title / abstract stating the two-regime design and the general claim
    Part I  - the continuous channel (full body of paper 8)
    Part II - the sampled channel    (full body of paper 7)
    Cross-regime conclusion
    merged references (union, de-duplicated)
    merged declarations
"""
import io, os, re, sys

BASE = '/home/user/papers/'
A = 'paper08_governance_delay_v45.tex'       # continuous delay (DDE)
B = 'paper07_sampled_governance_v50.tex'     # sampled review (sample-and-hold)
OUT = 'paper08_governance_delay_v46.tex'

sa = io.open(BASE + A, encoding='utf-8', errors='replace').read()
sb = io.open(BASE + B, encoding='utf-8', errors='replace').read()


def not_in_comment(s, pos):
    """True if the match at pos is real LaTeX, not inside a % comment.

    Provenance headers in this corpus MENTION \\documentclass and \\begin{document}
    (e.g. "v61 was THREE complete LaTeX documents concatenated (3x \\documentclass,
    3x \\begin{document})"), so a naive find() splits inside a comment.
    """
    line_start = s.rfind('\n', 0, pos) + 1
    return '%' not in s[line_start:pos]


def find_real(s, pat):
    for m in re.finditer(pat, s):
        if not_in_comment(s, m.start()):
            return m
    return None


def split_body(s):
    """-> (preamble, body, references, declarations)"""
    m = find_real(s, r'\\begin\{document\}')
    assert m, "no real \\begin{document}"
    pre, rest = s[:m.start()], s[m.end():]
    m = find_real(rest, r'\\subsection\{References\}')
    assert m, "no References heading"
    body, tail = rest[:m.start()], rest[m.start():]
    d = find_real(tail, r'\\(?:sub)*section\*?\{(?:Declarations|Data Availability|Data availability)')
    if d:
        refs, decl = tail[:d.start()], tail[d.start():]
    else:
        refs, decl = tail, ''
    return pre, body, refs, decl


pre_a, body_a, refs_a, decl_a = split_body(sa)
pre_b, body_b, refs_b, decl_b = split_body(sb)


def _match_brace(s, i):
    """i indexes an opening '{'; return the index of its BALANCED closing '}' (or -1)."""
    depth = 0
    while i < len(s):
        ch = s[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def strip_cmd(x, cmd):
    """remove every \\cmd[...]{...} using BALANCED-brace matching.

    A \\{[^\\}]*\\} regex is wrong here: paper 8's \\author block contains nested
    braces (\\textsuperscript{1}, \\href{..}{..}), so the non-nesting class stops at the
    first '}' and leaves the affiliation tail as stray markup --- which then raises
    "There's no line here to end" on a bare \\\\[0.35em].
    """
    out, pos = [], 0
    pat = re.compile(r'\\' + cmd + r'\*?\s*(?:\[[^\]]*\])?\s*\{')
    while True:
        m = pat.search(x, pos)
        if not m:
            out.append(x[pos:])
            break
        if not not_in_comment(x, m.start()):
            out.append(x[pos:m.end()])
            pos = m.end()
            continue
        j = _match_brace(x, m.end() - 1)
        if j < 0:
            out.append(x[pos:m.end()])
            pos = m.end()
            continue
        out.append(x[pos:m.start()])
        pos = j + 1
    return ''.join(out)


def strip_front(x):
    """remove the per-paper title / author / date / maketitle / linenumbers /
    tableofcontents, so the merged file has exactly one of each.

    The per-paper ABSTRACT IS DELIBERATELY KEPT. It is content, and dropping it would
    lose material: each Part therefore opens with its own original abstract, beneath
    the combined two-regime abstract at the head of the document.
    """
    for cmd in ['title', 'author', 'date', 'maketitle', 'linenumbers', 'tableofcontents']:
        x = strip_cmd(x, cmd)
    x = x.replace('\\end{document}', '')
    return x


body_a = strip_front(body_a)
body_b = strip_front(body_b)

# ---------------- namespace labels so the two Parts cannot collide ----------------
# 6 labels collide (conclusion, discussion, introduction, limitations, references,
# related). Prefix BOTH parts, so every reference in the merged file is unambiguous.
for body, pref in ((body_a, 'dde-'), (body_b, 'sh-')):
    for lb in sorted(set(re.findall(r'\\label\{([^}]*)\}', body))):
        body_new = body.replace('\\label{%s}' % lb, '\\label{%s%s}' % (pref, lb))
        body_new = re.sub(r'\\ref\{%s\}' % re.escape(lb),
                          lambda m: '\\ref{%s%s}' % (pref, lb), body_new)
        body_new = re.sub(r'\\eqref\{%s\}' % re.escape(lb),
                          lambda m: '\\eqref{%s%s}' % (pref, lb), body_new)
        body = body_new
    if pref == 'dde-':
        body_a = body
    else:
        body_b = body

# ---------------- merge preambles (union of packages) ----------------
extra = []
for line in pre_b.split('\n'):
    t = line.strip()
    if t.startswith('\\usepackage') or t.startswith('\\newcommand') or \
       t.startswith('\\DeclareMathOperator') or t.startswith('\\newtheorem'):
        if t not in pre_a:
            extra.append(t)
if extra:
    anchor = pre_a.rfind('\\begin{document}')
    pre_a = pre_a[:anchor] + '\n'.join(extra) + '\n' + pre_a[anchor:]

# ---------------- merge references (union, de-duplicated, alphabetical) ----------------
def split_entries(block):
    body = re.sub(r'^\\subsection\{References\}.*?\n', '', block, flags=re.S)
    parts = re.split(r'(?<=\.)\s+(?=[A-ZÄÖÅ][\w\'{}\\\"~\^\- ]{1,30}?, )', body)
    return [p.strip() for p in parts if p.strip()]


def norm(e):
    return re.sub(r'[^a-z0-9]', '', e.lower())[:110]


ea, eb = split_entries(refs_a), split_entries(refs_b)
merged, seen = [], set()
for e in ea + eb:
    k = norm(e)
    if k in seen:
        continue
    seen.add(k)
    merged.append(e)
merged.sort(key=lambda e: re.sub(r'[^a-z]', '', e.lower())[:24])

# ---------------- new front matter ----------------
TITLE = ("Governance latency: the delay, the clock, and the stability of "
         "periodically reviewed renewable resources")

ABSTRACT = r"""
\begin{abstract}
\noindent\textbf{The general claim.} Whether management stabilises or destabilises a renewable
resource is decided by the \emph{latency of the institution}, not by the ecology alone --- and it
is decided jointly by two things that are usually studied separately: \emph{how long} the
institution takes to convert observed decline into deployed response, and \emph{in what form} that
delay is represented. This paper treats both under one heading, \textbf{governance latency}, and
analyses it in the two formalisations the literature actually uses: a continuous delay in the
control loop, and a clock that observes and updates only at discrete review times. They are not
interchangeable. The same system, at the same parameter vector, has different stability boundaries
under the two --- and the difference is not a numerical nicety: boundaries move, artefact
thresholds appear, and in one channel the instability verdict fails outright in a third of the
perturbation corners tested. \emph{What a model says about governance timing is therefore a
statement about the operator as much as about the institution}, and a stability claim about a
reviewed resource is not interpretable until the decision clock is declared.

\noindent\textbf{Why two regimes.} A delay result proved for a continuous control loop does not
transfer to a body that meets every few years, and a review-interval result computed from a
sampled map does not transfer to a continuously-adjusted fishery. Each regime therefore supports
only half of the claim, and each has been read as though it supported the whole. Analysed together,
the two regimes do something neither does alone: they separate the \emph{phenomenon} --- latency
in the institutional loop is destabilising, and rule-dependently so --- from the
\emph{representation}, whose choice changes the computed answer. Part I establishes the phenomenon
in the continuous channel and Part II establishes that the representation matters in the sampled
channel. Neither result is the other's robustness check; they are different theorems about
different operators, and the paper keeps them separate rather than averaging them.

\noindent\textbf{What is found.} In the continuous channel, the effect of delay is governed by the
sign of the response rule and is not monotone: for the \emph{mobilising} rule, in which effort
responds to decline by deploying more effort, intermediate delay \emph{stabilises} the
equilibrium, with two subcritical Hopf crossings bounding the stabilising window; for the
\emph{protective} rule, a quota-tracking law, loop gain stays below one at the calibrated point and
the equilibrium is exponentially stable at every delay --- a no-Hopf theorem. So ``delay
destabilises'' is false as a generality: where the delay sits, and what the rule does with it,
determine the sign. In the sampled channel, the review interval is itself a stability variable, and
the operator used to compute it is not innocent: at an illustrative baseline the exact sample-and-hold
map crosses once near a $6.5$-year interval while one-step approximations report artefact
crossings, and the protective channel is stable at every interval tested. That crossing is reported
as a band, not a threshold --- under a half-percent joint parameter perturbation it ranges from
under one year to nearly eleven, and under one percent the instability verdict itself fails in
twenty of sixty-four corners --- so the robust content is the operator contrast and the
protective-channel result rather than the location of the crossing. Empirically, a
multiplicity-controlled screen of 42 fish stocks finds no robust institutional cycles, and a
32-system cross-sector search finds no unconfounded oscillator: periodicity alone cannot diagnose
governance feedback.

\noindent\textbf{Structure.} Part I is the continuous-delay study and Part II the sampled-review
study. Each is self-contained --- its own model, results, discussion and conclusions --- and each is
reproduced in full from its companion paper without condensation, opening with that paper's own
abstract. A cross-regime conclusion follows, stating what transfers between the two formalisations
and what does not.
\end{abstract}
"""

CROSS = r"""
\section{Cross-regime conclusion}
\label{conclusion}

The two parts above analyse one object --- the latency between observing a decline and changing
what is deployed --- in the two formalisations the literature uses for it. Read together they
support a claim that neither supports alone, and they delimit each other.

\emph{The claim, and why it needs both parts.} Whether governance stabilises or destabilises a
renewable stock is decided by institutional timing, not by ecological lag alone. Part I shows this
is not a vague assertion but a signed, rule-dependent one: delay is destabilising under a
mobilising rule and not destabilising at all under a protective one, where a no-Hopf theorem gives
exponential stability at every delay. ``Delay destabilises'' is therefore false as a generality ---
\emph{where the latency sits, and what the rule does with it, determine the sign}. Part II shows
the clock is not merely a magnitude but a \emph{design variable with its own stability
consequences}: the interval between reviews moves stability boundaries, and the protective channel
is stable at every interval tested. Neither part's result is implied by the other's, and neither is
the other's robustness check --- they are results about different operators, and the paper reports
them separately rather than pooling them.

\emph{What does \textbf{not} transfer, and why this matters more than what does.} The most useful
thing the two parts establish jointly is a negative: \emph{the representation changes the answer.}
Part II's operator contrast shows stability boundaries moving or vanishing with the discretisation,
with one-step approximations reporting crossings the exact map does not have, and Part I records
the same phenomenon from the other side, an apparent $2.3$-yr threshold under annual protective
review that is a discretisation artefact. A stability claim about a reviewed resource is therefore
\emph{not interpretable until the decision clock is declared} --- and this is a caution directed as
much at the synthesis literature as at either formalism, since a boundary quoted without its
operator is not a result. Correspondingly, the paper's own most-quoted number is reported as a band
rather than a threshold: the $\sim\!6.5$-yr crossing is reproducible across discretisation schemes
($6.50$--$6.73$ yr) but is not identifiable in the parameters, sweeping $0.87$--$10.67$ yr under a
half-percent joint perturbation and vanishing entirely in twenty of sixty-four corners under one
percent. \emph{The operator axis and the parameter axis are different axes}, and stability across
the first says nothing about the second.

\emph{What does transfer.} Three things survive both formalisations. (i) \emph{Rule sign governs
the effect of latency}: mobilising and protective rules respond oppositely to delay in the
continuous channel and oppositely to review cadence in the sampled one, and in both the protective
law is the stable one. (ii) \emph{Faster assessment is not always safer}: the review interval is a
local spectral design parameter, not a monotone good --- in the mobilising channel annual review is
the \emph{unstable} end. (iii) \emph{Periodicity alone cannot diagnose governance feedback}: the
42-stock screen finds no robust institutional cycle and the 32-system search no unconfounded
oscillator, so an observed cycle in a managed stock is not evidence of institutional feedback
without a rule-signed mechanism to attribute it to.

\emph{The design consequences, stated generally.} Because latency is a design variable, the
governance clock can be designed rather than inherited: the interval, the discretisation and the
rule sign are jointly selectable, and Parts I and II between them identify which combinations are
stable and which are not. Because the representation changes the computed answer, any periodic
review regime --- fisheries assessment, climate stocktakes, groundwater permitting --- should be
evaluated on the operator it actually runs on, not on a continuous approximation to it. And because
the parameter axis is the fragile one, a reviewed regime should be assessed for sensitivity to its
own calibration before its stability boundary is quoted.
"""

HEAD = r"""
\part*{Part I --- The continuous channel: governance delay as a lag in the control loop}
\label{part:continuous}
\addcontentsline{toc}{part}{Part I --- The continuous channel}
"""
HEAD2 = r"""
\part*{Part II --- The sampled channel: governance delay as a review clock}
\label{part:sampled}
\addcontentsline{toc}{part}{Part II --- The sampled channel}
"""

# ---------------- assemble ----------------
doc = []
doc.append(pre_a)
doc.append('\\begin{document}\n')
doc.append('\\title{' + TITLE + '}\n')
doc.append(ABSTRACT.strip() + '\n')
doc.append('\\maketitle\n\n')
doc.append('\\tableofcontents\n\n\\newpage\n\n')
doc.append(HEAD.strip() + '\n\n')
doc.append(body_a.strip() + '\n\n')
doc.append(HEAD2.strip() + '\n\n')
doc.append(body_b.strip() + '\n\n')
doc.append(CROSS.strip() + '\n\n')
doc.append('\\subsection*{References}\n\\label{references}\n')
doc.append('\n\n'.join(merged) + '\n\n')
for d in (decl_a, decl_b):
    if d.strip():
        doc.append(d.replace('\\end{document}', '').strip() + '\n')
doc.append('\n\\end{document}\n')

out = ''.join(doc)

# ------------------------------------------------------------------ gate
# This merge is scripted, so damage it introduces returns on the next re-merge
# however carefully the .tex is repaired by hand. Paper08's reference list was
# rebuilt by hand on 2026-10-01 (5 glued lines split, 26 detached tails
# reattached, 5 duplicate entries removed, the list re-sorted) and a clean
# re-merge reproduced every one of those artifacts plus a second Declarations
# block, a second supplementary-material passage and the cross-unit
# paper4_supplementary pointer. Gate the assembled document and refuse to write
# it if the structural classes fire. Fix this script, not the output.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import phase0_scan
phase0_scan.report_gate(phase0_scan.gate_text(out, os.path.basename(OUT)), OUT)

io.open(BASE + OUT, 'w', encoding='utf-8').write(out)

# ---------------- checks ----------------
c = "\n".join(re.sub(r'(?<!\\)%.*$', '', l) for l in out.split('\n'))
print("written:", OUT)
print("  words:", len(re.findall(r"[A-Za-z']+", c)))
print("  doc counts:", c.count('\\documentclass'), c.count('\\begin{document}'), c.count('\\end{document}'))
L = set(re.findall(r'\\label\{([^}]*)\}', c))
R = set(re.findall(r'\\ref\{([^}]*)\}', c))
missing = sorted(r for r in R if r not in L)
print("  labels:", len(L), " refs:", len(R), " MISSING:", missing or "NONE")
print("  merged reference entries:", len(merged))

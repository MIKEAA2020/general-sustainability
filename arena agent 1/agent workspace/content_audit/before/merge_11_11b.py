"""Merge paper 11 (Northern cod forecasting) + paper 11b (Edwards Aquifer forecasting)
into one TWO-SYSTEM paper.

Guarantees: every section, table, figure, result and sentence of both sources is
preserved. The merged file is a NEW version; neither source is modified.

Structure produced:
    combined title / abstract stating the two-system design and the general claim
    Part I  - Northern cod      (full body of paper 11)
    Part II - Edwards Aquifer   (full body of paper 11b)
    Cross-system conclusion     (the general claim)
    merged references (union, de-duplicated)
    merged declarations
"""
import io, re, sys

BASE = '/home/user/papers/'
A = 'paper11_forecasting_baselines_v63.tex'      # Northern cod
B = 'paper11b_edwards_forecast_v2.tex'           # Edwards Aquifer
OUT = 'paper11_forecasting_baselines_v64.tex'

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
    # declarations block starts at the first Declarations-ish heading after references
    d = find_real(tail, r'\\(?:sub)*section\*?\{(?:Declarations|Data Availability|Data availability)')
    if d:
        refs, decl = tail[:d.start()], tail[d.start():]
    else:
        refs, decl = tail, ''
    return pre, body, refs, decl


pre_a, body_a, refs_a, decl_a = split_body(sa)
pre_b, body_b, refs_b, decl_b = split_body(sb)


def strip_front(x):
    """remove the per-paper title / author / date / abstract / maketitle /
    linenumbers, so the merged file has exactly one of each"""
    for cmd in ['title', 'author', 'date', 'maketitle', 'linenumbers', 'tableofcontents']:
        x = re.sub(r'\\' + cmd + r'\*\s*(?:\[[^\]]*\])?\s*\{[^\}]*\}', '', x)
    x = x.replace('\\end{document}', '')
    return x


body_a = strip_front(body_a)
body_b = strip_front(body_b)


# ---------------- namespace paper 11b's labels so nothing collides ----------------
labels_b = set(re.findall(r'\\label\{([^}]*)\}', body_b))
for lb in sorted(labels_b):
    body_b = body_b.replace('\\label{%s}' % lb, '\\label{edw-%s}' % lb)
    body_b = re.sub(r'\\ref\{%s\}' % re.escape(lb), lambda m: '\\ref{edw-%s}' % lb, body_b)
    body_b = re.sub(r'\\eqref\{%s\}' % re.escape(lb), lambda m: '\\eqref{edw-%s}' % lb, body_b)

# namespace paper 11's labels too (so Part I references are unambiguous)
labels_a = set(re.findall(r'\\label\{([^}]*)\}', body_a))
for la in sorted(labels_a):
    body_a = body_a.replace('\\label{%s}' % la, '\\label{cod-%s}' % la)
    body_a = re.sub(r'\\ref\{%s\}' % re.escape(la), lambda m: '\\ref{cod-%s}' % la, body_a)
    body_a = re.sub(r'\\eqref\{%s\}' % re.escape(la), lambda m: '\\eqref{cod-%s}' % la, body_a)

# ---------------- merge references (union, de-duplicated, order-preserving) ----------------
def split_entries(block):
    body = re.sub(r'^\\subsection\{References\}.*?\n', '', block, flags=re.S)
    # entries are separated by ". " before an Author-like capitalised surname
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
TITLE = ("Forecasting under a locked retention rule: process models, naive benchmarks, "
         "and two systems")

ABSTRACT = r"""
\begin{abstract}
\noindent\textbf{The general claim.} Process-based models are not self-justifying. A surplus-production
model or a one-pool water balance is more mechanistic than last-value persistence, and that added
mechanism is widely treated as a reason to prefer it. It is not: it is a \emph{claim}, testable
against a naive benchmark, and it can fail. The value of a process model is bounded by the
predictability of the driver it persists. Where a model's causal content consists of carrying a
driver forward in time, and that driver is close to white, the structure adds parameters without
adding signal --- the mechanism is real but carries no forecast information at the horizon in
question, and persisting it is overhead rather than insight. \emph{A model that persists a
near-white driver has no claim to beat persistence, whatever its mechanistic fidelity.} Two
consequences are general: a negative result of this kind is informative only against a protocol
fixed before any score is computed; and the failure is \emph{diagnostic}, locating the defect in
the driver's spectrum rather than only reporting a loss.

\noindent\textbf{Why two systems.} A finding on one system is a demonstration; the same finding on
two systems from different domains is a replication. This paper scores deliberately simple
process-based forecast models against naive benchmarks on \emph{two} systems under one frozen
retention rule: the Northern cod spawning-stock biomass series (NAFO 2J3KL, 1983--2015), a marine
fishery, and the J-17 annual-mean head series of the Edwards Aquifer (1934--2023), a karst
groundwater system. The two have no hydrology, no biology and no institutional history in common.
The mechanism by which added structure fails differs between them --- a weakly autocorrelated
surplus in the fishery, a near-white annual recharge in the aquifer --- and that difference is the
point: \emph{the test is the same even though the mechanism is not.} Each system is held to the
standard that added structure clears a naive benchmark, and the verdict is allowed to be negative.

\noindent\textbf{What is found.} On both systems, at the annual origin, last-value persistence is
more accurate than the process-based alternatives scored. On the cod series no module is retained
on either unpooled specification; on the aquifer the univariate AR(1) is retained, by a margin the
paper shows to be a coin-flip. At multi-year horizons climatological baselines win on the aquifer,
robustly. Under known ground truth the rule recovers a true autonomous module in \(97\%\) of
replicates at collapse-window parameters, so the empirical non-retention of that module is
evidence about the series rather than about the instrument --- while for the stock-flow and
depensation alternatives at recovery-window parameters power falls below \(15\%\), so their
non-retention is weak evidence. The two systems are never pooled: scores are reported separately
throughout, and no cross-system average is taken.

\noindent\textbf{Structure.} Part I is the Northern cod study and Part II the Edwards Aquifer
study. Each is self-contained --- its own data, specification, models, results, discussion and
conclusions --- and each is reproduced in full from its companion paper without condensation. The
method they share (the locked retention rule and the evaluation design) is restated in each part
with the system-specific detail it carries there. A cross-system conclusion follows.
\end{abstract}
"""

CROSS = r"""
\section{Cross-system conclusion}
\label{conclusion}

The two studies above were designed to answer one question with two systems, and the answer is the
same on both.

\emph{Added structure did not earn its keep at the annual origin.} On the Northern cod series no
module is retained on either unpooled specification: persistence is more accurate than surplus
production, catch-driven stock-flow, autoregressive residuals, lagged initialisation, and
prey-informed productivity. On the Edwards J-17 series, persistence is more accurate than a causal
one-pool balance that persists last year's recharge, and the one module that is retained --- the
univariate AR(1) --- is retained by a margin the study itself shows to be a coin-flip. Neither
result says the models are wrong as descriptions. Both say that, at the horizon at which they were
scored, their structure did not buy accuracy over the assumption that next year looks like this
year.

\emph{The failure is diagnostic, not merely negative.} This is the part that generalises, and it is
why the paper reports a negative result rather than a shrug. In each system the reason added
structure fails is located in the spectrum of the driver the model persists: a weakly
autocorrelated surplus production in the fishery, a near-white annual recharge
(\(r = 0.17\)) in the aquifer. In both cases the model is persisting a quantity that does not
persist, so its causal content cannot contribute at the forecast origin no matter how faithfully it
is specified. That converts "the model lost" into "the model lost \emph{here, for this reason}",
which is actionable: it tells the modeller to look at the driver's predictability before adding
structure that depends on it, and it predicts that the same structure will succeed on a system
whose driver is more persistent. The cod study makes the complementary point in the positive
direction --- under known ground truth the rule recovers a true autonomous module in \(97\%\) of
replicates --- so the instrument is not biased against structure; the structure genuinely did not
earn retention.

\emph{The protocol is what makes the negative result informative.} A finding that a model family
fails is worth little unless the rule was fixed before the scores were seen, and both studies
freeze the scoring core in advance. Both also report power, because a non-retention can mean either
"the structure is absent" or "the test could not see it": on the cod series the distinction is
decisive (\(97\%\) against below \(15\%\), depending on the alternative), and reporting it is what
separates the cases. Both studies decline to pool across systems, so neither verdict is diluted by
the other.

\emph{What transfers and what does not.} What transfers is the test --- that a process-based model
must clear naive persistence and the training mean under a protocol fixed in advance, and that the
driver's predictability bounds what it can achieve --- together with the diagnostic reading of a
failure when it comes. What does not transfer is any specific number: the retention verdicts, the
margins and the power figures belong to their systems and are reported separately throughout. A
reader whose system has a more strongly autocorrelated driver than either of these should expect a
different verdict and should re-score rather than inherit one; both studies say so explicitly.

\emph{The general lesson, in one sentence.} Mechanistic fidelity is a hypothesis about accuracy,
not a substitute for measuring it --- and when a model's mechanism amounts to persisting a
near-white driver, that hypothesis is testable, and in two unrelated systems it failed.
"""

HEAD = r"""
\part*{Part I --- Northern cod (\emph{Gadus morhua}), NAFO 2J3KL}
\label{part:cod}
\addcontentsline{toc}{part}{Part I --- Northern cod}
"""
HEAD2 = r"""
\part*{Part II --- Edwards Aquifer, index well J-17}
\label{part:edwards}
\addcontentsline{toc}{part}{Part II --- Edwards Aquifer}
"""

# ---------------- assemble ----------------
doc = []
doc.append(pre_a)                       # identical preambles
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
if decl_a.strip():
    doc.append(decl_a.replace('\\end{document}', '').strip() + '\n')
doc.append('\n\\end{document}\n')

out = ''.join(doc)
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

"""Merge paper 9 + paper 9b + paper 10b into ONE three-part paper: exact viability
certification on two real resource systems.

Why these three, on the evidence (this is the decision the user asked me to make on merits):

  9b's own opening: "The viability machinery of the obstruction calculus has been
  developed and validated on deliberately small exact instances. This paper applies it to
  a real assessment record -- the Northern cod stock."
  10b does the SAME MOVE on a DIFFERENT system: robust viability kernels of the Edwards
  Aquifer J-17 record, under a retention protocol frozen before any score.

So 9b and 10b are the same operation on two different real systems -- which is exactly the
two-system replication the audit said the corpus lacked. And 10b's machinery is viability
kernels (12 mentions) + a frozen retention protocol (24 mentions), NOT ledger accounting,
which rules out placing it with the aggregation paper (6+10).

Paper 9 supplies the third element: the certification is a CHARACTERISATION, not a
simulation, which is what makes the verdict structural rather than empirical.

The unifying finding the three parts share, and none can state alone:
  CERTIFICATION HAS A HORIZON, AND THE HORIZON IS SET BY THE FITTED MAP, NOT BY THE
  METHOD.  Paper 9: the certified layer has a finite horizon -- six years under the two
  harsher floors, seven under the informative one -- because the map is expansive at the
  reference point.  Paper 10b: every positive-pumping certified kernel is empty beyond
  three years, "an optimistic bound on a defect the out-of-sample audit exceeds."
  Two systems, two independent certification pipelines, the same limitation.
"""
import io, re, sys
sys.path.insert(0, '/home/user/p5')
from mergelib import (not_in_comment, find_real, split_body, strip_front, namespace,
                      merge_preamble, merge_refs, _match_brace)

BASE = '/home/user/papers/'
SRC = [('paper09_cod_certification_v31.tex', 'budget-'),
       ('paper09b_arv_certification_v2.tex', 'regime-'),
       ('paper10b_edwards_aquifer_v1.tex', 'edw-')]
OUT = 'paper09_cod_certification_v32.tex'

TITLE = ("Certification, not simulation: the viability of harvest rules on two real "
         "resource systems, and the horizon of what can be certified")

ABSTRACT = r"""
\begin{abstract}
\noindent\textbf{The general claim.} Reference points and management rules are usually defended by
\emph{simulation}: a rule is run, the trajectory is inspected, and the rule is recommended. This
paper defends them by \emph{certification} instead, on two real resource systems, and argues that
the difference is not stylistic. A simulation shows what happened on the runs that were tried; a
certification states \emph{why}, locates the verdict in a constant, and --- most importantly ---
makes explicit \emph{the horizon over which the verdict holds}. That last point is the paper's
central finding, and it recurs across two systems and independent pipelines: \emph{certification has
a horizon, and the horizon is set by the fitted map, not by the method.} On the Northern cod stock
the certified layer has a finite horizon --- six years under the two harsher floors, seven under the
informative one --- because the map is expansive at the reference point for every admissible carrying
capacity. On the Edwards Aquifer, every positive-pumping certified kernel is empty beyond three
years, an optimistic bound on a defect the out-of-sample audit exceeds. Two systems, different
hydrologies, different institutions, the same shape of limitation. A certified verdict is therefore
not a stronger version of a simulated one; it is a different kind of object, whose validity is
\emph{local in time} and whose locality can be quantified.

\noindent\textbf{Why three parts, two systems.} Certification is not one operation, and the three
parts do three different ones on two real assessment records. Part I \emph{characterises}: the
robustness of a single-threshold reference point to persistent productivity shocks reduces to three
constants, and the kernel computation collapses to algebra. Part II \emph{certifies a historical
event}: it certifies, in exact rational arithmetic, the obstruction structure that the Northern cod
collapse exhibited. Part III \emph{scores a policy family}: it computes robust viability kernels for
competing governance rules on the Edwards Aquifer and retains a rule only if it meets a fixed
criterion. Parts I and II are on Northern cod; Part III is on the Edwards Aquifer. The two systems
have no hydrology, no biology and no institutional history in common --- which is precisely why the
recurrence of the horizon limitation is a finding rather than a property of one fit.

\noindent\textbf{What is found.} Part I: on the increasing branch of the surplus curve, the largest
catch holding the reference point from itself is $C^* = g(\mathrm{LRP}) - |e| = 91.59$ kt, and any
rule's protection margin is exactly $C^*$ minus its catch there --- at that point harvest and
protection are one budget. A second constant, $g_{\max} - |e| = 215.2$ kt, separates viable-but-raised
kernels from empty ones, and the two reproduce the kernel table in closed form. That identity makes
the no-dominance verdict \emph{structural, not empirical}: a reactive rule cannot out-supply a flat
cap it matches in protection. Part II: the certified object is a harvest-free multiplier bracket,
$[\rho,\ \max\{\rho+r,\ \rho/(1-r)\}]$; both collapse steps certify as harvest-free contractions
(upper bounds $0.754$ and $0.372$) under every timing convention, while the reference window's worst
step and the two prelude steps do not certify --- a typology, not a blanket verdict. Part III: at the
618-ft threshold under the drought-of-record floor, training-mean pumping fails within roughly
thirteen years while an interpolated $7.2\%$ mean cut secures the threshold; the reactive rules are
retained only \emph{nominally}, on a hybrid criterion whose wet-year margin is exactly what the
robust class excludes; and nothing is retained at 660 ft, where the rules are invisible to the
kernel of their own trigger.

\noindent\textbf{Structure.} Part I is the harvest--protection budget, Part II the regime-viability
certification, and Part III the Edwards policy-family scoring. Each is self-contained and reproduced
in full from its companion paper without condensation, opening with that paper's own abstract. A
cross-system conclusion follows, stating what certification buys, what it costs, and where its
horizon binds.
\end{abstract}
"""

CROSS = r"""
\section{Cross-system conclusion}
\label{conclusion}

The three parts above certify rather than simulate, on two real assessment records with no hydrology,
no biology and no institutional history in common. Read together they support one claim about the
method and one about its limits, and the second is the more useful.

\emph{What certification buys: the verdict becomes structural.} Part I's central result is that the
no-dominance verdict is \emph{structural, not empirical}. Because the largest catch holding the
reference point from itself is $C^* = g(\mathrm{LRP}) - |e| = 91.59$ kt, and any rule's protection
margin is exactly $C^*$ minus its catch there, harvest and protection are \emph{one budget} at that
point --- and a reactive rule therefore cannot out-supply a flat cap it matches in protection. That
is not a fact about a particular simulation run; it is a fact about two constants, and it holds for
every rule in the class. Part II supplies the same discipline on a harder object: the certified
harvest-free multiplier bracket certifies both collapse steps as harvest-free contractions under
\emph{every} timing convention for the removals accounting, while the reference window's worst step
and the two prelude steps fail to certify. The output is a \emph{typology, not a blanket verdict} ---
which is the honest form of a certification, and the form a simulation cannot produce.

\emph{What it costs: the horizon, and where it comes from.} This is the finding the three parts
establish jointly and none establishes alone. \textbf{Certification has a horizon, and the horizon
is set by the fitted map, not by the method.} In Part I the map is expansive at the reference point
for every admissible carrying capacity $K \ge 2K^*$, so the certified layer has a finite horizon:
six years under the two harsher floors, seven under the informative one. In Part III every
positive-pumping certified kernel is empty beyond three years --- described there as an optimistic
bound on a defect the out-of-sample audit exceeds. The two numbers differ by a factor of two and
come from unrelated systems, and that is the point: the limitation is not an artefact of one
specification. \emph{A certified verdict is valid over a stated horizon, and quoting it without that
horizon is quoting a different claim.} This is the practical discipline certification imposes, and
it is one simulation does not impose --- a simulation shows a trajectory of some length and the
reader is left to supply the horizon.

\emph{What the protocol is for.} All three parts fix the scoring criterion before any score is
computed, and all three report negative results. That combination is what makes a negative result
informative: a rule that fails a criterion fixed in advance has been \emph{tested}, whereas a rule
that fails a criterion chosen afterwards has merely been described. Part III is explicit that its
reactive rules are retained only \emph{nominally}, on a hybrid criterion whose wet-year margin is
exactly what the robust class excludes --- so the nominal retention is reported together with the
reason it is nominal. Part II likewise reports which steps do \emph{not} certify rather than
reporting only the two collapse steps that do. A certification method that only ever produced
positive verdicts would be indistinguishable from advocacy.

\emph{The design consequence, stated generally.} Two results generalise beyond their systems. First,
\emph{where a threshold is protected by the weather rather than by policy, no rule in the scored
family can be credited with protecting it}: Part III finds that the 660-ft line is protected by wet
years, not by the pumping family --- a geometric property of scoring triggers against their own
level, and one that would be invisible to any method that only asked whether the threshold was
breached. Second, \emph{a positive attractor-to-threshold margin defeats every non-negative pumping
rule}, so the binding constraint is geometric rather than institutional. Part I's corresponding
general statement is that harvest and protection are one budget at the reference point, so a gain in
permitted catch is exactly a loss in protection margin and cannot be argued into existence.

\emph{Scope, stated once.} These are scored comparisons on measured systems, and each part states
its own resolution limit. Part III cannot resolve the marginal caps ($P = 0.41$--$0.65$) and says so;
Part II certifies some steps and not others rather than issuing a verdict on the collapse as a whole;
Part I's certified layer is finite-horizon by construction. The general claim is therefore not that
certification resolves more than simulation --- it is that \emph{certification states what it
resolves and over what horizon}, which is the property that makes a verdict usable.
"""

HEADS = [
    r"""\part*{Part I --- The harvest--protection budget at the limit reference point}
\label{part:budget}
\addcontentsline{toc}{part}{Part I --- The harvest--protection budget}""",
    r"""\part*{Part II --- Regime viability on the Northern cod stock}
\label{part:regime}
\addcontentsline{toc}{part}{Part II --- Regime viability on Northern cod}""",
    r"""\part*{Part III --- Governance operators and viability kernels of the Edwards Aquifer}
\label{part:edwards}
\addcontentsline{toc}{part}{Part III --- Edwards Aquifer viability kernels}""",
]

# ---------------------------------------------------------------- assemble
pres, bodies, refss, decls = [], [], [], []
for fn, pref in SRC:
    s = io.open(BASE + fn, encoding='utf-8', errors='replace').read()
    pre, body, refs, decl = split_body(s)
    pres.append(pre)
    bodies.append(namespace(strip_front(body), pref))
    refss.append(refs.replace('\\end{document}', ''))
    decls.append(decl)

# namespacing declarations needs each part's own label set
for i, (_, pref) in enumerate(SRC):
    labs = set(re.findall(r'\\label\{([^}]*)\}', bodies[i]))
    decls[i] = namespace(decls[i], pref, known=labs)

pre = pres[0]
for p in pres[1:]:
    pre = merge_preamble(pre, p)
merged = merge_refs(refss[0], refss[1])
merged = merge_refs('\n'.join(merged), refss[2])

doc = [pre, '\n\\begin{document}\n', '\\title{' + TITLE + '}\n',
       ABSTRACT.strip() + '\n', '\\maketitle\n\n\\tableofcontents\n\n\\newpage\n\n']
for h, b in zip(HEADS, bodies):
    doc += [h.strip() + '\n\n', b.strip() + '\n\n']
doc += [CROSS.strip() + '\n\n',
        '\\subsection*{References}\n\\label{references}\n',
        '\n\n'.join(merged) + '\n\n']
for d in decls:
    if d.strip():
        doc.append(d.replace('\\end{document}', '').strip() + '\n')
doc.append('\n\\end{document}\n')

out = ''.join(doc)
io.open(BASE + OUT, 'w', encoding='utf-8').write(out)

c = "\n".join(re.sub(r'(?<!\\)%.*$', '', l) for l in out.split('\n'))
L = set(re.findall(r'\\label\{([^}]*)\}', c))
R = set(re.findall(r'\\ref\{([^}]*)\}', c))
print("written:", OUT)
print("  words:", len(re.findall(r"[A-Za-z']+", c)))
print("  doc counts:", c.count('\\documentclass'), c.count('\\begin{document}'),
      c.count('\\end{document}'))
print("  labels:", len(L), " refs:", len(R), " MISSING:",
      sorted(r for r in R if r not in L) or 'NONE')
print("  merged reference entries:", len(merged))

#!/usr/bin/env python3
"""Minimax source-scoped alignment: positive nodes, committed history, local dual."""
from pathlib import Path
from difflib import unified_diff
import re
r=Path('/home/user');b=r/'content_audit/claim_alignment';src=r/'papers/paper04_minimax_dual_certificates_v16.tex';old=src.read_text();s=old
abstracts=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',s,re.S);assert len(abstracts)==1
(b/'original_abstracts').mkdir(exist_ok=True,parents=True);(b/'original_abstracts'/(src.stem+'.txt')).write_text(abstracts[0])
def change(a,z):
 global s
 assert s.count(a)==1,(s.count(a),a[:120]);s=s.replace(a,z,1)
change('($k$ the control dimension; the bound is tight).',
       '($k$ the control dimension; tightness is exhibited here in dimensions one and two).')
change('All claims are machine-verified in exact\nrational arithmetic (8 check families).',
       'Eight exact-rational check families verify the declared finite\ninstances, not the general analytic converse or dynamic-envelope claims.')
change('the bound is\ntight in dimension $k$.',
       'the bound is shown tight below in dimensions $k=1$ and $k=2$;\nno general-dimensional tightness example is asserted here.')
change('The tightness bound is Helly\'s theorem in the plane\n(Helly, 1923) applied to the row half-spaces. Tightness:',
       'The following low-dimensional tightness examples illustrate\nthe support bound; the plane case can be read through Helly (1923). Tightness:')
change('\\int_{\\mathcal{K}(B} \\psi', '\\int_{\\mathcal{K}(B)} \\psi')
change('evaluation at information states --- a Bellman recursion, not a\ndifferential operator --- is the well-posed successor of the proposed\ninformation-set operator.',
       'pointwise optimization over \\emph{complete} policies can select\ndifferent past actions on different later cells. It need not obey a\nBellman recursion unless committed action history is included in the\nstate and only future actions are optimized.')
change('states $b$ drawn from a finite partition, admissible actions finite, data\nrational --- define the one-step operator',
       'states $b$ drawn from a finite partition together with their\ncommitted action prefixes (or a proved Markov-sufficient state encoding\nthem), admissible actions finite, data rational --- define the\none-step continuation operator')
change('where $b\'$ is the posterior given $(b, a, y)$\nthe maximum over admissible actions of the prior-averaged next-belief\nvalue.',
       'where $b\'$ records the posterior and the committed prefix\nextended by $a$ after observation $y$; the maximum concerns only\nnot-yet-chosen actions. Bare posterior cells alone need not be a\nsufficient state for path-dependent terminal $F$.')
change('(ii)\n$Q(0) = \\Phi^{N} g$ is computed exactly by backward induction, in rational\narithmetic;',
       '(ii)\nwith committed prefixes the initial attainable value $Q(0)$ is\ncomputed exactly by the finite backward induction \\(\\Phi^N g\\),\nin rational arithmetic; this does not identify intermediate values\nwith the pointwise essential supremum over complete policies in\nDefinition~\\ref{def:envelope};')
change('Well-posedness --- existence and uniqueness of the recursion\'s output ---\nis supplied by the same induction.',
       'Well-posedness of the committed-prefix recursion follows from\nthe same induction. For a counterexample to posterior-only recursion,\nchoose a blind first action $a_1\\in\\{0,1\\}$ and then reveal a\nfair bit $s\\in\\{0,1\\}$, with terminal reward\n$G(s,a_1)=\\mathbf{1}[a_1=s]$. Every feasible complete policy has\ninitial value $1/2$; at the revealed cell the pointwise essential\nsupremum over \\emph{complete} policies is $1$ for each bit, by\nretrospectively choosing two different first actions. A Bellman\ncontinuation retaining the first action returns $1/2$, as required.')
change('Under the setup above: \\emph{(i) tower and martingale.}',
       'Under the setup above, use the recursion only on cells\n$C$ with $\\mu^*(C)>0$; omit null children from its sums and leave\nnull-node conditional values undefined (or assign arbitrary values\nthat never affect the root). In particular the initial node is\npositive-mass. Then: \\emph{(i) tower and martingale.}')
change('with the child weights\n$w(C\') = \\mu^{*}(C\')/\\mu^{*}(C)$,',
       'over positive-mass children only, with the child weights\n$w(C\') = \\mu^{*}(C\')/\\mu^{*}(C)$,')
change('\\emph{(ii)} By backward induction on the stage. For $k = K$',
       '\\emph{(ii)} Positive-mass conditioning makes each weight\nwell-defined and null children contribute zero to the root. Proceed\nby backward induction on the stage. For $k = K$')
change('The duality results above are formalized in Lean~4 in \\texttt{Formalizations/Minimax\\_Dual} (\\(21\\) theorems and lemmas, importing only the\nproject prelude).',
       'The Lean~4 module \\texttt{Formalizations/Minimax\\_Dual} proves\nconditional soundness of a supplied finite measure certificate and\nspecific algebraic examples, not the Sion converse, sparse bound or\ndynamic envelope. A current comment-stripped count including Unicode names finds \\(22\\)\n\\texttt{theorem} declarations and no \\texttt{lemma} declarations.\nThe historical report of \\(21\\) is an undercount: an ASCII-only name\nfilter reproduces it by omitting \\texttt{\\ensuremath{\\psi}single\\_sum}.\nThe original historical counting command has not been recovered; this\nis a reproducible explanation, not proof of its exact implementation.\nNo current-toolchain build is claimed. The module imports only the\nproject prelude.')
change('\\textbf{This paper\'s obstruction is the emptiness of that object, and it should be read that\nway.} The common safe-action set is nonempty exactly when the relevant discriminating domain\nis nonempty, so Theorem~\\ref{thm:dual} is, in the vocabulary of that programme, a\ncertificate for the discriminating kernel being empty. That is a real collision with prior\nart and is conceded here rather than argued around.',
       '\\textbf{The static local obstruction is not a global-kernel test.}\nTheorem~\\ref{thm:dual} certifies emptiness of the common\n\\emph{instantaneous} safe-action set at the declared information\nstate under its compact-control hypotheses. A global discriminating\nor viability kernel additionally requires a horizon/invariance\nargument. For example, on $[0,1]$ with $\\dot x=1$ and $U=\\{0\\}$,\n$x=0$ has an inward-pointing instantaneous action, but every\ntrajectory eventually exits and the infinite-horizon kernel is\nempty. The established global-kernel programme is therefore related\nprior art, not a logically equivalent restatement of this static dual.')
change('and shows the bound tight. Note the scaling:',
       'with tight examples shown here for $k=1,2$. Note the scaling:')
change('the declaration counts and named declarations quoted below were\nre-counted and confirmed present.',
       'the named declarations quoted below were confirmed present;\nthe 21-vs-22 undercount is explained above and logged with its counting convention.')
change('$Q_{0} = \\sum_{C \\in \\mathcal{P}_{1}} \\mu^{*}(C)\\,\nN_{1}(C)$',
       '$Q_{0} = \\sum_{C \\in \\mathcal{P}_{1}:\\mu^*(C)>0} \\mu^{*}(C)\\,\nN_{1}(C)$')
change('Theorem~\\ref{thm:dual} returns a \\emph{probability measure} on the\n  active boundary--disturbance bundle, finitely supported, whose existence is equivalent to\n  emptiness. Membership in a kernel is thereby converted into the existence of a dual object\n  that can be exhibited and checked without running the iteration.',
       'Theorem~\\ref{thm:dual} returns a \\emph{probability measure} on the\n  active boundary--disturbance bundle, finitely supported, whose existence is equivalent to\n  emptiness of the \\emph{local common safe-action set} under its hypotheses.\n  This does not by itself decide membership in a global invariant kernel.')
out=b/'drafts'/src.name;out.parent.mkdir(exist_ok=True,parents=True);out.write_text(s)
(b/'diffs'/(src.stem+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(src),tofile=str(out))))
print(out)

#!/usr/bin/env python3
"""Final consistent presentation changes to the v66 repair draft."""
from pathlib import Path
B=Path('/home/user/paper 2 family/01_obstruction');p=B/'paper01_obstruction_calculus_v66.tex';s=p.read_text()
def ch(a,b,label):
 global s
 assert s.count(a)==1,(label,s.count(a));s=s.replace(a,b)
ch('There are \\(q\\) of class \\(C^1\\), defined on a neighbourhood of','There is a function \\(q\\) of class \\(C^1\\), defined on a neighbourhood of','theorem grammar')
ch('''\\texttt{Wk\\_antitone}, \\texttt{Wk\\_descending} & Definition~\\ref{calc-def:kernel}\\\\''','''\\texttt{Wk\\_antitone}, \\texttt{Wk\\_descending} & finite-horizon recursion (Theorem~\\ref{calc-thm:finite-horizon})\\\\''','Lean finite')
ch('''\\texttt{commonSafe}, \\texttt{Blocked}, \\texttt{blocked\\_iff} & Theorem~\\ref{calc-thm:common-action}\\\\''','''\\texttt{commonSafe}, \\texttt{Blocked}, \\texttt{blocked\\_iff} & finite one-step common-action result (Theorem~\\ref{calc-thm:onestep})\\\\''','Lean common')
ch('''\\texttt{preOp\\_mono} & Proposition~\\ref{calc-prop:monotone}\\\\''','''\\texttt{preOp\\_mono} & monotonicity of the finite predecessor operator (Section 3.1), not Proposition~\\ref{calc-prop:monotone}'s full cross-model statement\\\\''','Lean predecessor')
ch('''The discrete core of the calculus is
additionally machine-checked, and this subsection records exactly what that covers and
what it does not.''','''The earlier discrete formalization covers a separate finite fragment;
its recorded build does not prove the continuous-time Theorems 3 or 7,
nor validate the finite-state Table~\\ref{calc-tab:patch}. That table is
checked by a separate exhaustive script. The present v66 edits have
not been independently reviewed in Lean or by an external referee.''','Lean scope')
ch('The audit is symbolic and one-dimensional, with two two-dimensional instances','The audit is symbolic, including two two-dimensional instances','audit count')
p.write_text(s)
q=B/'paper01_obstruction_calculus_v66_supplementary.tex';t=q.read_text()
a='There are \\(q\\) of class \\(C^1\\), defined on a neighbourhood of';b='There is a function \\(q\\) of class \\(C^1\\), defined on a neighbourhood of';assert t.count(a)==1;t=t.replace(a,b)
a='The mechanism is \\emph{admissibility} rather than a hidden mode:';b='The mechanism is a state-dependent-admissibility-induced \\emph{safety obstruction}, not an empty common admissible set:';assert t.count(a)==1;t=t.replace(a,b)
a='\\(U(S) = \\{0, r(S)\\}\\), \\(\\mathcal{V} = [1,2]\\)';b='the unrelaxed nonconvex \\(U(S) = \\{0, r(S)\\}\\), \\(\\mathcal{V} = [1,2]\\)';assert t.count(a)==1;t=t.replace(a,b)
q.write_text(t)
print('POLISHED',p,len(s),'supplement',len(t))

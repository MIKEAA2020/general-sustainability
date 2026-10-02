#!/usr/bin/env python3
"""Layout-only v67 head from v66; preserve v65/v66 unchanged."""
from pathlib import Path
from shutil import copyfile
R=Path('/home/user');D=R/'paper 2 family/01_obstruction';src=D/'paper01_obstruction_calculus_v66.tex';dst=D/'paper01_obstruction_calculus_v67.tex'
s=src.read_text()
old=r'''\begin{center}
\begin{tabular}{@{}ll@{}}
\toprule
Lean declaration & Result here\\
\midrule
\texttt{finite\_horizon\_sound}, \texttt{finite\_horizon\_complete} & Theorem~\ref{calc-thm:finite-horizon}\\
\texttt{Wk\_antitone}, \texttt{Wk\_descending} & finite-horizon recursion (Theorem~\ref{calc-thm:finite-horizon})\\
\texttt{commonSafe}, \texttt{Blocked}, \texttt{blocked\_iff} & finite one-step common-action result (Theorem~\ref{calc-thm:onestep})\\
\texttt{preOp\_mono} & monotonicity of the finite predecessor operator (Section 3.1), not Proposition~\ref{calc-prop:monotone}'s full cross-model statement\\
\bottomrule
\end{tabular}
\end{center}'''
new=r'''\begin{table}[tbp]
\centering
\scriptsize
\setlength{\tabcolsep}{2pt}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{.50\columnwidth}>{\raggedright\arraybackslash}p{.43\columnwidth}@{}}
\toprule
Lean declaration & Claim supported here\\
\midrule
\texttt{finite\_horizon\_sound} & Finite recursion (Theorem~\ref{calc-thm:finite-horizon})\\
\texttt{finite\_horizon\_complete} & Finite recursion (Theorem~\ref{calc-thm:finite-horizon})\\
\texttt{Wk\_antitone} & Finite recursion (Section 3.1)\\
\texttt{Wk\_descending} & Finite recursion (Section 3.1)\\
\texttt{commonSafe} & Finite one-step result (Theorem~\ref{calc-thm:onestep})\\
\texttt{Blocked} & Finite one-step result (Theorem~\ref{calc-thm:onestep})\\
\texttt{blocked\_iff} & Finite one-step result (Theorem~\ref{calc-thm:onestep})\\
\texttt{preOp\_mono} & Finite predecessor only; not full Proposition~\ref{calc-prop:monotone}\\
\bottomrule
\end{tabular}
\caption{Selected Lean declarations. None formalizes the continuous-time Theorems 3 or 7 or independently checks Table~\ref{calc-tab:patch}.}
\label{calc-tab:lean-scope}
\end{table}'''
assert s.count(old)==1,s.count(old)
s=s.replace(old,new)
old=r'\includegraphics[width=0.82\linewidth]{figs_p2/fig_p2_coverage.png}'
new=r'\includegraphics[width=0.98\textwidth]{figs_p2/fig_p2_coverage_v67.png}'
assert s.count(old)==1;s=s.replace(old,new)
assert not dst.exists() or dst.read_text()==s
if not dst.exists():dst.write_text(s)
supp_src=D/'paper01_obstruction_calculus_v66_supplementary.tex';supp_dst=D/'paper01_obstruction_calculus_v67_supplementary.tex'
assert not supp_dst.exists() or supp_dst.read_bytes()==supp_src.read_bytes()
if not supp_dst.exists():copyfile(supp_src,supp_dst)
# The v65/v66 main-figure assets are separate from the family folder; mirror
# the two unchanged dependencies so the v67 family directory compiles alone.
for name in ('fig_p2_common_action.png','fig_p2_timing.png'):
 a=R/'b01/figs_p2'/name;b=D/'figs_p2'/name
 assert a.is_file() and (not b.exists() or b.read_bytes()==a.read_bytes())
 if not b.exists():copyfile(a,b)
print('CREATED',dst,len(s),'supplement',supp_dst,'figure assets complete')

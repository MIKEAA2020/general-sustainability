#!/usr/bin/env python3
"""Narrow editorial repairs to NEW versions of staged 01–05 and live 01–05.
Lean evidence promotion was separately diff-reviewed; this script does not touch old sources.
"""
from pathlib import Path
from difflib import unified_diff
import re, shutil
R=Path('/home/user');A=R/'content_audit/editorial_revisions'
pairs={
 '01':('01_obstruction','paper01_obstruction_calculus_v63.tex','paper01_obstruction_calculus_v64.tex'),
 '02':('02_probabilistic_sufficiency','paper02_probabilistic_sufficiency_v12.tex','paper02_probabilistic_sufficiency_v13.tex'),
 '03':('03_computational_certification','paper03_computational_certification_v16.tex','paper03_computational_certification_v17.tex'),
 '04':('04_minimax_dual_certificates','paper04_minimax_dual_certificates_v16.tex','paper04_minimax_dual_certificates_v17.tex'),
 '05':('05_exact_belief_computation','paper05_exact_belief_computation_v16.tex','paper05_exact_belief_computation_v17.tex'),
}
TIP='1d27e763c4b55d9d2c355ccc31b31689e435b772'
def once(s,a,b):
 assert s.count(a)==1,('match',s.count(a),a[:160]);return s.replace(a,b,1)
def move(s,start,end,anchor):
 assert all(s.count(q)==1 for q in (start,end,anchor)),(start,end,anchor)
 i=s.index(start);j=s.index(end,i);k=s.index(anchor)
 assert k<i,(k,i)
 block=s[i:j];s=s[:i]+s[j:];s=s.replace(anchor,block+'\n'+anchor,1);return s
oldfiles=[]
for key,(dir,old,new) in [(k,pairs[k]) for k in ('04','05')]:
 for lineage in ('staged','live'):
  base=(R/'paper 2 family'/dir/old) if lineage=='staged' else (R/'papers'/new)
  output=(R/'paper 2 family'/dir/new) if lineage=='staged' else base
  src=base.read_text();s=src
  if key=='01':
   s=once(s,r'with \(r\) continuous and injective, \(U(S) = \{0, r(S)\}\)',r'with the concrete choice \(r(S)=S\) (continuous, injective, and bounded below by \(1\) on \([1,2]\)), and \(U(S) = \{0, S\}\)')
   s=once(s,'injectivity of \\(r\\) rules out a common \\(r(S)\\) --- so the policy must hold \\(u = 0\\), and \\(\\dot S = -r(S) < 0\\) drives every compatible trajectory out of \\(\\mathcal{V}\\) in finite time.', 'the only action shared by all \\(U(S)\\) is zero --- so every observation-based policy must hold \\(u=0\\). Then \\(S(t)=S(0)e^{-t}\\) crosses the lower boundary at \\(t=\\log S(0)\\le\\log 2\\) for \\(S(0)>1\\), and leaves immediately from \\(S(0)=1\\).')
   s=once(s,r'\subsubsection{3.7 A worked case: an exact obstruction on a continuum}',r'\subsubsection{3.8 A worked case: an exact obstruction on a continuum}')
   s=once(s,r'\subsubsection{3.8 Mechanized verification of the discrete core}',r'\subsubsection{3.9 Mechanized verification of the discrete core}')
   # Remove source-only stale header decision; preserve substantive source-version note.
   s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
  elif key=='02':
   s=move(s,r'\section{Related work}',r'\subsection*{References}',r'\subsection{The augmented model, the safety value, and the selector}')
   s=once(s,"(folder \\texttt{arena agent 1/paper rewrites/latex}, at the commit\npinned to this article's submission)","(folder \\texttt{arena agent 1/paper rewrites/latex}, at the verified\nrepository revision \\texttt{"+TIP+"})")
   s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
  elif key=='03':
   s=move(s,r'\section{Related work}',r'\subsection*{References}',r'\subsection{Model, information, and quantifiers}')
   s=once(s,'The certificate produced by the pipeline of this paper has a size that scales with the\n\\emph{information--time product}: the product of how much the controller can learn and over how\nlong a horizon it must act. It does not scale with the input dimension --- the dimension of the\nstate, of the disturbance, or of the discretisation standing in for either. A high-dimensional\nsystem about which little can be learned over a short horizon is cheap to certify; a\nlow-dimensional system observed richly over a long horizon is expensive. Dimensionality is the\nwrong axis, and pipelines organised around reducing it are optimising the wrong quantity.',
'The \\emph{minimal support of this certificate} is bounded by the information--time rank\nof the declared relaxation. Proposition~\\ref{prop:rank} shows that the number of scalar\ncontrol inputs alone does not bound how many compatible modes a witness must involve.\nThis is a statement about certificate support, not a dimension-independent bound on\nassembling or solving the linear program: the state, disturbance, and discretisation\nstill affect computational cost.')
   s=once(s,"(folder \\texttt{arena agent 1/paper rewrites/latex}, at the commit\npinned to this article's submission)","(folder \\texttt{arena agent 1/paper rewrites/latex}, at the verified\nrepository revision \\texttt{"+TIP+"})")
   s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
  elif key=='04':
   start=r'\begin{table}[h]';end=r'\section{The measure dual of the common-action obstruction}'
   assert s.count(start)==1 and s.count(end)==1
   region=s[s.index(start):s.index(end)]
   region=once(region,r'\begin{tabular}{@{}l p{4.6cm} l@{}}',r'\begin{tabular}{@{}l p{0.82\linewidth}@{}}')
   region=once(region,r'Family & Statement certified & Checks \\',r'Family & Check family / reported scope \\')
   blank=' & '+('\\'*2)+'\n'
   assert region.count(blank)==8,region.count(blank)
   region=region.replace(blank,' '+('\\'*2)+'\n')
   s=once(s,s[s.index(start):s.index(end)],region)
   s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
  elif key=='05':
   s=once(s,r'\title{Exactness is not the limitation: belief-state computation at scale and the audits that bind the obstruction calculus to its worked systems}',r'\title{Exactness is not the limitation: belief-state computation at scale}')
   s=once(s,r'\part*{Part I --- Exact belief-state computation at scale}'+'\n'+r'\label{part:scale}'+'\n'+r'\addcontentsline{toc}{part}{Part I --- Computation at scale}'+'\n\n','')
   s=once(s,"The title's ``Scale~II'' refers to a companion relation, not to a volume number. The\ntheory being computed here",'The theory being computed here')
   s=once(s,'All claims below\nare regenerated by the paper\'s verification script in exact integer\nand rational arithmetic, standard library only.','The four-cube core and its finite tables are regenerated by a deposited\nstandard-library exact-arithmetic script. The five-cube classification is\nproved in Section~\\ref{scale-fivecube}; separate finite clique and alpha-mask\nchecks use NetworkX and NumPy, respectively, and are identified in the\nverification methods rather than attributed to the legacy script.')
   if lineage=='live':
    stage=(R/'paper 2 family'/dir/old).read_text()
    mark=r'\subsection{Verification methods}\label{scale-methods}'
    end=r'\subsection{Delimitations}\label{scale-scope}'
    assert all(t.count(mark)==1 and t.count(end)==1 for t in (s,stage))
    s=once(s,s[s.index(mark):s.index(end)],stage[stage.index(mark):stage.index(end)])
   s=once(s,'Their source-specific results accompany this\nalignment draft and are not covered by a green legacy script.',r'The separate source-specific scripts and preserved run logs are archived with this manuscript in \texttt{artifacts/ebc\_fivecube/}; they are not covered by the legacy four-cube script.')
   s=once(s,'The five-parameter classification added after that version requires a separate verification record; coverage by this older script is not claimed.', 'The five-parameter classification has an analytic proof in this article; the separate finite enumeration scripts and run logs are attached at \\texttt{artifacts/ebc\\_fivecube/}. Coverage by the older four-cube script is not claimed.')
   s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
  assert s!=src,(key,lineage)
  if lineage=='staged':assert not output.exists(),output;output.write_text(s)
  else:output.write_text(s)
  d=''.join(unified_diff(src.splitlines(True),s.splitlines(True),fromfile=str(base.relative_to(R)),tofile=str(output.relative_to(R))))
  (A/f'editorial_{key}_{lineage}.diff').write_text(d)
  print(key,lineage,output.relative_to(R),len(d.splitlines()),'diff lines')

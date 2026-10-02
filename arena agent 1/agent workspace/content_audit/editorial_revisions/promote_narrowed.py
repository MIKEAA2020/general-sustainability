#!/usr/bin/env python3
"""Reportable, per-paper promotion of previously reviewed Lean prose only.
The other editorial repairs are a separate pass. Originals are never overwritten.
"""
from pathlib import Path
from difflib import unified_diff
R=Path('/home/user')
M={
 '01':('paper01_obstruction_calculus_v63.tex','paper01_obstruction_calculus_v64.tex','01_obstruction'),
 '02':('paper02_probabilistic_sufficiency_v12.tex','paper02_probabilistic_sufficiency_v13.tex','02_probabilistic_sufficiency'),
 '03':('paper03_computational_certification_v16.tex','paper03_computational_certification_v17.tex','03_computational_certification'),
 '04':('paper04_minimax_dual_certificates_v16.tex','paper04_minimax_dual_certificates_v17.tex','04_minimax_dual_certificates'),
 '05':('paper05_exact_belief_computation_v16.tex','paper05_exact_belief_computation_v17.tex','05_exact_belief_computation'),
}
def take(text,start,end):
 assert text.count(start)==1,(start,text.count(start));p=text.index(start)
 assert text.count(end,p+len(start))>=1,end
 q=text.index(end,p+len(start));return text[p:q]
def swap_from_stage(live,staged,start_live,end_live,start_staged=None,end_staged=None):
 old=take(live,start_live,end_live)
 new=take(staged,start_staged or start_live,end_staged or end_live)
 assert old!=new,start_live
 return live.replace(old,new,1)
def replace_once(text,a,b):
 assert text.count(a)==1,(a,text.count(a));return text.replace(a,b,1)
for i in ['01','02','03','04','05']:
 oldfn,newfn,group=M[i]; live_path=R/'papers'/oldfn; staged_path=R/'paper 2 family'/group/oldfn
 live=live_path.read_text();stage=staged_path.read_text();result=live
 if i=='01':
  result=swap_from_stage(result,stage,r'\noindent\textbf{Verification provenance.}',r'\paragraph{Two scope limits, stated plainly.}',r'\noindent\textbf{Current Lean provenance.}')
  result=replace_once(result,r'\texttt{sorryAx} appears nowhere.',r'\texttt{sorryAx} is absent from the checked P1 declarations and the audited aggregate-import footprints; project-wide generated dependencies are disclosed below.')
 if i=='02':
  result=swap_from_stage(result,stage,'Scaling past the certified instances',r'\subsection{Conclusion}')
  result=swap_from_stage(result,stage,r'\item \textbf{Machine-checking}:','\\end{enumerate}'.replace('\\','\\'))
  marker=r'\noindent Not claimed:'
  result=replace_once(result,marker,take(stage,r'\noindent\textbf{Current Lean provenance.}',marker)+marker)
 if i=='03':
  result=swap_from_stage(result,stage,r'\noindent\textbf{A mechanized layer, distinct from the scripts.}', 'Three scripts and one package')
 if i=='04':
  result=swap_from_stage(result,stage,'Dynamic-envelope, quantization, and stochastic-bridge extensions are','\\end{abstract}'.replace('\\','\\'))
  result=swap_from_stage(result,stage,r'\section{Mechanized verification}',r'\noindent\textbf{Scope.}')
 if i=='05':
  result=swap_from_stage(result,stage,r'\subsection{Mechanized verification}',r'\subsection{Verification methods}')
  result=swap_from_stage(result,stage,r'\noindent\textbf{Verification provenance.}',r'\noindent\textbf{Scope.}',r'\noindent\textbf{Current Lean provenance.}') if r'\noindent\textbf{Verification provenance.}' in result else result
  # Mechanized-section replacement already includes Current Lean provenance.
 assert result!=live,i
 assert 'The build has not been re-run since the toolchain' not in result,i
 if i=='02':assert 'nine distinct generated axiom names' in result
 if i=='04':assert 'not the Sion converse, sparse bound' in result
 if i=='05':assert 'No EBC declaration enumerates' in result
 out=R/'papers'/newfn;assert not out.exists(),out;out.write_text(result)
 diff=''.join(unified_diff(live.splitlines(True),result.splitlines(True),fromfile=str(live_path.relative_to(R)),tofile=str(out.relative_to(R))))
 d=R/'content_audit/editorial_revisions'/('promotion_'+i+'.diff');d.write_text(diff)
 print(i,newfn,len(diff.splitlines()),'diff lines',len(result)-len(live),'new chars')

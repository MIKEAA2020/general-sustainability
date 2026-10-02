#!/usr/bin/env python3
"""Non-destructive paper09/ARV two-document host extraction.
Live v32 and the pre-host ARV v2 draft stay intact as remote-backed ancestors.
This produces review candidates, not an approved Preprints.org submission.
"""
from pathlib import Path
from difflib import unified_diff
import re
R=Path('/home/user');base=R/'content_audit/claim_alignment';live=(R/'papers/paper09_cod_certification_v32.tex').read_text();arv_file=base/'drafts/paper09b_arv_certification_v2.tex';arv=(base/'original_sections/paper09b_arv_v2_prehost.tex').read_text()
assert 'Part II --- Regime viability on the Northern cod stock' in live
start=live.index('\\part*{Part II --- Regime viability on the Northern cod stock}')
end=live.index('\\part*{Part III --- Governance operators',start)
embedded=live[start:end]
archive=base/'original_sections/paper09_v32_embedded_ARV.tex';archive.parent.mkdir(exist_ok=True);archive.write_text(embedded)
main=live[:start]+live[end:]
def once(old,new):
 global main
 assert main.count(old)==1, (old[:90],main.count(old))
 main=main.replace(old,new,1)
# Keep the original substantive cod/Edwards results; remove only the old three-part framing.
a0=main.index('\\begin{abstract}');a1=main.index('\\end{abstract}',a0)
abstract=main[a0:a1]
q0=abstract.index('\\noindent\\textbf{Why three parts, two systems.}')
q1=abstract.index('\\noindent\\textbf{What is found.}',q0)
abstract=abstract[:q0]+'''\\noindent\\textbf{Why two systems and a cod companion.} The main paper compares two
methods of certification on two real assessment systems. The Northern cod analysis
characterises a fitted-model harvest--protection budget; the Edwards Aquifer analysis
scores governance rules under an independently fitted map. The separately titled
\\emph{Part II companion, Regime Viability on the Northern Cod Stock}, uses the
same cod record but a different, exact-rational multiplier-bracket method. Its
historical-event certificate is not a fitted-model result of this main paper.

'''+abstract[q1:]
q0=abstract.index('Part II: the certified object is a harvest-free multiplier bracket,')
q1=abstract.index('at the\n618-ft threshold',q0)
abstract=abstract[:q0]+'The Edwards analysis: '+abstract[q1:]
q0=abstract.index('\\noindent\\textbf{Structure.}')
abstract=abstract.replace('Part I: on the increasing branch','System I: on the increasing branch').replace('The Edwards analysis: at the','System II: at the')
abstract=abstract.replace('\\emph{Part II companion, Regime Viability on the Northern Cod Stock}, uses', '\\emph{Part II companion: Regime Viability on the Northern Cod Stock} uses')
q0=abstract.index('\\noindent\\textbf{Structure.')
abstract=abstract[:q0]+'''\\noindent\\textbf{Structure.} System I gives the cod harvest--protection budget;
System II scores the Edwards policy family. Each keeps its source-specific methods and
results. A cross-system conclusion states what certification establishes and the horizon
on which it holds. The companion's exact-rational cod analysis is separately compiled
and cross-cited, rather than inserted as a second document inside this source.
'''
main=main[:a0]+abstract+main[a1:]
once('\\part*{Part I --- The harvest--protection budget at the limit reference point}', '\\part*{System I --- The harvest--protection budget at the limit reference point}')
once('\\addcontentsline{toc}{part}{Part I --- The harvest--protection budget}', '\\addcontentsline{toc}{part}{System I --- The harvest--protection budget}')
once('\\part*{Part III --- Governance operators and viability kernels of the Edwards Aquifer}', '\\part*{System II --- Governance operators and viability kernels of the Edwards Aquifer}')
once('\\addcontentsline{toc}{part}{Part III --- Edwards Aquifer viability kernels}', '\\addcontentsline{toc}{part}{System II --- Edwards Aquifer viability kernels}')
# The conclusion's first and third parts are source content; delete its embedded ARV claim only.
q0=main.index('\\section{Cross-system conclusion}');q1=main.index('\\subsection*{References}',q0)
conclusion=main[q0:q1]
conclusion=conclusion.replace('The three parts above certify', 'The two systems above certify').replace('the three parts\nestablish jointly','the two systems\nestablish jointly').replace('All three parts fix','Both system analyses fix').replace('all three report negative results','both report negative results')
conclusion=conclusion.replace('Part III','The Edwards analysis')
conclusion=re.sub(r'Part I(?!I)', 'The cod analysis', conclusion)
# The original text calls this Part II; remove its whole distinct claim through the next paragraph.
needle=' Part II supplies the same discipline on a harder object:'
assert conclusion.count(needle)==1
left=conclusion.index(needle);right=conclusion.index('\\emph{What it costs:',left)
conclusion=conclusion[:left]+'\n\n'+conclusion[right:]
# Remove the ARV-only sentence about negative interval verdicts.
needle=' Part II likewise reports which steps do \\emph{not} certify rather than\nreporting only the two collapse steps that do.'
assert conclusion.count(needle)==1
conclusion=conclusion.replace(needle,'')
needle='Part II certifies some steps and not others rather than issuing a verdict on the collapse as a whole;\n'
assert conclusion.count(needle)==1
conclusion=conclusion.replace(needle,'')
conclusion=conclusion.replace('In The cod analysis', 'In the cod analysis').replace('In The Edwards analysis','In the Edwards analysis').replace('The cod analysis\'s certified layer','the cod analysis\'s certified layer').replace('each part states','each system analysis states')
conclusion += '''\\noindent The separately compiled Part II companion, \\emph{Regime Viability on the Northern Cod Stock},
uses the same cod study system but asks the distinct exact-rational, non-fitted-model
question of which realized intervals certify a contraction; its arithmetic and scope
are reported there, not silently attributed to the fitted-model analysis above.

'''
main=main[:q0]+conclusion+main[q1:]
# Remove ARV-only declarations while keeping cod/Edwards provenance intact.
for heading in ('\\emph{Applied-regime-viability record.} All inputs', '\\emph{Applied-regime-viability record.} The verification script'):
 assert main.count(heading)==1
 a=main.index(heading);b=main.index('\\emph{Edwards Aquifer.}',a)
 main=main[:a]+main[b:]
assert '\\section{The record spine}\\label{regime-spine}' not in main
assert '\\includegraphics[width=0.96\\linewidth]{figs_arv/fig_record.pdf}' not in main
assert len(re.findall(r'(?m)^\\begin\{document\}',main))==1
assert len(re.findall(r'(?m)^\\end\{document\}',main))==1
# Companion title and reciprocal citation; leave its independent interval-specific record rows.
assert arv.count('\\title{Regime Viability on the Northern Cod Stock:')==1
arv2=arv.replace('\\title{Regime Viability on the Northern Cod Stock:', '\\title{Part II --- Regime Viability on the Northern Cod Stock:',1)
needle='The viability machinery of the obstruction calculus has been developed'
assert arv2.count(needle)>=1
intro='''\\noindent\\textbf{Companion relation.} This Part II accompanies
\\emph{Certification, not simulation: the viability of harvest rules on two real resource systems,
and the horizon of what can be certified} (paper09 main). It shares the Northern cod
study-system record named there but not the main paper's fitted-model method:
the interval-specific inputs, exact-rational arithmetic, and brackets required for
this document's certificates are stated here so that it compiles and verifies independently.

'''
section='\\section{Introduction}\\label{intro}'
assert arv2.count(section)==1
arv2=arv2.replace(section,section+'\n\n'+intro,1)
# The main is called System I, not a separately titled Part I; disambiguate
# this one legacy self-reference without touching other companion studies.
oldref='counterpart on this same record is certified in the companion paper (Part~I).'
assert arv2.count(oldref)==1
arv2=arv2.replace(oldref,'counterpart on this same record is certified in the paper09 main (System I).',1)
# The original, reviewed ARV abstract is intact; only the title and body citation changed.
old_abs=re.search(r'\\begin\{abstract\}.*?\\end\{abstract\}',arv,re.S).group()
assert old_abs in arv2
mainpath=base/'drafts/paper09_cod_certification_v32.tex';mainpath.write_text(main);arv_file.write_text(arv2)
for name,original,final in ((mainpath.name,live,main),(arv_file.name,arv,arv2)):
 diff=''.join(unified_diff(original.splitlines(True),final.splitlines(True),fromfile='papers/'+name if name==mainpath.name else 'claim_alignment/drafts/'+name+' (pre-host)',tofile='claim_alignment/drafts/'+name))
 (base/'diffs'/name.replace('.tex','_host_2026-10-02.diff')).write_text(diff)
print('paper09 main',len(live),'->',len(main),'bytes; extracted ARV',len(embedded),'bytes; companion',len(arv),'->',len(arv2),'bytes')

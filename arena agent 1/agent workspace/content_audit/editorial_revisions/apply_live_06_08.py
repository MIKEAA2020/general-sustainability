#!/usr/bin/env python3
"""New live 06–08 manuscript and attached Markdown versions, narrowly reviewed."""
from pathlib import Path
from difflib import unified_diff
R=Path('/home/user');D=R/'content_audit/editorial_revisions'
def once(s,a,b):
 assert s.count(a)==1,(s.count(a),a[:160]);return s.replace(a,b,1)
def save(old,new,s):
 p=R/'papers'/old;q=R/'papers'/new;assert not q.exists(),q;orig=p.read_text();assert s!=orig;q.write_text(s)
 (D/('editorial_'+new+'.diff')).write_text(''.join(unified_diff(orig.splitlines(True),s.splitlines(True),fromfile=str(p.relative_to(R)),tofile=str(q.relative_to(R)))))
 print(q.name,len(s.splitlines()))
old='paper06_assessment_separation_v67.tex';s=(R/'papers'/old).read_text()
a='Aggregation is a claim, not a presentation: the geometry of the acceptance gap and the typed ledger that forbids closing it'
b='Aggregation is a claim, not a presentation: the geometry of the acceptance gap'
s=once(s,a,b)
s=once(s,r'\part*{Part I --- The assessment separation: a quantifier commutation that fails}'+'\n'+r'\label{part:separation}'+'\n'+r'\addcontentsline{toc}{part}{Part I --- The assessment separation}'+'\n\n','')
s=once(s,'An Obstruction Calculus for Viability under Incomplete Observation}. Manuscript submitted for publication.','An Obstruction Calculus for Viability under Incomplete Observation}. Prior public preprint version (v12), Zenodo, \\url{https://doi.org/10.5281/zenodo.22552616}.')
s=once(s,'How Aggregation Can Conceal Composition: Aggregate Biocapacity and the Identifiability of Modelled Ecological-Capital Drawdown}. Manuscript submitted for publication.','How Aggregation Can Conceal Composition: Aggregate Biocapacity and the Identifiability of Modelled Ecological-Capital Drawdown}. Manuscript; publication status not independently verified here.')
s=once(s,'paper06\\_assessment\\_separation\\_v67\\_supplementary.md','paper06\\_assessment\\_separation\\_v68\\_supplementary.md')
s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
save(old,'paper06_assessment_separation_v68.tex',s)
old='paper06_assessment_separation_v67_supplementary.md';s=(R/'papers'/old).read_text();s=s.replace(a,b);save(old,'paper06_assessment_separation_v68_supplementary.md',s)

def sensitivity(s,prefix):
 start=r'\subsection{3.5 Sensitivity of the crossing: why 6.5 is reported as a band}'
 end=r'\subsection{4 Discussion}'
 anchor=r'\subsubsection{3.5 The selected 42-stock spectral'
 assert all(s.count(q)==1 for q in [start,end,anchor]),prefix
 i=s.index(start);j=s.index(end,i);block=s[i:j];s=s[:i]+s[j:]
 block=once(block,start,r'\subsubsection{3.4.1 Sensitivity of the crossing: why 6.5 is reported as a band}')
 s=once(s,anchor,block+'\n'+anchor)
 # Section 3.5 inside sampled abstract unambiguously describes sensitivity.
 needle='under a one-percent perturbation the instability verdict itself fails in a third of cases (Section 3.5)'
 s=once(s,needle,needle.replace('Section 3.5','Section 3.4.1'))
 return s
old='paper07_sampled_governance_v50.tex';s=(R/'papers'/old).read_text();s=sensitivity(s,'07');s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.');save(old,'paper07_sampled_governance_v51.tex',s)
old='paper08_governance_delay_v46.tex';s=(R/'papers'/old).read_text();s=sensitivity(s,'08')
s=once(s,'(Abaee, 2026, Sampled Governance, Section 3.5)','(Abaee, 2026, Sampled Governance, Section 3.4.1)')
s=once(s,'The full interval-enclosure table (enclosures for both candidates and\nboth gating variants, with the verified root intervals in','The cross-candidate interval-enclosure table is in the main text. Supplementary S1 gives\nthe gated Candidate A derivation and its verified root intervals in')
s=once(s,'a per-statement inventory (each statement of the main article with its status — theorem, conditional statement, numerical result, conjecture, or definition — and its evidence source: displayed proof, interval certificate, re-execution-verified computation, or numerical record) is available from the authors and accompanies the deposited material.', 'the status synopsis of S7 gives the principal evidence tiers; no separate complete per-statement delay inventory is attached here.') if 'a per-statement inventory (each statement' in s else s
# the accurate S7 text lives in the supplement; main text previously said "statement inventory" without listing one
s=once(s,'the statement inventory, the\ndelayed-recruitment registration records', 'the S7 evidence-tier synopsis, the\ndelayed-recruitment registration records')
s=once(s,'paper08\\_governance\\_delay\\_v46\\_supplementary\\_delay.md','paper08\\_governance\\_delay\\_v47\\_supplementary\\_delay.md')
s=once(s,'paper08\\_governance\\_delay\\_v46\\_supplementary\\_governance.md','paper08\\_governance\\_delay\\_v47\\_supplementary\\_governance.md')
# keep original Part I and II abstracts and independent sections intact; bridge their different operators
part=r'\part*{Part II --- The sampled channel: governance delay as a review clock}'
s=once(s,part,'\\noindent\\textbf{Bridge between operators.} Part I varies an institutional response lag \\(\\tau\\) inside a continuous feedback law; Part II varies the review interval \\(T_r\\) of a sample-and-hold map. Their spectral boundaries are not estimates of one shared delay, so each result retains its own model and evidential scope.\n\n'+part)
s=s.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
save(old,'paper08_governance_delay_v47.tex',s)
old='paper08_governance_delay_v46_supplementary_delay.md';s=(R/'papers'/old).read_text()
s=once(s,'The delay $\\tau$ is the institutional review interval.','The delay $\\tau$ is the response/deployment lag in the continuous feedback channel; it is not the sampled review interval $T_r$ of Part II.')
s=once(s,'## S3. The Fold-Certificate Gap\n','## S3. The Fold-Certificate Gap\n\n**Current status (read before the historical component list).** After the S3 assessment was drafted, the rebuilt Krawczyk stages certified the two fold candidates for the finite-dimensional collocation maps. The free-delay enclosure, interval transversality/curvature checks and continuous-DDE lift remain open; no validated continuous-time fold theorem is asserted. The component list below records the pre-rebuild state and is superseded at the discrete level by S12.\n')
s=once(s,'## S7. Statement Inventory','## S7. Evidence-tier synopsis')
s=once(s,'A per-statement inventory (each statement of the main article with its status — theorem, conditional statement, numerical result, conjecture, or definition — and its evidence source: displayed proof, interval certificate, re-execution-verified computation, or numerical record) is available from the authors and accompanies the deposited material.','This section is an evidence-tier synopsis, not a complete per-statement inventory. The latter is not supplied with this supplementary file; individual main-text claims must therefore be checked against their displayed proof or named computational record.')
s=once(s,'*Accompanies: "Governance latency: the delay, the clock, and the stability of periodically reviewed renewable resources."*','*Accompanies: "Governance latency: the delay, the clock, and the stability of periodically reviewed renewable resources" (version 47).*')
save(old,'paper08_governance_delay_v47_supplementary_delay.md',s)
old='paper08_governance_delay_v46_supplementary_governance.md';s=(R/'papers'/old).read_text()
s=once(s,'*Accompanies: "Governance latency: the delay, the clock, and the stability of periodically reviewed renewable resources."*','*Accompanies: "Governance latency: the delay, the clock, and the stability of periodically reviewed renewable resources" (version 47).*')
s=once(s,'### S11.1 One-at-a-time sensitivity battery (§3.4)','### S11.1 One-at-a-time sensitivity battery (§3.4.1)')
save(old,'paper08_governance_delay_v47_supplementary_governance.md',s)

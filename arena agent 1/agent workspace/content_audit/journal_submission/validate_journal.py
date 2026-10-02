#!/usr/bin/env python3
"""Scoped journal-facing structure and support checks (not a theorem proof)."""
from pathlib import Path
import re,json,hashlib,urllib.parse
R=Path('/home/user');P=R/'papers';S=R/'paper 2 family';A=R/'content_audit/journal_submission'
heads={'paper01_obstruction_calculus':65,'paper02_probabilistic_sufficiency':14,'paper03_computational_certification':18,'paper04_minimax_dual_certificates':18,'paper05_exact_belief_computation':18,'paper06_assessment_separation':69,'paper07_sampled_governance':52,'paper08_governance_delay':48,'paper09_cod_certification':34,'paper09b_arv_certification':4,'paper11_forecasting_baselines':66,'paper11c_worked_systems_audit':4}
checks=[]
def chk(label,condition):checks.append((label,bool(condition)))
for stem,v in heads.items():
 p=P/f'{stem}_v{v}.tex';s=p.read_text()
 chk(p.name+' exists / pdf',p.with_suffix('.pdf').exists())
 chk(p.name+' no manuscript source memo comments',not re.search(r'^\s*%',s,re.M))
 chk(p.name+' no change-log phrases',not re.search(r'(?i)(?:earlier|previous) version of this (?:paper|manuscript)|(?:manuscript submitted for publication|alignment draft|pre-rebuild state|reproduced in full from its companion)',s))
s=(P/'paper08_governance_delay_v48.tex').read_text();delay=(P/'paper08_governance_delay_v48_supplementary_delay.md').read_text();sample=(P/'paper08_governance_delay_v48_supplementary_governance.md').read_text()
chk('08 one abstract',s.count(r'\begin{abstract}')==s.count(r'\end{abstract}')==1)
chk('08 two retained part lead-ins',s.count(r'\subsection*{Study scope and principal findings}')==2)
chk('08 one keywords list',s.count('Keywords:')==1)
chk('08 local operator proof separate from continuous fold',all(q in s for q in ['The local spectral comparisons use the characteristic equation and sampled monodromy, not a fold theorem','fold theorem for the continuous delay equation remains open','Krawczyk-enclosed finite-dimensional turning candidate']))
chk('08 no unqualified certified continuous fold',not re.search(r'certified (?:continuous[ -]delay )?fold',s,re.I))
chk('08 delay S7 no nonexistent inventory promise', 'thematic evidence-tier synopsis rather than an exhaustive claim-by-claim table' in delay and 'per-statement inventory' not in delay)
chk('08 supplement exact pointers and sections', all(q in s for q in [r'paper08\_governance\_delay\_v48\_supplementary\_delay.md',r'paper08\_governance\_delay\_v48\_supplementary\_governance.md']) and '## S3.' in delay and '## S7.' in delay and 'S1' in sample)
chk('08 supplement no merge comments',not delay.startswith('<!--') and not sample.startswith('<!--'))
for d in [P,S/'01_obstruction']:
 chk(str(d)+' 01 proof and SI',r'r(S)=S' in (d/'paper01_obstruction_calculus_v65.tex').read_text() and r'[0,2]' in (d/'paper01_obstruction_calculus_v65_supplementary.tex').read_text())
for d in [P,S/'11_forecasting_baselines']:
 x=d/'paper11_forecasting_baselines_v66_SI.md';chk(str(d)+' 11 SI exact content',hashlib.sha256(x.read_bytes()).hexdigest()=='fb3f8bd2e1eb5590c20371a6107fe7a40670eb67c8f92ae73682e26c31a4f122' and (d/'paper11_forecasting_baselines_v66_SI_PROVENANCE.md').is_file())
index=(R/'LATEST_FAMILY_FILES.md').read_text();links=re.findall(r'\]\(([^)]+)\)',index);chk('latest index local file links valid',all((R/urllib.parse.unquote(u)).is_file() for u in links if u.endswith(('.md','.tex','.pdf'))))
comp=json.loads((A/'COMPILE_RESULTS.json').read_text());chk('25/25 compiled without stub figures or undefined references',len(comp)==25 and all(x['status']=='COMPILED' and x['undefined_reference_warnings']==0 for x in comp))
(A/'VALIDATION_RESULTS.json').write_text(json.dumps([{'check':a,'passed':b} for a,b in checks],indent=2))
for name,ok in checks:print('PASS' if ok else 'FAIL',name)
print('TOTAL',sum(ok for _,ok in checks),'/',len(checks))
assert all(ok for _,ok in checks)

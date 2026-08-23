#!/usr/bin/env python3
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
m=list(csv.DictReader((ROOT/'A001_A002_theorem_interface_map.csv').open(encoding='utf-8')))
loc={r['locator_id']:r for r in csv.DictReader((ROOT/'A001_A002_source_proof_locator.csv').open(encoding='utf-8'))}
FIELDS=['map_id','source_id','source_label','theorem_family','retention_tier','paper_destination','selection_reason','formal_source_words','proof_location_status','verification_dependencies']

def decide(r):
 src=r['source_id']; lab=r['source_label']; fam=r['theorem_family'].split()[0]
 if fam=='F14': return 'docket','monograph/conditional docket','conjecture, hypothesis, programme, or open problem'
 if src=='A002':
  if lab=='Remark': return 'bounded_appendix','Paper 2 appendix or omit if redundant','nonformal explanatory remark'
  return 'main','Paper 2','canonical A002 restricted theorem/definition family'
 # A001 selections
 if fam=='F04': return 'main','Paper 2','unique recovery/emergency-envelope family'
 if fam=='F02': return 'main','Paper 2','dimensionally correct CES family complementary to A002 Farkas alternative'
 if fam=='F13':
  keep=['Theorem 2.1','Theorem 2.3','Theorem 2.4','Theorem 5.2']
  if any(k in lab for k in keep): return 'main','Paper 2','nonduplicate foundational proposition or obstruction'
  return 'delegated','Paper 1/monograph','duplicate tangency/definition or architectural framing'
 if fam=='F03':
  keep=['Theorem 4.2','Theorem 4.4','Theorem 4.5','Theorem 4.7','Example 4.1','Theorem 4.8','Theorem 4.9','Proposition 4.1','Theorem 13.1','Theorem 13.2']
  if any(k in lab for k in keep): return 'main','Paper 2','unique obstruction, observer transfer, tangency, or implementation theorem'
  return 'delegated','Paper 1/Paper 5/monograph','duplicate hierarchy/kernel formulation or application framing'
 if fam=='F10':
  if 'Theorem 16.1' in lab: return 'main','Paper 2','restricted composition theorem target'
  if 'Counterexample 10.1' in lab or 'Example 10.1' in lab: return 'bounded_appendix','Paper 2 example section','minimal destruction/rescue motivation'
  return 'delegated','monograph/Paper 3','detailed patch or cascade family not needed for theorem-atlas core'
 if fam=='F11':
  if 'Theorem 13.1' in lab or 'Theorem 13.2' in lab: return 'main','Paper 2','formal implementation equivalence/safety result'
  return 'delegated','Paper 1/monograph','commons games and institutional applications'
 if fam=='F12':
  if 'Theorem 14.2' in lab or 'Theorem 17.1' in lab: return 'bounded_appendix','Paper 2 or Paper 1','selected compactness/small-noise obstruction'
  return 'delegated','Paper 1/monograph','intergenerational interpretation or stochastic docket'
 if fam=='F07': return 'delegated','Paper 4/monograph','model-specific delay or quantitative margin result'
 if fam in {'F08','F09'}: return 'delegated','Paper 3/monograph','resource/application theorem family'
 return 'delegated','manual destination review','not selected into canonical core'
rows=[]
for r in m:
 tier,dest,reason=decide(r); l=loc.get(r['map_id'],{})
 n=int(l.get('statement_words') or 0)+int(l.get('proof_words') or 0)
 rows.append({'map_id':r['map_id'],'source_id':r['source_id'],'source_label':r['source_label'],'theorem_family':r['theorem_family'],
  'retention_tier':tier,'paper_destination':dest,'selection_reason':reason,'formal_source_words':n,
  'proof_location_status':l.get('proof_presence','nonformal_remark'),'verification_dependencies':r['verification_dependencies']})
out=ROOT/'paper2_retained_row_budget.csv'
with out.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
from collections import Counter,defaultdict
cnt=Counter(r['retention_tier'] for r in rows); ww=defaultdict(int)
for r in rows:ww[r['retention_tier']]+=int(r['formal_source_words'])
main=ww['main']; app=ww['bounded_appendix']; overhead=round((main+app)*0.35); total=main+app+overhead
with (ROOT/'paper2_retained_row_budget_report.md').open('w',encoding='utf-8') as f:
 f.write('# Paper 2 Retained-Row Budget After Source Selection\n\n')
 f.write('| Tier | Rows | Located formal source words |\n|---|---:|---:|\n')
 for k in ['main','bounded_appendix','delegated','docket']:f.write(f'| `{k}` | {cnt[k]} | {ww[k]:,} |\n')
 f.write(f'\n- Main plus bounded-appendix formal blocks: **{main+app:,} words**.\n')
 f.write(f'- Planning allowance for introductions, connective definitions, examples, status notes, and reproducibility (35%): **{overhead:,} words**.\n')
 f.write(f'- Preliminary retained-manuscript equivalent: **{total:,} words**, before bibliography and figures.\n\n')
 f.write('## Interpretation\n\n')
 f.write('Source selection reduces the gross 40,582-word intake substantially. The estimate is not a venue decision: source proof blocks are not publication prose, unresolved verification may expand statements, and a target policy has not been selected. A single Paper 2 is feasible only if exact proof audit and rewriting keep the final manuscript within a verified venue limit with revision buffer. Otherwise the pre-authorized coherent 2A/2B split triggers. Delegated rows remain assigned to other papers or the monograph and are not deleted.\n')
print(dict(cnt),dict(ww),'estimated',total)

#!/usr/bin/env python3
"""Compare every new paper09 Table 1 numeric cell to unrounded fit rerun."""
from pathlib import Path
import re,csv
s=Path('/home/user/papers/paper09_cod_certification_v36.tex').read_text()
s=s.split('\\textbf{Table 1.} Lower boundaries',1)[1].split('\\endlastfoot',1)[1].split('\\end{longtable}',1)[0]
records=[]
for chunk in re.split(r'\\\\',s):
 cols=[c.strip() for c in chunk.split('&')]
 if len(cols)!=7:continue
 name=cols[0]
 if name.startswith('BAU'):key='BAU'
 elif name.startswith('flat '):key='flat_'+name.split(' ')[1]
 elif name.startswith('S1 /'):key='flat_60'
 elif name.startswith('Family A'):
  m=re.search(r'=([0-9]+\.[0-9]+)',name);assert m,name;key='A_phi'+str(float(m.group(1)))
 elif name.startswith('Family B'):
  key='graded2' if 'graded2' in name else 'graded3'
 else:raise AssertionError(name)
 v=[]
 for c in cols[1:]:
  q=re.search(r'\d+\.\d+',c);v.append(float(q.group()) if q else None)
 records.append((name,key,v))
assert len(records)==13,len(records)
rerun={(x['floor'],x['policy']):x for x in csv.DictReader(open('/home/user/content_audit/revision_pair_cod_2026-10-02/COD_EXACT_TABLE.csv'))}
comparisons=[]
for name,key,vals in records:
 for j,floor in enumerate(['worst','q05','q10']):
  source=rerun[(floor,key)]
  for col,val in [('T1',vals[2*j]),('Tinf',vals[2*j+1])]:
   computed=None if not source[col] else float(source[col]);good=(val is None and computed is None) or (val is not None and computed is not None and abs(val-computed)<=.051)
   comparisons.append((name,floor,col,val,computed,good))
bad=[x for x in comparisons if not x[-1]]
print('Table1 13 rows, 3 classes, 2 horizons:',len(comparisons),'cells, mismatches',len(bad));print('\n'.join(map(str,bad[:30])))
assert not bad

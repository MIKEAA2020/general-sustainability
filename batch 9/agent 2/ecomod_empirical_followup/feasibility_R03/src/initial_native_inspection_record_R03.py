import re,json
from pathlib import Path
import numpy as np
P=Path('/home/user/.cache/cci_next_R03')
def parse(text):
 data=text.split('---------------------------------------------',1)[1];values={};current=None
 for line in data.splitlines():
  line=line.strip();m=re.match(r'(agb(?:_sd)?)(?:\.\1)?\[',line)
  if m:current=m.group(1);values[current]=[];continue
  if current and line.startswith('['):
   tail=re.sub(r'^(?:\[\d+\])+\s*,?\s*','',line);a=np.fromstring(tail,sep=',',dtype=np.int32);values[current].extend(a.tolist())
 for k in ['agb','agb_sd']:
  if len(values[k])!=65536:raise ValueError('shape')
 return {k:np.asarray(v,dtype=np.int32).reshape(256,256)for k,v in values.items()}
a={y:parse((P/f'BRA_{y}.ascii').read_text())for y in [2015,2023]};out={}
for y,d in a.items():
 g,s=d['agb'],d['agb_sd'];r={'agb_zero':int((g==0).sum()),'sd_zero':int((s==0).sum()),'both_zero':int(((g==0)&(s==0)).sum()),'agb_positive_sd_zero':int(((g>0)&(s==0)).sum()),'agb_zero_sd_positive':int(((g==0)&(s>0)).sum()),'negative_agb':int((g<0).sum()),'negative_sd':int((s<0).sum()),'sd_max':int(s.max())}
 for key,mask in [('all',np.ones(g.shape,dtype=bool)),('positive_agb',g>0),('zero_agb',g==0)]:
  r['sd_quantiles_'+key]=np.quantile(s[mask],[0,.25,.5,.75,1]).tolist()
 print(y,r);out[y]=r
print('joint states',[(i,j,int(((a[2015]['agb']==0)==i).astype(bool).sum()))for i,j in []])
for key in ['agb','agb_sd']:print(key,'identical endpoints',int((a[2015][key]==a[2023][key]).sum()))
(P/'native_initial_summary.json').write_text(json.dumps(out,indent=2)+'\n')

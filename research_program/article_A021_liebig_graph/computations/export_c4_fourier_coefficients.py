#!/usr/bin/env python3
"""Export Newton-solved Fourier coefficients with one-ulp outward float hulls."""
import csv,hashlib,json
from pathlib import Path
import numpy as np
root=Path(__file__).parent
records=[]
for K in [80,120,240]:
 z=np.load(root/f'c4_fourier_K{K}_operator.npz');u=z['u'];P=float(z['period']);n=len(u);c=np.fft.fft(u,axis=0)/n;modes=np.fft.fftfreq(n,d=1/n).astype(int);out=root/f'c4_fourier_coefficients_K{K}.csv'
 with out.open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['K','period','mode','state','real','imag','real_lo_1ulp','real_hi_1ulp','imag_lo_1ulp','imag_hi_1ulp'])
  for mode,row in sorted(zip(modes,c),key=lambda x:x[0]):
   for j,name in enumerate(['N','A','Z','E']):
    re=float(row[j].real);im=float(row[j].imag);w.writerow([K,format(P,'.17g'),int(mode),name,format(re,'.17g'),format(im,'.17g'),format(np.nextafter(re,-np.inf),'.17g'),format(np.nextafter(re,np.inf),'.17g'),format(np.nextafter(im,-np.inf),'.17g'),format(np.nextafter(im,np.inf),'.17g')])
 h=hashlib.sha256(out.read_bytes()).hexdigest();records.append({'K':K,'period':P,'nodes':n,'rows':4*n,'file':str(out.relative_to(root.parent.parent.parent.parent)) if False else out.name,'sha256':h,'size':out.stat().st_size})
(root/'c4_fourier_coefficients_manifest.json').write_text(json.dumps({'format':'Fourier convention u(theta_j)=sum_k a_k exp(2 pi i k j/n); CSV hull is one IEEE-754 ulp around stored coefficient only, not a mathematical orbit enclosure','exports':records},indent=2));print(json.dumps(records,indent=2))

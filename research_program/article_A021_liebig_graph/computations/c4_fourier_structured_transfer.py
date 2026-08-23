#!/usr/bin/env python3
"""Structured low-mode consistency from K=240 to a large fine grid (default K=600).

Applies the fine Jacobian to prolonged coarse modes in batches without forming the
full fine Jacobian, then restricts and preconditions with J_Kc^{-1}.
"""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.linalg import lu_factor,lu_solve
from c4_floquet_discrete import jac
root=Path(__file__).parent
ap=argparse.ArgumentParser();ap.add_argument('--Kc',type=int,default=240);ap.add_argument('--Kf',type=int,default=600);ap.add_argument('--batch',type=int,default=64);a=ap.parse_args();Kc,Kf=a.Kc,a.Kf
zc=np.load(root/f'c4_fourier_K{Kc}_operator.npz');uc=zc['u'];P=float(zc['period']);Jc=zc['J'];nc=2*Kc+1;nf=2*Kf+1;dc=4*nc+1

def interp(nout,nin):
 I=np.eye(nin);C=np.fft.fft(I,axis=0)/nin;kin=np.fft.fftfreq(nin,d=1/nin).astype(int);theta=np.arange(nout)/nout
 return np.real(np.exp(2j*np.pi*np.outer(theta,kin))@C)
def mat_symbol(n,sym):
 I=np.eye(n);return np.fft.ifft(sym[:,None]*np.fft.fft(I,axis=0),axis=0).real
E=interp(nf,nc);R=interp(nc,nf);fc=np.fft.fftfreq(nc,d=1/nc);Dth=mat_symbol(nc,2j*np.pi*fc);sy=np.exp(-2j*np.pi*fc*4.5/P);S=mat_symbol(nc,sy);SP=mat_symbol(nc,sy*(2j*np.pi*fc*4.5/P**2))
uf=E@uc;zdc=S@uc[:,2];zdf=E@zdc;zdpf=E@(SP@uc[:,2]);refdf=E@(Dth@uc)
AA=np.zeros((nf,4,4));BB=np.zeros((nf,4));ff=np.zeros((nf,4))
# local vector field replicated here through exact jac and inferred rhs from saved orbit derivative relation
from c4_cycle_naim import rhs
for i in range(nf):
 A0,B0=jac(uf[i],zdf[i]);AA[i]=A0;BB[i]=B0[:,2];ff[i]=rhs(uf[i],zdf[i])
lift=np.zeros((dc,dc))
for lo in range(0,dc,a.batch):
 hi=min(dc,lo+a.batch);b=hi-lo;Vc=np.zeros((nc,4,b));pv=np.zeros(b)
 for jj,col in enumerate(range(lo,hi)):
  if col<4*nc: Vc[col//4,col%4,jj]=1
  else:pv[jj]=1
 Vf=np.einsum('ij,jkb->ikb',E,Vc);dVc=np.einsum('ij,jkb->ikb',Dth,Vc);dVf=np.einsum('ij,jkb->ikb',E,dVc)
 delc=S@Vc[:,2,:];delf=E@delc
 Y=dVf-P*np.einsum('ijk,ikb->ijb',AA,Vf)-P*BB[:,:,None]*delf[:,None,:]
 Y+=(-ff-P*BB*zdpf[:,None])[:,:,None]*pv[None,None,:]
 Yr=np.einsum('ij,jkb->ikb',R,Y);lift[:4*nc,lo:hi]=Yr.reshape(4*nc,b)
 lift[-1,lo:hi]=np.einsum('ij,ijb->b',refdf/nf,Vf)
D=Jc-lift;lu=lu_factor(Jc);pre=lu_solve(lu,D)
out={'K_coarse':Kc,'K_fine_structured':Kf,'coarse_dimension':dc,'fine_state_dimension':4*nf,'prolongation_inf_norm':float(np.linalg.norm(E,np.inf)),'restriction_inf_norm':float(np.linalg.norm(R,np.inf)),'raw_consistency_inf':float(np.linalg.norm(D,np.inf)),'preconditioned_consistency_inf':float(np.linalg.norm(pre,np.inf)),'status':'structured finite fine-grid transfer; not continuum tail proof'}
(root/f'c4_fourier_structured_transfer_K{Kc}_K{Kf}.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

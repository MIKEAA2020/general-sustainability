"""Rigorous whole-series orbit AND fold-null residual upper bounds.
Interval FFT + analytic-strip alias/tail estimates. This is not an existence
or inverse/contraction certificate. Exact decimal polynomial inputs are saved.
"""
from pathlib import Path
import json,time
import numpy as np
from mpmath import iv,mp
from fold_continuum_stage_v43 import analytic_tails
from interval_decimal_v42 import outward_bounds
ROOT=Path(__file__).resolve().parents[1]
def fft(a,inverse=False):
    n=len(a);out=list(a);j=0
    for i in range(1,n):
        bit=n>>1
        while j&bit:j^=bit;bit>>=1
        j^=bit
        if i<j:out[i],out[j]=out[j],out[i]
    length=2;sgn=1 if inverse else -1
    while length<=n:
        half=length//2;roots=[iv.exp(iv.mpc(0,sgn*2)*iv.pi*k/length)for k in range(half)]
        for start in range(0,n,length):
            for k in range(half):
                u=out[start+k];v=roots[k]*out[start+k+half];out[start+k]=u+v;out[start+k+half]=u-v
        length*=2
    if inverse:out=[x/n for x in out]
    return out

def polynomial_coeff(x):
    c=np.fft.fft(x,axis=0)/len(x);m=len(x)//2;result=[]
    for j in range(3):result.append({'a0':str(float(c[0,j].real)),'a':[str(float(2*c[k,j].real))for k in range(1,m+1)],'b':[str(float(-2*c[k,j].imag))for k in range(1,m+1)]})
    return result

def padded(c,n):
    out=[iv.mpc(0)for _ in range(n)];out[0]=iv.mpc(iv.mpf(c['a0']))
    for k,(a,b)in enumerate(zip(c['a'],c['b']),1):out[k]=iv.mpc(iv.mpf(a),-iv.mpf(b))/2;out[-k]=iv.mpc(iv.mpf(a),iv.mpf(b))/2
    return out

def run(nfft=4096):
    mp.dps=80;iv.dps=65;fixed=json.loads((ROOT/'data/fold_exact_fourier_inputs_v43.json').read_text())['records'];archive=np.load(ROOT/'data/fold_odd_grid_seeds_v43.npz');records=[]
    for name in ['lower','upper']:
        start=time.time();w=archive[name+'_257_w'];v=archive[name+'_257_v'];tau=next(r['tau']for r in json.loads((ROOT/'data/fold_continuum_stage_v43.json').read_text())['records']if r['fold']==name and r['nodes']==257)
        input=fixed[name];tails=analytic_tails(w,v,tau,exact_coefficients=input);strip=tails['accepted_strips'][-1];iv.dps=65;T=iv.mpf(input['period_decimal']);rho=iv.mpf(input['null_period_decimal']);tt=iv.mpf(input['tau_decimal']);phi=tt/T;CU=input['polynomial_U_exact_decimal_coefficients'];CV=input['polynomial_V_exact_decimal_coefficients'];cu=[padded(c,nfft)for c in CU];cv=[padded(c,nfft)for c in CV];freq=[k if k<nfft//2 else k-nfft for k in range(nfft)];shift=[iv.exp(iv.mpc(0,-2)*iv.pi*k*phi)for k in freq]
        print(name,'interval polynomial evaluation',flush=True)
        U=[fft(c,True)for c in cu];V=[fft(c,True)for c in cv];U=[[x*nfft for x in a]for a in U];V=[[x*nfft for x in a]for a in V]
        zd=[x*nfft for x in fft([x*s for x,s in zip(cu[1],shift)],True)];vd=[x*nfft for x in fft([x*s for x,s in zip(cv[1],shift)],True)];zder=[x*nfft for x in fft([x*s*iv.mpc(0,2)*iv.pi*k for x,s,k in zip(cu[1],shift,freq)],True)]
        frows=[[],[],[]];hrows=[[],[],[]];one=iv.mpf(1);r=iv.mpf('.02');q=iv.mpf('.001');eta=iv.mpf('.914');d0=iv.mpf('.01')
        for i in range(nfft):
            nn,zz,ee=U[0][i],U[1][i],U[2][i];vn,vz,ve=V[0][i],V[1][i],V[2][i];z=zd[i];D=q*ee*nn-r*nn+r*nn*nn/100;ex=iv.exp(10*D);sig=ex/(1+ex);f1=-D;f2=(iv.log(1+ex)/10-zz)/5;B=eta*ee*(z-ee/30)+d0*z/(1+z);g=1-ee/30;f3=g*B;AN=r-2*r*nn/100-q*ee;AE=-q*nn;BN=sig*(-AN)/5;BE=sig*(-AE)/5;CE=-B/30+g*eta*(z-2*ee/30);CZ=g*(eta*ee+d0/(1+z)**2)
            fs=[f1,f2,f3];js=[AN*vn+AE*ve,BN*vn-vz/5+BE*ve,CE*ve+CZ*vd[i]]
            for j in range(3):frows[j].append(fs[j]);hrows[j].append(T*js[j]+rho*fs[j]+(phi*rho*CZ*zder[i]if j==2 else 0))
        print(name,'interval Fourier integration',flush=True)
        fc=[[x/nfft for x in fft(a)]for a in frows];hc=[[x/nfft for x in fft(a)]for a in hrows];alpha=iv.mpf(strip['strip_half_width']);aa=2*iv.pi*alpha;nu=iv.mpf('1.001');Mf=[iv.mpf(x[1])for x in strip['complex_rhs_bounds']];Mh=[iv.mpf(x[1])for x in strip['complex_null_rhs_bounds']];rs=[iv.mpf(0)for _ in range(3)];ns=[iv.mpf(0)for _ in range(3)];K=nfft//2-1
        for k in range(-K,K+1):
            ix=k%nfft;weight=nu**abs(k);alias_factor=2*iv.exp(-aa*(nfft-abs(k)))/(1-iv.exp(-aa*nfft))
            for j in range(3):
                rr=iv.mpc(0,2)*iv.pi*k*cu[j][ix]-T*fc[j][ix];vv=iv.mpc(0,2)*iv.pi*k*cv[j][ix]-hc[j][ix];rs[j]+=(abs(rr)+T*Mf[j]*alias_factor)*weight;ns[j]+=(abs(vv)+Mh[j]*alias_factor)*weight
        factor=2*(nu*iv.exp(-aa))**(K+1)/(1-nu*iv.exp(-aa))
        upper=lambda x:outward_bounds(x)[1]
        for j in range(3):rs[j]+=T*Mf[j]*factor;ns[j]+=Mh[j]*factor
        phase=abs(iv.mpf(CU[0]['b'][0]))/2;nullphase=abs(iv.mpf(CV[0]['b'][0]))/2
        rec={'fold':name,'tau_decimal':input['tau_decimal'],'period_decimal':input['period_decimal'],'null_period_decimal':input['null_period_decimal'],'nfft':nfft,'nu':'1.001','analytic_strip_half_width':strip['strip_half_width'],'residual_weighted_l1_component_upper_bounds':[upper(x)for x in rs],'null_residual_weighted_l1_component_upper_bounds':[upper(x)for x in ns],'phase_residual_upper_bound':upper(phase),'null_phase_residual_upper_bound':upper(nullphase),'normalisation':'fix a nonzero N-cosine coefficient of V to its exact baseline value; residual zero by definition of the fixed normalization constant','polynomial_U_exact_decimal_coefficients':CU,'polynomial_V_exact_decimal_coefficients':CV,'seconds':time.time()-start}
        records.append(rec);print(name,'certified full residual upper bounds',rec['residual_weighted_l1_component_upper_bounds'],rec['null_residual_weighted_l1_component_upper_bounds'],flush=True)
        result={'status':'Rigorous full infinite-Fourier orbit/kernel residual bounds for two exact approximate fold polynomials; NOT a continuum fold existence certificate','method':'Outward interval radix-2 FFT with analytic-strip trapezoidal alias and infinite-tail bounds; all coefficients and parameters are explicit exact decimal inputs','arithmetic':'mpmath.iv 65 decimal digits (strip proof 70 digits)','missing':['validated inverse of the full bordered infinite-dimensional fold operator','finite-tail coupling and nonlinear contraction/radii inequalities','continuum fold nondegeneracy and simple periodic Floquet multiplier'],'records':records};(ROOT/'data/interval_fourier_residual_v43.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
if __name__=='__main__':run()

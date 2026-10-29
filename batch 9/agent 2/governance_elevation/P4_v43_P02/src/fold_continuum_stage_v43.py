"""Odd-grid augmented folds and rigorous infinite Fourier-tail bounds.
This stage does not assert an inverse bound or a continuum fold certificate.
"""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.signal import resample
from mpmath import mp,iv
import fold_pipeline_v43 as p
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'inherited_v42/src'))
from interval_decimal_v42 import outward_bounds

def offgrid(w,v,tau,count=8193):
    n=(len(w)-1)//3;Y=w[:-1].reshape(n,3);V=v[:-1].reshape(n,3);T=w[-1];rho=v[-1];k=np.fft.fftfreq(n,d=1/n);cy=np.fft.fft(Y,axis=0)/n;cv=np.fft.fft(V,axis=0)/n;t=np.arange(count)/count;basis=np.exp(2j*np.pi*np.outer(t,k));U=(basis@cy).real;Udot=(basis@((2j*np.pi*k)[:,None]*cy)).real;VV=(basis@cv).real;Vdot=(basis@((2j*np.pi*k)[:,None]*cv)).real;phase=np.exp(-2j*np.pi*k*tau/T);zd=(basis@(cy[:,1]*phase)).real;vd=(basis@(cv[:,1]*phase)).real;zdot=(basis@(2j*np.pi*k*cy[:,1]*phase)).real
    F=np.array([p.rhs(u,z)for u,z in zip(U,zd)]);J=np.empty_like(F)
    for i,(u,z)in enumerate(zip(U,zd)):
        A,B=p.rhs_jac(u,z);J[i]=A@VV[i]+B*vd[i]
    res=Udot-T*F;null=Vdot-T*J-rho*F-(tau/T)*rho*np.array([p.rhs_jac(u,z)[1]for u,z in zip(U,zd)])*zdot[:,None]
    return {'physical_orbit_defect':np.max(abs(res/T),axis=0).tolist(),'phase_null_defect':np.max(abs(null),axis=0).tolist(),'period':float(T),'stock_min':float(U[:,0].min()),'stock_max':float(U[:,0].max())}

def analytic_tails(w,v,tau,exact_coefficients=None):
    mp.dps=80;iv.dps=70;n=(len(w)-1)//3;m=n//2;T=iv.mpf(str(w[-1]));rho=iv.mpf(str(abs(v[-1])));phi=iv.mpf(str(tau))/T
    def coeff(a):
        c=np.fft.fft(a.reshape(n,3),axis=0)/n
        return [[iv.mpf(str(float(c[0,j].real)))]+[(iv.mpf(str(float(2*c[k,j].real))),iv.mpf(str(float(-2*c[k,j].imag))))for k in range(1,m+1)]for j in range(3)]
    C=coeff(w[:-1]);V=coeff(v[:-1])
    if exact_coefficients is not None:
        def explicit(cs):return [[iv.mpf(c['a0'])]+[(iv.mpf(a),iv.mpf(b))for a,b in zip(c['a'],c['b'])]for c in cs]
        C=explicit(exact_coefficients['polynomial_U_exact_decimal_coefficients']);V=explicit(exact_coefficients['polynomial_V_exact_decimal_coefficients']);T=iv.mpf(exact_coefficients['period_decimal']);rho=abs(iv.mpf(exact_coefficients['null_period_decimal']));phi=iv.mpf(exact_coefficients['tau_decimal'])/T
    c0=[float(x[0].mid)for x in C]
    def hi(x):return mp.mpf(x._mpi_[1])
    def lo(x):return mp.mpf(x._mpi_[0])
    def bounds(C,alpha):
        out=[];imag=[];der=[];osc=[]
        for cc in C:
            A=abs(cc[0]);I=iv.mpf(0);D=iv.mpf(0);O=iv.mpf(0)
            for k,(a,b)in enumerate(cc[1:],1):
                amp=abs(a)+abs(b);ch=(iv.exp(2*iv.pi*k*alpha)+iv.exp(-2*iv.pi*k*alpha))/2;sh=(iv.exp(2*iv.pi*k*alpha)-iv.exp(-2*iv.pi*k*alpha))/2;A+=amp*ch;I+=amp*sh;D+=2*iv.pi*k*amp*ch;O+=amp*ch
            out.append(A);imag.append(I);der.append(D);osc.append(O)
        return out,imag,der,osc
    accepted=[]
    for width in ['.001','.002','.004','.006','.008','.010','.012','.016','.020','.024','.032']:
        alpha=iv.mpf(width);A,I,DU,O=bounds(C,alpha);AV,_,_,_=bounds(V,alpha);nn,zz,ee=A;ni,zi,ei=I;den=1+C[1][0]-O[1];dim=iv.mpf('.001')*(ee*ni+nn*ei)+iv.mpf('.02')*ni+iv.mpf('.0004')*nn*ni
        if lo(den)<=0 or hi(10*dim)>=lo(iv.pi/2):continue
        D=iv.mpf('.001')*nn*ee+iv.mpf('.02')*nn+iv.mpf('.0002')*nn*nn;soft=iv.log(1+iv.exp(10*D))/10+iv.pi/20;gate=1+ee/30;B=iv.mpf('.914')*ee*(zz+ee/30)+iv.mpf('.01')*zz/den;MF=[D,(soft+zz)/5,gate*B]
        AN=iv.mpf('.02')+iv.mpf('.0004')*nn+iv.mpf('.001')*ee;AE=iv.mpf('.001')*nn;CE=B/30+gate*iv.mpf('.914')*(zz+2*ee/30);CZ=gate*(iv.mpf('.914')*ee+iv.mpf('.01')/den**2);AZ=iv.mpf('.2');BN=AN/5;BE=AE/5
        MJ=[AN*AV[0]+AE*AV[2],BN*AV[0]+AZ*AV[1]+BE*AV[2],CE*AV[2]+CZ*AV[1]];nullM=[T*MJ[j]+rho*MF[j]+(phi*rho*CZ*DU[1]if j==2 else 0)for j in range(3)]
        nu=iv.mpf('1.001');ratio=nu*iv.exp(-2*iv.pi*alpha);tail=[]
        for cut in [m,128,256,512,1024]:
            if cut<m:continue
            factor=2*ratio**(cut+1)/(1-ratio);tail.append({'cutoff':cut,'orbit_phase_residual_tail':[outward_bounds(T*x*factor)for x in MF],'null_residual_tail':[outward_bounds(x*factor)for x in nullM]})
        accepted.append({'strip_half_width':width,'softplus_imaginary_argument_bound':outward_bounds(10*dim),'rational_denominator_real_lower_bound':outward_bounds(den),'nu':'1.001','complex_rhs_bounds':[outward_bounds(x)for x in MF],'complex_null_rhs_bounds':[outward_bounds(x)for x in nullM],'tails':tail})
    if not accepted:raise ValueError('No certified analytic strip')
    return {'object':'Exact real trigonometric polynomials defined by the saved IEEE coefficient decimals; not an enclosed true orbit','coefficient_definition':'a0=Re FFT_0/n; a_k=2Re FFT_k/n; b_k=-2Im FFT_k/n, with exact real cos/sin coefficients','arithmetic':'mpmath.iv, 70 decimal digits; no empirical FFT-tail extrapolation','accepted_strips':accepted,'missing_for_continuum_fold':['validated bordered Jacobian/inverse assembly for the enlarged Fourier block','rigorous inverse/resolvent and finite-tail coupling bounds for the full bordered fold operator','contraction and continuum transversality/curvature inclusions']}

def run():
    records=[];archive={}
    for name,seedkey in [('lower','z'),('upper','z_m128')]:
        seed=ROOT/'inherited'/('lower_fold_seed_m128_v43.npz'if name=='lower'else'upper_fold_seeds_v43.npz');z=np.load(seed)[seedkey];w=z[:385];tau=z[385]
        for nodes in [65,129,257]:
            t0=time.time();Y=resample(w[:-1].reshape(-1,3),nodes,axis=0);w0=np.r_[Y.ravel(),w[-1]];p.configure(nodes);zz,ell,err=p.moore_spence(w0,tau,tol=3e-9,maxit=12,verbose=True);dim=3*nodes+1;w=zz[:dim];tau=zz[dim];v=zz[dim+1:];v=v/max(abs(v[:-1].reshape(nodes,3)[:,0]));diag=offgrid(w,v,tau);row={'fold':name,'nodes':nodes,'tau':float(tau),'augmented_residual':err,'seconds':time.time()-t0,**diag};records.append(row);archive[f'{name}_{nodes}_w']=w;archive[f'{name}_{nodes}_v']=v
            print(json.dumps(row),flush=True)
            if err>1e-6:raise ValueError('Odd-grid fold solve did not converge')
            if nodes==257:row['analytic_tails']=analytic_tails(w,v,tau)
            (ROOT/'data/fold_continuum_stage_v43.json').write_text(json.dumps({'certification':'Nominal odd-grid augmented fold solves plus interval analytic-strip/nonlinear-tail bounds; NOT a full continuum fold certificate','records':records},indent=2)+'\n');np.savez_compressed(ROOT/'data/fold_odd_grid_seeds_v43.npz',**archive)
    return records
if __name__=='__main__':run()

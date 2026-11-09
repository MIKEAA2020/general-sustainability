"""One-stock comparator, exact positive part, stage-consistent RK4 method of steps.
B uses CURRENT G(A); only stock regeneration and carrying-capacity INPUTS are
delayed. Constant no-wave prehistory. Floor enforced after each complete RK4 step.
No empirical measurements and no transfer of comparator results to two-land model.
"""
from pathlib import Path
import csv,json,math
import numpy as np
from numba import njit
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]
@njit
def G(A,rho,Amax):return rho*A*(1-A/Amax)
@njit
def Bval(t,A,D,p):
    rho,Amax,b0,bg,e,r,eta,alpha,db,kappa,tw,tg,tp,Kmin,Efixed=p
    tb=db/(1+math.exp(-kappa*(t-tw)))
    return (b0+tb)*math.exp(-alpha*D)*A+bg*G(A,rho,Amax)
@njit
def past(a,col,time,dt,h):
    if time<=0:return h
    x=time/dt;j=int(math.floor(x+1e-10));f=x-j
    if abs(f)<1e-9:f=0.
    return a[j,col] if f==0 else a[j,col]*(1-f)+a[j+1,col]*f
@njit
def rhs(t,y,a,dt,p,A0,B0):
    rho,Amax,b0,bg,e,r,eta,alpha,db,kappa,tw,tg,tp,Kmin,Efixed=p
    A,P,D=y;B=Bval(t,A,D,p)
    bf=(b0+db/(1+math.exp(-kappa*(t-tw))))*math.exp(-alpha*D)
    E=e*P if Efixed<0 else Efixed
    Ap=past(a,0,t-tg,dt,A0) if tg>0 else A
    Bp=past(a,3,t-tp,dt,B0) if tp>0 else B
    return np.array([G(Ap,rho,Amax)-max(E-bf*A,0.)/bg,
        r*P*(1-P/max(Bp/e,Kmin)),max(E-B,0.)-eta*D])
@njit
def run(p,T,dt,A0=1.,P0=.1):
    n=round(T/dt);a=np.zeros((n+1,4));a[0,0]=A0;a[0,1]=P0;a[0,3]=Bval(0.,A0,0.,p)
    B0=p[2]*A0+p[3]*G(A0,p[0],p[1])
    for i in range(n):
        t=i*dt;y=a[i,:3]
        k1=rhs(t,y,a,dt,p,A0,B0);k2=rhs(t+dt/2,y+dt/2*k1,a,dt,p,A0,B0)
        k3=rhs(t+dt/2,y+dt/2*k2,a,dt,p,A0,B0);k4=rhs(t+dt,y+dt*k3,a,dt,p,A0,B0)
        z=y+dt/6*(k1+2*k2+2*k3+k4)
        a[i+1,0]=max(z[0],.02);a[i+1,1]=max(z[1],0.);a[i+1,2]=max(z[2],0.)
        a[i+1,3]=Bval(t+dt,a[i+1,0],a[i+1,2],p)
    return a

def pars(full=False,tg=0.,tp=0.,fixed=-1.):
    # rho,Amax,b0,bG,e,r,eta,alpha,db,kappa,tw,tg,tp,Kmin,Efixed
    if full:return np.array([.08,1.2,.5,.6,.55,.02,.03,.2,.5,.04,120.,15.,25.,1e-4,-1.])
    return np.array([.05,1.2,.5,.8,.55,.02,.05 if fixed>=0 else 0.,.03 if fixed>=0 else 0.,1.5 if fixed>=0 else 0.,.2,15.,tg,tp,1e-6,fixed])
def savecsv(name,rows):
    with(R/'data'/(name+'_C18_A01.csv')).open('w',newline='')as f:
        w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)));w.writeheader();w.writerows(rows)
def export(name,a,dt,stride=1):
    savecsv(name,[dict(t_yr=i*dt,A=row[0],P=row[1],D=row[2],B=row[3]) for i,row in enumerate(a) if i%stride==0])
def plotfull(a,dt):
    t=np.arange(len(a))*dt;fig,ax=plt.subplots(2,1,figsize=(9,5.6),sharex=True,layout='constrained')
    for j,label,c in [(0,'A (stock units)','#246588'),(1,'P (cap)','#b45438'),(3,'B (gha)','#4f8058')]:ax[0].plot(t,a[:,j],label=label,color=c)
    ax[0].axhline(.02,color='gray',ls=':');ax[0].set_ylabel('Value (units differ)');ax[0].legend(frameon=False)
    ax[1].plot(t,a[:,2],color='#766092');ax[1].set(xlabel='Time (yr)',ylabel='D (gha yr)')
    for p in ax:p.grid(alpha=.2)
    fig.savefig(R/'figures/si_onestock_full_trajectory_C18_A01.pdf');plt.close(fig)
def maskwindow(a,dt):
    good=(np.diff(a[:,3])>1e-9)&(np.diff(a[:,0])<-1e-9);best=(0,0);i=0
    while i<len(good):
        if good[i]:
            j=i
            while j<len(good) and good[j]:j+=1
            if j-i>best[1]-best[0]:best=(i,j)
            i=j
        i+=1
    i,j=best
    return dict(start_yr=i*dt,end_yr=j*dt,width_yr=(j-i)*dt,A_start=a[i,0],A_end=a[j,0],B_start=a[i,3],B_end=a[j,3])
def main():
    plt.rcParams.update({"font.size":12})
    refinements=[];fullbase=None
    for dt in [.1,.05,.025]:
        a=run(pars(full=True),900.,dt,P0=.45);contact=np.flatnonzero(a[:,0]<=.02000001)
        refinements.append(dict(case='full',dt_yr=dt,first_floor_time_yr=float(contact[0]*dt) if len(contact) else None,final_A=a[-1,0],peak_D=a[:,2].max(),minimum_A=a[:,0].min()))
        if dt==.1:fullbase=a.copy();export('comparator_full_trajectory',a,dt);plotfull(a,dt)
        else:refinements[-1]['max_A_difference_vs_dt_point1']=float(np.max(np.abs(a[::round(.1/dt),0]-fullbase[:,0])))
    a=run(pars(fixed=.6),250.,.01);export('comparator_fixed_mask',a,.01,10);window=maskwindow(a,.01)
    sweep=[]
    for E in np.round(np.arange(.5,.651,.005),3):
        z=run(pars(fixed=E),250.,.02);win=maskwindow(z,.02)
        sweep.append(dict(Efixed_gha=E,initial_conversion_gap=max(E-(.5+1.5/(1+math.exp(3)))*1.,0.),width_yr=win['width_yr']))
    savecsv('comparator_mask_shortfall_sweep',sweep)
    fig,ax=plt.subplots(1,2,figsize=(9.2,4.2),layout='constrained');t=np.arange(len(a))*.01
    ax[0].plot(t,a[:,0],label='A (stock units)');ax[0].plot(t,a[:,3],label='B (gha)');ax[0].axvspan(window['start_yr'],window['end_yr'],alpha=.2,color='#ad7b28');ax[0].set(xlim=(0,40),xlabel='Time (yr)',ylabel='Value (units differ)',title='(a) Fixed-demand masking');ax[0].legend(frameon=False)
    ax[1].plot([z['initial_conversion_gap'] for z in sweep],[z['width_yr'] for z in sweep]);ax[1].set(xlabel='Initial fast-output gap (gha)',ylabel='Mask duration (yr)',title='(b) Shortfall sweep')
    fig.savefig(R/'figures/si_onestock_mask_window_C18_A01.pdf');plt.close(fig)
    pair=[];fig,ax=plt.subplots(1,2,figsize=(9.2,4.2),layout='constrained')
    for j,tg in enumerate([10.,30.]):
        for dt in [.2,.1]:
            b=run(pars(tg=tg,tp=25.),2000.,dt)
            pair.append(dict(taug_yr=tg,dt_yr=dt,final_A=b[-1,0],final_P=b[-1,1],minimum_A=b[:,0].min()))
            if dt==.2:
                export('comparator_delay_'+str(int(tg)),b,dt,5);t=np.arange(len(b))*dt
                for c,label in [(0,'A (stock units)'),(1,'P (cap)'),(3,'B (gha)')]:ax[j].plot(t,b[:,c],label=label)
                ax[j].set(title=f'τg = {tg:g} yr; τp = 25 yr',xlabel='Time (yr)',ylabel='Value (units differ)');ax[j].legend(fontsize=11,frameon=False)
    fig.savefig(R/'figures/si_onestock_delay_examples_C18_A01.pdf');plt.close(fig)
    savecsv('comparator_delay_refinement',pair)
    cells=[];fig,ax=plt.subplots(1,2,figsize=(9.2,4.4),layout='constrained')
    aa=np.round(np.arange(.1,1.301,.1),2);pp=np.round(np.arange(.05,1.551,.1),2)
    counts=[]
    from matplotlib.colors import ListedColormap
    from matplotlib.patches import Patch
    for k,tg in enumerate([0.,30.]):
        image=np.zeros((len(aa),len(pp)),int);counter={0:0,1:0,2:0}
        for i,A0 in enumerate(aa):
            for j,P0 in enumerate(pp):
                b=run(pars(tg=tg,tp=25.),1200.,.5,A0,P0);v=b[-1,0];c=1 if v>=.95*1.2 else 0 if v<=.05 else 2
                image[i,j]=c;counter[c]+=1;cells.append(dict(taug_yr=tg,A0=A0,P0=P0,final_A=v,final_P=b[-1,1],classification=['low','high','intermediate'][c]))
        counts.append(dict(taug_yr=tg,low=counter[0],high=counter[1],intermediate=counter[2],total=len(aa)*len(pp)))
        ax[k].imshow(image,origin='lower',aspect='auto',extent=[0,1.6,.05,1.35],cmap=ListedColormap(['#b45438','#4f8058','#c1c0c6']),vmin=0,vmax=2);ax[k].set(xlabel='Initial P (cap)',ylabel='Initial A (stock units)',title=f'τg = {tg:g} yr; τp = 25 yr')
    fig.legend(handles=[Patch(color=c,label=l)for c,l in [('#4f8058','High endpoint'),('#b45438','Low endpoint'),('#c1c0c6','Intermediate')]],loc='outside lower center',ncol=3,frameon=False)
    fig.savefig(R/'figures/si_onestock_basin_C18_A01.pdf');plt.close(fig);savecsv('comparator_basin_cells',cells)
    # Analytic characteristic residual, not a search-based assertion of complete spectrum.
    astar=.8;a1=.05*(1-2*astar/1.2);a3=.5/.8;aE=-.55/.8;a4=.02*(.5+.8*a1)/.55
    def char(s,tg,tp):return (s-a1*math.exp(-s*tg)-a3)*(s+.02)-aE*a4*math.exp(-s*tp)
    roots=[]
    for tg,tp in [(0.,0.),(30.,25.)]:
        x=brentq(lambda x:char(x,tg,tp),.1,1.);roots.append(dict(taug=tg,taup=tp,neutral_residual=char(0,tg,tp),positive_real_root=x,positive_root_residual=char(x,tg,tp)))
    savecsv('comparator_roots',roots);savecsv('comparator_full_refinement',refinements)
    summary=dict(full_refinement=refinements,mask=window,delay_pairs=pair,basin_counts=counts,roots=roots,
        scheme='Classical RK4, delayed queries at each substage, linear interpolation; positive parts exact; post-step lower projection.',
        B_readout='Current G(A), not delayed G. Stage carrying capacity uses current B for zero delay.')
    (R/'data/comparator_summary_C18_A01.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()

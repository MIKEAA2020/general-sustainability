"""Secondary common-support ecological and recursive sampled-surrogate tests.
Exploratory protocol amendment is disclosed; no continuous-DDE fit is asserted.
"""
from pathlib import Path
import json
import numpy as np,pandas as pd
from scipy.optimize import least_squares,nnls
from field_response_test_v43 import flow,arrays,metrics
ROOT=Path(__file__).resolve().parents[1]
def stock_flow(N,U,p,R=None):
    r,b,h=p[:3];a=r-h*U
    if R is None:
        phi=np.where(abs(a)>1e-7,np.expm1(a)/np.where(abs(a)>1e-7,a,1),1+a/2+a*a/6);return N*np.exp(a)/(1+b*N*phi)
    c=p[3]*R;d=np.sqrt(a*a+4*b*c);rp=np.where(a<0,2*c/np.maximum(d-a,1e-300),(a+d)/(2*b));rm=np.where(a>=0,-2*c/np.maximum(d+a,1e-300),(a-d)/(2*b));ratio=(N-rp)/(N-rm)*np.exp(-d);return(rp-ratio*rm)/(1-ratio)
def fit(a,recruit=False):
    N,U,R,target=a[:,2],a[:,3],a[:,4],a[:,5];X=np.column_stack([N,-N*N,-U*N]+([R]if recruit else[]));init=nnls(X,target-N)[0];init=np.clip(init,1e-5,10)
    f=lambda p:stock_flow(N,U,p,R if recruit else None)-target
    opt=least_squares(f,init,bounds=(np.full(len(init),1e-8),np.full(len(init),20.)),max_nfev=300);return opt.x,float(np.sqrt(np.mean(f(opt.x)**2))),bool(opt.success)
def run():
    data=json.loads((ROOT/'data/field_response_test_v43.json').read_text());df=pd.read_csv(ROOT/'data/herring_assessment_clean_v43.csv');Bscale=data['reference_scales']['biomass_training_median'];Cscale=data['reference_scales']['catch_training_median'];N=df.TBiomass.to_numpy()/Bscale;U=(df.Catches.to_numpy()/Cscale)/N;yr=df.Year.to_numpy(int);Rraw=df.Recruitment.to_numpy();R=Rraw/np.nanmedian(Rraw[(yr>=1960)&(yr<=1994)]);out={};predrows=[];best=None
    for g in [0,1,2,3]:
        a=np.array([[yr[i],yr[i+1],N[i],U[i],R[i-g]if g else 0,N[i+1]]for i in range(3,len(yr)-1)if yr[i+1]<=2024 and np.isfinite(U[i])]);a=a[np.isfinite(a).all(axis=1)];train=a[(a[:,1]>=1960)&(a[:,1]<=1994)];val=a[(a[:,1]>=1995)&(a[:,1]<=2009)];p,loss,ok=fit(train,bool(g));vl=metrics(val[:,5],stock_flow(val[:,2],val[:,3],p,val[:,4]if g else None))['RMSE'];label='logistic'if not g else'recruitment_lag'+str(g)
        out[label]={'validation_RMSE':vl,'training_RMSE':loss,'parameters':p.tolist(),'fit_success':ok}
        if g and(best is None or vl<out[best]['validation_RMSE']):best=label
    final={}
    for label,g in [('logistic',0),(best,int(best[-1]))]:
        a=np.array([[yr[i],yr[i+1],N[i],U[i],R[i-g]if g else 0,N[i+1]]for i in range(3,len(yr)-1)if yr[i+1]<=2024 and np.isfinite(U[i])]);a=a[np.isfinite(a).all(axis=1)];pre=a[(a[:,1]>=1960)&(a[:,1]<=2009)];test=a[(a[:,1]>=2010)&(a[:,1]<=2024)];p,loss,ok=fit(pre,bool(g));pred=stock_flow(test[:,2],test[:,3],p,test[:,4]if g else None);ar=np.linalg.lstsq(np.column_stack([np.ones(len(pre)),pre[:,2]]),pre[:,5],rcond=None)[0];arp=ar[0]+ar[1]*test[:,2];m=metrics(test[:,5],pred);m.update(parameters=p.tolist(),n_pretest=len(pre),n_test=len(test),RMSE_ratio_to_persistence=m['RMSE']/metrics(test[:,5],test[:,2])['RMSE'],RMSE_ratio_to_AR1=m['RMSE']/metrics(test[:,5],arp)['RMSE'],fit_success=ok,near_parameter_bound=bool(min(p)<1e-6 or max(p)>19.9));final[label]=m
        if not g:basepars=p
        for row,pp,ap in zip(test,pred,arp):predrows.append({'model':label,'target_year':int(row[1]),'observed_N':row[5],'predicted_N':pp,'persistence':row[2],'AR1':ap})
    # A free recursive annual surrogate. After 2009 no observed N, C or R enters.
    recurs={};rows=[];index={int(y):i for i,y in enumerate(yr)};i0=index[2009];trueN=N[[index[y]for y in range(2010,2025)]];trueU=U[[index[y]for y in range(2010,2025)]];preix=[i for i in range(len(yr)-1)if 1960<=yr[i+1]<=2009];X=np.column_stack([np.ones(len(preix)),N[preix],U[preix]]);Y=np.column_stack([N[np.array(preix)+1],U[np.array(preix)+1]]);VAR=np.linalg.lstsq(X,Y,rcond=None)[0];xy=np.array([N[i0],U[i0]]);var=[]
    for _ in range(15):xy=np.r_[1,xy]@VAR;var.append(xy.copy())
    var=np.array(var)
    for label,hyper in data['selected_hyperparameters'].items():
        f=data['scenarios']['TBiomass'][label];pars=f['parameters'];M=f['effort_ceiling'];tm=hyper['memory'];lag=hyper['lag'];z=np.empty(i0+16);z[0]=np.log(2)/10;alpha=np.exp(-1/tm)
        for i in range(1,i0+1):z[i]=alpha*z[i-1]+(1-alpha)*np.logaddexp(0,10*(N[i-1]-N[i]))/10
        nn,uu=N[i0],U[i0];path=[]
        for step in range(15):
            i=i0+step;nd=stock_flow(np.array([nn]),np.array([uu]),basepars)[0];ud=flow(np.array([uu]),np.array([z[i-lag]]),pars[0],pars[1],M,label=='protective')[0];z[i+1]=alpha*z[i]+(1-alpha)*np.logaddexp(0,10*(nn-nd))/10;path.append([nd,ud]);nn,uu=nd,ud
        path=np.array(path);recurs[label]={'stock':metrics(trueN,path[:,0]),'proxy':metrics(trueU,path[:,1]),'stock_RMSE_ratio_to_constant_persistence':metrics(trueN,path[:,0])['RMSE']/metrics(trueN,np.full(15,N[i0]))['RMSE'],'stock_RMSE_ratio_to_VAR1':metrics(trueN,path[:,0])['RMSE']/metrics(trueN,var[:,0])['RMSE'],'proxy_RMSE_ratio_to_constant_persistence':metrics(trueU,path[:,1])['RMSE']/metrics(trueU,np.full(15,U[i0]))['RMSE'],'proxy_RMSE_ratio_to_VAR1':metrics(trueU,path[:,1])['RMSE']/metrics(trueU,var[:,1])['RMSE'],'domain_violations':int(np.sum(path<=0))}
        for k,(n,u)in enumerate(path):rows.append({'law':label,'year':2010+k,'observed_N':trueN[k],'observed_U':trueU[k],'predicted_N':n,'predicted_U':u,'VAR1_N':var[k,0],'VAR1_U':var[k,1],'constant_N':N[i0],'constant_U':U[i0]})
    pd.DataFrame(predrows).to_csv(ROOT/'data/field_stock_predictions_v43.csv',index=False);pd.DataFrame(rows).to_csv(ROOT/'data/field_recursive_predictions_v43.csv',index=False)
    K=basepars[0]/basepars[1];pf=data['scenarios']['TBiomass']['protective'];E0=pf['parameters'][1]*pf['effort_ceiling'];Nb=K*(1-basepars[2]*E0/basepars[0]);gamma=basepars[2]*K*E0*(1+K/Nb)
    result={'protective_sufficient_basin_gain_diagnostic':{'E0':E0,'K':float(K),'Nb':float(Nb),'Gamma':float(gamma),'sufficient_condition_satisfied':bool(gamma<1),'not_a_proof_of_instability':True},'status':'Exploratory secondary test; not a fit of the original continuous-delay DDE','ecological_observation_operator':'normalized reported total biomass; observed normalized catch-intensity proxy drives one-year stock flow; q-like scale fitted, not presumed','stock_equation':'Ndot=(r-h U)N-b N^2 [+ beta R_(year-g)] with exact held-input Riccati flow','selection_grid':out,'selected_recruitment_model':best,'one_step_test':final,'recursive_test':recurs,'recursive_definition':'Annual held-effort stock flow plus start-measurement command update and modeled decline-memory update; not claimed identical to the continuous DDE','recursive_initialization_year':2009,'future_observed_stock_catch_recruitment_used':False,'recruitment_in_recursive_model':False,'cautions':['secondary design follows the initial component test and is explicitly exploratory','age-structured biomass is assessment-derived, with correlated errors','recruitment is an explanatory competitor, not independent institutional evidence','component tests or an annual-surrogate forecast do not establish causal deployment delay or the full autonomous DDE']}
    (ROOT/'data/field_stock_and_recursive_v43.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return result
if __name__=='__main__':run()

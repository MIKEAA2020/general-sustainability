% =========================================================================
% three_state_core_dde_plots.m
% Browser-safe, plot-focused cross-check of the corrected three-state core
% for onlinematlab.com / myCompiler.io (Octave/MATLAB).  Pure scalar, no
% toolboxes.  FIXED: effort is NOT clamped to Dref (the earlier bug); only N
% is floored, exactly as the verified Python implementation does.
%
% Shows, over a short horizon (browser-friendly):
%   (1) tau=5.57   : lower bistable window  -> large-amplitude cycle
%   (2) tau=77     : middle (monostable)    -> decays to equilibrium
%   (3) tau=148.3  : upper bistable window  -> large cycle (basin seed)
%   (4) tau=3.666  : near tau_-             -> subcritical basin capture
% Each ~200-500 yr trajectory is a few thousand RK4 steps -> browser-safe.
% =========================================================================
clear; clc; close all;

% ---------- parameters (Candidate A, corrected core) ----------
r=0.02; K=100; q=0.001; eta=0.914; Emax=30; Dref=1.0;
delta0=0.01; Zref=1.0; k=10.0; taum=5.0; delta=log(2)/k;

% ---------- equilibrium (positive root: a<0 so use -sqrt branch) ----------
Zs=delta; a=-eta/Emax; b=eta*Zs/Dref; c=delta0*Zs/(Zref+Zs);
disc=b*b-4*a*c;
Estar=(-b-sqrt(disc))/(2*a);      % <-- the positive root (a<0)
Nstar=K*(1-q*Estar/r);
fprintf('Equilibrium: N*=%.4f  E*=%.4f  Z*=%.4f  (manuscript 89.552 / 2.090 / 0.0693)\n',Nstar,Estar,Zs);

% ---------- run the 4 showcase trajectories ----------
cases = { ...
  5.57,  40.0, 0.1, 8.0,  400, 'tau=5.57  (lower bistable window: LARGE CYCLE)'; ...
  77.0,  40.0, 0.1, 8.0,  400, 'tau=77    (middle, monostable: DECAYS to equilibrium)'; ...
  148.3, 134.0, Zs, 0.84, 400, 'tau=148.3 (upper bistable window: LARGE CYCLE)'; ...
  3.666, Nstar*1.02, Zs, Estar*1.02, 600, 'tau=3.666 (near tau_-: subcritical basin capture / slow growth)'; ...
};
figure;
for i=1:size(cases,1)
    tau=cases{i,1}; N0=cases{i,2}; Z0=cases{i,3}; E0=cases{i,4}; T=cases{i,5}; lab=cases{i,6};
    [t, N, E] = dde_series(N0,Z0,E0,tau,T,0.05, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    subplot(2,2,i); plot(t,N,'b-','LineWidth',1.2); hold on;
    plot([t(1) t(end)],[Nstar Nstar],'r--','LineWidth',1); grid on;
    title(lab,'FontSize',8); xlabel('year'); ylabel('N'); ylim([0 1.6*max(N)]);
end
print('-dpng','three_state_dde_cases.png');   % save (some sandboxes support)
fprintf('\nPlots generated. Compare: lower fold ~5.574 (cycle here at 5.57),\n');
fprintf('middle quiet (decay here at 77), upper fold ~148.3 (cycle at 148.3 from\n');
fprintf('the large-stock basin seed 134/0.069/0.84).  Note critical slowing:\n');
fprintf('tau=5.60 and tau=149 need ~1e6-yr horizons to show the collapse the\n');
fprintf('manuscript reports (a browser-safe short window shows the transient).\n');

% =========================================================================
% dde_series: fixed-step RK4 DDE with circular delay buffer; returns
% (time, N, E) sampled every 5 steps.  N floored at 0; E NOT clamped
% (the effort equation is self-limiting via (1-E/Emax)).
% =========================================================================
function [t, Ns, Es] = dde_series(N0,Z0,E0,tau,T,dt, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
    nd=max(1,round(tau/dt)); Zbuf=Z0*ones(1,nd+1);
    N=N0; Z=Z0; E=E0; bp=0; ns=round(T/dt);
    nout=floor(ns/5)+1; t=zeros(nout,1); Ns=zeros(nout,1); Es=zeros(nout,1); oi=1;
    t(1)=0; Ns(1)=N; Es(1)=E;
    for st=1:ns
        Zd=Zbuf(mod(bp-nd,nd+1)+1);
        [k1N,k1Z,k1E]=dde_rhs(N,Z,E,Zd, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
        [k2N,k2Z,k2E]=dde_rhs(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,Zd, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
        [k3N,k3Z,k3E]=dde_rhs(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,Zd, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
        [k4N,k4Z,k4E]=dde_rhs(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,Zd, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
        N=N+dt/6*(k1N+2*k2N+2*k3N+k4N);
        Z=Z+dt/6*(k1Z+2*k2Z+2*k3Z+k4Z);
        E=E+dt/6*(k1E+2*k2E+2*k3E+k4E);
        N=max(N,0);
        bp=mod(bp+1,nd+1); Zbuf(bp+1)=Z;
        if mod(st,5)==0, oi=oi+1; t(oi)=st*dt; Ns(oi)=N; Es(oi)=E; end
    end
    t=t(1:oi); Ns=Ns(1:oi); Es=Es(1:oi);
end

% =========================================================================
% dde_rhs: RHS of the corrected three-state core.
% =========================================================================
function [fN,fZ,fE]=dde_rhs(N,Z,E,Zd, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
    S=r*N*(1-N/K);
    fN=S-q*E*N;
    u=q*E*N-S;
    sp=(k*u>30)*u + (k*u<=30)*(log1p(exp(k*u))/k);
    fZ=(max(0, sp - log(2)/k + delta) - Z)/taum;
    fE=(1-E/Emax)*( eta*E*(Zd/Dref - E/Emax) + delta0*Zd/(Zref+Zd) );
end

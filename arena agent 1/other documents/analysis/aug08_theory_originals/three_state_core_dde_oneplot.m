% =========================================================================
% three_state_core_dde_oneplot.m
% Single-panel version for onlinematlab.com / myCompiler.io (Octave/MATLAB).
% Edit "which" below to 1..4 and run; each renders ONE plot (more reliable
% in browser sandboxes than multi-subplot).
%   which=1: tau=5.57  lower window  -> LARGE CYCLE
%   which=2: tau=77    middle        -> decays to equilibrium
%   which=3: tau=148.3 upper window  -> LARGE CYCLE (basin seed 134)
%   which=4: tau=3.666 near tau_-    -> subcritical basin capture
% =========================================================================
clear; clc; close all;
which = 1;                     % <<< EDIT HERE

r=0.02; K=100; q=0.001; eta=0.914; Emax=30; Dref=1.0;
delta0=0.01; Zref=1.0; k=10.0; taum=5.0; delta=log(2)/k;
Zs=delta; a=-eta/Emax; b=eta*Zs/Dref; c=delta0*Zs/(Zref+Zs);
disc=b*b-4*a*c; Estar=(-b-sqrt(disc))/(2*a); Nstar=K*(1-q*Estar/r);

switch which
  case 1, tau=5.57;  N0=40.0; Z0=0.1; E0=8.0;    T=500; lab='tau=5.57  lower bistable window: LARGE CYCLE';
  case 2, tau=77.0;  N0=40.0; Z0=0.1; E0=8.0;    T=500; lab='tau=77    middle, monostable: DECAYS to equilibrium';
  case 3, tau=148.3; N0=134.0; Z0=Zs; E0=0.84;   T=500; lab='tau=148.3 upper bistable window: LARGE CYCLE';
  case 4, tau=3.666; N0=Nstar*1.02; Z0=Zs; E0=Estar*1.02; T=700; lab='tau=3.666 near tau_-: subcritical basin capture (slow growth)';
end
[t, N] = dde_series(N0,Z0,E0,tau,T,0.05, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
plot(t,N,'b-','LineWidth',1.4); hold on;
plot([t(1) t(end)],[Nstar Nstar],'r--','LineWidth',1.2); grid on;
title(lab,'FontSize',9); xlabel('year'); ylabel('N');
legend('N(t)','N* = 89.55'); ylim([0 1.7*max(N)]);
fprintf('N* = %.2f  E* = %.2f\n', Nstar, Estar);
fprintf('done: plot for which=%d (tau=%.2f)\n', which, tau);

% ---------------------------------------------------------------------
function [t,Ns] = dde_series(N0,Z0,E0,tau,T,dt, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
  nd=max(1,round(tau/dt)); Zbuf=Z0*ones(1,nd+1); N=N0; Z=Z0; E=E0; bp=0; ns=round(T/dt);
  nout=floor(ns/5)+1; t=zeros(nout,1); Ns=zeros(nout,1); oi=1; t(1)=0; Ns(1)=N;
  for st=1:ns
    Zd=Zbuf(mod(bp-nd,nd+1)+1);
    [k1N,k1Z,k1E]=dde_rhs(N,Z,E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    [k2N,k2Z,k2E]=dde_rhs(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    [k3N,k3Z,k3E]=dde_rhs(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    [k4N,k4Z,k4E]=dde_rhs(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    N=N+dt/6*(k1N+2*k2N+2*k3N+k4N); Z=Z+dt/6*(k1Z+2*k2Z+2*k3Z+k4Z); E=E+dt/6*(k1E+2*k2E+2*k3E+k4E);
    N=max(N,0); bp=mod(bp+1,nd+1); Zbuf(bp+1)=Z;
    if mod(st,5)==0, oi=oi+1; t(oi)=st*dt; Ns(oi)=N; end
  end
  t=t(1:oi); Ns=Ns(1:oi);
end

function [fN,fZ,fE]=dde_rhs(N,Z,E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
  S=r*N*(1-N/K); fN=S-q*E*N;
  u=q*E*N-S; sp=(k*u>30)*u + (k*u<=30)*(log1p(exp(k*u))/k);
  fZ=(max(0,sp-log(2)/k+delta)-Z)/taum;
  fE=(1-E/Emax)*(eta*E*(Zd/Dref-E/Emax)+delta0*Zd/(Zref+Zd));
end

% =========================================================================
% dde_diagnostic.m  --  CLEAN version (no HTML escapes)
% Decisive numeric check: tau=5.57 from (40,0.1,8), T=500.
% Prints final N and tail amplitude.
%   tail_amp > 15  => correct (large cycle present; reference ~31.6)
%   tail_amp ~ 0   => wrong (browser integration differs)
% Run in myCompiler.io (real Octave) or local Octave/MATLAB.
% =========================================================================
clear; clc; close all;
r=0.02; K=100; q=0.001; eta=0.914; Emax=30; Dref=1.0;
delta0=0.01; Zref=1.0; k=10.0; taum=5.0; delta=log(2)/k;

Zs=delta; a=-eta/Emax; b=eta*Zs/Dref; c=delta0*Zs/(Zref+Zs);
disc=b*b-4*a*c; Estar=(-b-sqrt(disc))/(2*a); Nstar=K*(1-q*Estar/r);
fprintf('N* = %.4f  E* = %.4f\n', Nstar, Estar);

tau=5.57; N0=40.0; Z0=0.1; E0=8.0; T=500; dt=0.05;
[t, N, E] = dde_series(N0,Z0,E0,tau,T,dt, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);

nt=length(N); tail0=round(0.8*nt);
tail_amp = max(N(tail0:end)) - min(N(tail0:end));
fprintf('tau=5.57 (40,0.1,8) T=500:\n');
fprintf('  final N = %.2f   tail_amp = %.2f\n', N(end), tail_amp);
fprintf('  reference (validated Python): final N ~ 87.3, tail_amp ~ 31.6\n');
if tail_amp > 15
  fprintf('  CORRECT: large cycle present\n');
else
  fprintf('  WRONG: no cycle (integration differs from validated)\n');
end
fprintf('  N profile (every ~50 yr):');
for k=1:10:nt
  fprintf(' %.0f', N(k));
end
fprintf('\n');

% ---------------------------------------------------------------------
function [t,Ns,Es] = dde_series(N0,Z0,E0,tau,T,dt, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
  nd=max(1,round(tau/dt)); Zbuf=Z0*ones(1,nd+1); N=N0; Z=Z0; E=E0; bp=0; ns=round(T/dt);
  nout=floor(ns/5)+1; t=zeros(nout,1); Ns=zeros(nout,1); Es=zeros(nout,1); oi=1; t(1)=0; Ns(1)=N; Es(1)=E;
  for st=1:ns
    Zd=Zbuf(mod(bp-nd,nd+1)+1);
    [k1N,k1Z,k1E]=dde_rhs(N,Z,E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    [k2N,k2Z,k2E]=dde_rhs(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    [k3N,k3Z,k3E]=dde_rhs(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    [k4N,k4Z,k4E]=dde_rhs(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
    N=N+dt/6*(k1N+2*k2N+2*k3N+k4N); Z=Z+dt/6*(k1Z+2*k2Z+2*k3Z+k4Z); E=E+dt/6*(k1E+2*k2E+2*k3E+k4E);
    N=max(N,0); bp=mod(bp+1,nd+1); Zbuf(bp+1)=Z;
    if mod(st,5)==0, oi=oi+1; t(oi)=st*dt; Ns(oi)=N; Es(oi)=E; end
  end
  t=t(1:oi); Ns=Ns(1:oi); Es=Es(1:oi);
end

function [fN,fZ,fE]=dde_rhs(N,Z,E,Zd,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
  S=r*N*(1-N/K); fN=S-q*E*N;
  u=q*E*N-S;
  sp=(k*u>30)*u + (k*u<=30)*(log1p(exp(k*u))/k);
  fZ=(max(0, sp - log(2)/k + delta) - Z)/taum;
  fE=(1-E/Emax)*( eta*E*(Zd/Dref - E/Emax) + delta0*Zd/(Zref+Zd) );
end

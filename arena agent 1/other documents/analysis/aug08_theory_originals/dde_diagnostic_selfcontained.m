% =========================================================================
% dde_diagnostic_selfcontained.m
% Fully self-contained (NO local functions) -- works on JDoodle/myCompiler
% Octave where script-local functions defined below the call fail.
% Decisive numeric check: tau=5.57 from (40,0.1,8), T=500.
%   tail_amp > 15  => correct (large cycle present; reference ~31.6)
%   tail_amp ~ 0   => wrong (integration differs)
% =========================================================================
clear; clc; close all;
r=0.02; K=100; q=0.001; eta=0.914; Emax=30; Dref=1.0;
delta0=0.01; Zref=1.0; k=10.0; taum=5.0; delta=log(2)/k;

Zs=delta; a=-eta/Emax; b=eta*Zs/Dref; c=delta0*Zs/(Zref+Zs);
disc=b*b-4*a*c; Estar=(-b-sqrt(disc))/(2*a); Nstar=K*(1-q*Estar/r);
fprintf('N* = %.4f  E* = %.4f\n', Nstar, Estar);

tau=5.57; N0=40.0; Z0=0.1; E0=8.0; T=500; dt=0.05;

% ---- RK4 DDE integration, inlined (no function calls) ----
nd=max(1,round(tau/dt)); Zbuf=Z0*ones(1,nd+1);
N=N0; Z=Z0; E=E0; bp=0; ns=round(T/dt);
nout=floor(ns/5)+1; t=zeros(nout,1); Ns=zeros(nout,1); Es=zeros(nout,1);
oi=1; t(1)=0; Ns(1)=N; Es(1)=E;
for st=1:ns
    Zd=Zbuf(mod(bp-nd,nd+1)+1);
    % --- k1 ---
    S=r*N*(1-N/K);
    u=q*E*N-S;
    spv=(k*u>30)*u + (k*u<=30)*(log1p(exp(k*u))/k);
    k1N=S-q*E*N;
    k1Z=(max(0, spv - log(2)/k + delta) - Z)/taum;
    k1E=(1-E/Emax)*( eta*E*(Zd/Dref - E/Emax) + delta0*Zd/(Zref+Zd) );
    % --- k2 ---
    N2=N+dt/2*k1N; Z2=Z+dt/2*k1Z; E2=E+dt/2*k1E;
    S2=r*N2*(1-N2/K); u2=q*E2*N2-S2;
    spv2=(k*u2>30)*u2 + (k*u2<=30)*(log1p(exp(k*u2))/k);
    k2N=S2-q*E2*N2;
    k2Z=(max(0, spv2 - log(2)/k + delta) - Z2)/taum;
    k2E=(1-E2/Emax)*( eta*E2*(Zd/Dref - E2/Emax) + delta0*Zd/(Zref+Zd) );
    % --- k3 ---
    N3=N+dt/2*k2N; Z3=Z+dt/2*k2Z; E3=E+dt/2*k2E;
    S3=r*N3*(1-N3/K); u3=q*E3*N3-S3;
    spv3=(k*u3>30)*u3 + (k*u3<=30)*(log1p(exp(k*u3))/k);
    k3N=S3-q*E3*N3;
    k3Z=(max(0, spv3 - log(2)/k + delta) - Z3)/taum;
    k3E=(1-E3/Emax)*( eta*E3*(Zd/Dref - E3/Emax) + delta0*Zd/(Zref+Zd) );
    % --- k4 ---
    N4=N+dt*k3N; Z4=Z+dt*k3Z; E4=E+dt*k3E;
    S4=r*N4*(1-N4/K); u4=q*E4*N4-S4;
    spv4=(k*u4>30)*u4 + (k*u4<=30)*(log1p(exp(k*u4))/k);
    k4N=S4-q*E4*N4;
    k4Z=(max(0, spv4 - log(2)/k + delta) - Z4)/taum;
    k4E=(1-E4/Emax)*( eta*E4*(Zd/Dref - E4/Emax) + delta0*Zd/(Zref+Zd) );
    % --- advance ---
    N=N+dt/6*(k1N+2*k2N+2*k3N+k4N);
    Z=Z+dt/6*(k1Z+2*k2Z+2*k3Z+k4Z);
    E=E+dt/6*(k1E+2*k2E+2*k3E+k4E);
    N=max(N,0);
    bp=mod(bp+1,nd+1); Zbuf(bp+1)=Z;
    if mod(st,5)==0, oi=oi+1; t(oi)=st*dt; Ns(oi)=N; Es(oi)=E; end
end
t=t(1:oi); Ns=Ns(1:oi); Es=Es(1:oi);

% ---- report ----
nt=length(Ns); tail0=round(0.8*nt);
tail_amp = max(Ns(tail0:end)) - min(Ns(tail0:end));
fprintf('tau=5.57 (40,0.1,8) T=500:\n');
fprintf('  final N = %.2f   tail_amp = %.2f\n', Ns(end), tail_amp);
fprintf('  reference (validated Python): final N ~ 87.3, tail_amp ~ 31.6\n');
if tail_amp > 15
  fprintf('  CORRECT: large cycle present\n');
else
  fprintf('  WRONG: no cycle (integration differs from validated)\n');
end
fprintf('  N profile (every ~50 yr):');
for k=1:10:nt
  fprintf(' %.0f', Ns(k));
end
fprintf('\n');

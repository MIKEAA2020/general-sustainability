% ============================================================
% 3-state core DDE cross-check (Octave/MATLAB, paste into myCompiler.io)
% Fixed-step RK4 + circular delay buffer.  Pure scalar, no toolboxes.
% ============================================================
clear; clc;
tr=@(c,a,b) (c*a+(1-c)*b);
% --- parameters (Candidate A, corrected core) ---
r=0.02; K=100; q=0.001; eta=0.914; Emax=30; Dref=1.0;
delta0=0.01; Zref=1.0; k=10.0; taum=5.0; delta=log(2)/k;

% --- equilibrium ---
Zs=delta; a=-eta/Emax; b=eta*Zs/Dref; c=delta0*Zs/(Zref+Zs);
disc=b*b-4*a*c; E1=(-b+sqrt(disc))/(2*a); E2=(-b-sqrt(disc))/(2*a);
Estar=max(E1,E2); Nstar=K*(1-q*Estar/r);
fprintf('Equilibrium: N*=%.4f Z*=%.4f E*=%.4f (manuscript 89.552/0.0693/2.090)\n',Nstar,Zs,Estar);

% --- RK4 DDE with circular buffer, returns [Nf, tail_amp] ---
function [Nf,amp]=dde(N0,Z0,E0,tau,T,dt,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
  nd=max(1,round(tau/dt)); Zbuf=Z0*ones(1,nd+1); N=N0; Z=Z0; E=E0; bp=0;
  ns=round(T/dt); t0=round(0.8*ns); Nmin=inf; Nmax=-inf;
  for st=1:ns
    Zd=Zbuf(mod(bp-nd,nd+1)+1);
    S=r*N*(1-N/K);
    u=q*E*N-S; sp=(k*u>30)*u + (k*u<=30)*(log1p(exp(k*u))/k);
    k1N=S-q*E*N; k1Z=(max(0,sp-log(2)/k+delta)-Z)/taum;
    k1E=(1-E/Emax)*(eta*E*(Zd/Dref-E/Emax)+delta0*Zd/(Zref+Zd));
    N2=N+dt/2*k1N; Z2=Z+dt/2*k1Z; E2=E+dt/2*k1E; S2=r*N2*(1-N2/K);
    u2=q*E2*N2-S2; sp2=(k*u2>30)*u2+(k*u2<=30)*(log1p(exp(k*u2))/k);
    k2N=S2-q*E2*N2; k2Z=(max(0,sp2-log(2)/k+delta)-Z2)/taum;
    k2E=(1-E2/Emax)*(eta*E2*(Zd/Dref-E2/Emax)+delta0*Zd/(Zref+Zd));
    N3=N+dt/2*k2N; Z3=Z+dt/2*k2Z; E3=E+dt/2*k2E; S3=r*N3*(1-N3/K);
    u3=q*E3*N3-S3; sp3=(k*u3>30)*u3+(k*u3<=30)*(log1p(exp(k*u3))/k);
    k3N=S3-q*E3*N3; k3Z=(max(0,sp3-log(2)/k+delta)-Z3)/taum;
    k3E=(1-E3/Emax)*(eta*E3*(Zd/Dref-E3/Emax)+delta0*Zd/(Zref+Zd));
    N4=N+dt*k3N; Z4=Z+dt*k3Z; E4=E+dt*k3E; S4=r*N4*(1-N4/K);
    u4=q*E4*N4-S4; sp4=(k*u4>30)*u4+(k*u4<=30)*(log1p(exp(k*u4))/k);
    k4N=S4-q*E4*N4; k4Z=(max(0,sp4-log(2)/k+delta)-Z4)/taum;
    k4E=(1-E4/Emax)*(eta*E4*(Zd/Dref-E4/Emax)+delta0*Zd/(Zref+Zd));
    N=N+dt/6*(k1N+2*k2N+2*k3N+k4N); Z=Z+dt/6*(k1Z+2*k2Z+2*k3Z+k4Z); E=E+dt/6*(k1E+2*k2E+2*k3E+k4E);
    N=max(N,0); E=min(max(E,0),Emax);
    bp=mod(bp+1,nd+1); Zbuf(bp+1)=Z;
    if st>=t0, Nmin=min(Nmin,N); Nmax=max(Nmax,N); end
  end
  Nf=N; amp=Nmax-Nmin;
end

% --- stability: near-equil perturbation decays? ---
fprintf('\nLocal stability (2%% perturbation, T=5e4 yr):\n');
for tau=[1 3.666 5.5 77 148.3 150.36 160]
  [Nf,~]=dde(Nstar*1.02,Zs,Estar*1.02,tau,5e4,0.05,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
  fprintf('  tau=%7.2f: |Nf-N*|=%.3e -> %s\n',tau,abs(Nf-Nstar),sprintf('%s',char('stable'+~abs(Nf-Nstar)<1)));
end

% --- fold brackets: large-cycle persistence (far history 40/0.1/8, T=1e6) ---
fprintf('\nLarge-cycle persistence (N0=40,E0=8,Z0=0.1, T=1e6):\n');
for tau=[5.0 5.5 5.57 5.6 77 148.0 148.3 149.0]
  [~,amp]=dde(40.0,0.1,8.0,tau,1e6,0.05,r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
  fprintf('  tau=%6.2f: tail amp=%7.1f -> %s\n',tau,amp,tr(amp>15,'CYCLE','decay'));
end
fprintf('\nExpected: folds ~5.574 (lower) and ~148.3 (upper); quiet at 77.\n');

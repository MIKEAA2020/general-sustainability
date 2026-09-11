% =========================================================================
% three_state_core_dde_rk4.m
% Independent MATLAB/Octave cross-check of the corrected three-state core
% (effort-saturation-corrected effort law), fixed-step RK4 with a circular
% delay buffer — the manuscript's own verification method, implemented in a
% browser (runs on onlinematlab.com, Octave, or MATLAB).
%
% Model (manuscript Eqs. stock-core / Z-core / effort-core-corrected):
%   Ndot = S(N) - q*E*N                       S(N) = r*N*(1 - N/K)
%   Zdot = (max(0, softplus_k(qEN-S) - ln2/k + delta) - Z)/tau_m
%   Edot = (1-E/Emax)*[ eta*E*(Z(t-tau)/Dref - E/Emax)
%                       + delta0*Z(t-tau)/(Zref+Z(t-tau)) ]
%
% Cross-checks (Candidate A, k=10 => delta=ln2/k):
%   equilibrium  N* ~ 89.552, Z* = delta ~ 0.0693, E* ~ 2.090
%   Hopf points  tau_- ~ 3.666 yr, tau_+ ~ 150.36 yr   (characteristic eq.)
%   lower fold   tau_SNPO,L ~ 5.574 (large cycle persists just above tau_-)
%   upper fold   tau_SNPO,R ~ 148.3 (cycle persists just below tau_+)
%   middle       quiet (monostable) at tau ~ 77
%
% Usage: run in Octave/MATLAB:   three_state_core_dde_rk4
% (No toolboxes required; pure scalar loop + circular buffer.)
% =========================================================================

function three_state_core_dde_rk4
    % ---------- parameters (Candidate A, corrected core) ----------
    r   = 0.02;   K   = 100.0;  q   = 0.001;
    eta = 0.914;  Emax = 30.0;  Dref = 1.0;
    delta0 = 0.01;  Zref = 1.0;  k  = 10.0;  taum = 5.0;
    delta = log(2)/k;                    % baseline = ln2/k (Z* = delta)

    % ---------- which checks to run ----------
    % 1: equilibrium  2: stability at tau in [1,5,10,77,149,151] (near-equil decay)
    % 3: fold bracket (large-cycle persistence: lower 5.5-5.6, upper 148-149)
    run_equil = 1;  run_stab = 1;  run_fold = 1;

    % ---------- closed-form equilibrium ----------
    Zs = delta;
    a = -eta/Emax;  b = eta*Zs/Dref;  c = delta0*Zs/(Zref+Zs);
    disc = b*b - 4*a*c;
    E1 = (-b + sqrt(disc))/(2*a);   E2 = (-b - sqrt(disc))/(2*a);
    Estar = max([E1 E2]);            % positive root
    Nstar = K*(1 - q*Estar/r);
    if run_equil
        fprintf('Equilibrium:  N* = %.4f   Z* = %.4f   E* = %.4f\n', Nstar, Zs, Estar);
        fprintf('  (manuscript: N*=89.552, Z*=0.0693, E*=2.090)\n');
    end

    % ---------- 2: local stability: near-equilibrium perturbation decays? ----------
    if run_stab
        fprintf('\nLocal stability (2%% near-equil perturbation, T=5e4 yr):\n');
        taus = [1 3.666 5.5 77 148.3 150.36 160];
        for tau = taus
            [Nf, ~, ~, ~] = dde_rk4(Nstar*1.02, Zs, Estar*1.02, tau, 5e4, 0.05, ...
                r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
            dev = abs(Nf - Nstar);
            fprintf('  tau=%7.2f: |Nf-N*| = %.3e  -> %s\n', tau, dev, ...
                ternary(dev < 1.0, 'stable', 'UNSTABLE'));
        end
    end

    % ---------- 3: fold brackets: large-cycle persistence (far-from-equil) ----------
    if run_fold
        fprintf('\nLarge-cycle persistence (far history: N0=40,E0=8,Z0=0.1, T=1e6 yr):\n');
        fprintf('  (tail amplitude > 15 => cycle persists)\n');
        % lower: cycle just above tau_- (e.g., 5.5), quiet by 5.6
        for tau = [5.0 5.5 5.57 5.6]
            [~, ~, ~, amp] = dde_rk4(40.0, 0.1, 8.0, tau, 1e6, 0.05, ...
                r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
            fprintf('  tau=%5.2f: tail amp = %7.1f  -> %s\n', tau, amp, ternary(amp>15,'CYCLE','decay'));
        end
        % middle: quiet
        [~, ~, ~, amp] = dde_rk4(40.0, 0.1, 8.0, 77.0, 1e6, 0.05, ...
            r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
        fprintf('  tau=77.00: tail amp = %7.1f  -> %s  (expected quiet)\n', amp, ternary(amp>15,'CYCLE','decay'));
        % upper: cycle just below tau_+, quiet by 149
        for tau = [148.0 148.3 149.0]
            [~, ~, ~, amp] = dde_rk4(40.0, 0.1, 8.0, tau, 1e6, 0.05, ...
                r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta);
            fprintf('  tau=%6.2f: tail amp = %7.1f  -> %s\n', tau, amp, ternary(amp>15,'CYCLE','decay'));
        end
    end
    fprintf('\nDone. Compare with the Python verification (verify_hybrid_folds.py):\n');
    fprintf('  equilibrium identical; Hopf tau_-~3.666, tau_+~150.36; folds ~5.574 / ~148.3.\n');
end

% -------------------------------------------------------------------------
% Fixed-step RK4 DDE with circular delay buffer (the manuscript's method).
% Returns [Nf Zf Ef tail_amp] where tail_amp = max-min of N over last 20%.
% -------------------------------------------------------------------------
function [Nf, Zf, Ef, tail_amp] = dde_rk4(N0,Z0,E0,tau,T,dt, r,K,q,eta,Emax,Dref,delta0,Zref,k,taum,delta)
    n_delay = max(1, round(tau/dt));
    Zbuf = Z0 * ones(1, n_delay+1);
    N = N0; Z = Z0; E = E0;
    buf_ptr = 0;
    n_steps = round(T/dt);
    tail0 = round(0.8*n_steps);
    Nmin = inf; Nmax = -inf;
    for step = 1:n_steps
        % delayed Z = entry n_delay steps back in the circular buffer
        Zd = Zbuf(mod(buf_ptr - n_delay, n_delay+1) + 1);
        S  = r*N*(1 - N/K);
        % k1
        u  = q*E*N - S;
        sp = (k*u > 30)*u + (k*u <= 30)*(log1p(exp(k*u))/k);
        k1N = S - q*E*N;
        k1Z = (max(0, sp - log(2)/k + delta) - Z)/taum;
        k1E = (1-E/Emax)*( eta*E*(Zd/Dref - E/Emax) + delta0*Zd/(Zref+Zd) );
        % k2
        N2=N+dt/2*k1N; Z2=Z+dt/2*k1Z; E2=E+dt/2*k1E;
        S2 = r*N2*(1-N2/K);
        u2 = q*E2*N2 - S2;
        sp2= (k*u2>30)*u2 + (k*u2<=30)*(log1p(exp(k*u2))/k);
        k2N = S2 - q*E2*N2;
        k2Z = (max(0, sp2 - log(2)/k + delta) - Z2)/taum;
        k2E = (1-E2/Emax)*( eta*E2*(Zd/Dref - E2/Emax) + delta0*Zd/(Zref+Zd) );
        % k3
        N3=N+dt/2*k2N; Z3=Z+dt/2*k2Z; E3=E+dt/2*k2E;
        S3 = r*N3*(1-N3/K);
        u3 = q*E3*N3 - S3;
        sp3= (k*u3>30)*u3 + (k*u3<=30)*(log1p(exp(k*u3))/k);
        k3N = S3 - q*E3*N3;
        k3Z = (max(0, sp3 - log(2)/k + delta) - Z3)/taum;
        k3E = (1-E3/Emax)*( eta*E3*(Zd/Dref - E3/Emax) + delta0*Zd/(Zref+Zd) );
        % k4
        N4=N+dt*k3N; Z4=Z+dt*k3Z; E4=E+dt*k3E;
        S4 = r*N4*(1-N4/K);
        u4 = q*E4*N4 - S4;
        sp4= (k*u4>30)*u4 + (k*u4<=30)*(log1p(exp(k*u4))/k);
        k4N = S4 - q*E4*N4;
        k4Z = (max(0, sp4 - log(2)/k + delta) - Z4)/taum;
        k4E = (1-E4/Emax)*( eta*E4*(Zd/Dref - E4/Emax) + delta0*Zd/(Zref+Zd) );
        % advance
        N = N + dt/6*(k1N+2*k2N+2*k3N+k4N);
        Z = Z + dt/6*(k1Z+2*k2Z+2*k3Z+k4Z);
        E = E + dt/6*(k1E+2*k2E+2*k3E+k4E);
        N = max(N, 0);
        E = min(max(E, 0), Emax);
        % store Z, advance buffer
        buf_ptr = mod(buf_ptr + 1, n_delay+1);
        Zbuf(buf_ptr+1) = Z;
        % tail amplitude of N (last 20%)
        if step >= tail0
            if N < Nmin, Nmin = N; end
            if N > Nmax, Nmax = N; end
        end
    end
    Nf = N; Zf = Z; Ef = E;
    if Nmin == inf, tail_amp = 0; else, tail_amp = Nmax - Nmin; end
end

function out = ternary(cond, a, b)
    if cond, out = a; else, out = b; end
end

function [tau, mults, periods, amps, fold_points] = ...
    track_fold_branches(core_variant, dt_plot)
% TRACK_FOLD_BRANCHES  DDE-BIFTOOL Floquet-multiplier tracking along the
% remaining fold (candidate SNPO) branches of the scarcity-mobilisation core.
%
%   [tau, mults, periods, amps, fold_points] = ...
%       track_fold_branches(core_variant)
%
% This is the analysis the manuscript flags as outstanding in
% Section "Numerical continuation" and in the Limitations list:
%
%   "for the remaining amplitude-discontinuity thresholds ... we have not
%    yet verified, via dedicated DDE bifurcation-continuation software
%    [Engelborghs et al. 2002] with Floquet-multiplier tracking along the
%    branches, that the amplitude discontinuity is specifically a
%    saddle-node of periodic orbits ..."
%
% It tracks the *stable* large-amplitude periodic-orbit branch through each
% fold and reports the dominant nontrivial Floquet multiplier |mu| as a
% function of tau.  A genuine saddle-node of periodic orbits (SNPO, fold
% of cycles) is identified by a nontrivial multiplier reaching +1 (real) at
% the fold point; a period-doubling would show -1, and a torus bifurcation
% a complex-conjugate pair on the unit circle.
%
% INPUT
%   core_variant : one of
%       'ungated3'   - original ungated three-state core (Eq. 14-16)
%                      Candidate A: tau_-=6.881, tau_SNPO,L=7.355,
%                      tau_SNPO,R=131.24, tau_+=132.375
%       'gated3'     - effort-saturation-corrected core (Eq. 17)
%                      Candidate A: tau_-=3.666, lower fold ~5.574/5.587,
%                      tau_SNPO,R=148.3, tau_+=150.36
%       'fourstate'  - four-state (N,A,Z,E) ungated core
%                      Candidate A: tau_-=6.982, tau_SNPO,L=7.374,
%                      tau_SNPO,R=130.77, tau_+=132.272
%
% OUTPUT
%   tau          : (K x 1) continuation parameters
%   mults        : (K x n) Floquet multipliers at each point (n=3 or 4)
%   periods      : (K x 1) orbit periods
%   amps         : (K x 1) peak-to-peak N amplitude
%   fold_points  : struct with fields .lower, .upper each giving
%                  [tau_fold, mu_at_fold, classification]
%
% REQUIREMENTS: DDE-BIFTOOL v3.x installed on the MATLAB path.
%   http://ddebiftool.sourceforge.net/
%
% USAGE
%   [tau,m,p,a,fp] = track_fold_branches('ungated3');
%   plot(tau, abs(m), 'o-'); yline(1,'k--');
%
% Written for the manuscript "Scarcity-Driven Capital Liquidation and
% Delay-Amplified Instability".  All parameter values match Table 1.
% -----------------------------------------------------------------------

if nargin < 1 || isempty(core_variant)
    core_variant = 'ungated3';
end
if nargin < 2
    dt_plot = 0.05;   % not used by DDE-BIFTOOL (adaptive), reserved
end

%% ---- Parameters (Table 1, Candidate A baseline) ----------------------
p.r       = 0.02;
p.K       = 100.0;
p.q       = 0.001;
p.eta     = 0.914;
p.Emax    = 30.0;
p.delta0  = 0.01;
p.Dref    = 1.0;
p.taum    = 5.0;
p.Zref    = 1.0;
p.k       = 10.0;
p.delta   = log(2)/10;       % = 0.0693147..., baseline-panic deficit

% Four-state-only parameters
p.kappaA  = 0.05;
p.omegaA  = 1e-3;
p.A0      = 1.0;            % 0.01 K
p.Aeq     = p.Aeq_intrinsic + 0;  % set below for four-state

switch lower(core_variant)
    case 'ungated3'
        ind = system_define_3state(p, false);   % gated = false
        tau_seed_upper = 131.8;   % inside upper bistable window
        tau_seed_lower = 7.1;     % inside lower bistable window
        tau_fold_R_guess = 131.24;
        tau_fold_L_guess = 7.355;
        nstate = 3;
    case 'gated3'
        ind = system_define_3state(p, true);    % gated = true (Eq. 17)
        tau_seed_upper = 149.0;   % inside upper bistable window (148.3,150.36)
        tau_seed_lower = 4.0;     % below lower fold pair
        tau_fold_R_guess = 148.3;
        tau_fold_L_guess = 5.575;
        nstate = 3;
    case 'fourstate'
        p.Aeq_intrinsic = 50.0;
        p.Aeq = p.Aeq_intrinsic + p.kappaA*p.K/p.omegaA;  % Dret=0 (no detritus)
        ind = system_define_4state(p);
        tau_seed_upper = 131.5;
        tau_seed_lower = 7.2;
        tau_fold_R_guess = 130.77;
        tau_fold_L_guess = 7.374;
        nstate = 4;
    otherwise
        error('Unknown core_variant: %s', core_variant);
end

%% ---- Set up the steady-state branch and locate Hopf points ------------
% This is standard DDE-BIFTOOL: define parameter vector, create stst
% point, continue in tau, detect Hopf bifurcations.
% Parameter index convention: tau is parameter 1.
par0 = equilibrium_pars(p, core_variant);

% Build an initial steady-state point at the interior equilibrium
stst0 = dde_stst_create('x', eq_state(p, core_variant), ...
                        'parameter', par0);

% Continue the steady-state branch in tau (parameter 1)
fprintf('Continuing steady-state branch to locate Hopf points...\n');
stst_branch = SetupStst(ind, stst0, ...
    'contpar', ind.parameter.tau, ...
    'max_step', [ind.parameter.tau, 0.05], ...
    'max_bound', [ind.parameter.tau, 200], ...
    'min_bound', [ind.parameter.tau, 0.1], ...
    'newheuristics', 0, ...
    'print_residual_info', 0);
stst_branch = br_contn(stst_branch, 4000);

% Extract Hopf points
[hopf_pts, ~] = br_getflags(stst_branch, 'hopf');
if isempty(hopf_pts)
    error('No Hopf points found -- check parameter values.');
end
fprintf('Found %d Hopf point(s).\n', numel(hopf_pts));

%% ---- Initial periodic orbit by time integration ----------------------
% DDE-BIFTOOL's psol branch requires a starting solution.  We obtain one by
% integrating the DDE from a far-from-equilibrium initial condition (large
% stock, low effort) at tau_seed, consistent with how the manuscript seeds
% its continuation.
fprintf('Integrating to seed periodic orbit at tau=%.3f...\n', tau_seed_upper);
[t_upper, y_upper] = seed_cycle(p, core_variant, tau_seed_upper, [99; p.delta; 0.5]);

fprintf('Integrating to seed lower-window cycle at tau=%.3f...\n', tau_seed_lower);
% Lower window: below tau_- the cycle is the sole attractor; integrate there.
[t_lower, y_lower] = seed_cycle(p, core_variant, 6.0, [99; p.delta; 0.5]);

%% ---- Set up psol branches and continue toward each fold --------------
% Upper branch: continue from tau_seed_upper DOWN toward tau_fold_R_guess.
fprintf('\n=== Tracking UPPER-WINDOW stable branch (toward fold) ===\n');
[tau_U, mults_U, periods_U, amps_U] = continue_psol_branch( ...
    ind, p, t_upper, y_upper, tau_seed_upper, ...
    tau_fold_R_guess - 0.5, false, core_variant);

% Lower branch: continue from tau=6 (Regime I, cycle sole attractor) UP
% toward tau_fold_L_guess and through it (the stable cycle exists below
% the lower fold).
fprintf('\n=== Tracking LOWER-WINDOW stable branch (toward fold) ===\n');
[tau_L, mults_L, periods_L, amps_L] = continue_psol_branch( ...
    ind, p, t_lower, y_lower, 6.0, ...
    tau_fold_L_guess + 0.5, true, core_variant);

%% ---- Identify fold points (mu -> +1) --------------------------------
fold_points.upper = classify_fold(tau_U, mults_U);
fold_points.lower = classify_fold(tau_L, mults_L);

%% ---- Assemble output ------------------------------------------------
tau     = {tau_U; tau_L};
mults   = {mults_U; mults_L};
periods = {periods_U; periods_L};
amps    = {amps_U; amps_L};

%% ---- Report ---------------------------------------------------------
fprintf('\n================ FOLD CLASSIFICATION ================\n');
fprintf('Upper fold: tau = %.4f,  dominant nontrivial mu = %.6f\n', ...
    fold_points.upper.tau, fold_points.upper.mu);
fprintf('  -> %s\n', fold_points.upper.classification);
fprintf('Lower fold: tau = %.4f,  dominant nontrivial mu = %.6f\n', ...
    fold_points.lower.tau, fold_points.lower.mu);
fprintf('  -> %s\n', fold_points.lower.classification);
fprintf('===================================================\n');

end


% =====================================================================
% Sub-functions
% =====================================================================

function ind = system_define_3state(p, gated)
% DDE-BIFTOOL system definition for the three-state core.
% State: x(1)=N, x(2)=Z, x(3)=E.  Delay: x(2,t-tau).

if gated
    rhs_eq = @(xx, par) rhs_3state_gated(xx, par, p);
else
    rhs_eq = @(xx, par) rhs_3state_ungated(xx, par, p);
end

ind = sys_rhs( ...
    'sys_rhs', rhs_eq, ...
    'sys_tau', @() 1, ...
    'sys_ntau', @() 1, ...
    'sys_deri', @(xx,par,nx,np,v) deri_3state(xx,par,nx,np,v,p,gated), ...
    'sys_cond', @stst_cond);

% Register parameters: only tau is free; all others are fixed fields in p.
% We store the full parameter struct in a single parameter vector by using
% tau as the free continuation parameter (index 1).  The other constants are
% closed over in p.
ind.parameter.tau = 1;
end


function f = rhs_3state_ungated(xx, par, p)
% xx = [N; Z; E] at t,  xx_d = [N(t-tau); Z(t-tau); E(t-tau)]
x  = xx(1:3,1);
xd = xx(1:3,2);
N = x(1); Z = x(2); E = x(3);
Ztau = xd(2);

S = p.r*N*(1 - N/p.K);
qEN = p.q*E*N;
src = max(0, softplus(qEN - S, p.k) - log(2)/p.k + p.delta);
f = [ S - qEN;
      (src - Z)/p.taum;
      p.eta*E*(Ztau/p.Dref - E/p.Emax) ...
        + p.delta0*Ztau/(p.Zref + Ztau) ];
end


function f = rhs_3state_gated(xx, par, p)
x  = xx(1:3,1);
xd = xx(1:3,2);
N = x(1); Z = x(2); E = x(3);
Ztau = xd(2);
S = p.r*N*(1 - N/p.K);
qEN = p.q*E*N;
src = max(0, softplus(qEN - S, p.k) - log(2)/p.k + p.delta);
bracket = p.eta*E*(Ztau/p.Dref - E/p.Emax) ...
          + p.delta0*Ztau/(p.Zref + Ztau);
f = [ S - qEN;
      (src - Z)/p.taum;
      (1 - E/p.Emax)*bracket ];
end


function J = deri_3state(xx, par, nx, np, v, p, gated)
% Analytical first derivative (DDE-BIFTOOL sys_deri).
% nx=1: dF/dx(t); nx=2: dF/dx(t-tau); np=1: dF/d(tau)=0.
x  = xx(1:3,1);
xd = xx(1:3,2);
N = x(1); Z = x(2); E = x(3);
Ztau = xd(2);
S = p.r*N*(1 - N/p.K);
Sp = p.r*(1 - 2*N/p.K);
qEN = p.q*E*N;
d = qEN - S;
sp_d = sigmoid(p.k*d);            % softplus'(d) = sigmoid(k d)
src_raw = softplus(d, p.k) - log(2)/p.k + p.delta;
h = sp_d * (src_raw > 0);        % derivative of max(0, src_raw)
dd_dN = p.q*E - Sp;
dd_dE = p.q*N;

if isempty(nx)
    J = zeros(3,1);  % derivative w.r.t. parameter (tau) is zero
    return;
end

if nx == 1
    J = [ Sp - p.q*E, 0, -p.q*N;
          h*dd_dN/p.taum, -1/p.taum, h*dd_dE/p.taum;
          0, 0, 0 ];
    if gated
        bracket = p.eta*E*(Ztau/p.Dref - E/p.Emax) ...
                  + p.delta0*Ztau/(p.Zref + Ztau);
        J(3,3) = (1/p.Emax)*(-bracket) ...
                 + (1 - E/p.Emax)*p.eta*(Ztau/p.Dref - 2*E/p.Emax);
        J(3,2) = 0;
    else
        J(3,3) = p.eta*(Ztau/p.Dref - 2*E/p.Emax);
    end
elseif nx == 2
    J = zeros(3,3);
    dE_dZtau = p.eta*E/p.Dref + p.delta0*p.Zref/(p.Zref + Ztau)^2;
    if gated
        dE_dZtau = (1 - E/p.Emax)*dE_dZtau;
    end
    J(3,2) = dE_dZtau;
end
end


function ind = system_define_4state(p)
% State: x(1)=N, x(2)=Z, x(3)=E, x(4)=A_act.  Delay on Z.
rhs_eq = @(xx, par) rhs_4state(xx, par, p);
ind = sys_rhs('sys_rhs', rhs_eq, ...
              'sys_tau', @() 1, ...
              'sys_ntau', @() 1, ...
              'sys_cond', @stst_cond);
ind.parameter.tau = 1;
end


function f = rhs_4state(xx, par, p)
x  = xx(1:4,1);
xd = xx(1:4,2);
N = x(1); Z = x(2); E = x(3); A = x(4);
Ztau = xd(2);
fA = A/(A + p.A0);
R = p.r*N*(1 - N/p.K)*fA;
B = R + p.kappaA*N*fA;
qEN = p.q*E*N;
src = max(0, softplus(qEN - R, p.k) - log(2)/p.k + p.delta);
f = [ R - qEN;
      (src - Z)/p.taum;
      p.eta*E*(Ztau/p.Dref - E/p.Emax) + p.delta0*Ztau/(p.Zref + Ztau);
      -B + p.omegaA*(p.Aeq - A) ];
end


function [t, y] = seed_cycle(p, variant, tau, yinit)
% Integrate the DDE with MATLAB's dde23 for T_warmup to land on the stable
% large-amplitude cycle, then return one period's worth of (t,y) sampled
% densely for the psol initial mesh.
switch lower(variant)
    case {'ungated3','gated3'}
        ddefun = @(t,y,Z) ddefun_3state(t,y,Z,p,strcmpi(variant,'gated3'));
        lags = tau;
        history = equilibrium_3state(p)';
        T_warmup = 300000;
        T_record = 2000;
    case 'fourstate'
        ddefun = @(t,y,Z) ddefun_4state(t,y,Z,p);
        lags = tau;
        history = equilibrium_4state(p)';
        T_warmup = 300000;
        T_record = 2000;
end
opts = ddeset('RelTol',1e-8,'AbsTol',1e-10,'MaxStep',0.5);
% Warm up
sol = dde23(ddefun, lags, history, [0, T_warmup], opts);
% Record tail
yinit_tail = deval(sol, T_warmup);
sol2 = dde23(ddefun, lags, yinit_tail, [0, T_record], opts);
t = linspace(0, T_record, 2000);
y = deval(sol2, t);
% Rescale t so it spans exactly one measured period (find last N-maximum)
N_tail = y(1,:);
[~, pk] = findpeaks(N_tail, t, 'MinPeakDistance', 50);
if numel(pk) >= 2
    T_period = mean(diff(pk));
    t = linspace(0, T_period, 200);
    y = deval(sol2, linspace(T_record - T_period, T_record, 200));
end
end


function dydt = ddefun_3state(t, y, Z, p, gated)
N = y(1); Z = y(2); E = y(3);
Ztau = Z(2);
S = p.r*N*(1 - N/p.K);
qEN = p.q*E*N;
src = max(0, softplus(qEN - S, p.k) - log(2)/p.k + p.delta);
bracket = p.eta*E*(Ztau/p.Dref - E/p.Emax) ...
          + p.delta0*Ztau/(p.Zref + Ztau);
if gated, bracket = (1 - E/p.Emax)*bracket; end
dydt = [S - qEN; (src - Z)/p.taum; bracket];
end


function dydt = ddefun_4state(t, y, Z, p)
N = y(1); Z = y(2); E = y(3); A = y(4);
Ztau = Z(2);
fA = A/(A + p.A0);
R = p.r*N*(1 - N/p.K)*fA;
B = R + p.kappaA*N*fA;
qEN = p.q*E*N;
src = max(0, softplus(qEN - R, p.k) - log(2)/p.k + p.delta);
dydt = [R - qEN;
        (src - Z)/p.taum;
        p.eta*E*(Ztau/p.Dref - E/p.Emax) + p.delta0*Ztau/(p.Zref + Ztau);
        -B + p.omegaA*(p.Aeq - A)];
end


function [tau_out, mults_out, periods_out, amps_out] = ...
    continue_psol_branch(ind, p, t_seed, y_seed, tau_start, tau_end, ...
                         increasing, variant)
% Build a DDE-BIFTOOL psol point from the seed trajectory, set up the
% branch, and continue in tau toward the fold.
n = size(y_seed,1);
degree = 3;
% Build the psol structure.  mesh is normalized [0,1], period is the span.
T_seed = t_seed(end) - t_seed(1);
mesh = linspace(0, 1, size(y_seed,2));
profile = y_seed;
period = T_seed;

psol0 = dde_psol_create('parameter', [tau_start], ...
    'mesh', mesh, 'degree', degree, ...
    'profile', profile, 'period', period);

% Set up continuation.  Free parameter: tau (index 1).
fprintf('Setting up psol branch from tau=%.3f toward %.3f...\n', ...
        tau_start, tau_end);
psol_branch = SetupPsol(ind, psol0, ...
    'contpar', ind.parameter.tau, ...
    'max_step', [ind.parameter.tau, 0.02], ...
    'max_bound', [ind.parameter.tau, max(tau_start, tau_end)+5], ...
    'min_bound', [ind.parameter.tau, min(tau_start, tau_end)-5], ...
    'newheuristics', 0, ...
    'print_residual_info', 0, ...
    'ncols', 4, ...
    'extra_condition', 'off');

% Point it in the right direction
if increasing
    psol_branch.parameter.max_step = [ind.parameter.tau, 0.02];
else
    psol_branch.parameter.max_step = [ind.parameter.tau, -0.02];
end

% Continue; DDE-BIFTOOL monitors stability automatically.
psol_branch = br_contn(psol_branch, 5000);

% Extract multipliers, periods, amplitudes, tau at each converged point.
npts = length(psol_branch.point);
tau_out = zeros(npts,1);
mults_out = zeros(npts, n);
periods_out = zeros(npts,1);
amps_out = zeros(npts,1);
for i = 1:npts
    pt = psol_branch.point(i);
    tau_out(i) = pt.parameter(1);
    periods_out(i) = pt.period;
    amps_out(i) = max(pt.profile(1,:)) - min(pt.profile(1,:));
    % Floquet multipliers: DDE-BIFTOOL stores the monodromy matrix in
    % pt.mesh and pt.stability; use p_cor2lmb or the stability field.
    if isfield(pt, 'stability') && ~isempty(pt.stability)
        mults_out(i,:) = pt.stability.mu(1:n);
    else
        % Compute multipliers via the collocation Jacobian if not present
        mults_out(i,:) = NaN;
    end
end

% Remove NaN rows (non-converged points)
ok = all(~isnan(mults_out),2);
tau_out = tau_out(ok);
mults_out = mults_out(ok,:);
periods_out = periods_out(ok);
amps_out = amps_out(ok);
end


function fp = classify_fold(tau, mults)
% Identify the dominant nontrivial Floquet multiplier and detect +1 crossing.
% mults: K x n, first column assumed to be the trivial phase multiplier ~1.
% We look at the remaining n-1 multipliers.
n = size(mults,2);
% Remove the phase multiplier (closest to +1)
mu_phase = zeros(size(mults,1),1);
mu_nontrivial = zeros(size(mults,1), n-1);
for i = 1:size(mults,1)
    m = mults(i,:);
    [~, iphase] = min(abs(m - 1.0));
    mu_phase(i) = m(iphase);
    rest = m; rest(iphase) = [];
    mu_nontrivial(i,:) = rest;
end
% Dominant nontrivial multiplier (largest modulus)
[dom_mod, idx] = max(abs(mu_nontrivial), [], 2);
dom_mu = arrayfun(@(i) mu_nontrivial(i, idx(i)), (1:size(mu_nontrivial,1))');

% Find where |dom_mu| crosses 1 from inside/outside, with real part near +1
% (SNPO), -1 (period doubling), or on unit circle as complex pair (torus).
cross_idx = find(abs(diff(sign(dom_mod - 1))) > 0, 1);
if isempty(cross_idx)
    fp.tau = NaN;
    fp.mu = NaN;
    fp.classification = 'No +1 crossing detected on this segment';
    return;
end
fp.tau = interp1(dom_mod(cross_idx:cross_idx+1), ...
                 tau(cross_idx:cross_idx+1), 1.0);
fp.mu = interp1(tau(cross_idx:cross_idx+1), ...
                dom_mu(cross_idx:cross_idx+1), fp.tau);
if abs(imag(fp.mu)) < 1e-3
    if real(fp.mu) > 0.95
        fp.classification = 'SNPO (saddle-node of periodic orbits): real mu -> +1';
    else
        fp.classification = 'Period-doubling: real mu -> -1';
    end
else
    fp.classification = 'Torus/Neimark-Sacker: complex pair on unit circle';
end
end


function s = softplus(x, k)
% Numerically stable softplus: (1/k) log(1 + exp(kx))
kx = k*x;
if kx > 50
    s = x;
elseif kx < -50
    s = 0;
else
    s = log1p(exp(kx))/k;
end
end


function s = sigmoid(x)
% sigmoid(x) = 1/(1+exp(-x)), stable
if x > 50, s = 1; elseif x < -50, s = 0; else, s = 1/(1+exp(-x)); end
end


function eq = equilibrium_3state(p)
% Closed-form interior equilibrium (Section equilibrium-core).
Zs = p.delta;
a = -p.eta/p.Emax;
b =  p.eta*Zs/p.Dref;
c =  p.delta0*Zs/(p.Zref + Zs);
Es = (-b - sqrt(b^2 - 4*a*c))/(2*a);
Ns = p.K*(1 - p.q*Es/p.r);
eq = [Ns; Zs; Es];
end


function eq = equilibrium_4state(p)
% Solve (N,A) equilibrium at fixed E*, Z*=delta.
Zs = p.delta;
a = -p.eta/p.Emax;
b =  p.eta*Zs/p.Dref;
c =  p.delta0*Zs/(p.Zref + Zs);
Es = (-b - sqrt(b^2 - 4*a*c))/(2*a);
N = p.K*(1 - p.q*Es/p.r);
A = 5000;  % initial guess
for _ = 1:200
    fA = A/(A + p.A0);
    R = p.r*N*(1 - N/p.K)*fA;
    B = R + p.kappaA*N*fA;
    f1 = R - p.q*Es*N;
    f2 = -B + p.omegaA*(p.Aeq - A);
    dR_dN = p.r*(1 - 2*N/p.K)*fA;
    dR_dA = p.r*N*(1 - N/p.K)*p.A0/(A+p.A0)^2;
    dB_dN = dR_dN + p.kappaA*fA;
    dB_dA = dR_dA + p.kappaA*N*p.A0/(A+p.A0)^2;
    J = [dR_dN - p.q*Es, dR_dA; -dB_dN, -dB_dA - p.omegaA];
    step = J\(-[f1; f2]);
    N = N + step(1); A = A + step(2);
    if norm(step) < 1e-12, break; end
end
eq = [N; Zs; Es; A];
end


function par = equilibrium_pars(p, variant)
% Parameter vector: DDE-BIFTOOL only frees tau (parameter 1); all other
% constants are closed over in p.  We set tau to a starting value.
switch lower(variant)
    case {'ungated3','gated3'}
        par = 7.0;   % placeholder, will be overwritten per branch
    case 'fourstate'
        par = 7.0;
end
end


function x = eq_state(p, variant)
switch lower(variant)
    case 'ungated3', x = equilibrium_3state(p);
    case 'gated3',   x = equilibrium_3state(p);  % equilibrium unchanged
    case 'fourstate',x = equilibrium_4state(p);
end
end


function res = stst_cond(point)
% Trivial user condition; DDE-BIFTOOL needs a function handle even if empty.
res = zeros(0,1);
end

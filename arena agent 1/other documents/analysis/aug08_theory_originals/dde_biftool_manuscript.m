function dde_biftool_manuscript(core_variant)
% DDE_BIFTOOL_MANUSCRIPT  Collocation-grade Floquet classification of the
% manuscript's folds (SNPO vs period-doubling vs torus).
%
%   dde_biftool_manuscript('gated3')   % default: corrected core (Eq. 17)
%
% This closes the open item flagged in the manuscript's Limitations:
%   "...we have not yet verified, via dedicated DDE bifurcation-continuation
%    software [Engelborghs et al. 2002] with Floquet-multiplier tracking
%    along the branches, that the amplitude discontinuity is specifically a
%    saddle-node of periodic orbits..."
%
% A fold of periodic orbits (SNPO) is confirmed when the DOMINANT NONTRIVIAL
% Floquet multiplier hits exactly +1 (real) at the fold point.  Distinguishers:
%   real mu -> +1  : saddle-node of periodic orbits (SNPO)
%   real mu -> -1  : period-doubling
%   complex pair on |mu|=1 : torus (Neimark-Sacker)
%
% REQUIREMENTS: DDE-BIFTOOL 3.x on the MATLAB path.
%   https://github.com/DDE-BIFTOOL/DDE-BIFTOOL
%   (git clone; then addpath(genpath('<clone>')) )
%
% VERIFIED REFERENCE NUMBERS (from the manuscript's characteristic equation
% and shooting suite; use them to confirm the run is sane):
%   gated3 (corrected core, Eq. 17), Candidate A:
%     equilibrium   N*=89.551883  Z*=0.0693147  E*=2.089623
%     Hopf pair     tau_-=3.6662  tau_+=150.3585
%     folds         stable-cycle fold   ~5.574-5.575
%                   unstable-branch fold ~5.587
%                   upper-window fold   ~148.3
%
% WHAT TO LOOK FOR:
%   * At each fold, the dominant nontrivial |mu| should rise to 1.0 and the
%     multiplier should be REAL +1 at the fold point -> "SNPO".
%   * The unstable branch born at tau_- (subcritical Hopf) should fold at
%     ~5.587 with a real multiplier crossing +1.
%   * The upper fold at ~148.3 should also show a real +1 crossing.
%
% If DDE-BIFTOOL errors, send me the first error line: the API differs
% between 2.x and 3.x and I'll patch the call.

if nargin < 1 || isempty(core_variant)
    core_variant = 'gated3';
end

%% ---------- Parameters (Candidate A baseline, Table 1) ----------
p.r      = 0.02;
p.K      = 100.0;
p.q      = 0.001;
p.eta    = 0.914;
p.Emax   = 30.0;
p.delta0 = 0.01;
p.Dref   = 1.0;
p.taum   = 5.0;
p.Zref   = 1.0;
p.k      = 10.0;
p.delta  = log(2)/10;        % 0.0693147...

gated = strcmpi(core_variant, 'gated3');

%% ---------- System definition (DDE-BIFTOOL 3.x) ----------
funcs.sys_rhs   = @(xx,par) rhs_core(xx, par, p, gated);
funcs.sys_tau   = @(par) par(1);      % <-- CRITICAL: delay = continuation par
funcs.sys_ntau  = @() 1;
funcs.sys_deri  = @(xx,par,nx,np,v) deri_core(xx, par, nx, np, v, p, gated);
% funcs.sys_cond  = @() 0;            % no user conditions (omit = zero)

% Equilibrium (closed form; identical for gated/ungated)
eq = equilibrium_core(p);

fprintf('DDE-BIFTOOL manuscript run  [%s]\n', core_variant);
fprintf('Equilibrium: N*=%.6f  Z*=%.6f  E*=%.6f\n', eq(1), eq(2), eq(3));

%% ---------- Step 1: steady-state branch -> Hopf points ----------
par0 = 7.0;                              % tau start (par(1) = tau)
stst = dde_stst_create('x', eq, 'parameter', par0);
stst_branch = SetupStst(funcs, stst, ...
    'contpar', 1, ...
    'max_step', [1 0.05], ...
    'max_bound', [1 200], ...
    'min_bound', [1 0.1], ...
    'newheuristics', 0, ...
    'print_residual_info', 0);
fprintf('\nStep 1: continuing steady-state branch (tau: 0.1 -> 200)...\n');
stst_branch = br_contn(stst_branch, 4000);

[hopf_idx, ~] = br_getflags(stst_branch, 'hopf');
fprintf('Found %d Hopf point(s)\n', numel(hopf_idx));
for i = 1:numel(hopf_idx)
    hp = stst_branch.point(hopf_idx(i));
    fprintf('  Hopf at tau = %.5f\n', hp.parameter(1));
end
% Expect: tau_- ~ 3.6662 and tau_+ ~ 150.3585

%% ---------- Step 2: lower-window stable cycle through its fold ----------
% For tau < tau_- the equilibrium is unstable; the large cycle is the sole
% attractor.  Seed at tau=4.0 (well inside), continue UP through the fold at
% ~5.575.
fprintf('\nStep 2: lower-window stable cycle (seed tau=4, continue UP)...\n');
[psol_lo, tau_lo, mu_lo] = continue_cycle(funcs, p, gated, 4.0, ...
    [99; p.delta; 0.5], 5.7, +1);
classify_fold_along(tau_lo, mu_lo, 'LOWER stable-cycle fold');

%% ---------- Step 3: unstable branch from the lower Hopf (optional but
%             closes the 5.587 fold) ----------
% The Hopf at tau_- is SUBCRITICAL: a small UNSTABLE orbit is born there.
% Branch-switch from the Hopf point to trace it to its own fold ~5.587.
if numel(hopf_idx) >= 1
    hp = stst_branch.point(hopf_idx(1));   % the tau_- Hopf
    fprintf('\nStep 3: unstable orbit from lower Hopf (tau_0=%.4f)...\n', hp.parameter(1));
    try
        psol_h = SetupPsol(funcs, hp, 'contpar', 1, ...
            'max_step', [1 0.02], 'max_bound', [1 hp.parameter(1)+0.3], ...
            'min_bound', [1 hp.parameter(1)-0.3], 'newheuristics', 0);
        psol_h = br_contn(psol_h, 500);
        [tau_h, mu_h] = collect_psol(psol_h);
        classify_fold_along(tau_h, mu_h, 'UNSTABLE-branch fold (~5.587)');
    catch ME
        fprintf('  Branch switching from Hopf failed: %s\n', ME.message);
        fprintf('  (Falls back to the shooting evidence already on record:\n');
        fprintf('   real multiplier 1.0514 at tau=5.584 -> 0.998983 at 5.587,\n');
        fprintf('   i.e. a real +1 crossing -> SNPO.)\n');
    end
end

%% ---------- Step 4: upper-window stable cycle through its fold ----------
% Large cycle coexists with stable equilibrium in (148.3, 150.36); seed at
% tau=149 from a large stock (basin-capture: large stock -> cycle), continue
% DOWN through the fold at ~148.3.
fprintf('\nStep 4: upper-window stable cycle (seed tau=149, continue DOWN)...\n');
[psol_up, tau_up, mu_up] = continue_cycle(funcs, p, gated, 149.0, ...
    [99; p.delta; 0.5], 147.5, -1);
classify_fold_along(tau_up, mu_up, 'UPPER stable-cycle fold');

fprintf('\n================ DONE ================\n');
fprintf('If all three folds report "real mu -> +1": the manuscript''s\n');
fprintf('SNPO classification is confirmed at collocation grade, and the\n');
fprintf('Limitations sentence can be updated to "confirmed".\n');

end


%% =====================================================================
%  Core RHS (gated = Eq. 17 effort law; ungated = Eq. 14-16)
%  State x(1)=N, x(2)=Z, x(3)=E.  Delay on Z only (x_d(:,1) = x(t-tau)).
% =====================================================================
function f = rhs_core(xx, par, p, gated)
    x  = xx(:,1);
    xd = xx(:,2);
    N = x(1); Z = x(2); E = x(3);
    Ztau = xd(2);
    S = p.r*N*(1 - N/p.K);
    qEN = p.q*E*N;
    src = max(0, softplus(qEN - S, p.k) - log(2)/p.k + p.delta);
    bracket = p.eta*E*(Ztau/p.Dref - E/p.Emax) ...
              + p.delta0*Ztau/(p.Zref + Ztau);
    if gated
        bracket = (1 - E/p.Emax)*bracket;
    end
    f = [ S - qEN;
          (src - Z)/p.taum;
          bracket ];
end


function J = deri_core(xx, par, nx, np, v, p, gated)
    x  = xx(:,1);
    xd = xx(:,2);
    N = x(1); Z = x(2); E = x(3);
    Ztau = xd(2);
    S = p.r*N*(1 - N/p.K);
    Sp = p.r*(1 - 2*N/p.K);
    qEN = p.q*E*N;
    d = qEN - S;
    src_raw = softplus(d, p.k) - log(2)/p.k + p.delta;
    h = sigmoid(p.k*d) * double(src_raw > 0);   % d/dd max(0, src_raw)
    dd_dN = p.q*E - Sp;
    dd_dE = p.q*N;

    % parameter derivative: tau enters only through the delay
    if nx == 0
        J = zeros(3, numel(par));
        return;
    end
    if nx == 1      % dF/dx(t)
        J = [ Sp - p.q*E,           0,      -p.q*N;
              h*dd_dN/p.taum,  -1/p.taum,  h*dd_dE/p.taum;
              0,                      0,      0 ];
        bracket = p.eta*E*(Ztau/p.Dref - E/p.Emax) ...
                  + p.delta0*Ztau/(p.Zref + Ztau);
        if gated
            J(3,3) = (-1/p.Emax)*bracket ...
                     + (1 - E/p.Emax)*p.eta*(Ztau/p.Dref - 2*E/p.Emax);
        else
            J(3,3) = p.eta*(Ztau/p.Dref - 2*E/p.Emax);
        end
        if nargin >= 6 && ~isempty(v)     % directional (Hessian) form
            J = J*v;
        end
    elseif nx == 2   % dF/dx(t-tau)
        J = zeros(3,3);
        dE_dZtau = p.eta*E/p.Dref + p.delta0*p.Zref/(p.Zref + Ztau)^2;
        if gated
            dE_dZtau = (1 - E/p.Emax)*dE_dZtau;
        end
        J(3,2) = dE_dZtau;
        if nargin >= 6 && ~isempty(v)
            J = J*v;
        end
    else
        J = zeros(3,3);
    end
end


function eq = equilibrium_core(p)
    Zs = p.delta;
    a = -p.eta/p.Emax;
    b =  p.eta*Zs/p.Dref;
    c =  p.delta0*Zs/(p.Zref + Zs);
    Es = (-b - sqrt(b^2 - 4*a*c))/(2*a);
    Ns = p.K*(1 - p.q*Es/p.r);
    eq = [Ns; Zs; Es];
end


function [psol, tau, mu] = continue_cycle(funcs, p, gated, tau_seed, ...
                                          yinit, tau_target, direction)
% Seed a stable cycle with dde23, wrap it into a psol point, continue in tau.
    lags = tau_seed;
    history = equilibrium_core(p)';
    T_warmup = 300000;   % ~1000 cycles at period ~250-320 yr
    T_rec    = 3000;

    ddefun = @(t,y,Z) dde_rhs(t,y,Z,p,gated);
    opts = ddeset('RelTol',1e-8,'AbsTol',1e-10,'MaxStep',0.5);
    sol = dde23(ddefun, lags, history, [0 T_warmup], opts);
    ytail = deval(sol, T_warmup);
    sol2 = dde23(ddefun, lags, ytail, [0 T_rec], opts);

    % Measure one period from N peaks, take the last period (manual peak
    % finder - no toolbox dependency)
    tt = linspace(0, T_rec, 4000);
    yy = deval(sol2, tt);
    Nt = yy(1,:);
    pk = find( Nt(2:end-1) > Nt(1:end-2) & Nt(2:end-1) >= Nt(3:end) );
    pk = pk + 1;
    pk = pk(Nt(pk) > mean(Nt) + 0.3*std(Nt));   % keep prominent peaks
    if numel(pk) < 2
        error('Could not find a cycle in the seed integration.');
    end
    T_period = mean(diff(tt(pk(end-2:end))));
    t_last = linspace(T_rec - T_period, T_rec, 200);
    y_last = deval(sol2, t_last);

    % Wrap into a psol point (degree 3, normalized mesh)
    mesh = linspace(0, 1, size(y_last,2));
    psol0 = dde_psol_create('parameter', tau_seed, ...
        'mesh', mesh, 'degree', 3, ...
        'profile', y_last, 'period', T_period);
    fprintf('  seed cycle: period = %.3f yr\n', T_period);

    br = SetupPsol(funcs, psol0, 'contpar', 1, ...
        'max_step', [1 direction*0.02], ...
        'max_bound', [1 max(tau_seed,tau_target)+3], ...
        'min_bound', [1 min(tau_seed,tau_target)-3], ...
        'newheuristics', 0, ...
        'print_residual_info', 0);
    br = br_contn(br, 2000);
    [tau, mu] = collect_psol(br);
    psol = br;
end


function [tau, mu] = collect_psol(br)
% Extract (tau, Floquet multipliers) from every converged psol point.
    n = numel(br.point);
    tau = zeros(n,1);
    mu  = cell(n,1);
    for i = 1:n
        pt = br.point(i);
        tau(i) = pt.parameter(1);
        if isfield(pt, 'stability') && ~isempty(pt.stability) ...
                && isfield(pt.stability, 'mu')
            m = pt.stability.mu(:);
            % sort by modulus descending
            [~, ord] = sort(abs(m), 'descend');
            mu{i} = m(ord);
        else
            mu{i} = [];
        end
    end
end


function classify_fold_along(tau, mu, label)
% Walk the branch; find where the dominant nontrivial multiplier crosses the
% unit circle and classify the crossing (+1 / -1 / complex).
    fprintf('--- %s ---\n', label);
    if isempty(tau)
        fprintf('  no points collected\n'); return;
    end
    dom = nan(numel(tau),1);
    dommu = nan(numel(tau),1);
    for i = 1:numel(tau)
        m = mu{i};
        if isempty(m), continue; end
        % first multiplier ~ trivial (phase). Take the second (dominant
        % nontrivial) by modulus; if only one, use it.
        if numel(m) >= 2
            dom(i) = abs(m(2));
            dommu(i) = m(2);
        else
            dom(i) = abs(m(1));
            dommu(i) = m(1);
        end
    end
    ok = ~isnan(dom);
    fprintf('  n=%d points, tau range [%.4f, %.4f]\n', sum(ok), ...
        min(tau(ok)), max(tau(ok)));
    % report multiplier near the max-|mu| point
    [mx, imx] = max(dom(ok));
    fprintf('  max |mu_nontrivial| = %.5f at tau = %.4f (mu = %+.5f %+.5fi)\n', ...
        mx, tau(ok(imx)), real(dommu(ok(imx))), imag(dommu(ok(imx))));
    if mx > 0.98
        if abs(imag(dommu(ok(imx)))) < 0.05 && real(dommu(ok(imx))) > 0.9
            fprintf('  -> SNPO (saddle-node of periodic orbits): real mu -> +1\n');
        elseif abs(imag(dommu(ok(imx)))) < 0.05 && real(dommu(ok(imx))) < -0.9
            fprintf('  -> PERIOD-DOUBLING: real mu -> -1\n');
        else
            fprintf('  -> TORUS/Neimark-Sacker candidate: complex pair on |mu|=1\n');
        end
    else
        fprintf('  (|mu| did not reach 1.0 on this segment - may need to\n');
        fprintf('   continue closer to the fold; check the tau range.)\n');
    end
end


function s = softplus(x, k)
    kx = k*x;
    if kx > 50,      s = x;
    elseif kx < -50, s = 0;
    else,            s = log1p(exp(kx))/k;
    end
end

function s = sigmoid(x)
    if x > 50,       s = 1;
    elseif x < -50,  s = 0;
    else,            s = 1/(1+exp(-x));
    end
end

function dydt = dde_rhs(t, y, Z, p, gated)
    N = y(1); Zv = y(2); E = y(3);
    Ztau = Z(2,1);               % delayed Z (single delay tau)
    S = p.r*N*(1 - N/p.K);
    qEN = p.q*E*N;
    src = max(0, softplus(qEN - S, p.k) - log(2)/p.k + p.delta);
    bracket = p.eta*E*(Ztau/p.Dref - E/p.Emax) ...
              + p.delta0*Ztau/(p.Zref + Ztau);
    if gated, bracket = (1 - E/p.Emax)*bracket; end
    dydt = [S - qEN; (src - Zv)/p.taum; bracket];
end

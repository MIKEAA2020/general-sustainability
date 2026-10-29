
## S17. Complete equilibrium root counts for every positive delay

At a mobilising registered vector, write
$$\Delta(\lambda,\tau)=P(\lambda)-k\lambda e^{-\lambda\tau},\quad P=(\lambda+a)(\lambda+d)(\lambda+c),\quad a,c,d,k>0.$$
The exact coefficients come from the positive quadratic effort equilibrium, not rounded Jacobian values. The outward scalar calculation of S13 supplies two disjoint simple positive roots of
$$H(x)=(x+a^2)(x+d^2)(x+c^2)-k^2x.$$
The cubic has two coefficient sign changes; the two verified roots exhaust its possible positive roots by Descartes' rule. Also $\Delta(0,\tau)=adc>0$.

**Proof of Theorem 5.2.** At $\tau=0$, put $p_2=a+d+c$, $p_1=ad+ac+dc-k$, $p_0=adc$. The interval tests $p_2>0$, $p_0>0$, $p_2p_1-p_0<0$ give the Routh first-column signs $+,+,-,+$, hence exactly two right-half-plane roots. For $\operatorname{Re}\lambda\ge0$, each $|\lambda+s|\ge|\lambda|$ for $s>0$. At a root, $|\lambda|^3\le k|\lambda|$, uniformly in nonnegative delay. A half-disk of radius greater than $\sqrt{k}$ therefore encloses all unstable roots and has no roots on its curved boundary. Analytic root counting on each compact delay interval changes only at the two imaginary-frequency families; no unstable root can arrive from infinity, including as $\tau\downarrow0$.

At an imaginary root, implicit differentiation gives
$$\left(\frac{d\lambda}{d\tau}\right)^{-1}=-\frac{P'(\lambda)/P(\lambda)-1/\lambda+\tau}{\lambda}.$$
Taking real parts at $\lambda=i\omega$ yields
$$\operatorname{Re}\left[\left(\frac{d\lambda}{d\tau}\right)^{-1}\right]=\frac1{\omega^2+a^2}+\frac1{\omega^2+d^2}+\frac1{\omega^2+c^2}-\frac1{\omega^2}=\frac{H'(\omega^2)}{|P(i\omega)|^2}.$$
The nonzero interval signs prove simplicity and a direction independent of recurrence: the lower family removes two unstable roots; the upper adds two. Thus, off all critical delays,
$$U(\tau)=2-2n_-(\tau)+2n_+(\tau),\quad n_j=\#\{m\ge0:\tau_j+2\pi m/\omega_j<\tau\}.$$
For $\tau>\max(\tau_-,\tau_+)$ not critical, $n_+>(\tau-\tau_+)/P_+$ and $n_-<(\tau-\tau_-)/P_-+1$. Hence
$$U(\tau)>2\{\tau(1/P_+-1/P_-)-\tau_+/P_++\tau_-/P_-\}.$$
Since $P_+<P_-$, this is positive above the cutoff in Theorem 5.2. The cutoff exceeds both fundamental delays at every registered vector. The finite interval event list resolves the order below it without overlapping event boxes. All stable intervals are therefore identified; critical endpoints are excluded. At simultaneous events beyond the cutoff the two simple pairs can be counted together, without creating an asymptotically stable critical point. Finally,
$$U(\tau)=\frac{\omega_+-\omega_-}{\pi}\tau+O(1).$$

SPECTRAL_TABLE

The exact endpoint intervals, Routh inequalities, disk radii, cutoff bounds and complete finite event order are in `global_equilibrium_spectrum_v43.json`. This is an equilibrium spectrum result on an unbounded delay axis. It neither supplies the complete Floquet spectrum of a periodic orbit nor rules out coexisting nonlinear attractors at a stable equilibrium.

## S18. Complete protective basin: invariance, comparison and nonlinear gains

Consider
$$\dot N=rN(1-N/K)-qEN,\quad \dot Z=\{\Phi(-\dot N)-Z\}/\tau_m,$$
with $\Phi\ge0$, $|\Phi(x)-\Phi(y)|\le|x-y|$ and $\Phi(0)=\delta$. Let
$$C(Z)=E_0Z_{\rm ref}/(Z_{\rm ref}+Z),\quad b(E)=\eta_p(1-E/M).$$
The continuous/native effort law is $\dot E=b(E)(C(Z_{\rm meas})-E)$. Native review reads $Z(t_k-\tau)$ and holds that signal until $t_{k+1}$, with fixed $T_r=t_{k+1}-t_k>0$. For exact nonlinear frozen-effort review, the ecological/memory state flows with $E=E_k$ during the interval, and the command is
$$E_{k+1}=\Psi_{T_r}(E_k,C(Z_{\rm meas,k})),$$
where $\Psi$ is the exact scalar nonlinear relaxation flow, not the flow of a linearisation. Start- or end-review timing only changes the bounded measurement age; the gain proof covers either stated causal convention. Delay is fixed and finite. A bounded initial memory history is nonnegative and need not be in equilibrium.

**Invariance and persistence.** At $N=K$ the stock derivative is nonpositive; at $N=0$ it vanishes. Positive stock stays positive by the exponential variation formula. Memory is nonnegative and bounded, since $-\dot N$ is bounded on the physical stock/effort rectangle and $\Phi$ is globally Lipschitz. Since $0\le C\le E_0<M$, the interval $0\le E\le\bar E=\max(E(0),E_0)<M$ is invariant. Consequently
$$b(E)\ge b_{\min}=\eta_p(1-\bar E/M)>0.$$
Continuous/native comparison gives $\limsup E\le E_0$. The exact scalar flow satisfies
$$\Psi_T(E,C)-C=(E-C)\exp\left(-\int_0^T b(E(s))\,ds\right),$$
so it is a convex relaxation with $0<\alpha\le e^{-b_{\min}T}<1$. This proves the same upper bound and limiting effort bound for reviewed commands and their physical holds. For every sufficiently small $\varepsilon>0$, eventually $E\le E_0+\varepsilon$. Logistic comparison then gives
$$\liminf N\ge K(1-q(E_0+\varepsilon)/r).$$
Letting $\varepsilon\downarrow0$ proves $\liminf N\ge N_b>0$.

**Uniqueness.** At a positive equilibrium, $\dot N=0$, so $Z=\delta$. The effort equilibrium is $E=C(\delta)$ and the stock equilibrium follows. A fixed exact-review command must also equal its frozen quota because $\alpha<1$. No other positive rest exists.

**Asymptotic gains.** Define $n=\log(N/N^*)$, $e=E-E^*$, $z=Z-\delta$ and the positive logarithmic-mean coefficient
$$a(t)=\frac rK\frac{N-N^*}{\log(N/N^*)},\qquad a(t)=rN^*/K\text{ at }N=N^*.$$
The logarithmic mean lies between its positive arguments. Thus asymptotically $a\ge rN_b/K-o(1)$ and always $a\le r$. Also
$$\dot n=-a(t)n-qe,\qquad D=-\dot N=N\{a(t)n+qe\}.$$
All errors are ultimately bounded. Stable scalar convolution and the definition $L_x=\limsup_{t\to\infty}|x(t)|$ give
$$L_n\le\frac{qK}{rN_b}L_e,\qquad L_D\le K(rL_n+qL_e),\qquad L_z\le L_D.$$
The last step uses $|\Phi(D)-\Phi(0)|\le|D|$ and the memory filter's unit asymptotic gain. Since $|C(Z)-C(\delta)|\le L_C|Z-\delta|$, continuous/native tracking has $L_e\le L_CL_z$: outside any slightly enlarged quota-error interval, the tracking error points inward with rate at least $b_{\min}$. Every fixed bounded signal age preserves this limiting error bound after its initial history has washed out. For exact review, the same conclusion follows by iterating the convex scalar relaxation with uniform contraction factor at most $e^{-b_{\min}T_r}$.

Substitution yields
$$L_e\le qKL_C(1+K/N_b)L_e=\Gamma L_e.$$
The strict gain forces $L_e=L_n=L_z=0$.

**Stability, not only attraction.** Choose a neighbourhood of the equilibrium with $N>N_b-\varepsilon>0$, and $\varepsilon$ small enough that $qKL_C\{1+K/(N_b-\varepsilon)\}<1$. On any finite interval before a first exit, the same scalar estimates hold with suprema instead of limsups and additional terms bounded by the initial stock/effort errors and memory-history norm. Closing the strict gain bounds all three suprema by a fixed multiple of those initial errors. Sufficiently small initial errors therefore preclude the first exit. This proves Lyapunov stability. Together with the global attraction just proved, it establishes global asymptotic stability relative to the stated basin, without assuming differentiability of a general Lipschitz $\Phi$.

**Complete basin and limits.** The faces $N=0$ and $E=M$ are invariant for all three protected implementations and cannot converge to the positive equilibrium. Every other physical state with bounded nonnegative memory history is covered. Hence the basin is exact, not just an invariant subset or a finite set of histories. No nonconstant recurrent omega-limit set exists in it. The result supplies no uniform convergence rate near those excluded faces or as delay/cadence becomes arbitrarily large. Mixed/mobilising laws, Euler commands and unbounded signal ages do not inherit the proof. The inequality is sufficient, not necessary: $\Gamma\ge1$ does not itself imply failure.

**Outward constants.** At the common protective point, $E_0=E^*(1+\delta)$, $Z_{\rm ref}=1$, $E_0\approx2.2344650544$, $N_b\approx88.827674728$ and $\Gamma\approx0.474997056688$. For the box stated in the main article, interval evaluation gives $\Gamma\le0.686293596959<1$, with positive $1-qE_0/r$ and $E_0<M$ throughout. The source is `global_protective_basin_v43.py`; `global_protective_basin_v43.json` stores exact outward endpoints. The box treats $E^*$ and $\delta$ as protective-controller design coordinates and sets $E_0=E^*(1+\delta)$; it is not a fitted ecological/institutional confidence region.

## S19. Infinite-Fourier residual validation for approximate folds

Let $s=t/T$ and $\sigma=\tau/T$. Real trigonometric polynomials $U,V$ of degree 128 define exact approximate orbit and kernel functions. Their real cosine/sine coefficients, $T$, $\tau$ and $\rho$ are stored as exact decimal strings in `fold_exact_fourier_inputs_v43.json` and read directly by the validation, not inferred from a later platform FFT. Put $SU(s)=U(s-\sigma)$ and let $A=f_U(U,SU)$, $B=f_{Z_d}(U,SU)$. The orbit and kernel residuals are
$$R=U_s-Tf(U,SU),$$
$$Q=V_s-T\{AV+B\,SV_Z\}-\rho f(U,SU)-(\tau/T)\rho B\,S(U_Z)_s.$$
Here $\rho$ is the period component of the null vector, and $B$ is a column acting on the delayed memory only. The sign of the last term follows by differentiating $U(s-\tau/T)$ with respect to period. The phase constraints are the sine-mode integrals of $U_N$ and $V_N$. For kernel normalisation, fix its first $N$ cosine coefficient to its nonzero exact baseline value (0.4701250465138572 for the lower fold and 0.1851445547935097 for the upper). This affine normalisation has zero residual by definition, and does not assert nullity of a true continuum operator.

### S19.1 Analytic strip bounds

For $u=a_0+\sum_{j=1}^m(a_j\cos2\pi js+b_j\sin2\pi js)$ on $|\operatorname{Im}s|\le\alpha$, use
$$|u|\le|a_0|+\sum_j(|a_j|+|b_j|)\cosh(2\pi j\alpha),$$
$$|\operatorname{Im}u|\le\sum_j(|a_j|+|b_j|)\sinh(2\pi j\alpha),\quad |u_s|\le\sum_j2\pi j(|a_j|+|b_j|)\cosh(2\pi j\alpha).$$
Real shifts preserve the strip. For $D=qNE-rN+(r/K)N^2$, these bounds enclose $|D|$ and $|\operatorname{Im}D|$. The test $\kappa|\operatorname{Im}D|<\pi/2$ puts $1+e^{\kappa D}$ in the open right half-plane, proving analyticity of the principal softplus and bounding the complex sigmoid by one. A positive lower bound on $\operatorname{Re}(1+Z)$ excludes the rational pole. The softplus magnitude is bounded by
$$|\kappa^{-1}\log(1+e^{\kappa D})|\le\kappa^{-1}\log(1+e^{\kappa|D|})+\pi/(2\kappa).$$
Polynomial/rational differentiation then gives component bounds $M_{f,j}$ for $f$ and $M_{h,j}$ for $h=T(AV+B\,SV_Z)+\rho f+(\tau/T)\rho B\,S(U_Z)_s$. The accepted widths are $\alpha=0.008$ (lower) and $0.006$ (upper). All inequalities are evaluated with outward interval arithmetic at 70 decimal digits; coefficient and derivative bounds are recorded in `fold_continuum_stage_v43.json`.

### S19.2 Complete residual norm, not just an off-grid sample

For an analytic periodic component bounded by $M$ on the strip, Cauchy's estimate gives $|\widehat f_k|\le M e^{-2\pi\alpha|k|}$. A trapezoidal DFT with $L$ equispaced samples aliases only modes $k+\ell L$, so for $|k|<L/2$,
$$\left|\widehat f_k-\widehat f^{\rm DFT}_k\right|\le\frac{2M e^{-2\pi\alpha(L-|k|)}}{1-e^{-2\pi\alpha L}}.$$
The radix-2 interval FFT evaluates the exact-decimal polynomials at $L=4096$ interval-enclosed roots of unity, evaluates $f,h$ by interval complex arithmetic, and computes interval DFT coefficients. Both evaluation and transform rounding are enclosed; an ordinary floating FFT is not used to certify these coefficients.

With $K_F=2047$ and $\nu=1.001<e^{2\pi\alpha}$, add each finite coefficient modulus, weighted by $\nu^{|k|}$, its alias bound, and the full omitted tail. For example,
$$\|R_j\|_{1,\nu}\le\sum_{|k|\le K_F}\nu^{|k|}\left(|2\pi i k\widehat U_{j,k}-T\widehat f^{\rm DFT}_{j,k}|+T A_{j,k}\right)+\frac{2TM_{f,j}(\nu e^{-2\pi\alpha})^{K_F+1}}{1-\nu e^{-2\pi\alpha}}.$$
The kernel bound has $M_h$ in place of $TM_f$. The derivative-polynomial coefficients vanish beyond degree 128, so this tail contains every remaining residual mode, including the omitted Nyquist pair. Interval arithmetic uses 65 decimal digits and endpoints are serialised by exact binary-to-decimal outward integer rounding, not nearest formatting.

FOURIER_TABLE

The orbit and kernel phase residuals are respectively at most $1.217\times10^{-15}$ and $2.592\times10^{-18}$ (lower), and $6.978\times10^{-15}$ and $2.376\times10^{-17}$ (upper). These phase-variable norms differ from the physical-time off-grid defects. The exact coefficient strings and componentwise bounds are in `interval_fourier_residual_v43.json`; its source implements the alias/tail proof above.

### S19.3 What remains for continuum existence

A residual inclusion is a rigorous statement about an explicitly specified approximate polynomial; it is not a zero inclusion. A complete bordered fold validation additionally needs a controlled inverse including the finite/infinite coupling, a nonlinear contraction or radii inequality, and enclosed continuum transversality/curvature. Varying period/delay changes the shift and can lose derivatives in a naive fixed Wiener-space formulation; a proof must use appropriate smoothing, analytic-strip loss or a regularised formulation. Neither the finite Krawczyk box nor finite Arnoldi multipliers supplies these estimates. The discrepancy of about $5.5\times10^{-7}$ between the upper finite $m=64$ certificate and the 257-point approximation is therefore important discretisation information, not a contradiction between certificates of the same system. Continuum existence and complete periodic Floquet spectra remain unproved.

## S20. Assessment-based dynamic tests and negative endpoints

### S20.1 Data, observation gauge and temporal support

ICES SAG stock `her.27.3a47d`, assessment 2025, key 19373 provides total biomass, its reported low/high values, catch, recruitment and age-2--6 fishing pressure. Raw StockDownload, SummaryTable and StockSettings JSON responses, the stock metadata and the cleaned table are archived. The API's total-biomass unit field is blank, whereas catch units are tonnes. Accordingly the proxy
$$N=B/B_{\rm med},\quad U=(C/C_{\rm med})/N$$
is invariant to separate unit rescaling of biomass and catch and is not interpreted as an absolute $qE$. Reference medians use 1950--1994 only. SSB and reported age-specific fishing pressure are not substituted for total biomass or removal. The incomplete terminal 2025 row is excluded; all test targets are completed years through 2024. The assessment is a single retrospectively revised vintage, not independent annual observations or real-time assessments.

The initial computation used target years 1951--1994 for training but silently lost early targets differently across lag candidates. After inspecting its outputs, the support error was corrected by common training targets 1960--1994, giving every candidate observed lagged predictors. Validation remains 1995--2009 and test remains 2010--2024. The initial results are retained under `initial_unequal_support_...`; the post-inspection amendment is explicit in `ANALYSIS_PROTOCOL_v43_P02.md`. Thus this is a transparent retrospective analysis, not external preregistration or an untouched confirmatory holdout. Secondary ecological/recursive diagnostics were specified after that initial response test and before their own estimation and remain exploratory.

### S20.2 Response laws and selection

For $D_y=N_{y-1}-N_y$, memory is
$$Z_y=e^{-1/t_m}Z_{y-1}+(1-e^{-1/t_m})\log(1+e^{10D_y})/10,$$
initialised in 1947 at $\log(2)/10$. Origin year $y$ predicts $U_{y+1}$ with $Z_{y-\ell}$ held throughout the one-year scalar flow. The mobilising law is
$$\dot U=(1-U/M)\{\eta U(Z-U/M)+d_0Z/(1+Z)\};$$
the protective law is
$$\dot U=(1-U/M)\eta_p\{fM/(1+Z)-U\},\quad0<f<1.$$
Both have two continuously fitted coefficients. Candidate memory times are $\{0.25,1,2,5,10\}$, integer lags $0,\ldots,12$, and cap multipliers $\{1.05,1.5,2,4\}$, giving 260 candidates per law. The cap is the fixed multiplier times the maximum origin proxy in the fitting period; its deterministic reference maximum is recomputed for the pretest refit, not selected using the test. Training least squares estimates the two coefficients; validation RMSE selects the discrete candidate; the two coefficients are refitted on all 50 pretest targets. Test performance never selects a hyperparameter. Bounded local least squares starts from nonnegative least-squares fits of the first-order rate approximation; it does not certify a global parameter optimum. Response rates are bounded above by 20, with positive lower bounds of $10^{-7}$ for adjustment rates and $10^{-8}$ for the mobilising additive coefficient; the protective cap fraction lies in $[10^{-6},0.999999]$. Full solver tolerances and candidate diagnostics are in the executable source and grid.

The common-support selection is $(t_m,\ell,M/\max U)=(0.25,5,4)$ for mobilising and $(0.25,2,1.05)$ for protective. The fitted lags are tuning values, not estimates of deployment delay. Scalar RK4 uses 64 substeps/year and is checked at 128; maximum central prediction discrepancies are below $6\times10^{-13}$. Persistence and affine AR(1) use exactly the same target support. Catch intensity derives partly from the stock variable driving the signal, and stock/catch share an age-structured assessment; neither predictor independence nor direct observation of effort is assumed.

RESPONSE_TABLE

The mobilising additive coefficient is near its positive lower bound $10^{-8}$; this is not an interior well-identified fit. The protective central RMSE is about 13.5% below persistence but only 0.47% below AR(1), on 15 dependent annual targets. The low/high biomass paths are coherent stress scenarios, not independent observations, a simultaneous confidence set or replication. They cannot establish a robust causal mechanism from such a small gain.

### S20.3 Ecological competitor and recursive sampled surrogate

A secondary observed-input ecological model has exact held-input annual flow
$$\dot N=(r-hU)N-bN^2+\beta R_{y-g},\quad r,b,h>0,\quad\beta\ge0,$$
where $R$ is recruitment normalised by its 1960--1994 median. The logistic model sets $\beta=0$; the competing augmented model selects $g\in\{1,2,3\}$ by validation and refits on pretest targets. Coefficient $h$ absorbs the observation gauge; it is not assumed to be a measured absolute removal coefficient. The exact Riccati solution, not an Euler stock step, is fitted by least squares. Lag-one recruitment is selected, reducing test error markedly, but the resulting stock prediction still fails both baselines. Neither the scalar-logistic ecology nor an institutional interpretation is rescued by the response-only fit.

The exploratory recursive annual surrogate starts from the observed 2009 $N,U$ and pre-2010 memory history. With logistic parameters fitted on pretest data, each future step (i) flows stock for one year with $U_y$ held, (ii) updates the scalar effort command from start-year delayed memory using its exact-to-numerical-accuracy scalar flow, and (iii) updates memory from the modelled stock decline. No future observed stock, catch or recruitment enters. This particular causal sampled surrogate is not claimed identical to the continuous DDE or the flow-then-end-review operator in the local theorem. Its comparator is recursively iterated affine VAR(1) fitted to $(N,U)$ on the same pretest targets; persistence is the constant 2009 state, not annually refreshed persistence. Componentwise one-step and recursive metrics are therefore distinct endpoints.

STOCK_TABLE

RECURSIVE_TABLE

Both recursive stock paths fail persistence and VAR(1). The protective proxy path beats both, but cannot validate a joint mechanism whose stock path fails. The fitted protective global sufficient gain is approximately 2.31309, outside Theorem 7.5; exceeding one is not a proof of instability. The source scripts, complete grids, pointwise predictions, domain checks and raw-data hash are supplied. No uncertainty envelope is presented as repeated field evidence, and no theoretical delay threshold is transported to herring. The result is a reproducible field challenge to the scalar ecology and a small conditional response advantage, not full dynamic field validation.

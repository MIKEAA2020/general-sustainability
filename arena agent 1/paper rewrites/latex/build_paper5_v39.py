"""Build paper5 v39 main tex from v38: remaining-audit-points incorporation +
rejected-research execution (sensitivity battery, F-grid, NS verification,
alternative-band screens, computed Figures 3-5)."""
import re

SRC = '/home/user/paper5_v38/paper5_sampled_governance_v38.tex'
DST = '/home/user/paper5_v39/paper5_sampled_governance_v39.tex'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:220]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

def repw(old_joined, new, tag):
    global s
    pat = re.compile(re.escape(old_joined).replace(r'\ ', r'\s+'))
    ms = pat.findall(s)
    assert len(ms) == 1, f'{tag}: count={len(ms)}\n---\n{old_joined[:220]}'
    s = pat.sub(lambda _: new, s, count=1)
    print(f'{tag}: OK (flex)')

# V version comment
rep('% The decision clock (paper 5, revision v38): venue-synthesis Nature Sustainability elevation (title, abstract, Box1-to-S1, extractive grounding, cross-sector clock, conceptual Figure 1, regimes Box, advice chain, 4.8 design principles, subsidies/UNFCCC refs) with line numbers for review.',
    '% The decision clock (paper 5, revision v39): remaining-audit-points incorporation and rejected-research execution (sensitivity battery, F-reparameterisation grid, Neimark-Sacker verification, alternative-band screens, computed Figures 3-5, Table-3 completion) with line numbers for review.',
    'V-version')

# M1 H0 positivity
repw(r'(H0) \(r,K,q,E_{\max},\tau_m>0\).',
     r'(H0) \(r,K,q,E_{\max},\tau_m,Z_{\rm ref},\Delta_{\rm ref}>0\).',
     'M1-H0')

# M2 protective saturation
repw(r'reviewed through the same projection \(\Pi_{[0,E_{\max}]}\).',
     r'reviewed through the same projection \(\Pi_{[0,E_{\max}]}\). At \(E=0\) the law commands \(\eta_p E_{\rm cap}(Z)>0\), so zero effort is not absorbing; saturation at \(E_{\max}\) is through the gate and the projection.',
     'M2-saturation')

# M3a linear detrend
repw('coefficient by lag-1 autocorrelation of the detrended series',
     'coefficient by lag-1 autocorrelation of the linearly detrended series',
     'M3a-detrend')

# M3b Lomb-Scargle settings
repw('200 replicates, seed 7, detrending inside each replicate)',
     r'200 replicates, seed 7, detrending inside each replicate; Lomb-Scargle on 1,500 frequencies from \(1/(2\cdot{\rm span})\) to 0.5 yr\(^{-1}\))',
     'M3b-LS')

# M3c band verdict independence
repw('and D (14--30 yr, trend/regime).',
     'and D (14--30 yr, trend/regime). No multiplier-crossing verdict depends on the archived diagnostics.',
     'M3c-bands')

# M4 formal power definition
repw('and apply the same band-power statistic (the conventional power-analysis framing of Cohen, 1988).',
     r'and apply the same band-power statistic. Formally the reported power is \(P({\rm reject}\mid{\rm injected\ signal})\) at the 5\% level over the design grid (the conventional power-analysis framing of Cohen, 1988).',
     'M4-power')

# M5 exact map definition
repw(r'is the exponential update (the exact update) \(e_{n+1}',
     r'is the exponential update (the exact update; its review map the exact map) \(e_{n+1}',
     'M5-exactmap')

# M6a evidential gap
repw('No candidate satisfied all four criteria after primary-source and station-level review.',
     'No candidate satisfied all four criteria after primary-source and station-level review. The zero count is an evidential gap, not a disconfirmation: it records that no unconfounded oscillator was found, not that none exists.',
     'M6a-gap')

# M6b anchoveta guard
repw('so the unclassified controller prevents that comparison from testing the mechanism.',
     'so the unclassified controller prevents that comparison from testing the mechanism. The 3.7 yr catch periodicity is not a review interval.',
     'M6b-anchoveta')

# M7 cod guard
repw("The case's positive content is a descriptive partition.",
     "The case's positive content is a descriptive partition, offered as a consistency check of the assessment-window mechanics rather than an empirical rejection of scalar autonomous or single-driver dynamics.",
     'M7-codguard')

# M8a 4.1 interpretation-first
repw("are the paper's core methodological finding. The same feedback loop",
     "are the paper's core methodological finding. Stability windows are operator-specific: they do not transfer across review-map operators. The same feedback loop",
     'M8a-41-conclusion')

# M8b 4.1 trim repeated numbers
repw('The complete crossing record sharpens the operator finding: On one plant the exact update has exactly one crossing (extractive, 6.501 yr) and none (protective), while the Euler update reports artefact bands.',
     'The complete crossing record sharpens the operator finding: on one plant the exact and Euler updates disagree on the number and location of crossings (Section 3.4).',
     'M8b-41-trim')

# M9 Table 4 CE/CZ row
repw(r'\(C_E\), \(C_Z\) & linearised protective gains',
     r'\(C_E\), \(C_Z\) & linearised effort-law coefficients (per channel; protective values in Section 2.1)',
     'M9-T4row')

# M10 Table 3 caption + new rows
repw('No value here is newly computed; the baseline-core vector is printed here, with the code constants block pinned per row,',
     'No value here is newly computed except the linearised-gains, crossing-angle, eigenvalue, and solver rows, which are computed in Supplementary S11; the baseline-core vector is printed here, with the code constants block pinned per row,',
     'M10a-T3caption')
rep('Stage reconstruction & class natural mortality',
    r'''Logistic hold-map core & linearised mobilising gains \((C_E, C_Z)\) & \((-0.059518, +1.785019)\) & Supplementary S11 (sensitivity battery) \\
Logistic hold-map core & crossing angle \(\theta_0\) (exact map, 6.501 yr) & 0.175494 rad & Supplementary S11 \\
Logistic hold-map core & continuous eigenvalues \(\lambda\) (undelayed loop) & \(-0.278147\), \(+0.000360\pm0.027683i\) & Supplementary S11 \\
Logistic hold-map core & derivative construction & closed-form monodromy (no finite differences) & Section 3.4 \\
Logistic hold-map core & solver; precision; grid check & matrix exponential (\texttt{expm}); IEEE-754 double; 2k/20k/200k scans identical & Supplementary S11 \\
Stage reconstruction & class natural mortality''',
    'M10b-T3rows')

# M11 Section 3.4 research block (appended at section end)
BLOCK34 = r'''Three verification records qualify the crossing record. First, a one-at-a-time sensitivity battery perturbs each baseline parameter (\(r\), \(K\), \(q\), \(E_{\max}\), \(\eta\), \(\delta_0\), \(Z_{\rm ref}\), \(\Delta_{\rm ref}\), \(\tau_m\), \(\delta\)) by \(\pm 5\%\) and \(\pm 10\%\), reproducing all eight committed values before extension (Supplementary S11). The exact-map crossing is highly sensitive to \(r\), \(K\), \(q\), \(E_{\max}\), \(\eta\), and \(\Delta_{\rm ref}\) --- several \(\pm 10\%\) cells remove the crossing or move it past 13 yr --- moderately sensitive to \(\tau_m\), affected by \(\delta\) (removed at \(-10\%\)), and insensitive to \(\delta_0\) and \(Z_{\rm ref}\) (crossing moves \(< 0.07\) yr). The protective channel is stable in every battery cell (maximum \(\rho = 0.9971\)), so the channel contrast survives uniform \(\pm 10\%\) perturbation. The spectral-radius curves for all four update--channel combinations are Figure~\ref{fig:rho-scan}.

Second, the equilibrium fishing mortality \(F^* = qE^*\) organises the \(q\)-sensitivity: \(q\) and \(E_{\max}\) perturbations act on the crossing almost entirely through \(F^*\) (\(q \times 1.05\) and \(E_{\max} \times 1.05\) give \(F^* = 0.00219\) with crossings at 13.797 and 13.790 yr respectively; \(\times 1.10\) gives 18.377 and 18.367 yr), and a decade-spanning \(q\) grid shows review-instability turning on as \(F^*\) rises through the baseline 0.00209, with the equilibrium infeasible (\(N^*<0\)) once \(F^*>r\) (Supplementary S11).

Third, the 6.501 yr crossing is a verified Neimark--Sacker bifurcation of the nonlinear sampled map: the finite-difference Jacobian matches the monodromy to \(10^{-6}\), the crossing is transversal (\(d|\mu|/dT_r = -0.000683\)) and non-resonant through fourth order, and the first Lyapunov coefficient is sign-definite across a sevenfold finite-difference step range (\(a(0) \approx -0.0008\), supercritical). Long-horizon iterates rotate at the predicted frequency (rotation number 0.027--0.029 against \(\theta_0/2\pi = 0.0279\)); the invariant circle itself is not directly exhibited because convergence at \(|\rho-1| \sim 10^{-4}\) is too slow for the tested horizons (Supplementary S11).

\begin{figure}[htbp]
\centering
\includegraphics[width=0.9\linewidth]{../figs_p5/fig_rho_scan_v39.png}
\caption{Spectral radius \(\rho(T_r)\) against review interval at the baseline parameter vector (Table 3) for the four update--channel combinations. Horizontal line: the unit circle; dotted verticals: the 6.501, 47.536, 79.143, and 2.306 yr crossings and the annual review (1 yr). The exact mobilising curve crosses once; the Euler mobilising curve reports two artefact crossings; the exact protective curve never reaches unity.}
\label{fig:rho-scan}
\end{figure}

\subsubsection{3.5'''
rep(r'\subsubsection{3.5', BLOCK34, 'M11-S34block')

# M12 Section 3.5 alternative-band sentence + Figure 4
BLOCK35 = r'''The screen's zero count holds under exploratory alternative bands: a broad 2--10 yr band, management-cadence bands (1--3, 3--8, 8--20 yr), and an 8--80 yr effort-proxy band all return zero Benjamini--Hochberg-significant cells, with the effort-proxy band unresolvable (record span below three upper periods) on all 42 records (Supplementary S11). Figure~\ref{fig:screen} shows the baseline \(q\)-value distribution and per-stock null excess.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.9\linewidth]{../figs_p5/fig_screen_v39.png}
\caption{Baseline screen diagnostics. Left: Benjamini--Hochberg \(q\)-values over the 84 target-band cells (dashed line: 0.05; no cell significant). Right: per-stock band power relative to the 95\% per-stock AR(1) threshold in bands A and B (horizontal line: unity).}
\label{fig:screen}
\end{figure}

\subsubsection{3.6'''
rep(r'\subsubsection{3.6', BLOCK35, 'M12-S35fig')

# M13 Section 3.8 Figure 5 (appended at section end, before Discussion)
BLOCK38 = r'''Figure~\ref{fig:cod} plots the Table-2 SSB and mortality series against the two windows.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.9\linewidth]{../figs_p5/fig_cod_v39.png}
\caption{Northern cod Table-2 series by window. Black: spawning stock biomass; red steps: instantaneous natural mortality; shaded: the crash (1991--1995) and non-recovery (1995--2015) windows.}
\label{fig:cod}
\end{figure}

\subsection{4'''
rep(r'\subsection{4', BLOCK38, 'M13-S38fig')

# M14 cod fluctuation correction (report count)
for old1015 in ('10--15 yr fluctuation', '10\u201315 yr fluctuation'):
    c = s.count(old1015)
    s = s.replace(old1015, 'post-1995 variability (coefficient of variation 0.37--0.39) with no dominant spectral peak (Supplementary S11)')
    print(f'M14-1015 {old1015!r}: replaced {c}')

print('len delta:', len(s) - n0)
import os
os.makedirs('/home/user/paper5_v39', exist_ok=True)
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)

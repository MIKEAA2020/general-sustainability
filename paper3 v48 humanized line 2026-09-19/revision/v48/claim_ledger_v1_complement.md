# The complement of the claim ledger: what it did not read

The ledger speaks about 719 sentences. This is the rest of the draft, so that the counts in `claim_ledger_v1.md` can be read as a statement about the document and not only about a sample of it. Nothing here is judged; it is listed with the reason it is out.


| class | count |
|---|---|
| draft body blocks the extractor kept | 292 |
| kept blocks that produced no row at all | 8 |
| sentences extracted and then left out | 7 |, of which 0 carry a figure or a citation
| blocks of the file never read as prose | 233 |


## The sentences extracted and left out

Those marked as carrying a figure or a citation are the ones worth a glance: an excluded sentence that states a number is the only kind of exclusion that could hide a contradiction.

- `D0047` §1.1 · left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind

  > Each is informative about something.
- `D0159` §1.2 · left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind

  > Contributions, with each one's status.
- `D0177` §1.3 · left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind

  > Section 7 supplies first-passage semantics.
- `D0341` §3.5 · left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind

  > Theorem 5 (Flux-bounding envelopes). *Assume:*
- `D0420` §4.8 · left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind

  > Two obligations ride the theorem.
- `D0478` §6.1 · left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind

  > Definition 4 (Local net-depletion ratio).
- `D0531` §6.5.2 · left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind

  > Groundwater (G3P v1.12 basin series).

## Blocks of the draft never read as prose, and why

- prose with no sentence of six words or more: 147
- a heading: 59
- the reading note at the head of the file: 15
- a table, display or code block: 7
- back matter: 4
- author line or front matter: 1

<details><summary>the first 40, so the classification can be checked</summary>

> *a heading* — # Typed Flux Ledgers and Depletion Arithmetic ### Conservation, componentwise diagnostics, and the semantics of depletion horizons
> *author line or front matter* — *Amin Abaee — Independent Researcher — ORCID 0000-0002-0019-1842 — amin_abaee@ut.ac.ir — 6 September 2026*
> *the reading note at the head of the file* — > **How to read this version.** This is a plain-language rendering of the article. The argument, the numbers, the tables, the named examples and every stated limit are th
> *prose with no sentence of six words or more* — ---
> *a heading* — ## Abstract — in plain words, then in the author's terms
> *the reading note at the head of the file* — > **[Editor's note — flagged for the author, not their claim.]** The abstract's "flux-reconstruction identity" says unobserved *fluxes* are recovered from observed *stock
> *prose with no sentence of six words or more* — ---
> *a heading* — # 1. Introduction
> *a heading* — ## 1.1 Two ways this kind of accounting goes wrong
> *a heading* — ## 1.2 What this article builds, and what it refuses to
> *a heading* — ## 1.3 How the article is organised
> *the reading note at the head of the file* — > **In plain words.** This section builds the ledger. Four rules do all the work. (1) Every box holds one named material in one named place, with one unit. (2) Nothing mo
> *a table, display or code block* — | Symbol | Means | Where | |---|---|---| | $N$ | living stock; nutrient stock *(local to §2.4)* | §2.2; §2.4 | | $S^{\top}$ | typed stoichiometric (incidence) operator | 
> *a heading* — ## 2.1 Typed stocks, primitive fluxes, and the incidence discipline
> *prose with no sentence of six words or more* — A ledger state $x\in\mathbb{R}^m_+$ collects compartments, and each entry carries a material identity, a spatial support and a physical unit. Internal dynamics use non-ne
> *prose with no sentence of six words or more* — $$\dot x = S^{\top} v(x,y,\theta) + B\,u_\partial(t) + d\,x(t),\qquad v\ge 0 \tag{1}$$
> *prose with no sentence of six words or more* — If $L^{\top}S^{\top}=0$, then $\tfrac{d}{dt}(L^{\top}x) = L^{\top}B u_\partial + L^{\top}dx$: one conservation law per conserved moiety and boundary. That identity does *
> *prose with no sentence of six words or more* — 1. $dx$ must itself be typed. A physical disturbance on represented material is a different object from a structural discrepancy term. 2. $S^{\top}$ may contain signed en
> *a heading* — ## 2.2 The closed finite-donor ledger
> *prose with no sentence of six words or more* — $$s=\frac{A_{\mathrm{act}}}{A_{\mathrm{act}}+A_0}\ (\text{support factor}),\qquad \sigma=\frac{A_{\mathrm{geo}}}{A_{\mathrm{geo}}+A_{g0}}\ (\text{donor fraction}),$$ $$R(
> *prose with no sentence of six words or more* — $R$ is net regeneration — how much new living stock appears. $T$ is gross uptake — how much mineral the living stock pulls in. $B$ is gross turnover: everything the biota
> *prose with no sentence of six words or more* — $$e_{GA}=\omega_A A_{\mathrm{eq,intrinsic}}\,\sigma,\qquad e_{AG}=\omega_A A_{\mathrm{act}},\qquad C_{A,\mathrm{lim}}=C_A\sigma,\qquad \gamma_U U\ \text{(detritus return)
> *a table, display or code block* — | Recharge law | Form | Status | |---|---|---| | **Primitive donor-limited exchange** | $e_{GA}=\omega_A A_{\mathrm{eq,intrinsic}}\sigma$ | The closed block's law (§2.2).
> *prose with no sentence of six words or more* — $$\dot N=R-qEN,\qquad \dot A_{\mathrm{act}}=-B+e_{GA}-e_{AG}+\gamma_U U,$$ $$\dot A_{\mathrm{geo}}=-e_{GA}+e_{AG},\qquad \dot U=T-\gamma_U U. \tag{2}$$
> *prose with no sentence of six words or more* — This comes with a **memory–effort pair** $(Z,E)$ driven by $qEN-R$ — never by mining; $q$ is the per-effort extraction coefficient of the harvest law. The pair is the reg
> *prose with no sentence of six words or more* — The block's harvest routing is the $\alpha=0$ corner of §2.3: harvest $qEN$ leaves the natural block entirely as product. A positive detritus-routed fraction $\alpha>0$ w
> *prose with no sentence of six words or more* — The **registered parameterization** is
> *prose with no sentence of six words or more* — $$r=0.02,\quad K=100,\quad q=0.001,\quad \kappa_A=0.05,\quad \omega_A=10^{-3},\quad A_0=1,\quad A_{\mathrm{eq,intrinsic}}=50,\quad \gamma_U=0.2.$$
> *prose with no sentence of six words or more* — The geological half-saturation $A_{g0}$ is declared positive (for smoothness of $\sigma$) under the separation-of-scale condition $A_{\mathrm{geo}}\gg A_{g0}$, a regime i
> *prose with no sentence of six words or more* — With $A_0>0$ and $A_{g0}>0$ the right-hand side of (2) is locally Lipschitz on the closed orthant, and the comparison $\dot N\le rN(1-N/K)$, with $\dot N\le0$ once $N\ge 
> *prose with no sentence of six words or more* — $$\dot M=-qEN-C_{A,\mathrm{lim}},\qquad M=N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U,$$
> *a heading* — ## 2.3 The six-compartment illustration
> *prose with no sentence of six words or more* — $$\dot z=S(\alpha,\rho_P)\,v(z,u),\quad z=(X,U,A,G,P,W)^{\top},\quad v=(g,m,h,d_U,e_{GA},e_{AG},c_G,r_P)^{\top},$$
> *prose with no sentence of six words or more* — $$S(\alpha,\rho_P)=\begin{pmatrix} 1&-1&-1&0&0&0&0&0\\ 0&1&\alpha&-1&0&0&0&\rho_P\\ -1&0&0&1&1&-1&0&0\\ 0&0&0&0&-1&1&-1&0\\ 0&0&1-\alpha&0&0&0&1&-1\\ 0&0&0&0&0&0&0&1-\rho
> *a heading* — ## 2.4 The four-stock resource–sink–nutrient–product system
> *prose with no sentence of six words or more* — $$\dot{\mathsf S}=g(\mathsf S,\mathsf N)-H,\qquad \dot{\mathsf K}=\theta_K H-\theta_\delta \mathsf K,$$ $$\dot{\mathsf N}=-g(\mathsf S,\mathsf N)+\theta_\delta\mathsf K+I
> *prose with no sentence of six words or more* — where $\theta_K$ is the sink-generation fraction, $\theta_\delta$ the assimilation rate, $I_{\mathsf N}$ external nutrient input and $Q_{\mathsf P}$ product disposal. Add
> *prose with no sentence of six words or more* — $$\frac{d}{dt}(\mathsf S+\mathsf K+\mathsf N+\mathsf P)=I_{\mathsf N}-Q_{\mathsf P},$$
> *prose with no sentence of six words or more* — 1. **No assimilation** ($\delta\equiv0$). Then $\dot{\mathsf K}\ge w(H_{\min})>0$, and the sink exceeds any finite ceiling $K_{\max}$ in finite time. 2. **Weak assimilati
> *a heading* — ## 2.5 Mechanism typing: routing is never determined by diagnostic labels

</details>


## Kept prose blocks that produced no ledger row

These are blocks the extractor read and the ledger then had nothing to say about: usually a block of two- and three-word list items, where every candidate was below the six-word floor.

> block 9 — Each is informative about something. None is what it is usually taken to be.
> block 35 — **Contributions, with each one's status.**
> block 61 — rNs rN²s/K qEN T γ_U U e_GA e_AG C_A,lim N 1 −1 −1 0 0 0 0 0 A_act −1 1 0 −1 1 1 −1 0 A_geo 0 0 0 0 0 −1 1 −1 U 0 0 0 1 −1 0 0 0
> block 113 — **Theorem 5 (Flux-bounding envelopes).** *Assume:*
> block 116 — *and the envelopes , . Then for all and all .*
> block 180 — **Definition 4 (Local net-depletion ratio).**
> block 204 — **Groundwater (G3P v1.12 basin series).**
> block 274 — while . The pair is the witness for .
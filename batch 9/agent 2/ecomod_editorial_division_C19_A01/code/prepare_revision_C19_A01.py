"""Build C19 main/SI sources from frozen C18 sources.

The transform is deliberately exact-anchor based: every expected source record or
paragraph must occur once. It changes reference metadata and editorial division
only; it does not generate or alter numerical results.
"""
from pathlib import Path
import difflib
import json
import re

R = Path(__file__).resolve().parents[1]
OLD = R / "inherited_C18"


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def replace_span(text, start, end, new, label):
    if text.count(start) != 1 or text.count(end) != 1:
        raise RuntimeError(f"{label}: span anchors are not unique")
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + new + text[j:]


def replace_bibitem(text, key, record):
    pattern = rf"(?m)^\\bibitem\[\{{Abaee\(2026{key[-1]}\)\}}\]\{{{key}\}}.*$"
    matches = re.findall(pattern, text)
    if len(matches) != 1:
        raise RuntimeError(f"{key}: expected one bibliography record, found {len(matches)}")
    return re.sub(pattern, lambda _match: record, text, count=1)


RECORDS = {
    "Abaee2026a": r"\bibitem[{Abaee(2026a)}]{Abaee2026a} Abaee, A. (2026a). \emph{Governance Delay and the Stability of Harvested Stocks: Mobilising and Protective Feedback Rules, and the Review Interval as a Design Parameter}. Preprints.org preprint (version 1, posted 30 October 2026). \url{https://doi.org/10.20944/preprints202610.3095.v1}.",
    "Abaee2026b": r"\bibitem[{Abaee(2026b)}]{Abaee2026b} Abaee, A. (2026b). \emph{Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules}. Preprints.org preprint (version 1, posted 29 October 2026). \url{https://doi.org/10.20944/preprints202610.2983.v1}.",
    "Abaee2026c": r"\bibitem[{Abaee(2026c)}]{Abaee2026c} Abaee, A. (2026c). \emph{Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons}. Preprints.org preprint (version 1, posted 30 October 2026). \url{https://doi.org/10.20944/preprints202610.3123.v1}.",
}


def use_content_based_companion_locators(text, include_ledger):
    """Avoid carrying unverified numbering from older companion working versions."""
    text = replace_once(
        text,
        r"\citep[Sections~2 and 4 of][]{Abaee2026b}",
        r"\citep{Abaee2026b}",
        "transition companion section locator",
    )
    text = replace_once(
        text,
        r"(Theorem~2 in \citet{Abaee2026b})",
        r"(compensatory-acceptance result in \citealt{Abaee2026b})",
        "transition companion acceptance-result locator",
    )
    text = replace_once(
        text,
        r"Theorem~4(iii) in \citet{Abaee2026b}",
        r"The diagonal-gap analysis in \citet{Abaee2026b}",
        "transition companion diagonal-gap locator",
    )
    if include_ledger:
        text = replace_once(
            text,
            r"\citep[Sections~1.1 and 10.1]{Abaee2026c}",
            r"\citep{Abaee2026c}",
            "ledger companion section locator",
        )
    return text


def transform_main(text):
    for key in RECORDS:
        text = replace_bibitem(text, key, RECORDS[key])
    text = use_content_based_companion_locators(text, include_ledger=True)
    text = replace_once(
        text,
        "ecomod_audit_remediation_C18_A01",
        "ecomod_editorial_division_C19_A01",
        "data availability URL",
    )
    text = replace_once(
        text,
        r"Symbols and units are listed in SI~\S S1.",
        r"SI Table S1 lists symbols and units.",
        "explicit SI Table S1 citation",
    )

    numerical = r"""We integrate the delay equations by the method of steps with explicit first-order Euler updates. Current states are read at the preceding node; time-dependent inputs and delayed values are evaluated at the new time, with linear interpolation of the delayed $q$ and $B$ histories. The delayed quality velocity is projected before each update, followed by clipping to $K_q$ as a finite-step safeguard. Reserve area is reconstructed from total-area conservation, the positive-part operator is exact, and the stated bounds on $A_c,A_f,q,P,D,$ and $K$ are enforced. The reserve threshold is monitored rather than projected, and the optional fast-land ceiling is inactive. Baseline demonstrations and threshold bisections use $\Delta t=0.05$\,yr; broader drawdown sweeps use $0.1$\,yr, with selected thresholds rechecked at $0.05$\,yr.

Pre-run histories cover the full longest active delay window, $[-\max\{\tau_g,\tau_p\},0]$, with $q(s)=q_0$ and $B(s)=B_0$ calculated from the initial state. In the matched technology-wave experiment, both runs share the no-wave prehistory; the active $T_b(0)$ changes current $B(0)$, and later wave-adjusted $B$ values enter the delayed carrying-capacity input. SI~\S S3 gives the complete node convention and state constraints.

Enumerated checks in SI~\S S3 show exact agreement between post-Euler clipping and explicit pre-update projection in the tested cases and smaller state differences under timestep refinement; they do not provide a universal error bound. SI Table S2 reports the current-quality comparator $G_c(q(t))$ only as a sensitivity check. All reported baseline trajectories use the selected projected delayed-quality law in Eq.~\eqref{eq:q}.

"""
    text = replace_span(
        text,
        "We integrate the delay equations by the method of steps",
        r"\section{Results}",
        numerical,
        "concise main numerical implementation",
    )

    text = replace_once(
        text,
        "At any given quality level, that contribution changes linearly with $A_c$; it has no interior maximum with respect to area.",
        "At any given quality level, that contribution changes linearly with $A_c$; it has no interior maximum with respect to area. SI Table S7 summarizes the composition-premium, neutrality and discount regimes.",
        "explicit SI Table S7 citation",
    )
    text = replace_once(
        text,
        r"Across the tested fast-land yields, $\lambda_1$ shifts only from $-0.0522$ at $b_f=0.60$ to $-0.0556$\,yr$^{-1}$ at $b_f=2.00$ and never changes sign (Table~\ref{tab:model}a).",
        r"Across the tested fast-land yields, $\lambda_1$ shifts only from $-0.0522$ at $b_f=0.60$ to $-0.0556$\,yr$^{-1}$ at $b_f=2.00$ and never changes sign; SI Table S3 reports the full sweep and balance-branch slopes.",
        "delegate full yield sweep to SI Table S3",
    )
    text = replace_once(
        text,
        r"Table~\ref{tab:model}b gives the initial populations for which $A_c$ comes within",
        r"Table~\ref{tab:model} gives the initial populations for which $A_c$ comes within",
        "main proximity table reference",
    )
    text = replace_once(
        text,
        "They rise with starting area; no jump appears at any tested tolerance.",
        "They rise with starting area; no jump appears at any tested tolerance. SI Table S4 reports the accompanying minimum-area grid.",
        "explicit SI Table S4 citation",
    )

    model_table = r"""\begin{table}[!htbp]
\centering\small
\caption{Initial populations at which minimum capital-land area approaches its floor. For endogenous-demand runs with $A_{f0}=0.6$\,ha, $q_0=0.9$, $\tau_g=20$\,yr, and $\tau_p=25$\,yr, the table reports $P_0$ at which $\min_tA_c$ comes within the stated distance of $\Acmin=0.05$\,ha. The first two columns use a $P_0$ grid with step $0.1$ ($\Delta t=0.1$\,yr, $T=400$\,yr); the final column uses bisection with the $10^{-6}$\,ha proximity criterion ($\Delta t=0.05$\,yr, $T=1000$\,yr). Sampled drawdown depth is monotone across the tested grid (Fig.~\ref{fig:model}c); neither the finite grid nor selected bisections establish general continuity. These values define proximity bands, not a single threshold.}
\label{tab:model}
\begin{tabular}{l l l l}
\toprule
$A_{c0}$ (ha) & within $10^{-2}$\,ha & within $10^{-4}$\,ha & within $10^{-6}$\,ha \\
\midrule
$0.40$ & $\approx1.8$ & $\approx2.1$ & $\approx2.41$ \\
$0.70$ & $\approx2.2$ & $\approx2.4$ & $\approx2.70$ \\
$1.00$ & $\approx2.6$ & $\approx2.8$ & $\approx2.98$ \\
$1.18$ & $\approx2.8$ & $\approx3.0$ & $\approx3.14$ \\
\bottomrule
\end{tabular}
\end{table}"""
    text = replace_span(
        text,
        r"\begin{table}[!htbp]" + "\n" + r"\centering\small" + "\n" + r"\caption{Model results at the baseline parameter set.",
        "\n" + r"\subsection{Technology gains are finite; debt depends on the shortfall}",
        model_table + "\n\n",
        "remove duplicated main fast-yield table panel",
    )

    text = replace_once(
        text,
        "These are conditional model results, not forecasts or empirical estimates.",
        "SI Table S13 reports the matched peak-debt values, and SI Fig. S5 shows the $P_0=1.0$ trajectories. These are conditional model results, not forecasts or empirical estimates.",
        "explicit SI Table S13 and Figure S5 citations",
    )
    text = replace_once(
        text,
        "matching the delayed-quality recovery table in the Supplementary Information (Table S5; $\\Delta t=0.1$\\,yr).",
        "matching the delayed-quality recovery table in the Supplementary Information (SI Table S5; $\\Delta t=0.1$\\,yr).",
        "explicit SI Table S5 citation",
    )
    text = replace_once(
        text,
        "The result depends on timing and rates; neither gate is universally preferable.",
        "The result depends on timing and rates; neither gate is universally preferable. SI Table S6 reports all nine gate and conversion-freeze policies at three timesteps.",
        "explicit SI Table S6 citation",
    )
    text = replace_once(
        text,
        "The yield interval must be attainable independently of the permitted areas; additional joint restrictions require a different feasible set.",
        "The yield interval must be attainable independently of the permitted areas; additional joint restrictions require a different feasible set. SI Table S10 sets out the observation-operator mapping, and SI Table S11 gives the observability ladder.",
        "explicit SI Tables S10 and S11 citations",
    )
    text = replace_once(
        text,
        r"Continuity and attainment of the yield interval supply a feasible allocation at each permitted $a$; SI~\S S9 gives the construction and endpoint witnesses.",
        r"Continuity and attainment of the yield interval supply a feasible allocation at each permitted $a$; SI~\S S9 gives the construction and SI Table S14 the endpoint witnesses.",
        "explicit SI Table S14 citation",
    )
    text = replace_once(
        text,
        r"SI~\S S10 reports the matched control and technology conditions, separates technology and debt contributions, and documents the state constraints. These calculations characterize the stated histories and parameters.",
        r"SI Table S15 reports all four conditions, SI Table S16 separates technology and debt contributions, and SI Table S17 gives the seven-step refinement and closure residuals. These calculations characterize the stated histories and parameters.",
        "explicit SI Tables S15 to S17 citations",
    )
    text = replace_once(
        text,
        r"and 1973 as the first year with $E_{\mathrm{prod}}/B>1$ (SI~\S S5).",
        r"and 1973 as the first year with $E_{\mathrm{prod}}/B>1$ (SI Table S8).",
        "explicit SI Table S8 citation",
    )
    text = replace_once(
        text,
        "The identity is exact for this proxy, but its allocation changes with the anchor and is not a physical-stock attribution.",
        "The identity is exact for this proxy, but its allocation changes with the anchor and is not a physical-stock attribution. SI Table S9 reports sensitivity to the 1961 account-share anchor.",
        "explicit SI Table S9 citation",
    )
    text = replace_once(
        text,
        r"The model yields five conditional predictions, with an operational test map in SI~\S S11.",
        r"The model yields five conditional predictions, with an operational test map in SI Table S18 and sampling and uncertainty rules in SI~\S S11.",
        "explicit SI Table S18 citation",
    )

    comparator = r"""SI~\S S7 reports a separate one-stock comparator, not a result for the two-land state $A_c$. Its full delayed trajectory (SI Fig. S1), fixed-demand masking example (SI Fig. S2), selected regeneration-delay trajectories (SI Fig. S3), and finite-grid endpoint classification (SI Fig. S4) use comparator-specific states and parameters. At the illustrated no-debt settings its equilibrium relation is monotone; these runs establish neither a fold nor a universal critical delay or collapse mechanism in the two-land model."""
    text = replace_span(
        text,
        r"SI~\S S7 gives a separate one-stock comparator.",
        "\n\nThese results also clarify when to expect common early-warning indicators.",
        comparator,
        "concise comparator paragraph with explicit SI figure citations",
    )

    measurement = r"""For the NFA, these findings concern account composition, not physical stocks. Section~\ref{sec:empirical} reports the Edition 2026 aggregate, per-person and component changes; their contrast shows why an aggregate and its constituents answer different questions. None of those account values measures forest biomass or condition, soil carbon, wetland extent, fish biomass, or another physical stock. In particular, a decline in Forest biocapacity does not establish a decline in forest biomass, and Built-up land is an NFA accounting class, not ecological capital \citep{Lo2026NFA,Borucke2013,Blomqvist2013,GiampietroSaltelli2014,Galli2016,vdBerghGrazi2015}.

The model baseline likewise illustrates an accounting mechanism rather than an observed global trend (Fig.~\ref{fig:model}a). With restoration off, one-way conversion leaves $A_c$ below its starting value after the shortfall closes; it then remains at the lower balance level rather than declining indefinitely. This conditional result is distinct from the NFA evidence."""
    text = replace_span(
        text,
        "For the NFA, these findings concern account composition, not physical stocks.",
        "\n\nWe assembled no common-boundary global physical-stock series",
        measurement,
        "remove repeated Discussion numbers while retaining claims and citations",
    )
    text = replace_once(
        text,
        "The SI measurement specification is a specification—not an inventory—with candidate stock, extent, condition, and annual-flow measures and the requirements for comparing them; it contains no endpoint values.",
        "SI Table S12 is an unpopulated measurement specification—not an inventory—with candidate stock, extent, condition, and annual-flow measures and the requirements for comparing them; it contains no endpoint values.",
        "explicit SI Table S12 citation",
    )

    # Main retains the formal results and a concise reason for each; the full
    # derivations already reside in SI and are not duplicated here.
    text = replace_span(
        text,
        "\\begin{proof}\nDifferentiate \\eqref{eq:B}",
        "\n\nFigure~\\ref{fig:model}a follows",
        "\\noindent\\emph{Proof sketch.} Differentiate Eq.~\\eqref{eq:B} and substitute the land flows; the reduced shortfall statement follows from $\\dot S=-\\dot B$. SI~\\S S2.1 gives the general identity with varying debt, quality and restoration.",
        "concise composition proof and SI derivation link",
    )
    text = replace_span(
        text,
        "\\begin{proof}\n(i) With $S=0$",
        "\n\nThe equality point",
        "\\noindent\\emph{Proof sketch.} The balance relation follows from $\\mu A_r=\\eta_fA_f$ and area conservation; direct substitution on the active-shortfall branch gives $J$. The debt fixed-point statement follows from monotonicity of $\\eta D+B_{eq}(\\Acmin;D)-E$. SI~\\S S2.2--S2.4 gives the derivations and branch restrictions.",
        "concise ceiling proof and SI derivation link",
    )
    text = replace_span(
        text,
        "\\begin{proof}\n(i) is $0\\le T_b",
        "\n\nWith fixed demand",
        "\\noindent\\emph{Proof sketch.} The three statements follow from $0\\le T_b\\le\\Delta b$, the comparison inequality for $\\dot D$, and comparison of the two contributions to $\\ln b_f$. SI~\\S S2.5 gives the derivation and the additive-comparator qualification.",
        "concise boundedness proof and SI derivation link",
    )
    text = replace_span(
        text,
        "\\begin{proof}\nAt fixed $A_c=a$",
        "\n\nFor a model-scale illustration",
        "\\noindent\\emph{Proof sketch.} Solve the supply inequalities at fixed $A_c$, then intersect the resulting area bounds when $A_f$ is observed. SI~\\S S9 proves attainment and sharpness; SI Table S14 supplies feasible endpoint witnesses.",
        "concise identification proof and SI derivation link",
    )
    return text


def transform_si(text):
    for key in ["Abaee2026a", "Abaee2026b"]:
        text = replace_bibitem(text, key, RECORDS[key])
    text = use_content_based_companion_locators(text, include_ledger=False)
    text = replace_once(
        text,
        r"Table~\ref{tab:si_sweep} extends the main-text fast-land-yield sweep in Table~2(a) by reporting the balance-branch slope.",
        r"Table~\ref{tab:si_sweep} reports the full fast-land-yield sweep summarized in the main-text fixed-demand results, including the balance-branch slope.",
        "SI sweep no longer refers to removed main panel",
    )
    text = replace_once(
        text,
        "\\begin{thebibliography}{99}\n\\small",
        "\\begin{thebibliography}{99}\n\\footnotesize",
        "avoid nearly empty trailing SI bibliography page",
    )
    return text


def main():
    old_main = (OLD / "ecomod_C18_A01_main.tex").read_text()
    old_si = (OLD / "ecomod_C18_A01_SI.tex").read_text()
    new_main = transform_main(old_main)
    new_si = transform_si(old_si)
    (R / "ecomod_C19_A01_main.tex").write_text(new_main)
    (R / "ecomod_C19_A01_SI.tex").write_text(new_si)
    for kind, old, new in [("main", old_main, new_main), ("SI", old_si, new_si)]:
        diff = "".join(
            difflib.unified_diff(
                old.splitlines(True),
                new.splitlines(True),
                fromfile=f"inherited_C18/ecomod_C18_A01_{kind}.tex",
                tofile=f"ecomod_C19_A01_{kind}.tex",
            )
        )
        (R / "evidence" / f"source_diff_{kind}_C19_A01.patch").write_text(diff)
    summary = {
        "source": "C18 A01 frozen main/SI sources",
        "target": "C19 A01",
        "companion_dois": {
            "Abaee2026a": "10.20944/preprints202610.3095.v1",
            "Abaee2026b": "10.20944/preprints202610.2983.v1",
            "Abaee2026c": "10.20944/preprints202610.3123.v1",
        },
        "main_source_words": len(re.findall(r"\b[\w'-]+\b", new_main)),
        "SI_source_words": len(re.findall(r"\b[\w'-]+\b", new_si)),
        "numerical_data_or_figure_regeneration": False,
        "core_results_removed_from_main": False,
        "duplicated_main_fast_yield_panel_removed": True,
    }
    (R / "metadata" / "editorial_transform_summary_C19_A01.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()

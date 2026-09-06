#!/usr/bin/env python3
"""Wave-7 build: paper5_sampled_governance v22 -> v23. Quality-scan fixes, presentation-layer only.

1. §3.4's one-plant operator contrast CORRECTED against the companion's declared orientation:
   the certified window (3.666, 150.358) yr is the delay-stabilised window of an
   undelayed-unstable loop (the companion's own record: unstable for 0 < tau < tau_-,
   stabilising lower crossing, destabilising upper crossing). The earlier text had read it as
   a delay-destabilised window, which inverted the continuous-delay stability at tau = 1 yr
   and manufactured the recorded zero-delay tension. No frozen record of THIS paper changes
   (rho = 1.00035, the 6.501 crossing, the 47.536/79.143 artefact readings, the 2.306
   protective reading all stand); only the attributed direction of the companion's window and
   the comparison points built on it are corrected.
2. The undelayed-limit reconciliation paragraph re-scoped: the companion's undelayed record
   (Routh-Hurwitz violation; lambda > 0) resolves the sign the paragraph had left open, and
   the records close at the zero-delay limit (both operators unstable undelayed; zero
   crossings strictly between 0 and tau_-; the edge contrast carries the operator difference).
3. Abstract: the garbled 'annual-review equilibrium crosses the unit circle near 6.5 yr'
   replaced by the multipliers/review-interval form.
4. Notation: the duplicated delta/delta_0 distinction dropped from the Notation (kept at the
   display it explains); 'no symbol serves two sorts' -> 'no other symbol...' (S itself is
   declared two-scope two sentences earlier); Table 3's eta descriptor harmonised to
   'effort-response coefficient' (the companion's term; delta_0 keeps 'effort-law gain').
5. §3.3/§3.4: the duplicated em-dash clause deleted; the q-referent clarified (the archived
   stage record declares no q); '[6.50, 200+] yr' -> the tested range '[6.50, 200]' yr; the
   complete-crossing-record paragraph cites Figure 1; the Benjamini-Yekutieli fallback cited
   with its reference entry added.
Non-destructive: no spectral record, crossing, verdict, table row, or recorded value changes.
"""
import hashlib

SRC = "../../arena agent 1/paper rewrites/paper5_sampled_governance_v22.md"
DST = "../../arena agent 1/paper rewrites/paper5_sampled_governance_v23.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: count {text.count(old)}: {old[:80]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

# --- 1. one-plant operator contrast corrected ---
sub_once(
 "Annual review is unstable under sampling ($\\rho = 1.00035$) but stable under continuous delay ($\\tau = 1$ yr $< \\tau_-$, the unstable window's lower edge); at $T_r = 8$ yr the ordering reverses (sampled stable, continuous delay inside its unstable window). The operator moves the stability window on the same plant — the cross-plant observation of Section 2.3 is now a same-plant one.",
 "The companion's window is delay-stabilising, not delay-destabilising: the undelayed loop is already unstable, the lower crossing at $\\tau_- = 3.666$ yr is stabilising, the upper crossing at $\\tau_+ = 150.358$ yr destabilising, and the loop is linearly unstable for $0 < \\tau < \\tau_-$ (Author et al., in review). Annual review is unstable under sampling ($\\rho = 1.00035$), and the same loop under continuous delay is likewise unstable at $\\tau = 1$ yr; at $T_r = 8$ yr both operators are stable (the sampled loop restabilised above its 6.50-yr crossing, the continuous loop inside its stabilised window). The operator contrast on one plant is an edge contrast: the sampled operator's restabilising crossing (6.50 yr) sits above the continuous operator's stabilising entry (3.666 yr), and the sampled loop's stability persists to the 200-yr scan ceiling where the continuous loop has already destabilised at $\\tau_+$ — the operator moves both edges of the stability window on the same plant, and the cross-plant observation of Section 2.3 is now a same-plant one.",
 "operator contrast corrected")

# --- 2. undelayed-limit reconciliation re-scoped ---
sub_once(
 "and this section records both that the undelayed equilibrium of the hold-map core is already unstable (annual $\\rho = 1.00035$) and that the same loop under continuous delay is stable at $\\tau = 1$ yr, below the companion's first Hopf crossing at 3.666 yr. Those records do not close at the zero-delay limit. If the continuous eigenvalue $\\lambda$ is positive — the direction the sampled record suggests through Section 3.2's relation — then the continuous-delay equation is unstable as $\\tau \\to 0$ and an even number of crossings must lie between $0$ and $3.666$ yr that neither this manuscript nor the companion's certified pair reports. If $\\lambda \\le 0$, then the sampled instability persisting down to $T_r = 0.2$ yr is inconsistent with Section 3.2's transfer conditions on this parameterisation. The eigenvalue $\\lambda$ is not printed in this manuscript (the spectral-margins record above; Appendix A), so the reconciliation is recorded as open rather than adjudicated: the operator-scoped records stand as recorded — annual instability under sampling, stability under continuous delay at $\\tau = 1$ yr, and the reversal at $T_r = 8$ yr — and Section 2.3's same-loop declaration and Section 3.2's transfer statement are read as scoped to their own hypotheses, not as a continuity argument connecting the two records at zero delay.",
 "and this section records that the undelayed equilibrium of the hold-map core is already unstable (annual $\\rho = 1.00035$). The companion's undelayed record fixes the remaining sign: the undelayed linearisation of the same loop violates the Routh–Hurwitz condition, so $\\lambda > 0$ — the direction the sampled record suggests through Section 3.2's relation, with the sampled instability persisting down to $T_r = 0.2$ yr. Under that sign the records close at the zero-delay limit: the loop is unstable under both operators at zero delay and at $\\tau = 1$ yr, and the stabilising crossing at 3.666 yr is the first crossing (zero crossings lie strictly between $0$ and $\\tau_-$, an even count, as the stability-switch principle requires) — no unreported crossings are needed. The two operators then differ only in where they place the window's edges, as the one-plant contrast above records. The eigenvalue $\\lambda$ is not printed in this manuscript (the spectral-margins record above; Appendix A); its sign is read from the companion's undelayed record, and the operator-scoped records stand as recorded — annual instability under sampling, instability under continuous delay at $\\tau = 1$ yr, and the same-plant edge contrast — with Section 2.3's same-loop declaration and Section 3.2's transfer statement consistent with both.",
 "undelayed-limit reconciliation re-scoped")

# --- 3. abstract clause ---
sub_once(
 "the logistic hold map's annual-review equilibrium crosses the unit circle near 6.5 yr",
 "the logistic hold map's equilibrium multipliers cross the unit circle at a review interval near 6.5 yr",
 "abstract crossing clause")

# --- 4. notation ---
sub_once(
 "with shift $\\delta$ (a constant regularisation offset, distinct from and unrelated to the effort-law gain $\\delta_0$) and sharpness $k$. The effort law is $F_B$.",
 "with shift $\\delta$ and sharpness $k$ (the shift is a constant regularisation offset, distinct from and unrelated to the effort-law gain $\\delta_0$, as the display below states). The effort law is $F_B$.",
 "notation delta dedupe")
sub_once(
 "The two scopes of $S$ never share an equation, and no symbol serves two sorts:",
 "The two scopes of $S$ never share an equation, and no other symbol serves two sorts:",
 "no other symbol")
sub_once("| effort-law gain $\\eta$ |", "| effort-response coefficient $\\eta$ |", "eta descriptor")

# --- 5. small fixes ---
sub_once(
 "annual review is stable at every tested response value — all declared annual-review trajectories converged at every tested response value — and the archived record places",
 "annual review is stable at every tested response value, and the archived record places",
 "dash duplicate cut")
sub_once(
 "(the paper declares no $q$ for the stage map; both values are reported)",
 "(the archived stage record declares no $q$; both values are reported for the reconstruction)",
 "q referent")
sub_once("stable on $[6.50, 200{+}]$ yr", "stable on $[6.50, 200]$ yr", "200+ -> 200")
sub_once(
 "On the logistic hold-map core the unit-circle crossing record over $[0.2, 200]$ yr is now complete.",
 "On the logistic hold-map core the unit-circle crossing record over $[0.2, 200]$ yr is now complete (Figure 1).",
 "Figure 1 cited")
sub_once(
 "the Benjamini–Yekutieli procedure under arbitrary dependence is the declared fallback",
 "the Benjamini–Yekutieli procedure under arbitrary dependence (Benjamini and Yekutieli, 2001) is the declared fallback",
 "BY cited")
by_entry = "Benjamini, Y., and Yekutieli, D. 2001. The control of the false discovery rate in multiple testing under dependency. Journal of the Royal Statistical Society B, 63: 425–441."
assert text.count(by_entry) == 0
bh_line = [l for l in text.split("\n") if l.startswith("Benjamini, Y., and Hochberg")][0]
text = text.replace(bh_line, bh_line + "\n" + by_entry, 1)
edits.append("BY entry added")

# --- version log ---
OLD_LOG_PREFIX = "*Version log (v22).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v23).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style), with one substantive attribution correction. (1) §3.4's one-plant operator contrast is "
"corrected against the companion delay study's declared orientation: the certified Hopf window "
"$(3.666, 150.358)$ yr is the delay-stabilised window of an undelayed-unstable loop — unstable for "
"$0 < \\tau < \\tau_-$, stabilising lower crossing, destabilising upper crossing — not a delay-destabilised window. "
"The earlier text had read the window in the classic orientation, which inverted the continuous-delay stability at "
"$\\tau = 1$ yr (it is unstable) and the reading at $T_r = 8$ yr (both operators stable there), and manufactured the "
"zero-delay tension the undelayed-limit paragraph then recorded as open. (2) That reconciliation paragraph is "
"re-scoped: the companion's undelayed record (a Routh–Hurwitz violation, so $\\lambda > 0$) resolves the sign, the "
"records close at the zero-delay limit (no unreported crossings required), and the operator difference is the "
"edge contrast (6.50 vs 3.666 yr lower edges; 200-yr scan ceiling vs 150.358-yr destabilisation). No frozen record "
"of this paper changes: $\\rho = 1.00035$, the 6.501 crossing, the 47.536/79.143 Euler artefact readings, the 2.306 "
"protective reading, and every table row stand as recorded. (3) The abstract's garbled clause ('the annual-review "
"equilibrium crosses the unit circle near 6.5 yr') reads 'equilibrium multipliers cross the unit circle at a review "
"interval near 6.5 yr'. (4) Notation: the duplicated $\\delta$/$\\delta_0$ distinction dropped from the Notation "
"(kept at the display it explains); 'no symbol serves two sorts' corrected to 'no other symbol' ($S$ itself is "
"declared two-scope); Table 3's $\\eta$ descriptor harmonised to 'effort-response coefficient'. (5) §3.3/§3.4's "
"duplicated em-dash clause deleted; the $q$-referent clarified (the archived stage record declares no $q$); "
"'$[6.50, 200{+}]$ yr' corrected to the tested range '$[6.50, 200]$ yr'; the complete crossing record cites "
"Figure 1; the Benjamini–Yekutieli fallback is cited with its reference entry added."
)
text = text[:i] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
for n in ["1.00035", "6.501", "47.536", "79.143", "2.306", "0.9967", "0.9838"]:
    assert body_old.count(n) == body_new.count(n), f"FAIL {n}: {body_old.count(n)}->{body_new.count(n)}"
for n in ["6.50", "3.666"]:  # narrative re-uses may add; nothing may be lost
    assert body_new.count(n) >= body_old.count(n), f"FAIL {n}: {body_old.count(n)}->{body_new.count(n)}"
assert "200{+}" not in body_new
assert "unstable window's lower edge" not in body_new
assert "stable under continuous delay" not in body_new
assert "no other symbol serves two sorts" in body_new
def table_lines(s):
    return [l for l in s.split("\n") if l.startswith("|")]
diff = [(o, n) for o, n in zip(table_lines(src), table_lines(text)) if o != n]
assert all("effort-law gain" in o and "effort-response coefficient" in n for o, n in diff) and len(diff) == 1, f"FAIL {diff}"
a_old = src[src.index("## Abstract"):src.index("## 1 Introduction")]
a_new = text[text.index("## Abstract"):text.index("## 1 Introduction")]
assert a_old.replace("the logistic hold map's annual-review equilibrium crosses the unit circle near 6.5 yr",
                     "the logistic hold map's equilibrium multipliers cross the unit circle at a review interval near 6.5 yr") == a_new

open(DST, "w", encoding="utf-8").write(text)
print(f"OK  P5 v23 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")

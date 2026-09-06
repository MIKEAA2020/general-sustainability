#!/usr/bin/env python3
"""Wave-7 build: paper4_delay_dynamics v27 -> v28 (+ supplementary S12 status-note append).

Quality-scan fixes, presentation-layer only:
1. §9.4 typo 'labled' -> 'labelled'; §9.6's 'Section 4.1' -> 'Theorem 4.1' (branch recurrence
   is Theorem 4.1's content; §4.1 is the scalar archetype).
2. §9.2's duplicate multiplier restatement and its version-log pointer dropped; §9.5's
   standalone duplicate onset sentence dropped; §9.6's inline off-by-one flag parenthetical
   trimmed (the dedicated flag paragraph carries it) and 'Correcting the earlier status:'
   -> 'Status:'; the second version-log pointer ('superseded earlier readings ... recorded in
   the version log') dropped.
3. Figure 1 cited from the running text (the five-regime topology paragraph).
4. §2.4's τ_m sentence reworded ('never share a letter' was literally false); Corollary 2.1's
   ν(t) gains a site-local note (ν is the Halanay decay rate in §10.2); §1.2's convention name
   harmonised to the flow-then-update form; the ζ/ς mapping note moved before the values; 'the
   classified six' named.
5. References: Aiello & Freedman moved to its alphabetical position (after Åström); the same
   journal rendered one way (J. Differ. Equ.).
6. The supplementary-material paragraph: 'wave-4 relocation' de-tagged; the S3 description
   scoped to its actual open items with the pre-rebuild status note named; S10's pre-v25
   labels mapped.
7. paper4_supplementary_v4.md: S12 appended — the S3 pre-rebuild status note and the
   supplementary's pre-v25 statement-label mapping (append-only).
Non-destructive: no theorem, spectral record, or table value changes.
"""
import hashlib

SRC = "../../arena agent 1/paper rewrites/paper4_delay_dynamics_v27.md"
DST = "../../arena agent 1/paper rewrites/paper4_delay_dynamics_v28.md"
SUP = "../../arena agent 1/paper rewrites/paper4_supplementary_v4.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: count {text.count(old)}: {old[:80]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

# --- 1. typo + pointer ---
sub_once("the two objects must be labled distinctly", "the two objects must be labelled distinctly", "labled typo")
sub_once("($\\approx253$ yr, Section 4.1)", "($\\approx253$ yr, Theorem 4.1)", "4.1 -> Theorem 4.1")

# --- 2. duplicate/narration trims ---
sub_once(
 "The registered record places the basin-bisection endpoint $0.011$ yr below the fold and returns large-branch multiplier $0.2040$ at $\\tau = 4.0$ and small-arm multiplier $1.0192$ at $5.584$; superseded earlier values on these points are recorded in the version log, not in this section.",
 "The registered record places the basin-bisection endpoint $0.011$ yr below the fold.",
 "9.2 duplicate restatement cut")
sub_once("The registered grids place the onset at $[148.6, 149.5]$ yr. ", "", "9.5 onset duplicate cut")
sub_once("lists ten symbols, an off-by-one to flag), and its delay-feedback loop is the companion's, not (1). Correcting the earlier status: these are verified",
         "lists ten symbols), and its delay-feedback loop is the companion's, not (1). Status: these are verified",
         "9.6 flag parenthetical + status")
sub_once("both arms cross $+1$ there; superseded earlier readings are recorded in the version log);",
         "both arms cross $+1$ there);",
         "9.2 version-log pointer cut")

# --- 3. Figure 1 cited ---
sub_once("so the classification is a statement about the declared domain, not the entire positive delay axis",
         "so the classification is a statement about the declared domain (Figure 1), not the entire positive delay axis",
         "Figure 1 cited")

# --- 4. notation/wording ---
sub_once("the two are distinct objects and never share a letter in an equation containing both.",
         "the two are distinct objects, distinguished by subscript wherever they co-occur.",
         "tau_m wording")
sub_once("the monotone bounded input $\\nu(t) = \\Phi_k(qE(t)N(t) - S(N(t))) \\le \\Phi_k(qE_{\\max}K)$.",
         "the monotone bounded input $\\nu(t) = \\Phi_k(qE(t)N(t) - S(N(t))) \\le \\Phi_k(qE_{\\max}K)$ (the letter $\\nu$ is site-local here — the filter input — and denotes the Halanay decay rate in Section 10.2).",
         "nu scope note")
sub_once("the update timing fixed by the pre-review/post-review convention of Section 8",
         "the update timing fixed by the flow-then-update (pre-review/post-review) convention of Section 8",
         "convention name")
sub_once("at $\\eta = 5$, $\\varsigma = 0.8$, $K_0 = 0.03$, $q = 0.01$ are confirmed. In the code symbol convention the savings parameter is $\\zeta$ (the manuscript's $\\varsigma$), and the fuel-efficiency parameter is $K_0$.",
         "In the code symbol convention the savings parameter is $\\zeta$ (the manuscript's $\\varsigma$), and the fuel-efficiency parameter is $K_0$; at $\\eta = 5$, $\\varsigma = 0.8$, $K_0 = 0.03$, $q = 0.01$ are confirmed.",
         "zeta mapping moved")
sub_once("$\\approx 3{,}800$–$35{,}000$ on the classified six)", "$\\approx 3{,}800$–$35{,}000$ on the six classified crossings)", "classified six")

# --- 5. references ---
aiello = "Aiello, W.G., Freedman, H.I., 1990. A time-delay model of single-species growth with stage structure. Mathematical Biosciences 101(2), 139–153.\n\n"
assert text.count(aiello.strip()) == 1
text = text.replace(aiello, "", 1)
astrom = "Åström, K.J., Wittenmark, B., 1997. Computer-Controlled Systems: Theory and Design, 3rd ed. Prentice Hall, Upper Saddle River.\n"
assert text.count(astrom.strip()) == 1
text = text.replace(astrom, astrom + aiello, 1)
edits.append("Aiello refiled")
sub_once("J. Differential Equations 269(5), 4215–4252", "J. Differ. Equ. 269(5), 4215–4252", "journal harmonised")

# --- 6. supplementary paragraph fixes ---
sub_once("(the $\\eta_{\\mathrm{crit}}$ sweep and pair-birth structure, the slow-fast intermittency diagnostics, and the sigmoid-gated effort screen record; wave-4 relocation from Sections 9.3 and 10.4)",
         "(the $\\eta_{\\mathrm{crit}}$ sweep and pair-birth structure, the slow-fast intermittency diagnostics, and the sigmoid-gated effort screen record; relocated from Sections 9.3 and 10.4)",
         "wave-4 tag dropped")
sub_once("the fold-certificate gap documentation (why the continuous-lift and Moore–Spence routes fail for this system, component by component)",
         "the fold-certificate gap documentation (the open continuum routes — the free-$\\tau$ enclosure, the transversality and curvature conditions, and the continuous-delay lift — component by component; S3's status list predates the rebuilt discrete-stage certificates and carries the appended status note, S12)",
         "S3 pointer scoped")
sub_once("the expanded proofs of Corollary 5.1 and Proposition 6.1 (S10)",
         "the expanded proofs of Corollary 5.1 and Proposition 6.1 (S10, which retains the pre-v25 labels Corollary 3 and Proposition 5 for these two objects)",
         "S10 label mapping")

# --- version log ---
OLD_LOG_PREFIX = "*Version log (v27).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v28).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no theorem, spectral record, or table value changes. "
"(1) §9.4's 'labled' typo; §9.6's 'Section 4.1' corrected to Theorem 4.1 (the recurrent-branch statement is "
"Theorem 4.1's; §4.1 is the scalar archetype). (2) Duplication and edit-narration trims: §9.2's duplicate "
"multiplier restatement and both in-body version-log pointers dropped; §9.5's standalone duplicate onset sentence "
"dropped; §9.6's inline off-by-one parenthetical trimmed (the dedicated State-count flag paragraph carries it) and "
"'Correcting the earlier status:' → 'Status:'. (3) Figure 1 cited from the five-regime topology paragraph. "
"(4) §2.4's τ_m sentence reworded ('never share a letter' was literally false of τ_m/τ_M/τ_p); Corollary 2.1's ν(t) "
"gains a site-local note (ν is the Halanay decay rate in §10.2); §1.2's convention named in the flow-then-update "
"form; the ζ/ς code-symbol mapping moved before the values it explains; 'the classified six' named. (5) References: "
"Aiello & Freedman moved to its alphabetical position (after Åström); the journal abbreviation harmonised. "
"(6) The supplementary-material paragraph drops the 'wave-4' process tag, scopes the S3 description to the open "
"continuum routes with the pre-rebuild status note named, and maps S10's pre-v25 labels. The supplementary gains S12 "
"(append-only): the S3 status note (S3's component list predates the rebuilt Krawczyk stage — items (i) and (iii) "
"are resolved at the discrete level by the §9.2 certificates; the free-τ enclosure, the transversality/curvature "
"conditions, and the continuous-delay lift remain open) and the pre-v25 statement-label mapping for S5/S6/S10/S1.1."
)
text = text[:i] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
for n in ["0.2040", "1.0192", "5.5872362", "148.6", "149.5", "3.666149", "150.358477",
          "6.50", "2.306", "0.9838", "0.9967", "0.029", "nine states", "ten symbols"]:
    co, cn = body_old.count(n), body_new.count(n)
    if n in ("0.2040", "1.0192", "148.6"):
        assert cn == co - 1, f"FAIL {n}: {co}->{cn}"
    elif n == "149.5":
        assert cn == co - 1, f"FAIL {n}: {co}->{cn}"
    else:
        assert cn == co, f"FAIL {n}: {co}->{cn}"
assert "labled" not in body_new
assert "wave-4" not in body_new
assert body_new.count("version log") < body_old.count("version log")
def table_lines(s):
    return [l for l in s.split("\n") if l.startswith("|")]
assert table_lines(src) == table_lines(text), "FAIL table lines changed"
assert text.rindex("Åström, K.J.") < text.rindex("Aiello, W.G.") < text.rindex("Beretka, S.")

open(DST, "w", encoding="utf-8").write(text)

# --- supplementary: append S12 (idempotent) ---
sup = open(SUP, encoding="utf-8").read()
S12 = (
"\n\n---\n\n## S12. Status and Label Notes (Wave-7 Append)\n\n"
"**S3 status note (dated at the wave-7 build).** S3's component list records the pre-rebuild state of the A025 fold "
"computation. The rebuilt Krawczyk stage of the A025 pipeline (main text, Sections 5.1 and 9.2; the recovered "
"compute core of S9.5) has since obtained the discrete-collocation certificates: items (i) and (iii) — the converged "
"Moore–Spence zero and the discrete Krawczyk inclusion — are resolved at the discrete level for the lower fold "
"(the enclosure $[5.587236198689, 5.587236198691]$) and the second fold carries its interval-Krawczyk certificate. "
"Item (ii) (the free-$\\tau$ contracting enclosure near the turning region), item (iv) (the interval transversality "
"and curvature conditions), and item (v) (the continuous-DDE lift) remain open, so S3's headline 'The fold "
"certificate is not obtained' now reads as the status of the validated continuous fold theorem, which no main-text "
"statement claims.\n\n"
"**Statement-label mapping.** S5, S6, S10, and S1.1 retain pre-v25 statement labels for the following objects; the "
"main text's current labels are: Proposition 2 → the hypothesis of Remark 5.1; Corollary 3 → Corollary 5.1; "
"Proposition 5 → Proposition 6.1; Theorem 2 → Theorem 4.1; Proposition 1 → Lemma 2.1; Theorem 6 → Theorem 10.1. "
"S10's heading ('Expanded Proofs: Corollary 3 and Proposition 5') refers to the objects the main text now labels "
"Corollary 5.1 and Proposition 6.1.\n"
)
if "## S12. Status and Label Notes" in sup:
    print("    supplementary S12 already appended — verified, no write")
else:
    sup = sup.rstrip("\n") + S12
    open(SUP, "w", encoding="utf-8").write(sup)

print(f"OK  P4 v28 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")

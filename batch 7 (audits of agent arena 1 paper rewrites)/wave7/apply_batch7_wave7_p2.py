#!/usr/bin/env python3
"""Wave-7 build: paper2_obstruction_calculus v10 -> v11. Quality-scan fixes, presentation-layer only.

1. §1.1: the finite/checkable classification corrected (Theorems 3 and 5 are the finite forms;
   Theorem 4 is a drift certificate) and the definition's 'finite, checkable' softened to the
   checkable-with-finite-cases form.
2. Abstract: the mechanism count corrected (two finitely checkable, two closed-form
   conditional, one construction) and the CE-trap sentence's kernel compression fixed.
3. §1.1 item 6 + §6.2's Bias paragraph: 'empties a nonempty perfect-information kernel' ->
   empties the epistemic kernel of a system whose perfect-information kernel is nonempty.
4. Theorem 1's proof: the 'of earlier versions ... corrected at this revision' meta-narration
   dropped (the mathematical statement kept); §2.4's '(re-lettered ... at this revision)' and
   Remark 1's '(recorded at this revision)' parentheticals dropped.
5. §4.3: the Viab_Pi display written in the declared signature Viab(V; U, Pi) with the class
   letter (the lowercase pi form is undefined); the §4.3 display updated to match.
6. §2.4: lambda added to the local-scope fence (Farkas multiplier / observer decay rate).
7. §6.4: 'full-information viability certification (K = RViab)' -> robust viability
   certification (the hierarchy's own naming).
8. §4.1: the certainly-safe set's apposition fixed (it is the region where the index may
   certify safety; outside it the index must fall silent).
9. §3.3: the zero-margin/tube-safety relationship sentence restructured.
10. (H3.1): 'the following remark' -> the tube-safety form below.
11. §7: 'Each certificate identifies' -> 'Each certificate that admits a design remedy'.
12. §6.5's literature paragraph: the dangling apposition given a verb; UK spellings
    harmonised to the paper's US-dominant forms (realised/organise/labelled).
Non-destructive: no theorem statement, hypothesis, proof step, or display changed except the
two Viab-notation harmonisations; no numbers (there are none to change).
"""
import hashlib

SRC = "../../arena agent 1/paper rewrites/paper2_obstruction_calculus_v10.md"
DST = "../../arena agent 1/paper rewrites/paper2_obstruction_calculus_v11.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: count {text.count(old)}: {old[:80]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

# --- 1. classification fix ---
sub_once(
 "In its polyhedral common-action and certification forms (Theorems 3–5) the argument is a finite, checkable test.",
 "In its polyhedral common-action and certification forms (Theorems 3 and 5) the argument is a finite, checkable test.",
 "Theorems 3 and 5")
sub_once(
 "An obstruction certificate (a finite, checkable witness that no observation-based policy exists) is an argument that a prescribed class of observation-based policies fails",
 "An obstruction certificate (a checkable witness that no observation-based policy exists — finite in the polyhedral and finite-fibre cases) is an argument that a prescribed class of observation-based policies fails",
 "definition softened")

# --- 2. abstract count + CE-trap compression ---
sub_once(
 "Five mechanisms are established — four as finite objects, the timing bound as a closed-form template — with a sixth exhibited under a policy-class restriction.",
 "Five mechanisms are established — two finitely checkable (the polyhedral common-action and finite-fibre certification forms), two as closed-form conditional certificates (the exit and timing bounds), and one minimal construction — with a sixth exhibited under a policy-class restriction.",
 "mechanism count")
sub_once(
 "shows that under a biased observation such a controller can empty a nonempty perfect-information kernel.",
 "shows that under a biased observation such a controller can empty the epistemic kernel of a system whose perfect-information kernel is nonempty.",
 "abstract CE compression")

# --- 3. empties compressions (2 body sites) ---
sub_once(
 "Even an *injective* observation empties a nonempty perfect-information kernel if the policy class is restricted",
 "Even an *injective* observation empties the epistemic kernel of a system whose perfect-information kernel is nonempty if the policy class is restricted",
 "1.1 item 6 compression")
sub_once(
 "a biased indicator with an uncorrected certainty-equivalence policy empties a nonempty perfect-information kernel.",
 "a biased indicator with an uncorrected certainty-equivalence policy empties the epistemic kernel of a system whose perfect-information kernel is nonempty.",
 "Bias compression")

# --- 4. meta-narration drops ---
sub_once(
 "the remark of earlier versions that convexity of $D$ was needed only for Filippov-style closure arguments was backwards — closure and relaxation are the standard tools for this step — and is corrected at this revision.",
 "convexity of $D$ was not needed for the closure step — closure and relaxation are the standard tools for it.",
 "Thm 1 proof meta drop")
sub_once(
 "the Lyapunov function of Appendix A.2 is $W = S_1 + S_2$ (re-lettered from the control-set letter at this revision).",
 "the Lyapunov function of Appendix A.2 is $W = S_1 + S_2$ (appendix-local).",
 "2.4 relettered drop")
sub_once(
 "defined here (one formal definition, recorded at this revision):",
 "defined here in one formal definition:",
 "Remark 1 recorded drop")

# --- 5. Viab notation harmonisation ---
sub_once(
 "so $\\mathrm{Viab}_{\\Pi_{\\mathrm{CE}}} \\subsetneq \\mathrm{Viab}_{\\Pi_{\\mathrm{output}}} = \\mathrm{Viab}_{\\Pi_{\\mathrm{state}}}$ — the kernel empties exactly when the controller refuses the correction.",
 "so $\\mathrm{Viab}(\\mathcal{V}; U, \\Pi_{\\mathrm{CE}}) \\subsetneq \\mathrm{Viab}(\\mathcal{V}; U, \\Pi_{\\mathrm{output}}) = \\mathrm{Viab}(\\mathcal{V}; U, \\Pi_{\\mathrm{state}})$ — the kernel empties exactly when the controller refuses the correction.",
 "Viab_Pi display")
sub_once(
 "$$\\mathrm{Viab}(\\mathcal{V}; U, \\pi_{\\mathrm{CE}}) = \\varnothing.$$",
 "$$\\mathrm{Viab}(\\mathcal{V}; U, \\Pi_{\\mathrm{CE}}) = \\varnothing.$$",
 "pi -> Pi display")

# --- 6. lambda fence ---
sub_once(
 "and the erosion radius of its eroded kernels (site-local); $d$ is the disturbance input in the body",
 "and the erosion radius of its eroded kernels, and $\\lambda$ is the Farkas multiplier of Theorem 3's checkability certificate and the observer decay rate of Section 5(c) (site-local); $d$ is the disturbance input in the body",
 "lambda fence")

# --- 7. RViab naming ---
sub_once(
 "full-information viability certification ($K = \\mathrm{RViab}(\\mathcal{V})$)",
 "robust viability certification ($K = \\mathrm{RViab}(\\mathcal{V})$)",
 "RViab naming")

# --- 8. certainly-safe apposition ---
sub_once(
 "The certainly-safe set is the honest relaxation: the region where the index may certify safety, and the region where it must fall silent.",
 "The certainly-safe set is the honest relaxation: it is the region where the index may certify safety; outside it, the index must fall silent.",
 "certainly-safe apposition")

# --- 9. zero-margin restructure ---
sub_once(
 "the two certificates are stated separately ($\\inf_{x \\in B} q(x) = 0$ with $T_{\\mathrm{obs}} > 0$ — any strictly positive observation delay is then too late under a uniform outward drift), not a $T_{\\mathrm{obs}} \\to \\infty$ limit.",
 "the two certificates are stated separately; the common-action obstruction is the zero-margin instance ($\\inf_{x \\in B} q(x) = 0$ with $T_{\\mathrm{obs}} > 0$ — any strictly positive observation delay is then too late under a uniform outward drift), and the pair is not related as a $T_{\\mathrm{obs}} \\to \\infty$ limit.",
 "zero-margin restructure")

# --- 10. following remark ---
sub_once(
 "must be replaced by the tube-safety statement of the following remark",
 "must be replaced by the tube-safety statement of the tube-safety form below",
 "following remark")

# --- 11. each certificate ---
sub_once(
 "Each certificate identifies the design change that removes it:",
 "Each certificate that admits a design remedy identifies it:",
 "each certificate")

# --- 12a. dangling apposition ---
sub_once(
 "The exact relationship, reconciled with Section 6.3: correctly carried out under the set-membership semantics, the estimation-space solution propagates the belief under a single control signal, so its controls *are* common controls and joint admissibility is built into the estimation-space problem's own admissibility — that is Section 6.3's statement, and it is the correct one for the semantics adopted here.",
 "The exact relationship is the one stated in Section 6.3: correctly carried out under the set-membership semantics, the estimation-space solution propagates the belief under a single control signal, so its controls *are* common controls and joint admissibility is built into the estimation-space problem's own admissibility.",
 "apposition fix")

# --- 12b. spellings ---
sub_once("the disturbance is chosen along the realised control", "the disturbance is chosen along the realized control", "realized")
sub_once("that organise the analysis", "that organize the analysis", "organize")
c = text.count("labelled")
assert c == 2, f"FAIL labelled count {c}"
text = text.replace("labelled", "labeled")
edits.append("labeled x2")

# --- version log ---
OLD_LOG_PREFIX = "*Version log (v10).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v11).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no theorem statement, hypothesis, proof step, or displayed "
"value changes. (1) The §1.1/abstract finite-object accounting is corrected: the finite forms are Theorems 3 and 5 "
"(the earlier 'Theorems 3–5' range swept in Theorem 4, which the next sentence classifies as a drift certificate), "
"the definition's 'finite, checkable' is scoped to the polyhedral and finite-fibre cases, and the abstract's "
"'four as finite objects' count reads two finitely checkable + two closed-form conditional + one construction. "
"(2) Three 'empties a nonempty perfect-information kernel' compressions are corrected to the precise form (the "
"epistemic kernel empties while the perfect-information kernel is nonempty) — the abstract's CE-trap sentence, §1.1 "
"item 6, and the Bias paragraph. (3) Theorem 1's proof drops its 'of earlier versions … corrected at this revision' "
"narration (the mathematical statement kept); §2.4's '(re-lettered … at this revision)' and Remark 1's '(recorded at "
"this revision)' parentheticals are dropped. (4) The §4.3 Viab display is written in the declared signature "
"Viab(V; U, Π) with the class letter Π_CE (the lowercase form was undefined); λ joins §2.4's local-scope fence. "
"(5) 'full-information viability certification' corrected to robust viability certification; the certainly-safe "
"set's apposition fixed; the zero-margin/tube-safety relationship restructured; 'the following remark' points at the "
"tube-safety form; 'Each certificate identifies' scoped to certificates that admit a design remedy; the §6.5 "
"literature sentence's dangling apposition given a verb; UK spellings harmonised to the paper's US-dominant forms."
)
text = text[:i] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
# meta-narration dropped except the two intentional disclosures (the Def-1 withdrawal tombstone
# and the §2.4 fraktur-retirement notation declaration)
leftover = [m for m in ["of earlier versions", "at this revision"] if m in body_new]
assert all("fraktur information symbols" in body_new or m == "of earlier versions" for m in leftover)
assert "the remark of earlier versions" not in body_new
assert "(re-lettered from the control-set letter at this revision)" not in body_new
assert "(one formal definition, recorded at this revision)" not in body_new
assert "empties a nonempty perfect-information kernel" not in body_new
assert body_new.count("realised") == 0 and body_new.count("organise") == 0 and body_new.count("labelled") == 0
assert body_new.count("Theorems 3 and 5") == 1
assert "Viab_{\\Pi" not in body_new and "U, \\pi_{\\mathrm{CE}}" not in body_new
for needle in ["Farkas, 1902", "Aubin", "Veliov", "Theorem 1", "Theorem 5"]:
    assert body_old.count(needle) == body_new.count(needle), f"FAIL {needle}"

open(DST, "w", encoding="utf-8").write(text)
print(f"OK  P2 v11 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")

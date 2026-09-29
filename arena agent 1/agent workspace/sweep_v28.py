#!/usr/bin/env python3
"""Refined residual sweep for paperE2_cod_intervention_v28.tex.

Uses lookbehinds so that a token is only flagged when it appears WITHOUT the
sign/context that makes it legitimate.  Fixes two false-positive classes found
in the first sweep:
  * "114.9" is a substring of the CORRECT signed class "-114.9"
  * "460.0" is legitimately UNSIGNED as the defect magnitude epsilon
"""
import re

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v28.tex"
tex = open(TEX, encoding="utf-8").read()

# token -> (regex, why)
CHECKS = [
    # --- Fox-campaign / source-year constants that must be GONE ------------
    ("2219.6", r"2219\.6", "Fox q05/T=inf kernel (stale)"),
    ("2070.9", r"2070\.9", "Fox q05 finite kernel (stale)"),
    ("920.2",  r"920\.2",  "Fox A phi=0.75 q10 T=1 (stale) -> 954.7"),
    ("989.0",  r"989\.0",  "Fox misc (stale)"),
    ("1025.5", r"1025\.5", "Fox misc (stale)"),
    ("1064.7", r"1064\.7", "Fox misc (stale)"),
    ("1111.3", r"1111\.3", "Fox misc (stale)"),
    ("1161.0", r"1161\.0", "Fox misc (stale)"),
    ("206.6",  r"206\.6",  "Fox campaign max residual (stale) -> 179.8"),
    # --- source-year SD: illegal unless explicitly labelled source-year ----
    ("114.9 UNSIGNED", r"(?<![-\d.])114\.9",
     "source-year SD; registered is 135.0"),
    ("-10.9", r"(?<![\d.])-10\.9(?![-\d])",
     "source-year mean; registered is -20.4"),
    # --- Table 3 Fox values ------------------------------------------------
    ("0.906", r"0\.906", "Fox Table 3 (stale)"),
    ("0.862", r"0\.862", "Fox Table 3 (stale)"),
    ("0.958", r"0\.958", "Fox Table 3 (stale)"),
    ("0.647", r"0\.647", "Fox Table 3 (stale)"),
    ("0.835", r"0\.835", "Fox Table 3 (stale)"),
    ("0.903", r"0\.903", "Fox Table 3 (stale)"),
    ("0.857", r"0\.857", "Fox Table 3 (stale)"),
    ("0.955", r"0\.955", "Fox Table 3 (stale)"),
    # --- class magnitudes must carry their sign ---------------------------
    ("318.8 UNSIGNED", r"(?<!-)\b318\.8", "class floor should be signed -318.8"),
    ("460.0 UNSIGNED (non-epsilon)", r"(?<!-)\b460\.0",
     "only legal as the epsilon magnitude; check context"),
]

# Contexts where a source-year constant is LEGITIMATE: it must appear inside an
# explicit comparison sentence naming the source-year convention.  Section 3.8
# contrasts the two pools, and Section 3.5 / the dominance discussion genuinely
# use the source-year residual convention.
LEGIT_SRCYEAR = re.compile(
    r"source[- ]year (pool|convention|floors?|informative|classes|"
    r"training residuals|10th-percentile|runner)", re.I)


def legit(ctx):
    """A source-year constant is fine if an explicit source-year label sits
    within ~160 chars of it."""
    return bool(LEGIT_SRCYEAR.search(ctx))


clean = True
for name, pat, why in CHECKS:
    hits = list(re.finditer(pat, tex))
    if not hits:
        continue
    for m in hits:
        i = m.start()
        ln = tex[:i].count("\n") + 1
        ctx = tex[max(0, i - 160):i + 160].replace("\n", " ")
        # epsilon magnitude is a legitimate unsigned 460.0
        if name.startswith("460.0") and re.search(
                r"varepsilon\s*=\s*\$?\\?\(?" + re.escape("460.0"), ctx):
            continue
        # a source-year constant is legitimate when explicitly labelled as such
        if name in ("114.9 UNSIGNED", "0.906", "0.903", "0.835", "0.647",
                    "-10.9", "206.6") and legit(ctx):
            continue
        clean = False
        print(f"  LIVE  {name}  ({why})")
        print(f"        line {ln}: ...{ctx[max(0, len(ctx)//2-95):len(ctx)//2+95]}...\n")

print("  CLEAN" if clean else "  ^ review each hit above")
print('\n"seven" occurrences:', len(re.findall(r"\bseven\b", tex)))
print("doc chars:", len(tex))

#!/usr/bin/env python3
"""Source-level QA for the local ECOMOD Continued 11 draft.

Checks that assembled main/SI match the modular TeX sources, table includes
are expanded, labels/references and citations resolve, and TeX braces and
begin/end environments are balanced. This is a lint/check script, not a TeX
compiler or scientific proof.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
MAIN_PARTS = ["parts/00_front.tex", "parts/01_methods.tex", "parts/02_results.tex", "parts/03_discussion.tex", "parts/04_refs.tex"]
SI_PARTS = ["parts/si_00.tex", "parts/si_01.tex", "parts/si_02.tex", "parts/si_refs.tex"]
MAIN_OUT = "ecomod_continued_11_revision_draft_20261028.tex"
SI_OUT = "ecomod_continued_11_revision_draft_20261028_SI.tex"
TABLE_RE = re.compile(r"\\input\{(parts/si_tab_(?:delay|drawdown|recovery)\.tex)\}\n?")
errors: list[str] = []
notes: list[str] = []

def slurp(parts: list[str]) -> str:
    return "".join((ROOT / p).read_text(encoding="utf-8") for p in parts)

def check_doc(name: str, text: str, bibliography_text: str) -> None:
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    dup_labels = [x for x, n in Counter(labels).items() if n > 1]
    if dup_labels:
        errors.append(f"{name}: duplicate labels: {', '.join(dup_labels)}")
    known = set(labels)
    refs = []
    for cmd in ("ref", "eqref", "autoref", "cref", "Cref", "pageref"):
        refs.extend(re.findall(r"\\" + cmd + r"\{([^}]+)\}", text))
    missing = sorted(set(refs) - known)
    if missing:
        errors.append(f"{name}: unresolved internal references: {', '.join(missing)}")
    bibkeys = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^{}]+)\}", bibliography_text)
    duplicate_bib = [x for x, n in Counter(bibkeys).items() if n > 1]
    if duplicate_bib:
        errors.append(f"{name}: duplicate bibliography keys: {', '.join(duplicate_bib)}")
    cited: list[str] = []
    for match in re.finditer(r"\\cite[a-zA-Z*]*\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}", text):
        cited.extend(k.strip() for k in match.group(1).split(",") if k.strip())
    uncited = sorted(set(cited) - set(bibkeys))
    if uncited:
        errors.append(f"{name}: citation keys missing from bibliography: {', '.join(uncited)}")
    unused = sorted(set(bibkeys) - set(cited))
    if unused:
        notes.append(f"{name}: {len(unused)} bibliography item(s) not cited in this document: {', '.join(unused[:8])}" + (" …" if len(unused) > 8 else ""))


def check_tex_balance(name: str, text: str) -> None:
    # Ignore TeX comments while retaining URL % escapes inside \url arguments
    # as ordinary characters. Comment stripping is intentionally conservative.
    brace_depth = 0
    line_no = 1
    for line in text.splitlines():
        # TeX comments begin at an unescaped percent. Avoid treating percent
        # escapes inside \url{...} as comments by preserving that macro token.
        scrub = line
        if r"\url{" not in line and r"\href{" not in line:
            m = re.search(r"(?<!\\)%", line)
            if m:
                scrub = line[:m.start()]
        i = 0
        while i < len(scrub):
            ch = scrub[i]
            if ch == "\\":
                # A backslash quotes the next character for brace counting.
                i += 2
                continue
            if ch == "{":
                brace_depth += 1
            elif ch == "}":
                brace_depth -= 1
                if brace_depth < 0:
                    errors.append(f"{name}: extra closing brace near line {line_no}")
                    return
            i += 1
        line_no += 1
    if brace_depth:
        errors.append(f"{name}: unbalanced braces (net depth {brace_depth})")
    envs = re.findall(r"\\(begin|end)\{([^}]+)\}", text)
    stack: list[tuple[str, int]] = []
    for kind, env in envs:
        if kind == "begin":
            stack.append((env, len(stack) + 1))
        elif not stack or stack[-1][0] != env:
            expected = stack[-1][0] if stack else "none"
            errors.append(f"{name}: environment mismatch at \\end{{{env}}}; expected {expected}")
            return
        else:
            stack.pop()
    if stack:
        errors.append(f"{name}: unclosed environments: " + ", ".join(x[0] for x in stack[-8:]))

main = slurp(MAIN_PARTS)
si_modular = slurp(SI_PARTS)
si_expected = TABLE_RE.sub(lambda m: (ROOT / m.group(1)).read_text(encoding="utf-8").rstrip("\n") + "\n", si_modular)
main_actual = (ROOT / MAIN_OUT).read_text(encoding="utf-8")
si_actual = (ROOT / SI_OUT).read_text(encoding="utf-8")
if main_actual != main:
    errors.append(f"assembled main differs from concatenated source modules")
if si_actual != si_expected:
    errors.append(f"assembled SI differs from source modules/table fragments")
if "\\input{" in si_actual or "\\input{" in main_actual:
    errors.append("unexpanded \\input remains in assembled output")

check_doc("main", main_actual, (ROOT / "parts/04_refs.tex").read_text(encoding="utf-8"))
check_doc("SI", si_actual, (ROOT / "parts/si_refs.tex").read_text(encoding="utf-8"))
check_tex_balance("main", main_actual)
check_tex_balance("SI", si_actual)

# Revision-specific regression checks.
bs = chr(92)
regressions = {
    "projected law in main": ("literal", bs + "Pi_{T_{K_q}(q(t))}G_c" + bs + "big(q(t-" + bs + "tau_g)" + bs + "big)"),
    "quality-index scope": ("regex", r"uncalibrated, model-defined quality index"),
    "imposed quality bound": ("regex", r"not an estimated ecological threshold"),
    "finite-step implementation check": ("regex", r"finite-step consistency test"),
    "saturation-induced delay qualification": ("regex", r"saturation-induced degeneracy, not general delay robustness"),
    "correct recovery endpoint": ("regex", r"0\.677"),
    "correct recovery fraction": ("regex", r"0\.46"),
    "balance-family distinction": ("regex", r"strict-surplus allocations are a separate no-conversion family"),
    "debt derivative correction": ("literal", bs + "partial" + bs + "dot D/" + bs + "partial D=" + bs + "alpha b_fA_f-" + bs + "eta"),
}
combined = main_actual + "\n" + si_actual
for name, (kind, expected) in regressions.items():
    matched = expected in combined if kind == "literal" else bool(re.search(expected, combined))
    if not matched:
        errors.append(f"revision regression check failed: {name}")

expected_title = "A rising biocapacity total can mask ecological-capital land drawdown: a two-land model"
old_title = "Aggregate biocapacity does not identify its composition: a two-land model of ecological-capital land drawdown"
if (bs + "title{" + expected_title + "}") not in main_actual:
    errors.append("main title does not match the assembled C10 title")
if expected_title not in si_actual:
    errors.append("SI title does not match the assembled C10 title")
contact_needles = (
    ("clickable email", bs + "href{mailto:amin_abaee@ut.ac.ir}"),
    ("clickable ORCID", bs + "href{https://orcid.org/0000-0002-0019-1842}"),
)
for doc_label, document in (("main", main_actual), ("SI", si_actual)):
    for label, needle in contact_needles:
        if needle not in document:
            errors.append(f"missing {label} hyperlink in {doc_label}")
    if bs + "ead{" in document:
        errors.append(f"legacy unlinked ead field remains in {doc_label}")
if "ORCID: " + contact_needles[1][1] + "{ORCID:" in main_actual:
    errors.append("duplicate ORCID label in main corresponding-author note")

visible_text = re.sub(re.escape(bs) + r"href\{[^}]*\}\{[^}]*\}", "", combined)
visible_text = re.sub(re.escape(bs) + r"url\{[^}]*\}", "", visible_text)
if old_title in visible_text:
    errors.append("stale pre-C10 title remains in submission text")
for obsolete in ("v45", "C10 producer-to-output", "local C11 rebase", "historical run generated the C10 table", "version mismatch", "change log"):
    if obsolete in visible_text:
        errors.append(f"internal lineage/provenance language remains in submission text: {obsolete}")
for obsolete in ("0.828\\,ha", "0.71$", "Hutchinson1948", "Pearl1925"):
    if obsolete in combined:
        errors.append(f"obsolete manuscript string remains: {obsolete}")

if notes:
    print("NOTES:")
    print("\n".join(f"- {n}" for n in notes))
if errors:
    print("FAIL:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("PASS: assembled TeX matches modular sources and table fragments")
print("PASS: labels, references, citations, braces, and environments checked")
print("PASS: revision-specific model, scope, recovery, and balance checks")

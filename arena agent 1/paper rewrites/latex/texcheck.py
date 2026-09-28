"""
texcheck -- a checking discipline for LaTeX manuscripts.

Why this exists
---------------
The batteries in this programme lean on *needle* checks: assert that a literal
string occurs in the .tex. Needles police prose against prose. Three failure
modes have now been observed in the wild:

  1. a needle hard-codes a value that is wrong, so it *enforces* the error
     (the 736 case);
  2. a needle is stale, so it fails on correct prose and gets "fixed" by
     editing the needle rather than the paper;
  3. a needle loop tests the wrong variable, so the check asserts nothing at
     all (minimax v6-v11: 14 absence checks collapsed into one duplicated
     presence check, inside a harness whose exit code was always 0).

texcheck supplies four things needles cannot:

  A. **Table parsing.** `table_rows(tex, label)` returns the actual cells of a
     labelled tabular. The check is then driven by *what the table says*, not by
     a string someone retyped into the verifier. If the table is edited, the
     parsed value changes and the comparison re-runs.

  B. **Exact numeric comparison.** `num()` parses decimals, integers, `\\tfrac`,
     `\\frac`, `\\dfrac` and `\\times 10^{-k}` into `fractions.Fraction`, so
     recomputed values are compared to printed values exactly -- no float
     tolerance, no "looks close enough".

  C. **A falsifiability harness.** `assert_falsifiable()` mutates the tex in
     several independent ways and requires the battery to fail on *each* one.
     A battery that cannot fail is worth nothing, and this makes that a
     first-class, reported property rather than something discovered by
     accident six versions later.

  D. **Honest accounting.** `Report` records every check, prints failures, and
     computes the exit code from the failures -- not from the length of the
     pass list.

Usage
-----
    from texcheck import Report, table_rows, num, assert_falsifiable

    R = Report()
    rows = table_rows(tex, "tab:coverage")
    R.eq("row 1 viable count", computed_viable, printed_viable)
    ...
    R.finish()                       # prints total, sets exit code

    if "--falsify" in sys.argv:
        assert_falsifiable(TEX, __file__, MUTATIONS)
"""

import re
import sys
from fractions import Fraction


# ----------------------------------------------------------------- accounting
class Report:
    """Records every check. Failures are never dropped from the denominator."""

    def __init__(self):
        self.rows = []          # (name, ok, detail)

    def _add(self, name, ok, detail=""):
        ok = bool(ok)
        self.rows.append((name, ok, detail))
        print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
        return ok

    def ok(self, name, cond, detail=""):
        return self._add(name, cond, detail)

    def eq(self, name, computed, printed, detail=""):
        """Exact comparison of two values (Fraction / int / str)."""
        good = (computed == printed)
        if not good:
            detail = f"computed {computed} != printed {printed}" + (
                f" ({detail})" if detail else "")
        return self._add(name, good, detail)

    def close(self, name, computed, printed, tol=Fraction(1, 10**6)):
        """Comparison with an explicit, printed tolerance."""
        d = abs(Fraction(computed) - Fraction(printed))
        good = d <= tol
        return self._add(name, good, "" if good else
                         f"|{computed} - {printed}| = {float(d):.3g} > tol {float(tol):.3g}")

    @property
    def n_pass(self):
        return sum(1 for _, ok, _ in self.rows if ok)

    @property
    def n_total(self):
        return len(self.rows)

    def finish(self):
        n, t = self.n_pass, self.n_total
        print(f"\nverification: {n}/{t} checks pass")
        if n != t:
            print("FAILED:")
            for name, ok, detail in self.rows:
                if not ok:
                    print("  -", name, ("[" + detail + "]") if detail else "")
        raise SystemExit(0 if n == t else 1)


# ------------------------------------------------------------- latex parsing
# glyphs that carry meaning inside a table cell -> keep them as tokens
_GLYPH = {
    "circ": "CIRC", "bullet": "BULLET", "ast": "AST", "star": "STAR",
    "checkmark": "CHECK", "times": "TIMES", "dagger": "DAG", "ddagger": "DDAG",
    "emptyset": "EMPTY", "infty": "INF", "dots": "...", "ldots": "...",
    "le": "<=", "ge": ">=", "leq": "<=", "geq": ">=", "neq": "!=",
    "in": " in ", "notin": " notin ", "subset": " subset ", "subseteq": " subseteq ",
}


def _strip_cell(c):
    c = c.strip()
    # \multicolumn{n}{spec}{payload} -> payload
    c = re.sub(r"\\multicolumn\s*\{\d+\}\s*\{[^{}]*\}\s*\{", "{", c)
    c = re.sub(r"\\(top|mid|bottom)rule|\\cmidrule(\([^)]*\))?(\{\d+-\d+\})?|\\hline",
               " ", c)
    c = re.sub(r"\\(begin|end)\{minipage\}(\[[^]]*\])?", " ", c)
    c = re.sub(r"\\(raggedright|raggedleft|centering|linewidth|columnwidth)\b", " ", c)
    c = re.sub(r"\\(textbf|textit)\s*\{([^{}]*)\}", r"\2", c)
    for k, v in _GLYPH.items():
        c = re.sub(r"\\" + k + r"\b", " " + v + " ", c)
    c = re.sub(r"\\(textbf|textit|emph|text|textrm|mathrm|mathbf|mathit|label|ref|"
               r"cite|emph)\s*\{([^{}]*)\}", r"\2", c)
    c = c.replace("\\(", " ").replace("\\)", " ").replace("$", " ")
    c = re.sub(r"\\(left|right)\b", " ", c)
    c = c.replace("{", " ").replace("}", " ")
    c = c.replace("\\\\", " ")
    return " ".join(c.split())


def _tabular_body(block):
    """Return the body of the first tabular in `block`, brace-aware on the spec."""
    m = re.search(r"\\begin\{tabular\}", block)
    if not m:
        return None
    i = m.end()
    # brace-aware column spec
    if i < len(block) and block[i] == "{":
        depth, j = 0, i
        while j < len(block):
            if block[j] == "{":
                depth += 1
            elif block[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        i = j + 1
    end = block.find("\\end{tabular}", i)
    return block[i:end] if end > 0 else block[i:]


def environments(tex, env):
    """Yield (body, start, end) for each \\begin{env}...\\end{env}, nested-aware."""
    out = []
    for m in re.finditer(r"\\begin\{" + re.escape(env) + r"\}", tex):
        depth, i = 1, m.end()
        pat = re.compile(r"\\(begin|end)\{" + re.escape(env) + r"\}")
        while depth:
            n = pat.search(tex, i)
            if not n:
                break
            depth += 1 if n.group(1) == "begin" else -1
            i = n.end()
        out.append((tex[m.end():pat.search(tex, i - 1).start()] if depth == 0 else tex[m.end():i],
                    m.start(), i))
    return out


def table_rows(tex, label):
    """Return the cells of the tabular carrying \\label{<label>} as list of lists.

    Finds the enclosing table environment by the label, then parses the tabular
    inside it. Handles \\multicolumn by expanding the payload into one cell.
    """
    idx = tex.find("\\label{" + label + "}")
    if idx < 0:
        raise KeyError("no \\label{%s} in tex" % label)
    start = tex.rfind("\\begin{table", 0, idx)
    end = tex.find("\\end{table", idx)
    if start < 0 or end < 0:
        raise KeyError("label %s not inside a table environment" % label)
    block = tex[start:end]

    body = _tabular_body(block)
    if body is None:
        raise KeyError("no tabular in the table carrying %s" % label)

    rows = []
    for raw in re.split(r"\\\\", body):
        raw = raw.strip()
        if not raw:
            continue
        # strip rules anywhere in the row; skip only if nothing else remains
        # (a data row may legitimately start with \midrule on the same line)
        probe = re.sub(r"\\(top|mid|bottom)rule|\\cmidrule(\([^)]*\))?(\{\d+-\d+\})?|\\hline",
                       " ", raw).strip()
        if not probe:
            continue
        raw = probe
        cells, depth, cur = [], 0, ""
        for ch in raw:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            if ch == "&" and depth == 0:
                cells.append(cur)
                cur = ""
            else:
                cur += ch
        cells.append(cur)
        cells = [_strip_cell(c) for c in cells]
        # drop pure-rule rows and the cmidrule line
        if any(c for c in cells):
            rows.append(cells)
    return rows


# ------------------------------------------------------------ number parsing
_FRAC = {
    "tfrac": None, "dfrac": None, "frac": None,
}


def num(s, _default=None):
    """Parse a LaTeX number into an exact Fraction.

    Handles: integers, decimals, \\frac/\\tfrac/\\dfrac{a}{b}, a\\times 10^{k},
    and a leading minus / unicode minus. Returns _default (None) if no number
    is present.
    """
    if s is None:
        return _default
    s = str(s).strip()
    s = (s.replace("\\(", "").replace("\\)", "").replace("$", "")
          .replace("{,}", "").replace(",", "").replace("\\,", "")
          .replace("\\!", "").replace("~", " ")
          .replace("\u2212", "-").replace("\u00a0", " "))
    s = re.sub(r"\\(mathrm|mathbf|text)\s*\{([^{}]*)\}", r"\2", s)
    s = re.sub(r"\\(approx|sim|simeq)\s*", "", s)
    s = s.strip()

    # a \times 10^{k}
    m = re.match(r"^(-?\d*\.?\d+)\s*\\times\s*10\^\{?(-?\d+)\}?$", s)
    if m:
        return Fraction(m.group(1)) * Fraction(10) ** int(m.group(2))

    # \frac / \tfrac / \dfrac
    for name in ("tfrac", "dfrac", "frac"):
        pat = r"\\" + name + r"\s*\{([^{}]*)\}\s*\{([^{}]*)\}"
        m = re.search(pat, s)
        if m:
            try:
                return Fraction(num(m.group(1))) / Fraction(num(m.group(2)))
            except Exception:
                return _default

    m = re.search(r"-?\d+(?:\.\d+)?", s)
    if m:
        return Fraction(m.group(0))
    return _default


# ------------------------------------------------------------ falsifiability
def assert_falsifiable(tex_path, verifier_path, mutations, workdir=None, timeout=900):
    """Require the battery to FAIL on each independent mutation of the tex.

    `mutations` is a list of (name, old, new). Each is applied to a scratch copy
    of the tex; the verifier is run against it and must exit non-zero. Any
    mutation that the battery fails to catch is reported, because a battery that
    cannot detect a corrupted claim is not evidence of anything.
    """
    import os
    import shutil
    import subprocess
    import tempfile

    src = open(tex_path, encoding="utf-8").read()
    here = os.path.dirname(os.path.abspath(tex_path))
    base = workdir or tempfile.mkdtemp(prefix="falsify_")

    print("\n--- falsifiability harness (%d mutations) ---" % len(mutations))
    missed = []
    for name, old, new in mutations:
        if old not in src:
            print(f"  SKIP  {name}: anchor not present in the tex")
            missed.append(name + " (anchor missing)")
            continue
        d = os.path.join(base, re.sub(r"\W+", "_", name))
        os.makedirs(d, exist_ok=True)
        # the verifier plus everything it needs (data, chained scripts)
        for f in os.listdir(here):
            if f == os.path.basename(tex_path):
                continue
            s, t = os.path.join(here, f), os.path.join(d, f)
            if os.path.isfile(s):
                shutil.copy2(s, t)
            elif os.path.isdir(s):
                shutil.copytree(s, t, dirs_exist_ok=True)
        open(os.path.join(d, os.path.basename(tex_path)), "w", encoding="utf-8").write(
            src.replace(old, new, 1))
        # run the COPY: verifiers resolve their tex via __file__, so invoking the
        # original path would silently re-read the unmutated manuscript.
        vcopy = os.path.join(d, os.path.basename(verifier_path))
        shutil.copy2(os.path.abspath(verifier_path), vcopy)
        r = subprocess.run([sys.executable, vcopy],
                           cwd=d, capture_output=True, text=True, timeout=timeout)
        caught = (r.returncode != 0)
        print(f"  {'CAUGHT ' if caught else 'MISSED '} {name}"
              + ("" if caught else "   <-- battery cannot detect this"))
        if not caught:
            missed.append(name)

    print("--- falsifiability: %d/%d mutations detected ---"
          % (len(mutations) - len(missed), len(mutations)))
    if missed:
        print("UNDETECTED:", ", ".join(missed))
    return not missed


def longtable_rows(tex, marker):
    """Return the cells of the longtable that follows `marker`.

    Some manuscripts in this programme number tables with a bold run-in
    (``\\textbf{Table 4.}``) rather than a \\label, and use `longtable` rather
    than `tabular`. This finds the next longtable after the marker and parses
    it with the same cell splitter as `table_rows`.
    """
    i = tex.find(marker)
    if i < 0:
        raise KeyError("marker %r not found" % marker)
    m = re.search(r"\\begin\{longtable\}\s*(\[[^]]*\])?", tex[i:])
    if not m:
        raise KeyError("no longtable after %r" % marker)
    start = i + m.end()
    end = tex.find("\\end{longtable}", start)
    body = _scan_spec(tex[start:end]) if False else tex[start:end]
    # strip the column spec (brace-aware) exactly as _tabular_body does
    j = 0
    if j < len(body) and body[j] == "{":
        depth, k = 0, j
        while k < len(body):
            if body[k] == "{":
                depth += 1
            elif body[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        body = body[k + 1:]
    return _parse_rows(body)


def _parse_rows(body):
    rows = []
    for raw in re.split(r"\\\\", body):
        raw = raw.strip()
        if not raw:
            continue
        probe = re.sub(r"\\(top|mid|bottom)rule|\\cmidrule(\([^)]*\))?(\{\d+-\d+\})?|\\hline"
                       r"|\\noalign\{\}|\\endhead|\\endfirsthead|\\endfoot|\\endlastfoot",
                       " ", raw).strip()
        if not probe:
            continue
        raw = probe
        cells, depth, cur = [], 0, ""
        for ch in raw:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            if ch == "&" and depth == 0:
                cells.append(cur)
                cur = ""
            else:
                cur += ch
        cells.append(cur)
        cells = [_strip_cell(c) for c in cells]
        if any(c for c in cells) and not re.match(r"^>\{|\*\{?\d", cells[0]):
            rows.append(cells)
    return rows

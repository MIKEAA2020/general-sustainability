#!/usr/bin/env python3
"""Portable version: combine the closure-review markdown records into a
glyph-safe build copy for PDF compilation.

Paths are resolved relative to this script's location (tools/), so the bundle
can be rebuilt anywhere. Writes <root>/_build/combined.md.

Glyph policy (read before editing — see HANDOFF.md section 5):
- ONLY U+1D400-1D7FF (Mathematical Alphanumeric Symbols) and U+2100-214F
  (Letterlike math letters) are NFKD-mapped to plain letters, because the
  DejaVu font set used by the PDF pipeline lacks those planes.
- A short explicit table handles symbols absent from specific fonts.
- NEVER widen the NFKD ranges. Incident record: an earlier version mapped
  U+2000-U+2BFF wholesale, which silently deleted the combining solidus from
  negated relations (!=, not-in, not-subset, stroked arrows) — a semantic
  corruption of the mathematics, not a typesetting change.
"""
import os
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "_build", "combined.md")

FILES = [
    "00_MASTER_CLOSURE_REVIEW.md",
    "01_result_records/R01_T1_operator_II_false_positives.md",
    "01_result_records/R02_T2_closed_loop_bridge.md",
    "01_result_records/R03_T3_viability_diagnostic_bridge.md",
    "01_result_records/R04_T4_domain_admission.md",
    "01_result_records/R05_T5_restricted_assume_guarantee.md",
    "01_result_records/R06_T6_aggregation_memory.md",
    "01_result_records/R07_T7_intergenerational.md",
    "01_result_records/R08_T8_hierarchy_completion.md",
    "01_result_records/R09_T9_boundary_theorem.md",
]

EXPLICIT = {
    "\u27fa": "\u21d4",  # ⟺ -> ⇔
    "\u27f9": "\u21d2",  # ⟹ -> ⇒
    "\u27f8": "\u21d0",  # ⟸ -> ⇐
    "\u27f5": "\u2190",  # ⟵ -> ←
    "\u27f6": "\u2192",  # ⟶ -> →
    "\u2a06": "\u2294",  # ⨆ -> ⊔
    "\u1d40": "^T",      # ᵀ -> ^T (transpose)
    "\u1d57": "^t",      # ᵗ -> ^t
    "\u220e": "\u25a1",  # ∎ (end of proof; absent from DejaVu Serif) -> □
    "\u22a8": "|=",      # ⊨ (models; absent from DejaVu Mono) -> |=
}

NFKD_RANGES = ((0x1D400, 0x1D7FF), (0x2100, 0x214F))

NOTE = """
> **Typesetting note (PDF rendering only).** The canonical packet typefaces for
> schematic objects (double-struck K, W, R, M, T, P; fraktur A, S, B; sans-serif
> Z, I, P, D, O, U, W; script V, D, A, K, S, Y) are rendered in this PDF as the
> corresponding plain letters (K, W, R, ...). The markdown source files retain
> the canonical forms and remain the documents of record. Long arrows are
> rendered as their short equivalents.

"""


def norm_char(ch: str) -> str:
    if ch in EXPLICIT:
        return EXPLICIT[ch]
    cp = ord(ch)
    for lo, hi in NFKD_RANGES:
        if lo <= cp <= hi:
            d = unicodedata.normalize("NFKD", ch)
            return "".join(c for c in d if not unicodedata.combining(c))
    return ch


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    parts = [NOTE]
    for f in FILES:
        path = os.path.join(ROOT, f)
        with open(path, encoding="utf-8") as fh:
            parts.append("".join(norm_char(c) for c in fh.read()).rstrip() + "\n\n")
        parts.append("\\newpage\n\n")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts))
    text = open(OUT, encoding="utf-8").read()
    chars = sorted(set(c for c in text if ord(c) > 127))
    print(f"Wrote {OUT} ({len(text)} chars, {len(chars)} distinct non-ASCII)")
    print("Residual non-ASCII inventory (must be covered by DejaVu fonts):")
    print("".join(chars))


if __name__ == "__main__":
    main()

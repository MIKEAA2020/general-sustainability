#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .cache/tex
for name in followup_F10_main followup_F10_SI; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.cache/tex "$name.tex"
  cp ".cache/tex/$name.pdf" "$name.pdf"
done

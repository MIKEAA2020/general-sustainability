#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .cache/tex
python src/assemble_manuscripts_F11.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.cache/tex followup_F11_A01_main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.cache/tex followup_F11_A01_SI.tex
cp .cache/tex/followup_F11_A01_main.pdf followup_F11_A01_main.pdf
cp .cache/tex/followup_F11_A01_SI.pdf followup_F11_A01_SI.pdf

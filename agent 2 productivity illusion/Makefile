# Build the ECOMOD v40 manuscript (engine-adaptive: LuaLaTeX recommended).
#   make          -> build PDF (latexmk -lualatex)
#   make view     -> build then open the PDF
#   make clean    -> remove build artifacts
#
# NOTE: since v38 the preamble is engine-adaptive (iftex): LuaLaTeX/XeLaTeX
# use fontspec + unicode-math (with \IfFontExistsTF guards since v39, so a
# missing system font falls back to bundled Latin Modern); pdfLaTeX falls
# back to lmodern. LuaLaTeX is the recommended engine (the shipped PDFs are
# built with tectonic/lualatex).

MAIN   := manuscript_ECOMOD_v40
ENGINE := lualatex

.PHONY: all view clean

all:
        latexmk -$(ENGINE) $(MAIN).tex

view: all
        $(if $(wildcard $(MAIN).pdf),open $(MAIN).pdf,xdg-open $(MAIN).pdf)

clean:
        latexmk -C $(MAIN).tex
        rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).synctex.gz $(MAIN).fdb_latexmk $(MAIN).fls

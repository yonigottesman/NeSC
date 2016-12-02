LANG=C
# Makefile for creating PDF files from tex source
# Used for creating papers

# name of the project/PDF to create
PAPER=vdisk

# define the tools
LATEX := /usr/bin/pdflatex
BIBTEX := /usr/bin/bibtex
DVIPS := /usr/bin/dvips
DVIPDF := /usr/bin/dvipdf
DVIPDFM := /usr/bin/dvipdfm
DVIPDFMX := /usr/bin/dvipdfmx
PS2EPSI := /usr/bin/ps2epsi
DIA := /usr/bin/dia -e
CONVERT := /usr/bin/convert
GNUPLOT := /usr/bin/gnuplot

# define the flags for each tool
LATEX_FLAGS := -shell-escape -halt-on-error
BIBTEX_FLAGS := -terse
DVIPS_FLAGS :=  -Ppdf -G0
DVIPDFM_FLAGS := -p letter
DVIPDFMX_FLAGS := -p letter

# rules to test for the existence of tools
HAS_DVIPDFMX := $(shell test -x $(DVIPDFMX) && echo yes)
HAS_DVIPDFM := $(shell test -x $(DVIPDFM) && echo yes)

# targets
PS  := $(PAPER).ps
PDF := $(PAPER).pdf
DVI := $(PAPER).dvi
TEX_INPUTS:= $(wildcard *.tex) $(wildcard *.cls)
GENERATED_FIGS := $(DIAFIGS:.dia=.eps) $(PNGFIGS:.png=.eps)
EPSFIGS := 

AUX := 	$(PDF:.pdf=.aux) $(PDF:.pdf=.log) $(PDF:.pdf=.toc) \
	$(PDF:.pdf=.lof) $(PDF:.pdf=.lot) $(PDF:.pdf=.bbl) \
	$(PDF:.pdf=.blg) $(PDF:.pdf=.aux.bak)

FIGS :=  $(EPSFIGS) $(GENERATED_FIGS)

.PHONY:		all clean
.PRECIOUS:	$(DVI)

all:	$(PDF)

$(DVI):	$(FIGS) $(TEX_INPUTS)

clean:	
	$(RM) $(PDF) $(PS) $(DVI) $(AUX) $(BBL)

%.eps:	%.dia
	$(GNUPLOT) $@ $<

%.eps:	%.png
	$(CONVERT) $< $@

%.ps:	%.dvi
	$(DVIPS) $(DVIPS_FLAGS) -o $@ $<

%.pdf:   $(TEX_INPUTS) %.bib
	@echo "Running $(LATEX) on $*.tex"
	@$(LATEX) $(LATEX_FLAGS) $*.tex
	@echo "Running $(BIBTEX) on $*"
	@$(BIBTEX) $(BIBTEX_FLAGS) $*
	@echo "Making sure cross-referencing is OK - running $(LATEX) again"
	@$(LATEX) $*
	@echo "Sometimes twice is not enough - running $(LATEX) the third time"
	@$(LATEX) $*

bib:
	$(BIBTEX) $(BIBTEX_FLAGS) $(PAPER)

watermark: all
	@rm -f $(PAPER)-draft.pdf
	@pdftk $(PAPER).pdf background wmark/wmark.pdf output $(PAPER)-draft.pdf



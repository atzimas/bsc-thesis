PDOC	:= pandoc
SRCS_MD	:= $(wildcard ./*.md)
TARGET	:= presentation

.PHONY: all clean pdf pptx

all: pdf pptx

pdf:
	$(PDOC) -t beamer --slide-level=2 $(SRCS_MD) -o $(TARGET).$@

pptx:
	$(PDOC) $(SRCS_MD) -o $(TARGET).$@

clean:
	$(RM) $(TARGET).*
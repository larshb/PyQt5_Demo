PYUIC = pyuic5
PYTHON = python3

UIS = $(wildcard *.ui)
PYUIS = $(UIS:%.ui=ui_%.py)

all: $(PYUIS)

ui_%.py: %.ui
	$(PYUIC) $< -o $@

.PHONY: window
window: all
	$(PYTHON) main.py

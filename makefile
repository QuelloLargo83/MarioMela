ifeq ($(OS),Windows_NT)
	RM = rmdir /s /Q
else
	RM = rm -rf
endif

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) game.py


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	$(RM)  __pycache__
	$(RM)  $(VENV)

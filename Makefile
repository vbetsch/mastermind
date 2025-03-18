VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
REQUIREMENTS_FILE := requirements.txt

PROJECT_NAME := mastermind
ROOT_FOLDER := src
TESTS_FOLDER := tests/


all: run
.PHONY: all

.env:
	echo 'ERROR: No environment variable configured'
	exit 1

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip


install: $(VENV)/bin/activate
	$(PIP) install -r ${REQUIREMENTS_FILE}

requirements: install
	$(PIP) freeze > ${REQUIREMENTS_FILE}

run: install .env
	$(PYTHON) main.py

tests: install
	pytest ${TESTS_FOLDER}

coverage: install
	pytest --cov=${ROOT_FOLDER} --cov-report=term-missing --cov-fail-under=10 ${TESTS_FOLDER}

.PHONY: install requirements run tests coverage

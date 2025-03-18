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


UML_FILE_EXTENSION := dot
UML_IMAGE_EXTENSION := png
UML_FILE_NAME_TO_CONVERT := classes
UML_GENERATED_FILE_NAME := uml
UML_FILE_TO_CONVERT := ${UML_FILE_NAME_TO_CONVERT}.${UML_IMAGE_EXTENSION}

uml: install
	pyreverse -o ${UML_FILE_EXTENSION} -p ${PROJECT_NAME} ${ROOT_FOLDER}.
	dot -Tpng ${UML_FILE_NAME_TO_CONVERT}_${PROJECT_NAME}.${UML_FILE_EXTENSION} -o ${UML_FILE_TO_CONVERT}
	mv ${UML_FILE_TO_CONVERT} ${UML_GENERATED_FILE_NAME}.${UML_IMAGE_EXTENSION}
	rm *.${UML_FILE_EXTENSION}

.PHONY: uml

clean:
	rm -rf $(VENV)
	find . -name "__pycache__" -exec rm -rf {} +

.PHONY: clean

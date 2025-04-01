VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
REQUIREMENTS_FILE := requirements.txt

PROJECT_NAME := mastermind
ROOT_FOLDER := src
TESTS_FOLDER := tests
UML_FOLDER := docs/img/c4


all: run
.PHONY: all

.env:
	echo 'ERROR: No environment variable configured'
	exit 1

$(VENV)/bin/activate:
	python3.13 -m venv $(VENV)
	$(PIP) install --upgrade pip


install: $(VENV)/bin/activate
	$(PIP) install -r ${REQUIREMENTS_FILE}

requirements:
	$(PIP) freeze > ${REQUIREMENTS_FILE}

run: install .env
	rm src/infra/database/mastermind.db
	$(PYTHON) main.py

tests: install
	pytest ${TESTS_FOLDER}

coverage: install
	pytest --cov=${ROOT_FOLDER} --cov-report=term-missing --cov-fail-under=10 ${TESTS_FOLDER}

.PHONY: install requirements run tests coverage


UML_FILE_EXTENSION := dot
UML_IMAGE_EXTENSION := png
UML_FILE_NAME_TO_CONVERT := classes
UML_GENERATED_FILE_NAME := code
UML_FILE_TO_CONVERT := ${UML_FILE_NAME_TO_CONVERT}.${UML_IMAGE_EXTENSION}

uml: install
	pyreverse -o ${UML_FILE_EXTENSION} -p ${PROJECT_NAME} ${ROOT_FOLDER}/.
	dot -Tpng ${UML_FILE_NAME_TO_CONVERT}_${PROJECT_NAME}.${UML_FILE_EXTENSION} -o ${UML_FILE_TO_CONVERT}
	mv ${UML_FILE_TO_CONVERT} ${UML_FOLDER}/${UML_GENERATED_FILE_NAME}.${UML_IMAGE_EXTENSION}
	rm *.${UML_FILE_EXTENSION}

.PHONY: uml


tree:
	tree -dL 6 --gitignore -I 'docs|__pycache__'


clean:
	rm -rf $(VENV)
	rm *.${UML_FILE_EXTENSION}
	rm *.${UML_IMAGE_EXTENSION}
	rm .env
	find . -name "__pycache__" -exec rm -rf {} +

.PHONY: clean

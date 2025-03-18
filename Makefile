requirements_file := requirements.txt
tests_folder := tests/

all: run
.PHONY: all

install:
	pip install -r ${requirements_file}

requirements:
	pip freeze > ${requirements_file}

run:
	./venv/bin/python main.py

tests:
	pytest ${tests_folder}

coverage:
	pytest --cov=src --cov-report=term-missing --cov-fail-under=10 ${tests_folder}

.PHONY: install requirements run tests coverage

requirements_file := requirements.txt

all: run
.PHONY: all

install:
	pip install -r ${requirements_file}

requirements:
	pip freeze > ${requirements_file}

run:
	./venv/bin/python main.py

tests:
	./venv/bin/python -m unittest tests/libs/test_singleton.py

coverage:
	pytest --cov=src --cov-report=term-missing --cov-fail-under=10 tests/

.PHONY: install requirements run tests coverage

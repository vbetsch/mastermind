requirements_file := requirements.txt

all: run
.PHONY: all

install:
	pip install -r ${requirements_file}

requirements:
	pip freeze > ${requirements_file}

run:
	./venv/bin/python src/main.py

tests:
	./venv/bin/python -m unittest tests/libs/test_singleton.py

.PHONY: install requirements run tests

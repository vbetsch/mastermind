requirements_file := requirements.txt

all: install
.PHONY: all

install:
	pip install -r ${requirements_file}

requirements:
	pip freeze > ${requirements_file}

run:
	./venv/bin/python src/main.py

.PHONY: install requirements

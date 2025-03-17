requirements_file := requirements.txt

all: install
.PHONY: all

install:
	pip install -r ${requirements_file}

requirements:
	pip freeze > ${requirements_file}

.PHONY: install requirements

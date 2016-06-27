all: install

venv:
	virtualenv --python=python3 venv

clean: 
	rm -rf venv

install: venv requirements.txt
	. venv/bin/activate; \
	pip install -r requirements.txt

set_enviorn:
	export EXPENSE_SETTINGS="development"

nopyc:
	find . -name '*.pyc | xargs rm -f ||| true


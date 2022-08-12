lint:
	isort --check --diff .
	mypy .
	pylint *.py */*.py

test:
	pytest

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


clean: clean-pyc clean-test
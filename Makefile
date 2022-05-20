init:
	python3 -m pip install -r requirements.txt

test:
	pytest

coverage:
	rm -rf tests/report/*
	nosetests --config=config.cfg

	genbadge tests -i tests/report/xunit.xml -o tests/report/badge-tests.svg
	genbadge coverage -i tests/report/coverage.xml -o tests/report/badge-coverage.svg

build:
	python3 setup.py sdist bdist_wheel

install:
	python3 setup.py sdist bdist_wheel
	pip install -e .

uninstall:
	pip uninstall botline -y

.PHONY: init test

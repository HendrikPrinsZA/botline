init:
	pip install -r requirements.txt

test:
	pytest

coverage:
	rm -rf reports/coverage/*
	rm -rf reports/status/*

	pytest --junitxml=reports/status/junit.xml --html=reports/status/report.html
	genbadge tests --input-file=reports/status/junit.xml -o reports/status/badge.svg

	coverage xml -o reports/coverage/coverage.xml
	coverage html -d reports/coverage
	genbadge coverage --input-file=reports/coverage/coverage.xml --output-file=reports/coverage/badge.svg

install:
	python3 setup.py sdist bdist_wheel
	pip install -e .

uninstall:
	pip uninstall botline -y
	
.PHONY: init test
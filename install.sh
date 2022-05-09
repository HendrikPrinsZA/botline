#!/bin/bash

# ref https://towardsdatascience.com/how-to-publish-a-python-package-to-pypi-7be9dd5d6dcd
# python -m pip install –-user –-upgrade setuptools wheel

# setup 
python3 setup.py sdist bdist_wheel

# install
pip install -e .

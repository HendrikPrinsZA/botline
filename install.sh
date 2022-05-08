#!/bin/bash

# setup 
python3 setup.py sdist bdist_wheel

# install
pip install -e .
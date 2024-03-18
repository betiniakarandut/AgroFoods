#!/bin/bash

# Lint Python files using Flake8
flake8 --max-line-length 88 .

# Auto-fix linting issues using autopep8
autopep8 --in-place --aggressive --aggressive /*.py

#!/usr/bin/env python
from setuptools import setup

# Minimal shim: calling setup() without arguments defers to pyproject.toml metadata (PEP 621)
# This file exists for tools/legacy workflows that expect setup.py to be present.
if __name__ == "__main__":
    setup()

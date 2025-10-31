name: Run Pylint

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pylint

      - name: Run Pylint
        run: |
          # Run pylint on all Python files, ignoring missing __init__.py warnings
          pylint $(git ls-files '*.py') || true

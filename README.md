# Test Coverage Cases Repository

This repository contains various test cases for analyzing Python code coverage tools. It includes different scenarios and edge cases to validate coverage analysis functionality.

## Structure
- `src/`: Source code with various test cases
  - `simple/`: Basic functions and classes
  - `complex/`: Nested classes and inheritance
  - `utils/`: Utility functions and decorators
  - `circular/`: Circular import examples

- `tests/`: Corresponding test files
  - Coverage varies between fully tested, partially tested, and untested

## Installation
```bash
pip install -r requirements.txt
```

## Running Tests
```bash
pytest
```

## Coverage Report
```bash
pytest --cov=src tests/
```

# Makefile

.PHONY: install init lint format typecheck test all

# 0. Initialize the local development environment
install:
	pip install -e ".[dev]"

init: install
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type pre-push

# 1. Check for programming errors and style violations
lint:
	ruff check .

# 2. Automatically fix formatting issues
format:
	ruff format .

# 3. Run static type checking
typecheck:
	mypy app

# 4. Run the test suite
test:
	pytest

# 5. Run everything sequentially (Great for a complete local pass)
all: lint format typecheck test

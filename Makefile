.PHONY: help install test lint format check typecheck clean

# Default target
help:
	@echo "Available targets:"
	@echo "  make install    - Install dependencies with Poetry"
	@echo "  make test       - Run tests with pytest"
	@echo "  make lint       - Run ruff linter"
	@echo "  make format     - Format code with ruff"
	@echo "  make typecheck  - Run mypy type checker"
	@echo "  make check      - Run all checks (lint, typecheck, test)"
	@echo "  make clean      - Remove build artifacts"

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .
	poetry run ruff check --fix .

typecheck:
	poetry run mypy .

check: lint typecheck test

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	rm -rf dist build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

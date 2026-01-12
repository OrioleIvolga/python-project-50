.PHONY: lint

lint:
	uv run ruff check .

test:
	uv run pytest --cov=gendiff --cov-report=term-missing
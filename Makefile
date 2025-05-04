install:
	uv sync

help:
	uv run -- gendiff -h

FILE1 ?= /home/dixon/python-project-50/file1.json
FILE2 ?= /home/dixon/python-project-50/file2.json

difference:
	uv run gendiff $(FILE1) $(FILE2)

build:
	uv build

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

package-install:
	uv tool install dist/*.whl

package-reassemble:
	uv tool install --force dist/*.whl

check-lint:
	uv run ruff check gendiff

fix-lint:
	uv run ruff check --fix gendiff
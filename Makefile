install:
	uv sync

help:
	uv run -- gendiff -h

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reassemble:
	uv tool install --force dist/*.whl

check-lint:
	uv run ruff check brain_games

fix-lint:
	uv run ruff check --fix brain_games
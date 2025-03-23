brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

package-install:
	uv tool install --reinstall dist/*.whl

package-reinstall: 
	uv tool install dist/*.whl --force

lint:
	uv run ruff check brain_games

ruff-fix:
	uv run ruff check --fix

build:
	uv build
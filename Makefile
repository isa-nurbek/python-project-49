brain-games:
	uv run brain-games

package-install:
	uv tool install --reinstall dist/*.whl

package-reinstall: 
	uv tool install dist/*.whl --force

lint:
	uv run ruff check brain_games

build:
	uv build
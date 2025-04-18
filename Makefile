brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

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
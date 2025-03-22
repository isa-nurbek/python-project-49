brain-games:
	uv run brain-games

package-install:
	uv tool install --reinstall dist/*.whl

package-reinstall: 
	uv tool install dist/*.whl --force

build:
	uv build
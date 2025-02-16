clean:
	rm -rf dist/ build/ *.egg-info

build: clean
	python -m build

test:
	pip install ".[all]"
	black --check .
	flake8

upload: build
	twine upload dist/*

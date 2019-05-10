.PHONY: all clean build test release

all: build

clean:

	rm -rf *.c
	rm -rf *.egg-info
	rm -rf *.pyi
	rm -rf *.so
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist

build: clean

	pip install --upgrade black

	black .

	python generate.py

	pip install --upgrade setuptools

	CFLAGS="-Werror -Wno-deprecated-declarations" python setup.py develop sdist bdist_wheel

test: build

	pip install --upgrade hypothesis
	pip install --upgrade pytest
	pip install --upgrade pytest-forked
	pip install --upgrade pytest-xdist

	# pytest --forked --numprocesses auto --verbose --verbose

release: test

	pip install --upgrade twine

	twine check dist/*
	twine upload dist/*

	python -c 'from generate import API; print("APIs:", len(API))'

build-35:

	pip install --upgrade setuptools

	CFLAGS="-Werror -Wno-deprecated-declarations" python develop setup.py sdist

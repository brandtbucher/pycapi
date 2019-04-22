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

	pip3 install --upgrade black

	black .

	python3 generate.py

	pip3 install --upgrade setuptools

	CFLAGS="-Werror -Wno-deprecated-declarations" python3 setup.py sdist develop

test: build

	pip3 install --upgrade hypothesis
	pip3 install --upgrade pytest
	pip3 install --upgrade pytest-forked
	pip3 install --upgrade pytest-xdist

	# pytest --forked --numprocesses auto --verbose --verbose

release: test

	pip3 install --upgrade twine

	twine check dist/*
	twine upload dist/*

	python3 -c 'from generate import API; print("APIs:", len(API))'

build-35:

	pip3 install --upgrade setuptools

	CFLAGS="-Werror -Wno-deprecated-declarations" python3 setup.py sdist develop

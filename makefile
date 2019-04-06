.PHONY: all clean build test release

all: build

clean:

	rm -rf *.egg-info
	rm -rf *.so
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist

build: clean

	pip3 install --upgrade black && black *.py; true
	pip3 install --upgrade setuptools

	CFLAGS="-Werror -Wno-deprecated-declarations" python3 setup.py sdist develop

test: build

	# pip3 install --upgrade hypothesis
	# pip3 install --upgrade pytest
	# pip3 install --upgrade pytest-forked

	# pytest --forked --verbose --verbose

release: test

	pip install --upgrade twine

	twine check dist/*
	twine upload dist/*

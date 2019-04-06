.PHONY: all clean build test release

export CFLAGS = -Werror -Wno-deprecated-declarations

all: build

clean:

	rm -rf *.egg-info *.so MANIFEST build dist

build: clean

	pip3 install -r requirements.txt
	python3 setup.py clean build sdist develop

test: build

	black *.py
	pylint *.py
	mypy --strict *.py

	python3 setup.py check
	twine check dist/*

	# pytest --forked --verbose --verbose

release: test

	twine upload dist/*

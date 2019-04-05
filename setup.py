from pathlib import Path
from setuptools import Extension, setup  # type: ignore


if __name__ == "__main__":

    with (Path(__file__).parent / "README.md").open() as file:
        long_description = file.read()

    setup(
        author="Brandt Bucher",
        author_email="brandtbucher@gmail.com",
        description="Python bindings to the CPython C API.",
        ext_modules=[
            Extension(
                extra_compile_args=["-Wno-deprecated-declarations"],
                name="pycapi",
                sources=["pycapi.c"],
            )
        ],
        keywords="API C CPython Python",
        license="MIT",
        long_description=long_description,
        long_description_content_type="text/markdown",
        name="pycapi",
        url="https://github.com/brandtbucher/pycapi",
        version="0.8.0",
    )

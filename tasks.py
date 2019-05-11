import invoke
import sys


ARTIFACTS = {"*.c", "*.egg-info", "*.pyi", "*.so", "MANIFEST", "build", "dist"}


@invoke.task
def clean(context):

    context.run("{} setup.py develop --uninstall".format(sys.executable))

    for artifact in sorted(ARTIFACTS):
        context.run("rm -rf {artifact}".format(artifact=artifact))


@invoke.task(clean)
def build(context):

    context.run(
        "{} -m pip install --upgrade -r requirements.txt".format(sys.executable)
    )

    context.run("{} generate.py".format(sys.executable))

    if (3, 5) < sys.version_info:
        context.run("black .")

    context.run(
        'CFLAGS="-Werror -Wno-deprecated-declarations" {} setup.py develop sdist bdist_wheel'.format(
            sys.executable
        )
    )


@invoke.task(build)
def test(context):

    # context.run("mypy --strict .")
    # context.run("pytest")

    pass


@invoke.task(test)
def release(context):
    context.run("twine check dist/*")
    context.run("twine upload dist/*")

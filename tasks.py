import invoke
import sys


ARTIFACTS = ["*.egg-info", "*.so", "MANIFEST", "build", "dist"]


@invoke.task
def clean(context):

    print("\nCLEAN\n")

    context.run("{} setup.py develop --uninstall".format(sys.executable))

    for artifact in sorted(ARTIFACTS):
        context.run("rm -rf {artifact}".format(artifact=artifact))


pre_build = clean


if (3, 6) <= sys.version_info:

    ARTIFACTS.extend(("*.c", "*.pyi"))

    @invoke.task(clean)
    def generate(context):

        print("\nGENERATE\n")

        context.run("{} generate.py".format(sys.executable))
        context.run("black .")

    pre_build = generate


@invoke.task(pre_build)
def build(context):

    print("\nBUILD\n")

    context.run(
        "{} setup.py develop sdist bdist_wheel".format(sys.executable),
        env={"CFLAGS": "-Werror -Wno-deprecated-declarations"},
        replace_env=False,
    )

    context.run("twine check dist/*")


@invoke.task(build)
def test(context):

    print("\nTEST\n")

    if (3, 6) <= sys.version_info:

        context.run(
            "{} -c \"import generate, pycapi; print('APIs:', len([api for api in dir(pycapi) if not api.startswith('_')]), '/', len(generate.API))\"".format(
                sys.executable
            )
        )

    # context.run("mypy --strict .")
    # context.run("pytest")

    pass


@invoke.task(test)
def release(context):

    print("\nRELEASE\n")

    context.run("twine upload dist/*")

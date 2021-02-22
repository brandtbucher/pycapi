import invoke
import sys


ARTIFACTS = ["*.egg-info", "*.so", "MANIFEST", "build", "dist"]

if (3, 6) <= sys.version_info:
    ARTIFACTS.extend(("*.c", "*.pyi"))


@invoke.task
def clean(context):
    context.run("{} setup.py develop --uninstall".format(sys.executable), echo=True)
    for artifact in sorted(ARTIFACTS):
        context.run("rm -rf {artifact}".format(artifact=artifact), echo=True)


@invoke.task(clean)
def generate(context):
    if (3, 6) <= sys.version_info:
        context.run("{} generate.py".format(sys.executable), echo=True)
        context.run("black .", echo=True)


@invoke.task(generate)
def build(context):
    context.run(
        "{} setup.py develop sdist bdist_wheel".format(sys.executable),
        env={"CFLAGS": "-Werror -Wno-deprecated-declarations"},
        replace_env=False,
        echo=True,
    )
    context.run("twine check dist/*", echo=True)


@invoke.task(build)
def test(context):
    if (3, 6) <= sys.version_info:
        context.run(
            "{} -c \"import generate, pycapi; print('APIs:', len([api for api in dir(pycapi) if not api.startswith('_')]), '/', len(generate.API + generate.MACROS))\"".format(
                sys.executable
            ),
            echo=True,
        )
    # context.run("mypy --strict .", echo=True)
    # context.run("pytest", echo=True)

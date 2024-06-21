from invoke import task

from tasks.common import VENV_PREFIX


@task
def coverage(ctx, file=None):
    """
    Run test cases coverage

    Examples:
        # Run all test cases
        $ inv test.coverage

        # Run a specific test file in app/routers/{file}
        $ inv test.coverage --file=workload
        $ inv test.coverage -f=workload

    """
    if file:
        ctx.run(
            f"{VENV_PREFIX} python3 -m pytest --cov=app/routers/{file} --cov-report=term-missing",
            pty=True,
            warn=True,
        )
    else:
        ctx.run(
            f"{VENV_PREFIX} python3 -m pytest --cov=app --cov-report=term-missing",
            pty=True,
            warn=True,
        )


@task
def run(ctx, file=None):
    """
    Run pytest for specified test cases in the app/routers directory or all tests if no file is specified.

    Examples:
        # Run all test cases
        $ inv test.run

        # Run a specific test file in app/routers/{file}
        $ inv test.run --file=workload
        $ inv test.run -f=workload

    """
    if file:
        cmd = f"{VENV_PREFIX} python3 -m pytest app/routers/{file} -p no:warnings"
    else:
        cmd = f"{VENV_PREFIX} python3 -m pytest app -p no:warnings"
    ctx.run(cmd, pty=True, warn=True)

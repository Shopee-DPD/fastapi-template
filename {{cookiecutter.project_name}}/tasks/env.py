import os

from invoke import task

from tasks.common import VENV_PREFIX


@task
def run(ctx):
    """
    Run the app through uvicorn
    """
    if not os.path.exists("./.git/hooks/pre-commit"):
        ctx.run(
            f"{VENV_PREFIX} pre-commit install --hook-type pre-push",
            pty=True,
            warn=True,
        )
    ctx.run(
        f"{VENV_PREFIX} uvicorn app.main:app --reload --host 0.0.0.0",
        pty=True,
        warn=True,
    )

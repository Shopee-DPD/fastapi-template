from invoke import task

from tasks.common import VENV_PREFIX


def _ctx_run(ctx, cmd, task_name, **kwargs) -> None:
    print(f"▶︎ Coding style - {task_name}")

    file_selector = (
        "git diff --name-only --cached | grep '\\.py$' | xargs echo | xargs "
    )

    ctx.run(
        f"{file_selector} {VENV_PREFIX} {cmd}",
        pty=True,
        **kwargs,
    )

    print("\n")


@task
def flake8(ctx) -> None:
    """Check style through flake8"""
    _ctx_run(
        ctx,
        cmd="flake8",
        task_name="Check flake8",
    )


@task
def black(ctx) -> None:
    """Reformat python files through black"""
    _ctx_run(
        ctx,
        cmd="black",
        task_name="Reformat black",
    )


@task
def isort(ctx) -> None:
    """Reformat python files through isort"""
    _ctx_run(
        ctx,
        cmd="isort",
        task_name="Reformat isort",
    )


@task
def black_check(ctx) -> None:
    """Check style through black"""
    _ctx_run(
        ctx,
        cmd="black --check",
        task_name="Check black",
    )


@task
def isort_check(ctx) -> None:
    """Check style through isort"""
    _ctx_run(
        ctx,
        cmd="isort --check-only",
        task_name="Check isort",
    )


@task
def run(ctx, reformat: bool = False) -> None:
    """Check/Reformat style through black, isort and flake8

    Examples:
        # Check style through black, isort, flake8
        $ inv style.run

        # Reformat python files through black and isort
        $ inv style.run --reformat
        $ inv style.run -r

    """
    if reformat:
        isort(ctx)
        black(ctx)
    else:
        black_check(ctx)
        isort_check(ctx)
        flake8(ctx)

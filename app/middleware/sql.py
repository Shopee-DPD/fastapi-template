import pprint as pp
from time import perf_counter
from typing import Any, Callable

from fastapi import Request, Response
from sqlalchemy import event
from sqlalchemy.engine import Engine, ExecutionContext
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from app.database.db import engine


class SQLAlchemyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    def register(self, engine: Engine) -> None:
        event.listen(engine, "before_cursor_execute", self.before_execute, named=True)
        event.listen(engine, "after_cursor_execute", self.after_execute, named=True)

    def unregister(self, engine: Engine) -> None:
        event.remove(engine, "before_cursor_execute", self.before_execute)
        event.remove(engine, "after_cursor_execute", self.after_execute)

    def before_execute(self, context: ExecutionContext, **kwargs: Any) -> None:
        context._start_time = perf_counter()  # type: ignore[attr-defined]

    def after_execute(self, context: ExecutionContext, **kwargs: Any) -> None:
        duration = perf_counter() - context._start_time  # type: ignore[attr-defined]

        query = {
            "duration": f"{duration:.5f}",
            "sql": context.statement,
            "params": context.parameters,
        }
        print("\n")
        pp.pprint(query)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        dash_line = "-" * 50
        print(f"{dash_line} EXECUTE SQL SCRIPT START {dash_line} \n")
        self.register(engine)
        response: Response = await call_next(request)
        self.unregister(engine)
        print(f"\n {dash_line} EXECUTE SQL SCRIPT END {dash_line}")
        return response

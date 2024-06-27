import json
import logging
import pprint as pp
import time
from typing import Callable
from uuid import uuid4

from fastapi import Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Message

logger = logging.getLogger(__name__)
elk_logger = logging.getLogger("app.elk")


class RouterLoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        self._logger = elk_logger
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.perf_counter()

        # await self.set_body(request)
        request_id = str(uuid4())
        request.state.frontend_request_id = request_id
        response = await self.execute_request(call_next, request)
        request_log_dict = await self.parse_request(request)
        response, response_log_dict = await self.parse_response(response)

        execution_time = time.perf_counter() - start_time

        log_dict = {
            "taken_time": f"{execution_time:0.4f}",
            "request-id": request_id,
            **request_log_dict,
            **response_log_dict,
        }
        self._logger.info(
            "middleware-log",
            extra=log_dict,
        )
        pp.pprint(log_dict)
        response.headers["X-API-Request-ID"] = request_id
        response.headers["X-Process-Time"] = str(execution_time)
        return response

    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive() -> Message:
            return receive_

        request._receive = receive

    async def parse_request(self, request: Request) -> dict:
        request_log_dict = {}
        rsq_body = None
        try:
            query_params_str = (
                f"?{request.query_params}" if request.query_params else None
            )
            user = getattr(request.state, "user", {})
            headers = getattr(request, "headers", {})
            request_log_dict = {
                "method": request.get("method"),
                "path": request.get("path"),
                "origin": headers.get("origin", None),
                "content-type": headers.get("content-type", None),
                "user_agent": headers.get("user-agent", None),
                "user_id": user.get("id") if user else None,
                "query": query_params_str,
                "body_rsq": str(rsq_body),
            }
        except Exception as e:
            self._logger.error(f"Error parsing request: {e}")

        return request_log_dict

    async def parse_response(self, response: Response):
        resp_body = None
        response_logging = {}

        if response.status_code < 400:
            overall_status = "successful"
        else:
            overall_status = "failed"
            try:
                if "application/json" in response.headers["Content-Type"]:
                    if "body_iterator" in response.__dict__:
                        resp_body = [
                            section
                            async for section in response.__dict__["body_iterator"]
                        ]
                        response.__setattr__(
                            "body_iterator", AsyncIteratorWrapper(resp_body)
                        )
                        resp_body = json.loads(resp_body[0].decode())
                    else:
                        resp_body = json.loads(response.body.decode())
            except Exception as e:
                self._logger.debug(f"failed to parse response body: {e}")

        response_logging = {
            "status": overall_status,
            "status_code": response.status_code,
            "body_rsp": str(resp_body),
        }

        return response, response_logging

    async def execute_request(self, call_next: Callable, request: Request) -> Response:
        try:
            response: Response = await call_next(request)
        except Exception as e:
            logger.exception(e)
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=jsonable_encoder({"detail": str(e)}),
            )
        return response


class AsyncIteratorWrapper:
    """The following is a utility class that transforms a
    regular iterable to an asynchronous one.

    link: https://www.python.org/dev/peps/pep-0492/#example-2
    """

    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value

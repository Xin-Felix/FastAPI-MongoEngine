import traceback
from asyncio.log import logger
from urllib.request import Request

from fastapi import FastAPI

from responsebody.response import fail


def global_exception(app: FastAPI):
    @app.exception_handler(Exception)  # 全局捕获,
    async def unknown_exception_handler(request: Request,
                                        exc: Exception):
        logger.error(traceback.format_exc())
        return fail(msg=str(exc) if exc.__dict__.get("err_desc") is None else exc.__dict__.get("err_desc"),
                    code=400 if exc.__dict__.get("err_code") is None else exc.__dict__.get("err_code"))


def __init__():
    print("global_exception is init")

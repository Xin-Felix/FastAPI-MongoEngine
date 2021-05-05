from typing import Union

from fastapi import status
from fastapi.responses import JSONResponse, Response  # , ORJSONResponse


# 注意有个 * 号 不是笔误， 意思是调用的时候要指定参数 e.g.resp_200（data=xxxx)
def success(*, data: Union[list, dict, str] = None, code: int = status.HTTP_200_OK,
            msg: str = "success", ) -> Response:
    return JSONResponse(
        status_code=code,
        content={
            'code': code,
            'message': msg,
            'data': data,
        }
    )


def fail(*, data: str = None, msg: str = "bad request", code: int = status.HTTP_400_BAD_REQUEST) -> Response:
    return JSONResponse(
        status_code=code,
        content={
            'code': code,
            'message': msg,
            'data': data,
        }
    )

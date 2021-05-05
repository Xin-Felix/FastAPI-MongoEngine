from fastapi import APIRouter

from exception.my_exception import MyError
from responsebody.response import success

welcome_router = APIRouter()


@welcome_router.get("/error")
async def error():  # 自定义错误
    raise MyError(err_desc="手动抛出错误")
    return success()


@welcome_router.get("/")
async def home():
    return success(msg="项目启动成功")


@welcome_router.get("/403")
async def to_403():
    return success(code=403)


@welcome_router.get("/404")
async def to_404():
    return success(code=404)

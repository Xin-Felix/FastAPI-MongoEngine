from urllib.request import Request

from fastapi import FastAPI

from api.comment.welcome_controller import welcome_router
from api.login.login import login_router
from api.message_controller.data_type_controller import data_type_router
from api.message_controller.data_type_default_controller import data_type_default_router
from api.message_controller.event_controller import event_router
from api.message_controller.step_controller import step_router
from config.setting import init_setting
from exception.global_exception import global_exception
from mapper.init_db import init_db


def init_app(app: FastAPI()):
    """整个项目初始化"""

    app.include_router(welcome_router, tags=["其他api"])
    app.include_router(login_router, tags=["登录校验api"])

    # app.include_router(event_router, dependencies=[Depends(get_current_user)])  # 注册路由,添加依赖,校验token
    app.include_router(event_router, tags=["事件相关api"], prefix="/admin")

    app.include_router(step_router, tags=["步骤相关api"], prefix="/admin")
    app.include_router(data_type_router, tags=["数据字段api"], prefix="/admin")
    app.include_router(data_type_default_router, tags=["数据字段默认值api"], prefix="/admin")

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):  # 请求前拦截器
        """第一步请求进来走这里,然后处理请求"""
        # print(request.__dict__)
        response = await call_next(request)  # 当请求处理完毕后返回响应对象,返回给前端
        response.headers["diy-header"] = str("diy-header")  # 这是自定义响应头,返回给前端
        return response

    global_exception(app)  # 注册全局异常
    init_setting()  # 初始化环境变量
    init_db()  # 初始化数据库

    return app


def __init__():
    print("router is init")

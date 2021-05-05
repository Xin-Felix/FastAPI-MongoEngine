from fastapi import FastAPI

from router.router import init_app  # 启动入口

"""启动方式"""


def init():  # docker启动
    return init_app(FastAPI())  # 初始化


app = init()

if __name__ == '__main__':
    import uvicorn

    app = init()  # 本地启动
    uvicorn.run(app="app:app", host="127.0.0.1", port=8080, log_level="info", reload=True)

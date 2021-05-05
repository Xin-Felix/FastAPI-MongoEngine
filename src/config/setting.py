import os

MONGODB_URL = os.getenv("MONGODB_URL")  # mongodb链接
SECRET_KEY = os.getenv("SECRET_KEY")  # 密钥
ALGORITHM = os.getenv("ALGORITHM")  # 算法
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")  # 过期时间


def init_setting():  # 初始化设置
    print("setting is init")

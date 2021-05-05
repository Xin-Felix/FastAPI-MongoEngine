from mongoengine import *

from config.setting import MONGODB_URL

mongodb = connect(host=MONGODB_URL)  # 连接数据库


def init_db():  # 初始化数据库
    print("databases is init")

import datetime

from mapper.init_db import *


class Comment(Document):  # 评论
    user = StringField(required=True)  # 用户名
    content = StringField(required=True)  # 评论内容
    time = DateTimeField(default=datetime.datetime.now())  # 评论时间

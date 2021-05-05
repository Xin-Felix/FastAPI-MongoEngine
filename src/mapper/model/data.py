import datetime

from mapper.init_db import *
from mapper.model.comment import Comment
from mapper.model.step import Step
from mapper.model.user_auth import UserAuth


class Data(DynamicDocument):  # 储存的数据,动态不固定
    user_auth = ListField(ReferenceField(UserAuth))  # 关联用户权限
    user = StringField(required=True)  # 创建订单用户
    step = ReferenceField(Step)  # 对应步骤
    time = DateTimeField(default=datetime.datetime.now())  # 创建时间
    comment = ListField(ReferenceField(Comment))  # 关联评论

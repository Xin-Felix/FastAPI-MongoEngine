from mapper.init_db import *


class UserAuth(Document):  # 用户权限
    user_name = StringField(required=True)  # 用户名
    user_auth = ListField(choices=[1, 2, 3, 4])  # 权限列表[1,2,3]

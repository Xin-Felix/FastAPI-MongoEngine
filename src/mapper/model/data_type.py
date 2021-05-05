from mapper.init_db import *
from mapper.model.step import Step


class DataType(Document):  # 数据结构
    data_name = StringField(required=True)  # 名称
    data_type = IntField(default=1, choices=[1, 2, 3, 4, 5, 6])  # 输入框,下拉框,单选框,多选框等等
    data_des = StringField(default=None)  # 描述,提示
    data_must = IntField(default=1, choices=[1, 2])  # 是否必填
    step = ReferenceField(Step, required=True)
    data_use = IntField(default=1, choices=[1, 2])  # 是否使用

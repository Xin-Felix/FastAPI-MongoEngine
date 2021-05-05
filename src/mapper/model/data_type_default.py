from mapper.init_db import *
from mapper.model.data_type import DataType


class DataTypeDefault(Document):  # 默认参数
    key = StringField(required=True)  # key
    value = StringField(required=True)  # value
    data_type = ReferenceField(DataType, required=True)  # 关联字段

from mapper.init_db import *
from mapper.model.data import Data
from mapper.model.event import Event
from mapper.model.step import Step


class EventData(Document):  # 步骤对应模板对应的数据
    event_id = ReferenceField(Event)  # 关联事件
    data = ListField(ReferenceField(Data))  # 关联步骤数据 一对多,多个数据
    curr_step = ReferenceField(Step)  # 当前步骤

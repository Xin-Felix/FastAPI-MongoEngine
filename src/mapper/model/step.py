from mapper.init_db import *
from mapper.model.event import Event


class Step(Document):  # 步骤
    event = ReferenceField(Event, required=True)
    step_name = StringField(required=True)  # 步骤名

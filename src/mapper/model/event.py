from mapper.init_db import *
from mapper.service.event_service import EventService


class Event(Document):  # 事件

    meta = {'queryset_class': EventService}

    event_name = StringField(required=True, unique=True)  # 事件名

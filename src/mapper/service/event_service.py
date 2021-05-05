from json import loads

from mongoengine import QuerySet


class EventService(QuerySet):  #
    def get_all_message(self, message: str = ''):
        events = self.filter(event_name=message)  # 查询
        return loads(events.to_json())

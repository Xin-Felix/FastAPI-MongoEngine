import json

from bson import ObjectId
from fastapi import APIRouter

from exception.my_exception import MyError
from mapper.model.event import Event
from responsebody.response import success
from validator.event import CheckEvent

event_router = APIRouter()


@event_router.post("/add_event")
async def add_event(event: CheckEvent):
    Event(**event.dict()).save()
    return success()


@event_router.put("/update_event")  # 更新操作
async def update_event(event: CheckEvent, event_id: str):
    events = Event.objects(id=ObjectId(event_id)).first()
    if not events:
        raise MyError(err_desc="事件信息未找到")
    events.update(**event.dict())
    return success()


@event_router.get("/get_all_event")
async def get_all_event():
    events = Event.objects
    return success(data=json.loads(events.to_json()))

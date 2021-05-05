import json

from bson import ObjectId
from fastapi import APIRouter

from exception.my_exception import MyError
from mapper.model.event import Event
from mapper.model.step import Step
from responsebody.response import success
from validator.step import CheckStep

step_router = APIRouter()


@step_router.post("/add_step")
async def add_step(step: CheckStep, event_id: str):
    event = Event.objects(id=ObjectId(event_id)).first()
    if not event:
        raise MyError(err_desc="事件信息未找到")
    Step(**step.dict(), event=event).save()
    return success()


@step_router.get("/get_step_by_event")
async def get_step_by_event(event_id: str):
    step = Step.objects(event=ObjectId(event_id))
    return success(data=json.loads(step.to_json()))


@step_router.put("/update_step")  # 更新操作
async def update_step(step: CheckStep, step_id: str):
    Step(id=ObjectId(step_id)).update(**step.dict())
    return success()

from pydantic import BaseModel


class CheckEvent(BaseModel):  # 事件
    event_name: str  # 事件名

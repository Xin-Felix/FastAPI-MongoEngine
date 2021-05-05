from pydantic import BaseModel


class CheckStep(BaseModel):  # 事件
    step_name: str  # 事件名

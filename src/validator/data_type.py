from pydantic import BaseModel


class CheckDataType(BaseModel):
    data_name: str  # 名称
    data_type: int = 1  # 输入框,下拉框,单选框,多选框等等
    data_des: str = None  # 描述,提示
    data_must: int = 1  # 是否必填
    data_use: int = 1  # 是否使用

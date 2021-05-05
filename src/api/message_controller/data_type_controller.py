import json

from bson import ObjectId
from fastapi import APIRouter

from exception.my_exception import MyError
from mapper.model.data_type import DataType
from mapper.model.data_type_default import DataTypeDefault
from mapper.model.step import Step
from responsebody.response import success
from validator.data_type import CheckDataType

data_type_router = APIRouter()


@data_type_router.post("/add_data_type")
async def add_data_type(data_type: CheckDataType, step_id: str):
    step = Step.objects(id=ObjectId(step_id)).first()
    if not step:
        raise MyError(err_desc="步骤信息未找到")
    DataType(**data_type.dict(), step=step).save()
    return success()


@data_type_router.get("/get_data_type_by_step")
async def get_data_type_by_step(step_id: str):
    data_type = DataType.objects(step=ObjectId(step_id))
    data_type_dict = json.loads(data_type.to_json())
    print(data_type_dict)
    for i in range(len(data_type_dict)):
        data_type_dict[i]["data_type_default_list"] = json.loads(
            DataTypeDefault.objects(data_type=ObjectId(data_type[i].id)).to_json())
    return success(data=data_type_dict)

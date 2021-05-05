from bson import ObjectId
from fastapi import APIRouter

from exception.my_exception import MyError
from mapper.model.data_type import DataType
from mapper.model.data_type_default import DataTypeDefault
from responsebody.response import success
from validator.data_type_default import CheckDataTypeDefault

data_type_default_router = APIRouter()


@data_type_default_router.post("/add_data_type_default")
async def add_data_type_default(data_type_default: CheckDataTypeDefault, data_type_id: str):
    data_type = DataType.objects(id=ObjectId(data_type_id)).first()
    if not data_type:
        raise MyError(err_desc="字段信息未找到")
    DataTypeDefault(**data_type_default.dict(), data_type=data_type).save()
    return success()


@data_type_default_router.put("/update_data_type_default")
async def add_data_type_default(data_type_default: CheckDataTypeDefault, data_type_default_id: str):
    DataTypeDefault.objects(id=ObjectId(data_type_default_id)).update(**data_type_default.dict())
    return success()

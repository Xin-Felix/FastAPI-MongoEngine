from datetime import timedelta

from fastapi import APIRouter
from pydantic import BaseModel

from config.setting import ACCESS_TOKEN_EXPIRE_MINUTES
from responsebody.response import success
from util.jwt.create_token import create_access_token

login_router = APIRouter()


class User(BaseModel):
    username: str
    password: str


@login_router.post("/token")
async def login_for_access_token(user: User):
    # 生成并返回token信息
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"data": user.dict()}, expires_delta=access_token_expires
    )
    return success(data="Bearer " + access_token)

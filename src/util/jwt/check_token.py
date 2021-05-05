import jwt
from fastapi import Header
from jwt import PyJWTError

from config.setting import SECRET_KEY, ALGORITHM
from exception.my_exception import MyError
# 检查是否携带token
from util.jwt.create_token import pwd_context


# 检查token
async def get_current_user(authorization: str = Header(..., alias="Authorization")):  # 解析token
    if len(authorization) < 8:
        raise MyError(err_desc="token异常")

    authorization = authorization[7:]
    try:
        payload = jwt.decode(authorization, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload.get("data"))
    except PyJWTError:
        raise MyError(err_desc="token异常")


# 校验哈希密码
def verify_password(plain_password, hashed_password):  # 原未加密密码  已加密的hash密码
    return pwd_context.verify(plain_password, hashed_password)

from datetime import datetime, timedelta
from typing import Optional

import jwt
from passlib.context import CryptContext

from config.setting import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 生成token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=30)):
    secret = data.copy()
    secret.update({"expires_delta": datetime.utcnow() + expires_delta})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# 密码哈希
def get_password_hash(pwd):
    return pwd_context.hash(pwd)

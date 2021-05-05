from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):  # 评论
    user: str  # 用户名
    content: str  # 评论内容
    time: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 评论时间

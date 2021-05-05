from pydantic import BaseModel


class CheckDataTypeDefault(BaseModel):
    key: str  # key
    value: str  # value

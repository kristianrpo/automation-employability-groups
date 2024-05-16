from pydantic import BaseModel

class MessageParams(BaseModel):
    msg: str

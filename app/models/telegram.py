from pydantic import BaseModel

class Telegram(BaseModel):
    api_id: int
    api_hash: str
    entity: str
    sessionstring: str
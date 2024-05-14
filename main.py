from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

app = FastAPI()

class TelegramParams(BaseModel):
    api_id: int
    api_hash: str
    entity: str
    sessionstring: str
    msg: str

@app.post("/send_message_telegram/")
async def send_telegram_message(params: TelegramParams):
    try:
        client = TelegramClient(StringSession(params.sessionstring), params.api_id, params.api_hash)
        await client.start()
        chat = await client.get_entity(params.entity)
        await client.send_message(chat, params.msg)
        await client.disconnect()
        return [{"result": {"sender_chat":{"title":chat.title}}}]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
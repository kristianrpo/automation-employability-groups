from fastapi import FastAPI, HTTPException, Depends
from app.models.message_params import MessageParams
from app.services.message_service import MessageService
from app.services.service_registry import ServiceRegistry
from app.services.telegram_service import TelegramService
from fastapi import Depends, FastAPI, HTTPException
from typing import Dict

app = FastAPI()

service_registry = ServiceRegistry()

@app.on_event("startup")
async def on_startup_event():
    service_registry.register_service("telegram", TelegramService())

@app.post("/send_message/{platform}")
async def send_message_endpoint(platform: str, params: MessageParams, service: MessageService = Depends(service_registry.get_service)):
    try:
        result = await service.send_message(params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

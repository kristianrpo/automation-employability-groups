from fastapi import Depends, FastAPI, HTTPException
from fastapi import FastAPI, HTTPException, Depends
from typing import Union
from app.services_factory.service_factory import ServiceFactory
from app.models.telegram_service_model import TelegramModel
from app.services_factory.service_telegram_factory import TelegramFactory
from app.utils.active_services import ActiveServices

app = FastAPI()

active_services = ActiveServices()

@app.on_event("startup")
async def on_startup_event():
    active_services.register_factory_service("telegram", TelegramFactory())

@app.post("/send_message/{platform}")
async def send_message_endpoint(platform: str, params: Union[TelegramModel], serviceFactory: ServiceFactory = Depends(active_services.get_factory_service)):
    try:
        service = serviceFactory.create_service(params)
        result = await service.send_message()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI, HTTPException, Depends
from app.models.telegram import Telegram
from app.services.message_service import MessageService
from app.services.service_registry import ServiceRegistry
from app.services.telegram_service import TelegramService
from fastapi import Depends, FastAPI, HTTPException
from typing import Union

app = FastAPI()

service_registry = ServiceRegistry()

@app.on_event("startup")
async def on_startup_event():
    """
    Function to handle the startup event of the application.
    It registers the Telegram service in the service registry.
    """
    service_registry.register_service("telegram", TelegramService())

@app.post("/send_message/{platform}")
async def send_message_endpoint(platform: str, params: Union[Telegram], service: MessageService = Depends(service_registry.get_message_service)):
    """
    Send a message to a specified platform.

    Parameters:
    - platform (str): The platform to send the message to.
    - params (Union[Telegram]): The parameters required to send the message.
    - service (MessageService): The message service to use for sending the message.

    Returns:
    - The result of sending the message.

    Raises:
    - HTTPException: If an error occurs while sending the message.
    """
    try:
        result = await service.send_message(params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from abc import ABC, abstractmethod
from app.models.message_params import MessageParams

class MessageService(ABC):
    @abstractmethod
    async def send_message(self, params: MessageParams):
        pass

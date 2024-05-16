from abc import ABC, abstractmethod
from app.models.message_params import MessageParams

class MessageService(ABC):
    """Abstract base class for message services."""

    @abstractmethod
    async def send_message(self, params: MessageParams):
        """Send a message using the specified parameters.

        Args:
            params (MessageParams): The parameters for sending the message.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

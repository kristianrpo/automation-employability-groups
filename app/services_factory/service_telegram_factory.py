from .service_factory import ServiceFactory
from app.services.telegram_service import TelegramService

class TelegramFactory(ServiceFactory):
    """
    Factory class for creating TelegramService instances.
    """
    
    def create_service(self, params):
        """
        Creates and returns a TelegramService instance.

        Parameters:
        - msg (str): The message to be passed to the TelegramService.
        - api_id_telegram (int): The API ID for the Telegram service.
        - api_hash_telegram (str): The API hash for the Telegram service.
        - entity_telegram (str): The entity for the Telegram service.
        - sessionstring_telegram (str): The session string for the Telegram service.

        Returns:
        - TelegramService: An instance of the TelegramService class.
        """
        return TelegramService(params.msg,params)
    
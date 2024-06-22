from .service_model import ServiceModel

class TelegramModel(ServiceModel):
    """
    Represents a Telegram model.

    Attributes:
        api_id_telegram (int): The API ID for Telegram.
        api_hash_telegram (str): The API hash for Telegram.
        entity_telegram (str): The entity for Telegram.
        sessionstring_telegram (str): The session string for Telegram.
    """
    api_id_telegram: int
    api_hash_telegram: str
    entity_telegram: str
    sessionstring_telegram: str
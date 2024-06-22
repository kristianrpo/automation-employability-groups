from .service import Service
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

class TelegramService(Service):
    """
    A class that provides methods to send messages using Telegram.

    Args:
        api_id_telegram (int): The API ID for the Telegram API.
        api_hash_telegram (str): The API hash for the Telegram API.
        entity_telegram (str): The entity ID for the chat or user to send the message to.
        sessionstring_telegram (str): The session string for the Telegram client.
        msg (str): The message to be sent.

    Attributes:
        api_id_telegram (int): The API ID for the Telegram API.
        api_hash_telegram (str): The API hash for the Telegram API.
        entity_telegram (str): The entity ID for the chat or user to send the message to.
        sessionstring_telegram (str): The session string for the Telegram client.
    """

    def __init__(self,msg,params):
        super().__init__(msg,params)
        self.api_id_telegram = params.api_id_telegram
        self.api_hash_telegram = params.api_hash_telegram
        self.entity_telegram = params.entity_telegram
        self.sessionstring_telegram = params.sessionstring_telegram

    async def send_message(self):
        """
        Sends the message using the Telegram client.

        Returns:
            list: A list containing a dictionary with the result of the message sending operation.
        Raises:
            Exception: If an error occurs while sending the message.
        """
        try:
            client = TelegramClient(StringSession(self.sessionstring_telegram), self.api_id_telegram, self.api_hash_telegram)
            await client.start()
            chat = await client.get_entity(self.entity_telegram)
            await client.send_message(chat, self.msg)
            await client.disconnect()
            return [{"result": {"sender_chat": {"title": chat.title}}}]
        except Exception as e:
            raise e

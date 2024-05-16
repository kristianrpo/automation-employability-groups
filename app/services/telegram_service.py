from app.models.telegram import Telegram
from app.services.message_service import MessageService
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

class TelegramService(MessageService):
    """A class that provides methods for sending messages via Telegram."""

    async def send_message(self, params: Telegram):
        try:
            client = TelegramClient(StringSession(params.sessionstring_telegram), params.api_id_telegram, params.api_hash_telegram)
            await client.start()
            chat = await client.get_entity(params.entity_telegram)
            await client.send_message(chat, params.msg)
            await client.disconnect()
            return [{"result": {"sender_chat": {"title": chat.title}}}]
        except Exception as e:
            raise e

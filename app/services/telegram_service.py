from app.models.telegram import Telegram
from app.services.message_service import MessageService
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

class TelegramService(MessageService):
    async def send_message(self, params: Telegram):
        try:
            client = TelegramClient(StringSession(params.sessionstring), params.api_id, params.api_hash)
            await client.start()
            chat = await client.get_entity(params.entity)
            await client.send_message(chat, params.msg)
            await client.disconnect()
            return [{"result": {"sender_chat": {"title": chat.title}}}]
        except Exception as e:
            raise e

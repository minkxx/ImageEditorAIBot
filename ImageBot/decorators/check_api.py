from functools import wraps

from pyrogram.types import Message

from ImageBot.database.get_user_api import get_user_api


async def add_api(client, m):
    TEXT = "Please add your API"
    await client.send_message(
        chat_id=m.chat.id,
        text=TEXT,
        reply_to_message_id=m.id,
    )


def check_api(func):
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        if get_user_api(message.chat.id):
            return await func(client, message, *args, **kwargs)
        else:
            return await add_api(client, message, *args, **kwargs)

    return wrapper

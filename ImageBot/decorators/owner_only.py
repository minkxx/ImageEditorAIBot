from functools import wraps

from pyrogram.types import Message

from ImageBot import ADMIN_USERS_ID


async def admin_msg(client, m):
    TEXT = "You are not an admin to execute this command!"
    await client.send_message(
        chat_id=m.chat.id,
        text=TEXT,
        reply_to_message_id=m.id,
    )


def admin(func):
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        if message.chat.id in ADMIN_USERS_ID:
            return await func(client, message, *args, **kwargs)
        else:
            return await admin_msg(client, message, *args, **kwargs)

    return wrapper

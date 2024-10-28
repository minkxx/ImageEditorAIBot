from pyrogram import filters
from pyrogram.types import Message

from ImageBot import bot
from ImageBot.database.get_user_photo_ids import get_user_photo_id
from ImageBot.services.cloudinary.load_client import load_api_client
from ImageBot.utils.keyboards import photo_edit_keyboard
from ImageBot.decorators.check_api import check_api
from ImageBot.decorators.force_sub import force_sub


@bot.on_message(filters.command("uploaded"))
@force_sub
@check_api
async def uploaded_photos(c: bot, m: Message):
    photo_ids = get_user_photo_id(m.chat.id)
    
    if len(photo_ids) == 0:
        await c.send_message(chat_id=m.chat.id, text="You haven't uploaded anything yet!")
        return

    api_cli = load_api_client(m.chat.id)
    for photo_id in photo_ids:
        url = api_cli.get_secure_url(photo_id)
        await c.send_photo(
            chat_id=m.chat.id,
            photo=url,
            caption="select an operation",
            reply_markup=photo_edit_keyboard(photo_id),
        )

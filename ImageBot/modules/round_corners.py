from pyrogram import filters, enums
from pyrogram.types import CallbackQuery

from ImageBot import bot
from ImageBot.services.cloudinary.load_client import load_api_client
from ImageBot.utils.download_img import download_img_cloudinary
from ImageBot.database.get_user_photo_ids import get_user_photo_id

import os
import time


@bot.on_callback_query(filters.regex(pattern="^(round_corners=.*)$"))
async def round_corners(c: bot, cbq: CallbackQuery):
    image_id = cbq.data.split("=")[-1]
    user_id = cbq.message.chat.id

    photo_id = get_user_photo_id(user_id)

    if image_id in photo_id:
        api_cli = load_api_client(user_id)
        width = await c.ask(chat_id=user_id, text="Enter width of the image (px)")
        radius = await c.ask(
            chat_id=user_id,
            text="Enter radius (px)\nFor a perfect circle radius must be equal to width",
        )
        await c.send_chat_action(chat_id=user_id, action=enums.ChatAction.UPLOAD_PHOTO)
        url = api_cli.round_corners(image_id, width.text, radius.text)
        await c.send_photo(
            chat_id=user_id,
            caption=f"Here's your image with round corners.",
            photo=download_img_cloudinary(
                url, os.path.join("downloads", f"{user_id}-{image_id}.png")
            ),
        )
    else:
        x = await c.send_message(
            chat_id=user_id, text=f"This photo with id='{image_id}' has been deleted."
        )
        time.sleep(2)
        await x.delete()
        await cbq.message.delete()

from pyrogram import filters
from pyrogram.types import Message

from ImageBot import bot

from ImageBot import bot
from ImageBot.database.get_user_photo_ids import get_user_photo_id

from ImageBot.services.cloudinary.load_client import load_api_client

from ImageBot.decorators.force_sub import force_sub
from ImageBot.decorators.check_api import check_api

from ImageBot.utils.keyboards import photo_edit_keyboard


@bot.on_message(filters.photo)
@force_sub
@check_api
async def edit_photo(c: bot, m: Message):
    user_id = m.chat.id
    file_id = m.photo.file_id
    flag = True

    while flag:
        image_public_id_msg = await c.ask(
            chat_id=m.chat.id, text="Enter image public id (unique id)"
        )
        if image_public_id_msg.text in get_user_photo_id(user_id):
            await c.send_message(
                chat_id=user_id,
                text="Public id already in use. Please try something unique.",
            )
            continue
        else:
            flag = False
    image_public_id = image_public_id_msg.text

    dl_img = await c.download_media(
        message=file_id, file_name=f"{user_id}-{image_public_id}.png"
    )

    await c.send_photo(
        chat_id=m.chat.id,
        photo=dl_img,
        caption="select an operation",
        reply_markup=photo_edit_keyboard(image_public_id),
    )

    api_cli = load_api_client(user_id)
    api_cli.upload_image_to_cloudinary(
        image_path=dl_img, image_public_id=image_public_id
    )


@bot.on_message(filters.video)
async def test(c: bot, m: Message):
    print(m.video.file_id)
    await c.send_message(chat_id=m.chat.id, text=f"`{m.video.file_id}`")

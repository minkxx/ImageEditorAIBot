import asyncio
import importlib

from pyrogram import idle

from ImageBot import bot, LOG_GROUP, BOT_NAME, BOT_USERNAME
from ImageBot.modules import ALL_MODULES

from ImageBot.modules.updater import load_restart_msg

HELPABLE = {}


loop = asyncio.get_event_loop()


async def start_bot():
    global HELPABLE
    for module in ALL_MODULES:
        imported_module = importlib.import_module("ImageBot.modules." + module)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.replace(" ", "_").lower()] = (
                    imported_module
                )
    bot_modules = ""
    j = 1
    for i in ALL_MODULES:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print("+===============================================================+")
    print("|                        AI Image Editor                        |")
    print("+===============+===============+===============+===============+")
    print("|                         Modules Loaded                        |")
    print(bot_modules)
    print("+===============+===============+===============+===============+")
    print(f"{BOT_NAME} started")
    print("Sending online status!")
    await bot.send_message(LOG_GROUP, f"Bot started!\n@{BOT_USERNAME}")
    print("Sent!")
    restart_msg = load_restart_msg()
    if restart_msg:
        await bot.edit_message_text(
            chat_id=restart_msg.chat.id,
            message_id=restart_msg.id,
            text="Bot restarted!",
        )
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(start_bot())

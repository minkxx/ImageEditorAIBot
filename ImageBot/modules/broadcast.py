from pyrogram import filters
from pyrogram.types import Message

from ImageBot import bot
from ImageBot.decorators.owner_only import admin
from ImageBot.database.get_all_users import get_users_from_db

blocked_chats = []


@bot.on_message(filters.command("broadcast") & filters.private)
@admin
async def broadcast(c: bot, m: Message):
    if not m.reply_to_message:
        await c.send_message(
            chat_id=m.chat.id,
            text="**⚠️ Please reply to a message to broadcast!!**",
            reply_to_message_id=m.id,
        )
    else:
        msg = await c.send_message(chat_id=m.chat.id, text="`Starting broadcast..`")
        all_users = get_users_from_db()
        done_count = 0
        error_count = 0
        error_text = f"**⚠️ Unable! to broadcast on these chats **"
        for user_id in all_users:
            await msg.edit_text(f"Sending broadcast to user: `{user_id}`")
            try:
                await c.copy_message(
                    chat_id=user_id,
                    from_chat_id=m.chat.id,
                    message_id=m.reply_to_message.id,
                )
                done_count += 1
                await msg.edit_text(f"Broadcast sent to user: `{user_id}`")
            except Exception as e:
                error_text += f"\n `{user_id}`"
                blocked_chats.append(user_id)
                error_count += 1
                await msg.edit_text(f"Unable broadcast to user: `{user_id}`")
        else:
            await msg.delete()
            await c.send_message(
                chat_id=m.chat.id,
                text=f"**✅ Successfully** broadcasted message to {done_count} chats out of {len(all_users)}.\n**⚠️ Error** {error_count} chats",
            )
        if error_count:
            await c.send_message(chat_id=m.chat.id, text=error_text)

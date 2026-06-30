# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import time, re
from config import BOT_USERNAME
from pyrogram.enums import MessageEntityType
from pyrogram import filters
from pyrogram.types import Message
from MADARAMUSIC import app
from MADARAMUSIC.mongo.readable_time import get_readable_time
from MADARAMUSIC.mongo.afkdb import add_afk, is_afk, remove_afk


@app.on_message(filters.command(["fk", "afk", "off", "bye", "ye"], prefixes=["a", "A", "b", "B", "/", "!", "."]))
async def active_afk(_, message: Message):
    if message.sender_chat:
        return

    user_id = message.from_user.id
    reason = (message.text.split(None, 1)[1].strip())[:100] if len(message.command) > 1 else None

    afk_data = {
        "type": "text_reason" if reason else "text",
        "time": time.time(),
        "data": None,
        "reason": reason,
    }
    await add_afk(user_id, afk_data)

    await message.reply_text(
        f"❖ {message.from_user.first_name} ɪs ɴᴏᴡ ᴀғᴋ!" +
        (f"\n\n● ʀᴇᴀsᴏɴ: `{reason}`" if reason else "")
    )


@app.on_message(~filters.me & ~filters.bot & ~filters.via_bot, group=1)
async def chat_watcher_func(_, message: Message):
    if message.sender_chat:
        return

    if message.text:
        lowered = message.text.lower()
        if any(lowered.startswith(prefix + cmd) for prefix in ["/", ".", "!", "a", "b"] for cmd in ["afk", "fk", "off", "bye", "ye"]):
            return

    msg = ""
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    verifier, afk_data = await is_afk(user_id)
    if verifier:
        await remove_afk(user_id)
        seenago = get_readable_time(int(time.time() - afk_data["time"]))
        reason = afk_data["reason"]
        if afk_data["type"] == "text_reason" and reason:
            msg += f"<b>❖ {user_name[:25]}</b> ɪs ʙᴀᴄᴋ ᴀғᴛᴇʀ {seenago}\n\n● ʀᴇᴀsᴏɴ: `{reason}`\n\n"
        else:
            msg += f"<b>❖ {user_name[:25]}</b> ɪs ʙᴀᴄᴋ ᴀғᴛᴇʀ {seenago}\n\n"

    if message.reply_to_message:
        try:
            replied_user = message.reply_to_message.from_user
            if replied_user:
                afk_check, afk_data = await is_afk(replied_user.id)
                if afk_check:
                    seenago = get_readable_time(int(time.time() - afk_data["time"]))
                    reason = afk_data["reason"]
                    if afk_data["type"] == "text_reason" and reason:
                        msg += f"<b>❖ {replied_user.first_name[:25]}</b> ɪs ᴀғᴋ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ: `{reason}`\n\n"
                    else:
                        msg += f"<b>❖ {replied_user.first_name[:25]}</b> ɪs ᴀғᴋ ғᴏʀ {seenago}\n\n"
        except:
            pass

    if message.entities:
        for ent in message.entities:
            try:
                if ent.type == MessageEntityType.MENTION:
                    username = message.text[ent.offset + 1 : ent.offset + ent.length]
                    user = await app.get_users(username)
                elif ent.type == MessageEntityType.TEXT_MENTION:
                    user = ent.user
                else:
                    continue

                afk_check, afk_data = await is_afk(user.id)
                if afk_check:
                    seenago = get_readable_time(int(time.time() - afk_data["time"]))
                    reason = afk_data["reason"]
                    if afk_data["type"] == "text_reason" and reason:
                        msg += f"<b>❖ {user.first_name[:25]}</b> ɪs ᴀғᴋ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ: `{reason}`\n\n"
                    else:
                        msg += f"<b>❖ {user.first_name[:25]}</b> ɪs ᴀғᴋ ғᴏʀ {seenago}\n\n"
            except:
                continue

    if msg:
        await message.reply_text(msg, disable_web_page_preview=True)

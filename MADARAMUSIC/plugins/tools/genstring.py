# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import asyncio
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from MADARAMUSIC import app
from MADARAMUSIC.utils.emojis import (
    E_SPARK, E_STAR, E_CROWN, E_THUNDER, E_FIRE,
    E_GEAR, E_BACK, E_CLOSE, E_DIAMOND, E_GLOBE,
)
import config
from config import BANNED_USERS

SESSION_HELP = """
<blockquote><b>⚡ ᴍᴀᴅᴀʀᴀ ᴍᴜsɪᴄ — sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ</b></blockquote>

<blockquote expandable>
<b>💎 ᴡʜᴀᴛ ɪs ᴀ sᴛʀɪɴɢ sᴇssɪᴏɴ?</b>
A string session lets MADARA MUSIC use your account as an assistant to join voice chats.

<b>🔐 ᴀᴠᴀɪʟᴀʙʟᴇ ᴛʏᴘᴇs:</b>
• <b>Pyrogram v2</b> — recommended (latest)
• <b>Pyrogram v1</b> — legacy / older deployments
• <b>Telethon</b> — alternative library

⚠️ <b>ᴡᴀʀɴɪɴɢ:</b> Never share your string session with anyone. It gives full access to your account.
</blockquote>
"""

CONVERSATION_ACTIVE = {}


def _type_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✨ ᴘʏʀᴏɢʀᴀᴍ ᴠ2",
                callback_data="gs_pyro2",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_SPARK,
            ),
        ],
        [
            InlineKeyboardButton(
                "⚙️ ᴘʏʀᴏɢʀᴀᴍ ᴠ1",
                callback_data="gs_pyro1",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_GEAR,
            ),
            InlineKeyboardButton(
                "🌐 ᴛᴇʟᴇᴛʜᴏɴ",
                callback_data="gs_telethon",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_GLOBE,
            ),
        ],
        [
            InlineKeyboardButton(
                "✖️ ᴄʟᴏsᴇ",
                callback_data="gs_close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ])


@app.on_message(filters.command("genstring") & filters.private & ~BANNED_USERS)
async def genstring_start(client, message: Message):
    await message.reply_text(
        SESSION_HELP,
        reply_markup=_type_keyboard(),
    )


@app.on_callback_query(filters.regex(r"^gs_(pyro2|pyro1|telethon|close)$"))
async def genstring_type_cb(client, cq):
    user_id = cq.from_user.id
    data = cq.data

    if data == "gs_close":
        CONVERSATION_ACTIVE.pop(user_id, None)
        await cq.message.delete()
        return

    lib = {"gs_pyro2": "Pyrogram v2", "gs_pyro1": "Pyrogram v1", "gs_telethon": "Telethon"}[data]

    await cq.message.edit_text(
        f"<blockquote><b>✨ ɢᴇɴᴇʀᴀᴛɪɴɢ: {lib}</b></blockquote>\n\n"
        f"⚡ <b>ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ</b>\n"
        f"<code>Format: +91XXXXXXXXXX</code>\n\n"
        f"⚠️ <i>This is processed securely. Never share with anyone.</i>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="gs_close",
                                 style=ButtonStyle.DANGER, icon_custom_emoji_id=E_CLOSE)
        ]]),
    )
    CONVERSATION_ACTIVE[user_id] = {"step": "phone", "lib": lib}
    await cq.answer()


@app.on_message(filters.private & filters.text & ~BANNED_USERS, group=5)
async def genstring_conversation(client, message: Message):
    user_id = message.from_user.id
    state = CONVERSATION_ACTIVE.get(user_id)
    if not state:
        return

    step = state["step"]
    lib  = state["lib"]

    if step == "phone":
        phone = message.text.strip()
        if not phone.startswith("+") or not phone[1:].isdigit():
            await message.reply_text(
                "❌ <b>ɪɴᴠᴀʟɪᴅ ғᴏʀᴍᴀᴛ.</b>\n\nSend phone as <code>+91XXXXXXXXXX</code>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="gs_close",
                                         style=ButtonStyle.DANGER, icon_custom_emoji_id=E_CLOSE)
                ]]),
            )
            return

        CONVERSATION_ACTIVE[user_id]["phone"] = phone
        CONVERSATION_ACTIVE[user_id]["step"] = "generating"

        wait_msg = await message.reply_text(
            f"<blockquote><b>⚡ ɢᴇɴᴇʀᴀᴛɪɴɢ {lib} sᴇssɪᴏɴ…</b></blockquote>\n\n"
            f"📱 Phone: <code>{phone}</code>\n"
            f"⏳ <i>Starting session — check your Telegram for the OTP…</i>",
        )

        try:
            session_str = await _generate_session(user_id, phone, lib, message, wait_msg)
            if session_str:
                await wait_msg.delete()
                await message.reply_text(
                    f"<blockquote><b>✅ {lib} sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ!</b></blockquote>\n\n"
                    f"<code>{session_str}</code>\n\n"
                    f"⚠️ <b>ᴋᴇᴇᴘ ᴛʜɪs sᴇᴄʀᴇᴛ. ɴᴇᴠᴇʀ sʜᴀʀᴇ ɪᴛ.</b>\n\n"
                    f"💎 Add it as <code>STRING_SESSION</code> in your deployment.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            "✨ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴᴏᴛʜᴇʀ", callback_data="gs_pyro2",
                            style=ButtonStyle.PRIMARY, icon_custom_emoji_id=E_SPARK,
                        )
                    ]]),
                )
        except Exception as e:
            await wait_msg.edit_text(f"❌ <b>ᴇʀʀᴏʀ:</b> <code>{e}</code>")
        finally:
            CONVERSATION_ACTIVE.pop(user_id, None)


async def _generate_session(user_id: int, phone: str, lib: str, message: Message, wait_msg):
    """Generate a Pyrogram or Telethon string session interactively."""
    from pyrogram import Client
    api_id   = config.API_ID
    api_hash = config.API_HASH

    if "Pyrogram" in lib:
        version = 2 if "v2" in lib else 1
        # For Pyrogram, use StringSession
        from pyrogram.types import Message as PyroMessage
        temp_client = Client(
            name=f"_genstr_{user_id}",
            api_id=api_id,
            api_hash=api_hash,
            in_memory=True,
        )
        await temp_client.connect()
        sent_code = await temp_client.send_code(phone)
        otp_msg = await message.reply_text(
            f"⚡ <b>OTP sᴇɴᴛ ᴛᴏ</b> <code>{phone}</code>\n\n"
            f"📩 <b>ᴇɴᴛᴇʀ ᴛʜᴇ OTP ʏᴏᴜ ʀᴇᴄᴇɪᴠᴇᴅ:</b>\n"
            f"<i>Format: 1 2 3 4 5 (with spaces)</i>",
        )
        CONVERSATION_ACTIVE[user_id]["step"] = "otp"
        CONVERSATION_ACTIVE[user_id]["_client"] = temp_client
        CONVERSATION_ACTIVE[user_id]["_code_hash"] = sent_code.phone_code_hash
        CONVERSATION_ACTIVE[user_id]["_otp_msg"] = otp_msg
        CONVERSATION_ACTIVE[user_id]["_result"] = asyncio.Future()
        result_fut = CONVERSATION_ACTIVE[user_id]["_result"]
        try:
            session_str = await asyncio.wait_for(result_fut, timeout=180)
            return session_str
        except asyncio.TimeoutError:
            await temp_client.disconnect()
            raise Exception("OTP timeout — please try again")

    elif lib == "Telethon":
        try:
            from telethon import TelegramClient
            from telethon.sessions import StringSession
        except ImportError:
            raise Exception("Telethon not installed. Add 'telethon' to requirements.txt")

        tl_client = TelegramClient(StringSession(), api_id, api_hash)
        await tl_client.connect()
        await tl_client.send_code_request(phone)
        otp_msg = await message.reply_text(
            f"⚡ <b>OTP sᴇɴᴛ ᴛᴏ</b> <code>{phone}</code>\n\n"
            f"📩 <b>ᴇɴᴛᴇʀ ᴛʜᴇ OTP:</b>",
        )
        CONVERSATION_ACTIVE[user_id]["step"] = "otp_telethon"
        CONVERSATION_ACTIVE[user_id]["_tl"] = tl_client
        CONVERSATION_ACTIVE[user_id]["_otp_msg"] = otp_msg
        CONVERSATION_ACTIVE[user_id]["_result"] = asyncio.Future()
        result_fut = CONVERSATION_ACTIVE[user_id]["_result"]
        try:
            session_str = await asyncio.wait_for(result_fut, timeout=180)
            return session_str
        except asyncio.TimeoutError:
            await tl_client.disconnect()
            raise Exception("OTP timeout — please try again")


@app.on_message(filters.private & filters.text & ~BANNED_USERS, group=6)
async def genstring_otp_handler(client, message: Message):
    user_id = message.from_user.id
    state = CONVERSATION_ACTIVE.get(user_id)
    if not state:
        return

    step = state.get("step")

    if step == "otp":
        otp = message.text.strip().replace(" ", "")
        temp_client = state.get("_client")
        code_hash   = state.get("_code_hash")
        result_fut  = state.get("_result")
        try:
            await temp_client.sign_in(phone=state["phone"], phone_code_hash=code_hash, phone_code=otp)
            session_str = await temp_client.export_session_string()
            await temp_client.disconnect()
            result_fut.set_result(session_str)
        except Exception as e:
            result_fut.set_exception(e)

    elif step == "otp_telethon":
        otp = message.text.strip().replace(" ", "")
        tl = state.get("_tl")
        result_fut = state.get("_result")
        try:
            await tl.sign_in(phone=state["phone"], code=otp)
            session_str = tl.session.save()
            await tl.disconnect()
            result_fut.set_result(session_str)
        except Exception as e:
            result_fut.set_exception(e)

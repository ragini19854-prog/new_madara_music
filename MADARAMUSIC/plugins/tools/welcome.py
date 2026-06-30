# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import os
import random
import asyncio
from logging import getLogger

from pyrogram import Client, filters, enums
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus, ButtonStyle
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops

from MADARAMUSIC import app
from MADARAMUSIC.utils.database import add_served_chat, get_assistant, is_active_chat
from MADARAMUSIC.misc import SUDOERS
from MADARAMUSIC.utils.emojis import E_HEART, E_SPARK, E_STAR, E_MUSIC, E_CROWN

LOGGER = getLogger(__name__)

# ── Resolves asset paths portably ────────────────────
_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets")


def _asset(name):
    return os.path.join(_ASSETS, name)


# ── 4 girl pics used as random welcome photos ─────────
GIRL_PICS = [
    _asset("girl1.png"),
    _asset("girl2.png"),
    _asset("girl3.png"),
    _asset("girl4.png"),
]


class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data.setdefault(chat_id, {"state": "on"})

    async def rm_wlcm(self, chat_id):
        self.data.pop(chat_id, None)


wlcm = WelDatabase()


class temp:
    ME      = None
    CURRENT = 2
    CANCEL  = False
    MELCOW  = {}
    U_NAME  = None
    B_NAME  = None


def circle(pfp, size=(500, 500), brightness_factor=1.1):
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


def _get_welcome_bg():
    """Return welcome card background. Uses girl3 or falls back to wel2.png."""
    candidates = [_asset("girl3.png"), _asset("girl4.png"), _asset("wel2.png")]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None


def welcomepic(pic, user, chatname, user_id, uname, brightness_factor=1.1):
    os.makedirs("downloads", exist_ok=True)

    bg_path = _get_welcome_bg()
    if bg_path:
        background = Image.open(bg_path).convert("RGBA").resize((1280, 720), Image.LANCZOS)
    else:
        background = Image.new("RGBA", (1280, 720), (10, 10, 30, 255))

    # dark overlay so text is readable
    overlay = Image.new("RGBA", background.size, (0, 0, 0, 120))
    background = Image.alpha_composite(background, overlay)

    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, size=(260, 260), brightness_factor=brightness_factor)

    background.paste(pfp, (60, 230), pfp)

    draw = ImageDraw.Draw(background)
    try:
        font_big = ImageFont.truetype(_asset("font.ttf"), size=52)
        font_med = ImageFont.truetype(_asset("font.ttf"), size=36)
        font_sm  = ImageFont.truetype(_asset("font.ttf"), size=28)
    except:
        font_big = font_med = font_sm = ImageFont.load_default()

    # heading
    draw.text((390, 200), "⎊ ᴡᴇʟᴄᴏᴍᴇ ⎊", fill=(255, 215, 0), font=font_big)
    draw.text((390, 275), f"ɴᴀᴍᴇ : {user[:22]}", fill=(255, 255, 255), font=font_med)
    draw.text((390, 330), f"ɪᴅ    : {user_id}", fill=(200, 200, 255), font=font_sm)
    draw.text((390, 375), f"ᴜ     : @{uname if uname else 'None'}", fill=(200, 255, 200), font=font_sm)
    draw.text((390, 425), f"ɢʀᴏᴜᴘ : {chatname[:24]}", fill=(255, 200, 200), font=font_sm)

    out = f"downloads/welcome_{user_id}.png"
    background.convert("RGB").save(out)
    return out


@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = (
        "<blockquote><b>⚡ ᴡᴇʟᴄᴏᴍᴇ ᴄᴏᴍᴍᴀɴᴅ</b></blockquote>\n\n"
        "✅ <code>/welcome on</code> — Enable welcome card\n"
        "❌ <code>/welcome off</code> — Disable welcome card"
    )
    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id
    member  = await app.get_chat_member(chat_id, message.from_user.id)
    if member.status not in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        return await message.reply_text(
            "❌ <b>ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴄʜᴀɴɢᴇ ᴡᴇʟᴄᴏᴍᴇ sᴇᴛᴛɪɴɢs!</b>",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✖️ ᴄʟᴏsᴇ", callback_data="close",
                                     style=ButtonStyle.DANGER, icon_custom_emoji_id=E_SPARK)
            ]]),
        )

    A     = await wlcm.find_one(chat_id)
    state = message.text.split(None, 1)[1].strip().lower()

    if state == "off":
        if A:
            await message.reply_text("⚠️ <b>ᴡᴇʟᴄᴏᴍᴇ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ!</b>")
        else:
            await wlcm.add_wlcm(chat_id)
            await message.reply_text(
                f"❌ <b>ᴡᴇʟᴄᴏᴍᴇ ᴅɪsᴀʙʟᴇᴅ ɪɴ</b> {message.chat.title}",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("✅ ᴇɴᴀʙʟᴇ ᴀɢᴀɪɴ", callback_data="welcome_on",
                                         style=ButtonStyle.SUCCESS, icon_custom_emoji_id=E_HEART)
                ]]),
            )
    elif state == "on":
        if not A:
            await message.reply_text("⚠️ <b>ᴡᴇʟᴄᴏᴍᴇ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ!</b>")
        else:
            await wlcm.rm_wlcm(chat_id)
            await message.reply_text(
                f"✅ <b>ᴡᴇʟᴄᴏᴍᴇ ᴇɴᴀʙʟᴇᴅ ɪɴ</b> {message.chat.title}",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("❌ ᴅɪsᴀʙʟᴇ", callback_data="welcome_off",
                                         style=ButtonStyle.DANGER, icon_custom_emoji_id=E_SPARK)
                ]]),
            )
    else:
        await message.reply_text(usage)


@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id

    A = await wlcm.find_one(chat_id)
    if A:
        return

    if not (member.new_chat_member and not member.old_chat_member):
        return
    if member.new_chat_member.status == "kicked":
        return

    user  = member.new_chat_member.user
    count = await app.get_chat_members_count(chat_id)

    try:
        pic = await app.download_media(user.photo.big_file_id, file_name=f"pp{user.id}.png")
    except:
        pic = _asset("upic.png")

    # Delete old welcome message
    old = temp.MELCOW.get(f"welcome-{chat_id}")
    if old:
        try:
            await old.delete()
        except:
            pass

    try:
        welcomeimg = welcomepic(
            pic,
            user.first_name or "User",
            member.chat.title or "Group",
            user.id,
            user.username,
        )

        msg = await app.send_photo(
            chat_id,
            photo=welcomeimg,
            caption=(
                "<blockquote><b>⎊ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ⎊</b></blockquote>\n\n"
                f"🎵 <b>ɴᴀᴍᴇ :</b> {user.mention}\n"
                f"🆔 <b>ɪᴅ   :</b> <code>{user.id}</code>\n"
                f"👤 <b>ᴜsᴇʀ :</b> @{user.username if user.username else 'None'}\n"
                f"👥 <b>ᴍᴇᴍʙᴇʀs :</b> {count}\n\n"
                f"<i>⭐ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ғᴀᴍɪʟʏ!</i>"
            ),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "👤 ᴠɪᴇᴡ ᴘʀᴏғɪʟᴇ",
                        url=f"tg://openmessage?user_id={user.id}",
                        style=ButtonStyle.PRIMARY,
                        icon_custom_emoji_id=E_STAR,
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                        style=ButtonStyle.SUCCESS,
                        icon_custom_emoji_id=E_MUSIC,
                    ),
                ],
            ]),
        )
        temp.MELCOW[f"welcome-{chat_id}"] = msg

        # Try to clean up profile pic download
        if pic != _asset("upic.png"):
            try:
                os.remove(pic)
            except:
                pass

        # Auto-delete after 5 minutes
        await asyncio.sleep(300)
        try:
            await msg.delete()
        except:
            pass

    except Exception as e:
        LOGGER.error(f"[welcome] error: {e}")

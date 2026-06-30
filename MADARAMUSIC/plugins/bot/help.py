# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import random
from typing import Union
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton
from MADARAMUSIC import app
from MADARAMUSIC.utils import help_pannel
from MADARAMUSIC.utils.database import get_lang
from MADARAMUSIC.utils.decorators.language import LanguageStart, languageCB
from MADARAMUSIC.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT, MADARA_IMG
from strings import get_string, helpers
from MADARAMUSIC.utils.stuffs.buttons import BUTTONS
from MADARAMUSIC.utils.stuffs.helper import Helper

EFFECT_IDS = [
    5046509860389126442,
    5107584321108051014,
    5104841245755180586,
    5159385139981059251,
]

@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            random.choice(MADARA_IMG),
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
            message_effect_id=random.choice(EFFECT_IDS),
        )

@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
        _["help_2"], 
        reply_markup=InlineKeyboardMarkup(keyboard),
        message_effect_id=random.choice(EFFECT_IDS),
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)


@app.on_callback_query(filters.regex("mbot_cb") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_M, reply_markup=InlineKeyboardMarkup(BUTTONS.MBUTTON))


@app.on_callback_query(filters.regex('managebot123'))
async def on_back_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_pannel(_, True)
    if cb == "settings_back_helper":
        await CallbackQuery.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )

@app.on_callback_query(filters.regex('mplus'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"mbot_cb")]])
    if cb == "Okieeeeee":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)
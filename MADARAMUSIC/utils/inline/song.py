from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
from MADARAMUSIC.utils.emojis import E_AUDIO, E_VIDEO, E_CLOSE


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_AUDIO,
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_VIDEO,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ]
    return buttons

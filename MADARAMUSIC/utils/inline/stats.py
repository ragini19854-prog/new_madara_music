from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from MADARAMUSIC.utils.emojis import E_STATS, E_FIRE, E_CLOSE, E_BACK


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["SA_B_1"],
            callback_data="TopOverall",
            style=ButtonStyle.SUCCESS,
            icon_custom_emoji_id=E_FIRE,
        ),
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_2"],
            callback_data="bot_stats_sudo",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_STATS,
        ),
        InlineKeyboardButton(
            text=_["SA_B_3"],
            callback_data="TopOverall",
            style=ButtonStyle.SUCCESS,
            icon_custom_emoji_id=E_FIRE,
        ),
    ]
    upl = InlineKeyboardMarkup([
        sudo if status else not_sudo,
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ])
    return upl


def back_stats_buttons(_):
    upl = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="stats_back",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_BACK,
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        ),
    ]])
    return upl

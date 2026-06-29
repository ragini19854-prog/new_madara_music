from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
from MADARAMUSIC.utils.emojis import (
    E_LOCK, E_LANG, E_GEAR, E_VOICE, E_CLOSE, E_BACK,
    E_CHECK, E_WARN, E_KEY, E_MUSIC,
)


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ST_B_1"],
                callback_data="AU",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_KEY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_3"],
                callback_data="LG",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_LANG,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_2"],
                callback_data="PM",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_MUSIC,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_4"],
                callback_data="VM",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_VOICE,
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


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Vᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜",
                callback_data="VOTEANSWER",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_VOICE,
            ),
            InlineKeyboardButton(
                text=_["ST_B_5"] if mode == True else _["ST_B_6"],
                callback_data="VOMODECHANGE",
                style=ButtonStyle.SUCCESS if mode == True else ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CHECK if mode == True else E_WARN,
            ),
        ],
        [
            InlineKeyboardButton(
                text="-2",
                callback_data="FERRARIUDTI M",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_WARN,
            ),
            InlineKeyboardButton(
                text=f"ᴄᴜʀʀᴇɴᴛ : {current}",
                callback_data="ANSWERVOMODE",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_GEAR,
            ),
            InlineKeyboardButton(
                text="+2",
                callback_data="FERRARIUDTI A",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_CHECK,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_BACK,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ST_B_7"],
                callback_data="AUTHANSWER",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_LOCK,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if status == True else _["ST_B_9"],
                callback_data="AUTH",
                style=ButtonStyle.SUCCESS if status == True else ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CHECK if status == True else E_WARN,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_1"],
                callback_data="AUTHLIST",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_KEY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_BACK,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ST_B_10"],
                callback_data="SEARCHANSWER",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_MUSIC,
            ),
            InlineKeyboardButton(
                text=_["ST_B_11"] if Direct == True else _["ST_B_12"],
                callback_data="MODECHANGE",
                style=ButtonStyle.SUCCESS if Direct == True else ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CHECK if Direct == True else E_WARN,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_13"],
                callback_data="AUTHANSWER",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_VOICE,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Group == True else _["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
                style=ButtonStyle.SUCCESS if Group == True else ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CHECK if Group == True else E_WARN,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_14"],
                callback_data="PLAYTYPEANSWER",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_GEAR,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Playtype == True else _["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
                style=ButtonStyle.SUCCESS if Playtype == True else ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CHECK if Playtype == True else E_WARN,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_BACK,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ]
    return buttons

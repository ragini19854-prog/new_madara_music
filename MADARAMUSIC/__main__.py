import asyncio
import importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import config
from MADARAMUSIC import LOGGER, app, userbot
from MADARAMUSIC.core.call import MADARA
from MADARAMUSIC.misc import sudo
from MADARAMUSIC.plugins import ALL_MODULES
from MADARAMUSIC.utils.database import get_banned_users, get_gbanned

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("String Session Not Filled, Please Fill A Pyrogram Session")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            config.BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            config.BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MADARAMUSIC.plugins" + all_module)
    LOGGER("MADARAMUSIC.plugins").info("✅ All Features Loaded | MADARA MUSIC 🎵")
    await userbot.start()
    await MADARA.start()
    try:
        await MADARA.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("MADARAMUSIC").error(
            "PlZ START YOUR LOG GROUP VOICECHAT/CHANNEL\n\nMADARA MUSIC BOT STOPPED..."
        )
        exit()
    except:
        pass
    await MADARA.decorators()
    LOGGER("MADARAMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  🎵 MADARA MUSIC BOT STARTED\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("MADARAMUSIC").info("🛑 MADARA MUSIC BOT STOPPED..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

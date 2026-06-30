# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
from pyrogram import filters
from pyrogram.types import Message
from MADARAMUSIC import app
from MADARAMUSIC.core.call import MADARA
from MADARAMUSIC.utils.database import set_loop
from MADARAMUSIC.utils.decorators import AdminRightsCheck
from MADARAMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await MADARA.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )

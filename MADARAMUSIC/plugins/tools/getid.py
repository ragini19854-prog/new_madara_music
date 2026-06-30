# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
from pyrogram import filters
from MADARAMUSIC import app
from MADARAMUSIC.misc import SUDOERS

@app.on_message(filters.video & filters.private & SUDOERS)
async def get_video_id(client, message):
    # Jaise hi tu video bhejega, bot uski file_id reply kar dega
    file_id = message.video.file_id
    await message.reply_text(f"**Yᴇ ʀᴀʜɪ Tᴇʀɪ Fɪʟᴇ ID:**\n\n`{file_id}`")
    

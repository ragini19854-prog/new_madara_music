import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Required credentials
API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Bot and owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "YourUsername")
BOT_USERNAME = getenv("BOT_USERNAME", "MadaraMusicBot")
BOT_NAME = getenv("BOT_NAME", "MADARA MUSIC")
ASSUSERNAME = getenv("ASSUSERNAME", "")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Limits and IDs
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", 0))
OWNER_ID = int(getenv("OWNER_ID", 0))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
DEEP_API = getenv("DEEP_API")

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/yourusername/MADARA-MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MadaraMusicSupport")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MadaraMusicChat")

# Assistant settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Song download limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Session strings
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# Miscellaneous
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

DEBUG_IGNORE_LOG = True

###### IMAGE URLS ######

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/ak96mx.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/ak96mx.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/lrwbj6.jpg"
STATS_IMG_URL = "https://files.catbox.moe/ak96mx.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/aesldg.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/aesldg.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/aesldg.jpg"


MADARA_IMG = [
    "https://files.catbox.moe/dw0as6.jpg",
    "https://files.catbox.moe/t2m1pv.jpg",
    "https://files.catbox.moe/lsbotb.jpg",
    "https://files.catbox.moe/huuy1f.jpg",
    "https://files.catbox.moe/7vfivr.jpg",
    "https://files.catbox.moe/dqtuv2.jpg",
    "https://files.catbox.moe/ac3tzn.jpg"
]


# Helper function
def time_to_seconds(time: str) -> int:
    """Convert time string (MM:SS) to total seconds."""
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

# Calculate total duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is invalid. It must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is invalid. It must start with https://")

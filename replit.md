# MADARA MUSIC Bot

A fully-featured Telegram music bot built with Python, Pyrogram, and PyTgCalls. Plays music in Telegram group voice chats from YouTube, Spotify, SoundCloud, Apple Music, Resso, and direct Telegram files.

## Features

- 🎵 Play music in Telegram voice chats
- 📱 Supports YouTube, Spotify, SoundCloud, Apple Music, Resso, Telegram files
- 🎛️ Audio/video streaming with controls (pause, resume, skip, seek, loop, speed)
- 👥 Multi-assistant support (up to 7 string sessions)
- 🌐 Multi-language support (English, Hindi, Arabic, Punjabi)
- 🛡️ Admin tools, ban/unban, group management
- 🎨 Thumbnail generation for now-playing cards
- 🤖 Many extra tools (weather, QR, stickers, translator, etc.)

## Project Structure

```
MADARAMUSIC/           # Main bot package
├── core/              # Bot, call engine, MongoDB, userbot
├── platforms/         # YouTube, Spotify, SoundCloud, Apple, Resso, Telegram APIs
├── plugins/           # All command handlers
│   ├── admins/        # Admin controls (pause, skip, stop, etc.)
│   ├── bot/           # Bot commands (start, help, settings)
│   ├── extra/         # Extra features
│   ├── misc/          # Misc handlers
│   ├── play/          # Play commands
│   └── tools/         # Utility tools
├── utils/             # Helpers, database, thumbnails, formatters
└── mongo/             # MongoDB collection helpers
config.py              # All configuration (loaded from env vars)
strings/               # Multi-language string files
requirements.txt       # Python dependencies
```

## Setup

### Required Environment Variables

Set these in the Replit Secrets panel:

| Variable | Description |
|---|---|
| `API_ID` | Telegram API ID from my.telegram.org |
| `API_HASH` | Telegram API Hash from my.telegram.org |
| `BOT_TOKEN` | Bot token from @BotFather |
| `MONGO_DB_URI` | MongoDB connection URI |
| `OWNER_ID` | Your Telegram user ID |
| `LOGGER_ID` | Log group/channel ID (bot must be admin there) |
| `STRING_SESSION` | Pyrogram string session (assistant account) |

### Optional Environment Variables

| Variable | Default | Description |
|---|---|---|
| `BOT_NAME` | `MADARA MUSIC` | Bot display name |
| `OWNER_USERNAME` | - | Your Telegram username |
| `SUPPORT_CHANNEL` | - | Support channel URL |
| `SUPPORT_CHAT` | - | Support chat URL |
| `SPOTIFY_CLIENT_ID` | - | Spotify API client ID |
| `SPOTIFY_CLIENT_SECRET` | - | Spotify API client secret |
| `STRING_SESSION2-7` | - | Extra assistant sessions |

### Running the Bot

1. Fill all required secrets in the Replit Secrets panel
2. Click **Run** (Start MADARA MUSIC Bot workflow)

## User Preferences

- Bot branding: **MADARA MUSIC** (renamed from original STRANGER MUSIC / SHUKLAMUSIC)

<div align="center">

<img src="https://files.catbox.moe/ak96mx.jpg" width="200" height="200" style="border-radius: 50%;" alt="MADARA MUSIC">

# 𝗠𝗔𝗗𝗔𝗥𝗔 𝗠𝗨𝗦𝗜𝗖 🎵

### ⚡ The Most Powerful Telegram Music Bot Ever Built ⚡

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0%2B-orange?style=for-the-badge&logo=telegram&logoColor=white)](https://pyrogram.org)
[![PyTgCalls](https://img.shields.io/badge/PyTgCalls-Latest-red?style=for-the-badge&logo=telegram)](https://pytgcalls.github.io)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ragini19854-prog/new_madara_music?style=for-the-badge&color=yellow)](https://github.com/ragini19854-prog/new_madara_music/stargazers)

<br>

> **🎧 Stream music directly in your Telegram group voice chats**
> **with stunning UI, colored buttons, and premium emoji support.**

<br>

[🚀 Deploy Now](#-deployment) • [✨ Features](#-features) • [⚙️ Config](#%EF%B8%8F-configuration) • [📞 Support](#-support)

---

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎵 Music Streaming
- ▶️ Play from **YouTube**, **Spotify**, **SoundCloud**
- 🍎 **Apple Music** & **Resso** support
- 📁 Direct **Telegram file** playback
- 🔴 **Live stream** support
- 🎶 Audio & Video streaming modes
- 📋 Queue management system

</td>
<td width="50%">

### 🎛️ Playback Controls
- ⏸ Pause / ▶️ Resume
- ⏭ Skip tracks
- ⏹ Stop & clear queue
- 🔁 Loop mode (1 to 999x)
- 🔀 Queue shuffle
- ⚡ Speed control (0.5x → 2.0x)
- ⏩ Seek forward / backward

</td>
</tr>
<tr>
<td width="50%">

### 🎨 Premium UI
- 🌈 **Colored inline buttons** (KuriGram / pyrofork style)
- 💎 **Premium emoji** on every button
- 🖼️ Beautiful **now-playing thumbnails**
- 📊 Live **progress bar** in controls
- 🎴 Auto-generated track cards
- ✨ Message effects & animations

</td>
<td width="50%">

### 🛡️ Admin & Management
- 👥 Multi-assistant support (7 sessions)
- 🔒 Authorization system
- 🚫 Global ban / group ban
- 📢 Tag-all & group management
- 🌐 Multi-language (EN, HI, AR, PA)
- ⚙️ Per-group settings panel

</td>
</tr>
<tr>
<td width="50%">

### 🤖 Extra Tools
- 🌤️ Weather lookup
- 🔗 QR code generator
- 🌐 URL shortener
- 🔤 Font styler & figlet
- 📸 Sticker creator
- 🌍 Translator (50+ languages)

</td>
<td width="50%">

### 📊 Statistics & Monitoring
- ⚡ Real-time ping & uptime
- 💾 RAM / CPU / Disk stats
- 📈 Usage statistics
- 🏆 Top played tracks (Global/Group/Personal)
- 📋 Chat & user counters

</td>
</tr>
</table>

---

## 🚀 Deployment

### 📋 Prerequisites

Before deploying, make sure you have:

| Requirement | How to Get |
|-------------|-----------|
| **Telegram API ID** | [my.telegram.org](https://my.telegram.org) |
| **Telegram API Hash** | [my.telegram.org](https://my.telegram.org) |
| **Bot Token** | [@BotFather](https://t.me/BotFather) |
| **MongoDB URI** | [MongoDB Atlas](https://cloud.mongodb.com) (Free tier works) |
| **String Session** | [@StringFatherBot](https://t.me/StringFatherBot) or run `python3 gen_session.py` |
| **Log Group ID** | Create a Telegram group, add your bot as admin, get the ID |

---

### ▶️ Deploy on Replit (Recommended)

[![Run on Replit](https://replit.com/badge/github/ragini19854-prog/new_madara_music)](https://replit.com/github/ragini19854-prog/new_madara_music)

1. Click the button above
2. Fill in all secrets in the **Secrets** panel
3. Hit **Run** ✅

---

### 🐳 Deploy with Docker

```bash
# Clone the repository
git clone https://github.com/ragini19854-prog/new_madara_music
cd new_madara_music

# Copy and fill the environment file
cp sample.env .env
nano .env

# Build and run
docker-compose up -d
```

---

### 🖥️ Deploy on VPS / Linux Server

```bash
# Update system packages
sudo apt-get update && sudo apt-get upgrade -y

# Install Python 3.10+
sudo apt-get install python3.10 python3-pip ffmpeg git -y

# Clone repository
git clone https://github.com/ragini19854-prog/new_madara_music
cd new_madara_music

# Install dependencies
pip3 install -r requirements.txt

# Configure environment
cp sample.env .env
nano .env   # Fill in your values

# Start the bot
python3 -m MADARAMUSIC
```

---

### ☁️ Deploy on Heroku

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ragini19854-prog/new_madara_music)

---

## ⚙️ Configuration

Copy `sample.env` to `.env` and fill in the values:

```env
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#       🔐 REQUIRED VARIABLES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID=              # From my.telegram.org
API_HASH=            # From my.telegram.org
BOT_TOKEN=           # From @BotFather
MONGO_DB_URI=        # MongoDB connection URI
OWNER_ID=            # Your Telegram User ID
LOGGER_ID=           # Your log group/channel ID
STRING_SESSION=      # Pyrogram string session

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#       ⚙️ OPTIONAL VARIABLES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOT_NAME=MADARA MUSIC          # Bot display name
OWNER_USERNAME=YourUsername    # Your Telegram username
SUPPORT_CHANNEL=               # https://t.me/YourChannel
SUPPORT_CHAT=                  # https://t.me/YourChat

# ── Spotify API (optional but recommended) ──
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=

# ── Extra assistant sessions (optional) ──
STRING_SESSION2=
STRING_SESSION3=
STRING_SESSION4=
STRING_SESSION5=
STRING_SESSION6=
STRING_SESSION7=
```

---

## 📖 Commands

<details>
<summary><b>🎵 Music Commands</b></summary>

| Command | Description |
|---------|-------------|
| `/play [song name / URL]` | Play a song in voice chat |
| `/vplay [song name / URL]` | Play video in voice chat |
| `/pause` | Pause the stream |
| `/resume` | Resume the stream |
| `/skip` | Skip to next track |
| `/stop` | Stop and clear queue |
| `/queue` | Show current queue |
| `/shuffle` | Shuffle the queue |
| `/loop [num/disable]` | Set loop count |
| `/seek [seconds]` | Seek forward |
| `/seekback [seconds]` | Seek backward |
| `/speed` | Open speed control panel |
| `/song [name]` | Download a song |

</details>

<details>
<summary><b>⚙️ Settings & Admin Commands</b></summary>

| Command | Description |
|---------|-------------|
| `/settings` | Open group settings |
| `/auth [user]` | Authorize a user |
| `/unauth [user]` | Remove authorization |
| `/authusers` | List authorized users |
| `/reload` | Refresh admin cache |
| `/reboot` | Reboot bot for this chat |
| `/lang` | Change bot language |

</details>

<details>
<summary><b>🛡️ Owner / Sudo Commands</b></summary>

| Command | Description |
|---------|-------------|
| `/gban [user]` | Global ban a user |
| `/ungban [user]` | Remove global ban |
| `/block [chat]` | Blacklist a chat |
| `/unblock [chat]` | Remove from blacklist |
| `/sudolist` | List sudo users |
| `/stats` | Bot statistics |
| `/broadcast` | Broadcast message |

</details>

<details>
<summary><b>🔧 Utility Commands</b></summary>

| Command | Description |
|---------|-------------|
| `/ping` | Check bot latency |
| `/id` | Get user/chat ID |
| `/tr [lang] [text]` | Translate text |
| `/qr [text]` | Generate QR code |
| `/weather [city]` | Get weather |
| `/font [text]` | Style your text |
| `/sticker` | Create sticker |
| `/zip` / `/unzip` | Archive files |

</details>

---

## 🗂️ Project Structure

```
new_madara_music/
│
├── MADARAMUSIC/                # 🎯 Main bot package
│   ├── core/                   # Core engine
│   │   ├── bot.py              # Pyrogram client (MADARA class)
│   │   ├── call.py             # PyTgCalls voice chat engine
│   │   ├── userbot.py          # Assistant account manager
│   │   └── mongo.py            # MongoDB connection
│   │
│   ├── platforms/              # Platform APIs
│   │   ├── Youtube.py          # YouTube downloader
│   │   ├── Spotify.py          # Spotify resolver
│   │   ├── Soundcloud.py       # SoundCloud support
│   │   ├── Apple.py            # Apple Music support
│   │   ├── Resso.py            # Resso support
│   │   └── Telegram.py         # Telegram file handler
│   │
│   ├── plugins/                # Command handlers
│   │   ├── admins/             # Admin controls
│   │   ├── bot/                # Start, help, settings
│   │   ├── extra/              # Extra features
│   │   ├── misc/               # Miscellaneous
│   │   ├── play/               # Play commands
│   │   └── tools/              # Utility tools
│   │
│   ├── utils/                  # Utilities & helpers
│   │   ├── emojis.py           # 💎 Premium emoji constants
│   │   ├── inline/             # Inline keyboard builders
│   │   ├── database.py         # Database helpers
│   │   ├── thumbnails.py       # Thumbnail generator
│   │   └── formatters.py       # Text formatters
│   │
│   └── mongo/                  # MongoDB collections
│
├── strings/                    # 🌐 Multi-language strings
│   └── langs/
│       ├── en.yml              # 🇺🇸 English
│       ├── hi.yml              # 🇮🇳 Hindi
│       ├── ar.yml              # 🇸🇦 Arabic
│       └── pa.yml              # 🇮🇳 Punjabi
│
├── config.py                   # ⚙️ Configuration loader
├── requirements.txt            # 📦 Python dependencies
└── sample.env                  # 📋 Environment template
```

---

## 🎨 UI Preview

```
╔══════════════════════════════╗
║  🎵  N O W   P L A Y I N G  ║
╠══════════════════════════════╣
║  Track: Shape of You         ║
║  Duration: 3:54              ║
║  Platform: YouTube 🎬        ║
╠══════════════════════════════╣
║  🎵 00:45 ══♫════════ 03:09  ║
╠══════════════════════════════╣
║  [▶️ RESUME]  [⏸ PAUSE]      ║
║  [⏭ SKIP]    [⏹ STOP]       ║
╚══════════════════════════════╝
```

> All buttons are **color-coded** with **premium emoji icons**:
> 🟢 Green = Resume / Enable
> 🔵 Blue = Navigation / Info
> 🔴 Red = Stop / Close / Danger

---

## 🌐 Supported Platforms

<div align="center">

| Platform | Audio | Video | Playlist | Live |
|----------|:-----:|:-----:|:--------:|:----:|
| 🎥 YouTube | ✅ | ✅ | ✅ | ✅ |
| 🎵 Spotify | ✅ | ❌ | ✅ | ❌ |
| ☁️ SoundCloud | ✅ | ❌ | ✅ | ❌ |
| 🍎 Apple Music | ✅ | ❌ | ✅ | ❌ |
| 🎶 Resso | ✅ | ❌ | ❌ | ❌ |
| 📁 Telegram Files | ✅ | ✅ | ❌ | ❌ |

</div>

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Support

<div align="center">

Having issues? Join our community!

[![Support Chat](https://img.shields.io/badge/Support_Chat-Join_Now-blue?style=for-the-badge&logo=telegram)](https://t.me/MadaraMusicChat)
[![Update Channel](https://img.shields.io/badge/Updates-Subscribe-red?style=for-the-badge&logo=telegram)](https://t.me/MadaraMusicUpdates)

</div>

---

## ⭐ Star History

If you find this project useful, please consider giving it a ⭐ star!

[![Star History Chart](https://api.star-history.com/svg?repos=ragini19854-prog/new_madara_music&type=Date)](https://star-history.com/#ragini19854-prog/new_madara_music)

---

## 📜 License

```
MADARA MUSIC - Telegram Music Bot
Based on StrangerMusic by ItzShukla (Educational Use)
Modified and enhanced by the MADARA MUSIC project.

This source code is open for educational and non-commercial use ONLY.
You are required to retain this credit in all copies.
```

---

<div align="center">

**Made with ❤️ by MADARA MUSIC Team**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/ragini19854-prog)

⭐ **Don't forget to star this repo if you like it!** ⭐

</div>

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "hina_music_bot")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", 5)
)  # Remember to give value in Seconds

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", 300)
)  # Remember to give value in Minutes


EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    True,
)

# Fill True if you want to load extra plugins
# Fill here the external plugins repo where plugins that you want to load
EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/toxicraunak/Extra-Plugin",
)

# Your folder name in your extra plugins repo where all plugins stored
EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

LOGGERS = "\x54\x68\x65\x54\x65\x6C\x65\x67\x72\x61\x6D\x52\x6F\x62\x6F\x74"  # connect errors api key "Dont change it"
# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", 1000)
)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", 7029912634).split())
)  # Input type must be interger

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/toxicraunak/meow_music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/haxkx2"
)  # Example:- https://t.me/akaChampu
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/haxkx2_gc"
)  # Example:- https://t.me/TheChampuClub
# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", True)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", 1800)
)  # Remember to give value in Seconds

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorize command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", False)


# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", 3))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", 5))


# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/toxicraunak/meow_music")


# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "a29b0b331adf4c428ce3a73a9b20a306")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "e463dede19b04610ad27dc43eb19b56e")


# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", 999))


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", 500))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))  # Remember to give value in bytes
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496)) # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes


# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", False)


# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @ChampuStringBot
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "musiclogs.txt"
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://graph.org/file/8bd25e1b5fffb97ea343e.jpg",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/18ba535b174ac0649b23b.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://graph.org/file/709fdd164660d5add7b5f.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://graph.org/file/244e7569f41400dd0e024.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://graph.org/file/244e7569f41400dd0e024.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://graph.org/file/8bd25e1b5fffb97ea343e.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://graph.org/file/18ba535b174ac0649b23b.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://graph.org/file/49379e9fe323b923a2dc4.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://telegra.ph/file/9fbc748ad0d552e403ba6.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://graph.org/file/93cf947713f49e9e4f99a.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://graph.org/file/fe28e2fb73cdade0c8a10.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://graph.org/file/709fdd164660d5add7b5f.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://graph.org/file/1a4e7f09f968d9207a291.jpg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )


if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )


if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "https://graph.org/file/18ba535b174ac0649b23b.jpg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "https://graph.org/file/3434af0772e3ed4e4f27c.jpg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://graph.org/file/1bfce7a64228c69e43802.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://graph.org/file/6e59e4dbcb74fec678d10.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://graph.org/file/49379e9fe323b923a2dc4.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://graph.org/file/709fdd164660d5add7b5f.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://graph.org/file/244e7569f41400dd0e024.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://graph.org/file/851a9a173ea0bbe740e4c.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://graph.org/file/8bd25e1b5fffb97ea343e.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7566423124:AAEWm6SMbQdV7W9NywaGNRqYnn6TAYRJnOo")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27322718"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4f6d1b67cf101aea5cf0536885aa1b82")
#Your db channel Id
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@seishiro_log_forbot")
# NAMA OWNER
OWNER = os.environ.get("OWNER", "ADITYA ABHINAV")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6701907262"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://abhinavaditya035:YtKy9wcKcaukIH9q@cluster0.ydyi6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "0")
FORCE_SUB_CHANNEL2 = os.environ.get("FORCE_SUB_CHANNEL2", "0")
FORCE_SUB_CHANNEL3 = os.environ.get("FORCE_SUB_CHANNEL3", "0")
FORCE_SUB_CHANNEL4 = os.environ.get("FORCE_SUB_CHANNEL4", "0")


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "900")) # auto delete in seconds

START_PIC = os.environ.get("START_PIC", "https://wallpapers.com/images/hd/naruto-final-form-1920-x-1200-qmz41z5fd42hgr3y.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://wallpapers.com/images/hd/naruto-final-form-1920-x-1200-qmz41z5fd42hgr3y.jpg")

START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!!! <b>{first}</b>\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "8156773974  6546791787").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ {first}...\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʙᴀᴋᴋᴀᴀᴀ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6701907262)

LOG_FILE_NAME = "bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

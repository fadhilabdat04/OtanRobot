# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open("{}/EmikoRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 25669107  # integer value, dont use ""
    API_HASH = "e30b39cdb86e92f66339e9070a7e1e9b"
    TOKEN = "6031007486:AAFMxypvl32GLsci2OWJwleD1jfvlAPg9Ig"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1345594412  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OPENWEATHERMAP_ID = 22322
    OWNER_USERNAME = "Arabnihnge"
    BOT_USERNAME = "BabuArabRobot"
    SUPPORT_CHAT = "SiArab_Support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001829610428
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001749511943
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOG = -1001511989554

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://cmumeqmp:s_gXyCS_rRIXftIQKoqKRush_NeRvw4d@rosie.db.elephantsql.com/cmumeqmp"  # needed for any database modules
    MONGO_DB_URI = "mongodb+srv://fadhilabdat:fadhil123@cluster0.jtimqg8.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    ARQ_API_URL = "0"
    ARQ_API_KEY = "PBXFMD-NWMWEN-FMFLQP-JBGTTF-ARQ"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "1345594412")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "1345594412")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "1345594412")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "1345594412")
    WOLVES = get_user_list("elevated_users.json", "1345594412")
    DONATION_LINK = "https://www.paypal.me/fadhil406"  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = "siap"
    HEROKU_API_KEY = "YES"
    REM_BG_API_KEY = "yahoo"
    LASTFM_API_KEY = "yeah"
    CF_API_KEY = "jk"
    BL_CHATS = []  # List of groups that you want blacklisted.
    SESSION_STRING = "1BVtsOHABu0iJ8KoYBi9q30mlboZU-v1rHd6F38EyB5Crd56pUmbFRp-TyRYKcNpVvPE5XlW5P9Ggmk55kfGaGPD3Z6MEZfuc0Vd6ntoX9nYCWUvJD2Wsr5BMgEYMHfeuwI2CHNgeUFRfG1Rhg50PrXQPvkzNvN9n8v7qSTJSjDA8wDEBYF5F_x4w5xsUH-isbeP35h3-iG0AkQkODVOzY05Cj1Mz6LmUstHOGNHfH_Kt7Z3bPG4hWxE69sI0pAQjvYL5crAAzRACcO7qMrQLmbutxOOQ4KlxGSykkxj7Le4pbwQFQ6lK4gnqoQisiocfJhM2rMeR1_yE9I1a-gTPKxgIRet8HvU="
    STRING_SESSION = "1BVtsOHABu0iJ8KoYBi9q30mlboZU-v1rHd6F38EyB5Crd56pUmbFRp-TyRYKcNpVvPE5XlW5P9Ggmk55kfGaGPD3Z6MEZfuc0Vd6ntoX9nYCWUvJD2Wsr5BMgEYMHfeuwI2CHNgeUFRfG1Rhg50PrXQPvkzNvN9n8v7qSTJSjDA8wDEBYF5F_x4w5xsUH-isbeP35h3-iG0AkQkODVOzY05Cj1Mz6LmUstHOGNHfH_Kt7Z3bPG4hWxE69sI0pAQjvYL5crAAzRACcO7qMrQLmbutxOOQ4KlxGSykkxj7Le4pbwQFQ6lK4gnqoQisiocfJhM2rMeR1_yE9I1a-gTPKxgIRet8HvU="
    MONGO_PORT = 27017
    MONGO_DB = "Emiko"

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True

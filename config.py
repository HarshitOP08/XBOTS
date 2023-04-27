import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 25018506
API_HASH = "5a6e89f9369c6f22abf80a99df29eaf5"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("6093506337:AAFfvzSpCFmAEP8gQ4LJ1I6ZU7igeoHW6BQ", default=None)
BOT_TOKEN2 = getenv("6285873839:AAGT1N4iY23zLZ2UC2EP2EcAk1z3_DY7jCc", default=None)
BOT_TOKEN3 = getenv("6133633723:AAHjMixz0P-e8HaT6j4-iPfk6YoRQvjg2Nc", default=None)
BOT_TOKEN4 = getenv("5809398548:AAFsr9RxM2IYovlN6S2Y8ypmykBogNj4o_4", default=None)
BOT_TOKEN5 = getenv("6113977873:AAHXfvjweESSYDD2fFE9rZmfZtU4hYUgPTI", default=None)
BOT_TOKEN6 = getenv("6007307263:AAGPbY8egV9UqcbmlyjYnV_6xGlHm_JAodY", default=None)
BOT_TOKEN7 = getenv("5915098399:AAGC6ZmTwcvCPjWPrVv_tp0tFp24I1GbvX4", default=None)
BOT_TOKEN8 = getenv("6193082481:AAHTdTm3l7aWSZYOAasTPP7Q8V76aY4Ow4s", default=None)
BOT_TOKEN9 = getenv("6103237130:AAHBYtPDQ5OE4GZx74rRSk6reb8A2W20Nq0", default=None)
BOT_TOKEN10 = getenv("6111532789:AAFfPIDhBzpw0d2CdL7HsKUX1gVfDLMi-Pw", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("5656982887 6064188188 5340731575", default="5656982887 6064188188 5340731575").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("5340731575", default="5340731575"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

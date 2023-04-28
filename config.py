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

BOT_TOKEN = getenv("5434645359:AAHuE1hQkt--uPIDLdO54dxxnxWunqB8wgE", default=None)
BOT_TOKEN2 = getenv("5900914378:AAFDJj14JBdbgerk9y2taWDGbu8bO2yE9KE", default=None)
BOT_TOKEN3 = getenv("5813154255:AAFqaplPlOSJ2F6X5v7aE7n8s0Hf5_iMsok", default=None)
BOT_TOKEN4 = getenv("5869813860:AAEB1VQGeu62s6t4TlkNj7r_ogczOye3BXM", default=None)
BOT_TOKEN5 = getenv("5828332963:AAFHW29YPdU8s5EBuWS2GmkeKQJkRSa2af8", default=None)
BOT_TOKEN6 = getenv("6062475150:AAFRD52L5eFpAQ9MmZuRFahrAmCIc3qBt04", default=None)
BOT_TOKEN7 = getenv("6207466976:AAH32OUJiCGWVWobnlCKd2BFQdxIsVusycM", default=None)
BOT_TOKEN8 = getenv("6142329825:AAHlLwOaMVnPcfkRoyjrWA7hCeO5xCO-0U0", default=None)
BOT_TOKEN9 = getenv("6060359118:AAHl5ptnWfIGgDpAB9-WwBDD0hFeRDEIIkQ", default=None)
BOT_TOKEN10 = getenv("6020773841:AAF4Fg1x5sXBLvEJm-kJkFarCr12uEaBdik", default=None)

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

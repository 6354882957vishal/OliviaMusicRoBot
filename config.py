from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"26489431))
API_HASH = getenv("API_HASH"9a2fce85339bb79254a55368a61ab92f)

BOT_TOKEN = getenv("BOT_TOKEN",6927939487:AAEDqqWSxxEsvQ5d7dtEQ7TCn3MgYL-SSIk )
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"2108417544))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("SESSION", 1BVtsOGwBu4i6Iq4KX2iYmh_k6RVEVHd8Wh_jXDYBfq2sOx39i5TYn97MPieZMeWBJCsfNIAPR8E13TLL1KwnwMt-9HS35iiWn916CJ_zjvWr2qidzLBLxgR_jofbAqqzSeTm3kUzb9TUkom8oUzZxBkZrtVTYCgnyEziSwET6xPV5JoNbukVvcDfoCwaGSXsNTFwqt2SY7IQr8_FRuglRQGxs91BQwwWJFoQt6pvCgjuloxP8KMyWIJy5-gQMP_RV3vl0T0dai3otShNp__y8NuptVdtaw1qtN_BIxzDQ1s7_cemvfsFynMrtqv_sumaOvlRArwqJew7Svdxi0pYNg4cgke4j1U=)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tbcbotschat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tbc_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5090817443").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

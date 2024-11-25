
import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7416197769:AAGEcM63Uad_IXtRRv-95D4RcTlxc_2U3qw")
    API_ID = int(os.environ.get("API_ID", "20821267"))
    API_HASH = os.environ.get("API_HASH", "8723cdf433be176300044547ee6bab7a")
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Rajahd41:Rajahd41@cluster0.omrv9cu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_USERS = [7224758848, 7513565186, 6804641253, 5427627648]


# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '11450835'))
    API_HASH = str(getenv('API_HASH', '0fadb61feae6ccf016932823bbf1565c'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6611868437:AAFS9g3wZBqTSMdT50EUKez5ehmQ8c-urww'))
    FILE_BOT_TOKEN = str(getenv('FILE_BOT_TOKEN', '6600157823:AAFXUIEJZyNKfDd92v5wfBbNRYFOooMKhrE'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1002025354142'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1254785184").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'therialex_1206'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Alex1206:Alex1206@cluster0.mc96iiw.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
    DB_URI = str(getenv('DB_URI', 'mongodb+srv://Alex1206:Alex1206@cluster0.mc96iiw.mongodb.net/?retryWrites=true&w=majority'))
    DB_NAME = str(getenv("DB_NAME", "filesharebot"))
    SECOND_BOTUSERNAME = str(getenv("SECOND_BOTUSERNAME", "Files_123_bot"))

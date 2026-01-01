#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29115102"))
API_HASH = environ.get("API_HASH", "1a331db2b00e9d2decaa9c7276449eb6")
BOT_TOKEN = environ.get("BOT_TOKEN", "7903742155:AAGLWumrUPxZpl0yakb4oDhfuq74wtWRzdY")
OWNER = int(environ.get("OWNER", "1224092270"))
CREDIT = environ.get("CREDIT", "STRANGER BOYS")
AUTH_USER = os.environ.get('AUTH_USERS', '1224092270').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


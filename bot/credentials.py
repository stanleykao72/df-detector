import os

# bot_token = '1168941932:AAGiYEV79cjssoQX_rZ5IwE4nbFhliKlh5M'
bot_token = os.getenv("bot_token")
# bot_user_name = 'imagedetect_bot'
bot_user_name = os.getenv("bot_user_name")
# telegram_user_id
telegram_user_id = int(os.getenv("telegram_user_id"))
# URL = "https://dfdetector.herokuapp.com/"
URL = os.getenv("URL")
#URL = 'https://1d5cecb69736.ngrok.io'
api_id = 1432612
api_hash = "e744c3ed5106f87db7330f0275f4b769"
from dotenv import load_dotenv
from internet_speed_twitter_bot import InternetSpeedTwitterBot
import os

load_dotenv()
PROMISED_DOWN = 200
PROMISED_UP = 150
TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASSWORD = os.getenv("PASS")
USER = os.getenv("USER")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(email=TWITTER_EMAIL, password=TWITTER_PASSWORD, user=USER, down=PROMISED_DOWN, up=PROMISED_UP)
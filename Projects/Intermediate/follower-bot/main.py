from insta_follower import InstaFollower
from dotenv import load_dotenv
import os

load_dotenv()

TARGET_ACCOUNT = "animes/"
USER = os.getenv("EMAIL")
PASS = os.getenv("PASS")

bot = InstaFollower()
bot.login(email=USER, password=PASS)
bot.find_followers(account=TARGET_ACCOUNT)
bot.follow()
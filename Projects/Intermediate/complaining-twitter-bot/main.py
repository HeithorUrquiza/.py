from dotenv import load_dotenv
import os



load_dotenv()
PROMISED_DOWN = 80
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASSWORD = os.getenv("PASS")
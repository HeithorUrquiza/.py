""" import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
PARAMETERS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": os.getenv("API_KEY")
}

resp = requests.get("https://www.alphavantage.co/query", params=PARAMETERS)
resp.raise_for_status()
data = resp.json()["Time Series (Daily)"]

daily_list = [value for (key, value) in data.items()]
yestday_closing = float(daily_list[0]["4. close"])
bf_yestday_closing = float(daily_list[2]["4. close"])

percent_of_diff = round(((yestday_closing - bf_yestday_closing) / yestday_closing) * 100, 2)

if percent_of_diff > -999999:
    resp = requests.get("https://newsapi.org/v2/top-headlines?q=tesla&apiKey=57ee34fa9d6c4f5e874af88a60eeac8a")
    resp.raise_for_status()
    data = resp.json()

    news = data["articles"][0:3]
    for new in news:
        print(new["title"])
        print(new["description"])
        print("---------------------------") """
        
from entities.mail_service import MailService

app = MailService()
app.send_email()

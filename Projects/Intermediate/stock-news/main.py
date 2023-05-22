import requests
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

if percent_of_diff > 5:
    print(percent_of_diff)
    print("Get news")

import requests
import os
from dotenv import load_dotenv

load_dotenv()

PARAMETERS_STOCK = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": os.getenv("STOCK_API_KEY")
}

PARAMETERS_NEWS = {
    "q": "Tesla",
    "searchIn": "title",
    "apikey": os.getenv("NEWS_API_KEY")
}

class APIRequest:
    
    def __init__(self):
        self.data_stock = None
        self.data_news = None
        self.percent = None
        self.stock_req()
        self.check_percent()
        
        
    def stock_req(self):
        resp = requests.get("https://www.alphavantage.co/query", params=PARAMETERS_STOCK)
        resp.raise_for_status()
        self.data_stock = resp.json()["Time Series (Daily)"]
        
        
    def news_req(self):
        resp = requests.get("https://newsapi.org/v2/everything", params=PARAMETERS_NEWS)
        resp.raise_for_status()
        self.data_news = resp.json()
       
        
    def check_percent(self):
        daily_list = [value for (key, value) in self.data_stock.items()]
        yestday_closing = float(daily_list[0]["4. close"])
        bf_yestday_closing = float(daily_list[1]["4. close"])
        percent_of_diff = round(((yestday_closing - bf_yestday_closing) / yestday_closing) * 100, 2)
        self.percent = percent_of_diff
    
    
    def get_news_details(self):
        self.news_req()
        news = self.data_news["articles"][0:3]
        news_details = [f"Title:: {new['title']}\nDescrip:: {new['description']}" for new in news]
        #news_details = [(new["title"], new["description"]) for new in news]
            
        return news_details
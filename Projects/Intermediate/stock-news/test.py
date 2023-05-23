import requests

resp = requests.get("https://newsapi.org/v2/top-headlines?q=trump&apiKey=57ee34fa9d6c4f5e874af88a60eeac8a")
resp.raise_for_status()
data = resp.json()

news = data["articles"][0:3]

news_details = [(new["title"], new["description"]) for new in news]
print(news_details)
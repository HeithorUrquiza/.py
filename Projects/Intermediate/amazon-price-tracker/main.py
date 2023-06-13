import requests
import os
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
HEADER = {
    "User-Agent": os.getenv("USER_AGENT"),
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

resp = requests.get(url=URL, headers=HEADER)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText()
price_float = float(price.split("$")[1].replace(",","."))
title = soup.find(id="productTitle").getText().strip()

if price_float <= 950.0:
    msg = f"{title} is now for R${price_float}. Enjoy!!"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Amazon Price Alert!!\n\n{msg}\n\n{URL}".encode("utf-8"))
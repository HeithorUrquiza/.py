import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = -16.68
MY_LONG = -49.26
EMAIL = "heithorur@gmail.com"
PASSWORD = os.getenv("EMAIL_PASSWORD")

parameters = {
    "lat": -7.634500,
    "lon": -72.668579,
    "exclude": "current,minutely,daily",
    "appid": os.getenv("OWM_API_KEY")
}

resp = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
resp.raise_for_status()
weather_data = resp.json()
hourly = weather_data["hourly"][:12]

will_rain = False
for hour in hourly:
    weather_id = hour["weather"][0]["id"]
    if int(weather_id) < 600:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, 
                            msg=f"Subject:Rain Alert!!\n\nIt's going rain today! Don't forget your umbrella")
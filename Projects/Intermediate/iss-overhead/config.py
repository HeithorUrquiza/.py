import requests
import smtplib
from datetime import datetime
import time

MY_LAT = -16.406330
MY_LONG = -49.218719
EMAIL = "heithorur@gmail.com"
PASSWORD = "zuafczxqizjirsum"

class ISSAlert:
    
    def __init__(self):
        self.time_now = datetime.now().hour


    def is_overhead(self):
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_lat = float(data["iss_position"]["latitude"])
        iss_lng = float(data["iss_position"]["longitude"])
        
        if (MY_LAT + 5) <= iss_lat <= (MY_LAT - 5) and (MY_LONG + 5) <= iss_lng <= (MY_LONG - 5):
            return True


    def is_night(self):
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        
        if sunset <= self.time_now <= sunrise:
            return True
        
        
    def send_email(self):
        while True:
            if self.is_overhead() and self.is_night():
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:ISS comes!!\n\nIss is overhead, look up!")
                    break
        time.sleep(60)
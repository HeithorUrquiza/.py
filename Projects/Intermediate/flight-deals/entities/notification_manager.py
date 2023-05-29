import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

class NotificationManager:
    
    def send_SMS(self, msg, emails):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject: Flight Deal\n\n{msg}".encode('utf-8'))  
                print("Email sent")   
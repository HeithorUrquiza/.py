import smtplib
import os
from dotenv import load_dotenv
from entities.api_request import APIRequest

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

class MailService:
    
    def __init__(self) -> None:
        self.email = EMAIL
        self.password = PASSWORD
        self.APIreq = APIRequest()
        self.news_list = self.APIreq.get_news_details()
        
        
    def send_email(self):
        if self.APIreq.percent > 5 or self.APIreq.percent < -5:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(from_addr=self.email, to_addrs=self.email, msg=f"Subject:{self.subject()}\n\nHeadline: {self.news_list[0][0]}\n\nBrief: {self.news_list[0][1]}")
                

    def subject(self):
        if self.APIreq.percent > 5:
            return f"TSLA increase {self.APIreq.percent}%"
        elif self.APIreq.percent < -5:
            return f"TSLA decrease {self.APIreq.percent} %"
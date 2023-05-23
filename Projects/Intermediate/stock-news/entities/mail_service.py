import smtplib
import os
from dotenv import load_dotenv
from entities.api_request import APIRequest

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

class MailService:
    
    def __init__(self) -> None:
        self.email = EMAIL
        self.password = PASSWORD
        self.APIreq = APIRequest()
        self.mesages = []
        self.news_list = self.APIreq.get_news_details()
        
        
    def write_msg(self):
        for new in self.news_list:
            new = new.replace("-", "-")
            new = new.replace("’", "'")
            new = new.replace("…", "...")
            self.mesages.append(new)
        
        
    def send_email(self):
        if self.APIreq.percent > 0 or self.APIreq.percent < 0:
            self.write_msg()
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.set_debuglevel
                connection.login(user=self.email, password=self.password)
                connection.sendmail(from_addr=self.email, to_addrs=self.email, msg=f"Subject: {self.subject()}\n\n{self.mesages[0]}\n\n{self.mesages[1]}\n\n{self.mesages[2]}")
                
                
    def subject(self):
        if self.APIreq.percent > 0:
            return f"TESLA increase {self.APIreq.percent}%"
        elif self.APIreq.percent < 0:
            return f"TESLA decrease {abs(self.APIreq.percent)}%"
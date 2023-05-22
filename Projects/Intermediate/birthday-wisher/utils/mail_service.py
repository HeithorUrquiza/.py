import smtplib
import datetime as dt
import os
from utils.file_manager import FilesManager
from dotenv import load_dotenv

load_dotenv()

PLACEHOLDER = "[NAME]"
EMAIL = "heithorur@gmail.com"
PASSWORD = os.getenv("EMAIL_PASSWORD")

class MailService:
    
    def __init__(self):
        self.files_manager = FilesManager()
        self.email = EMAIL
        self.password = PASSWORD
        self.birthdays = self.files_manager.get_birthdays()
        self.message = None
        self.today = (dt.datetime.now().month, dt.datetime.now().day)
        
    
    def write_msg(self, name):
        letter = self.files_manager.random_letter()
        self.message = letter.replace(PLACEHOLDER, name)
        
        
    def send_email(self):
        if self.today in self.birthdays:
            self.write_msg(self.birthdays[self.today]["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(from_addr=self.email, to_addrs=self.birthdays[self.today]["email"], msg=f"Subject:Happy Birthday\n\n{self.message}")
import smtplib
from random import choice
from utils.dates_maneger import DatesManager

PLACEHOLDER = "[NAME]"
EMAIL = "tt4497754@gmail.com"
PASSWORD = "fydxhwwynomqtiny"

class MailService:
    
    def __init__(self):
        self.dates_manager = DatesManager()
        self.email = EMAIL
        self.password = PASSWORD
        self.name = None
        self.to_adress = None
        self.message = None
        self.letters = self.open_letters()
        
        
    def open_letters(self):
        with open("Projects/Intermediate/birthday-wisher/letter_templates/letter_1.txt") as letter_1:
            letter1 = letter_1.read()
        with open("Projects/Intermediate/birthday-wisher/letter_templates/letter_2.txt") as letter_2:
            letter2 = letter_2.read()
        with open("Projects/Intermediate/birthday-wisher/letter_templates/letter_3.txt") as letter_3:
            letter3 = letter_3.read()
        return [letter1, letter2, letter3]
    
    
    def write_msg(self, name):
        letter = choice(self.letters)
        self.message = letter.replace(PLACEHOLDER, name)
        
        
    def send_email(self):
        self.name, self.to_adress = self.dates_manager.compare_dates()
        if self.name is not None and self.email is not None:
            #self.write_msg(self.name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(from_addr=self.email, to_addrs=self.to_adress, msg=f"Subject:Olha eu aqui\n\nDia 17/05/2032 vai ser nosso casamento. Anota ai!!!!!")
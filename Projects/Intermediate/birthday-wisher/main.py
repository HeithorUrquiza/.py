# smtp.gmail.com
# smtp.mail.yahoo.com

import smtplib
import datetime as dt
from random import choice

def read_txt():
    with open("Projects/Intermediate/birthday-wisher/quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        return choice(quotes)
        
def send_email(quote):
    email = "tt4497754@gmail.com"
    password = "fydxhwwynomqtiny"

    if get_weekday() == "Wed":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs="tsvdkavfqifc@yahoo.com", msg=f"Subject:Motivational Quote\n\n{quote}")
    
    
def get_weekday():
    data = dt.datetime.now()
    return data.strftime("%a")

quote = read_txt()
send_email(quote)
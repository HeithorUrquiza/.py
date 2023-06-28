""" def subsc_candidates():
    N = int(input())
    candidates = []

    for _ in range(N):
        nome, A, B, C = input().split()
        total_points = int(A) + int(B) + int(C)
        candidates.append((nome, total_points))
        
    return candidates


def evaluate_candidates(list):
    list.sort(key=lambda x: (-x[1], x[0].title()))

    for candidate in list:
        print(candidate[0])  
    

candidates_list = subsc_candidates()
print("\n")
evaluate_candidates(candidates_list) """

""" # smtp.gmail.com
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
send_email(quote) """
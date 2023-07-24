from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from datetime import datetime as dt
import smtplib
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "any-secret-key-test"
EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')
year = dt.now().strftime('%Y')


@app.route("/")
def home():
    return render_template('index.html', now=year)


@app.route("/message", methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    msg = request.form.get('message')
    
    if msg:
        text = f"Name: {name}\nEmail: {email}\n\n\n{msg}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASS)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Interested Recruiter!!\n\n{text}")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
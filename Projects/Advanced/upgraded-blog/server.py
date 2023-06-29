from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import smtplib
import os

resp = requests.get("https://api.npoint.io/1d971e35e2f35f98af72")
data = resp.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods={"GET", "POST"})
def contact_page():
    if request.method == "POST":
        send_email()
        return render_template("contact.html", msg=True)
    return render_template("contact.html", msg=False)


@app.route("/post/<int:index>")
def post(index):
    for post in data:
        if post["id"] == index:
            returned_post = post
    return render_template('post.html', post=returned_post)


def send_email():
    load_dotenv()
    msg = f"Name: {request.form['name']}\n"\
            f"Email: {request.form['email']}\n"\
            f"Phone: {request.form['phone']}\n"\
            f"Message: {request.form['message']}"
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("EMAIL"), password=os.getenv("PASS"))
        connection.sendmail(from_addr=os.getenv("EMAIL"), to_addrs=os.getenv("EMAIL"), msg=f"Subject:New Message 🚨!!\n\n{msg}".encode("utf-8"))


if __name__ == "__main__":
    app.run(debug=1)
from flask import Flask, render_template
import requests

resp = requests.get("https://api.npoint.io/1d971e35e2f35f98af72")
data = resp.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post(index):
    for post in data:
        if post["id"] == index:
            returned_post = post
    return render_template('post.html', post=returned_post)


if __name__ == "__main__":
    app.run(debug=1)
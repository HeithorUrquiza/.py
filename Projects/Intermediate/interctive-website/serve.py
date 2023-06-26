from flask import Flask, render_template
from datetime import datetime as dt
import requests
from post import Post

resp = requests.get("https://api.npoint.io/77679770798065188331")
all_posts = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in resp.json()]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    for post in all_posts:
        if post.id == blog_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=1)
    
    
    
    
""" def api_request(name):
    params = {"name": name}
    resp = requests.get("https://api.agify.io", params=params)
    age = resp.json()["age"]
    
    resp = requests.get("https://api.genderize.io", params=params)
    gender = resp.json()["gender"]
    
    return age, gender
 """

""" @app.route("/posts")
def guess():
    resp = requests.get("https://api.npoint.io/77679770798065188331")
    all_posts = resp.json()
    return render_template("index.html", posts=all_posts) """